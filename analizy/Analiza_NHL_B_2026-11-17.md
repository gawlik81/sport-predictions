# Analiza NHL B - noc 17->18.11.2026 (czas PL)

Sprawdzono: wt. 17.11.2026 ok. 13:15 CET. **Bramkarze startowi: WSZYSTKIE NIEPOTWIERDZONE** (Daily Faceoff 17.11: 0 z 22 potwierdzonych; poniżej "przewidywani" = domyślni startowi z DF). Skład może się zmienić do startu; potwierdzenia zwykle po porannej rozgrzewce (po 16:00 CET). Pewność wszędzie najwyżej średnia, dla rynków zależnych od bramkarza niska.

**Back-to-back:** żadna z 10 drużyn nie grała 16.11 (ESPN scoreboard 16.11: tylko MTL@NYR i VAN@UTA), więc brak B2B i korekty -0,1 gola.
**Rozliczenie:** "Mecz" Superbet = wynik po 60' (3-way, remis X); "Zwycięzca" i "Liczba goli" = z dogrywką i karnymi (gol w karnych nie jest golem w meczu). Skrypt (Poisson) zaniża remis po 60' (ok. 16% vs ~22-24% w lidze), więc p remisu i OT to szkic; p 60' 1/2 jest lekko zawyżone względem ML.
**Źródła:** Superbet (kursy, event_odds), NHL standings API (bilanse, GF/GA, dom/wyjazd, L10), Daily Faceoff (goalies, SV%/GAA; sezon/próba niesprecyzowane), sportbusy.com (kontuzje, linie rynkowe: kursy US do kontroli, część danych tej strony wygląda na nieaktualne - bilans Superbet/NHL ważniejszy), ESPN scoreboard. BettingPros: pominięte (brak klucza w sesji agenta). xG/GSAx/MoneyPuck: brak dostępu, λ z GF/GA + SV% + rynek, dlatego pewność maks. średnia. H2H: brak źródła (superbet_h2h nie obsługuje hokeja), waga w NHL niska, pominięte.

Metoda: λ = średnia ligi (~3,1) skorygowana o GF/GA obu drużyn (NHL standings), dom +0,1, bramkarz domyślny, kontuzje, i skontrolowana względem rynku (no-vig). Odstępstwa od rynku <=5 pp.

---

## 1. Toronto Maple Leafs @ Chicago Blackhawks - 01:30 PL (18.11), Superbet 15586358
Gospodarze: Chicago (dom). Back-to-back: brak obu.

**Bramkarze (niepotwierdzeni):** TOR Sergei Bobrovsky (.881, 3.47), CHI Spencer Knight (.882, 3.54) - obaj słabi (DF). Merzlikins (TOR) na IR.
**Statystyki (NHL standings):** TOR 8-12-2, GF 3,14 / GA 3,45, L10 2-8-0, seria 6 porażek, wyjazd 4-3-1 (GF 4,5/GA 3,5 z 8 m.). CHI 5-13-2, GF 2,30 / GA 4,15 (najgorsza obrona i atak ligi w tej parze), dom 5-5-1, L10 2-6-2, jedyny punkt z OT.
**Kontuzje:** TOR - Marchenko, Wood, Domi, Blankenburg, Sissons itd. na IR, Rielly DTD (sportbusy; Matthews bez pewności - Superbet wystawia jego rynek, status do sprawdzenia). CHI - Byram IR (sportbusy listuje Kane'a jako out - niepotwierdzone; Superbet ma rynki Kane'a).
**Oczekiwane gole:** CHI 2,9 - TOR 3,35 (łącznie 6,25). Seria 6 porażek TOR nie obniża p faworyta (forma w kursie); CHI to kandydat "kryzys" ale jest underdogiem, więc korekta już w λ.
**Rynek (Superbet):** 1X2 CHI 2,95 / X 4,00 / TOR 2,00; ML TOR 1,63, CHI 2,25 (no-vig TOR 58%); total 6,5: Over 1,92 / Under 1,87.

| Rynek | p | fair | kurs Superbet | EV | Pewność |
|---|---|---|---|---|---|
| ML TOR (z OT) | 57% | 1.75 | 1.63 | -7% | średnia-niska (bramkarz) |
| 60' TOR | 49% | 2.04 | 2.00 | -2% | niska |
| Puck line TOR +1.5 (z OT) | 79% | 1.27 | brak | - | niska |
| Puck line CHI +1.5 | 67% | 1.50 | brak | - | niska |
| Total Over 4.5 | 77% (rynek ~86%) | 1.29 | 1.16 | -10% | niska |
| Total Under 6.5 | 53% | 1.87 | 1.87 | 0% | niska |
| Total Over 5.5 | 59% | 1.68 | 1.58 | -6% | niska |

Typ: TOR ML bez przewagi (kurs poniżej fair). **Brak mocnego typu**; spore ryzyko: obie bramki dziurawe, więc wynik losowy. Ryzyka: zmiana bramkarza (Knight/Bobrovsky vs rezerwowi), Matthews/Kane status, seria porażek TOR (motywacja/zmiana trenera?).
Rynki zawodnika (celne strzały 3.5 + wygrana drużyny, asysty): to kombinacje z wynikiem drużyny; brak 2 niezależnych źródeł średnich - **brak podstaw**.

---

## 2. Anaheim Ducks @ St. Louis Blues - 02:00 PL, Superbet 15586971
Gospodarze: St. Louis (dom). B2B: brak.

**Bramkarze (niepotwierdzeni):** ANA Ville Husso (.881, 3.10), STL Jordan Binnington (.851, 4.26 - bardzo słaby). Sportbusy pokazuje też Hofer (STL, statystyka sprzed sezonu), więc zmiana w bramce STL realna (+/-).
**Statystyki:** ANA 11-9-1, GF 3,76 / GA 3,67 (mecze otwarte), wyjazd 7-3-0, L10 6-3-1. STL 9-9-2, GF 2,75 / GA 2,95, dom 5-3-1, L10 4-5-1, seria porażek 1.
**Kontuzje:** ANA - Poehling, Greer IR (sportbusy). STL - brak zgłoszeń.
**Oczekiwane gole:** STL 3,25 - ANA 3,1 (6,35). Dom +0,1, Binnington (.851) daje ANA +0,2, ale gorszy atak STL; wynik prawie 50/50. Rynek wyceniał STL wyżej (no-vig STL 56%), moja różnica ok. 4 pp - w limicie, dociągnięta w λ.
**Rynek:** 1X2 STL 2,10 / X 4,00 / ANA 2,80; ML STL 1,67, ANA 2,17; total Over 6,5 1,95 / Under 1,83.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| ML STL (z OT) | 52% | 1.91 | 1.67 | -13% | niska |
| ML ANA | 48% | 2.10 | 2.17 | +4% | niska |
| 60' ANA | 40% | 2.53 | 2.80 | +11% | niska |
| Puck line STL +1.5 | 75% | 1.34 | brak | - | niska |
| Puck line ANA +1.5 | 71% | 1.41 | brak | - | niska |
| Total Over 5.5 | 61% | 1.64 | 1.61 | -2% | niska |
| Total Over 6.5 / Under 6.5 | 48% / 52% | 2.07 / 1.93 | 1.95 / 1.83 | -6% / -5% | niska |

Typ: **brak mocnego typu** (wyrównane). ML ANA ma formalnie +EV, ale to efekt niepotwierdzonego bramkarza STL; oznacz jako "kandydat warunkowy" (potwierdzony Binnington -> ANA ML p ok. 50%, fair 2,0). Ryzyka: Hofer zamiast Binnington (STL +0,2 gola), Husso niestabilny.
Rynki zawodnika: **brak podstaw**.

---

## 3. Nashville Predators @ Minnesota Wild - 02:00 PL, Superbet 15586424
Gospodarze: Minnesota (dom). B2B: brak.

**Bramkarze (niepotwierdzeni):** MIN Jesper Wallstedt (.926, 1.94; DF 16 m. 11-2-3, .922/1.99), Gustavsson na IR (sportbusy) więc Wallstedt jest niemal pewny startem; NSH Juuse Saros (.918, 2.49; zwykle startuje; w pierwszym meczu sezonu grał).
**Statystyki:** MIN 15-3-4 (najlepszy bilans), GF 3,45 / GA 2,18, dom 5-0-2 (GF 3,6/GA 2,4), L10 8-0-2, seria W3. NSH 11-5-5, GF 3,05 / GA 2,81, wyjazd 5-2-3, L10 7-2-1. PDO MIN wysokie (GA 2,18 przy .926 - regresja możliwa) - skorygowane w dół o 0,1 gola.
**Kontuzje:** MIN - Maatta out, Faber (fractured skull, wcześniej wracał). NSH - Marchessault DTD.
**Oczekiwane gole:** MIN 3,2 - NSH 2,6 (5,8). Dwóch dobrych bramkarzy ścina total.
**Rynek:** 1X2 MIN 1,77 / X 4,25 / NSH 3,50; ML MIN 1,46, NSH 2,65 (no-vig MIN 64,5%); total Over 5,5 1,70 / Under 5,5 2,12; Over 6,5 2,10 / Under 6,5 1,71.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| ML MIN (z OT) | 60% | 1.67 | 1.46 | -12% | średnia |
| 60' MIN | 51% | 1.95 | 1.77 | -9% | średnia |
| Puck line NSH +1.5 | 65% | 1.53 | brak | - | średnia-niska |
| Puck line MIN +1.5 | 81% | 1.23 | brak | - | średnia |
| Total Under 6.5 | 57% (Poisson 61%, skorygowane o ogon) | 1.75 | 1.71 | -2% | średnia-niska |
| Total Under 7.5 | 74% | 1.35 | 1.27 | -6% | średnia-niska |
| Total Under 5.5 | 46% | 2.17 | 2.12 | -2% | niska |
| ML NSH | 40% | 2.49 | 2.65 | +6% | niska |

Typ: MIN ML to najsilniejszy kierunek ligi tej nocy, ale kurs 1.46 (poniżej fair 1.67) - brak EV. Pułap p 65-68% nieprzekroczony. Total Under 6.5 bez przewagi nad rynkiem. Ryzyka: Saros/Wallstedt w formie vs regresja PDO MIN, Gustavsson back (backup), gole w OT, pusta bramka.
Rynki zawodnika (Kaprizov, Boldy, Forsberg SOG): kombinacje z wygraną - **brak podstaw**.

---

## 4. Dallas Stars @ Vegas Golden Knights - 04:00 PL (18.11), Superbet 15592281
Gospodarze: Vegas (dom). B2B: brak.

**Bramkarze (niepotwierdzeni):** VGK Adin Hill (.907, 2.47), DAL Jake Oettinger (.902, 2.17). Stan Hill'a (wcześniejsze urazy sezonu) - sprawdzić.
**Statystyki:** VGK 13-6-3, GF 3,36 / GA 2,86, dom 7-4-1, L10 5-2-3. DAL 12-6-2 (sportbusy: 12-6-2), GF 2,80 / GA 2,50, wyjazd 4-1-2 (GA 13 w 7 m.), L10 6-3-1.
**Kontuzje:** DAL - Heiskanen DTD (najważniejszy; -0,15 gola obrona), Myers DTD, Duchene/Back/Bichsel/Capobianco IR. VGK - Hanifin out. Kontuzje obrońców po obu stronach (VGK bez Hanifina -0,05).
**Oczekiwane gole:** VGK 3,05 - DAL 2,75 (5,8).
**Rynek:** 1X2 VGK 2,20 / X 3,85 / DAL 2,72; ML VGK 1,72, DAL 2,10 (no-vig VGK 55%); total Over 5,5 1,82 / Under 1,97; Over 6,5 2,25 / Under 1,62.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| ML VGK (z OT) | 55% | 1.82 | 1.72 | -5% | średnia-niska |
| ML DAL | 45% | 2.22 | 2.10 | -5% | niska |
| 60' VGK | 46% | 2.15 | 2.20 | +2% | niska |
| Puck line DAL +1.5 | 70% | 1.43 | brak | - | średnia-niska |
| Total Under 6.5 | 61% (skoryg. 58%) | 1.72 | 1.62 | -6% | niska |
| Total Under 5.5 | 48% | 2.09 | 1.97 | -6% | niska |
| Total Over 5.5 | 52% | 1.92 | 1.82 | -5% | niska |

Typ: **brak mocnego typu** (wyrównane). Ryzyka: Heiskanen status (jeśli out: DAL λ -0,15 i total w górę), Hill rotacja.
Rynki zawodnika: **brak podstaw**.

---

## 5. Calgary Flames @ San Jose Sharks - 04:00 PL (18.11), Superbet 15586968
Gospodarze: San Jose (dom). B2B: brak.

**Bramkarze (niepotwierdzeni):** SJS Yaroslav Askarov (.890, 3.22; Nedeljkovic alternatywa; Keyser IR), CGY Dustin Wolf (.875, 3.58 - poniżej oczekiwań).
**Statystyki:** SJS 10-11-2, GF 2,74 / GA 3,52, dom 5-5-1, L10 4-5-1, seria W2; CGY 9-11-1, GF 2,43 / GA 3,52, wyjazd 3-6-1 (GA 38 w 10 m.), L10 4-5-1. Obie drużyny z najsłabszych defensyw.
**Kontuzje:** CGY - Huberdeau IR, Bahl IR, Zary out. SJS - Wennberg DTD, Sherwood DTD, Chernyshov/Musty/Keyser IR.
**Oczekiwane gole:** SJS 3,1 - CGY 2,85 (5,95). Celebrini dobrze w sezonie, ale deficyt defensywny.
**Rynek:** 1X2 SJS 2,20 / X 3,85 / CGY 2,67; ML SJS 1,78, CGY 2,02 (no-vig SJS 53%); total Over 5,5 1,75 / Under 5,5 2,05; Over 6,5 2,15 / Under 6,5 1,69.

| Rynek | p | fair | kurs | EV | Pewność |
|---|---|---|---|---|---|
| ML SJS (z OT) | 54% | 1.85 | 1.78 | -4% | niska |
| ML CGY | 46% | 2.18 | 2.02 | -7% | niska |
| 60' SJS | 46% | 2.19 | 2.20 | 0% | niska |
| Puck line CGY +1.5 | 70% | 1.43 | brak | - | niska |
| Total Over 5.5 | 55% | 1.83 | 1.75 | -4% | niska |
| Total Under 6.5 | 58% | 1.72 | 1.69 | -2% | niska |
| Total Over 4.5 | 74% | 1.35 | 1.23 | -9% | niska |

Typ: **brak mocnego typu**. Ryzyka: obaj bramkarze poniżej średniej (wynik bardzo losowy), zmiana bramkarza, gole w OT.
Rynki zawodnika: **brak podstaw**.

---

## Podsumowanie nocy
- Żaden mecz nie ma typu z dodatnim EV i p >= 55% przy kursie >1.2: kursy Superbet są zbliżone do mojej wyceny lub krótsze.
- Najwyższe p: MIN ML 60% (kurs 1.46, EV -12%), TOR ML 57% (1.63, -7%), VGK ML 55% (1.72, -5%). Puck line +1.5 dla underdogów p 65-79%, ale fair 1.23-1.53 i brak kursów w pobranych rynkach Superbet (sprawdzić w kuponie).
- Jedyne formalne +EV: ANA ML (+4%, kurs 2.17) i ANA 60' (+11% przy 2.80; warunkowe wobec Binnington/Hofer, pewność niska), NSH ML (+6%, 2.65, niska).
- Rynki zawodnika: brak podstaw (tylko kombinacje z wygraną drużyny, brak niezależnych średnich).
- Pewność ograniczona przez niepotwierdzonych bramkarzy; po ~16:00 CET warto sprawdzić Daily Faceoff i przeliczyć MIN, STL, DAL (Heiskanen) w pierwszej kolejności.

To są oszacowania probabilistyczne, nie gwarancje.
