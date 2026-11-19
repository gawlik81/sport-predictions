# Analiza NHL, noc 12/13.11.2026 (czas polski), część B

Skill: `nhl-analyst`. Sprawdzone 12.11.2026 (dzień meczów). Źródła: NHL API (tabela, terminarz, goalie leaders), Pinnacle (ML z OT, 60' 3-way, puck line, total; kursy amerykańskie przeliczone na dziesiętne, marża usunięta), Bettors Insider / The Lines / Dimers (props i kontekst CHI, FLA-DET). Modele: `nhl_model.py`, `nhl_props.py`.

**Ograniczenia danych (wpływają na pewność):**
- Żaden bramkarz startowy nie jest potwierdzony (rano w dniu meczu brak publicznego potwierdzenia dla tych 5 meczów). Pewność każdego rynku jest więc co najwyżej średnia, a rynki bramkarza i zawodnika bez typu.
- xG/CF%/GSAx nie pobrano (brak dostępu); λ opiera się na GF/GA z tabeli, ostatnich seriach, linii rynku i korektach z `SKILL.md`. Początek sezonu (16-19 meczów) to mała próba.
- H2H nie znaleziono w użytecznej postaci (waga w NHL niska, pominięte).
- Kursy Superbet dla tych meczów: brak (connector pokazuje tylko ligi e-hokeja). Kursy odniesienia to Pinnacle (nie do kuponu Superbet). BettingPros nie użyty w tej analizie.
- 60' 3-way: model Poissona zaniża remisy (16-17% vs ok. 22-24% w lidze i 23-24% w cenach Pinnacle), więc w tabelach podaję remis skorygowany do ok. 21%, a 1/2 przeskalowane proporcjonalnie.

## Kontekst terminarza (back-to-back, tabela)

| Drużyna | Mecz | Bilans / GF-GA | Poprzedni mecz | B2B |
|---|---|---|---|---|
| Detroit | 19 | 7-9-3, 51-59, L4 | 10.11 w St. Louis 2-3 | nie (1 dzień przerwy) |
| Florida | 19 | 10-7-2, 60-56, W1 | 10.11 w Columbus 4-1 | nie |
| Buffalo | 18 | 8-7-3, 53-65, L2 | 11.11 u siebie 3-8 z TBL | TAK, wyjazd do Chicago |
| Chicago | 18 | 4-13-1, 39-76 (GA 4,22), L4 | brak meczu 11.11 | nie |
| Winnipeg | 19 | 8-8-3, 53-65, W4 | 10.11 u siebie 4-2 z NJD | nie, ale wyjazd |
| Dallas | 17 | 10-5-2, 49-41, W1 | brak meczu 10-11.11 | nie, wypoczęta |
| St. Louis | 18 | 8-8-2, 53-55, W1 | 10.11 u siebie 3-2 z DET | TAK, wyjazd do Utah |
| Utah | 19 | 10-8-1, 66-68, L2 | 11.11 w Vegas 3-5 | TAK (5 wyjazdów z rzędu, teraz dom) |
| NY Islanders | 17 | 7-6-4, 49-52, OT x2 | 09.11 w San Jose 2-3 | nie (2 dni) |
| Los Angeles | 16 | 5-9-2, 45-55, L2 | 10.11 u siebie 0-3 z NSH | nie |

Goalie leaders NHL (sezon): Oettinger (DAL) GAA 1,99, 9 W, 3 SO (top); Tarasov (DET) .919 / 2,10; Hofer (STL) .920 / 2,33; Sorokin (NYI) .914; Forsberg (LAK) GAA 2,44. Chicago: Spencer Knight .881 / 3,66 (The Lines/Bettors Insider, niepotwierdzony jako starter). Winnipeg: w przekazach Skinner (niepotwierdzony; Hellebuyck jest już w NJ).

---

### Detroit Red Wings @ Florida Panthers (13.11, 01:30 PL; 12.11 19:30 ET)
**Typ:** brak mocnego typu (ML Florida 59%) | **Pewność:** niska/średnia (bramkarze niepotwierdzeni)
**λ:** FLA 3,25 - DET 2,75 (łącznie 6,0). Uzasadnienie: gospodarze +0,1; DET PK 69,5% (28. w lidze) daje FLA +0,1; FLA 3,16 GF/g; DET seria L4, ale kryzys faworyta nie jest korygowany. Rynek: Pinnacle total 6,0 (-103/-109), FLA ML -167 (61,0% bez marży).

| Rynek | p | fair | kurs Pinnacle | Pewność |
|---|---|---|---|---|
| ML (z OT) Florida / Detroit | 59% / 41% | 1,69 / 2,44 | 1,60 / 2,50 | średnia |
| 60' 3-way: FLA / remis / DET | 47% / 21% / 32% | 2,13 / 4,76 / 3,13 | 2,02 / 4,24 / 3,23 | niska |
| Puck line FLA -1,5 | 33,5% | 2,98 | 2,54 | niska |
| Puck line DET +1,5 | 66,5% (po korekcie do rynku 64%) | 1,50 (1,56) | 1,57 | niska |
| Total Over 5,5 / Under 5,5 | 55% / 45% | 1,82 / 2,22 | 1,76 / 2,12 | niska |
| Total Over 6,5 / Under 6,5 | 42,5% / 57,5% | 2,35 / 1,74 | 2,17 / 1,73 | niska |
| Total 6,0 (linia rynku) Over / Under | 49% / 51% | 2,04 / 1,96 | 1,97 / 1,92 | niska |

Rynki zawodnika: Verhaeghe gol +1,95 (Hard Rock, The Lines): przy średniej 0,30 gola/mecz p = 26%, fair 3,86 vs kurs 2,95 (implied 34%): brak value, bez typu. Strzały/obrony bramkarza: brak linii i startera, bez wyceny.
**Ryzyka:** zmiana bramkarza (Tarasov .919 po B2B-free dniu; Bobrovsky vs rezerwowy), gole w OT w totalu, przewaga rynku nad modelem w ML FLA (1,9 pp, w granicach).

---

### Buffalo Sabres @ Chicago Blackhawks (13.11, 02:00 PL; 12.11 20:00 ET)
**Typ:** ML Buffalo 59% (zgodny z rynkiem 59,3%; brak value) | **Pewność:** średnia dla ML, niska dla reszty
**λ:** CHI 2,85 - BUF 3,45 (łącznie 6,3). Uzasadnienie: CHI GA 4,22/g (31. w lidze), Knight .881, 1 wygrana w ostatnich 10; BUF drugi dzień B2B po 3-8 (-0,1 gola i gorsza obrona uwzględnione, bez nich BUF ~3,55). BUF ma też GA 3,6/g, więc CHI nie jest zerowe. Rynek: Pinnacle total 6,5 (-103/-109), BUF ML -155.

| Rynek | p | fair | kurs Pinnacle | Pewność |
|---|---|---|---|---|
| ML (z OT) Buffalo / Chicago | 59% / 41% | 1,69 / 2,44 | 1,65 / 2,40 | średnia |
| 60' 3-way: BUF / remis / CHI | 48% / 21% / 31% | 2,08 / 4,76 / 3,23 | 1,97 / 4,32 / 3,07 | niska |
| Puck line BUF -1,5 | 35% | 2,86 | 2,61 | niska |
| Puck line CHI +1,5 | 65% | 1,54 | 1,54 | niska |
| Total Over 5,5 / Under 5,5 | 59% / 41% | 1,69 / 2,44 | 1,62 / 2,39 | niska/średnia |
| Total Over 6,5 / Under 6,5 | 47,5% / 52,5% | 2,11 / 1,90 | 1,97 / 1,92 | niska |

Rynki zawodnika: Tage Thompson gol +140 (Bettors Insider; Dimers 45%): moja średnia 0,47 gola/mecz (słaby bramkarz CHI .881) daje p = 37,5%, fair 2,67 vs kurs 2,40 (implied 41,7%): brak value, bez typu. Obrony bramkarza: niepotwierdzony starter, bez typu.
**Ryzyka:** B2B po 3-8 (rezerwowy bramkarz BUF = realne ryzyko, wtedy p BUF spada o 3-5 pp), CHI gra u siebie z dużą zmiennością, pusta bramka podbija różnice (puck line).

---

### Winnipeg Jets @ Dallas Stars (13.11, 02:00 PL; 12.11 20:00 ET)
**Typ:** ML Dallas 62% (fair 1,61) | **Pewność:** średnia (Oettinger prawdopodobnie startuje, bez potwierdzenia)
**λ:** DAL 3,15 - WPG 2,40 (łącznie 5,55). Uzasadnienie: DAL najlepsza obrona (2,4 GA/g), Oettinger GAA 1,99, wypoczęci; WPG 3,4 GA/g, Skinner. WPG 4 wygrane z rzędu, ale to forma underdoga, bez wpływu na dodatnią korektę. Rynek: Pinnacle DAL ML -170 (61,4% bez marży), total 5,5 (Over -117 / Under +104).

| Rynek | p | fair | kurs Pinnacle | Pewność |
|---|---|---|---|---|
| ML (z OT) Dallas / Winnipeg | 62% / 38% | 1,61 / 2,63 | 1,59 / 2,53 | średnia |
| 60' 3-way: DAL / remis / WPG | 51% / 21% / 28% | 1,96 / 4,76 / 3,57 | 1,95 / 4,26 / 3,28 | niska |
| Puck line DAL -1,5 | 36,5% | 2,74 | 2,52 | niska |
| Puck line WPG +1,5 | 63,5% | 1,57 | 1,58 | niska |
| Total Over 5,5 / Under 5,5 | 50% / 50% (model 48/52, skorygowane do rynku) | 2,00 / 2,00 | 1,86 / 2,04 | niska |
| Total Over 6,5 / Under 6,5 | 36% / 64% | 2,78 / 1,56 | 2,31 / 1,72 | niska |

Rynki zawodnika: bez linii i potwierdzenia składu, brak wyceny. Obrony Oettingera: dopiero po potwierdzeniu startera (oczekiwane strzały WPG ~27-29).
**Ryzyka:** rezerwowy w bramce DAL (Oettinger gra często, ale B2B brak), Skinner po serii 4 wygranych, gole w OT. Under 5,5 z p 50% vs rynek 47,5%: przewaga niewielka, nie traktować jako value.

---

### St. Louis Blues @ Utah Mammoth (13.11, 03:00 PL; 12.11 21:00 ET)
**Typ:** brak mocnego typu (ML Utah 53%) | **Pewność:** niska
**λ:** UTA 3,10 - STL 2,90 (łącznie 6,0). Oba zespoły drugi dzień B2B (UTA przegrała 3-5 w Vegas po 5 wyjazdach z rzędu i wraca do domu; STL grała 10.11 u siebie z DET, potem przelot do Utah). Korekty B2B po -0,1 dla obu, więc się znoszą; UTA ma ofensywę (3,5 GF/g) i słabą defensywę (3,6 GA/g), Hofer .920 u STL (jeśli gra B2B; często gra rezerwowy, wtedy STL słabiej). Rynek: Pinnacle UTA -114 (51,9% bez marży), total 6,0 (-105/-107).

| Rynek | p | fair | kurs Pinnacle | Pewność |
|---|---|---|---|---|
| ML (z OT) Utah / St. Louis | 53% / 47% | 1,89 / 2,13 | 1,88 / 2,03 | niska |
| 60' 3-way: UTA / remis / STL | 42,5% / 21% / 36,5% | 2,35 / 4,76 / 2,74 | 2,36 / 4,21 / 2,57 | niska |
| Puck line UTA -1,5 | 29% | 3,45 | 3,15 | niska |
| Puck line STL +1,5 | 71% | 1,41 | 1,40 | niska |
| Total Over 5,5 / Under 5,5 | 55% / 45% | 1,82 / 2,22 | 1,75 / 2,14 | niska |
| Total Over 6,5 / Under 6,5 | 42,5% / 57,5% | 2,35 / 1,74 | 2,16 / 1,74 | niska |
| Total 6,0 Over / Under | 49% / 51% | 2,04 / 1,96 | 1,95 / 1,94 | niska |

Rynki zawodnika: bez linii/składu, brak wyceny.
**Ryzyka:** podwójne B2B = zwiększona szansa rezerwowych w obu bramkach (zwykle +0,2-0,4 gola dla rywala), wyższa wariancja totalu; to mecz do pominięcia.

---

### New York Islanders @ Los Angeles Kings (13.11, 04:00 PL; 12.11 22:00 ET)
**Typ:** brak mocnego typu (ML LA 52%) | **Pewność:** niska
**λ:** LAK 3,00 - NYI 2,90 (łącznie 5,9). Uzasadnienie: LAK słabsza ofensywa (2,8 GF/g) i słaba obrona (3,4 GA/g), seria L2 (0-3 z NSH); NYI 7-6-4, dwa mecze z rzędu do OT, Sorokin .914, 2 dni odpoczynku, ale długi przelot na zachód. Forsberg (LAK) GAA 2,44. Rynek: Pinnacle LAK -123 (53,8% bez marży), total 6,0 (-102/-110).

| Rynek | p | fair | kurs Pinnacle | Pewność |
|---|---|---|---|---|
| ML (z OT) LA / NYI | 52% / 48% | 1,92 / 2,08 | 1,81 / 2,11 | niska |
| 60' 3-way: LAK / remis / NYI | 41% / 21% / 38% | 2,44 / 4,76 / 2,63 | 2,28 / 4,14 / 2,69 | niska |
| Puck line LAK -1,5 | 27,5% | 3,64 | 3,06 | niska |
| Puck line NYI +1,5 | 72,5% | 1,38 | 1,42 | niska |
| Total Over 5,5 / Under 5,5 | 54% / 46% | 1,86 / 2,17 | 1,78 / 2,10 | niska |
| Total Over 6,5 / Under 6,5 | 41% / 59% | 2,44 / 1,69 | 2,18 / 1,72 | niska |
| Total 6,0 Over / Under | 47% / 53% | 2,13 / 1,89 | 1,98 / 1,91 | niska |

Rynki zawodnika: bez linii/składu, brak wyceny.
**Ryzyka:** rynek faworyzuje LA o 1,8 pp więcej niż model (w granicach 5 pp), bramkarz niepotwierdzony, dogrywka (NYI 2 mecze z rzędu).

---

## Zbiorcza tabela: mecz | rynek | linia | p | fair | pewność

| Mecz | Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|---|
| DET @ FLA | ML (z OT) | FLA | 59% | 1,69 | średnia |
| DET @ FLA | 60' 3-way | FLA / X / DET | 47 / 21 / 32% | 2,13 / 4,76 / 3,13 | niska |
| DET @ FLA | Puck line | DET +1,5 | 64-66% | 1,50-1,56 | niska |
| DET @ FLA | Puck line | FLA -1,5 | 33,5% | 2,98 | niska |
| DET @ FLA | Total | Over 5,5 / Under 5,5 | 55% / 45% | 1,82 / 2,22 | niska |
| DET @ FLA | Total | Over 6,5 / Under 6,5 | 42,5% / 57,5% | 2,35 / 1,74 | niska |
| BUF @ CHI | ML (z OT) | BUF | 59% | 1,69 | średnia |
| BUF @ CHI | 60' 3-way | BUF / X / CHI | 48 / 21 / 31% | 2,08 / 4,76 / 3,23 | niska |
| BUF @ CHI | Puck line | CHI +1,5 | 65% | 1,54 | niska |
| BUF @ CHI | Puck line | BUF -1,5 | 35% | 2,86 | niska |
| BUF @ CHI | Total | Over 5,5 / Under 5,5 | 59% / 41% | 1,69 / 2,44 | niska/średnia |
| BUF @ CHI | Total | Over 6,5 / Under 6,5 | 47,5% / 52,5% | 2,11 / 1,90 | niska |
| BUF @ CHI | Gracz | T. Thompson gol (Over 0,5) | 37,5% | 2,67 | niska (bez typu) |
| WPG @ DAL | ML (z OT) | DAL | 62% | 1,61 | średnia |
| WPG @ DAL | 60' 3-way | DAL / X / WPG | 51 / 21 / 28% | 1,96 / 4,76 / 3,57 | niska |
| WPG @ DAL | Puck line | WPG +1,5 | 63,5% | 1,57 | niska |
| WPG @ DAL | Puck line | DAL -1,5 | 36,5% | 2,74 | niska |
| WPG @ DAL | Total | Over 5,5 / Under 5,5 | 50% / 50% | 2,00 / 2,00 | niska |
| WPG @ DAL | Total | Over 6,5 / Under 6,5 | 36% / 64% | 2,78 / 1,56 | niska |
| STL @ UTA | ML (z OT) | UTA | 53% | 1,89 | niska |
| STL @ UTA | 60' 3-way | UTA / X / STL | 42,5 / 21 / 36,5% | 2,35 / 4,76 / 2,74 | niska |
| STL @ UTA | Puck line | STL +1,5 | 71% | 1,41 | niska |
| STL @ UTA | Puck line | UTA -1,5 | 29% | 3,45 | niska |
| STL @ UTA | Total | Over 5,5 / Under 5,5 | 55% / 45% | 1,82 / 2,22 | niska |
| STL @ UTA | Total | Over 6,5 / Under 6,5 | 42,5% / 57,5% | 2,35 / 1,74 | niska |
| NYI @ LAK | ML (z OT) | LAK | 52% | 1,92 | niska |
| NYI @ LAK | 60' 3-way | LAK / X / NYI | 41 / 21 / 38% | 2,44 / 4,76 / 2,63 | niska |
| NYI @ LAK | Puck line | NYI +1,5 | 72,5% | 1,38 | niska |
| NYI @ LAK | Puck line | LAK -1,5 | 27,5% | 3,64 | niska |
| NYI @ LAK | Total | Over 5,5 / Under 5,5 | 54% / 46% | 1,86 / 2,17 | niska |
| NYI @ LAK | Total | Over 6,5 / Under 6,5 | 41% / 59% | 2,44 / 1,69 | niska |

## Kandydaci i wnioski

- Najmocniejsze ML: Dallas 62% (fair 1,61) i Buffalo 59% (fair 1,69) oraz Florida 59% (fair 1,69). Wszystkie bliskie rynkowi bez marży (różnica <= 2 pp), więc brak EV względem Pinnacle: kurs Pinnacle DAL 1,59, BUF 1,65, FLA 1,60 daje EV od -1% do -6%. Nie ma tu typu z wyraźną przewagą.
- Puck line +1,5 (DET, CHI, WPG, STL, NYI) ma p 63-72%, fair 1,38-1,57 (powyżej progu 1,15), kursy Pinnacle zbliżone do fair (EV ok. 0%, najlepiej NYI +1,5 przy 1,42 vs p 72,5%: EV +3%, nie przekracza niepewności modelu).
- Totaly: bez konkretnych sygnałów (bramkarze niepotwierdzone); Under 6,5 (p 52-64%) i Over 5,5 w BUF @ CHI (59%, CHI GA 4,22/g, bramkarz .881) to jedyne rynki z umiarkowanym uzasadnieniem, ale pewność niska.
- Meczów do pominięcia: STL @ UTA (podwójne B2B) i NYI @ LAK (wyrównany).
- Przed kuponem: sprawdzić starterów (DailyFaceoff, po porannych skate'ach) i kursy Superbet; zmiana bramkarza zmienia p o 3-5 pp.

Szacunki probabilistyczne, nie gwarancje; skład i bramkarze mogą się zmienić do rozpoczęcia meczu.
