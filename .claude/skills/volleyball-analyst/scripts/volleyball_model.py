#!/usr/bin/env python3
"""Model meczu siatkarskiego z prawdopodobieństwa wygrania seta przez A.

Zwraca zwycięzcę meczu, dokładny wynik w setach, handicap setowy i total setów z fair odds.
Sety traktuje jako niezależne (uproszczenie); decydujący set można wycenić osobno (--p-decider).
Nie wycenia punktów w secie ani rynków zawodnika.
"""
import argparse


def match_dist(ps, bo, p_decider=None):
    need = bo // 2 + 1
    res = {}

    def walk(a, b, pr):
        if a == need or b == need:
            res[(a, b)] = res.get((a, b), 0) + pr
            return
        n = a + b  # numer seta (od 0)
        if p_decider is not None and n == bo - 1:
            p = p_decider
        else:
            p = ps[min(n, len(ps) - 1)]
        walk(a + 1, b, pr * p)
        walk(a, b + 1, pr * (1 - p))

    walk(0, 0, 1.0)
    return res


def p_match(p_set, bo):
    return sum(v for (x, y), v in match_dist([p_set], bo).items() if x > y)


def set_p_from_match(pm, bo):
    """Odwraca P(mecz) -> p seta (bisekcja)."""
    lo, hi = 0.001, 0.999
    for _ in range(80):
        mid = (lo + hi) / 2
        if p_match(mid, bo) < pm:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("p", type=float, nargs="*", help="p wygrania seta przez A (jedna wartość lub lista per set)")
    ap.add_argument("--bo", type=int, default=3, choices=(3, 5), help="format meczu: do 2 lub do 3 wygranych setów")
    ap.add_argument("--p-decider", type=float, default=None, help="p wygrania seta decydującego (np. tie-break do 15)")
    ap.add_argument("--from-match", type=float, default=None,
                    help="zamiast p seta podaj P(A wygra mecz) (np. z kursów bez marży); skrypt dobierze p seta")
    a = ap.parse_args()
    if a.from_match is not None:
        if not 0 < a.from_match < 1:
            ap.error("--from-match musi być w (0,1)")
        ps = [set_p_from_match(a.from_match, a.bo)]
        print(f"Z P(mecz)={a.from_match * 100:.1f}% wynika p seta A = {ps[0] * 100:.1f}% (bo{a.bo})\n")
    else:
        if not a.p:
            ap.error("podaj p seta albo --from-match")
        ps = a.p
    if not all(0 < x < 1 for x in ps) or (a.p_decider is not None and not 0 < a.p_decider < 1):
        ap.error("p musi być w (0,1)")

    res = match_dist(ps, a.bo, a.p_decider)
    fo = lambda x: f"{1 / x:.2f}" if x > 0 else "-"
    pa = sum(v for (x, y), v in res.items() if x > y)
    dec = f", set decydujący p={a.p_decider}" if a.p_decider is not None else ""
    print(f"bo{a.bo} (do {a.bo // 2 + 1} setów), p seta A: {[round(x, 3) for x in ps]}{dec}\n")
    print(f"P(A wygra mecz) = {pa * 100:.1f}%  fair {fo(pa)}   |   B: {(1 - pa) * 100:.1f}%  fair {fo(1 - pa)}\n")
    print("Wynik w setach:")
    for (x, y), v in sorted(res.items(), key=lambda kv: -kv[1]):
        print(f"  {x}:{y}  {v * 100:5.1f}%  fair {fo(v)}")

    print("\nHandicap setowy:")
    for h in (1.5, 2.5) if a.bo == 5 else (1.5,):
        a_minus = sum(v for (x, y), v in res.items() if x - y > h)
        b_minus = sum(v for (x, y), v in res.items() if y - x > h)
        print(f"  A -{h}: {a_minus * 100:5.1f}% (fair {fo(a_minus)})   B +{h}: {(1 - a_minus) * 100:5.1f}% (fair {fo(1 - a_minus)})")
        print(f"  B -{h}: {b_minus * 100:5.1f}% (fair {fo(b_minus)})   A +{h}: {(1 - b_minus) * 100:5.1f}% (fair {fo(1 - b_minus)})")

    tot = {}
    for (x, y), v in res.items():
        tot[x + y] = tot.get(x + y, 0) + v
    print("\nTotal setów:")
    for ln in sorted({n - 0.5 for n in tot if n - 0.5 > a.bo // 2}):
        over = sum(v for n, v in tot.items() if n > ln)
        if over > 0.999 or over < 0.001:
            continue
        print(f"  Over {ln}: {over * 100:5.1f}% (fair {fo(over)})   Under: {(1 - over) * 100:5.1f}% (fair {fo(1 - over)})")


if __name__ == "__main__":
    main()
