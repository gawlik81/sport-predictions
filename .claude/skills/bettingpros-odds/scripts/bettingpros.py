#!/usr/bin/env python3
"""Klient BettingPros Consumer API v3 (tylko stdlib). Klucz z env BETTINGPROS_API_KEY lub --key.

Użycie (z katalogu skilla):
  bettingpros.py events --sport NBA --date 2026-10-24
  bettingpros.py markets --sport NBA [--market_category game-odds]
  bettingpros.py counts --sport NBA --event_id 123
  bettingpros.py offers --sport NBA --event_id 123 --market_id 1 [--book_id 10:12] [--best_lines true]
  bettingpros.py props --sport NBA --date 2026-10-24 [--sort expected_value] [--limit 20]
  bettingpros.py books [--location NY]
  bettingpros.py odds 1.91 2.00         (kurs dziesiętny/amerykański -> p, fair, de-vig dla 2 stron)

Każdy parametr API podaje się jako --nazwa wartość (wielokrotne wartości po dwukropku: NBA:NHL).
Flagi: --all-pages (pobierz wszystkie strony, ostrożnie z limitem dziennym), --out plik.json.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.bettingpros.com/v3"
ENDPOINTS = {"events": "/events", "markets": "/markets", "counts": "/markets/offer-counts",
             "offers": "/offers", "props": "/props", "books": "/books"}
NEED_KEY_MSG = ("BRAK KLUCZA API. Poproś użytkownika o klucz BettingPros (x-api-key) i ustaw go: "
                "export BETTINGPROS_API_KEY=... (albo --key). Nie zapisuj klucza w repozytorium.")


def call(path, params, key):
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"x-api-key": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        hints = {403: "klucz brakujący/nieznany/dezaktywowany", 429: "limit dzienny (reset 00:00 UTC) lub zbyt szybko",
                 503: "tablica się buduje - ponów po Retry-After"}
        sys.exit(f"HTTP {e.code} ({hints.get(e.code, 'błąd')}): {body}")


def to_decimal(x):
    x = float(x)
    if abs(x) >= 100:  # amerykański
        return 1 + x / 100 if x > 0 else 1 + 100 / -x
    return x


def odds_cmd(vals):
    dec = [to_decimal(v) for v in vals]
    imp = [1 / d for d in dec]
    print(f"{'wejście':>8} {'dziesiętny':>10} {'p implik.':>10}")
    for v, d, p in zip(vals, dec, imp):
        print(f"{v:>8} {d:10.3f} {p * 100:9.1f}%")
    if len(dec) >= 2:
        s = sum(imp)
        print(f"marża: {(s - 1) * 100:.1f}%  | p bez marży: " + ", ".join(f"{p / s * 100:.1f}%" for p in imp)
              + "  | fair: " + ", ".join(f"{s / p:.2f}" for p in imp))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "odds":
        return odds_cmd(rest)
    if cmd not in ENDPOINTS:
        sys.exit(f"Nieznana komenda {cmd}. Dostępne: {', '.join(ENDPOINTS)}, odds")
    params, key, out, all_pages = {}, os.environ.get("BETTINGPROS_API_KEY", ""), None, False
    i = 0
    while i < len(rest):
        a = rest[i]
        if a == "--all-pages":
            all_pages = True
            i += 1
            continue
        if not a.startswith("--") or i + 1 >= len(rest):
            sys.exit(f"Zły argument: {a}")
        name, val = a[2:], rest[i + 1]
        if name == "key":
            key = val
        elif name == "out":
            out = val
        else:
            params[name] = val
        i += 2
    if not key:
        sys.exit(NEED_KEY_MSG)

    data = call(ENDPOINTS[cmd], params, key)
    pag = data.get("_pagination")
    if all_pages and pag:
        arr = pag["paginated_array"]
        page = pag["page"]
        while page < pag["total_pages"]:
            page += 1
            nxt = call(ENDPOINTS[cmd], {**params, "page": page}, key)
            data[arr].extend(nxt.get(arr, []))
    text = json.dumps(data, ensure_ascii=False, indent=1)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"zapisano {out} ({len(text)} znaków); klucze: {list(data)}")
    else:
        print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
