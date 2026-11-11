# Botosani - Otelul Galati (Superliga Rumunii, 09.11.2026, 19:00 PL, Superbet 14438702)

Analiza skrócona (start za <30 min przy wyborze meczu). Źródła: connector superbet (składy oficjalne, nieobecni, sędzia, średnie sezonu, H2H, forma, kursy), własny model Poissona (`poisson.py`, `markets.py`). Rezerwa (WebSearch, serwisy zewnętrzne) nie użyta.

## Dane
- Składy oficjalne obu drużyn (4-3-3 vs 4-3-3). Nieobecni: Botosani brak; Otelul Postelnicu i Lopes (kontuzje, powód nieznany, bez daty).
- Sędzia: George Catalin Roman; brak jego statystyk kartek/fauli, więc rynki kartek i fauli bez wysokiej pewności.
- Średnie sezonu (gosp. / goście): gole 1.3 / 1.1, stracone 1.4 / 1.6, xG 1.9 / 1.3, strzały celne 3.9 / 4.4, rożne 4.6 / 5.2, kartki 2.9 / 2.2.
- Forma Botosani (6): P 1-2 w Craiovie, R 2-2 UTA, P 1-3 z Petrolulem, P 0-2 z Dinamem, W 2-0 UTA, P 1-3 z CFR (1 W, 1 R, 4 P).
- Forma Otelul (6): R 1-1 Sepsi, P 3-4 Farul, R 1-1 Csikszereda, P 0-1 FCSB, R 1-1 Bacau, P 2-3 Corvinul (0 W, 3 R, 3 P).
- H2H (6 ost.): 1-1, ?, 0-1, 0-1 (Otelul-Botosani 0:1 we wrześniu 2025), 0-0, 2-3. Bilans od 2015: 2 W gosp., 5 R, 3 W gości.

## Model (λ 1.4 / 1.2; xG i gole sezonu, bez korekt kadrowych)
| Rynek | p modelu | p rynku bez marży | fair |
|---|---|---|---|
| 1 / X / 2 | 41.6 / 26.2 / 32.2% | 40.7 / 28.5 / 30.8% | 2.41 / 3.81 / 3.11 |
| Over 2.5 / Under 2.5 | 48.2 / 51.8% | 49.7 / 50.3% | 2.08 / 1.93 |
| Under 3.5 | 73.6% | | 1.36 |
| BTTS tak | 52.6% | 54.3% | 1.90 |
| Rożne Over 8.5 / 7.5 | 59.9% / 71.2% (średnia 9.6) | | 1.67 / 1.40 |
| Kartki Over 3.5 (średnia 4.2) | 57.2% | | 1.75 |

Zgodność z rynkiem: różnice < 3 pp, brak przewagi nad rynkiem.

## Kandydaci na kupon (kursy Superbet z API)
Wszystkie mają EV < 0 (wyliczone dla λ 1.3-1.5 / 1.1-1.3):
- 12 i Under 3.5 @1.68: p ok. 53.7%, EV ok. -10%.
- Under 2.5 @1.83: p 51.8%, EV -5%.
- Under 3.5 @1.31: p 73.6%, EV -3.6% (kurs poniżej progu 1.5).
- 1X i Under 4.5 @1.43: p ok. 60%, EV -14%.
- BTTS tak @1.70: p 52.6%, EV -10%.

Rynki rożnych i kartek: Over 7.5 rożnych @1.30 (p 71%, EV -7%), Over 8.5 @1.50 (p 60%, EV -10%); pewność niska (brak statystyk sędziego i drugiego źródła średniej).

## Wniosek
Brak kuponu z EV > 0; mecz wyrównany, rynek trafnie wyceniony. Wariant awaryjny: 12 i Under 3.5 (p ok. 54%, pewność średnia, EV ok. -10%), ryzyko: remis (ok. 26-28%) i mecz otwarty (4+ gole ok. 26%).

Oszacowania probabilistyczne, nie gwarancje.
