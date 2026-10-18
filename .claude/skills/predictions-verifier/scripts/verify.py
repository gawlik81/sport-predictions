#!/usr/bin/env python3
"""Rozliczenie typów i kuponów: trafienia vs oczekiwane, Brier, hipotetyczny zysk.

Użycie: python scripts/verify.py plik.json [--md]

Plik JSON:
{
  "legs": [
    {"id": "A", "opis": "Bournemouth wygra", "p": 0.804, "kurs": 1.193,
     "wynik": 1, "grupa": "piłka 1X2"}      # wynik: 1 trafiony, 0 nietrafiony, null/pominięty = nierozliczony lub zwrot
  ],
  "kupony": [
    {"nazwa": "Kupon 1", "nogi": ["A", "B"]}
  ],
  "top": ["A", "B"]                          # opcjonalnie: id nóg z rankingu TOP-N
}
`kurs` może być 0/null (nieznany) - noga wchodzi do bilansu trafień, ale nie do zysku.
Skrypt tylko liczy; interpretację (wariancja vs błąd procesu) robi skill.
"""
import json
import math
import sys


def fmt(x, nd=2):
    return f"{x:.{nd}f}".replace(".", ",")


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


def summarize(legs, label):
    settled = [l for l in legs if l.get("wynik") in (0, 1)]
    if not settled:
        return f"{label}: brak rozliczonych nóg"
    n = len(settled)
    hit = sum(l["wynik"] for l in settled)
    exp = sum(l["p"] for l in settled)
    var = sum(l["p"] * (1 - l["p"]) for l in settled)
    z = (hit - exp) / math.sqrt(var) if var > 0 else 0.0
    brier = sum((l["p"] - l["wynik"]) ** 2 for l in settled) / n
    return (f"{label}: {hit}/{n} trafionych, oczekiwane {fmt(exp)}, "
            f"różnica {fmt(hit - exp)} ({fmt(z)} odch. std.), Brier {fmt(brier, 3)}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    legs = data["legs"]
    by_id = {l["id"]: l for l in legs}
    for l in legs:
        if not 0 < l["p"] < 1:
            sys.exit(f"Noga {l['id']}: p musi być w (0,1), jest {l['p']}")

    print("## Nogi")
    print(summarize(legs, "Wszystkie"))
    if data.get("top"):
        print(summarize([by_id[i] for i in data["top"]], "TOP-N"))
    groups = {}
    for l in legs:
        groups.setdefault(l.get("grupa", "bez grupy"), []).append(l)
    if len(groups) > 1:
        print("\n## Grupy (rynek / dyscyplina)")
        for g, ls in sorted(groups.items()):
            print("- " + summarize(ls, g))

    print("\n## Pasma p")
    for lo, hi in [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 1.01)]:
        ls = [l for l in legs if lo <= l["p"] < hi]
        if ls:
            print("- " + summarize(ls, f"p {int(lo * 100)}-{min(int(hi * 100), 100)}%"))

    if data.get("kupony"):
        print("\n## Kupony")
        tot_hit = tot_exp = tot_pnl = 0.0
        settled_k = 0
        for k in data["kupony"]:
            ls = [by_id[i] for i in k["nogi"]]
            pk = math.prod(l["p"] for l in ls)
            results = [l.get("wynik") for l in ls]
            if any(r is None for r in results):
                print(f"- {k['nazwa']}: nierozliczony (brak wyniku nogi), p {pct(pk)}")
                continue
            won = all(r == 1 for r in results)
            kurs_known = all(l.get("kurs") for l in ls)
            kurs = math.prod(l["kurs"] for l in ls) if kurs_known else None
            pnl = (kurs - 1 if won else -1) if kurs_known else None
            miss = [l["opis"] for l in ls if l["wynik"] == 0]
            print(f"- {k['nazwa']}: {'TRAFIONY' if won else 'NIETRAFIONY'}"
                  f" | p {pct(pk)} | kurs {fmt(kurs) if kurs else '?'}"
                  f" | EV {pct(pk * kurs - 1) if kurs else '?'}"
                  + (f" | pudła: {', '.join(miss)}" if miss else ""))
            settled_k += 1
            tot_hit += won
            tot_exp += pk
            if pnl is not None:
                tot_pnl += pnl
        if settled_k:
            print(f"Razem: {int(tot_hit)}/{settled_k} kuponów, oczekiwane {fmt(tot_exp)}; "
                  f"zysk hipotetyczny przy stawce 1 na kupon: {fmt(tot_pnl)} "
                  f"(informacyjnie - dokumenty zwykle zalecają stawkę 0%, to nie dowód przewagi)")

    unsettled = [l["opis"] for l in legs if l.get("wynik") not in (0, 1)]
    if unsettled:
        print("\n## Nierozliczone / zwroty: " + "; ".join(unsettled))


if __name__ == "__main__":
    main()
