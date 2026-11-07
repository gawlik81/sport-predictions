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
