# Polska - Szwecja (UEFA Liga Narodów, dywizja B, Tarczyński Arena Wrocław), 17.11.2026, 20:45

Mecz o stawkę (Liga Narodów, nie towarzyski). Źródła: connector superbet-mcp (stats, h2h, missing_players, lineups, event_odds); rezerwa: WebSearch (nie znalazł składów na ten mecz, tylko artykuły z wrześniowego meczu). BettingPros: nie użyto (brak klucza w sesji).

## Dane
- Sędzia: Felix Zwayer (connector). Składy: tylko "przewidywane" (4-4-2 obie strony), niepotwierdzone. Polska: Lewandowski i Świderski z przodu (jeden z tytułów w wyszukiwarce sugeruje, że Urban posadził Lewandowskiego na ławce, ale dotyczy to prawdopodobnie meczu wrześniowego, niezweryfikowane).
- Nieobecni (connector): Polska - Kiwior (zawieszenie), Cash (uraz); Szwecja - brak wpisów (nie gwarantuje kompletu).
- Średnie sezonu (connector): gole strzelone 1,6 / 2,0, stracone 1,2 / 1,0, xG 1,7 / 1,8, celne 5,4 / 4,6, rożne 5,8 / 2,8, kartki 2,6 / 0,8 (Polska / Szwecja).
- H2H: Szwecja 3:1 (28.09.2026) i 3:2 (31.03.2026), Polska 2:0 (2022), Szwecja 3:2 (2021). Forma Polski: 1:2 Rumunia (14.11), 0:1 Bośnia, 6:0 Rumunia, 1:3 Szwecja. Forma Szwecji: 3:2 Bośnia, 1:0 Rumunia, 1:1 Bośnia, 3:1 Polska.
- Kursy Superbet 1X2: 2,15 / 3,80 / 3,10 (bez marży ok. 44 / 25 / 31%).

## Model (λ Polska 1,45, Szwecja 1,30; poisson.py)
| Rynek | p | fair |
|---|---|---|
| 1 / X / 2 | 40,7 / 25,5 / 33,8% | 2,46 / 3,93 / 2,95 |
| Over 1,5 / 2,5 / 3,5 | 76,0 / 51,9 / 29,7% | 1,32 / 1,93 / 3,37 |
| BTTS tak | 55,7% | 1,80 |
| Rożne Over 8,5 (średnia 9,2, szkic) | ok. 55% | 1,81 |
| Kartki Over 3,5 (średnia 4,2, szkic) | ok. 57% | 1,75 |

Model daje Polsce 3-4 pp mniej niż rynek (brak Kiwiora i Casha po stronie obrony nie uzasadnia schodzenia pod rynek o więcej, patrz zasady kalibracji). Pewność wyniku: niska (mecz wyrównany, brak mocnego typu). Rynek Superbet sugeruje więcej goli niż model (np. BTTS i Over 2,5 po 1,76 => ok. 57%, BTTS i Over 3,5 po 2,47 => ok. 40%), więc λ może być zaniżone; do wyjaśnienia.

## Kupon Bet Builder > 5
Kandydaci z oferty (kursy Superbet z API, wiążący kurs z kuponu w przeglądarce):
| Kombinacja | Kurs | Moje p (szkic, korelacje przybliżone) | EV |
|---|---|---|---|
| Over 3,5 gola; Polska wygra lub zremisuje; BTTS; Over 2,5 kartek; Over 8,5 rożnych | 5,5 | ok. 7-9% | ok. -55% |
| Każda drużyna Over 3,5 rożnych; każda Over 1,5 kartek; BTTS | 6,5 | ok. 5-7% | ok. -60% |
| Szwecja Over 3,5 rożnych... (6 nóg) | 11-18 | ułamki % | silnie ujemne |

Wniosek: kupon > 5 w tym meczu to 4-6 skorelowanych nóg, z których część zależy od niepotwierdzonych składów (kartki Szwecji średnio 0,8 to mała próba, rożne Szwecji 2,8). Pewność najsłabszej nogi: niska, a EV wyraźnie ujemne. Zgodnie z regułami skilla `superbet-coupon` kuponu nie przygotowano.

Wariant awaryjny o najwyższym p w kursie > 5 (tylko informacyjnie, nie do postawienia): pierwszy wiersz tabeli.

Oszacowania probabilistyczne, nie gwarancje.
