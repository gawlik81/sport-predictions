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


# ---------------------------------------------------------------------------
# Statystyki, składy, nieobecni, H2H (publiczne API Superbet/Scorealarm; sprawdzone dla piłki nożnej)
# ---------------------------------------------------------------------------

STAT_PL = {
    "goals_scored_per_game": "gole strzelone / mecz", "goals_conceded_per_game": "gole stracone / mecz",
    "average_xg": "xG / mecz", "average_shots_on_target": "strzały celne / mecz",
    "average_shots_off_target": "strzały niecelne / mecz", "average_corners": "rożne / mecz",
    "average_yellow_cards": "żółte kartki / mecz", "average_red_cards": "czerwone kartki / mecz",
    "average_cards": "kartki łącznie / mecz",
}
SEASON_PL = {
    "goals": "gole", "shots": "strzały", "shots_on_target": "strzały celne", "corners": "rożne",
    "yellow_cards": "żółte kartki", "red_cards": "czerwone kartki", "fouls": "faule", "xg": "xG",
    "ball_possession": "posiadanie piłki", "clean_sheets": "czyste konta", "offsides": "spalone",
    "big_chances_created": "stworzone dogodne sytuacje", "goalkeeper_saves": "obrony bramkarza",
    "tackles": "odbiory", "interceptions": "przechwyty",
}


def _name(o: dict | None) -> str | None:
    """Pełne imię i nazwisko / nazwa z listy names (type 1), z fallbackiem na pole name."""
    if not o:
        return None
    for n in o.get("names") or []:
        if n.get("type") == 1:
            return (n.get("value") or {}).get("string_value")
    return o.get("name")


def _ts(t: dict | None) -> str | None:
    return datetime.fromtimestamp(t["seconds"], tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if t and t.get("seconds") else None


REASON_PL = {"unknown_injury": "kontuzja (powód nieznany)", "injury": "kontuzja", "default_suspension": "zawieszenie",
             "suspension": "zawieszenie", "illness": "choroba", "doubtful": "wątpliwy", "national_team": "kadra narodowa"}


def _reason(m: dict) -> str | None:
    raw = ((m.get("type") or {}).get("args") or [None])[0]
    key = (raw or "").split(".")[-1]
    return REASON_PL.get(key, key or None)


def _need(data, event_id: int, what: str):
    if data is None:
        raise ValueError(f"Brak danych ({what}) dla wydarzenia {event_id}: to wydarzenie nie jest objęte statystykami "
                         "(inny sport niż piłka nożna, mecz juniorski/wirtualny albo zbyt wcześnie).")
    return data


def _squad(players: list) -> list:
    return [{"nr": (p.get("shirt_number") or {}).get("value"), "zawodnik": _name(p), "pozycja_kod": p.get("position"),
             "kapitan": bool(p.get("captain"))} for p in players or []]


@mcp.tool()
def superbet_lineups(event_id: int, sport: str = "soccer") -> dict:
    """Składy meczu. Zwraca status: 'oficjalny' (skład podany przez klub, zwykle ok. 60-75 min przed startem),
    'przewidywany' (typowany jedenasty skład) lub 'brak'. W odpowiedzi: ustawienie, XI, rezerwowi, trenerzy.
    sport: 'soccer' (sprawdzone); inne sporty mogą nie być obsługiwane."""
    lu = _need(client.lineups(event_id, sport), event_id, "składy")
    out = {"event_id": event_id}
    for side, label in (("team1", "gospodarze"), ("team2", "goście")):
        official = lu.get(f"{side}_lineup") or []
        possible = lu.get(f"{side}_possible_lineup") or []
        status = "oficjalny" if official else ("przewidywany" if possible else "brak")
        xi = official or possible
        out[label] = {
            "druzyna": _name(lu.get(side)), "status_skladu": status,
            "ustawienie": ((lu.get(f"{side}_formation") if official else lu.get(f"{side}_possible_formation")) or {}).get("value"),
            "trener": _name(lu.get(f"{side}_manager")), "xi": _squad(xi),
            "rezerwowi": _squad(lu.get(f"{side}_substitutions")),
        }
    out["uwaga"] = "Skład 'przewidywany' to typ serwisu, nie informacja klubu; do kuponu traktuj jako niepotwierdzony."
    return out


@mcp.tool()
def superbet_missing_players(event_id: int, sport: str = "soccer") -> dict:
    """Nieobecni (kontuzje, zawieszenia) obu drużyn: zawodnik, powód, od/do kiedy (jeśli znane)."""
    mp = _need(client.missing_players(event_id, sport), event_id, "nieobecni")
    out = {"event_id": event_id}
    for side, label in (("team1_missing_players", "gospodarze"), ("team2_missing_players", "goście")):
        block = mp.get(side) or {}
        out[label] = {"druzyna": _name(block.get("team")), "nieobecni": [
            {"zawodnik": _name(m.get("player")), "nr": (m.get("shirt_number") or {}).get("value"),
             "powod": _reason(m), "od": _ts(m.get("missing_since")),
             "do": _ts(m.get("missing_until")), "zrodlo": (m.get("source") or {}).get("value")}
            for m in block.get("missing_players") or []]}
    out["uwaga"] = "Powód bywa ogólny ('unknown_injury'); brak wpisu nie gwarantuje, że zawodnik zagra."
    return out


@mcp.tool()
def superbet_stats(event_id: int, sport: str = "soccer", season_details: bool = False) -> dict:
    """Statystyki przedmeczowe: średnie drużyn (gole, xG, strzały, rożne, kartki), sędzia i obsada, stadion,
    trenerzy, rozgrywki. season_details=true dodaje szczegółowe statystyki sezonu (sumy i średnie)."""
    ov = _need(client.overview(event_id, sport), event_id, "statystyki")
    t1, t2 = _name(ov.get("team1")), _name(ov.get("team2"))
    out = {
        "event_id": event_id, "mecz": f"{t1} - {t2}", "start": _ts(ov.get("match_date")),
        "rozgrywki": (ov.get("season") or {}).get("name"), "stadion": (ov.get("venue") or {}).get("name"),
        "trenerzy": {"gospodarze": _name(ov.get("team1_manager")), "goście": _name(ov.get("team2_manager"))},
        "sedziowie": [{"rola": {1: "główny", 2: "asystent", 3: "asystent", 4: "techniczny", 5: "VAR"}.get(r.get("type"), r.get("type")),
                       "nazwisko": r.get("name")} for r in ov.get("referees") or []],
        "srednie_przedmeczowe": {},
    }
    for st in ov.get("prematch_stats") or []:
        key = (st["text"].get("args") or [""])[0].split(".")[-1]
        out["srednie_przedmeczowe"][STAT_PL.get(key, key)] = {"gospodarze": st.get("team1"), "goście": st.get("team2")}
    if season_details:
        det = {}
        for st in ov.get("prematch_season_stats") or []:
            key = (st["text"].get("args") or [""])[0].split(".")[-1]
            kind = "suma" if st.get("aggregate_type") == 1 else "srednia"
            det.setdefault(SEASON_PL.get(key, key), {})[kind] = {"gospodarze": st.get("team1"), "goście": st.get("team2")}
        out["sezon"] = det
    out["uwaga"] = ("Średnie dotyczą bieżącego sezonu rozgrywek; sędzia bywa znany dopiero 1-3 dni przed meczem. "
                    "To dane serwisu, nie własny model: nie zastępują analizy.")
    return out


@mcp.tool()
def superbet_h2h(event_id: int, last: int = 5, sport: str = "soccer") -> dict:
    """Bezpośrednie spotkania (H2H) oraz forma obu drużyn: ostatnie wyniki z datą i wynikiem końcowym.
    last = ile ostatnich meczów w każdej sekcji (1-10)."""
    ov = _need(client.overview(event_id, sport), event_id, "H2H")
    ids = (ov.get("team1") or {}).get("id"), (ov.get("team2") or {}).get("id")
    if not all(ids):
        raise ValueError("Brak identyfikatorów drużyn w odpowiedzi serwisu.")
    h = _need(client.h2h(ids[0], ids[1], sport), event_id, "H2H")
    last = max(1, min(last, 10))

    def ev(e):
        score = next((s for s in e.get("scores") or [] if s.get("type") == 0), None)
        return {"data": _ts(e.get("match_date")), "mecz": f"{_name(e.get('team1'))} - {_name(e.get('team2'))}",
                "wynik": f"{score['team1']}:{score['team2']}" if score else None,
                "czerwone_kartki": (e.get("red_cards_count") or {}).get("value")}

    done = lambda lst: [x for x in lst or [] if x.get("match_status") == 100]
    st = h.get("h2h_statistics") or {}
    return {
        "event_id": event_id, "mecz": f"{_name(ov.get('team1'))} - {_name(ov.get('team2'))}",
        "bilans_h2h_od": h.get("h2h_year_since"),
        "bilans": {"wygrane_gospodarzy": st.get("team1"), "remisy": st.get("draw"), "wygrane_gosci": st.get("team2")},
        "ostatnie_h2h": [ev(e) for e in done(h.get("h2h_events"))[:last]],
        "forma_gospodarzy": [ev(e) for e in done(h.get("team1_events"))[:last]],
        "forma_gosci": [ev(e) for e in done(h.get("team2_events"))[:last]],
        "uwaga": "Bilans obejmuje całą historię (stare mecze ważą mało); sekcje 'ostatnie' są liczone od najnowszych.",
    }


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
