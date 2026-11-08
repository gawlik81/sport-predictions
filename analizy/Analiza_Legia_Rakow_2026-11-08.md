# Legia Warszawa - Raków Częstochowa (Ekstraklasa 26/27, 2026-11-08, 17:30 czasu polskiego)

Źródła: connector superbet-mcp (stats, lineups, missing_players, h2h, event_odds). Rezerwa nie użyta (brak czasu: do startu ok. 20 min). Kursy z API Superbet, wiążący jest kurs z kuponu.

**Typ:** brak mocnego typu; wariant awaryjny 12 & Poniżej 4.5 gola | **p:** 59-63% | **Fair:** ok. 1.62 | **Pewność:** średnia | **Kurs:** 1.54 | **EV:** ok. -5% (-8% do -2%)

## Dane
- **Składy oficjalne** obu drużyn (3-4-3). Legia: Hindrich; Piątkowski, Augustyniak, Deziel; Wszołek, Urbański, Szymański, Chodyna; Wjunnyk, Zjawiński, Stępniewski. Raków: Karić; Tudor, Racovițan, Svarnas; Pieńko, Repka, Koczerhin, Otieno; Diaby-Fadiga, Emreli, Makuch.
- **Nieobecni:** Legia - Adamski, Żewłakow (kontuzje), Kapustka (zawieszony); Raków - Perović. Brak kluczowych absencji.
- **Sędzia:** Jarosław Przybył (connector). Brak jego statystyk kartek, więc rynki kartek bez typu.
- **Średnie sezonu (connector):** Legia 1.8 gola strzelonego / 0.8 straconego, xG 1.6, SoT 4.7, rożne 4.5, kartki 1.3. Raków 1.5 / 2.2, xG 1.7, SoT 4.8, rożne 5.0, kartki 2.1 (2 czerwone w ostatnim meczu z Pogonią).
- **Forma:** Legia 1:2 z Lechem, 1:1 w Krakowie, 2:0 Wisła, 5:1 Korona. Raków 3:1 Pogoń, 1:2 w Wiśle, 2:1 Wieczysta (wyjazd), 1:4 GKS Katowice, 4:1 Polonia Bytom.
- **H2H (5 ostatnich):** 1:1, 1:1, 2:3, 1:0 dla Rakowa, 1:1. Wyrównane, remisów dużo.

## Model (Poisson, 3 warianty λ)
| Wariant | 1 / X / 2 | O2.5 | U3.5 | BTTS |
|---|---|---|---|---|
| 1.55 / 1.20 (baza) | 45,4 / 25,1 / 29,5% | 51,9% | 70,3% | 55,0% |
| 1.70 / 1.30 | 46,9 / 23,8 / 29,4% | 57,7% | 64,7% | 59,5% |
| 1.40 / 1.10 | 43,8 / 26,6 / 29,6% | 45,6% | 75,8% | 50,3% |
Rynek (Superbet, bez marży ok.): 1 47,5%, X 26%, 2 26,5%. Model zgodny z rynkiem (±5 pp).

## Wycena nóg (kurs z API; p i EV dla 3 wariantów λ)
| Noga | Kurs | p | EV |
|---|---|---|---|
| **12 & Poniżej 4.5 gola** | 1.54 | 59,5-63,4% | -8,4% do -2,4% |
| X2 | 1.78 | 53,1-56,2% | -5,4% do 0% |
| 12 & Poniżej 3.5 gola | 1.83 | 48,7-54,9% | -10,8% do +0,5% |
| 12 & Powyżej 1.5 gola | 1.58 | 52,8-61,3% | -16,5% do -3,2% |
| Poniżej 2.5 gola | 2.07 | 42,3-54,4% | -12,4% do +12,6% |
| BTTS tak | 1.67 | 50,3-59,5% | -16,1% do -0,7% |

Wniosek: żaden kupon w kursie 1.5-2.5 nie ma EV > 0 w wariancie bazowym ani stabilnie w pozostałych. Najwyższe p ma 12 & Poniżej 4.5 (pewność średnia: brak zależności od sędziego, składy oficjalne). Przewaga bukmachera jest po jego stronie. Pozostałe rynki z dodatnim EV tylko w jednym wariancie (Poniżej 2.5, BTTS nie) mają p < 50% w bazie i pewność niską.

Ryzyka: remis (ok. 25%, zabija nogę 12), 5+ goli (otwarta obrona Rakowa, 2.2 straconego), 2 czerwone Rakowa w ostatnim meczu to sygnał nerwowości. Rożne i kartki nie wyceniane (brak średnich z drugiego źródła, brak danych o sędzi).

*Oszacowania probabilistyczne, nie gwarancje.*
