#!/usr/bin/env python3
"""Rynki zawodnika w NHL: Over/Under (Poisson / ujemny dwumian) i strzelec gola w meczu.

Użycie:
  nhl_props.py <rynek> <średnia> [linia ...] [--vmr X]
  nhl_props.py sog 3.4 2.5 3.5 4.5
  nhl_props.py saves 26.5 24.5 26.5 28.5
  nhl_props.py points 0.95 0.5 1.5
  nhl_props.py goals 0.38 0.5        # = anytime goalscorer: P(>=1 gol)

<średnia> = oczekiwana wartość NA TEN MECZ (stopień/minuty w 5v5 i na PP × rywal), nie średnia
sezonowa. Presety VMR: sog 1.2, saves 1.3, goals 1.0, assists 1.0, points 1.05, hits 1.4, blocks 1.2,
shots_against (drużyna) 1.25. Interpretacja `goals 0.5` przy średniej 0.38 to Over 0.5 = anytime scorer.
Bramkarz (saves): średnia = oczekiwane strzały rywala × oczekiwany SV%; jeśli bramkarz nie jest
potwierdzony jako startujący, rynek nie dostaje typu.
"""
import sys
from math import exp, lgamma, log

PRESETS = {
    "sog": 1.2, "saves": 1.3, "goals": 1.0, "assists": 1.0, "points": 1.05, "hits": 1.4,
    "blocks": 1.2, "shots_against": 1.25,
}


def pmf(k, mu, vmr):
    if vmr <= 1.0001:
        return exp(-mu + k * log(mu) - lgamma(k + 1)) if mu > 0 else float(k == 0)
    n = mu / (vmr - 1.0)
    p = 1.0 / vmr
    return exp(lgamma(k + n) - lgamma(n) - lgamma(k + 1) + n * log(p) + k * log(1 - p))


def main(argv):
    vmr_arg = None
    if "--vmr" in argv:
        i = argv.index("--vmr")
        vmr_arg = float(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 2 or argv[0] not in PRESETS:
        sys.exit(__doc__)
    market, mu = argv[0], float(argv[1])
    vmr = vmr_arg or PRESETS[market]
    lines = [float(x) for x in argv[2:]] or [int(mu) + d + 0.5 for d in range(-2, 3) if int(mu) + d + 0.5 > 0]
    fo = lambda x: f"{1 / x:.2f}" if x > 0.001 else "-"
    print(f"rynek={market}  średnia={mu}  VMR={vmr}  (sd ≈ {(mu * vmr) ** 0.5:.2f})\n")
    print(f"{'linia':>6s} {'Over':>7s} {'fair':>6s} {'Under':>7s} {'fair':>6s}")
    for ln in lines:
        po = max(0.0, 1.0 - sum(pmf(k, mu, vmr) for k in range(int(ln) + 1)))
        print(f"{ln:6.1f} {po * 100:6.1f}% {fo(po):>6s} {(1 - po) * 100:6.1f}% {fo(1 - po):>6s}")
    print("\nUwaga: bez potwierdzonego składu, linii (centrum/skrzydło) i roli na PP typ ma najwyżej niską pewność.")


if __name__ == "__main__":
    main(sys.argv[1:])
