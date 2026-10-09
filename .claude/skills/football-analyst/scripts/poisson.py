#!/usr/bin/env python3
"""Rozkład Poissona dla meczu piłkarskiego: 1X2, Over/Under, BTTS, dokładne wyniki."""
import sys
from math import exp, factorial


def pmf(k, lam):
    return exp(-lam) * lam**k / factorial(k)


def main(lh, la, max_goals=10):
    grid = [[pmf(i, lh) * pmf(j, la) for j in range(max_goals + 1)] for i in range(max_goals + 1)]
    total = sum(map(sum, grid))
    p = lambda cond: sum(grid[i][j] for i in range(max_goals + 1) for j in range(max_goals + 1) if cond(i, j)) / total
    fo = lambda x: f"{1 / x:.2f}" if x > 0 else "-"

    rows = [("1 (gospodarze)", p(lambda i, j: i > j)), ("X (remis)", p(lambda i, j: i == j)),
            ("2 (goście)", p(lambda i, j: i < j))]
    for line in (1.5, 2.5, 3.5):
        rows.append((f"Over {line}", p(lambda i, j, l=line: i + j > l)))
        rows.append((f"Under {line}", p(lambda i, j, l=line: i + j < l)))
    rows += [("BTTS tak", p(lambda i, j: i > 0 and j > 0)), ("BTTS nie", p(lambda i, j: i == 0 or j == 0))]

    print(f"λ gospodarze={lh}, λ goście={la}\n")
    for name, prob in rows:
        print(f"{name:16s} {prob * 100:5.1f}%  fair {fo(prob)}")
    print("\nNajbardziej prawdopodobne wyniki:")
    scores = sorted(((grid[i][j] / total, i, j) for i in range(7) for j in range(7)), reverse=True)[:5]
    for prob, i, j in scores:
        print(f"  {i}-{j}  {prob * 100:4.1f}%  fair {fo(prob)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Użycie: poisson.py <lambda_gospodarze> <lambda_goscie>")
    main(float(sys.argv[1]), float(sys.argv[2]))
