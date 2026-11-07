"""Serwer MCP dla superbet.pl.

Odczyt (kursy) działa publicznie. Notatki i analizy są zapisywane lokalnie w
analizy/superbet/ (Superbet nie udostępnia API komentarzy). Stawianie zakładów jest
domyślnie wyłączone i wymaga: SUPERBET_ENABLE_BETTING=1, ticketu z weryfikacją kursu
oraz jawnego confirm=true.
"""
import json
import os
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import client

mcp = FastMCP("superbet")

ROOT = Path(os.environ.get("SUPERBET_DATA_DIR", Path(__file__).resolve().parents[3] / "analizy" / "superbet"))
TICKETS = ROOT / "tickets.json"
TICKET_TTL = 300  # s
MAX_STAKE = float(os.environ.get("SUPERBET_MAX_STAKE", "20"))  # PLN na kupon
PRICE_TOLERANCE = 0.0  # kurs musi być taki sam jak w tickecie lub wyższy


def _brief(e: dict) -> dict:
    return {
        "event_id": e["eventId"],
        "mecz": e.get("matchName"),
        "start_utc": e.get("utcDate"),
        "sport_id": e.get("sportId"),
        "tournament_id": e.get("tournamentId"),
        "betradar_id": e.get("betradarId"),
        "liczba_rynkow": e.get("marketCount"),
    }


@mcp.tool()
def superbet_events(date_from: str, date_to: str | None = None, query: str | None = None,
                    sport_id: int | None = None, limit: int = 50) -> list[dict]:
    """Lista wydarzeń prematch. Daty 'YYYY-MM-DD' (UTC); date_to domyślnie dzień po date_from.
    query filtruje po nazwie meczu, sport_id po ID sportu Superbet."""
    start = datetime.strptime(date_from, "%Y-%m-%d")
    end = datetime.strptime(date_to, "%Y-%m-%d") if date_to else start + timedelta(days=1)
    evs = client.events_by_date(start.strftime("%Y-%m-%d 00:00:00"), end.strftime("%Y-%m-%d 00:00:00"))
    if sport_id is not None:
        evs = [e for e in evs if e.get("sportId") == sport_id]
    if query:
        q = query.lower()
        evs = [e for e in evs if q in (e.get("matchName") or "").lower()]
    return [_brief(e) for e in evs[:limit]]


@mcp.tool()
def superbet_event_odds(event_id: int, market: str | None = None, max_markets: int = 40) -> dict:
    """Kursy dla wydarzenia, pogrupowane po rynkach. market filtruje po nazwie rynku (fragment,
    np. 'Gole', 'Handicap'). Każdy kurs ma odd_uuid potrzebny do kuponu."""
    e = client.event(event_id)
    if not e:
        raise ValueError(f"Brak wydarzenia {event_id}")
    markets: dict[str, list] = {}
    for o in e.get("odds", []):
        if o.get("status") != "active":
            continue
        name = o.get("marketName", "?")
        if market and market.lower() not in name.lower():
            continue
        markets.setdefault(name, []).append({
            "odd_uuid": o["uuid"], "wybor": o.get("name"), "opis": o.get("info"),
            "kurs": o.get("price"), "linia": o.get("specialBetValue"),
        })
    names = list(markets)[:max_markets]
    return {**_brief(e), "rynki": {n: markets[n] for n in names}, "pominieto_rynkow": len(markets) - len(names)}


@mcp.tool()
def superbet_add_note(event_id: int, text: str, kind: str = "comment", title: str | None = None,
                      match_name: str | None = None) -> dict:
    """Dodaje komentarz (kind='comment') lub analizę (kind='analysis') do meczu. Zapis lokalny:
    analizy/superbet/<event_id>.md. Nie wysyła niczego do Superbet."""
    if kind not in ("comment", "analysis"):
        raise ValueError("kind musi być 'comment' lub 'analysis'")
    ROOT.mkdir(parents=True, exist_ok=True)
    path = ROOT / f"{event_id}.md"
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    if not path.exists():
        path.write_text(f"# Superbet event {event_id}" + (f" - {match_name}" if match_name else "") + "\n\n")
    label = "Analiza" if kind == "analysis" else "Komentarz"
    with path.open("a") as f:
        f.write(f"## {label}{': ' + title if title else ''} ({ts})\n\n{text.strip()}\n\n")
    return {"zapisano": str(path), "kind": kind}


@mcp.tool()
def superbet_get_notes(event_id: int) -> str:
    """Zwraca wszystkie komentarze i analizy zapisane dla meczu."""
    path = ROOT / f"{event_id}.md"
    return path.read_text() if path.exists() else "Brak notatek dla tego wydarzenia."


def _load_tickets() -> dict:
    return json.loads(TICKETS.read_text()) if TICKETS.exists() else {}


def _save_tickets(t: dict) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    TICKETS.write_text(json.dumps(t, ensure_ascii=False, indent=1))


def _price_now(event_id: int, odd_uuid: str) -> dict | None:
    e = client.event(event_id)
    for o in (e or {}).get("odds", []):
        if o["uuid"] == odd_uuid and o.get("status") == "active":
            return {"kurs": o["price"], "opis": o.get("info"), "rynek": o.get("marketName"), "mecz": e.get("matchName")}
    return None


@mcp.tool()
def superbet_prepare_slip(selections: list[dict], stake: float) -> dict:
    """Buduje kupon (ticket) BEZ stawiania pieniędzy. selections: [{"event_id": int, "odd_uuid": str}].
    Sprawdza aktualne kursy i liczy kurs łączny oraz wygraną. Ticket ważny 5 min.
    Jeden kupon nie może mieć dwóch nóg z tego samego wydarzenia."""
    if not selections:
        raise ValueError("Pusta lista selections")
    if stake <= 0 or stake > MAX_STAKE:
        raise ValueError(f"Stawka musi być w (0, {MAX_STAKE}] PLN (SUPERBET_MAX_STAKE)")
    if len({s["event_id"] for s in selections}) != len(selections):
        raise ValueError("Dwie nogi z tego samego wydarzenia - niedozwolone")
    legs, total = [], 1.0
    for s in selections:
        p = _price_now(s["event_id"], s["odd_uuid"])
        if not p:
            raise ValueError(f"Kurs niedostępny lub zawieszony: {s}")
        legs.append({**s, **p})
        total *= p["kurs"]
    tid = uuid.uuid4().hex[:10]
    t = _load_tickets()
    t[tid] = {"legs": legs, "stake": stake, "total_odds": round(total, 3), "created": time.time(), "placed": False}
    _save_tickets(t)
    return {"ticket_id": tid, "nogi": legs, "kurs_laczny": round(total, 3), "stawka": stake,
            "mozliwa_wygrana": round(stake * total, 2), "wazny_s": TICKET_TTL,
            "uwaga": "Nic nie postawiono. Aby postawić: superbet_place_bet(ticket_id, confirm=true)."}


@mcp.tool()
def superbet_place_bet(ticket_id: str, confirm: bool = False) -> dict:
    """Stawia kupon z ticketu (PRAWDZIWE PIENIĄDZE). Wymaga: SUPERBET_ENABLE_BETTING=1, confirm=true,
    ticketu młodszego niż 5 min i niezmienionych (lub wyższych) kursów. Żądanie idzie na
    SUPERBET_PLACE_URL z nagłówkiem Authorization z SUPERBET_AUTH_TOKEN."""
    if os.environ.get("SUPERBET_ENABLE_BETTING") != "1":
        return {"postawiono": False, "powod": "Stawianie wyłączone (ustaw SUPERBET_ENABLE_BETTING=1)."}
    if not confirm:
        return {"postawiono": False, "powod": "Brak confirm=true. Pokaż użytkownikowi kupon i uzyskaj jego zgodę."}
    tickets = _load_tickets()
    t = tickets.get(ticket_id)
    if not t:
        raise ValueError("Nieznany ticket")
    if t["placed"]:
        return {"postawiono": False, "powod": "Ticket już użyty."}
    if time.time() - t["created"] > TICKET_TTL:
        return {"postawiono": False, "powod": "Ticket wygasł - przygotuj kupon ponownie."}
    for leg in t["legs"]:
        p = _price_now(leg["event_id"], leg["odd_uuid"])
        if not p or p["kurs"] < leg["kurs"] - PRICE_TOLERANCE:
            return {"postawiono": False, "powod": f"Kurs zmienił się/zawieszony: {leg['mecz']} ({leg['kurs']} -> {p and p['kurs']})"}
    url, token = os.environ.get("SUPERBET_PLACE_URL"), os.environ.get("SUPERBET_AUTH_TOKEN")
    if not url or not token:
        return {"postawiono": False, "powod": "Brak SUPERBET_PLACE_URL / SUPERBET_AUTH_TOKEN - endpoint zakładów trzeba "
                "najpierw ustalić z zalogowanej sesji (DevTools -> Network przy stawianiu kuponu)."}
    import httpx
    payload = {"stake": t["stake"], "selections": [{"eventId": l["event_id"], "oddUuid": l["odd_uuid"], "price": l["kurs"]} for l in t["legs"]]}
    r = httpx.post(url, json=payload, headers={"Authorization": token, **client.HEADERS}, timeout=25)
    ok = r.status_code < 300
    if ok:
        t["placed"] = True
        _save_tickets(tickets)
    return {"postawiono": ok, "http": r.status_code, "odpowiedz": r.text[:500]}
