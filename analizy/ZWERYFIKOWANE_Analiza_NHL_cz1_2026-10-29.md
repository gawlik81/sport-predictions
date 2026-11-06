# Analiza NHL cz. 1 - 29/30.10.2026 (czas polski, CET = UTC+1)

Sprawdzono: 29.10.2026, bramkarze wg Daily Faceoff (WebFetch) - skład i bramkarz mogą się zmienić do rozpoczęcia meczu. Statystyki: NHL.com (standings, goalie leaders, landing zawodnika) przez MCP `sportsdata`. Kursy: Pinnacle (MCP, kursy amerykańskie przeliczone, marża usunięta proporcjonalnie). BettingPros i Linemate nie użyte (brak klucza/sesji w tym zadaniu). Wszystkie liczby to oszacowania probabilistyczne, nie gwarancje.

Uwagi metodyczne:
- Początek sezonu (10-14 meczów): próbka mała, GF/GA regresowane do ~3,0 gola na drużynę.
- Poisson zaniża remisy po 60'. Rynek 60' (3-way) skorygowałem do remisu ~19% (Pinnacle wycenia remis na 20-21%); ML z dogrywką liczony wprost ze skryptu.
- Nie znaleziono ogólnodostępnego injury reportu z 29.10.2026 (WebSearch zwrócił tylko stare wpisy), więc kontuzje poza bramkarzami NIE są zweryfikowane - obniża to pewność każdego meczu.
- Rynki zawodnika: tylko jedno źródło (NHL.com), bez drugiego niezależnego, więc zgodnie z regułą skilla: niska pewność, nie na kupon.

## Tabela zbiorcza (własne p, rynek z dogrywką = ML, total = regulamin + gol w OT)

| # | Mecz (PL czas) | ML (z OT) | 60' (1 / X / 2) | Puck line | Total | Pewność |
|---|---|---|---|---|---|---|
| 1 | Winnipeg @ Tampa Bay (00:00) | TBL 63,7% (fair 1,57) | 53,4 / 19 / 27,6 | WPG +1,5 61,2% (1,63); TBL -1,5 38,8% (2,58) | 5,5: O 54,6% / U 45,4%; 6,5: U 58,5% | średnia |
| 2 | Utah @ Pittsburgh (00:00) | UTA 54,7% (1,83) | PIT 36,2 / 19 / UTA 44,9 | UTA +1,5 76,3% (1,31); PIT +1,5 68,5% (1,46) | 6,5: O 52,2% / U 47,8%; 7,5: U 65,8% | niska-średnia |
| 3 | Columbus @ Carolina (00:00) | CAR 68% (1,47) | CAR 57,5 / 19 / CBJ 23,5 | CAR -1,5 ~42% (2,38); CBJ +1,5 ~58% (1,72) | 5,5: O 53% / U 47%; 6,5: U 60,2% | średnia |
| 4 | Chicago @ Detroit (00:30) | DET 59,3% (1,69) | DET 49,3 / 19 / CHI 31,7 | CHI +1,5 66,4% (1,51); DET -1,5 33,6% (2,97) | 5,5: O 48% / U 52%; 6,5: U 64,9% | średnia |
| 5 | Boston @ St. Louis (01:00) | BOS 52,5% (1,91) | STL 38,1 / 19 / BOS 42,8 | BOS +1,5 71,6% (1,40); STL +1,5 75,6% (1,32) | 5,5: O 54,6% / U 45,4%; 6,5: U 58,3% | niska (brak mocnego typu) |
| 6 | Washington @ Nashville (01:00) | WSH 51,6% (1,94) | NSH 38,9 / 19 / WSH 42,1 | WSH +1,5 74,5% (1,34); NSH +1,5 71,8% (1,39) | 5,5: O 58,6% / U 41,4%; 6,5: U 54,2% | niska |

Kurs rynkowy Pinnacle (bez marży) dla porównania, ML z OT: TBL 65,7% / WPG 34,3%; UTA 55,0% / PIT 45,0%; CAR 69,4% / CBJ 30,6%; DET 58,7% / CHI 41,3%; STL 50,8% / BOS 49,2%; NSH 49,3% / WSH 50,7%. Linie: total TBL-WPG 6,0 (-110/-102), PIT-UTA 6,5 (-125/+111), CAR-CBJ 6,0 (-102/-110), DET-CHI 5,5 (-118/+105), STL-BOS 6,0 (-101/-111), NSH-WSH 6,5 (-102/-110). Żaden z moich ML nie odbiega od rynku o więcej niż ~4 pp, więc nie ma wyraźnego value na zwycięzcy; to są wyceny bazowe, nie okazje.

---

### 1. Tampa Bay Lightning - Winnipeg Jets (30.10, 00:00; 29.10 19:00 ET)
**Typ:** Tampa Bay ML (z dogrywką) | **p:** 63,7% | **Fair odds:** 1,57 | **Pewność:** średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: TBL / WPG | 63,7% / 36,3% | 1,57 / 2,76 | średnia |
| 60' 3-way: TBL / X / WPG | 53,4% / 19% / 27,6% | 1,87 / 5,3 / 3,62 | średnia |
| Puck line WPG +1,5 | 61,2% | 1,63 | niska-średnia |
| Puck line TBL +1,5 | 83,8% | 1,19 (granica 1,15-1,20) | średnia |
| Puck line TBL -1,5 | 38,8% | 2,58 | niska |
| Total 5,5 Under / Over | 45,4% / 54,6% | 2,20 / 1,83 | niska |
| Total 6,5 Under | 58,5% | 1,71 | niska |
**Statystyki drużyn:** TBL 11 meczów, 7-3-1, GF 38 / GA 34 (3,45 / 3,09), seria OT. WPG 12 meczów, 4-5-3, GF 28 / GA 36 (2,33 / 3,00), 3 wygrane w L10, seria 2 porażek, ostatnio 1-5 z FLA (27.10).
**H2H:** niska waga, nie badano szczegółowo.
**Bramkarze:** Vasilevskiy (TBL) potwierdzony, Skinner (WPG, SV% .911 w sezonie) potwierdzony - Daily Faceoff, 29.10. Brak zmiany λ względem średniej ligi poza lekkim plusem dla TBL.
**Informacje medialne:** WPG grał 27.10 (1 dzień przerwy), a jutro (30.10) gra na FLA - drugi dzień b2b jutro, więc dziś zwykle pierwszy mecz pary z Skinnerem. Connor: 9 goli w 12 meczach (17,3% SH% - nie do utrzymania). Kontuzje poza bramkarzami niesprawdzone.
**Oczekiwane gole:** TBL 3,40 - WPG 2,55 (łącznie 5,95). Rynek: team total TBL 3,5, WPG 2,5, total 6,0.
**Ryzyka:** wysoka losowość; mój ML TBL jest o 2 pp poniżej rynku (nie obniżałem dalej bez konkretów); gole w dogrywce; zmiana bramkarza.
**Rynek:** Pinnacle ML TBL -207 / WPG +184; PL TBL -1,5 +117 / WPG +1,5 -131; total 6,0 -110/-102; 60' TBL -127, X +364, WPG +263. WPG +1,5 (61% vs ~55% rynek) to jedyna różnica >5 pp - wymaga ostrożności, bo skrypt Poissona może zawyżać +1,5 przy niskim λ WPG.

### 2. Pittsburgh Penguins - Utah Mammoth (30.10, 00:00)
**Typ:** brak mocnego typu na zwycięzcę; najlepiej: Utah ML | **p:** 54,7% | **Fair odds:** 1,83 | **Pewność:** niska-średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: UTA / PIT | 54,7% / 45,3% | 1,83 / 2,21 | niska-średnia |
| 60' 3-way: PIT / X / UTA | 36,2% / 19% / 44,9% | 2,76 / 5,3 / 2,23 | niska |
| Puck line UTA +1,5 | 76,3% | 1,31 | średnia |
| Puck line PIT +1,5 | 68,5% | 1,46 | niska-średnia |
| Total 6,5 Over / Under | 52,2% / 47,8% | 1,92 / 2,09 | niska |
| Total 7,5 Under | 65,8% | 1,52 | niska |
**Statystyki drużyn:** UTA 13 meczów, 8-5-0, GF 47 / GA 43 (3,62 / 3,31), seria 1 porażki. PIT 12 meczów, 5-6-1, GF 40 / GA 40 (3,33 / 3,33), seria 2 wygranych, 3 wygrane w L10.
**H2H:** nie badano.
**Bramkarze:** Silovs (PIT, SV% .890 w sezonie) potwierdzony; Vejmelka (UTA) NIEPOTWIERDZONY (Daily Faceoff). Słaby SV% Silovsa zwiększa λ Utah o ok. +0,15; niepotwierdzony bramkarz Utah ogranicza pewność.
**Informacje medialne:** UTA grał 27.10 (porażka 1-3 z MIN u siebie), podróż do Pittsburgha. Kontuzje niesprawdzone.
**Oczekiwane gole:** PIT 3,15 - UTA 3,45 (łącznie 6,60). Rynek: total 6,5 over -125 (cena na Over), team totals PIT 3,5 (+130 O), UTA 3,5 (+104 O).
**Ryzyka:** Vejmelka niepotwierdzony; mecz wyrównany (p ~55/45); wysoki total zależy od słabego Silovsa.
**Rynek:** Pinnacle ML PIT +117 / UTA -129; PL UTA -1,5 +181 / PIT +1,5 -209; total 6,5 -125/+111; 60' PIT +173, X +338, UTA +119.

### 3. Carolina Hurricanes - Columbus Blue Jackets (30.10, 00:00)
**Typ:** Carolina ML (z dogrywką) | **p:** 68% | **Fair odds:** 1,47 | **Pewność:** średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: CAR / CBJ | 68% / 32% | 1,47 / 3,13 | średnia |
| 60' 3-way: CAR / X / CBJ | 57,5% / 19% / 23,5% | 1,74 / 5,3 / 4,26 | średnia |
| Puck line CAR -1,5 | ~42% | 2,38 | niska-średnia |
| Puck line CBJ +1,5 | ~58% | 1,72 | niska-średnia |
| Puck line CAR +1,5 | 86% | 1,16 (granica) | średnia |
| Total 5,5 Over / Under | 53% / 47% | 1,89 / 2,13 | niska |
| Total 6,5 Under | 60,2% | 1,66 | niska-średnia |
**Statystyki drużyn:** CAR 14 meczów, 10-2-2, 22 pkt, GF 53 / GA 34 (3,79 / 2,43), 8 wygranych w L10, seria 2 wygranych; najlepszy bilans w tej serii meczów. CBJ 10 meczów, 5-5-0, GF 26 / GA 33 (2,60 / 3,30), seria 2 wygranych (OT 27.10 w PHI).
**H2H:** nie badano.
**Bramkarze:** Greaves (CBJ) potwierdzony - prawdopodobnie rezerwowy (Talbot .894 w sezonie to numer 1; kto grał 27.10 niesprawdzone); Kochetkov (CAR, SV% .918) "likely". Rezerwowy CBJ dodaje CAR ok. +0,1 do λ.
**Informacje medialne:** CAR grał 27.10 (2-1 z BOS), 1 dzień przerwy; CBJ też 27.10 (2 dni). Kontuzje niesprawdzone.
**Oczekiwane gole:** CAR 3,50 - CBJ 2,40 (łącznie 5,90). Rynek: total 6,0, team total CAR 3,5, CBJ 2,5.
**Ryzyka:** moje 68% jest o 1,4 pp poniżej rynku (69,4%), więc brak value; Kochetkov tylko "likely"; CAR -1,5 zależy od pustej bramki.
**Rynek:** Pinnacle ML CAR -248 / CBJ +218; PL CAR -1,5 +104 / CBJ +1,5 -117; total 6,0 -102/-110; 60' CAR -148, X +377, CBJ +310.

### 4. Detroit Red Wings - Chicago Blackhawks (30.10, 00:30)
**Typ:** Detroit ML (z dogrywką) | **p:** 59,3% | **Fair odds:** 1,69 | **Pewność:** średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: DET / CHI | 59,3% / 40,7% | 1,69 / 2,46 | średnia |
| 60' 3-way: DET / X / CHI | 49,3% / 19% / 31,7% | 2,03 / 5,3 / 3,15 | średnia |
| Puck line CHI +1,5 | 66,4% | 1,51 | średnia |
| Puck line DET -1,5 | 33,6% | 2,97 | niska |
| Total 5,5 Under / Over | 52% / 48% | 1,92 / 2,08 | niska |
| Total 6,5 Under | 64,9% | 1,54 | niska-średnia |
**Statystyki drużyn:** DET 12 meczów, 5-4-3, GF 33 / GA 37 (2,75 / 3,08), seria 1 wygranej; ostatni mecz 26.10 w EDM (SO). CHI 12 meczów, 4-8-0, GF 26 / GA 44 (2,17 / 3,67) - najsłabsza obrona w tej serii meczów; seria 1 wygranej (2-1 z LAK 27.10).
**H2H:** nie badano.
**Bramkarze:** Gibson (DET) potwierdzony (Tarasov z .940 w sezonie to alternatywa); Knight (CHI, SV% .897) "likely". Słabe CHI + średni bramkarz.
**Informacje medialne:** DET ma 2-3 dni przerwy; CHI grał 27.10. Kontuzje niesprawdzone.
**Oczekiwane gole:** DET 3,05 - CHI 2,50 (łącznie 5,55). Rynek: total 5,5.
**Ryzyka:** CHI regresuje do średniej (GA 3,67 przesadza); Knight "likely"; niskie total sprzyja wariancji.
**Rynek:** Pinnacle ML DET -151 / CHI +136; PL DET -1,5 +165 / CHI +1,5 -189; total 5,5 -118/+105; 60' DET +105, X +336, CHI +200.

### 5. St. Louis Blues - Boston Bruins (30.10, 01:00)
**Typ:** brak mocnego typu (mecz wyrównany); lekko Boston ML | **p:** 52,5% | **Fair odds:** 1,91 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: BOS / STL | 52,5% / 47,5% | 1,91 / 2,10 | niska |
| 60' 3-way: STL / X / BOS | 38,1% / 19% / 42,8% | 2,62 / 5,3 / 2,34 | niska |
| Puck line BOS +1,5 | 71,6% | 1,40 | niska-średnia |
| Puck line STL +1,5 | 75,6% | 1,32 | niska-średnia |
| Total 5,5 Over / Under | 54,6% / 45,4% | 1,83 / 2,20 | niska |
| Total 6,5 Under | 58,3% | 1,72 | niska |
**Statystyki drużyn:** BOS 13 meczów, 9-3-1, GF 49 / GA 28 (3,77 / 2,15), 7 wygranych w L10, seria 1 porażki (1-2 w CAR 27.10); GA zawyżone przez gorącego Swaymana. STL 12 meczów, 5-6-1, GF 35 / GA 37 (2,92 / 3,08), seria 2 porażek (0-2 z MTL 27.10 u siebie).
**H2H:** nie badano.
**Bramkarze:** Swayman (BOS, SV% .921) potwierdzony; Hofer (STL, SV% .917) potwierdzony (Daily Faceoff; wpis o Hoferze miał błędny podgląd tekstu - status tylko wg listy). Dobrzy bramkarze po obu stronach.
**Informacje medialne:** obie drużyny grały 27.10 (1 dzień przerwy); STL w domu. Kontuzje niesprawdzone.
**Oczekiwane gole:** STL 2,90 - BOS 3,05 (łącznie 5,95). Rynek: total 6,0.
**Ryzyka:** rynek wycenia STL lekko wyżej (50,8%) mimo lepszych statystyk BOS; bez konkretów nie schodzę pod rynek; Boston GA 2,15 nie utrzyma się. Typ nie nadaje się na kupon.
**Rynek:** Pinnacle ML STL -109 / BOS -102; PL STL -1,5 +226 / BOS +1,5 -265; total 6,0 -101/-111; 60' STL +142, X +322, BOS +150.

### 6. Nashville Predators - Washington Capitals (30.10, 01:00)
**Typ:** brak mocnego typu (mecz wyrównany) | **p:** WSH 51,6% | **Fair odds:** 1,94 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: WSH / NSH | 51,6% / 48,4% | 1,94 / 2,07 | niska |
| 60' 3-way: NSH / X / WSH | 38,9% / 19% / 42,1% | 2,57 / 5,3 / 2,38 | niska |
| Puck line WSH +1,5 | 74,5% | 1,34 | niska-średnia |
| Puck line NSH +1,5 | 71,8% | 1,39 | niska-średnia |
| Total 5,5 Over | 58,6% | 1,71 | niska |
| Total 6,5 Under / Over | 54,2% / 45,8% | 1,84 / 2,18 | niska |
| Total 7,5 Under | 71,6% | 1,40 | niska |
**Statystyki drużyn:** WSH 11 meczów, 7-4-0, GF 39 / GA 34 (3,55 / 3,09), 2 wygrane z rzędu (5-2 z PHI 28.10). NSH 12 meczów, 4-3-5, GF 34 / GA 39 (2,83 / 3,25), tylko 3 wygrane w L10, seria OT/SO (porażka po SO z NYI 27.10).
**H2H:** nie badano.
**Bramkarze:** Saros (NSH, SV% .906) potwierdzony; Lindgren (WSH) NIEPOTWIERDZONY - to drugi dzień back-to-back dla WSH (grał 28.10 u siebie), więc Lindgren prawdopodobny, a Thompson (.903) mógł grać wczoraj. Ten sygnał uwzględniłem: λ WSH -0,1 (b2b) i brak premii za bramkarza; mimo to WSH wciąż lekko >50% przez siłę ataku.
**Informacje medialne:** NSH ma 2 dni przerwy (27.10), WSH b2b z podróżą. Tuch 9 goli, Stamkos i O'Reilly po 7 goli w sezonie. Kontuzje niesprawdzone.
**Oczekiwane gole:** NSH 3,05 - WSH 3,15 (łącznie 6,20). Rynek: total 6,5.
**Ryzyka:** niepotwierdzony bramkarz WSH; b2b może obniżyć WSH silniej niż -0,1; mój ML WSH 51,6% vs rynek 50,7% - brak przewagi.
**Rynek:** Pinnacle ML NSH -102 / WSH -108; PL WSH -1,5 +214 / NSH +1,5 -250; total 6,5 -102/-110; 60' NSH +147, X +347, WSH +137.

---

## Rynki zawodnika (niska pewność, jedno źródło - NHL.com; nie na kupon)

Zgodnie z regułą skilla (min. dwa niezależne źródła, potwierdzony skład/linia/PP): tylko dwa rynki dla jednego zawodnika, i to bez potwierdzonego składu.

| Zawodnik / mecz | Rynek | Średnia użyta | Linia | p | Fair | Pewność |
|---|---|---|---|---|---|---|
| Kyle Connor (WPG @ TBL) | Strzały Over | 3,8-4,0 (sezon 52 strzałów / 12 m. = 4,33; ostatnie 5: 3, 5, 3, 4, 2 = 3,4) | 3,5 | ~52-55% | ~1,85-1,95 | niska |
| Kyle Connor | Strzelec gola Over 0,5 | 0,42 (9 goli/12 m., SH% 17,3% regresowane do ~14%; kariera 0,47) | 0,5 | ~34% | 2,92 | niska |

Uwagi: Connor ma rolę na PP (4 gole z PP w sezonie, 21:21 TOI), ale brak potwierdzonego składu i drugiego źródła. Kolejne rynki zawodnika (strzały + punkty) są skorelowane. Brak rynków bramkarzy (obrony): bez statystyk strzałów na bramkę drużyn nie wyceniam ich; średnia ligi ~27 obron z odchyleniem ~5,9 jest tylko punktem odniesienia (Over 26,5 = 51,6% przy średniej 27).

---

## Ranking kandydatów (bez typów z fair odds ≤ 1,15; 1,15-1,20 oznaczone)

| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|
| CAR - CBJ | CAR ML (z OT) | 68% | 1,47 | średnia | Kochetkov (likely), Greaves (rezerwowy?) | Pinnacle -248 (fair rynku 1,44) - bez value |
| TBL - WPG | TBL ML (z OT) | 63,7% | 1,57 | średnia | potwierdzeni Vasilevskiy i Skinner | Pinnacle -207 (fair rynku 1,52) - bez value |
| DET - CHI | DET ML (z OT) | 59,3% | 1,69 | średnia | Knight "likely" | Pinnacle -151 (fair rynku 1,70) - neutralnie |
| DET - CHI | CHI +1,5 | 66,4% | 1,51 | średnia | j.w. | Pinnacle -189 (fair rynku ~1,53) - neutralnie |
| TBL - WPG | WPG +1,5 | 61,2% | 1,63 | niska-średnia | Skinner, b2b jutro | Pinnacle -131 (rynek ~55%) - różnica 6 pp, ostrożnie |
| TBL - WPG | TBL +1,5 | 83,8% | 1,19 (granica) | średnia | wynik 2+ goli dla WPG nie wymagany | Pinnacle -619 alt (brak value) |
| CAR - CBJ | CAR +1,5 | 86% | 1,16 (granica) | średnia | j.w. | brak ceny |
| PIT - UTA | UTA ML | 54,7% | 1,83 | niska-średnia | Vejmelka niepotwierdzony | Pinnacle -129 (fair rynku 1,82) - neutralnie |
| NSH - WSH | WSH ML | 51,6% | 1,94 | niska | Lindgren niepotwierdzony, b2b WSH | neutralnie |
| STL - BOS | BOS ML | 52,5% | 1,91 | niska | brak przewagi | neutralnie |

Wniosek: w tym bloku nie ma wyraźnego value względem Pinnacle. Mecze 5 i 6 są wyrównane (p 45-55%) i oznaczone jako brak mocnego typu. Mecze 1, 3, 4 mają potwierdzonych (lub "likely") bramkarzy i dają typy zwycięzcy o pewności średniej, ale po cenach rynkowych EV ≈ 0. Przy budowie kuponu (`bet-slip-builder`) potrzebne są kursy Betclic.pl; kursy tutaj to tylko Pinnacle.

Brakujące dane do uzupełnienia przed kuponem: injury report 29.10, potwierdzenie Vejmelki (UTA), Lindgrena (WSH), Kochetkova (CAR), Knighta (CHI) po rozjazdach porannych, kursy Betclic, drugie źródło do rynków zawodnika.
