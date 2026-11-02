# Analiza NBA - dzień USA 01.11.2026 (4 mecze, noc 01/02.11 PL)

Sprawdzono 01.11.2026 (rano czasu USA / południe PL). Statusy mogą się zmienić do rozpoczęcia meczu (oficjalny raport NBA aktualizowany do ok. 90 min przed). To oszacowania probabilistyczne, nie gwarancje.

## Źródła i metoda
- Net/off/def rating, pace: stats.nba.com przez MCP `nba_stats_call` (`leaguedashteamstats`, sezon 2026-27, **tylko 5-6 meczów na drużynę**). Próba bardzo mała, więc ratingi są tylko wskazówką, a wynik zakotwiczony w linii rynku; SD różnicy 12,5-13, SD sumy 18,5-19.
- Linie (spread/total): ESPN/DraftKings (MCP `espn_scoreboard`, stan 01.11). Moneyline DraftKings w feedzie puste, więc ML wyceniony z modelu i spreadu (bez kursu rynkowego). Kursów Betclic w tym pliku brak.
- Injury report: ESPN Injuries (dane Rotowire, 01.11). Oficjalnego PDF NBA nie udało się pobrać; `nba_daily_lineups` zwrócił 404, więc składy startowe niepotwierdzone.
- Statystyki zawodników: `leaguedashplayerstats` 2026-27 (4-6 meczów). Drugiego niezależnego źródła liczb nie było, więc **wszystkie rynki zawodnika mają niską pewność i nie są rekomendowane na kupon**. Rynki zawodnika wyceniane względem orientacyjnych linii (brak realnych linii/kursów prop w sesji).
- BettingPros: pominięty (nie weryfikowałem klucza w tej sesji). Linemate: poza zakresem.
- Back-to-back: żadna z 8 drużyn nie grała 31.10, więc nikt nie jest w drugim dniu B2B.
- H2H: pominięty (waga ~0, składy radykalnie inne).
- Kalibracja: bez odchyleń od rynku >5 pp; sygnały kadrowe są już w linii, więc moje spready to korekty o 0,5 pkt, nie value.

## Podsumowanie (najlepszy rynek meczu)

| Mecz | Wynik (G-Go) | Spread/Total modelu | Najlepszy typ | p | Fair | Pewność |
|---|---|---|---|---|---|---|
| ORL - BOS | 106,75 - 113,75 | BOS -7 / 220,5 | BOS wygrywa | 72% | 1.39 | średnia |
| IND - BKN | 117,25 - 113,25 | IND -4 / 230,5 | IND wygrywa | 60% | 1.67 | niska |
| GSW - LAC | 110,75 - 107,75 | GSW -3 / 218,5 | GSW wygrywa | 57% | 1.75 | niska |
| LAL - TOR | 115,5 - 111,5 | LAL -4 / 227 | LAL wygrywa | 60% | 1.67 | niska-średnia |

Spready i totale to praktycznie rzut monetą względem linii (48-53%): brak mocnego typu, patrz sekcje meczów.

---

### Orlando Magic - Boston Celtics (01.11, 21:30 PL; 15:30 ET) - DraftKings: BOS -6,5, total 221,5
**Typ:** BOS wygrywa (ML) | **p:** 72% | **Fair odds:** 1.39 | **Pewność:** średnia
**Rynki dodatkowe:**

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| BOS ML | 72% | 1.39 | średnia |
| ORL ML | 28% | 3.57 | - |
| BOS -6,5 | 51% | 1.94 | niska (brak mocnego typu) |
| ORL +6,5 | 49% | 2.04 | niska |
| BOS -4,5 | 58% | 1.72 | niska-średnia |
| BOS -8,5 | 45% | 2.21 | niska |
| Under 221,5 | 52% | 1.92 | niska |
| Over 221,5 | 48% | 2.09 | niska |
| Total BOS Over 112,5 | 54% | 1.83 | niska |
| Total ORL Under 107,5 | 53% | 1.90 | niska |

**Rynki zawodnika (orientacyjne linie, niska pewność, nie na kupon):** Tatum pkt 27,0 śr.: Over 26,5 = 49,5% (fair 2,02), Over 28,5 = 39,6%; Franz Wagner pkt 20,5: Over 19,5 = 52% (fair 1,91); Bane pkt 21,0: Over 18,5 = 61% (fair 1,63), Over 20,5 = 49%. Bane i Wagner dostają większe użycie po absencji Banchero i Suggsa (+1 do +2 pkt w średniej).
**Statystyki drużyn:** BOS 4-1, net +9,8, ORtg 118,0, DRtg 108,1, pace 100,7 (5 meczów). ORL 2-3, net -7,6, DRtg 117,0 (28. miejsce), pace 100,8; u siebie 0-2.
**H2H:** pominięty (inne składy).
**Informacje medialne (ESPN/Rotowire, 01.11):** ORL bez Banchero (Out, kostka, do ~22.11), Suggsa (Out, kolano, do 10.11), Isaaca (Out), Penda i Nelson (Out). BOS: Mitchell Robinson Q (rest), Devin Carter Out; Tatum i George w grze według danych. Brak B2B. Absencje ORL są już w linii -6,5 (Orlando bez dwóch gwiazd obrońców).
**Oczekiwane punkty:** ORL 106,75 - BOS 113,75 (spread BOS -7, total 220,5).
**Ryzyka:** niepotwierdzony skład startowy; Robinson (zbiórki BOS) może odpocząć; mała próba ratingów; ORL grało przeciętną obronę, ale BOS ma tylko 5 meczów danych; blowout (spread 6,5 + słaby ORL) skraca minuty Tatuma.
**Rynek:** ML nieznany (feed pusty); spread -110/-110, total -112/-108.

---

### Indiana Pacers - Brooklyn Nets (01.11, 23:00 PL; 17:00 ET) - DraftKings: IND -3,5, total 231,5
**Typ:** IND wygrywa (ML) | **p:** 60% | **Fair odds:** 1.67 | **Pewność:** niska
**Rynki dodatkowe:**

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| IND ML | 60% | 1.67 | niska |
| BKN ML | 40% | 2.50 | - |
| IND -3,5 | 51% | 1.94 | niska (brak mocnego typu) |
| BKN +3,5 | 49% | 2.06 | niska |
| IND -5,5 | 45% | 2.20 | niska |
| BKN +5,5 | 55% | 1.83 | niska |
| Under 231,5 | 52% | 1.92 | niska |
| Over 231,5 | 48% | 2.09 | niska |
| Total IND Over 116,5 | 53% | 1.90 | niska |
| Total BKN Under 112,5 | 47% | 2.11 (Over 53% / 1.90) | niska |

**Rynki zawodnika (niska pewność, nie na kupon):** Siakam pkt 22,0: Over 20,5 = 55% (fair 1,81); zbiórki 7,8: Over 6,5 = 62% (fair 1,60); Nembhard (po absencji Haliburtona, ok. 36 min) asysty 8,5: Over 7,5 = 59% (fair 1,69), pkt 18,0: Over 16,5 = 56% (fair 1,79). Randle pkt 22 (BKN) Over 21,5 = 49%; Porter Jr. pkt 20,5 Over 19,5 = 52%. Toppin Q: bez typu.
**Statystyki drużyn:** IND 2-4, net -2,7, ORtg 112,9, DRtg 115,6, pace 103,5 (2. miejsce w sieci tempo). BKN 0-5, net -10,5, DRtg 115,2, TOV% 18,3, pace 103,1. Oba zespoły szybkie, z fatalną obroną, stąd total 231,5.
**H2H:** pominięty.
**Informacje medialne:** IND bez Haliburtona (Out, hamstring, do ~13.11), Zubaca (Out, kostka, nieaktywny na ten mecz), McConnella (Out), Furphy'ego, Sheppard'a; Nesmith probable, Toppin Q. BKN bez Mikela Browna Jr. (Out, rest), Bilodeau (Out, bark); Demin Out. Brak B2B. Skład BKN bez rezerwowego rozgrywającego, zbiórki IND osłabione bez Zubaca.
**Oczekiwane punkty:** IND 117,25 - BKN 113,25 (spread IND -4, total 230,5).
**Ryzyka:** Pacers bez dwóch kluczowych graczy (Haliburton, Zubac) i 0-2 u siebie; BKN 0-5 może mieć motywację, ale to najsłabsza drużyna ligi w rankingu netto; niepewność SD podniesiona do 13.
**Rynek:** spread -108/-112, total -110/-110; ML brak.

---

### Golden State Warriors - LA Clippers (02.11, 02:30 PL; 18:30 PT 01.11) - DraftKings: GSW -2,5, total 219,5
**Typ:** GSW wygrywa (ML) | **p:** 57% | **Fair odds:** 1.75 | **Pewność:** niska
**Rynki dodatkowe:**

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| GSW ML | 57% | 1.75 | niska |
| LAC ML | 43% | 2.33 | - |
| GSW -2,5 | 51% | 1.94 | niska (brak mocnego typu) |
| LAC +2,5 | 49% | 2.06 | niska |
| GSW -4,5 | 45% | 2.20 | niska |
| LAC +4,5 | 55% | 1.83 | niska |
| Under 219,5 | 52% | 1.92 | niska |
| Over 219,5 | 48% | 2.09 | niska |
| Under 217,5 | 48% | 2.09 | niska |
| Total GSW Over 109,5 | 54% | 1.83 | niska |
| Total LAC Under 107,5 | 49% | 2.04 (Over 51% / 1.96) | niska |

**Rynki zawodnika (niska pewność, nie na kupon):** Garland (LAC) pkt 24 (przy nieobecnych Ingramie, Bealu, Strusie): Over 22,5 = 55% (fair 1,82); Lendeborg (GSW, śr. 19,8) pkt Over 19,5 = ok. 55-58% (fair ~1,72-1,80), Podziemski pkt 17: Over 16,5 = 49%. Rynki Currym wykluczone (Out).
**Statystyki drużyn:** GSW 3-3, net +0,9, ORtg 116,3, DRtg 115,3, pace 100,2. LAC 1-4 (0-3 na wyjeździe), net -5,9, ORtg 104,4 (25. miejsce), TOV% 22,2% (najgorsze w lidze), pace 101,2.
**H2H:** pominięty.
**Informacje medialne:** GSW bez Curry'ego (Out, rest), Draymonda Greena (Out, plecy), Porzingisa, Moody'ego, Butlera (Out); Gui Santos probable. LAC bez Ingrama, Bealea, Strusa (wszyscy Out do ~8.11), Niederhausera. Oba zespoły osłabione; spadek ofensywy GSW bez Curry'ego (-5 do -7 pkt w różnicy) jest już w linii -2,5 (skoro faworytem pozostaje GSW, rynek mocno karze Clippers).
**Oczekiwane punkty:** GSW 110,75 - LAC 107,75 (spread GSW -3, total 218,5).
**Ryzyka:** GSW bez Curry'ego i Greena może mieć sporo gorszą ofensywę niż w mojej liczbie (obniżone o ok. 5 pkt względem ratingu); status Curry'ego "rest" - możliwa zmiana; niska próba; wyrównany mecz.
**Rynek:** spread -108/-112, total -115/-105 (Over)/(Under); ML brak.

---

### Los Angeles Lakers - Toronto Raptors (02.11, 03:00 PL; 19:00 PT 01.11) - DraftKings: LAL -4,5, total 227,5
**Typ:** LAL wygrywa (ML) | **p:** 60% | **Fair odds:** 1.67 | **Pewność:** niska-średnia
**Rynki dodatkowe:**

| Rynek | p | Fair | Pewność |
|---|---|---|---|
| LAL ML | 60% | 1.67 | niska-średnia |
| TOR ML | 40% | 2.50 | - |
| LAL -2,5 | 55% | 1.83 | niska |
| LAL -4,5 | 48% | 2.07 | niska (brak mocnego typu) |
| TOR +4,5 | 52% | 1.94 | niska |
| Under 227,5 | 51% | 1.96 | niska |
| Over 227,5 | 49% | 2.04 | niska |
| Under 225,5 | 47% | 2.14 | niska |
| Total LAL Over 114,5 | 54% | 1.86 | niska |
| Total TOR Over 111,5 | 50% | 2.00 | niska |

**Rynki zawodnika (niska pewność, nie na kupon):** Dončić pkt 36 śr.: Over 33,5 = 58% (fair 1,71), Over 34,5 = 54%; asysty 8: Over 7,5 = 53% (fair 1,88); zbiórki 7: Over 6,5 = 53%; trójki 5,2: Over 4,5 = 59% (fair 1,70); PRA 51: Over 48,5 = 58% (fair 1,73). Wszystkie rynki Dončicia silnie skorelowane i podatne na blowout/minuty; Reaves pkt 24: Over 22,5 = 55%; Barnes (TOR) pkt 24: Over 22,5 = 55%.
**Statystyki drużyn:** LAL 4-2 (wg ESPN 4-2), net +6,0, ORtg 119,3 (2. miejsce), DRtg 113,3, eFG% 59,2% (1.), pace 99,7. TOR 3-2, net +10,8 (próba 5 meczów), DRtg 103,9 (4. miejsce), pace 102,0.
**H2H:** pominięty.
**Informacje medialne:** TOR bez Kawhi Leonarda (Out, kolano, do ~23.11) i Bittle'a; LAL: Ziaire Williams Q (foot), Thiero Out. Dončić w pełnym wymiarze (35,9 min). Brak B2B po obu stronach; Raptors na końcu serii wyjazdowej (3-2).
**Oczekiwane punkty:** LAL 115,5 - TOR 111,5 (spread LAL -4, total 227).
**Ryzyka:** TOR ma najlepszą obronę z mocnych drużyn (DRtg 103,9) w małej próbie; Dončić Q-status brak, ale jego minuty/obciążenie; Raptors po późnej podróży na Zachód; spread wąski, więc nie ma mocnego typu na spread.
**Rynek:** spread -110/-110, total -110/-110; ML brak.

---

## Ranking (z wszystkich rynków, fair > 1.15)

| # | Mecz | Rynek | p | Fair | Pewność | Zależność |
|---|---|---|---|---|---|---|
| 1 | ORL-BOS | BOS ML | 72% | 1.39 | średnia | status Robinsona/Tatuma; kurs ML nieznany |
| 2 | LAL-TOR | LAL ML | 60% | 1.67 | niska-średnia | status Dončicia; kurs nieznany |
| 3 | IND-BKN | IND ML | 60% | 1.67 | niska | status Nesmith/Toppin; kurs nieznany |
| 4 | ORL-BOS | BOS -4,5 (alt) | 58% | 1.72 | niska-średnia | blowout/minuty |
| 5 | GSW-LAC | GSW ML | 57% | 1.75 | niska | Curry rest; kurs nieznany |

Mocnych typów na spread i total brak (wszystkie 47-53% względem linii). Rynki zawodnika: niska pewność, **bez rekomendacji na kupon** (brak drugiego źródła liczb i realnych linii/kursów).

## Tabela kandydatów na kupon
| Mecz | Rynek | p | Fair | Pewność | Od czego zależy | Kurs rynkowy |
|---|---|---|---|---|---|---|
| ORL-BOS | BOS ML | 72% | 1.39 | średnia | skład BOS, Robinson | nieznany (spread -110) |
| LAL-TOR | LAL ML | 60% | 1.67 | niska-średnia | Dončić pełny wymiar | nieznany |
| IND-BKN | IND ML | 60% | 1.67 | niska | Nesmith, Toppin | nieznany |
| GSW-LAC | GSW ML | 57% | 1.75 | niska | Curry rest | nieznany |

Przed użyciem w `bet-slip-builder` potrzebne są kursy ML (Betclic), bo feed DraftKings ich nie zwrócił. To oszacowania probabilistyczne, nie gwarancje.
