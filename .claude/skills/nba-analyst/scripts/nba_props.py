#!/usr/bin/env python3
"""Rynki zawodnika i drużyny w NBA: Over/Under z rozkładu ujemnego dwumianowego lub normalnego.

Użycie:
  nba_props.py <rynek> <średnia> [linia ...] [--vmr X] [--sd X]
  nba_props.py points 24.8 22.5 24.5 26.5
  nba_props.py rebounds 8.9 7.5 8.5 9.5
  nba_props.py threes 3.1 2.5 3.5
  nba_props.py pra 41 37.5 40.5
  nba_props.py team_points 113 110.5 --sd 11

<średnia> = oczekiwana wartość NA TEN MECZ (średnia na minutę × spodziewane minuty × czynnik rywala),
nie średnia sezonowa. Linie podawaj jak u bukmachera (x.5). Presety wariancji (VMR = wariancja/średnia):
points 2.3, rebounds 1.4, assists 1.25, threes 1.05, steals 1.0, blocks 1.0, pra 2.0, pr 1.9,
pa 1.9, ra 1.5, turnovers 1.15. team_points używa rozkładu normalnego (--sd, domyślnie 11).
--vmr nadpisuje preset. Gdy zawodnik jest zagrożony blowoutem (faworyt o 10+ pkt), obniż średnią
(minuty) PRZED wywołaniem skryptu - skrypt tego nie robi.
"""
import sys
from math import erf, exp, lgamma, log, sqrt

PRESETS = {
    "points": 2.3, "rebounds": 1.4, "assists": 1.25, "threes": 1.05, "steals": 1.0, "blocks": 1.0,
    "pra": 2.0, "pr": 1.9, "pa": 1.9, "ra": 1.5, "turnovers": 1.15,
}


def pmf(k, mu, vmr):
    if vmr <= 1.0001:
        return exp(-mu + k * log(mu) - lgamma(k + 1)) if mu > 0 else float(k == 0)
    n = mu / (vmr - 1.0)
    p = 1.0 / vmr
    return exp(lgamma(k + n) - lgamma(n) - lgamma(k + 1) + n * log(p) + k * log(1 - p))


def over_count(line, mu, vmr):
    return max(0.0, 1.0 - sum(pmf(k, mu, vmr) for k in range(int(line) + 1)))


def over_normal(line, mu, sd):
    return 1 - 0.5 * (1 + erf((line - mu) / (sd * sqrt(2))))


def main(argv):
    def take(flag):
        nonlocal argv
        if flag in argv:
            i = argv.index(flag)
            v = float(argv[i + 1])
            argv = argv[:i] + argv[i + 2:]
            return v
        return None

    vmr_arg, sd_arg = take("--vmr"), take("--sd")
    if len(argv) < 2 or (argv[0] not in PRESETS and argv[0] != "team_points"):
        sys.exit(__doc__)
    market, mu = argv[0], float(argv[1])
    lines = [float(x) for x in argv[2:]] or [int(mu) + d + 0.5 for d in range(-3, 3)]
    fo = lambda x: f"{1 / x:.2f}" if x > 0.001 else "-"
    if market == "team_points":
        sd = sd_arg or 11.0
        print(f"rynek=team_points  średnia={mu}  SD={sd}\n")
        f = lambda ln: over_normal(ln, mu, sd)
    else:
        vmr = vmr_arg or PRESETS[market]
        print(f"rynek={market}  średnia={mu}  VMR={vmr}  (sd ≈ {(mu * vmr) ** 0.5:.2f})\n")
        f = lambda ln: over_count(ln, mu, vmr)
    print(f"{'linia':>6s} {'Over':>7s} {'fair':>6s} {'Under':>7s} {'fair':>6s}")
    for ln in lines:
        po = f(ln)
        print(f"{ln:6.1f} {po * 100:6.1f}% {fo(po):>6s} {(1 - po) * 100:6.1f}% {fo(1 - po):>6s}")
    print("\nUwaga: bez potwierdzonego składu, minut i statusu zawodnika typ ma najwyżej niską pewność.")


if __name__ == "__main__":
    main(sys.argv[1:])
