# Hoffenheim - Schalke (Bundesliga, 08.11.2026, 19:30)

Źródła: connector superbet-mcp (składy oficjalne, nieobecni, sędzia Martin Petersen, średnie sezonowe, forma, H2H, kursy); model Poissona (`poisson.py`). Rezerwa (WebSearch/MCP sportsdata) nie użyta ze względu na brak czasu (analiza robiona ok. 15 min przed startem).

## Dane
- Średnie sezonu: Hoffenheim 1,8 gola strzelonego / 2,0 straconego, xG 1,9; Schalke 0,5 / 1,1, xG 1,0. Rożne 6,1 vs 3,3; kartki 2,4 vs 1,4.
- Forma Hoffenheim: 1:1 Crystal Palace (środa, puchar), 0:2 Werder, 3:0 Leverkusen, 3:0 Lyon, 2:1 Gladbach. Forma Schalke: 0:2 RB Lipsk, 0:2 Dynamo Drezno (puchar), 0:1 Mainz, 1:2 Freiburg (strzelili gola w 1 z 4 meczów).
- H2H: ostatnie 5 meczów z lat 2021-23, Hoffenheim 3 wygrane, 2 porażki; stare, mała waga.
- Nieobecni (serwis, powód nieznany): Hoffenheim 7 graczy (Coufal figuruje w oficjalnym XI, więc lista jest nieaktualna), Schalke 4 (m.in. Sylla).
- Składy oficjalne obu drużyn; mecz po środowym meczu pucharowym Hoffenheim.

## Wycena (λ Hoffenheim 1,85 / Schalke 0,95; czułość 1,7-2,0 / 0,9-1,0)
| Rynek | p | fair | kurs rynku (Superbet) | EV |
|---|---|---|---|---|
| Hoffenheim wygra | 58,5% (54-63%) | 1,71 | 1,54 | -10% |
| Remis | 22,5% | 4,45 | 4,60 | |
| Schalke wygra | 19,0% | 5,26 | 5,30 | |
| Powyżej 1,5 gola | 76,9% | 1,30 | | |
| Powyżej 2,5 gola | 53,1% | 1,88 | | |
| BTTS tak | 51,7% | 1,93 | | |

Rynek bez marży: 61,5% / 20,6% / 17,9%; różnica z modelem < 5 pp, bez powodu do odchylenia.

## Kupony (Bet Builder Superbet, kurs 1,5-2,5)
| Kupon | Kurs | p (zakres) | fair | EV |
|---|---|---|---|---|
| Powyżej 1,5 gola + Schalke strzeli powyżej 0,5 | 1,50 | 55% (54-57%) | 1,80 | -17% |
| Hoff. wygra lub remis + Schalke < 2,5 + Hoff. > 1,5 gola | 1,55 | 51% (47-56%) | 1,95 | -21% |
| Hoff. wygra + Hoff. strzeli > 1,5 gola | 1,65 | 47% (42-52%) | 2,12 | -22% |
| Powyżej 2,5 gola + Hoff. strzeli > 1,5 gola | 1,65 | 45% (41-48%) | 2,23 | -26% |
| Powyżej 1,5 gola + Hoff. wygra lub remis | 1,35 | 64% | 1,57 | -14% (poza zakresem kursu) |

Wniosek: żaden kupon w zadanym kursie nie ma EV > 0 ani p > 50% z zapasem; rynek wycenia mecz zgodnie z modelem, a marża Bet Buildera (korelacje) zjada przewagę. Wariant awaryjny o najwyższym p: Powyżej 1,5 gola + Schalke strzeli (p ok. 55%, EV ok. -17%); pewność średnia (Schalke strzela rzadko: 0,5 gola/mecz, więc to najsłabsza noga).

Ryzyka: Schalke bez gola (ok. 40%), 1:0 dla Hoffenheim; rotacja Hoffenheim po pucharze.

To oszacowania probabilistyczne, nie gwarancje.
