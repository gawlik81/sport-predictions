# Analiza NBA - noc 13/14.11.2026 (czas PL), odświeżenie wieczorne

Wersja odświeżona ok. 22:45 CET 13.11.2026 względem `Analiza_NBA_2026-11-13.md` (09:18). Dziewięć meczów, start 01:00-04:30 14.11 (PL).

Źródła: ESPN injuries (`site.api.espn.com`, znacznik 21:41Z; statusy i komentarze RotoWire), `nba_daily_lineups` (przewidywane składy, wszystkie "Expected", bez potwierdzenia), `nba_odds_today` (FanDuel, Novibet, Mozzartbet: spread i moneyline; **bez totali**), Superbet (event 14588422: moneyline, handicap, total 221.5), stats.nba.com `leaguedashplayerstats` (średnie na mecz, 2026-27). BettingPros nie użyty (brak klucza). Totale i kursy Superbet poza IND-NYK **nie zostały odświeżone**: totale to linie z rana (DK/ESPN), kursy spreadu/ML to FanDuel/Novibet z 22:40. Przed kuponem sprawdzić `superbet_event_odds`.

Back-to-back: brak (żadna z 18 drużyn nie grała 12.11). Statusy mogą się zmienić do tipoffu (injury report NBA ok. 90 min przed meczem).

## Zmiany względem poprzedniej wersji

| Mecz | Zmiana | Wpływ na liczby |
|---|---|---|
| IND-NYK | Linia ruszyła o 2 pkt: NYK -6.5 -> **-8.5** (FanDuel, Mozzart: otwarcie 6.5), Superbet NYK ML 1.37 -> **1.27**, total 220.5 -> 221.5. Nesmith nadal Q (ESPN), McConnell probable; brak potwierdzonej przyczyny ruchu | Nesmith traktowany jako prawdopodobnie Out: margin NYK -6.2 -> **-7.5**, total 218.8 -> 220.5; p NYK 71.2% -> **73.1%** (SD 13) |
| ORL-MIL | Suggs: ESPN status "Out", ale komentarz (shootaround, Q) i skład "Expected" go wymieniają; da Silva, Cain nadal Q; Banchero, Isaac, Penda Out | Nie wiadomo, czy Suggs zagra: margin ORL -9.5 -> **-9.0**, SD 12.5; p ORL 76.4% -> **75.2%** |
| MIA-CLE | Larsson **Q -> doubtful** (choroba), Klay Thompson **probable**; Mobley Out potwierdzony, Giannis bez wpisu | MIA margin +1.0 -> **+0.7**; p MIA 51.6% -> **50.6%** |
| CHI-ATL | Statusy bez zmian: Powell, Swain, Flemings nadal Q; Awaka, Gilbert, Newell Out | Liczby bez zmian (ATL -9.5, p 77.9%); p w tabeli ściągnięte do 75% (rynek ok. 70%) |
| NOP-MEM | **Murphy Q/doubtful -> Out, Missi doubtful -> Out, McGowens Out, Watford Out, nowy: D. Murray Out**; Mathurin nadal Q; MEM: Edey, Post, Pippen Out | NOP traci kolejne ok. 2.5 pkt: margin MEM -6.5 -> **-7.0** (nie więcej, bo rynek -3.5 się nie ruszył), p MEM 70.5% -> **71.8%**, w tabeli ściągnięte do 68% |
| HOU-UTA | Linia HOU -16.5 -> **-15.5** (FanDuel, Mozzart), ML 1.091 | Margin -18.5 -> **-17.5**; p HOU 92.5% -> 90.5% (fair 1.11, pomijany) |
| SAS-GSW | Fox i Vassell nadal Q; Curry Out (2 tyg.), Butler, Porzingis (odszedł z koszykówki), Moody Out; Bassey probable | Bez zmian w kadrach; linia SAS -11.5/-12.5; model bez zmian (-11.6) |
| SAC-POR | **Achiuwa Q -> Out** (SAC), Youngblood Out (POR); Morant, Krejci, Sharpe Out | SAC margin POR -12.0 -> **-12.5**; p POR 85.1% -> **84.1%** (spread liczony od niższego punktu SAC 108.8); ML POR 1.217 |
| LAC-OKC | Sorber **Out**, "Mitchell Q" to **Ajay Mitchell** (kostka, ma być w składzie Expected); Ingram, Beal Out | Bez zmian punktów (OKC -7.0), p 72.6% |

Wniosek ogólny: przy NOP-MEM i IND-NYK zmiany statusów (lub ruch linii) są realne; w pozostałych meczach korekty są małe. Sygnał ryzyka (status Q/doubtful) zmienia p tylko tam, gdzie jest informacja (NOP, MIA, SAC, ORL, IND).

## Tabela rynków (p modelu, fair odds, kurs rynkowy i EV)

Kursy: FD = FanDuel/Novibet z `nba_odds_today` (22:40), SB = Superbet. EV = p x kurs - 1. "Ściągnięte" = p obniżone do max ok. +5-7 pp ponad rynek bez vig, zgodnie z regułami skilla (early season, 10-13 meczów).

| Mecz (PL) | Rynek | p | Fair | Kurs | EV | Pewność |
|---|---|---|---|---|---|---|
| IND-NYK 01:00 | NYK ML | 73.1% | 1.37 | SB 1.27 | -7% | średnia |
| | NYK -8.5 | 46.9% | 2.13 | SB 1.95, FD 1.909 | -9% | średnia |
| | IND +8.5 | 53.1% | 1.88 | SB 1.83 | -3% | średnia |
| | Total 221.5 Under / Over | 52.2% / 47.8% | 1.92 / 2.09 | SB (kurs total nie pobrany) | n/d | niska |
| | Total drużyny: IND 106.5, NYK 114.0 | ok. 50% przy linii = średniej | 2.00 | brak linii | n/d | niska |
| ORL-MIL 01:00 | ORL ML | 75.2% | 1.33 | FD 1.256 | -6% | średnia |
| | ORL -9.5 / MIL +9.5 | 48.4% / 51.6% | 2.07 / 1.94 | FD 1.909 | -8% / -1.5% | niska (Suggs) |
| | Total 223.5 Under / Over | 51.9% / 48.1% | 1.93 / 2.08 | brak | n/d | niska |
| | Total drużyny ORL 115.8, MIL 106.8 | ok. 50% | 2.00 | brak | n/d | niska |
| MIA-CLE 02:00 | MIA ML / CLE ML | 50.6% / 49.4% | 1.97 / 2.03 | FD 1.746 / 2.14 | -12% / +6% | niska (brak mocnego typu) |
| | MIA -2.5 / CLE +2.5 | 44.3% / 55.7% | 2.26 / 1.79 | FD 1.943 / 1.877 | -14% / +5% | niska |
| | Total 235.5 Under / Over; 236.5 Under | 50.4% / 49.6%; 52.5% | 1.98 / 2.02; 1.90 | brak | n/d | niska |
| | Total drużyny MIA 118.0, CLE 117.3 | ok. 50% | 2.00 | brak | n/d | niska |
| CHI-ATL 02:00 | ATL ML | 75% (model 77.9%, ściągnięte) | 1.33 | FD 1.364 | +2% | średnia |
| | ATL -7.5 | 54% (model 56.1%) | 1.85 | FD 1.98 | +7% | niska/średnia |
| | ATL -9.5 | 50.0% | 2.00 | brak | n/d | - |
| | Total 245.5 Under / Over | 50.8% / 49.2% | 1.97 / 2.03 | brak | n/d | niska |
| | Total drużyny CHI 117.8, ATL 127.3 | ok. 50% | 2.00 | brak | n/d | niska |
| NOP-MEM 02:00 | MEM ML | 68% (model 71.8%, ściągnięte) | 1.47 | FD 1.602 | +9% | niska (warunek: Mathurin) |
| | MEM -3.5 | 58% (model 60.6%) | 1.72 | FD 1.926 | +12% | niska |
| | MEM -5.5 / -6.5 | 54.6% / 51.5% | 1.83 / 1.94 | brak | n/d | niska |
| | Total 232.5 Under / Over; 235.5 Under | 49.8% / 50.2%; 56.1% | 2.01 / 1.99; 1.78 | brak | n/d | niska |
| | Total drużyny NOP 112.8, MEM 119.8 | ok. 50% | 2.00 | brak | n/d | niska |
| HOU-UTA 02:30 | HOU ML (pomijany) | 90.5% | 1.11 | FD 1.091 | -1% | wysoka (ML), fair <= 1.15 |
| | HOU -15.5 | 54% (model 56.1%) | 1.85 | FD 1.909 | +3% | średnia |
| | HOU -16.5 / -17.5 | 53.1% / 50.0% | 1.88 / 2.00 | brak | n/d | średnia |
| | Total 219.5 Under / Over | 50 / 50% | 2.00 | brak | n/d | niska |
| | Total drużyny HOU 118.5, UTA 101.0 | ok. 50% | 2.00 | brak | n/d | niska |
| SAS-GSW 03:30 | SAS ML | 80.3% | 1.25 | FD 1.154 | -7% | średnia |
| | SAS -11.5 / GSW +11.5 | 50.3% / 49.7% | 1.99 / 2.01 | FD 1.87 / 1.952 | -6% / -3% | średnia |
| | SAS -12.5 / GSW +12.5 | 47.2% / 52.8% | 2.12 / 1.90 | Novibet 1.94 / 1.86 | -8% / -2% | średnia |
| | Total 220.5 Over / Under (ściągnięte) | 51% / 49% | 1.96 / 2.04 | brak | n/d | niska |
| | Total drużyny SAS 116.8, GSW 105.2 | ok. 50% | 2.00 | brak | n/d | niska |
| SAC-POR 04:00 | POR ML | 84.1% | 1.19 | FD 1.217 | +2% | średnia |
| | POR -10.5 | 54% (model 56.1%) | 1.85 | FD 1.962 | +6% | średnia |
| | POR -11.5 / -12.5 | 53.1% / 50.0% | 1.88 / 2.00 | brak | n/d | średnia |
| | Total 229.5 Over / Under | 51.3% / 48.7% | 1.95 / 2.05 | brak | n/d | niska |
| | Total drużyny SAC 108.8, POR 121.3 | ok. 50% | 2.00 | brak | n/d | niska |
| LAC-OKC 04:30 | OKC ML | 72.6% | 1.38 | FD 1.345 | -2% | średnia |
| | OKC -7.5 / LAC +7.5 | 48.4% / 51.6% | 2.07 / 1.94 | FD 1.926 / 1.893 | -7% / -2% | średnia |
| | Total 222.5 Under / Over | 51.1% / 48.9% | 1.96 / 2.05 | brak | n/d | niska |
| | Total drużyny LAC 107.5, OKC 114.5 | ok. 50% | 2.00 | brak | n/d | niska |

Total drużyny: zgodnie z regułą ze SKILL.md (Under poniżej rynku bez konkretu = przesunięcie modelu) nie podaję przewagi; p ok. 50% przy linii równej średniej, wartość nie do wykorzystania bez linii Superbet.

## Mecze (skrót: stan na 22:45)

**IND-NYK (01:00):** NYK net +6.7, najwolniejsze tempo ligi (pace 95.1); IND bez Haliburtona (min. 10 dni), Sheppard, Furphy; Nesmith Q, McConnell probable. Przewidywane składy: Brunson, Hart, Bridges, Anunoby, Towns vs Nembhard, Nesmith, Oubre, Siakam, Zubac. Punkty IND 106.5 - NYK 114.0. Ryzyka: Nesmith zagra (spread bliżej -6), wolne tempo = wysoka wariancja. Rynek poszedł mocniej na NYK niż model; brak przewagi.

**ORL-MIL (01:00):** MIL 1-11, 1-9 w L10; ORL bez Banchero, Isaac, Penda; Suggs niejasny, da Silva i Cain Q. ORL 115.8 - MIL 106.8. Ryzyka: wielu Q po stronie ORL (SD 12.5), rynek -9.5 = model.

**MIA-CLE (02:00):** brak mocnego typu. Giannis (27.7 pkt, 12.6 zb.) bez wpisu w ESPN, Klay probable, Larsson doubtful; CLE bez Mobleya i Merrilla. MIA 118.0 - CLE 117.3. Jedyny rynek z formalnym EV > 0 (CLE +2.5 / CLE ML) opiera się na niskiej pewności; jest to rozbieżność modelu z rynkiem, nie przewaga.

**CHI-ATL (02:00):** CHI 1-9, najgorsza obrona ligi (DRtg 124.2); Powell, Swain Q, Awaka i Wilson Out; ATL bez Gueye, Gilberta, Newella, Veesaara, Flemings Q. CHI 117.8 - ATL 127.3. Ryzyka: Powell i Swain zagrają, wysoka SD 19 (pace obu drużyn w czołówce). Rynek -7.5 vs model -9.5: najlepszy kandydat po spreadzie.

**NOP-MEM (02:00):** NOP bez Murphy'ego, Missi, Murraya, McGowensa, Watforda (Mathurin Q); MEM bez Edeya, Posta, Pippena. MEM +5.8 net, NOP -7.1. NOP 112.8 - MEM 119.8. Typ warunkowy i niskiej pewności: rynek -3.5 mógł już wycenić Outs, a model (-7.0) odchodzi od rynku o 3.5 pkt (przy ściągnięciu p do 68%/58%). Ryzyka: Mathurin zagra i garstka NOP zagra ponad oczekiwania.

**HOU-UTA (02:30):** UTA 1-11 (0-10 w L10), bez Markkanena, Jacksona Jr., Nurkicia, Alexandra; HOU: Smart zawieszony, Capela i Adams Out (powrót 15-16.11). HOU 118.5 - UTA 101.0. Ryzyka: blowout; rynki zawodnika HOU tylko Under.

**SAS-GSW (03:30):** GSW bez Curry'ego (2 tyg.), Butlera, Porzingisa (zakończył karierę/odszedł), Moody'ego, B. Williamsa. SAS 10-2; Fox i Vassell Q. SAS 116.8 - GSW 105.2. Ryzyka: Fox out = spread bliżej 10; blowout skraca minuty Wembanyamy.

**SAC-POR (04:00):** SAC 1-10, bez Simmonsa, Raynauda, Achiuwy; POR bez Moranta, Sharpe'a, Krejciego, Youngblooda (POR forma 8-3 mogła być zawyżona). SAC 108.8 - POR 121.3. Ryzyka: 4 braki rotacji POR.

**LAC-OKC (04:30):** OKC bez J. Williamsa, Holmgrena, Wallace'a, Sorbera, Jaylina Williamsa; Ajay Mitchell Q; LAC bez Ingrama, Beala, Niederhausera. LAC 107.5 - OKC 114.5. Ryzyka: Mitchell out = -1.5 dla OKC; brak przewagi względem rynku.

## Rynki zawodnika (cena modelowa przy liniach referencyjnych)

**Pewność niska dla wszystkich: jedno źródło liczb (stats.nba.com, sezon, 8-12 meczów), brak linii rynkowych Superbet/FD, brak potwierdzonych składów (wszystkie "Expected").** Zgodnie ze SKILL.md nie rekomenduję żadnego z poniższych na kupon; to wycena do zestawienia z linią bukmachera po pobraniu `superbet_event_odds`. Średnie skorygowane o skład (+0.5 do +1.5 pkt przy brakach rywala/własnych) i o blowout (HOU -15.5: Durant, Sengun -2 pkt).

| Mecz | Zawodnik, rynek (średnia modelu) | Linia | Over p / fair | Under p / fair |
|---|---|---|---|---|
| IND-NYK | Brunson pkt (26.0) | 24.5 / 26.5 | 54.7% / 1.83; 44.4% / 2.25 | 45.3%; 55.6% |
| | Towns zb. (12.8) | 11.5 / 12.5 | 59.6% / 1.68; 50.0% | 40.4%; 50.0% |
| | Siakam pkt (23.5, bez Haliburtona) | 21.5 / 23.5 | 57.8% / 1.73; 46.7% / 2.14 | 42.2%; 53.3% |
| | Nembhard ast (7.6) | 6.5 / 7.5 | 61.2% / 1.63; 48.0% | 38.8%; 52.0% |
| ORL-MIL | Wagner pkt (23.5) | 22.5 | 52.2% / 1.92 | 47.8% |
| | Herro pkt (21.9) | 20.5 / 22.5 | 54.6% / 1.83; 43.3% | 45.4%; 56.7% |
| | Carter zb. (9.5) | 8.5 / 9.5 | 57.8% / 1.73; 46.7% | 42.2%; 53.3% |
| | Bane trójki (3.5) | 2.5 / 3.5 | 67.2% / 1.49; 46.1% | 32.8%; 53.9% |
| MIA-CLE | Giannis pkt (27.7) | 26.5 | 53.0% / 1.89 | 47.0% |
| | Giannis zb. (12.4) | 11.5 / 12.5 | 55.8% / 1.79; 46.2% | 44.2%; 53.8% |
| | D. Mitchell pkt (23.8, bez Mobleya) | 22.5 / 23.5 | 53.8% / 1.86; 48.4% | 46.2%; 51.6% |
| | Davion Mitchell ast (8.3) | 7.5 | 56.9% / 1.76 | 43.1% |
| CHI-ATL | Alexander-Walker pkt (21.9) | 20.5 | 54.6% / 1.83 | 45.4% |
| | Alexander-Walker trójki (3.9) | 2.5 / 3.5 | 74.0% / 1.35; 54.2% / 1.84 | 26.0%; 45.8% |
| | J. Johnson PRA (35.0) | 33.5 | 54.8% / 1.82 | 45.2% |
| NOP-MEM | Jerome pkt (26.2) | 24.5 | 55.8% / 1.79 | 44.2% |
| | Boozer zb. (10.5, bez Edeya/Posta) | 9.5 | 57.4% / 1.74 | 42.6% |
| | Zion pkt (22.7, bez Murphy'ego) | 21.5 | 53.4% / 1.87 | 46.6% |
| HOU-UTA | Durant pkt (18.5, blowout) | 20.5 | 34.8% | **65.2% / 1.53** |
| | K. George pkt (22.0, bez Markkanena/Jacksona) | 20.5 | 55.2% / 1.81 | 44.8% |
| SAS-GSW | Wembanyama pkt (28.5, blowout) | 27.5 | 52.0% / 1.92 | 48.0% |
| | Wembanyama zb. (10.8) | 10.5 | 50.0% | 50.0% |
| | Lendeborg pkt (22.5, bez Curry'ego) | 20.5 | 57.9% / 1.73 | 42.1% |
| SAC-POR | Acuff pkt (25.6; min 37) | 24.5 | 52.6% / 1.90 | 47.4% |
| | Sabonis zb. (12.8) | 12.5 | 50.0% | 50.0% |
| | Avdija pkt (24.0, bez Moranta/Sharpe'a) | 22.5 | 54.9% / 1.82 | 45.1% |
| LAC-OKC | Gilgeous-Alexander pkt (29.0) | 28.5 | 49.5% | 50.5% |
| | Garland pkt (21.5, bez Ingrama/Beala) | 20.5 | 52.3% / 1.91 | 47.7% |

Jedyna cena z wyraźną przewagą nad 50%: Durant Under 20.5 pkt (65%), ale przy nieznanej linii i blowout-assumption (spread HOU -15.5) - niska pewność, warunkowa. Rynki tego samego zawodnika (pkt + PRA) są skorelowane.

## Kandydaci (bez fair <= 1.15; wszystkie rynki)

| # | Mecz | Rynek | p | Fair | Kurs (źródło) | EV | Pewność | Zależy od |
|---|---|---|---|---|---|---|---|---|
| 1 | CHI-ATL | ATL -7.5 | 54% | 1.85 | FD 1.98 | +7% | niska/średnia | Powell, Swain, Flemings |
| 2 | SAC-POR | POR -10.5 | 54% | 1.85 | FD 1.962 | +6% | średnia | blowout/minuty, braki POR |
| 3 | NOP-MEM | MEM -3.5 | 58% | 1.72 | FD 1.926 | +12% | niska | Mathurin Q, model +3.5 pkt od rynku |
| 4 | NOP-MEM | MEM ML | 68% | 1.47 | FD 1.602 | +9% | niska | j.w. |
| 5 | MIA-CLE | CLE +2.5 | 55.7% | 1.79 | FD 1.877 | +5% | niska | Giannis/Klay, rynek MIA |
| 6 | HOU-UTA | HOU -15.5 | 54% | 1.85 | FD 1.909 | +3% | średnia | blowout, Smart/Capela out |
| 7 | CHI-ATL | ATL ML | 75% | 1.33 | FD 1.364 | +2% | średnia | Powell/Swain |
| 8 | SAC-POR | POR ML | 84.1% | 1.19 | FD 1.217 | +2% | średnia | fair 1.15-1.20 (granica) |

Pominięte: HOU ML (fair 1.11), SAS ML (EV < 0, SB/FD 1.14-1.154), NYK ML (SB 1.27, fair 1.37 - EV < 0), ORL ML (EV < 0), OKC ML (EV < 0). Wszystkie totale i total drużyny: p w granicach 47-53%, bez przewagi. Kursy FD/Novibet to nie Superbet; przed kuponem sprawdzić Superbet (event_id: IND-NYK 14588422, ORL-MIL 15434212, MIA-CLE 15434211, CHI-ATL 15434214, NOP-MEM 15434210, HOU-UTA 15434213, SAS-GSW 14588418, SAC-POR 15437216, LAC-OKC 15437217).

To oszacowania probabilistyczne, nie gwarancje; statusy zawodników mogą się zmienić do rozpoczęcia meczów.
