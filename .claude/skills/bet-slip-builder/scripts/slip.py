#!/usr/bin/env python3
"""Wycena zestawu typów: łączne p, fair odds, kurs rynkowy, EV (niezależność meczów)."""
import sys


def main(args):
    if not args or len(args) % 3:
        sys.exit('Użycie: slip.py "opis" p kurs ["opis" p kurs ...]   (kurs 0 lub - = nieznany)')
    legs = []
    for i in range(0, len(args), 3):
        name, p = args[i], float(args[i + 1])
        k = 0.0 if args[i + 2] in ("-", "0") else float(args[i + 2])
        if not 0 < p < 1:
            sys.exit(f"p musi być w (0,1): {name}")
        legs.append((name, p, k))

    total_p, total_k, known = 1.0, 1.0, True
    print(f"{'Typ':40s} {'p':>6s} {'fair':>6s} {'kurs':>6s} {'EV':>7s}")
    for name, p, k in legs:
        total_p *= p
        ev = f"{(p * k - 1) * 100:+.1f}%" if k else "-"
        print(f"{name[:40]:40s} {p * 100:5.1f}% {1 / p:6.2f} {k if k else '-':>6} {ev:>7s}")
        if 1 / p <= 1.15:
            print(f"  ! fair odds <= 1.15 ({name})")
        if k and p * k < 1:
            print(f"  ! ujemne EV ({name}): kurs {k} < fair {1 / p:.2f}")
        if k and k <= 1.2:
            print(f"  ! kurs nogi <= 1.2 (domyślny próg) ({name})")
        if k:
            total_k *= k
        else:
            known = False
    print(f"\nŁączne p: {total_p * 100:.1f}%   fair odds zestawu: {1 / total_p:.2f}")
    if known:
        ev = total_p * total_k - 1
        print(f"Łączny kurs: {total_k:.2f}   EV: {ev * 100:+.1f}%")
        if total_k <= 1.6:
            print("  ! łączny kurs <= 1.6 (domyślny próg)")
        if total_p <= 0.5:
            print("  ! łączne p <= 50% (domyślny próg)")
        if ev > 0 and total_k > 1:
            kelly = (total_p * total_k - 1) / (total_k - 1)
            print(f"Stawka (Kelly): {kelly * 100:.1f}% bankrolla pełne | "
                  f"{kelly * 50:.1f}% (1/2 Kelly, bezpieczniej) | "
                  f"{kelly * 25:.1f}% (1/4 Kelly) - sugestia, nie porada finansowa")
        else:
            print("Stawka: 0% bankrolla (EV <= 0, bez przewagi nad rynkiem)")
    else:
        print("Łączny kurs / EV: nieznane (brak kursu przy co najmniej jednej nodze)")


if __name__ == "__main__":
    main(sys.argv[1:])
