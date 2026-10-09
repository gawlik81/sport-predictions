#!/usr/bin/env python3
"""Rynki liczbowe w piłce (rożne, kartki, faule, strzały, rynki zawodnika): Over/Under z rozkładu
Poissona lub ujemnego dwumianowego (nadmierna wariancja).

Użycie:
  markets.py <rynek> <średnia> [linia ...] [--vmr X]
  markets.py corners 10.4 8.5 9.5 10.5 11.5
  markets.py cards 4.6 3.5 4.5 5.5
  markets.py player_fouls 1.8 0.5 1.5 2.5

<średnia> to oczekiwana liczba zdarzeń (suma obu drużyn dla rynków meczowych, jeden zawodnik dla
player_*). Linie podawaj jak u bukmachera (x.5). Bez linii skrypt wypisuje zakres wokół średniej.
Presety wariancji (VMR = wariancja / średnia): corners 1.25, cards 1.35, fouls 1.15, shots 1.25,
sot 1.15, offsides 1.10, player_fouls 1.05, player_cards 1.0, player_shots 1.10, player_sot 1.05,
goals 1.0. --vmr nadpisuje preset. VMR = 1 to czysty Poisson.
"""
import sys
from math import exp, lgamma, log

PRESETS = {
    "corners": 1.25, "cards": 1.35, "fouls": 1.15, "shots": 1.25, "sot": 1.15, "offsides": 1.10,
    "player_fouls": 1.05, "player_cards": 1.0, "player_shots": 1.10, "player_sot": 1.05, "goals": 1.0,
}


def pmf(k, mu, vmr):
    if vmr <= 1.0001:
        return exp(-mu + k * log(mu) - lgamma(k + 1)) if mu > 0 else float(k == 0)
    n = mu / (vmr - 1.0)  # liczba "sukcesów" NB
    p = 1.0 / vmr
    return exp(lgamma(k + n) - lgamma(n) - lgamma(k + 1) + n * log(p) + k * log(1 - p))


def over(line, mu, vmr, kmax=80):
    thr = int(line) + 1  # x.5 -> > x
    return max(0.0, 1.0 - sum(pmf(k, mu, vmr) for k in range(thr)))


def main(argv):
    vmr_arg = None
    if "--vmr" in argv:
        i = argv.index("--vmr")
        vmr_arg = float(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 2 or argv[0] not in PRESETS:
        sys.exit(__doc__)
    market, mu = argv[0], float(argv[1])
    vmr = vmr_arg if vmr_arg else PRESETS[market]
    lines = [float(x) for x in argv[2:]] or [int(mu) + d + 0.5 for d in range(-3, 3)]
    print(f"rynek={market}  średnia={mu}  VMR={vmr}  (sd ≈ {(mu * vmr) ** 0.5:.2f})\n")
    print(f"{'linia':>6s} {'Over':>7s} {'fair':>6s} {'Under':>7s} {'fair':>6s}")
    for ln in lines:
        po = over(ln, mu, vmr)
        pu = 1 - po
        fo = lambda x: f"{1 / x:.2f}" if x > 0.001 else "-"
        print(f"{ln:6.1f} {po * 100:6.1f}% {fo(po):>6s} {pu * 100:6.1f}% {fo(pu):>6s}")
    print("\nUwaga: liczby bez danych o sędzi/stylu/składach są szkicem; podaj pewność i źródła średniej.")


if __name__ == "__main__":
    main(sys.argv[1:])
