#!/usr/bin/env python3
"""Model serii e-sportowej z prawdopodobieństw wygrania map/gier przez A."""
import argparse


def series(ps, bo):
    need = bo // 2 + 1
    res = {}

    def walk(a, b, pr):
        if a == need or b == need:
            res[(a, b)] = res.get((a, b), 0) + pr
            return
        p = ps[min(a + b, len(ps) - 1)]
        walk(a + 1, b, pr * p)
        walk(a, b + 1, pr * (1 - p))

    walk(0, 0, 1.0)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("p", type=float, nargs="+", help="p wygrania mapy/gry przez A (jedna lub lista per mapa)")
    ap.add_argument("--bo", type=int, default=3, choices=(1, 3, 5))
    a = ap.parse_args()
    if not all(0 < x < 1 for x in a.p):
        ap.error("p musi być w (0,1)")
    res = series(a.p, a.bo)
    fo = lambda x: f"{1 / x:.2f}" if x > 0 else "-"
    pa = sum(v for (x, y), v in res.items() if x > y)
    print(f"bo{a.bo}, p map A: {a.p}\n")
    print(f"P(A wygra serię) = {pa * 100:.1f}%  fair {fo(pa)}   |   B: {(1 - pa) * 100:.1f}%  fair {fo(1 - pa)}\n")
    print("Wynik serii:")
    for (x, y), v in sorted(res.items(), key=lambda kv: -kv[1]):
        print(f"  {x}-{y}  {v * 100:5.1f}%  fair {fo(v)}")
    if a.bo > 1:
        print("\nHandicap map ±1.5:")
        h_a = sum(v for (x, y), v in res.items() if x - y >= 2)
        a_plus = sum(v for (x, y), v in res.items() if y - x < 2)
        b_plus = sum(v for (x, y), v in res.items() if x - y < 2)
        b_minus = sum(v for (x, y), v in res.items() if y - x >= 2)
        print(f"  A -1.5: {h_a * 100:5.1f}% (fair {fo(h_a)})   B +1.5: {b_plus * 100:5.1f}% (fair {fo(b_plus)})")
        print(f"  B -1.5: {b_minus * 100:5.1f}% (fair {fo(b_minus)})   A +1.5: {a_plus * 100:5.1f}% (fair {fo(a_plus)})")
        print("\nTotal map:")
        tot = {}
        for (x, y), v in res.items():
            tot[x + y] = tot.get(x + y, 0) + v
        for ln in sorted({n - 0.5 for n in tot if n - 0.5 > a.bo // 2}):
            over = sum(v for n, v in tot.items() if n > ln)
            if over > 0.999 or over < 0.001:
                continue
            print(f"  Over {ln}: {over * 100:5.1f}% (fair {fo(over)})   Under: {(1 - over) * 100:5.1f}% (fair {fo(1 - over)})")


if __name__ == "__main__":
    main()
