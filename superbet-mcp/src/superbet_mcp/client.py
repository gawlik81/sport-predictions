"""Klient publicznego API ofertowego Superbet (tylko odczyt, bez logowania)."""
import os
import httpx

BASE = os.environ.get(
    "SUPERBET_OFFER_BASE",
    "https://production-superbet-offer-pl.freetls.fastly.net/v2/pl-PL",
)
HEADERS = {"User-Agent": "Mozilla/5.0 (sport-predictions superbet-mcp)", "Accept": "application/json"}


def _get(path: str, params: dict | None = None) -> dict:
    r = httpx.get(f"{BASE}/{path}", params=params, headers=HEADERS, timeout=25)
    r.raise_for_status()
    body = r.json()
    if body.get("error"):
        raise RuntimeError(f"Superbet zwrócił błąd: {body}")
    return body


def events_by_date(start: str, end: str, offer_type: str = "prematch") -> list[dict]:
    """start/end w formacie 'YYYY-MM-DD HH:MM:SS' (UTC)."""
    return _get("events/by-date", {"offerType": offer_type, "startDate": start, "endDate": end})["data"]


def event(event_id: int) -> dict | None:
    data = _get(f"events/{event_id}")["data"]
    return data[0] if data else None


# --- statystyki, składy, H2H: publiczne API Superbet/Scorealarm (to samo, z którego korzysta strona) ---
STATS_BASE = os.environ.get("SUPERBET_STATS_BASE", "https://scorealarm-stats.freetls.fastly.net/v2")


def _stats_get(sport: str, path: str, params: dict) -> dict | None:
    r = httpx.get(f"{STATS_BASE}/{sport}/{path}/plsuperbetsport/pl-PL", params=params, headers=HEADERS, timeout=25)
    if r.status_code == 204 or not r.content:
        return None  # brak danych dla tego wydarzenia/sportu
    r.raise_for_status()
    return r.json()


def _fx(event_id: int) -> str:
    return f"ax:match:{event_id}"


def overview(event_id: int, sport: str = "soccer") -> dict | None:
    return _stats_get(sport, "fixtures/overview", {"fixture-id": _fx(event_id)})


def lineups(event_id: int, sport: str = "soccer") -> dict | None:
    return _stats_get(sport, "fixtures/lineups", {"fixture-id": _fx(event_id)})


def missing_players(event_id: int, sport: str = "soccer") -> dict | None:
    return _stats_get(sport, "fixtures/missing-players", {"fixture-id": _fx(event_id)})


def h2h(team1_id: str, team2_id: str, sport: str = "soccer") -> dict | None:
    return _stats_get(sport, "fixtures/h2h", {"team1-id": team1_id, "team2-id": team2_id})
