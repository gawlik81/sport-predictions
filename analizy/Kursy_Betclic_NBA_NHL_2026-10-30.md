# Kursy Betclic.pl (źródło główne) + weryfikacja gg397.bet - NBA/NHL, noc 30/31.10 i 31.10.2026

Pobrano: 30.10.2026, ok. 07:00 CET (czas polski). Źródła: betclic.pl (strony meczów, bez logowania), gg397.bet/pl. EV = p * kurs - 1 (p z `Analiza_NBA_2026-10-30.md` / `Analiza_NHL_2026-10-30.md`). Brak rynku = brak kursu.

## Ograniczenia pobrania
- Betclic pokazuje dla totalu meczu i handicapu tylko okno 3 linii (zwykle linie niższe od głównej linii DK/ESPN, np. ORL-TOR 216,5-218,5 przy DK 225,5), więc główne linie z analizy (U222,5 MIN-LAC, U225,5 TOR-ORL, U236,5 MIA-IND, U234,5 GSW-LAL, U231,5 PHX-DEN, U220,5 WAS-CHA, U235,5 BOS-CHI) są niedostępne. Dostępne są totale drużyn (jedna linia, kursy O/U) i ML.
- Rynki zawodnika NBA (Tatum PRA U43,5, Towns PRA O34,5 i inne): Betclic ich nie ma (zakładki Wynik/Punkty zawierają tylko suma meczu, połowy, kwarty, total drużyn, odd/even). Kursy BettingPros (-115) nie są kursami Betclic - nie wpisuję.
- NHL: Betclic miał wystawione tylko 3 mecze (VGK-NJ, FLA-WPG, CGY-SEA). Mecze z 31.10 (BOS-CHI, DET-STL, NSH-TBL, NYI-EDM, LAK-BUF, SJS-OTT) niewystawione. Total goli: okno linii 2,5-4,5 (kursy 1,01-1,22 po stronie Over); linii 5,5/6,5 z analizy brak. Brak rynków zawodnika i puck line.
- gg397.bet: kursy NBA dostępne tylko dla TOR-ORL i BKN-DET (strona główna koszykówki); na stronie turnieju NBA wszystkie kursy "-" (niewystawione/niezaładowane). Brak totali drużyn, więc dla kandydatów EV>0 weryfikacji gg397 nie uzyskano.
- Mecze VGK-NJ (pt 23:00) zaczyna się wieczorem 30.10 - nie rozpoczęty w momencie pobrania.

## A. Kandydaci z EV > 0 na Betclic (tylko totale drużyn)

| Mecz | Godz. PL | Rynek + linia | p | fair | Betclic | gg397 | EV | Uwagi |
|---|---|---|---|---|---|---|---|---|
| Warriors - Lakers | sob 03:00 | GSW total drużyny Under 116,5 | 59% | 1,70 | 1,81 | brak | +6,8% | linia identyczna z analizą; Over 1,86 |
| Suns - Nuggets | sob 03:00 | PHX total drużyny Under 113,5 | 55% | 1,82 | 1,84 | brak | +1,2% | linia identyczna; w granicy błędu |
| Timberwolves - Clippers | sob 01:00 | MIN total drużyny Under 114,5 (analiza: U115, p 59%) | ok. 57% (szac. po przesunięciu o 0,5) | ok. 1,75 | 1,87 | brak | ok. +6,6% | linia inna niż w analizie - p przybliżone |
| Raptors - Magic | sob 00:30 | ORL total drużyny Under 110,5 (analiza: U110, p 57%) | ok. 58% (szac.) | ok. 1,72 | 1,85 | brak | ok. +7% | linia inna - p przybliżone |
| Heat - Pacers | sob 01:00 | MIA total drużyny Under 122,5 (analiza: U122, p 59%) | ok. 60% (szac.) | ok. 1,67 | 1,79 | brak | ok. +7% | linia inna - p przybliżone |
| Celtics - Bulls | sob 00:30 | CHI total drużyny Under 109,5 (analiza: U110, p 55%) | ok. 54% (szac.) | ok. 1,85 | 1,87 | brak | ok. +1% | brak przewagi, blowout: ryzyko |

Przy liniach "szac." nie traktować EV jako potwierdzonego - p trzeba przeliczyć w nba-analyst dla linii Betclic.

## B. Moneyline NBA (Betclic vs fair) - brak EV > 0

| Mecz | Godz. PL | Rynek | p | fair | Betclic | gg397 | EV |
|---|---|---|---|---|---|---|---|
| Wizards - Hornets | sob 00:00 | WAS ML | 55% | 1,82 | 1,79 | brak | -1,5% |
| Celtics - Bulls | sob 00:30 | BOS ML | 89% | 1,12 | 1,07 (fair <= 1,15, pomijać) | brak | -4,8% |
| Nets - Pistons | sob 00:30 | DET ML | 74% | 1,35 | 1,31 | 1,24 | -3,1% |
| Raptors - Magic | sob 00:30 | TOR ML | 66% | 1,52 | 1,43 | 1,94 (rozbieżność, podejrzane) | -5,6% |
| Mavericks - Rockets | sob 01:00 | HOU ML | 67% | 1,49 | 1,42 | brak | -4,9% |
| Heat - Pacers | sob 01:00 | MIA ML | 69% | 1,45 | 1,31 | brak | -9,6% |
| Timberwolves - Clippers | sob 01:00 | MIN ML | 68% | 1,47 | 1,34 | brak | -8,9% |
| Warriors - Lakers | sob 03:00 | LAL ML | 57% | 1,75 | 1,70 | brak | -3,1% |
| Suns - Nuggets | sob 03:00 | DEN ML | 61% | 1,64 | 1,51 | brak | -7,9% |

(gg397 TOR ML 1,94 / ORL 1,81 oraz handicap TOR -5,5 = 2,11, total 229,5 O 2,01 / U 1,75 - rozbieżność względem Betclic >0,10 i niespójna z innymi rynkami; traktować jako błąd/nieaktualne.)

## C. Pozostałe dostępne kursy Betclic NBA (do bet-slip-buildera)

| Mecz | Total meczu (okno linii Betclic, O/U) | Handicap (okno) | Total drużyny gosp. / gość |
|---|---|---|---|
| Wizards - Hornets | 210,5: 1,32/3,13; 211,5: 1,35/2,94; 212,5: 1,39/2,78 | WAS -10,5: 3,51 ... | WAS 110,5 O1,82/U1,85; CHA 110,5 O1,89/U1,78 |
| Celtics - Bulls | 225,5: 1,33/3,04; 226,5: 1,37/2,86; 227,5: 1,41/2,70 | BOS -23,5: 3,25 ... | BOS 125,5 O1,86/U1,81; CHI 109,5 O1,80/U1,87 |
| Nets - Pistons | (nie pobrano) | - | - |
| 76ers - Knicks | 219,5: 1,34/3,02; 220,5: 1,37/2,84; 221,5: 1,41/2,68 | PHI -7,5: 3,10 ... | PHI 114,5 O1,88/U1,79; NYK 114,5 O1,79/U1,88; ML PHI 1,97 / NYK 1,78 |
| Raptors - Magic | 216,5: 1,32/3,09; 217,5: 1,36/2,91; 218,5: 1,40/2,75 | TOR -14,5: 3,60 ... | TOR 115,5 O1,80/U1,87; ORL 110,5 O1,82/U1,85 |
| Heat - Pacers | 233,5: 1,62/2,16; 234,5: 1,69/2,05; 235,5: 1,75/1,96 | MIA -8,5: 1,97; -9,5: 2,11 | MIA 122,5 O1,88/U1,79; IND 114,5 O1,80/U1,87 |
| Timberwolves - Clippers | 219,5: 1,62/2,17; 220,5: 1,68/2,07; 221,5: 1,75/1,97 | MIN -7,5: 1,92; -8,5: 2,05 | MIN 114,5 O1,80/U1,87; LAC 108,5 O1,88/U1,79 |
| Warriors - Lakers | 231,5: 1,65/2,11; 232,5: 1,72/2,01; 233,5: 1,79/1,92 | LAL -1,5: 1,77; GSW -1,5: 2,16 | GSW 116,5 O1,86/U1,81; LAL 118,5 O1,88/U1,79 |
| Suns - Nuggets | 227,5: 1,61/2,17; 228,5: 1,68/2,07; 229,5: 1,74/1,98 | DEN -1,5: 1,59; -2,5: 1,68; -3,5: 1,78 | PHX 113,5 O1,83/U1,84; DEN 117,5 O1,84/U1,83 |
| Mavericks - Rockets | (nie pobrano) | - | - |
| Jazz - Blazers, Hornets - 76ers (31.10) | niewystawione na Betclic | - | - |

Linie z analizy a Betclic: MIN-LAC U222,5 (brak; najbliższe U221,5 = 1,97), GSW-LAL U234,5 (brak; U233,5 = 1,92), PHX-DEN U231,5 (brak; U229,5 = 1,98), MIA-IND U236,5 (brak; U235,5 = 1,96), TOR-ORL U225,5 (brak). Przy niższych liniach p Under jest niższe niż w analizie - brak EV bez przeliczenia.

## D. NHL (Betclic; mecze 30/31.10)

| Mecz | Godz. PL | Rynek | p | fair | Betclic | gg397 | EV | Uwagi |
|---|---|---|---|---|---|---|---|---|
| Vegas - New Jersey | pt 23:00 | VGK ML (z OT) | 53% | 1,89 | 1,78 | brak | -5,7% | NJ 1,86 (p 47%: -12,6%) |
| Vegas - New Jersey | pt 23:00 | 60' VGK / X / NJ | 42,1/23/34,9% | 2,38/4,35/2,87 | 2,30 / 3,98 / 2,42 | brak | -3,2% / -8,5% / -15,5% | |
| Vegas - New Jersey | pt 23:00 | Total goli Under 6,5 | 56,7% | 1,76 | brak (okno 2,5-4,5) | brak | - | Under 4,5 = 3,85, Over 4,5 = 1,22 |
| Florida - Winnipeg | sob 00:00 | FLA ML (z OT) | 61% | 1,64 | 1,40 | brak | -14,6% | WPG 2,60 (p 39%: +1,4%, w granicy błędu) |
| Florida - Winnipeg | sob 00:00 | 60' FLA / X / WPG | 47,4/23/29,5% | 2,11/4,35/3,39 | 1,69 / 4,30 / 3,63 | brak | -19,9% / -1,1% / +7,1% | WPG 60' (p 29,5%, kurs 3,63) formalnie +7%, ale p niskie, pewność niska, b2b WPG |
| Florida - Winnipeg | sob 00:00 | Total goli Under 6,5 | 58% | 1,72 | brak | brak | - | okno 2,5-4,5; Betclic ma tylko progi niższe |
| Calgary - Seattle | sob 01:00 | SEA ML (z OT) | 52,5% | 1,90 | 1,78 | brak | -6,6% | CGY 1,86 (p 47,5%: -11,7%) |
| Calgary - Seattle | sob 01:00 | Total goli 6,5 | 49/51% | - | brak | brak | - | |
| BOS-CHI, DET-STL, NSH-TBL, NYI-EDM, LAK-BUF, SJS-OTT | sob 18:00-21:00 | wszystkie | - | - | niewystawione | niepobrane | - | w tym kandydat nr 1 NHL (BOS-CHI Under 6,5) - brak kursu Betclic |

Dodatkowo Betclic NHL (do wglądu): VGK-NJ total drużyny VGK O2,5 1,51/U2,33; NJ O2,5 1,56/U2,24. FLA-WPG: FLA O2,5 1,30/U3,15; WPG O2,5 1,88/U1,79. CGY-SEA: CGY O2,5 1,52/U2,31; SEA O2,5 1,48/U2,42. Brak p w analizie dla tych linii.

## Wniosek
- Przy Betclic nie ma żadnej nogi ML/spread NBA lub NHL z EV > 0. Jedyne dodatnie EV to Under totali drużyn NBA: pewny co do linii GSW U116,5 (1,81; EV +6,8%, p 59%, niska pewność wg analizy); PHX U113,5 (+1,2%, bez znaczenia); MIN U114,5, ORL U110,5, MIA U122,5 wymagają przeliczenia p dla linii Betclic.
- Kandydaci z analizy (Under totali meczu, Tatum/Towns PRA, BOS-CHI U6,5, FLA-WPG U6,5) - brak rynku/linii na Betclic; gg397 bez kursów. Nie wpisywano kursów z BettingPros/DK jako kursów Betclic.
- Weryfikacja gg397 dla nóg EV>0: niemożliwa (brak kursów NBA na stronie turnieju, brak totali drużyn).
