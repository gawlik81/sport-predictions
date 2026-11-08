# Inter Mediolan - Como (Serie A 26/27, 2026-11-08, 18:00 czasu polskiego)

Źródła: connector superbet-mcp (stats, lineups, missing_players, h2h, event_odds). Rezerwa nie użyta. Kursy z API Superbet, wiążący jest kurs z kuponu.

**Typ:** brak mocnego typu; wariant awaryjny 12 & Poniżej 4.5 gola | **p:** 57-62% (bazowo 59,5%) | **Fair:** ok. 1.68 | **Pewność:** średnia | **Kurs:** 1.63 | **EV:** ok. -3% (-7,5% do +1,5%)

## Dane
- **Składy oficjalne.** Inter (Chivu): Martínez; Akanji, Bastoni, Spence, Carlos Augusto, Dimarco; Barella, Çalhanoğlu, Zieliński; Thuram, Esposito. Como (Fabregas): Sanchez; Ramon, Kempf, Couto, Valle; Perrone, Milla, Paz, Da Cunha, Baturina; Douvikas. Ustawienia nie podano.
- **Nieobecni (connector):** Inter - Luis Henrique; Como - Chalobah, Kean, Rodriguez, Addai, Diao (5 kontuzji, w tym Kean).
- **Sędzia:** Daniele Chiffi (connector). Statystyk kartek nie zebrano.
- **Średnie sezonu:** Inter 2.6 gola strzelonego / 1.3 straconego, xG 2.7, SoT 7.2, rożne 6.3. Como 1.8 / 0.8, xG 1.8, SoT 6.3, rożne 7.1.
- **Forma:** Inter 0:3 Feyenoord (wyjazd), 1:3 z Milanem, 2:0 w Wenecji, 2:1 Fiorentina, 1:0 Szachtar. Como: "1:9" z Lens według connectora (wynik wygląda na błąd danych lub odwrócony, nie ufam mu), 1:0 Venezia, 3:1 w Turynie, 2:0 Sassuolo, 4:1 Man United.
- **H2H:** bilans całkowity 5 wygranych Interu, remis, 0 wygranych Como. 3:2, 4:3 (wyjazd), 4:0, 2:0 dla Interu. Dużo goli (średnio ok. 5 na mecz w ostatnich 3 meczach z wynikiem).

## Model (Poisson, 3 warianty λ)
| Wariant | 1 / X / 2 | U3.5 | U4.5 | BTTS tak |
|---|---|---|---|---|
| 1.70 / 1.30 | 46,9 / 23,8 / 29,4% | 64,7% | 81,5% | 59,5% |
| 1.85 / 1.40 | 48,2 / 22,6 / 29,2% | 59,1% | 77,2% | 63,5% |
| 1.55 / 1.15 | 46,5 / 25,2 / 28,2% | 71,4% | 86,3% | 53,8% |
Rynek bez marży: 1 44,2%, X 24,7%, 2 31,1%; Poniżej 3.5 ok. 58,8%; Poniżej 4.5 ok. 75,8%.

## Wycena nóg (kurs z API; p i EV dla 3 wariantów λ)
| Noga | Kurs | p | EV | Uwaga |
|---|---|---|---|---|
| **12 & Poniżej 4.5** | 1.63 | 56,7-62,3% | -7,5% do +1,5% | wybrana (najwyższe p, pewność średnia) |
| Inter wygra | 2.15 | 46,5-48,2% | 0% do +3,5% | p < 50% |
| Poniżej 3.5 gola | 1.61 | 59,1-71,4% | -4,8% do +15% | p o 6 pp nad rynkiem bez konkretnej informacji: pewność niska |
| 1X & Poniżej 4.5 | 1.65 | 55,2-62,4% | -8,9% do +3,0% | |
| X2 | 1.70 | 51,8-53,5% | -12% do -9% | |
| 12 & Powyżej 2.5 | 1.71 | 44,1-54,3% | -25% do -7% | |
| BTTS tak | 1.49 | 53,8-63,5% | -20% do -5% | kurs < 1.5 |

Wniosek: żaden kupon w kursie 1.5-2.5 nie ma EV > 0 w wariancie bazowym przy p > 50% i pewności średniej. Poniżej 3.5 daje dodatnie EV tylko przez p powyżej rynku (reguła: nie schodzić pod rynek o > 5 pp bez informacji, tu lecimy w drugą stronę, więc pewność niska). 12 & Poniżej 4.5 nie wymaga takiej przewagi, ale EV wychodzi ujemne: przewaga bukmachera po jego stronie.

Ryzyka: remis (ok. 24%), 5+ goli (H2H bardzo bramkowe; Inter 2.6 gola na mecz), gol Como z kontry mimo braków (Kean). Rożne, kartki nie wyceniane (brak statystyk Chiffi i drugiego źródła).

*Oszacowania probabilistyczne, nie gwarancje.*
