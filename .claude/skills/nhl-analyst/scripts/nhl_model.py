#!/usr/bin/env python3
"""Model meczu NHL: Poisson goli w 60 minutach + dogrywka (3v3) i rzuty karne.

Użycie:
  nhl_model.py <λ_gospodarze> <λ_goście> [--total L ...] [--ot-mult 2.0]
  nhl_model.py 3.1 2.8 --total 5.5 6.5

<λ_*> to oczekiwane gole drużyn w regulaminowych 60 minutach (średnia ligowa ~3.0 na drużynę;
uwzględnij już bramkarza, back-to-back, absencje). Wynik 3-way (60 min) to rynek "1X2" z remisem;
moneyline to zwycięzca meczu z dogrywką i karnymi (typowy rynek bukmacherski NHL).
Dogrywka: 5 min 3v3, częstość goli = --ot-mult (domyślnie 2.0) × tempo regulaminowe; zwycięzca OT
proporcjonalny do λ, ale ściągnięty w stronę 50/50 (waga 0.5); karne to 50/50. Poisson zaniża remisy po 60' (w lidze ok. 22-24% meczów kończy się po
dogrywce, tu zwykle 16-19%), więc przy rynku 3-way (remis) i moneyline traktuj wynik jako szkic.
Total: gole regulaminowe + gol w dogrywce (gol z rzutów karnych NIE liczy się do totalu u większości
bukmacherów - sprawdź regulamin). Puck line ±1.5 liczy różnicę po dogrywce/karnych (zwycięstwo
w karnych = różnica 1 gola).
"""
import sys
from math import exp, factorial


def pmf(k, lam):
    return exp(-lam) * lam**k / factorial(k)


def main(argv):
    ot_mult = 2.0
    if "--ot-mult" in argv:
        i = argv.index("--ot-mult")
        ot_mult = float(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    lines = []
    if "--total" in argv:
        i = argv.index("--total")
        lines = [float(x) for x in argv[i + 1:]]
        argv = argv[:i]
    if len(argv) != 2:
        sys.exit(__doc__)
    lh, la = float(argv[0]), float(argv[1])
    n = 14
    grid = [[pmf(i, lh) * pmf(j, la) for j in range(n)] for i in range(n)]
    norm = sum(map(sum, grid))
    P = lambda c: sum(grid[i][j] for i in range(n) for j in range(n) if c(i, j)) / norm
    fo = lambda x: f"{1 / x:.2f}" if x > 0.001 else "-"

    ph, pd, pa = P(lambda i, j: i > j), P(lambda i, j: i == j), P(lambda i, j: i < j)
    # dogrywka
    lam_ot = ot_mult * (lh + la) * 5 / 60
    p_goal_ot = 1 - exp(-lam_ot)
    share = 0.5 * (lh / (lh + la)) + 0.5 * 0.5
    ot_h = pd * p_goal_ot * share
    ot_a = pd * p_goal_ot * (1 - share)
    so = pd * (1 - p_goal_ot)
    ml_h = ph + ot_h + so * 0.5
    ml_a = pa + ot_a + so * 0.5

    print(f"λ gospodarze={lh}, λ goście={la}\n")
    print("Po 60 minutach (rynek 3-way):")
    for name, p in (("1 (gospodarze)", ph), ("X (remis po 60')", pd), ("2 (goście)", pa)):
        print(f"  {name:20s} {p * 100:5.1f}%  fair {fo(p)}")
    print("\nMoneyline (z dogrywką i karnymi):")
    print(f"  {'Gospodarze':20s} {ml_h * 100:5.1f}%  fair {fo(ml_h)}")
    print(f"  {'Goście':20s} {ml_a * 100:5.1f}%  fair {fo(ml_a)}")
    print(f"  (mecz kończy się w OT/karnych: {pd * 100:.1f}%, w tym karne {so * 100:.1f}%)")

    # puck line: różnica po meczu; wygrana w karnych = różnica 1
    d_h = {}  # rozkład różnicy dla gospodarzy
    for i in range(n):
        for j in range(n):
            pr = grid[i][j] / norm
            if i != j:
                d_h[i - j] = d_h.get(i - j, 0) + pr
    d_h[1] = d_h.get(1, 0) + ot_h + so * 0.5
    d_h[-1] = d_h.get(-1, 0) + ot_a + so * 0.5
    pl_h_minus = sum(p for d, p in d_h.items() if d >= 2)
    pl_a_plus = 1 - pl_h_minus
    pl_a_minus = sum(p for d, p in d_h.items() if d <= -2)
    pl_h_plus = 1 - pl_a_minus
    print("\nPuck line:")
    print(f"  gospodarze -1.5 {pl_h_minus * 100:5.1f}% fair {fo(pl_h_minus)} | goście +1.5 {pl_a_plus * 100:5.1f}% fair {fo(pl_a_plus)}")
    print(f"  goście -1.5     {pl_a_minus * 100:5.1f}% fair {fo(pl_a_minus)} | gospodarze +1.5 {pl_h_plus * 100:5.1f}% fair {fo(pl_h_plus)}")

    # total: gole regulaminowe + ewentualny gol w OT
    tot = {}
    for i in range(n):
        for j in range(n):
            s = i + j
            pr = grid[i][j] / norm
            if i == j:
                tot[s + 1] = tot.get(s + 1, 0) + pr * p_goal_ot
                tot[s] = tot.get(s, 0) + pr * (1 - p_goal_ot)
            else:
                tot[s] = tot.get(s, 0) + pr
    print("\nTotal goli (regulamin + gol w dogrywce):")
    for ln in lines or [4.5, 5.5, 6.5]:
        po = sum(p for s, p in tot.items() if s > ln)
        print(f"  Over {ln}: {po * 100:5.1f}% fair {fo(po)} | Under {ln}: {(1 - po) * 100:5.1f}% fair {fo(1 - po)}")
    btts = P(lambda i, j: i > 0 and j > 0)
    print(f"\nObie strzelą (60'): tak {btts * 100:.1f}% fair {fo(btts)} | nie {(1 - btts) * 100:.1f}% fair {fo(1 - btts)}")
    print("Uwaga: λ muszą uwzględniać potwierdzonego bramkarza; bez tego pewność jest co najwyżej niska.")


if __name__ == "__main__":
    main(sys.argv[1:])
