# Analiza NHL - 30/31.10.2026 (czas polski, CET = UTC+1)

Sprawdzono: 30.10.2026 rano. Dane: NHL.com (standings, goalie leaders, club-stats przez MCP `sportsdata` i WebFetch), Daily Faceoff (bramkarze), ESPN (injuries), Pinnacle (MCP; tylko Vegas-NJ i Calgary-Seattle miały wystawiony rynek), BettingPros (API, klucz działa; rynki meczowe wszystkich 9 meczów, ale rynki zawodnika/props jeszcze NIE wystawione, a w best_lines dla 4 meczów brak nazw stron - patrz uwagi). Skład i bramkarz mogą się zmienić do rozpoczęcia meczu.

## Uwagi metodyczne

- **Bramkarze: 0 z 26 potwierdzonych** (Daily Faceoff 30.10 i 31.10: wszyscy "Unconfirmed"). Wszystkie liczby mają więc co najwyżej pewność niską-średnią; rynki bramkarza i zawodnika nie wchodzą na kupon. Sprawdzić ponownie po porannym skate (ok. 3-5 h przed meczem).
- Początek sezonu (12-14 meczów): GF/GA regresowane ok. 50% do 3,0 gola; potem korekty o bramkarza (SV% sezonu regresowane do ~.900), kontuzje (ESPN) i back-to-back.
- **Poisson zaniża remis po 60'** (skrypt ok. 16-17%; Pinnacle wycenia ok. 23% po usunięciu marży). W tabelach 60' przeskalowałem remis do 23%. ML z dogrywką liczony wprost ze skryptu.
- **Puck line:** skrypt nie uwzględnia pustych bramek, więc dla strony -1.5 dodałem +3 pp, a dla +1.5 odjąłem 3 pp (korekta zgodna z rynkiem: Pinnacle VGK-NJ i CGY-SEA).
- Kolejne rynki tego samego meczu i zawodnika są skorelowane (nie łączyć w jednym kuponie).
- BettingPros: w best_lines dla TBL@NSH, EDM@NYI, BUF@LAK, OTT@SJS brak nazw stron ML/PL, więc znak faworyta jest wnioskowany (oznaczone "~"); używać tylko orientacyjnie.
- Rynki zawodnika: jedno źródło liczb (NHL.com, 12-14 meczów) + brak linii bukmachera, więc **pewność niska, nie rekomenduję na kupon**. Podaję p dla typowych linii; fair odds do porównania z kursem po wystawieniu.

## Tabela zbiorcza (ML = z dogrywką; total = regulamin + gol w OT)

| # | Mecz (PL czas) | λ gosp - gość (suma) | ML (z OT) | 60' 1 / X / 2 | Puck line (po korekcie) | Total | Pewność |
|---|---|---|---|---|---|---|---|
| 1 | Vegas - New Jersey (pt 23:00) | 3,15 - 2,90 (6,05) | VGK 53% (1,89) / NJ 47% (2,13) | 42,1 / 23 / 34,9 | VGK -1,5 33,0% (3,03); NJ +1,5 67,0% (1,49) | O5,5 56,2% / U6,5 56,7% | niska-średnia |
| 2 | Florida - Winnipeg (sob 31.10 00:00) | 3,15 - 2,55 (5,70) | FLA 61% (1,64) / WPG 39% (2,56) | 47,4 / 23 / 29,5 | FLA -1,5 37,6% (2,66); WPG +1,5 62,4% (1,60) | U6,5 ~58% (1,72); O5,5 50,5% | niska |
| 3 | Calgary - Seattle (sob 01:00) | 3,10 - 3,30 (6,40) | SEA 52,5% (1,90) / CGY 47,5% (2,11) | 35,9 / 23 / 41,6 | SEA -1,5 32,8% (3,05); CGY +1,5 67,2% (1,49) | O6,5 49,0% / U6,5 51,0% | niska |
| 4 | Boston - Chicago (sob 18:00) | 3,40 - 2,45 (5,85) | BOS 65% (1,54) / CHI 35% (2,86) | 52,7 / 23 / 24,7 | BOS -1,5 43,1% (2,32); CHI +1,5 56,9% (1,76) | U6,5 ~59% (1,69) | niska-średnia |
| 5 | Detroit - St. Louis (sob 18:00) | 2,75 - 2,80 (5,55) | DET 50% / STL 50% (2,00) | 37,7 / 23 / 39,2 | DET +1,5 70,7%; STL +1,5 72,1% | U6,5 ~62% (1,61); U5,5 52,0% | niska (brak typu) |
| 6 | Nashville - Tampa Bay (sob 19:00) | 2,95 - 3,30 (6,25) | TBL 56% (1,79) / NSH 44% (2,27) | 34,0 / 23 / 43,0 | TBL -1,5 ~32%; NSH +1,5 ~68% | O5,5 ~58% (1,72); U6,5 ~54% | niska |
| 7 | NY Islanders - Edmonton (sob 19:00) | 3,10 - 3,10 (6,20) | 50 / 50 (2,00) | 38,5 / 23 / 38,5 | NYI/EDM +1,5 70,2% | O5,5 ~57% (1,75); U6,5 ~54% | niska (brak typu) |
| 8 | Los Angeles - Buffalo (sob 21:00) | 3,05 - 3,20 (6,25) | BUF 52,4% (1,91) / LAK 47,6% (2,10) | 36,4 / 23 / 40,8 | BUF -1,5 31,9%; LAK -1,5 27,9% | O5,5 ~58% (1,72) | niska |
| 9 | San Jose - Ottawa (sob 21:00) | 3,25 - 3,00 (6,25) | SJS 52% (1,92) / OTT 48% (2,08) | 42,2 / 23 / 35,0 | SJS -1,5 33,3%; OTT +1,5 66,7% | O5,5 ~58% (1,72); U6,5 ~54% | niska |

Kursy: Pinnacle (meczów 1 i 3, kursy amerykańskie przeliczone): ML VGK -114 / NJ +101; PL VGK -1,5 +217 / NJ +1,5 -260; total 6,0 -111/-104 (alt 5,5 O -139, 6,5 U -131); 60' VGK +137 / X +311 / NJ +155. CGY -101 / SEA -111; PL SEA -1,5 +218 / CGY +1,5 -261; total 6,5 -101/-113; 60' CGY +150 / X +319 / SEA +139. BettingPros (best lines): FLA -203 / WPG +203, total 5,5 O -133, U6,5 -125, WPG +1,5 -121; BOS -212 / CHI +213, U6,5 -122, CHI +1,5 -122; DET/STL -104/+104, U6,5 -163; ~TBL -163 / NSH +150, U6,5 -127; EDM-NYI -113/+117, U6,5 -127; BUF-LAK +108/-108, U6,5 -127; OTT-SJS +-127, U6,5 -117.

---

### 1. Vegas Golden Knights - New Jersey Devils (pt 30.10, 23:00; 15:00 PT)
**Typ:** brak mocnego typu | **Najlepszy rynek:** Under 6,5 (z OT) | **p:** 56,7% | **Fair:** 1,76 | **Pewność:** niska-średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: VGK / NJ | 53% / 47% | 1,89 / 2,13 | niska-średnia |
| 60' 3-way: VGK / X / NJ | 42,1% / 23% / 34,9% | 2,38 / 4,35 / 2,87 | niska |
| PL VGK -1,5 / NJ +1,5 | 33,0% / 67,0% | 3,03 / 1,49 | niska |
| PL VGK +1,5 / NJ -1,5 | 73,7% / 20,3% | 1,36 / 4,93 | niska |
| Total 5,5 Over / Under | 56,2% / 43,8% | 1,78 / 2,28 | niska-średnia |
| Total 6,5 Over / Under | 43,3% / 56,7% | 2,31 / 1,76 | niska-średnia |
| Shots Eichel (VGK) O2,5 | 53,5% | 1,87 | niska (linia nieznana) |
| Shots J. Hughes / Meier (NJ) O3,5 | 43,3% | 2,31 | niska |
**Statystyki drużyn:** VGK 9-4-1, GF 3,64 / GA 2,79, seria 1 W; NJD 8-5-0, 3,31 / 2,92, 7 W w L10, przegrany 2:5 z COL (28.10). Special teams: Hertl 3 PPG, Hischier 4 PPG.
**H2H:** nie badano (niska waga).
**Bramkarze (Daily Faceoff, 30.10, niepotwierdzeni):** NJ Hellebuyck (1 GP, .944, próbka znikoma; Allen .887 8 GP) vs VGK Hill (.895; Hart DTD, .889). Zakładam Hellebuyck jako niepewny: -0,1 do -0,15 dla λ VGK.
**Informacje medialne:** NJD 3. mecz w 4 nocach (27, 28.10, dziś; wolne 29.10, brak b2b), podróż przez strefy. VGK 2 dni odpoczynku. ESPN: Hart DTD, Wotherspoon IR; NJ Casey IR.
**Oczekiwane gole:** VGK 3,15 - NJ 2,90 (6,05). Rynek Pinnacle: team total VGK 3,5 O +134, NJ 2,5 O -160 (zbieżne).
**Ryzyka:** nieznany bramkarz NJ (Hellebuyck vs Allen to ok. 0,3 gola różnicy), Hart DTD, gol w OT.
**Rynek:** mój ML VGK 53% vs Pinnacle 51,7%: zgodne. Under 6,5 -131 (fair 1,76) = EV ~0. Brak wartości.

### 2. Florida Panthers - Winnipeg Jets (sob 31.10, 00:00; 30.10 19:00 ET)
**Typ:** Florida ML (z OT) | **p:** 61% | **Fair:** 1,64 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: FLA / WPG | 61% / 39% | 1,64 / 2,56 | niska |
| 60' 3-way: FLA / X / WPG | 47,4% / 23% / 29,5% | 2,11 / 4,35 / 3,39 | niska |
| PL FLA -1,5 / WPG +1,5 | 37,6% / 62,4% | 2,66 / 1,60 | niska |
| PL FLA +1,5 | 78,6% | 1,27 | niska |
| Total 5,5 Over / Under | 50,5% / 49,5% | 1,98 / 2,02 | niska |
| Total 6,5 Under | ~58% (model 62,5%, skorygowane o rozrzut) | 1,72 | niska |
| Shots Connor (WPG) O3,5 | 53,0% | 1,89 | niska (b2b, linia nieznana) |
| Goals Connor (WPG) strzelec | 34,3% | 2,92 | niska |
| Shots B. Tkachuk (FLA) O2,5 | 55,6% | 1,80 | niska |
**Statystyki drużyn:** FLA 7-4-2, GF 3,00 / GA 2,85, wygrali 5:1 z WPG (27.10). WPG 4-6-3, GF 2,46 / GA 3,23, 2 W w L10, seria 3 porażek. Connor 10 goli / 55 strzałów (SH% 18% nie do utrzymania).
**H2H:** 27.10 FLA 5:1 WPG.
**Bramkarze (niepotwierdzeni):** WPG Daws (.885 / .872 wg club-stats; 2-2) bo Skinner grał 29.10 w TBL; FLA Schmid (.885; Markstrom IR). Obaj poniżej średniej: oba λ +0,1.
**Informacje medialne:** **WPG drugi dzień b2b** (29.10 6:4 przegrana w TBL, podróż na Florydę): -0,12 do λ WPG. ESPN: FLA bez Barkova (IR), Marchanda, Markstroma; WPG bez Morrisseya (obrona), Bjugstada, Namestnikova.
**Oczekiwane gole:** FLA 3,15 - WPG 2,55 (5,70).
**Ryzyka:** słabi bramkarze obu stron podnoszą total; FLA osłabiona (brak Barkova), rynek ją wycenia wyżej (-203 = ok. 64-65%).
**Rynek:** BettingPros best: FLA -203 (1,49) vs fair 1,64 = brak value; Under 6,5 -125 (1,80) vs fair 1,72 = EV ~+4% (jedna linia, niska pewność).

### 3. Calgary Flames - Seattle Kraken (sob 31.10, 01:00; 30.10 18:00 MT)
**Typ:** brak mocnego typu (Seattle ML niska) | **p:** 52,5% | **Fair:** 1,90 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: SEA / CGY | 52,5% / 47,5% | 1,90 / 2,11 | niska |
| 60' 3-way: CGY / X / SEA | 35,9% / 23% / 41,6% | 2,79 / 4,35 / 2,40 | niska |
| PL SEA -1,5 / CGY +1,5 | 32,8% / 67,2% | 3,05 / 1,49 | niska |
| PL SEA +1,5 / CGY -1,5 | 75,5% (72,4% po korekcie) / 27,6% | 1,38 / 3,62 | niska |
| Total 5,5 Over / Under | 61,6% / 38,4% | 1,62 / 2,61 | niska |
| Total 6,5 Over / Under | 49,0% / 51,0% | 2,04 / 1,96 | niska |
| Shots McMann (SEA) O2,5 | 61,7% (śr. 3,0 -> 55,6%) | 1,80 | niska |
**Statystyki drużyn:** CGY 5-7-0, GF 2,33 / GA 3,75, 5 W w L10 (rozjazd), 0:4 z EDM 28.10. SEA 8-4-1, GF 3,85 / GA 3,54, 5:4 z TOR 28.10. Mecze Seattle są wysokie (GA 3,5).
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** CGY Wolf (.839, 1-4-0, 4,81 GAA - regresja do ~.895 w modelu) lub Cooley (.914, DTD); SEA Daccord (.882, 3,95 GAA) lub Grubauer (.898). Bramkarze obu stron słabi - rynek niespójny, duża wariancja.
**Informacje medialne:** obie 1 dzień odpoczynku (CGY grał 28.10 w EDM, SEA 28.10 u siebie). ESPN: CGY bez Huberdeau (IR), Cooley/Othmann DTD; SEA bez McCanna (IR), Lindgrena, O'Briena.
**Oczekiwane gole:** CGY 3,10 - SEA 3,30 (6,40).
**Ryzyka:** nieznany bramkarz po obu stronach (każda zmiana = +/-0,3 gola), CGY niska ofensywa vs wysokie GA SEA.
**Rynek:** Pinnacle SEA -111 (50,9% -> novig 51,1%) vs mój 52,5%: zgodne; total 6,5 -101/-113 vs mój O 49,0%: zgodne. SEA -1,5 +218 (fair 3,05) = EV ~+4%, w granicy błędu - nie rekomenduję.

### 4. Boston Bruins - Chicago Blackhawks (sob 31.10, 18:00; 13:00 ET)
**Typ:** Boston ML (z OT) | **p:** 65% | **Fair:** 1,54 | **Pewność:** niska-średnia
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: BOS / CHI | 65% / 35% | 1,54 / 2,86 | niska-średnia |
| 60' 3-way: BOS / X / CHI | 52,7% / 23% / 24,7% | 1,90 / 4,35 / 4,05 | niska-średnia |
| PL BOS -1,5 / CHI +1,5 | 43,1% / 56,9% | 2,32 / 1,76 | niska |
| PL BOS +1,5 | 82,5% | 1,21 | średnia |
| Total 5,5 Over / Under | ~46% / ~54% (po podniesieniu totalu do 5,85) | 2,17 / 1,85 | niska |
| **Total 6,5 Under** | ~59% | 1,69 | niska-średnia |
| Shots Pastrnak (BOS) O3,5 | ~43,3% (śr. 3,4) | 2,31 | niska |
| Goals Pastrnak strzelec | 33% | 3,03 | niska |
| Saves Swayman (BOS) O23,5 / O24,5 | 53,8% / 46,7% (śr. 24,3) | 1,86 / 2,14 | niska (niepotwierdzony) |
**Statystyki drużyn:** BOS 9-4-1, GF 3,57 / GA 2,29 (najlepsza obrona z tej puli), L10 7 W, seria 2 porażek (1:2 CAR, 1:4 STL 29.10). CHI 4-9-0, GF 2,08 / GA 3,69 (najgorsze GF i GA), 1:4 z DET 29.10. Pastrnak 7 G, 18 pkt w 14 meczach.
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** BOS Swayman (.912, 2,35 GAA; DiPietro .941 3 GP), CHI Knight (.897; 340 strzałów w 11 meczach = 31/mecz).
**Informacje medialne:** obie grały 29.10 (1 dzień przerwy), CHI w podróży z Detroit. ESPN: CHI bez Byrama (Out); Bedard wrócił (7 GP, 3 G). BOS bez wpisów w injury report.
**Oczekiwane gole:** BOS 3,40 - CHI 2,45 (5,85).
**Ryzyka:** BOS dwie porażki z rzędu przy 1 golu (słaba ofensywa ostatnio, ale forma faworyta jest w kursie); wyjście DiPietro; CHI ma wysokie GA = ryzyko Over.
**Rynek:** BettingPros best: BOS -212 (1,47; novig ok. 67%) -> mój ML bez value; Under 6,5 best -122 (1,82) vs fair 1,69 = EV ok. +7% (jedna linia best, konsensus nieznany; różnica do rynku ok. 5 pp). CHI +1,5 -122 (1,82) vs fair 1,76 = EV +3%: za mało.

### 5. Detroit Red Wings - St. Louis Blues (sob 31.10, 18:00; 13:00 ET)
**Typ:** brak mocnego typu (mecz wyrównany) | **p:** 50% | **Fair:** 2,00 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: DET / STL | 49,1% -> 50% / 50% | 2,00 | niska |
| 60' 3-way: DET / X / STL | 37,7% / 23% / 39,2% | 2,65 / 4,35 / 2,55 | niska |
| PL DET -1,5 / STL -1,5 | 27,9% / 29,3% | 3,58 / 3,41 | niska |
| PL DET +1,5 / STL +1,5 | 70,7% / 72,1% | 1,41 / 1,39 | niska |
| Total 5,5 Over / Under | 48,0% / 52,0% | 2,08 / 1,92 | niska |
| Total 6,5 Under | ~62% (model 64,8%) | 1,61 | niska |
| Shots DeBrincat (DET) O3,5 | ~47% (śr. 3,5) | 2,11 | niska |
| Saves Hofer (STL) O25,5 / O26,5 | 52,3% / 45,4% (śr. 26,1) | 1,91 / 2,20 | niska (niepotwierdzony) |
**Statystyki drużyn:** DET 6-4-3, GF 2,85 / GA 2,92, 2 W seria, 4:1 z CHI (29.10). STL 6-6-1, GF 3,00 / GA 2,92, 4:1 z BOS (29.10). Wyrównane ofensywy, obrony.
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** DET Gibson (.874, 9 GP) lub Tarasov (.940 w 4 GP, 1,40 GAA); STL Hofer (.923, 2,24 GAA - najlepszy z tej pary). Gibson słaby -> +0,1 dla STL, Hofer dobry -> -0,1 dla DET (wliczone).
**Informacje medialne:** obie 29.10 (1 dzień przerwy); STL w podróży. ESPN: DET bez Larkina, Kaspera, Appletona, Edvinssona (spór kontraktowy), A. Johanssona (Out) = -0,2 gola; STL bez Kruga, Dube, Tuckera, Mailloux.
**Oczekiwane gole:** DET 2,75 - STL 2,80 (5,55).
**Ryzyka:** wybór bramkarza DET (Gibson vs Tarasov) zmienia wynik o ok. 0,3 gola; rotacja po b2b.
**Rynek:** BettingPros best: DET -104 / STL +104 (zgodne z 50/50); Under 6,5 -163 (1,61) = fair 1,61, EV ~0. Brak wartości.

### 6. Nashville Predators - Tampa Bay Lightning (sob 31.10, 19:00; 14:00 CT)
**Typ:** brak mocnego typu; najlepszy: Tampa Bay ML | **p:** 56% | **Fair:** 1,79 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: TBL / NSH | 56% / 44% | 1,79 / 2,27 | niska |
| 60' 3-way: NSH / X / TBL | 34,0% / 23% / 43,0% | 2,94 / 4,35 / 2,33 | niska |
| PL TBL -1,5 / NSH +1,5 | ~32% / ~68% | 3,1 / 1,47 | niska |
| Total 5,5 Over / Under | ~58% / ~42% | 1,72 / 2,38 | niska |
| Total 6,5 Over / Under | ~46% / ~54% | 2,17 / 1,85 | niska |
| Shots Hagel (TBL) O3,5 / O4,5 | 60,2% / 42,4% (śr. 4,3 z 4,58) | 1,66 / 2,36 | niska (linia nieznana) |
| Shots Josi (NSH) O2,5 | ok. 65% (35/13 = 2,7) | ~1,55 | niska |
| Goals Stamkos / O'Reilly (NSH) strzelec | ~30% | 3,3-3,4 | niska |
**Statystyki drużyn:** TBL 8-3-1, GF 3,67 / GA 3,17, 6:4 z WPG (29.10), 7 W w L10. NSH 4-4-5, GF 2,85 / GA 3,31, 3 W w L10, 3:4 z WSH (29.10). NSH PP mocny (O'Reilly 4 PPG, Forsberg/Stamkos po 3).
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** TBL Vasilevskiy (.876, 2,91 GAA; słaby start sezonu, Hildeby .885); NSH Saros (.902). Oba poniżej klasy - total w górę.
**Informacje medialne:** obie 29.10 (1 dzień przerwy), NSH u siebie. ESPN: TBL bez Girgensonsa (Out), Gourde (IR); NSH bez wpisów.
**Oczekiwane gole:** NSH 2,95 - TBL 3,30 (6,25).
**Ryzyka:** wybór bramkarza TBL; ML TBL rynek ok. -163 (59%) - wyżej niż mój model; brak wiarygodnych dodatkowych źródeł.
**Rynek:** BettingPros ~TBL -163 (1,61) vs fair 1,79: brak value; ~Under 6,5 -127 (1,79) vs fair 1,85: brak.

### 7. New York Islanders - Edmonton Oilers (sob 31.10, 19:00; 14:00 ET)
**Typ:** brak mocnego typu | **p:** 50% | **Fair:** 2,00 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: NYI / EDM | 50% / 50% | 2,00 | niska |
| 60' 3-way: NYI / X / EDM | 38,5% / 23% / 38,5% | 2,60 / 4,35 / 2,60 | niska |
| PL NYI +1,5 / EDM +1,5 | 70,2% / 70,2% | 1,42 | niska |
| Total 5,5 Over / Under | ~57% / ~43% | 1,75 / 2,33 | niska |
| Total 6,5 Over / Under | ~46% / ~54% | 2,17 / 1,85 | niska |
| Points McDavid (EDM) O0,5 / O1,5 | 77% / 45% (śr. 1,55 pkt; sezon 2,8) | 1,30 / 2,2 | niska |
| Points Draisaitl (EDM) O0,5 / O1,5 | 75,7% / 42,2% (śr. 1,45) | 1,32 / 2,37 | niska |
| Goals Draisaitl strzelec | 36,2% (sezon 12 G, SH% 25% regresowane) | 2,76 | niska |
| Shots Draisaitl O3,5 | 47% (śr. 3,6) | 2,1 | niska |
| Shots Schaefer (NYI) O3,5 / O2,5 | 49,3% / 68,8% (śr. 3,7; 27 min TOI) | 2,03 / 1,45 | niska |
| Saves Sorokin (NYI) O25,5 | 55,0% (śr. 26,5) | 1,82 | niska (niepotwierdzony) |
**Statystyki drużyn:** NYI 7-4-2, GF 3,08 / GA 2,69, 6 W w L10, 4:3 z MIN (29.10). EDM 9-2-2, GF 4,31 (najlepsza ofensywa) / GA 3,31, 4:0 z CGY (28.10). Draisaitl 12 G / 6 PPG, McDavid 36 pkt w 13 meczach.
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** NYI Sorokin (.915, 2,34 GAA), EDM Jarry (.889; Levi IR, Andersen IR). Przewaga bramkarska NYI ok. 0,25 gola, ale EDM ofensywnie dużo lepsza.
**Informacje medialne:** EDM 2 dni odpoczynku, NYI 1 dzień po MIN. ESPN: NYI bez Barzala (IR), Maccellego, Romanova; Pulock DTD. EDM bez Hymana (IR).
**Oczekiwane gole:** NYI 3,10 - EDM 3,10 (6,20).
**Ryzyka:** wszystkie rynki zawodnika EDM zależą od Draisaitla i McDavida (potwierdzenie zdrowia i PP); średnie sezonu zawyżone przez wysokie SH%.
**Rynek:** BettingPros best -113 / +117 (pick'em); Under 6,5 -127 (1,79) vs fair 1,85: brak value.

### 8. Los Angeles Kings - Buffalo Sabres (sob 31.10, 21:00; 13:00 PT)
**Typ:** brak mocnego typu | **p:** 52,4% (BUF) | **Fair:** 1,91 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: LAK / BUF | 47,6% / 52,4% | 2,10 / 1,91 | niska |
| 60' 3-way: LAK / X / BUF | 36,4% / 23% / 40,8% | 2,75 / 4,35 / 2,45 | niska |
| PL LAK -1,5 / BUF -1,5 | 27,9% / 31,9% | 3,58 / 3,13 | niska |
| PL LAK +1,5 / BUF +1,5 | 68,1% / 72,1% | 1,47 / 1,39 | niska |
| Total 5,5 Over / Under | ~58% / ~42% | 1,72 / 2,38 | niska |
| Total 6,5 Over / Under | ~46% / ~54% | 2,17 / 1,85 | niska |
| Shots Thompson (BUF) O3,5 | 54,9% (śr. 4,0 z 4,23) | 1,82 | niska |
| Goals Thompson strzelec | ~31,6% (0,38) | 3,16 | niska |
| Shots Kempe (LAK) O2,5 / O3,5 | 61,7% / 41,3% (śr. 3,3) | 1,62 / 2,42 | niska |
**Statystyki drużyn:** LAK 4-6-2, GF 2,83 / GA 3,50, 6:5 z OTT (29.10). BUF 6-4-3, GF 3,08 / GA 3,62, 7:6 z ANA (29.10). Obie obrony przeciekają; Thompson 8 G / 55 strzałów.
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** LAK Kuemper (.878, 3,65 GAA; Forsberg .902 5 GP); BUF Ellis (.880; Luukkonen .866; Lyon IR). Oba bramkarze słabi -> total w górę, +0,1-0,15 dla ataku rywala.
**Informacje medialne:** obie 29.10 (1 dzień przerwy); BUF z ANA (krótka podróż). ESPN: LAK bez Fiali, Zuccarello (-0,25 gola), Clarke DTD; BUF bez Kulicha (Out, wstrząs), Helenius (Out), Danforth, Timminsa.
**Oczekiwane gole:** LAK 3,05 - BUF 3,20 (6,25).
**Ryzyka:** duża wariancja (słabi bramkarze), mecz wyjazdowy BUF po meczu w ANA, brak potwierdzonych linii.
**Rynek:** BettingPros best +108 / -108 (pick'em), Under 6,5 -127: brak value dla Under; Over 5,5 nieskonfrontowany z kursem.

### 9. San Jose Sharks - Ottawa Senators (sob 31.10, 21:00; 13:00 PT)
**Typ:** brak mocnego typu | **p:** 52% (SJS) | **Fair:** 1,92 | **Pewność:** niska
**Rynki dodatkowe:**
| Rynek | p | fair | Pewność |
|---|---|---|---|
| ML z OT: SJS / OTT | 52% / 48% | 1,92 / 2,08 | niska |
| 60' 3-way: SJS / X / OTT | 42,2% / 23% / 35,0% | 2,37 / 4,35 / 2,86 | niska |
| PL SJS -1,5 / OTT +1,5 | 33,3% / 66,7% | 3,0 / 1,50 | niska |
| PL SJS +1,5 / OTT -1,5 | 73,3% / 26,7% | 1,36 / 3,75 | niska |
| Total 5,5 Over / Under | ~58% / ~42% | 1,72 / 2,38 | niska |
| Total 6,5 Over / Under | ~46% / ~54% | 2,17 / 1,85 | niska |
| Shots Celebrini (SJS) O3,5 / O4,5 | 54,9% / 40,6% (śr. 4,0 z 4,17) | 1,82 / 2,46 | niska |
| Goals Celebrini strzelec | ~31,6% | 3,16 | niska |
| Shots Batherson (OTT) O2,5 | ~53% (śr. 2,3-2,9) | ~1,9 | niska |
**Statystyki drużyn:** SJS 7-6-1, GF 2,86 / GA 3,36, 3:2 z VAN (29.10). OTT 8-5-1, GF 3,14 / GA 3,14, 6:5 z LAK (29.10, mecz o wysokim wyniku). Celebrini 16 pkt w 12 meczach, 50 strzałów.
**H2H:** nie badano.
**Bramkarze (niepotwierdzeni):** SJS Askarov (.900, 3,01 GAA; Nedeljkovic .903); OTT Johansson (.861, 4,04 GAA) lub Ersson (.849). **Ullmark (.945, 1,33 GAA) na IR** - OTT pozbawiona najlepszego elementu: +0,2 gola dla SJS.
**Informacje medialne:** obie 29.10 (1 dzień przerwy), OTT po meczu w LA (krótki lot). ESPN: OTT bez Ullmarka (IR), Eklunda (IR), Foegele (Out), Burakovsky DTD; SJS bez Chernyshova, Wennberga, Musty, Keysera (bramkarz, IR).
**Oczekiwane gole:** SJS 3,25 - OTT 3,00 (6,25).
**Ryzyka:** rynek mógł wycenić OTT jako faworyta (BettingPros ±127 - znak niepewny); jeśli Ullmark jednak wróci, ML OTT +8-10 pp.
**Rynek:** BettingPros best OTT/SJS ±127 (strona niepewna), Under 6,5 -117 (1,85) vs fair 1,85: EV ~0. Sprawdzić po otwarciu rynku.

---

## Ranking najlepszych rynków (bez fair ≤ 1,15; pewność niska/niska-średnia, nic na kupon przed potwierdzeniem bramkarzy)

| # | Mecz | Rynek | Linia | p | fair | Kurs rynku | EV | Pewność |
|---|---|---|---|---|---|---|---|---|
| 1 | Boston - Chicago | Total goli Under | 6,5 | 59% | 1,69 | 1,82 (BettingPros best) | ok. +7% | niska-średnia |
| 2 | Boston - Chicago | ML z OT Boston | - | 65% | 1,54 | 1,47 (BP) | -4% | niska-średnia |
| 3 | Florida - Winnipeg | ML z OT Florida | - | 61% | 1,64 | 1,49 (BP) | -9% | niska |
| 4 | Florida - Winnipeg | Total goli Under | 6,5 | 58% | 1,72 | 1,80 (BP) | ok. +4% | niska |
| 5 | Tampa Bay @ Nashville | Strzały Hagel Over | 3,5 | 60% | 1,66 | brak | - | niska |
| 6 | NYI - Edmonton | Punkty McDavid Over | 0,5 | 77% | 1,30 | brak | - | niska |
| 7 | Vegas - New Jersey | Total goli Under | 6,5 | 56,7% | 1,76 | 1,76 (Pinnacle) | 0% | niska-średnia |
| 8 | Detroit - St. Louis | Total goli Under | 6,5 | 62% | 1,61 | 1,61 (BP) | 0% | niska |
| 9 | Calgary - Seattle | ML z OT Seattle | - | 52,5% | 1,90 | 1,90 (Pinnacle) | 0% | niska |
| 10 | San Jose - Ottawa | ML SJS (bramkarz OTT bez Ullmarka) | - | 52% | 1,92 | do sprawdzenia | ? | niska |

Tylko #1 i #4 mają dodatnie EV, ale oba na jednej linii BettingPros (best line) i zależą od niepotwierdzonych bramkarzy; #1 to jedyny kandydat dla `bet-slip-builder` (po potwierdzeniu Swayman/Knight i kursie >= 1,75).

## Odrzucone (z powodem)

- **Detroit - St. Louis (ML, PL, total):** wyrównany mecz (50/50), Gibson vs Tarasov niepotwierdzony, EV Under = 0.
- **NY Islanders - Edmonton (ML, total):** wyrównany (50/50), brak przewagi nad rynkiem pick'em; Under 6,5 poniżej kursu.
- **Los Angeles - Buffalo (ML, total):** pick'em, obaj bramkarze słabi (.878/.880) - wysoka wariancja, brak value.
- **Calgary - Seattle (SEA -1,5, total):** różnica do Pinnacle w granicy błędu (+2 pp); Wolf/Cooley i Daccord niepotwierdzeni.
- **Vegas - New Jersey (ML, PL, total):** zgodne z rynkiem, EV 0; Hellebuyck vs Allen niepotwierdzony.
- **Nashville - Tampa Bay (ML TBL, total):** mój p (56%) poniżej rynku (~59%), a znak faworyta w best_lines BettingPros niepewny.
- **San Jose - Ottawa (ML):** rozbieżność z rynkiem nierozstrzygnięta (strona ±127 niepewna), bramkarz OTT bez Ullmarka niepotwierdzony.
- **Puck line -1,5 faworytów (BOS 2,32; FLA 2,66):** p 38-43%, kursy poniżej fair (BOS +100 = EV ujemne).
- **PL +1,5 / ML faworytów z fair <= 1,15-1,20:** FLA +1,5 (1,27), BOS +1,5 (1,21) - zbyt krótkie/brak value.
- **Strzelcy goli (Draisaitl 36%, Pastrnak 33%, Connor 34%, Thompson 32%, Celebrini 32%):** jedno źródło, wysokie SH% sezonu do regresji, brak kursów - nie rekomenduję.
- **Obrony bramkarzy (Swayman, Hofer, Sorokin):** startujący niepotwierdzeni (0 z 26), brak linii; zgodnie z regułą skilla bez typu.
- **Strzały/punkty (Hagel, Connor, Schaefer, DeBrincat, Celebrini, Thompson, McDavid, Draisaitl):** linie nie wystawione (BettingPros props puste dla 30-31.10), jedno źródło danych, skład/PP niepotwierdzone - tylko informacyjnie.

## Tabela kandydatów dla `bet-slip-builder`

| Mecz | Rynek | p | fair | Pewność | Zależność | Kurs znany |
|---|---|---|---|---|---|---|
| Boston - Chicago | Under 6,5 | 59% | 1,69 | niska-średnia | Swayman/Knight start; brak zmiany w składzie CHI | tak (BP best 1,82) |
| Boston - Chicago | ML Boston | 65% | 1,54 | niska-średnia | Swayman; EV ujemne wg BP | tak (1,47) |
| Florida - Winnipeg | Under 6,5 | 58% | 1,72 | niska | Daws/Schmid (obaj słabi) | tak (BP best 1,80) |
| Vegas - New Jersey | Under 6,5 | 56,7% | 1,76 | niska-średnia | Hellebuyck vs Allen | tak (Pinnacle 1,76) |

Po potwierdzeniu bramkarzy (ok. 3-5 h przed pierwszym pitchem, pt 23:00 PL dla VGK-NJ) trzeba ponownie przeliczyć λ: zmiana bramkarza = +/-0,2-0,4 gola dla rywala.

To są oszacowania probabilistyczne, nie gwarancje.
