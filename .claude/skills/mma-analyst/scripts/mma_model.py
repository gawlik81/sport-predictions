#!/usr/bin/env python3
"""Model walki MMA: zwycięzca, sposób wygranej, dystans, Over/Under rund.

Wejście to oszacowania analityka (z researchu), nie dane surowe:
  fa, fb - P(A wygra przez finisz), P(B wygra przez finisz) w całej walce,
  da     - P(A wygra na punkty | walka idzie na dystans),
  rounds - liczba rund (3 lub 5), w - względna intensywność finiszy w kolejnych rundach.
Model dobiera stałą intensywność rundową tak, by łączne P(finisz) = fa + fb,
dzieli finisze rundowe proporcjonalnie do fa:fb i zakłada równomierny rozkład finiszu w rundzie
(do linii Over/Under liczonych co pół rundy).
"""
import argparse


def solve_c(total, ws):
    """Znajdź c: 1 - prod(1 - c*w_r) = total (bisekcja)."""
    hi = 1.0 / max(ws)
    lo = 0.0
    for _ in range(100):
        mid = (lo + hi) / 2
        s = 1.0
        for w in ws:
            s *= 1 - mid * w
        if 1 - s < total:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def model(fa, fb, da, draw, rounds, ws, ko_a, ko_b):
    total = fa + fb
    share_a = fa / total if total > 0 else 0.5
    c = solve_c(total, ws) if total > 0 else 0.0
    surv = 1.0
    per_round = []  # (P(finisz w rundzie), P(przeżycie do jej początku))
    for w in ws:
        h = c * w
        per_round.append((surv * h, surv))
        surv *= 1 - h
    dist = surv
    return {
        "per_round": per_round,
        "dist": dist,
        "a_dec": dist * (1 - draw) * da,
        "b_dec": dist * (1 - draw) * (1 - da),
        "draw": dist * draw,
        "a_fin": fa, "b_fin": fb,
        "a_ko": fa * ko_a, "a_sub": fa * (1 - ko_a),
        "b_ko": fb * ko_b, "b_sub": fb * (1 - ko_b),
        "share_a": share_a,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fa", type=float, help="P(A wygra przez finisz KO/TKO/submission/DQ), 0-1")
    ap.add_argument("fb", type=float, help="P(B wygra przez finisz), 0-1")
    ap.add_argument("da", type=float, help="P(A wygra na punkty | dystans), 0-1 (bez remisu)")
    ap.add_argument("--rounds", type=int, default=3, choices=(2, 3, 5), help="liczba rund (UFC 3, walki o pas/main event 5; KSW zwykle 3)")
    ap.add_argument("--w", type=str, default=None, help="wagi finiszu per runda, np. 1.3,1,0.8 (domyślnie płasko)")
    ap.add_argument("--ko-a", type=float, default=0.7, help="udział KO/TKO w finiszach A (reszta submission)")
    ap.add_argument("--ko-b", type=float, default=0.7, help="udział KO/TKO w finiszach B")
    ap.add_argument("--draw", type=float, default=0.02, help="P(remis | dystans), domyślnie 2%%")
    ap.add_argument("--name-a", default="A")
    ap.add_argument("--name-b", default="B")
    a = ap.parse_args()
    for n, v in (("fa", a.fa), ("fb", a.fb), ("da", a.da), ("ko-a", a.ko_a), ("ko-b", a.ko_b), ("draw", a.draw)):
        if not 0 <= v <= 1:
            ap.error(f"{n} musi być w [0,1]")
    if a.fa + a.fb >= 0.99:
        ap.error("fa + fb musi być < 0.99")
    ws = [float(x) for x in a.w.split(",")] if a.w else [1.0] * a.rounds
    if len(ws) != a.rounds:
        ap.error("liczba wag --w musi równać się liczbie rund")
    m = model(a.fa, a.fb, a.da, a.draw, a.rounds, ws, a.ko_a, a.ko_b)
    fo = lambda x: f"{1 / x:.2f}" if x > 0.0005 else "-"
    pa = m["a_fin"] + m["a_dec"]
    pb = m["b_fin"] + m["b_dec"]
    print(f"{a.name_a} vs {a.name_b} | {a.rounds} rundy | wagi finiszu {ws}\n")
    print(f"Zwycięzca: {a.name_a} {pa * 100:.1f}% (fair {fo(pa)})   {a.name_b} {pb * 100:.1f}% (fair {fo(pb)})   remis {m['draw'] * 100:.1f}%")
    print(f"  (bez remisu - do porównania z kursem 2-way: {a.name_a} {pa / (pa + pb) * 100:.1f}%, {a.name_b} {pb / (pa + pb) * 100:.1f}%)\n")
    print("Sposób wygranej:")
    rows = [(f"{a.name_a} KO/TKO", m["a_ko"]), (f"{a.name_a} submission", m["a_sub"]), (f"{a.name_a} na punkty", m["a_dec"]),
            (f"{a.name_b} KO/TKO", m["b_ko"]), (f"{a.name_b} submission", m["b_sub"]), (f"{a.name_b} na punkty", m["b_dec"])]
    for name, v in rows:
        print(f"  {name:<28} {v * 100:5.1f}%  fair {fo(v)}")
    fin = m["a_fin"] + m["b_fin"]
    print(f"\nDystans: {m['dist'] * 100:.1f}% (fair {fo(m['dist'])})   Finisz: {fin * 100:.1f}% (fair {fo(fin)})\n")
    print("Finisz w rundzie:")
    for i, (p, _) in enumerate(m["per_round"], 1):
        print(f"  Runda {i}: {p * 100:5.1f}%  (fair {fo(p)})")
    print("\nOver/Under rund (finisz równomiernie w rundzie):")
    for k in range(a.rounds):
        line = k + 0.5
        # P(walka trwa dłużej niż 'line' rund) = przeżycie do początku rundy k+1 + połowa finiszu w rundzie k+1
        p_fin, surv = m["per_round"][k]
        over = surv - 0.5 * p_fin
        print(f"  Over {line}: {over * 100:5.1f}% (fair {fo(over)})   Under: {(1 - over) * 100:5.1f}% (fair {fo(1 - over)})")


if __name__ == "__main__":
    main()
