# Analiza NBA - 30.10.2026 (mecze nocne 31.10 PL + 31.10 dzień/wieczór)

Sprawdzono 30.10.2026 (ok. 02:00 UTC / rano PL). Status zawodników może się zmienić do rozpoczęcia meczu; raport oficjalny NBA publikowany jest dzień wcześniej i aktualizowany do ok. 90 min przed meczem. Wszystko poniżej to oszacowania probabilistyczne, nie gwarancje.

## Źródła i metoda
- Net/Off/Def rating, pace, eFG%: stats.nba.com przez MCP `nba_stats_call` (sezon 2026-27, **tylko 3-6 meczów na drużynę** - próba bardzo mała, ratingi traktowane z dużym szrinkiem, SD różnicy podniesione do 12,5-13).
- Linie, moneyline, total: ESPN/DraftKings (MCP `espn_scoreboard`, kursy closing z 30.10). Dla meczów Jazz-Blazers i Hornets-76ers (31.10) linii jeszcze nie ma (BettingPros i ESPN zwróciły puste oferty).
- Injury report: ESPN Injuries (dane Rotowire, stan z 29-30.10). Oficjalnego raportu NBA PDF z 30.10 nie udało się pobrać (WebSearch nie zwrócił), więc statusy DTD są niepotwierdzone.
- Statystyki zawodników: `leaguedashplayerstats` 2026-27 per game (4-5 meczów, średnie szrinkowane do oczekiwań). Drugie niezależne źródło liczb (BBRef/CTG) niedostępne w sesji, więc **rynki zawodnika mają maksymalnie niską pewność i nie są rekomendowane na kupon**, poza kilkoma z linią BettingPros zgodną z projekcją BP.
- BettingPros (klucz ustawiony): projekcje `props` (top 20 po EV) użyte jako kontrola; limit dzienny API (HTTP 429) uniemożliwił pobranie pełnej listy i linii/ofert dla Jazz-Blazers i Hornets-76ers. Mapowanie market_id: 156 pkt, 335 P+A, 336 P+R, 338 PRA.
- Back-to-back: 29.10 grały tylko CLE@ATL, SAC@NOP, MEM@POR. W piątek 30.10 nikt z uczestników nie gra B2B. 31.10: Hornets i 76ers oba w drugim dniu B2B (Hornets: pt u Wizards, 76ers: pt z Knicks); Blazers po jednym dniu przerwy (grali 29.10).
- H2H: pominięte (skład zmienia się radykalnie, waga ~0; brak wiarygodnych danych z podobnymi składami).
- Kalibracja: model liczy z mojego oczekiwanego wyniku; gdzie mój p odbiegał od rynku bez vig o >5 pp, przesunąłem go w stronę rynku (wartości "p końcowe").

## Rynek (DraftKings, close) vs mój model

| Mecz | Spread (gosp.) | Total | ML gosp./gość | Mój wynik (G-Go) | Mój spread/total |
|---|---|---|---|---|---|
| Wizards - Hornets | WAS -1,5 | 220,5 | -115/-105 | 110,5-107,5 | WAS -3 / 218 |
| Celtics - Bulls | BOS -15,5 | 235,5 | -850/+575 | 124,5-108,5 | BOS -16 / 233 |
| Nets - Pistons | BKN +7,5 | 221,5 | +230/-285 | 106,5-114,5 | DET -8 / 221 |
| 76ers - Knicks | PHI +1,5 | 228,5 | +105/-125 | 113,5-114,5 | NYK -1 / 228 |
| Raptors - Magic | TOR -5,5 | 225,5 | -205/+170 | 114,5-108 | TOR -6,5 / 222,5 |
| Mavericks - Rockets | DAL +5,5 | 226,5 | +180/-218 | 110-116 | HOU -6 / 226 |
| Heat - Pacers | MIA -7,5 | 236,5 | -278/+225 | 119,5-114 | MIA -5,5 / 233,5 |
| Timberwolves - Clippers | MIN -7,5 | 222,5 | -265/+215 | 112,5-106,5 | MIN -6 / 219 |
| Warriors - Lakers | GSW +1,5 | 234,5 | +110/-130 | 114-117 | LAL -3 / 231 |
| Suns - Nuggets | PHX +4,5 | 231,5 | +142/-170 | 112-116 | DEN -4 / 228 |
| Jazz - Trail Blazers (31.10 20:00) | brak linii | brak | brak | 112-116 | POR -4 / 228 |
| Hornets - 76ers (31.10 23:00) | brak linii | brak | brak | 108,5-112 | PHI -3,5 / 220,5 |

Wniosek ogólny: rynek NBA jest efektywny, moneyline/spread niemal wszędzie zgodny z moim p (różnice < 5 pp po szrinkowaniu). Jedyne przewagi to lekkie Under totali (patrz niżej), z niską pewnością.

---

## Wizards - Hornets (sob 31.10 00:00 PL; pt 30.10 18:00 ET)
**Typ:** brak mocnego typu (wyrównany) | WAS wygrywa p=55% (fair 1,82; rynek -115 = ok. 50-52% bez vig) | Pewność: niska
| Rynek | p | fair | uwagi |
|---|---|---|---|
| WAS ML | 55% | 1,82 | przesunięte z 58% do rynku |
| WAS -1,5 | 53% | 1,89 | |
| CHA +1,5 | 47% | 2,13 | |
| Total U220,5 | 54% | 1,85 | Hornets pace 98,7 (najwolniejsi), ORtg 102, bez Knuepla, White'a, G. Williamsa, Boswella |
| Total drużyny CHA U109,5 | 57% | 1,75 | średnia 107,5 |
| Total drużyny WAS U111 | 52% | 1,92 | średnia 110,5 |
**Statystyki:** WAS net -1,5 (ORtg 112,7, DRtg 114,2, pace 101,1); CHA net -7,5, DRtg 109,7, ORtg 102,2. 5 meczów, próba mała.
**Kontuzje:** WAS: Tre Johnson DTD (Achilles), Champagnie/Vukcevic/Watkins Out. CHA: Knueppel Out (hamstring), C. White Out, G. Williams Out, Boswell Out, Schröder DTD (stopa). Skład gwiazd WAS (Young, Davis, George, Sarr) zdrowy.
**Rynki zawodnika (linie szacunkowe, brak ofert):** Trae Young asysty śr. 9,8: Over 8,5 62% / Under 10,5 61%; A. Davis zbiórki 9,0: Over 8,5 52%; Davis pkt 21,5; Brandon Miller pkt 24,5 (użycie wyższe po absencjach, ale Schröder DTD): Over 23,5 52%. Niska pewność.
**Ryzyka:** status Schrödera i Tre Johnsona; mała próba; Hornets mogą grać jeszcze wolniej (Under) lub rozpaść się w ataku.

## Celtics - Bulls (sob 31.10 00:30 PL)
**Typ:** BOS ML p=89% fair 1,12 (pomijam: fair <= 1,15) | Pewność: średnia
| Rynek | p | fair |
|---|---|---|
| BOS ML | 89% | 1,12 (rynek 1,12) |
| BOS -15,5 | 51% | 1,96 |
| CHI +15,5 | 49% | 2,04 |
| Total U235,5 | 54% | 1,85 |
| Total drużyny CHI U110 | 55% | 1,82 |
**Statystyki:** BOS net +8,6 (ORtg 117, DRtg 108,5, pace 100); CHI net -15,9 (DRtg 121,7, pace 107,4 - najszybsi, ORtg 105,8), 1-4.
**Kontuzje:** CHI: Patrick Williams Out (adductor), Claxton Out, Jalen Smith DTD, Awaka DTD. BOS: Devin Carter Out (mono).
**Rynki zawodnika:** ryzyko blowoutu (spread 15,5) - minuty Tatuma/George'a spadają. Tatum PRA: średnia 40 (zamiast 42,3) - **Under 43,5 (BettingPros, -115) p=60% fair 1,67**; Tatum pkt 26,5 (26,5 Under 58%); P. George pkt 21 (Under 23,5 p=60% po szrinkowaniu z 67%; BP proj. 19,9 P+R, zgodne). Wilson (CHI) pkt 20: Under 20,5 56%. BP projekcje Under (Tatum, George) zgodne z blowoutem. Skorelowane (jeden mecz, ten sam scenariusz blowoutu).
**Ryzyka:** mecz wyrównany do 3. kwarty (Bulls pace 107 -> więcej posiadań, wyższe zbiórki/punkty), Tatum gra pełne minuty.

## Nets - Pistons (sob 31.10 00:30 PL)
**Typ:** DET ML p=74% fair 1,35 (rynek -285 = 1,35, brak value) | Pewność: średnia
| Rynek | p | fair |
|---|---|---|
| DET ML | 74% | 1,35 |
| DET -7,5 | 52% | 1,92 |
| BKN +7,5 | 48% | 2,08 |
| Total | 49% O / 51% U 221,5 | ok. 2,0 |
**Statystyki:** BKN 0-4, net -8,9 (DRtg 116,7, ORtg 107,8); DET 4-1, net +6,3 (DRtg 105,5, 3. w lidze), pace DET 98,1 (najwolniejsi).
**Kontuzje:** DET: Duren Out (hamstring), Isaiah Joe DTD (hip). BKN: Demin Out (kwestia kontraktu), Bilodeau Out.
**Rynki zawodnika:** Cade Cunningham pkt 22,5 (Over 21,5 52%), asysty 7,5 (Over 6,5 60%); Randle pkt 21,5; M. Porter Jr. trójki 2,3. Niska pewność.
**Ryzyka:** DET bez Durena na zbiórkach; mecz mógłby być blowout (spread 7,5 - umiarkowane).

## 76ers - Knicks (sob 31.10 00:30 PL)
**Typ:** brak mocnego typu (p ok. 50%) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| NYK ML | 52% | 1,92 (rynek -125) |
| PHI ML | 48% | 2,08 (rynek +105) |
| Total | 51% U228,5 | ok. 1,96 |
**Statystyki:** PHI 4-1, net +3,3, DRtg 103,3 (3.), pace 104; NYK 2-3, net -0,2, ORtg 110,7, pace 99. Rynek faworyzuje NYK mimo gorszego bilansu: linia PHI przesunęła się z -125 do +105 (sygnał kadrowy/rynkowy - Jaylen Brown DTD, kolano).
**Kontuzje:** PHI: Jaylen Brown DTD (kolano), Barlow/Fall/Walker/Hukporti Out. NYK: Alvarado Out (kostka).
**Rynki zawodnika:** Towns PRA śr. 38,8 - **Over 34,5 (BettingPros, -115) p=61% fair 1,64** (proj BP 39; Towns pkt 21,8, zb. 13,8; mecz bez ryzyka blowoutu); Towns zbiórki 12,5: Over 11,5 57%. Maxey pkt 27 (Over 25,5 55%), Embiid pkt 22/zb. 10 - ryzyko minut/odpoczynku; Brunson pkt 25,5. Jeśli Brown nie zagra: PHI spread +1,5 -> ok. +4 przeciw.
**Ryzyka:** status Browna (zmienia spread o 2-3 pkt), Embiid (load management po powrotach).

## Raptors - Magic (sob 31.10 00:30 PL)
**Typ:** TOR ML p=66% fair 1,52 (rynek -205 = 1,49; zgodne) | Pewność: niska-średnia
| Rynek | p | fair |
|---|---|---|
| TOR ML | 66% | 1,52 |
| TOR -5,5 | 53% | 1,89 |
| ORL +5,5 | 47% | 2,13 |
| Total U225,5 | 55% | 1,82 |
| Total drużyny ORL U110 | 57% | 1,75 |
**Statystyki:** TOR 3-1, net +14,6 (DRtg 97,9 - 1. w lidze, pace 104,6); ORL 1-3, net -10,8 (ORtg 104,4, DRtg 115,2).
**Kontuzje:** ORL: Banchero Out (kostka, do 22.11), Suggs Out, Isaac Out, Penda Out, Nelson Out - bardzo wyniszczeni. TOR: Kawhi Leonard Out (kolano, do 23.11), Bittle Out.
**Rynki zawodnika:** ORL bez Banchero/Suggsa: Franz Wagner pkt 24 (użycie w górę), PRA 36. BettingPros: Wagner PRA 35,5 Under (proj BP 30,6) - **konflikt z moim 36**, więc brak typu; Bane pkt 16 (Over 14,5 56%); Barnes PRA 31. Niska pewność.
**Ryzyka:** rynek już wycenia absencje Magic; TOR bez Kawhi ma słabszy atak; Under oparty na DRtg TOR i ataku ORL ORtg 104.

## Mavericks - Rockets (sob 31.10 01:00 PL)
**Typ:** HOU ML p=67% fair 1,49 (rynek -218 = 1,46) | Pewność: niska-średnia (Sengun DTD)
| Rynek | p | fair |
|---|---|---|
| HOU ML | 67% | 1,49 |
| HOU -5,5 | 52% | 1,92 |
| DAL +5,5 | 48% | 2,08 |
| Total | 51% U226,5 | 1,96 |
**Statystyki:** HOU 5-0, net +14,1 (ORtg 122,5, DRtg 108,4, eFG 59,4%); DAL 3-2, net +2,2 (ORtg 113,8, DRtg 111,6).
**Kontuzje:** HOU: Sengun DTD (plecy), Smart Out, Sheppard Out, Adams Out. DAL: Lively Out, Aldama Out, Biberovic Out, Marshall DTD (choroba), de Larrea Out.
**Rynki zawodnika:** Durant pkt 22,5 (Over 21,5 52%), Flagg PRA 34 (Over 32,5 55%), Irving pkt 18. Sengun bez typu (DTD).
**Ryzyka:** Sengun poza składem to -2 do -3 pkt dla HOU; przy 5-0 HOU rynek już drogi (regresja skuteczności).

## Heat - Pacers (sob 31.10 01:00 PL)
**Typ:** Under 236,5 p=55% fair 1,82 (total za wysoki wobec 2 osłabionych składów) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| MIA ML | 69% | 1,45 (rynek -278 = 1,36; MIA drożej niż fair - brak value) |
| IND ML | 31% | 3,23 |
| MIA -7,5 | 46% | 2,17 |
| IND +7,5 | 54% | 1,85 (rynek -115 ok. 53,5%, brak edge) |
| Total U236,5 | 55% | 1,82 (rynek -110) |
| MIA team U122 | 59% | 1,70 |
**Statystyki:** MIA 1-4, net -8,4 (DRtg 116,8, pace 103,8), ale z Giannisem (27,6 pkt, 11,2 zb.); IND 2-3, net +0,8 (ORtg 111,7, pace 103,3).
**Kontuzje:** IND: Haliburton Out (hamstring, do 13.11), Zubac Out, McConnell Out, Nembhard DTD (szyja), Nesmith DTD (hamstring), Sheppard/Furphy Out. MIA: Fontecchio DTD (choroba).
**Rynki zawodnika:** Giannis pkt 27 (Over 25,5 55%), zb. 10,5 (Over 9,5 57%); Siakam pkt 25 / PRA 36,5 (usage w górę po absencjach). Niska pewność.
**Ryzyka:** IND w pełni okrojone w backcourcie -> MIA może wygrać wyżej (spread 7,5 jest blisko mojego -5,5, więc ryzyko IND +7,5 to blowout; różnica mojego p od rynku na ML 6 pp - nie schodzę poniżej rynku bez konkretów, skorygowane).

## Timberwolves - Clippers (sob 31.10 01:00 PL)
**Typ:** Under 222,5 p=56% fair 1,79 | Pewność: niska-średnia
| Rynek | p | fair |
|---|---|---|
| MIN ML | 68% | 1,47 (rynek -265 = 1,38) |
| MIN -7,5 | 46% | 2,17 |
| LAC +7,5 | 54% | 1,85 |
| Total U222,5 | 56% | 1,79 (rynek -110) |
| MIN team U115 | 59% | 1,70 |
**Statystyki:** MIN 3-2, net +12,4 (DRtg 102,5 - 2. w lidze, pace 102,9) - ale przy Edwardsie (33 pkt); LAC 1-3, net -1,2 (ORtg 104,9, DRtg 106,1), TO% 23,2% (najgorsza w lidze).
**Kontuzje:** MIN: **Anthony Edwards Out** (zabieg kolana, do 21.12; ogłoszone 29.10 - linia ML MIN spadła z -360 do -265), DiVincenzo Out. LAC: Beal, Ingram, Strus, Niederhauser Out, Hachimura DTD.
**Rynki zawodnika:** Gobert zb. śr. 12,2 -> Over 11,5 52% (bez Edwardsa więcej zbiórek obwodowych dla MIN, ale mniej wygranej piłki); LaMelo asysty 6,5 (usage w górę); Garland pkt 22 (Over 20,5 55%). Niska pewność.
**Ryzyka:** MIN bez Edwardsa ma tylko 3-4 pkt przewagi nad realnym DRtg; LAC wyniszczone ofensywnie, więc mecz może być bardzo niski (Under) lub MIN blowout.

## Warriors - Lakers (sob 31.10 03:00 PL)
**Typ:** LAL ML p=57% fair 1,75 (rynek -130 = ok. 54,5%) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| LAL ML | 57% | 1,75 |
| LAL -1,5 | 55% | 1,82 (rynek -115) |
| Total U234,5 | 54% | 1,85 |
| GSW team U116,5 | 59% | 1,70 |
**Statystyki:** LAL 4-1, net +10,2 (ORtg 122,5, eFG 61,7% - nie do utrzymania, pace 100,9); GSW 2-3, net -2,0 (ORtg 115,7, DRtg 117,8). Dončić 36 pkt/8,3 ast.
**Kontuzje:** GSW: Butler Out (ACL), Porzingis Out (poza zespołem), Moody Out, Santos DTD. LAL: Carr Out, Thiero Out, Ziaire Williams DTD.
**Rynki zawodnika:** Dončić pkt 35 (Over 32,5 59% / Under 36,5 59%), ast 8,5, PRA 49,5; Curry trójki 3,7 (Over 2,5 71%); Reaves pkt 24. BettingPros: Reaves PRA O29,5 z kursem +150 - nieprawdopodobne (prawdopodobnie błędna/alt linia) - odrzucone. Niska pewność.
**Ryzyka:** regresja skuteczności LAL (eFG 61,7%); GSW u siebie z Curry (28,8 pkt); rynek pozostaje blisko pick'em.

## Suns - Nuggets (sob 31.10 03:00 PL)
**Typ:** DEN ML p=61% fair 1,64 (rynek -170 = 1,59) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| DEN ML | 61% | 1,64 |
| DEN -4,5 | 49% | 2,04 |
| PHX +4,5 | 51% | 1,96 |
| Total U231,5 | 54% | 1,85 |
| PHX team U113,5 | 55% | 1,82 |
**Statystyki:** PHX 1-2 (3 mecze), net -12,9 (DRtg 124,5, pace 98,7); DEN 2-2, net -3,7 (ORtg 108,3, DRtg 112). Jokić pkt 22/zb. 10,5/ast 9 (powinien wzrosnąć).
**Kontuzje:** DEN: Cameron Johnson Out, Diallo Out (osobiste), Spencer Jones Out, Strawther Out. PHX: Ighodaro DTD (oblique), Mark Williams Out.
**Rynki zawodnika:** Jokić zb. 11,5 (Over 10,5 57%), ast 9,5 (Over 8,5 59%), PRA 46; Booker pkt 26 - BettingPros proj. 26,7 pkt (Over 22,5) / PRA 37,9 (Over 32,5) i mój model rozbieżne (mały sample 3 meczów) - brak typu; Murray pkt 22.
**Ryzyka:** próba 3 meczów PHX, duża zmienność ratingu; Nuggets bez C. Johnsona słabsi w obronie skrzydeł.

## Jazz - Trail Blazers (sob 31.10 20:00 PL; 14:00 ET) - bez linii
**Typ:** brak - bez linii rynkowych (nie wyceniam przewagi) | POR wygrywa p=63% fair 1,59 (własna wycena) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| POR ML | 63% | 1,59 |
| POR -4 | 50% | 2,00 |
| POR -6 | 44% | 2,28 |
| Total 226,5 / 228,5 | O 53% / O 49% | |
**Statystyki:** POR 3-1, net +7,5 (ORtg 120,3, pace 101,5, grali 29.10 vs MEM, przerwa 1 dzień, wyjazd do SLC); UTA 1-4, net -8,0 (DRtg 116,7).
**Kontuzje:** UTA: Markkanen DTD (nadgarstek, powrót 31.10), Jaren Jackson Jr. Out (MCL), Nurkic Out, Alexander Out. POR: **Ja Morant DTD (hamstring), Robert Williams III DTD (kolano) - oba zgłoszone 30.10**, Sharpe Out.
**Rynki zawodnika:** Avdija PRA 36 (Over 33,5 60%), Lillard pkt 18,5; Keyonte George pkt 23,5. Bez potwierdzenia Morant/Markkanen brak typów.
**Ryzyka:** dwa kluczowe statusy DTD po obu stronach; brak linii; wczesny mecz po podróży.

## Hornets - 76ers (sob 31.10 23:00 PL; 18:00 ET) - bez linii, oba zespoły B2B
**Typ:** PHI ML p=60% fair 1,67 (własna wycena, bez linii) | Pewność: niska
| Rynek | p | fair |
|---|---|---|
| PHI ML | 60% | 1,67 |
| PHI -2,5 | 53% | 1,88 |
| PHI -3,5 | 50% | 2,00 |
| Total 220,5 | 50% | 2,00 |
**Statystyki:** CHA net -7,5 (ORtg 102,2, DRtg 109,7, pace 98,7); PHI 4-1, net +3,3, DRtg 103,3.
**Kontuzje:** CHA: Knueppel, White, G. Williams, Boswell Out (powrót ok. 2.11), Schröder DTD. PHI: Brown DTD (30.10), Walker Out do 31.10 (możliwy powrót).
**Back-to-back:** oba zespoły w drugim dniu B2B (CHA w Waszyngtonie, PHI w domu z NYK 30.10): zmęczenie symetryczne; skorygowano total o -1, SD podniesione do 13. Możliwy load management gwiazd PHI (Embiid) - realne ryzyko.
**Rynki zawodnika:** nie wyceniam (status po piątku nieznany).
**Ryzyka:** wynik piątkowych meczów, minuty po B2B, status Embiida/Browna.

---

## Ranking najlepszych rynków (wszystkie niskiej/średniej pewności)

| # | Mecz | Rynek | Linia | p | fair | Kurs rynkowy | Pewność |
|---|---|---|---|---|---|---|---|
| 1 | Timberwolves - Clippers | Total Under | 222,5 | 56% | 1,79 | -110 (DK) | niska-średnia |
| 2 | Raptors - Magic | Total Under | 225,5 | 55% | 1,82 | -105 (DK) | niska |
| 3 | Heat - Pacers | Total Under | 236,5 | 55% | 1,82 | -110 (DK) | niska |
| 4 | Celtics - Bulls | Tatum PRA Under (BettingPros) | 43,5 | 60% | 1,67 | -115 (BP) | niska (blowout) |
| 5 | Knicks @ 76ers | Towns PRA Over (BettingPros) | 34,5 | 61% | 1,64 | -115 (BP) | niska |
| 6 | Wizards - Hornets | CHA total drużyny Under | 109,5 | 57% | 1,75 | brak | niska |
| 7 | Warriors - Lakers | Total Under | 234,5 | 54% | 1,85 | -105 (DK) | niska |
| 8 | Suns - Nuggets | Total Under | 231,5 | 54% | 1,85 | -115 (DK) | niska |
| 9 | Raptors - Magic | TOR ML | - | 66% | 1,52 | -205 (1,49, brak value) | niska-średnia |
| 10 | Mavericks - Rockets | HOU ML | - | 67% | 1,49 | -218 (1,46, brak value) | niska-średnia |

Uwaga: faworyci (BOS ML fair 1,12; DET ML 1,35) i mecze z fair ≤ 1,15 nie wchodzą do rankingu poza BOS (odrzucony). Kursy rynkowe ML to w większości dokładnie moje fair - brak EV.

## Odrzucone (z powodem)
- **Celtics ML (fair 1,12)** - fair <= 1,15, zbyt krótki kurs.
- **Wizards - Hornets ML/spread, 76ers - Knicks ML/spread, Warriors - Lakers spread** - p w przedziale 45-55%, "brak mocnego typu".
- **Mecze Jazz - Blazers i Hornets - 76ers** - brak linii i kursów (BettingPros 429/puste, ESPN null) oraz niepotwierdzone statusy Morant/Williams III/Markkanen/Brown/Embiid; wyceny tylko orientacyjne.
- **Heat ML** - mój p 69% vs rynek 72% (-278) - bez edge, nie schodzę pod rynek; Pacers +7,5 - mój p 54% = rynek 53,5%.
- **Nets - Pistons wszystkie rynki** - fair = rynek, DET 74% = -285; brak EV.
- **Sengun (HOU), Nembhard/Nesmith (IND), Hachimura (LAC), Brown (PHI), Schröder (CHA), Morant/Williams/Markkanen** - status DTD/Questionable bez potwierdzenia, brak typów warunkowych jako wariant główny.
- **Wagner PRA U35,5 (BP) i W. Carter PRA U22,5 (BP)** - projekcja BP rozbieżna z moją (po absencjach ORL użycie rośnie), flaga zamiast typu.
- **Booker PRA/pkt (BP over)** - rozbieżność mojej średniej (26) z projekcją BP (33,6); 3 mecze próby.
- **Reaves PRA O29,5 (+150)** - kurs i linia niewiarygodne, wygląda na błąd/alt.
- **P. George P+A/PRA Under** - przeciwne sygnały (mój szrink vs BP proj. 18,7-23 przy średniej 25,8), niska wiarygodność.
- **Wszystkie pozostałe rynki zawodnika (pkt/zb./ast/trójki)** - brak linii bukmachera i brak drugiego niezależnego źródła średnich -> maksymalnie niska pewność, nie rekomendowane na kupon.

*To są oszacowania probabilistyczne, nie gwarancje; statusy kontuzji (zwłaszcza DTD) mogą się zmienić do rozpoczęcia meczu.*
