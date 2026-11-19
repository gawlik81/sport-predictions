# Analiza NBA - slate 13.11.2026 (USA), noc 14.11 czasu polskiego

Sprawdzenie danych: 13.11.2026 rano (ESPN injuries/pickcenter, stats.nba.com Advanced, ESPN standings, Superbet). Statusy GTD/Questionable mogą się zmienić do rozpoczęcia meczów; injury report NBA jest aktualizowany ok. 90 min przed meczem. `nba_daily_lineups` zwrócił 404 (brak potwierdzonych składów), więc składy to projekcje.

Źródła: stats.nba.com (net/off/def rating, pace; 10-13 meczów, mała próba), ESPN (injuries, tabela, linie DraftKings z pickcenter), Superbet (event 14588422: moneyline i total). BettingPros: nie użyty (brak klucza w sesji). Linie spreadu/totalu dla meczów poza Knicks@Pacers to DraftKings (ESPN), nie Superbet.

## Back-to-back

Wczorajszy slate (12.11 USA): TOR@PHI, DET@WSH, DAL@MIN, CHA@PHX. Żadna z 18 drużyn z tego slate'u nie grała 12.11, więc **nie ma back-to-back**. Część drużyn grała w środę 11.11 (NYK@CLE, MEM, UTA@MEM, HOU-GSW, SAS-CHI, POR@OKC, SAC-ORL 10.11): to 1 dzień przerwy, bez korekty, ale GSW po meczu w Houston (bójka Smart) i NYK/CLE po wspólnym meczu to tylko kontekst.

## Metoda

Tempo = średnia pace obu drużyn; punkty = pace/100 x (ORtg drużyny + DRtg rywala - 112.5) +/- 1.5 (parkiet). Następnie korekty za injury report (skala z SKILL.md) i **ściągnięcie do linii rynku** (early season: 10-13 meczów, rynek jest bardziej wiarygodny; bez konkretnej informacji nie schodzę z rynku >3 pkt). SD: 12-13 (różnica), 18-19 (suma), podniesione tam, gdzie 2+ statusów jest niejasnych.

Tabela surowa (przed korektami kadrowymi) vs rynek, różnica gospodarze-goście:

| Mecz | Model surowy (margin / total) | Rynek DK (margin / total) | Finalne punkty (gosp - goście) |
|---|---|---|---|
| IND-NYK | -5.4 / 218.6 | -6.5 / 219.5 | 106.3 - 112.5 |
| ORL-MIL | +12.5 / 224.8 | +9.5 / 223.5 | 116.0 - 106.5 |
| MIA-CLE | -3.7 / 234.4 | +2.5 / 236.5 | 118.3 - 117.3 |
| CHI-ATL | -14.7 / 243.4 | -7.5 / 245.5 | 117.8 - 127.3 |
| NOP-MEM | -10.0 / 235.5 | -3.5 / 235.5 | 113.0 - 119.5 |
| HOU-UTA | +23.6 / 220.0 | +16.5 / 219.5 | 119.0 - 100.5 |
| SAS-GSW | +6.5 / 230.4 | +12.5 / 220.5 | 116.8 - 105.2 |
| SAC-POR | -16.4 / 233.8 | -10.5 / 229.5 | 109.0 - 121.0 |
| LAC-OKC | -7.0 / 221.3 | -7.5 / 222.5 | 107.5 - 114.5 |

## Mecze

### Pacers - Knicks (14.11, 01:00; 13.11 USA) | Superbet 14588422
**Typ:** Knicks wygrywają | **p:** 71% | **Fair:** 1.41 | **Pewność:** średnia
| Rynek | p | Fair | Kurs rynkowy | Uwaga |
|---|---|---|---|---|
| Zwycięzca NYK (z dogr.) | 71.2% | 1.41 | Superbet 1.37 | EV < 0 |
| Spread NYK -6.5 | 49.0% | 2.04 | DK -110 ok. | bez przewagi |
| Total 219.5 Under | 51.6% | 1.94 | Superbet 220.5: Under 1.85 / Over 1.95 | bez przewagi |
**Staty:** NYK net +6.7 (ORtg 115.7, DRtg 109.0, pace 95.1, najwolniejsza drużyna ligi), 6-5, 6-4 w L10. IND net -1.9, 4-8, pace 101.1.
**Informacje:** IND bez Haliburtona (min. 10 dni), Shepparda, Furphy; Nesmith Q (kolano), McConnell probable. NYK bez wpisów w injury report (ESPN). Brak b2b.
**Punkty:** IND 106.3 - NYK 112.5 (spread NYK -6.2, total 218.8).
**Ryzyka:** Nesmith out obniża IND o ok. 1 pkt; wolne tempo NYK = więcej wariancji spreadu. Rynek zgodny z modelem, brak value.

### Magic - Bucks (14.11, 01:00)
**Typ:** Magic wygrywają | **p:** 76% | **Fair:** 1.31 | **Pewność:** średnia
| Rynek | p | Fair | Kurs (DK/sportsdata) | Uwaga |
|---|---|---|---|---|
| ORL ML | 76.4% | 1.31 | DK -378 (1.26), konsensus 1.23 | EV < 0 |
| ORL -9.5 | 50.0% | 2.00 | 1.90 | bez przewagi |
| Total 223.5 | Over 47.8% / Under 52.2% | 2.09 / 1.92 | - | bez przewagi |
**Staty:** MIL 1-11, net -14.5 (DRtg 120.7), 1-9 w L10; ORL net -5.0, 4-7.
**Informacje:** ORL bez Banchero (4-6 tyg.), Isaac, Suggs (ESPN: Out, w komentarzu questionable; niejasne), da Silva i Cain Q. MIL bez wpisów. Surowy model dawał ORL +12.5; odjąłem ok. 3 pkt za braki ORL.
**Punkty:** ORL 116.0 - MIL 106.5. **Ryzyka:** wiele Q po stronie ORL, SD podniesione do 12.5.

### Cavaliers - Heat (14.11, 02:00)
**Typ:** brak mocnego typu (p 45-55%) | **Pewność:** niska
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| MIA ML | 51.6% | 1.94 | DK 1.74 (-135) | EV < 0 |
| CLE ML | 48.4% | 2.07 | DK 2.14 | ok. 0 |
| Total 235.5 | 50/50 | 2.00 | - | bez przewagi |
**Staty:** CLE net +2.1 (pace 99.8), 6-6; MIA net -4.6 (DRtg 115.9, pace 102.8, 3. w lidze), 5-6.
**Informacje:** CLE bez Mobleya (Out), Merrill (Out). MIA: Antetokounmpo probable (nadgarstek), Klay Thompson Q (kostka), Larsson Q (choroba). Surowo CLE +3.7; za Mobleya -2.5 do -3 dla CLE, za niepełne MIA -1 -> MIA +1.0.
**Punkty:** MIA 118.3 - CLE 117.3. **Ryzyka:** status Giannisa (jeśli odpocznie, CLE faworytem o 4+); rynek MIA -2.5 mocniej stawia na MIA niż model.

### Hawks - Bulls (14.11, 02:00)
**Typ:** Hawks wygrywają | **p:** 80% | **Fair:** 1.25 | **Pewność:** średnia
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| ATL ML | 79.8% | 1.25 | DK -277 (1.36), sportsdata ok. 1.30 | rynek -277 = ok. 72% no-vig; model +8 pp, sprawdzić |
| ATL -7.5 | 56.6% | 1.77 | DK ok. 1.91 | przewaga ok. +6 pp, ale >5 pp od rynku |
| ATL -9.5 | 50.0% | 2.00 | - | - |
| Total 245.5 | 49.2% / 50.8% | 2.03 / 1.97 | - | bez przewagi |
**Staty:** CHI 1-9, net -15.1 (DRtg 124.2, najgorsza obrona ligi, pace 103.75); ATL net +2.1, 7-5, pace 103.5 (2. w lidze). Surowy model ATL -14.7.
**Informacje:** CHI bez Awaki, Caleba Wilsona; Powell (bark) i Swain (plecy) Q. ATL bez Gueye, Gilberta, Newella, Veesaara; Flemings Q.
**Punkty:** CHI 117.8 - ATL 127.3 (spread ATL -9.5). Skorygowałem tylko do -9.5 z -14.7 (ściągnięcie do rynku). **Ryzyka:** Powell/Swain zagrają = mniej, ATL gra szybko, więc wysokie SD (19).

### Pelicans - Grizzlies (14.11, 02:00)
**Typ:** Grizzlies wygrywają | **p:** 70% | **Fair:** 1.42 | **Pewność:** niska (zależy od statusów NOP)
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| MEM ML | 70.5% | 1.42 | DK -158 (1.63), sportsdata 1.57 | model +9 pp od rynku, tylko jeśli doubtful nie zagrają |
| MEM -3.5 | 59.1% | 1.69 | DK ok. 1.91 | przewaga warunkowa |
| MEM -6.5 | 50.0% | 2.00 | - | - |
| Total 235.5 | Under 56.3% | 1.78 | - | brak potwierdzenia, patrz ryzyka |
**Staty:** MEM net +5.8 (ORtg 116.4), 7-4, 6-4; NOP net -7.1 (DRtg 119.2), 4-8.
**Informacje:** NOP: Murphy (kolano), Mathurin (kciuk), Missi (kolano), McGowens (łokieć) doubtful, Watford Out (ESPN, ok. 13.11 rano). MEM: Edey (ankle management), Post (wstrząśnienie), Pippen Jr. Out.
**Punkty:** NOP 113.0 - MEM 119.5 (spread MEM -6.5, total 232.5). Surowo MEM -10; braki MEM (Edey) -3, braki NOP wliczone tylko częściowo (konserwatywnie), bo rynek -3.5 zdaje się nie wyceniać wszystkich doubtful. **Ryzyka:** Murphy/Mathurin zagrają -> MEM -3.5 do -4 i wartość znika; SD 13 / 19. Typ warunkowy, nie wariant główny kuponu.

### Jazz - Rockets (14.11, 02:30)
**Typ:** Rockets wygrywają | **p:** 92% | **Fair:** 1.08 (poniżej progu 1.15, pomijać w rankingach) | **Pewność:** wysoka (ML), średnia (spread)
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| HOU ML | 92.5% | 1.08 | DK -1580 | pomijam |
| HOU -16.5 | 56.4% | 1.77 | DK ok. 1.91 | przewaga ok. +5 pp |
| HOU -17.5 | 53.2% | 1.88 | - | - |
| Total 219.5 | 50/50 | 2.00 | - | bez przewagi |
**Staty:** UTA 1-11, 0-10 w L10, net -11.6; HOU net +9.2 (DRtg 109.3, pace 97.4), 9-3.
**Informacje:** UTA bez Markkanena (złamanie dłoni), Jacksona Jr. (MCL, 6-8 tyg.), Nurkicia, Alexandera. HOU: Smart zawieszony (3 mecze, bójka z GSW), Capela i Adams Out (rezerwy podkoszowe; powrót ok. 15.11). Surowo HOU +23.6, finalnie +18.5.
**Punkty:** HOU 119.0 - UTA 100.5. **Ryzyka:** blowout (spread >10) skraca minuty gwiazd, więc rynki zawodnika HOU tylko Under/ostrożnie; zmęczenie po środowym meczu z GSW.

### Warriors - Spurs (14.11, 03:30)
**Typ:** Spurs wygrywają | **p:** 80% | **Fair:** 1.24 | **Pewność:** średnia
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| SAS ML | 80.3% | 1.24 | DK -700 (1.14), sportsdata 1.14 | EV < 0, pomijać |
| SAS -12.5 | 47.2% | 2.12 | - | GSW +12.5: 52.8% / fair 1.90 |
| Total 220.5 | Over 53.1% / Under 46.9% | 1.88 / 2.13 | Superbet/DK 220.5 | model 222.0, bez konkretu; ściągnięte do rynku |
**Staty:** SAS 10-2, 10-0 w L10, net +11.0 (ORtg 119.3, DRtg 108.3); GSW net +7.5 (liczone z Currym).
**Informacje:** GSW bez Curry'ego (naddarcie mięśnia brzucha, 2 tyg.), Butlera (kolano), Porzingisa, Moody'ego, B. Williamsa; Bassey probable. SAS: Fox (biodro) i Vassell (przywodziciel) Q; Harris Out. Surowo SAS +6.5, po odjęciu Curry'ego (-5 do -6) i ew. Fox'a +11.6.
**Punkty:** SAS 116.8 - GSW 105.2. **Ryzyka:** Fox out = -2 i spread bliżej 10; Wembanyama i blowout (spread 12.5) obniżają minuty gwiazd SAS. Spread bez przewagi.

### Trail Blazers - Kings (14.11, 04:00)
**Typ:** Blazers wygrywają | **p:** 85% | **Fair:** 1.17 (granica progu) | **Pewność:** średnia
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| POR ML | 85.1% | 1.17 | DK -515 (1.19), sportsdata 1.18 | EV ok. +/-0 |
| POR -10.5 | 55.0% | 1.82 | DK ok. 1.91 | przewaga ok. +4 pp |
| POR -11.5 | 51.7% | 1.94 | - | - |
| Total 229.5 | 51/49 | 2.00 | - | bez przewagi |
**Staty:** SAC 1-10, net -12.1, DRtg 119.3; POR 8-3, net +7.1 (ORtg 118.5).
**Informacje:** POR bez Morant (poza grą), Sharpe'a (menisk, 6 mies.), Krejciego, Youngblooda; SAC bez Simmonsa (Achilles), Raynauda; Achiuwa Q. Surowo POR -16.4; po koszcie braków POR -12.
**Punkty:** SAC 109.0 - POR 121.0. **Ryzyka:** POR gra bez czterech rotacyjnych graczy, więc forma 8-3 może być zawyżona; SAC ma słabą obronę, ale wygrywa mecze rzadko.

### Thunder - Clippers (14.11, 04:30)
**Typ:** Thunder wygrywają | **p:** 73% | **Fair:** 1.38 | **Pewność:** średnia
| Rynek | p | Fair | Kurs | Uwaga |
|---|---|---|---|---|
| OKC ML | 72.6% | 1.38 | DK -283 (1.35), sportsdata 1.34 | EV < 0 |
| OKC -7.5 | 48.4% | 2.07 | DK ok. 1.91 | bez przewagi |
| Total 222.5 | 48.9% / 51.1% | 2.05 / 1.96 | - | bez przewagi |
**Staty:** OKC net +4.2 (DRtg 108.3, pace 98.75), 8-4, 6-4; LAC 2-8, net -5.8, pace 101.
**Informacje:** OKC bez J. Williamsa (operacja, złamanie strzałki), Holmgrena (kolano), Wallace'a, Sorbera, Jaylina Williamsa; Mitchell (kostka) Q. LAC bez Ingrama (Achilles), Beala, Niederhausera. Rating OKC mógł nie uwzględnić wszystkich braków (surowy model +7.0 dla OKC = rynek).
**Punkty:** LAC 107.5 - OKC 114.5. **Ryzyka:** Mitchell out = -1.5 do -2 dla OKC; zespół osłabiony (formacja bez dwóch topowych graczy), SD 12.5.

## Rynki zawodnika

Nie wyceniłem rynków zawodnika: brak potwierdzonych składów (`nba_daily_lineups` 404), wielu zawodników w statusie Q/doubtful, a przy drugim niezależnym źródle średnich (Basketball-Reference/CtG) nie sprawdziłem logów meczowych; zgodnie z SKILL.md bez dwóch źródeł i potwierdzenia statusu nie rekomenduję typu. Do ponownej weryfikacji po injury reporcie (ok. 90 min przed meczami).

## Ranking kandydatów (bez fair <= 1.15; z oznaczeniem warunków)

| # | Mecz | Rynek | p | Fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|---|
| 1 | Hawks-Bulls | ATL -7.5 | 56.6% | 1.77 | niska/średnia | Powell/Swain, +6 pp od rynku | DK ok. 1.91 (nie Superbet) |
| 2 | Pelicans-Grizzlies | MEM -3.5 | 59.1% | 1.69 | niska | NOP doubtful (Murphy, Mathurin, Missi) | DK ok. 1.91 |
| 3 | Rockets-Jazz | HOU -16.5 | 56.4% | 1.77 | średnia | blowout, Smart/Capela/Adams out | DK ok. 1.91 |
| 4 | Blazers-Kings | POR -10.5 | 55.0% | 1.82 | średnia | brak 4 rotacyjnych POR | DK ok. 1.91 |
| 5 | Knicks-Pacers | NYK ML | 71.2% | 1.41 | średnia | Nesmith Q | Superbet 1.37 (EV < 0) |
| 6 | Thunder-Clippers | OKC ML | 72.6% | 1.38 | średnia | Mitchell Q | DK 1.35 (EV < 0) |
| 7 | Magic-Bucks | ORL ML | 76.4% | 1.31 | średnia | Suggs/da Silva Q | 1.23-1.26 (EV < 0) |

Pominięte (fair <= 1.15 lub kurs rynkowy < fair): HOU ML 1.08, SAS ML (fair 1.24, kurs 1.14). Mecze bez mocnego typu: Cavaliers-Heat; wszystkie totale (p w granicach 47-53%).

Uwaga: rynek NBA jest efektywny, a próba sezonu to 10-13 meczów. Linie spreadu w tabeli nie są kursami Superbet (poza Knicks@Pacers). Kursy spreadu i totalu na Superbet należy sprawdzić `superbet_event_odds` przed kuponem (event_id: ORL-MIL 15434212, MIA-CLE 15434211, CHI-ATL 15434214, NOP-MEM 15434210, HOU-UTA 15434213, SAS-GSW 14588418, SAC-POR 15437216, LAC-OKC 15437217).

To oszacowania probabilistyczne, nie gwarancje; statusy zawodników mogą się zmienić do rozpoczęcia meczów.
