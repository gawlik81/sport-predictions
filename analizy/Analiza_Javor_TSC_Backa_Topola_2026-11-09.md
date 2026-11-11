# Javor - TSC Backa Topola (Prva Liga 26/27, 09.11.2026, 18:00)

Analiza ekspresowa (start za ok. godzinę). Źródła: connector superbet-mcp (składy oficjalne, statystyki sezonowe, H2H, forma, kursy Superbet). Rezerwa (WebSearch) nie była potrzebna do składów; brak listy nieobecnych ("Brak danych") i brak sędziego.

## Dane
- Gole/mecz (sezon): Javor 2.4 strzelone / 1.1 stracone, TSC 2.3 / 1.1. Strzały celne 5.0 vs 5.8, rożne 3.9 vs 6.2.
- Forma Javoru (8): 3:2, 3:1, 2:1, 3:0, 1:1, 3:1, 1:1, 4:2 (strzelił w każdym meczu, stracił w 7/8).
- Forma TSC (7 znanych): 1:2, 3:2, 2:1, 5:1, 4:1, 4:1, 2:2 (strzelił i stracił w każdym meczu).
- H2H (od 2018: 1 W Javor, 5 R, 9 W TSC); ostatnie: 1:1 (08.2026), 6:1 dla TSC (05.2026), 2:2 (08.2025).
- Składy: oficjalne dla obu drużyn (Javor 4-2-3-1, TSC 4-4-2). Sędzia nieznany.
- Kursy Superbet 1X2: 2.30 / 3.10 / 2.75 (bez marży ok. 38.8% / 28.8% / 32.4%).

## Model (poisson.py)
- λ 1.6 / 1.5 (wariant górny): Over 2.5 59.9%, BTTS 62.0%, 1X2 40.3 / 23.8 / 35.9.
- λ 1.4 / 1.3 (wariant dolny): Over 2.5 50.6%, BTTS 54.8%, 1X2 39.4 / 25.8 / 34.8.
- Rynek (bez marży): Over 2.5 ok. 51.9%, BTTS tak ok. 55%.

## Rynki (p zakres, kurs Superbet, EV przy p środkowym)
| Rynek | p | Kurs | EV |
|---|---|---|---|
| Powyżej 2.5 gola | 51-60% (środek ok. 55%) | 1.85 | ok. +2% |
| BTTS tak | 55-62% (środek ok. 58%) | 1.68 | ok. -3% |
| BTTS tak i powyżej 2.5 | ok. 45% | 2.10 | ok. -5% |
| Powyżej 1.5 gola | ok. 78% | 1.26 | ok. -2% |
| 1X2 | brak mocnego typu | | |

Typ: Powyżej 2.5 gola, pewność średnia (EV bliski zera, p w zakresie 51-60%, przewaga nad rynkiem ok. 3 pp, wynik wrażliwy na λ). Wyrównany mecz 1X2: brak typu.

## Ryzyka
Mecz zamknięty/nerwowy (remis 1:1 lub 1:0), zaniżone λ przez pojedyncze wysokie wyniki w próbie (6:1, 5:1), brak informacji o nieobecnych, nieznany sędzia.

Oszacowania probabilistyczne, nie gwarancje.
