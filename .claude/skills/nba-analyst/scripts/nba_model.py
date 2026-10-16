#!/usr/bin/env python3
"""Model meczu NBA: zwycięzca, spread, total i total drużyny z rozkładu normalnego.

Użycie:
  nba_model.py <pkt_gospodarze> <pkt_goście> [--sd-margin 12.0] [--sd-total 18.0] [--spread L ...] [--total L ...]
  nba_model.py 114.5 110.0 --spread -4.5 -2.5 --total 222.5 225.5

<pkt_*> to oczekiwane punkty drużyn w regulaminowym czasie + dogrywka (jak rozliczają bukmacherzy,
łącznie z OT). Spread = oczekiwana różnica (gospodarze - goście); linie spreadu podawaj z punktu
widzenia GOSPODARZY (np. -4.5 = gospodarze dają 4.5). SD różnicy ~12 pkt i SD sumy ~18 pkt to wartości
typowe dla NBA; zwiększ je w meczach z dużą niewiadomą składu (np. >2 gwiazdy w statusie GTD).
Zwycięzca z poprawką ciągłości (różnica jest całkowita, brak remisów dzięki dogrywkom).
"""
import sys
from math import erf, sqrt


def cdf(x, mu, sd):
    return 0.5 * (1 + erf((x - mu) / (sd * sqrt(2))))


def main(argv):
    def take(flag, default):
        if flag in argv:
            i = argv.index(flag)
            return float(argv[i + 1]), argv[:i] + argv[i + 2:]
        return default, argv

    sd_m, argv = take("--sd-margin", 12.0)
    sd_t, argv = take("--sd-total", 18.0)
    lists = {"--spread": [], "--total": []}
    pos = []
    cur = None
    for a in argv:
        if a in lists:
            cur = a
        elif cur:
            lists[cur].append(float(a))
        else:
            pos.append(float(a))
    if len(pos) != 2:
        sys.exit(__doc__)
    h, a = pos
    margin, total = h - a, h + a
    fo = lambda x: f"{1 / x:.2f}" if x > 0.001 else "-"

    # różnica całkowita: P(margin >= 1) = P(X > 0.5) po poprawce ciągłości
    p_home = 1 - cdf(0.5, margin, sd_m)
    print(f"gospodarze {h} - goście {a}  (gospodarze o {margin:+.1f} pkt, total {total:.1f}, SD różnicy {sd_m}, SD sumy {sd_t})\n")
    print(f"{'Gospodarze wygrywają':28s} {p_home * 100:5.1f}%  fair {fo(p_home)}")
    print(f"{'Goście wygrywają':28s} {(1 - p_home) * 100:5.1f}%  fair {fo(1 - p_home)}")

    if lists["--spread"]:
        print("\nSpread (linia z punktu widzenia gospodarzy; gospodarze pokrywają, gdy różnica > -linia):")
        for ln in lists["--spread"]:
            p = 1 - cdf(-ln, margin, sd_m)
            print(f"  gospodarze {ln:+.1f}: {p * 100:5.1f}% fair {fo(p)} | goście {-ln:+.1f}: {(1 - p) * 100:5.1f}% fair {fo(1 - p)}")
    if lists["--total"]:
        print("\nTotal punktów (z dogrywką):")
        for ln in lists["--total"]:
            po = 1 - cdf(ln, total, sd_t)
            print(f"  linia {ln:6.1f}: Over {po * 100:5.1f}% fair {fo(po)} | Under {(1 - po) * 100:5.1f}% fair {fo(1 - po)}")
    print("\nTotal drużyny (SD ~ 11 pkt): użyj nba_props.py team_points <średnia> <linie> --sd 11")
    print("Uwaga: model nie zna składów; średnie punktów muszą już uwzględniać absencje, tempo i back-to-back.")


if __name__ == "__main__":
    main(sys.argv[1:])
