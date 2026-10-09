#!/usr/bin/env python3
"""Model tenisowy punkt -> gem -> set -> mecz (punkty niezależne, stałe p_serve)."""
import argparse
from functools import lru_cache


@lru_cache(None)
def game(p, a=0, b=0):
    """P(serwujący wygrywa gem) przy stanie punktów a:b."""
    if a >= 4 and a - b >= 2:
        return 1.0
    if b >= 4 and b - a >= 2:
        return 0.0
    if a >= 3 and b >= 3:  # równowaga
        d = p * p / (p * p + (1 - p) ** 2)
        return d if a == b else (p + (1 - p) * d if a > b else p * d)
    return p * game(p, a + 1, b) + (1 - p) * game(p, a, b + 1)


def tiebreak(pa, pb, target=7):
    """P(A wygrywa tiebreak); A serwuje pierwszy punkt, potem zmiana co 2."""
    from collections import defaultdict
    st = {(0, 0): 1.0}
    win = 0.0
    for n in range(0, 200):
        nxt = defaultdict(float)
        for (a, b), pr in st.items():
            if (a >= target or b >= target) and abs(a - b) >= 2:
                win += pr if a > b else 0.0
                continue
            # kolejność serwisu: punkt 0 - A, potem B,B,A,A,...
            a_serves = ((n + 1) // 2) % 2 == 0
            pw = pa if a_serves else 1 - pb
            nxt[(a + 1, b)] += pr * pw
            nxt[(a, b + 1)] += pr * (1 - pw)
        st = nxt
        if not st:
            break
    return win


def set_dist(pa, pb, tb_target=7):
    """Rozkład seta: dict {(gemyA, gemyB): P} i P(A wygrywa seta); A serwuje pierwszy gem."""
    ga, gb = game(pa), game(pb)
    ptb = tiebreak(pa, pb, tb_target)
    res = {}

    def walk(a, b, pr):
        if a == 6 and b == 6:
            res[(7, 6)] = res.get((7, 6), 0) + pr * ptb
            res[(6, 7)] = res.get((6, 7), 0) + pr * (1 - ptb)
            return
        if (a >= 6 and a - b >= 2) or a == 7:
            res[(a, b)] = res.get((a, b), 0) + pr
            return
        if (b >= 6 and b - a >= 2) or b == 7:
            res[(a, b)] = res.get((a, b), 0) + pr
            return
        pw = ga if (a + b) % 2 == 0 else 1 - gb
        walk(a + 1, b, pr * pw)
        walk(a, b + 1, pr * (1 - pw))

    walk(0, 0, 1.0)
    return res, sum(v for (a, b), v in res.items() if a > b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pa", type=float, help="p_serve zawodnika A (0-1)")
    ap.add_argument("pb", type=float, help="p_serve zawodnika B (0-1)")
    ap.add_argument("--bo", type=int, default=3, choices=(3, 5))
    ap.add_argument("--tiebreak", type=int, default=7)
    a = ap.parse_args()
    # uproszczenie: kto serwuje pierwszy w secie nie wpływa istotnie; uśredniamy obie opcje
    d1, w1 = set_dist(a.pa, a.pb, a.tiebreak)
    d2, w2 = set_dist(a.pb, a.pa, a.tiebreak)
    dist = {}
    for (x, y), v in d1.items():
        dist[(x, y)] = dist.get((x, y), 0) + v / 2
    for (x, y), v in d2.items():
        dist[(y, x)] = dist.get((y, x), 0) + v / 2
    ps = sum(v for (x, y), v in dist.items() if x > y)
    need = a.bo // 2 + 1
    from math import comb
    # wynik setowy
    results = {}
    for k in range(need):  # przeciwnik wygrywa k setów
        n = need - 1 + k
        results[(need, k)] = comb(n, k) * ps**need * (1 - ps) ** k
        results[(k, need)] = comb(n, k) * (1 - ps) ** need * ps ** k
    pm = sum(v for (x, y), v in results.items() if x > y)
    fo = lambda p: f"{1 / p:.2f}" if p > 0 else "-"
    print(f"p_serve A={a.pa}, B={a.pb}, bo{a.bo}, tiebreak do {a.tiebreak}\n")
    print(f"P(A wygra seta) = {ps * 100:.1f}%  fair {fo(ps)}")
    print(f"P(A wygra mecz) = {pm * 100:.1f}%  fair {fo(pm)}   |   B: {(1 - pm) * 100:.1f}%  fair {fo(1 - pm)}\n")
    print("Wynik setowy:")
    for (x, y), v in sorted(results.items(), key=lambda kv: -kv[1]):
        print(f"  {x}-{y}  {v * 100:5.1f}%  fair {fo(v)}")
    # total gemów przez Monte Carlo-free: splot rozkładów liczby gemów w secie
    sets_games = {}
    for (x, y), v in dist.items():
        sets_games[x + y] = sets_games.get(x + y, 0) + v
    from itertools import product
    tot = {}
    for (x, y), v in results.items():
        n_sets = x + y
        # przybliżenie: niezależne sety o tym samym rozkładzie liczby gemów
        conv = {0: 1.0}
        for _ in range(n_sets):
            new = {}
            for g0, p0 in conv.items():
                for g1, p1 in sets_games.items():
                    new[g0 + g1] = new.get(g0 + g1, 0) + p0 * p1
            conv = new
        for g, p in conv.items():
            tot[g] = tot.get(g, 0) + v * p
    mean = sum(g * p for g, p in tot.items())
    print(f"\nOczekiwany total gemów: {mean:.1f}")
    lines = [round(mean) - 2.5 + i for i in range(5)]
    for ln in lines:
        over = sum(p for g, p in tot.items() if g > ln)
        print(f"  Over {ln:.1f}: {over * 100:5.1f}% (fair {fo(over)})   Under: {(1 - over) * 100:5.1f}% (fair {fo(1 - over)})")


if __name__ == "__main__":
    main()
