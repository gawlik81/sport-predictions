# Analiza NBA + NHL, noc 06->07.11.2026 (czas polski)

Terminarz: 9 meczów NBA i 3 NHL (data USA 06.11). Źródła: stats.nba.com, ESPN, NHL API, Pinnacle, BettingPros (limity 429), DraftKings (ESPN). Statusy graczy i bramkarze do potwierdzenia przed meczem.


---

# NBA - noc 06->07.11.2026 (data USA 06.11) - analiza (nba-analyst)
Sprawdzono: 06.11.2026 ok. 11:30 CET. Źródła: ESPN (scoreboard, game_summary: injuries, last5, H2H, kursy DraftKings), stats.nba.com (nba_stats_call: Advanced team, per-game player), nba_daily_lineups (UWAGA: feed zwrócił nieaktualne/projektowane składy - gameId 0022600025-33 to mecze z początku sezonu, więc statusów z niego NIE używam), BettingPros (klucz ustawiony; po 20 propsach HTTP 429, więc tylko 20 linii).
Wszystkie 3 drużyny po dniu wolnym (ostatni mecz 04.11 wieczorem USA) - brak back-to-back. Próbka: 8-9 meczów na drużynę (early season), p i SD skorygowane do rynku, SD marży 12-12.5, sumy 18-18.5.
Wszystkie statusy DTD mogą się zmienić do rozpoczęcia (injury report ok. 90 min przed meczem). Brak potwierdzonych składów -> żadne rynki zawodnika nie mają pewności "wysoka".

## 1) Washington Wizards @ Atlanta Hawks (07.11 01:00 CET; 19:00 ET)
Rynek (DraftKings/ESPN): ATL -6.5 (-110), total 227.5 (o-115/u-105; otwarcie 230.5), ML ATL -257 / WAS +211 (bez marży 69.2% / 30.8%).
Statystyki: ATL 5-4, ORtg 112.5, DRtg 109.9, net +1.8, pace 102.8 (6. w lidze); 115.8-113.0 ppg, wyjazdy 4-2, dom 1-2. WAS 4-4, ORtg 110.0, DRtg 109.8, net +0.2, pace 99.1, 29% z trzech (w sezonie), 108.9-109.0 ppg.
H2H: ATL wygrało 04.11 w Waszyngtonie 120-105 (2 dni wcześniej); H2H waży mało, mecz rewanżowy; pokazuje przewagę ATL w tempie.
Kadry: ATL - Jalen Johnson DTD (kostka, 18.3 pkt/9.0 zb/7.9 ast, 32.6 min), Out: Landale (rez. C, 15 min), Gilbert, Newell, Gueye. WAS - Anthony Davis DTD (skręcona kostka; 23.4/9.3), Out: Vukcevic, Beekman, Champagnie, Watkins. Spadek totalu 230.5->227.5 sugeruje rynkowy sygnał kadrowy (niepotwierdzony).
Oczekiwane punkty: ATL 115.5 - WAS 110.0 (spread -5.5, total 225.5). Model vs rynek: ATL ML 65.5% -> skorygowano do 67% (rynek 69%).
| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| ML ATL | - | 67% | 1.49 | średnia (fair <1.5, bliskie progu) |
| ML WAS | - | 33% | 3.03 | niska |
| ATL spread | -4.5 | 53.2% | 1.88 | niska |
| ATL spread | -5.5 | 50.0% | 2.00 | niska |
| ATL spread | -6.5 | 46.8% | 2.14 | niska (rynek) |
| WAS spread | +6.5 | 53.2% | 1.88 | niska-średnia |
| WAS spread | +7.5 | 56.4% | 1.77 | niska-średnia |
| WAS spread | +8.5 | 59.5% | 1.68 | niska-średnia |
| Total Over | 221.5 / 223.5 / 225.5 / 227.5 / 229.5 | 58.6 / 54.3 / 50.0 / 45.7 / 41.4% | 1.71 / 1.84 / 2.00 / 2.19 / 2.41 | niska |
| Total Under | 225.5 / 227.5 / 229.5 | 50.0 / 54.3 / 58.6% | 2.00 / 1.84 / 1.71 | niska (U227.5 = rynek +4 pp, brak konkretu) |
| Total ATL | 113.5 / 115.5 / 117.5 | O 57.2 / 50.0 / 42.8% | 1.75 / 2.00 / 2.34 | niska |
| Total WAS | 108.5 / 110.5 / 112.5 | O 55.4 / 48.2 / 41.0% (średnia 110) | 1.80 / 2.08 / 2.44 | niska |
Rynki zawodnika (średnie z 8-9 meczów, minuty niepotwierdzone; spread <10, blowout niskie ryzyko):
- Trae Young asysty (śr. 9.5, model 9.3): O8.5 56.5% (1.77), U9.5 55.3% (1.81). Punkty (19.6): O17.5 61.5% (1.63), O19.5 49%. BettingPros P+A 30.5 (o-105/u-114), proj 29 -> Under: U30.5 ~57% (zgodne z BP). Pewność: średnia.
- N. Alexander-Walker punkty (21.7, model 21.5): O19.5 58.1% (1.72), O20.5 52.3%, O22.5 41.1%; trójki (4.1/mecz, model 3.6 po shrinkage): O2.5 69.0% (1.45), O3.5 48.2%. Pewność: średnia (stabilny starter, brak flag).
- Anthony Davis (DTD, tylko jeśli zagra; model z dyskontem 22 pkt): punkty O20.5 55.2% (1.81); zbiórki (9.3) O8.5 55.6% (1.80); PRA (34): O31.5 59.8%, O33.5 50%, U35.5 59.5% (BettingPros linia 35.5, proj 36.8 -> Over; NIEZGODNOŚĆ z moim Under, flaga, brak typu). Pewność: niska (status).
- Jalen Johnson (DTD, 18.3/9.0/7.9): BettingPros PRA 37.5 (o-111/u-114), proj 41.7 Over, ale l10 2-8 Over; Under moje (śr. 35.2) ~60%, niezgodne z BP -> brak typu. Pewność: niska.
- CJ McCollum (BP): P+R/P+A linie 19.5; brak własnej bazy -> pominięty.
Ryzyka: Johnson i Davis DTD (gwiazda ATL out = -3 do -4 pkt marży; Davis out = WAS -3, total -2); rewanż po 15 pkt przewagi ATL; wysoka wariancja tempa ATL (pace 102.8); early season.
Najlepszy rynek: WAS +7.5/+8.5 (nieznacznie) lub Under 227.5; żaden mocny typ - mecz "brak mocnego typu" na zwycięzcę (fair 1.49).

## 2) Boston Celtics @ Charlotte Hornets (07.11 01:00 CET; 19:00 ET)
Rynek: BOS -8.5 (-115/-105), total 209.5 (o-111/u-109; otwarcie 210.5), ML BOS -337 / CHA +271 (bez marży 74.1% / 25.9%).
Statystyki: BOS 6-2 (dom 5-0, wyjazdy 1-2), ORtg 115.8, DRtg 109.2, net +6.6, pace 97.6; 114.3-108.3 ppg; ostatnie 5: 4-1. CHA 3-6 (L5), ORtg 101.5 (30.), DRtg 112.7, net -11.2, pace 96.8, 98.1 ppg, 40% FG, 19.4 strat/mecz (najwięcej w lidze, TOV% 20.1).
H2H: brak meczów w tym sezonie (0-0); kolejne 03.12, 24.01, 05.02.
Kadry: CHA - Kon Knueppel Out (hamstring, do 09.11), Grant Williams Out; DTD: Dennis Schroder (udo, 10.2 pkt/4.9 ast), Moussa Diabate (udo; 8.9/9.1 zb); Coby White (GP 2, 17 min - po powrocie, ograniczone minuty). BOS - Payton Pritchard DTD (oko, 13.0 pkt), Out: Devin Carter (choroba).
Oczekiwane punkty: BOS 110.0 - CHA 101.0 (spread BOS -9.0, total 211). Model ML BOS 78.6% -> do 77% (rynek 74%, różnica 3 pp: dwie kontuzje CHA).
| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| ML BOS | - | 77% | 1.30 | średnia |
| ML CHA | - | 23% | 4.35 | niska |
| BOS spread | -6.5 / -7.5 / -8.5 / -9.5 / -10.5 | 58.3 / 55.0 / 51.7 / 48.3 / 45.0% | 1.72 / 1.82 / 1.94 / 2.07 / 2.22 | niska-średnia (spread = rynek) |
| CHA spread | +8.5 / +9.5 / +10.5 | 48.3 / 51.7 / 55.0% | 2.07 / 1.94 / 1.82 | niska |
| Total Over | 205.5 / 207.5 / 209.5 / 211.5 / 213.5 | 62.0 / 57.7 / 53.3 / 48.9 / 44.5% | 1.61 / 1.73 / 1.88 / 2.05 / 2.25 | niska-średnia (O209.5 vs rynek: +3 pp) |
| Total Under | 209.5 / 211.5 / 213.5 | 46.7 / 51.1 / 55.5% | 2.14 / 1.96 / 1.80 | niska |
| Total BOS | 108.5 / 110.5 / 112.5 | O 55.4 / 48.2 / 41.0% | 1.80 / 2.08 / 2.44 | niska |
| Total CHA | 99.5 / 101.5 / 103.5 | O 55.4 / 48.2 / 41.0% (śr. 101) | 1.80 / 2.08 / 2.44 | niska; Under CHA nie przesuwamy poniżej rynku (brak linii) |
Rynki zawodnika (spread 8.5-9 -> lekkie ryzyko blowoutu: Tatum -2 min, śr. 27 -> 25.8):
- Jayson Tatum (7 meczów, 35.1 min): punkty (model 25.8): O24.5 53.7% (1.86), U26.5 56.7% (1.76); zbiórki 5.8: O5.5 50%; asysty 7.5: O6.5 59.9% (1.67). Pewność: średnia (asysty), niska (punkty).
- Paul George trójki (3.4/mecz, model 3.2): O2.5 61.4% (1.63), U3.5 60.4% (1.66). Pewność: średnia.
- Brandon Miller (CHA; po wypadnięciu Knueppela +użycie; 22.0 pkt, model 22.5): O20.5 57.9% (1.73), O22.5 46.7%; trójki (3.0): O2.5 57.1% (1.75). Ryzyko: blowout CHA nie szkodzi punktom aż tak (gra do końca), ale low-ORtg. Pewność: średnia.
- Moussa Diabate zbiórki (DTD, 9.1; model 8.8): O7.5 61.6% (1.62), O8.5 50% - tylko jeśli zagra (warunkowy; nie wariant główny).
- BettingPros: Sam Hauser pkt 7.5 (o-130/u100), proj 8.8; Coby White (DTD) kolejny rynek 1.5 (o-120/u122), proj 2.7 - brak własnej bazy, pominięte.
Ryzyka: BOS 1-2 na wyjeździe, wolne tempo (96.8-97.6) obniża wariancję (korzyść Under/CHA+ spread), ale dwie drużyny podatne na straty; Pritchard/Schroder/Diabate statusy; CHA dzień wolny po 5 porażkach z rzędu (brak b2b). Kurs ML BOS fair 1.30 (>1.15; pozwala w kuponach).
Najlepszy rynek: ML BOS (77%, ale rynek 74%: value minimalne) / Tatum asysty O6.5 / P. George trójki O2.5.

## 3) Philadelphia 76ers @ Cleveland Cavaliers (07.11 01:30 CET; 19:30 ET)
Rynek: PHI -2.5 (-108/-112), total 228.5 (o-112/u-108; otwarcie 233.5 - spadek o 5), ML PHI -148 / CLE +124 (bez marży 57.2% / 42.8%).
Statystyki: PHI 8-1 (W5, wyjazdy 4-0), ORtg 110.5, DRtg 105.1 (2. w lidze), net +5.4, pace 100.3, 13.0 strat/mecz (najmniej); 111.0-105.2 ppg. CLE 4-4 (L2: 2 mecze z OKC), ORtg 115.6 (5.), DRtg 113.7 (22.), net +1.9, pace 101.7, 119.3-117.1 ppg, 47.5 zb/mecz, dom 3-1.
H2H: PHI wygrało 22.10 u siebie 114-106 (CLE - PHI). Rewanż na wyjeździe, skład CLE wtedy inny (Harden w obu).
Kadry: CLE - Jarrett Allen DTD (kolano; 13.3/7.8), Peyton Watson DTD (udo; 10.8 pkt, 28.6 min), Tyrese Proctor DTD (kostka), Jaylon Tyson Out. PHI - Adem Bona DTD (plecy), Out: Barlow, Hukporti. Embiid (7 meczów, 33.4 min) i Brown oznaczeni DTD tylko w BettingPros (ESPN ich nie wymienia) -> niepotwierdzone, ryzyko load management. Spadek totalu -5 pkt sugeruje sygnał kadrowy lub wolniejszy styl.
Oczekiwane punkty: PHI 114.0 - CLE 112.5 (spread PHI -1.5, total 226.5). ML PHI 56.4% ~ rynek 57.2% -> p 55.5%.
| Rynek | Linia | p | fair | Pewność |
|---|---|---|---|---|
| ML PHI | - | 55.5% | 1.80 | niska (mecz wyrównany, brak mocnego typu) |
| ML CLE | - | 44.5% | 2.25 | niska |
| PHI spread | -1.5 / -2.5 / -3.5 | 50.0 / 46.8 / 43.6% | 2.00 / 2.14 / 2.29 | niska |
| CLE spread | +1.5 / +2.5 / +3.5 | 50.0 / 53.2 / 56.4% | 2.00 / 1.88 / 1.77 | niska |
| Total Over | 222.5 / 224.5 / 226.5 / 228.5 / 230.5 | 58.6 / 54.3 / 50.0 / 45.7 / 41.4% | 1.71 / 1.84 / 2.00 / 2.19 / 2.41 | niska |
| Total Under | 226.5 / 228.5 / 230.5 | 50.0 / 54.3 / 58.6% | 2.00 / 1.84 / 1.71 | niska (U228.5 54%, wobec rynku 52% po devig - rynek już zrobił spadek) |
| Total PHI | 112.5 / 114.5 / 116.5 | O 55.4 / 48.2 / 41.0% (śr. 114) | 1.80 / 2.08 / 2.44 | niska |
| Total CLE | 110.5 / 112.5 / 114.5 | O 57.2 / 50.0 / 42.8% | 1.75 / 2.00 / 2.34 | niska |
Rynki zawodnika (spread <3, brak blowoutu; minuty pełne):
- Tyrese Maxey (28.0 pkt, 37 min; BettingPros pkt 25.5 o-103/u108, proj 26.8; l10 8-2 Over; model 27.5): O25.5 57.2% (1.75), O27.5 47%, U29.5 62.6%. P+A 33.4/mecz, BP linia 30.5 (o-105/u+103), model 33: O30.5 60.3% (1.66; zgodne z BP). Pewność: średnia.
- Joel Embiid (DTD tylko w BP; 19.6/10.0/4.4, 33.4 min): zbiórki O8.5 61.0% (1.64), O9.5 50%; punkty O17.5 55.6%; PRA (model 34): U34.5 54.8% (BP linia 34.5, proj 33 -> Under, zgodne). Tylko po potwierdzeniu składu. Pewność: niska.
- LeBron James (15.7/7.4/7.4): punkty O14.5 54.1% (1.85); asysty O6.5 53.4%; zbiórki O6.5 57.6% (1.74). Pewność: niska-średnia.
- Jaylen Brown (21.8/6.9/3.9; BP PRA 30.5 o-106/u-125 DTD; BP proj 29 Under): PRA model 33: O31.5 55%, brak zgodności z BP -> brak typu.
- Donovan Mitchell (22.5/5.0/5.5, BP P+A 30.5 o-105/u-106, proj 33.7 Over; l10 4-6): moje P+A 28 -> U30.5 ~60% (niezgodne z BP) -> brak typu. Evan Mobley (18.8/8.3/3.5; BP P+A 22.5 o+102/u-104, proj 23.7): PRA model 30.5: O28.5 57.8%. Jarrett Allen (DTD kolano): P+R (21.1) O20.5 ~59.5% tylko jeśli zagra (warunkowy).
- Peyton Watson (DTD udo; BP PRA 19.5 o-110/u-120; proj 20.7) - niepotwierdzony, pominięty.
Ryzyka: Allen/Watson DTD (CLE bez Allena: zbiórki PHI rosną, margin -2 dla CLE), Embiid/Brown niepotwierdzony load management (PHI bez Embiida: -4 do -5 w marży), CLE dom 3-1, PHI wyjazd 4-0 i seria W5; spadek totalu o 5 punktów (sygnał). Mecz wyrównany: brak mocnego typu na zwycięzcę.
Najlepszy rynek: Maxey O25.5 pkt / Maxey P+A O30.5 oraz LeBron zbiórki O6.5 (obie warunkowe od składu).

## Ranking kandydatów na kupon (wszystkie rynki, fair >1.15)
| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|
| BOS@CHA | ML BOS | 77% | 1.30 | średnia | Pritchard DTD | DK -337 (1.30) |
| BOS@CHA | Tatum asysty O6.5 | 59.9% | 1.67 | średnia | blowout | brak |
| BOS@CHA | P. George trójki O2.5 | 61.4% | 1.63 | średnia | minuty | brak |
| PHI@CLE | Maxey P+A O30.5 | 60.3% | 1.66 | średnia | skład PHI | BP o-105 (1.95) |
| PHI@CLE | Maxey pkt O25.5 | 57.2% | 1.75 | średnia | minuty | BP o-103 (1.97) |
| WAS@ATL | N. Alexander-Walker trójki O2.5 | 69.0% | 1.45 | średnia | shrinkage 4.1->3.6 | brak |
| WAS@ATL | NAW pkt O19.5 | 58.1% | 1.72 | średnia | - | brak |
| WAS@ATL | Trae Young ast O8.5 | 56.5% | 1.77 | średnia | AD/Johnson | brak |
| WAS@ATL | ML ATL | 67% | 1.49 | średnia | Johnson DTD | DK -257 (1.39) |
| BOS@CHA | Miller pkt O20.5 | 57.9% | 1.73 | średnia | Knueppel out | brak |
Typy bez mocnej przewagi: wszystkie spready i totale (model blisko rynku +-3 pp), ML PHI/CLE (wyrównane).

Przypomnienie: to oszacowania probabilistyczne, nie gwarancje; statusy DTD mogą się zmienić do rozpoczęcia meczu.

---

# NBA - noc 06->07.11.2026 (data USA 06.11), 3 mecze (nba-analyst)
Sprawdzono: 06.11.2026 ok. 12:30 CET. Statusy mogą się zmienić do meczu. To oszacowania probabilistyczne, nie gwarancje.
Źródła: stats.nba.com (nba_stats_call, advanced teams + per-game players, sezon 2026-27, 8-9 GP = mała próba), ESPN injuries/scoreboard, nba_daily_lineups (projected, "Expected"), nba_odds_today (Novibet/FanDuel/Mozzartbet; tylko ML i spread), BettingPros (total + ML; spread/ML dla 2 meczów odcięte limitem 429; props niedostępne).
Back-to-back: żadna z 6 drużyn nie gra b2b (wszystkie grały 04.11 USA, 1 dzień wolny). Props: brak linii rynkowych, linie = progi robocze wokół mojej średniej (p ~50% przy linii = średnia); do użycia dopiero po porównaniu z linią Betclic.
Uwaga: feed lineups ma nietypowe składy (np. LeBron/Brown w PHI, Paul George w BOS); traktować jako nieweryfikowane, nie wykorzystuję tego dla badanych 3 meczów poza listą graczy.

## 1) Utah Jazz @ Dallas Mavericks (07.11 02:00 CET)
Tabela (rating/net/pace): DAL ORtg 112.5, DRtg 112.7, net -0.1, pace 99.6 (4-4). UTA ORtg 103.9, DRtg 115.1, net -11.3, pace 100.9 (1-7). DAL u siebie.
Injury: UTA - Jaren Jackson Jr. OUT (MCL 6-8 tyg.), Nurkic OUT, T. Alexander OUT. DAL - Lively OUT, de Larrea OUT, Biberovic OUT, Aldama (ESPN: status Out, ale komentarz "probable" - sprzeczne), Christie probable (hip). Flagg, Irving, Gafford, Washington w skladzie.
Rynek: ML DAL 1.35-1.37 / UTA 3.20 (no-vig DAL ~72%); spread DAL -6.5 (Mozzart 1.90) / -7.5 (Novibet 1.93); BettingPros total 226.5-227.5; ML DAL -251/+245 am.
Model: DAL 117 - UTA 110 (spread -7, total 227), SD 12.5. Korekta: net-rating +11 + HCA ~2.5 sciagniete do ~-7 (probka 8 gier, JJJ out).
| Rynek | p | fair |
| DAL wygrywa | 69.8% | 1.43 |
| UTA wygrywa | 30.2% | 3.32 |
| DAL -5.5 | 54.8% | 1.83 |
| DAL -6.5 | 51.6% | 1.94 |
| DAL -7.5 | 48.4% | 2.07 |
| DAL -8.5 | 45.2% | 2.21 |
| UTA +6.5 | 48.4% | 2.07 |
| UTA +7.5 | 51.6% | 1.94 |
| UTA +8.5 | 54.8% | 1.83 |
| Total O/U 225.5 | 53.3% / 46.7% | 1.88 / 2.14 |
| Total O/U 227.5 | 48.9% / 51.1% | 2.05 / 1.96 |
| Total O/U 229.5 | 44.5% / 55.5% | 2.25 / 1.80 |
| DAL team total O/U 116.5 (sr 117) | 51.8% / 48.2% | 1.93 / 2.08 |
| DAL team total O 114.5 | 59.0% | 1.70 |
| UTA team total O/U 109.5 (sr 110) | 51.8% / 48.2% | 1.93 / 2.08 |
| UTA team total U 111.5 | 55.4% | 1.80 |
Props (sr = moja srednia, linia robocza): Flagg pts sr 23.5: O22.5 52.2%, U24.5 58.6% (1.71); Flagg PRA sr 36: O/U 35.5 50%; Flagg ast sr 5.8: O5.5 50.7%; Irving pts sr 22 (6 GP z 8, 29.9 min): O/U 21.5 ~49/51%; Irving 3PM sr 3.0: O2.5 57.1% (1.75); K. George pts sr 21: 20.5 ~50%; K. George ast sr 5.5: U5.5 53.9%; Markkanen pts sr 18.5: O17.5 52.5%; Markkanen 3PM sr 2.8: O2.5 52.6%.
Blowout: spread ~7 = umiarkowane ryzyko, minuty gwiazd DAL -1.
Pewność: zwycięzca DAL srednia (p ~70% = rynek); spread brak przewagi; total brak przewagi (rynek 227); props niska (brak linii). Najlepszy rynek: DAL ML ~1.43 fair vs rynek 1.35-1.37 -> brak value; Irving O2.5 3PM ewentualnie.
Ryzyka: DAL 4-4 z netto ~0, UTA walczy (komenda: 1-7 to w czesci pech), rotacje DAL (Aldama niejasny), young team UTA wsparty Peterson/Bailey; wyniki UTA @ NO 120-113 przegrana.
H2H: brak istotnych (kompletnie inne skladu); pominięte.

## 2) Oklahoma City Thunder @ Memphis Grizzlies (07.11 02:00 CET)
Tabela: MEM ORtg 117.1, DRtg 106.8, net +10.3 (6-2), pace 101.5. OKC ORtg 111.7, DRtg 110.8, net +0.8 (6-2), pace 98.3. Probka 8 gier, OKC z duzymi stratami.
Injury: OKC - Holmgren OUT (8-10 tyg., patellar), Jalen Williams OUT (operacja), Cason Wallace OUT (labrum), Jaylin Williams OUT (back), Topic OUT, Sorber OUT. Gra SGA (30.1 ppg, 33.7 min), Hartenstein, A. Mitchell, McCain. MEM - Isaiah Stewart OUT, Scotty Pippen Jr. OUT (rezerwowi). Boozer, Jerome, Coward, Edey w skladzie.
Rynek: ML MEM 2.25-2.30 / OKC 1.64-1.65 (no-vig OKC ~58%); spread OKC -2.5 / -3.5; BettingPros total 224.5-225.5; ML MEM +144 / OKC -144 (am. ok. 1.69).
Model: MEM 111.7 - OKC 113.3 (OKC -1.6, total 225). Jestem pod rynkiem OKC (57% vs ~58% - ok, zgodne), spread model OKC -1.6 vs rynek -3: roznica 1.4 pkt, w granicach. Net rating MEM znacznie lepszy, ale OKC ma SGA i wyrafinowany system; wyrownany mecz.
| Rynek | p | fair |
| OKC wygrywa | 56.9% | 1.76 |
| MEM wygrywa | 43.1% | 2.32 |
| OKC -1.5 | 50.3% | 1.99 |
| OKC -2.5 | 47.0% | 2.13 |
| OKC -3.5 | 43.7% | 2.29 |
| MEM +1.5 | 49.7% | 2.01 |
| MEM +2.5 | 53.0% | 1.89 |
| MEM +3.5 | 56.3% | 1.78 |
| Total O/U 223.5 | 53.3% / 46.7% | 1.88 / 2.14 |
| Total O/U 225.5 | 48.9% / 51.1% | 2.05 / 1.96 |
| Total O/U 227.5 | 44.5% / 55.5% | 2.25 / 1.80 |
| MEM team total O/U 111.5 (sr 111.7) | 50.7% / 49.3% | 1.97 / 2.03 |
| OKC team total O/U 113.5 (sr 113.3) | 49.3% / 50.7% | 2.03 / 1.97 |
Props: SGA pts sr 29.5 (prop O29.5 47.1%, U31.5 62.2% 1.61); SGA PRA sr 38: U38.5 54.6%; SGA 3PM sr 2.5: U2.5 54.7%; SGA ast sr 4.5: U4.5 54.3%; Hartenstein reb sr 9.8: O/U 9.5 ~50%; A. Mitchell pts sr 17.5: U17.5 53.8%; Jerome pts sr 24 (27.4 ppg z 7 GP, regresja): O/U 23.5 ~50%, U25.5 61.0%; Boozer reb sr 9.5: U9.5 53.3%; Boozer PRA sr 31: 30.5 50%; Coward pts sr 14.5: U14.5 54.2%.
Blowout niskie (spread ~3).
Pewność: BRAK MOCNEGO TYPU (p 43-57%, spread <3). Zwyciezca niska/srednia. Props niska.
Ryzyka: SGA GTD nie na liscie ale gra duze minuty; OKC bez Holmgren/J.Will to gleboka zmiana (net OKC 0.8 vs poczatkowy sezon); MEM dobry start (6-2) moze byc wariancja; rynek moze ruszyc po statusach.
H2H: brak istotnych (inny sklad OKC).

## 3) Toronto Raptors @ Milwaukee Bucks (07.11 02:00 CET)
Tabela: MIL ORtg 106.3, DRtg 118.1, net -11.8, pace 103.5 (1-7; wyg. 109-102 @ BOS 04.11? wynik ESPN MIL @ BOS 109-102 wyglada na wygrana MIL, ale bilans MIL 1-7 wg BettingPros/NBA stats - niezgodnosc zrodel, sprawdz). TOR ORtg 115.8, DRtg 111.1, net +4.7, pace 101.9 (4-4). 
Injury: TOR - Kawhi Leonard OUT (re-eval za tydzien), Barnes (groin) QUESTIONABLE (ESPN 06.11 01:26Z), Bittle OUT. MIL - Kam Jones OUT (two-way); Herro, Jaquez, Turner, Kuzma, Rollins zdrowi.
Rynek: ML TOR 1.35-1.385 / MIL 3.15-3.20 (no-vig TOR ~71%); spread TOR -6.5 (Mozzart 1.90, Novibet 1.84); BettingPros total 230.5-231.5.
Model: MIL 112.5 - TOR 118.5 (TOR -6, total 231), SD 13 / 19 (Barnes Q). Korekta: surowa roznica net ~16+HCA ~2.5 sciagnieta do -6 (probka 8 gier); Barnes (23.5/7.6/5.1) Q: -1.
| Rynek | p | fair |
| TOR wygrywa | 69.1% | 1.45 |
| MIL wygrywa | 30.9% | 3.24 |
| TOR -4.5 | 54.6% | 1.83 |
| TOR -5.5 | 51.5% | 1.94 |
| TOR -6.5 | 48.5% | 2.06 |
| TOR -7.5 | 45.4% | 2.20 |
| MIL +4.5 | 45.4% | 2.20 |
| MIL +5.5 | 48.5% | 2.06 |
| MIL +6.5 | 51.5% | 1.94 |
| MIL +7.5 | 54.6% | 1.83 |
| Total O/U 229.5 | 53.1% / 46.9% | 1.88 / 2.13 |
| Total O/U 231.5 | 49.0% / 51.0% | 2.04 / 1.96 |
| Total O/U 233.5 | 44.8% / 55.2% | 2.23 / 1.81 |
| TOR team total O/U 118.5 (sr 118.5, SD11) | ~50% / 50% | 2.00 |
| MIL team total O/U 112.5 (sr 112.5) | 50.0% / 50.0% | 2.00 |
| MIL team total U 110.5 | 42.8% | -- (O 110.5 57.2% 1.75) |
Props: Herro pts sr 21.5: O20.5 52.3%, U22.5 58.9%; Herro 3PM sr 3.4: O2.5 65.4% (1.53), U3.5 56.1%; Jaquez pts sr 16.5: O15.5 52.7%; Barrett pts sr 20.5: O19.5 52.4%; Quickley pts sr 17.4: O/U 16.5 ~52%; Quickley ast sr 5.8: O5.5 50.7%; Barnes (tylko jesli zagra, Q): pts sr 22: U22.5 56.1%; PRA sr 36: O/U 35.5 50%. Typy na Barnesa warunkowe, nie rekomendowac.
Blowout: spread ~6.5 niski/umiarkowany.
Pewność: zwyciezca TOR srednia (p ~69% ~ rynek 71%); spread brak przewagi; total brak przewagi; najlepszy rynek: Herro O2.5 3PM (65.4%, fair 1.53, pewnosc niska-srednia bo brak linii/kursu) i TOR ML 1.45 fair (rynek 1.35-1.385 -> brak value).
Ryzyka: Barnes Q (jesli out: TOR -1.5 do -2 pkt p ~64%), Kawhi out, MIL u siebie po 1-7 w serii; MIL bilans niezgodny miedzy zrodlami, wymaga sprawdzenia.
H2H: brak istotnych.

## Ranking (p z fair >1.15), pewnosc wszedzie niska-srednia
1. Herro O2.5 3PM 65.4% / 1.53 (brak linii rynkowej)
2. DAL ML 69.8% / 1.43 oraz TOR ML 69.1% / 1.45 (fair ~ rynek, bez EV wzgledem Pinnacle-like)
3. Irving O2.5 3PM 57.1% / 1.75 (brak linii)
4. OKC ML 56.9% / 1.76 (wyrownany, slaby typ)

---

# NBA - noc 06->07.11.2026 (data USA 06.11): MIN@NOP, POR@LAL, SAS@SAC
Sprawdzenie danych: 06.11.2026 ok. 12:30 CET. Statusy graczy mogą się zmienić do rozpoczęcia meczu (injury report NBA.com niedostępny przez WebSearch; użyto ESPN game summary + BettingPros + NBA daily lineups).
Źródła: stats.nba.com (nba_stats_call leaguedashteamstats Advanced 2026-27, 7-9 meczów/drużynę - MAŁA PRÓBA), ESPN (scoreboard, game_summary: kontuzje, ostatnie 5 meczów, kursy DraftKings), nba_odds_today (Novibet/FanDuel/Tab/Mozzart), BettingPros (best lines, props, DTD), nba_daily_lineups (Expected, niepotwierdzone).
Wszystkie 6 drużyn grało 04.11 (USA) -> 1 dzień przerwy, brak back-to-back. Sezon wczesny: SD podniesione (margin 12.5-13, total 18.5), p regresowane do rynku.

## Statystyki drużyn (net/off/def rating, pace; bilans)
- MIN 6-3: +10.9 (116.1/105.2), pace 101.1. Bez Edwardsa (Out, operacja) i DiVincenzo (Out). Ostatnio W@HOU 117-107, L@SAS 111-121.
- NOP 4-4: +2.3 (113.4/111.1), pace 103.3. Missi Out, Murphy III DTD (kolano). Dwie dogrywki z rzędu (MEM, UTA), W 120-113 OT 04.11.
- LAL 7-2: +8.2 (121.1/112.9), pace 100.7, eFG 60.2% (1.). Doncic 38.5 pp/8.1 r/8.0 a (ESPN, 9 m.). Mamukelashvili DTD (choroba). Ostatni: W@SAC 116-103.
- POR 6-1: +10.4 (120.0/109.6), pace 101.3. Out: Morant, Sharpe, Krejci. W 132-119@PHX 04.11. H2H sezonu: POR 136-129 w LA (27.10).
- SAS 6-2: +8.0 (115.4/107.4), pace 99.9. Out: T. Harris, Quaintance. W 112-111 vs DAL 04.11. Wembanyama 29.0 pp/12.4 r/4.5 blk.
- SAC 1-7: -12.9 (106.5/119.4), pace 102.9, 3 z ostatnich 5 meczów: stracone 120-136. Out: Murray, Raynaud, Simmons. LaVine i Achiuwa DTD (BettingPros; ESPN ich nie listuje). L 103-116 vs LAL 04.11. H2H: SAS 130-103 (27.10).

## Rynek (DraftKings via ESPN; BettingPros best lines)
- MIN@NOP: MIN -4.5 (-105 / NOP +4.5 -115), ML MIN -184 / NOP +154, total 230.5 (o-112/u-108). Otwarcie MIN -5.5. Inne książki 1.56/2.40-2.52.
- POR@LAL: LAL -2.5 (-115 / POR +2.5 -105), ML LAL -148 / POR +124, total 232.5 (o-105/u-115). Najlepsze: POR +2.5 do +3.5.
- SAS@SAC: SAS -15.5 (-104; SAC +15.5 -116), ML SAS -990 / SAC +650, total 229.5 (-110/-110). Inne: -14.5 do -15.5.
Bez marży: MIN ML 62.2%, LAL ML 57.3%, SAS ML ~87%.

## MECZ 1: Minnesota Timberwolves @ New Orleans Pelicans (07.11 02:00 CET)
Model: NOP 112.7 - MIN 116.8 (MIN o 4.1, total 229.5; SD 12.5/18.5). Net rating MIN regresowany z +10.9 do ok. +5 (próba 9 m., brak Edwardsa), NOP z +2.3 do ok. 0; HCA +2.5. Zgodne z rynkiem (różnica spreadu 0.4).
Typ: brak mocnego typu (spread blisko linii). Najlepsze: MIN ML 64.4% (1.55) - rynek 1.54-1.56 -> brak EV.
| Rynek | Linia | p | fair | pewność |
| Zwycięzca MIN | ML | 64.4% | 1.55 | średnia |
| Zwycięzca NOP | ML | 35.6% | 2.81 | średnia |
| Spread MIN | -2.5 / -3.5 / -4.5 / -5.5 / -6.5 | 55.1 / 51.9 / 48.7 / 45.5 / 42.4% | 1.82/1.93/2.05/2.20/2.36 | niska |
| Spread NOP | +2.5 / +3.5 / +4.5 / +5.5 / +6.5 | 44.9 / 48.1 / 51.3 / 54.5 / 57.6% | 2.23/2.08/1.95/1.84/1.74 | niska |
| Total | 227.5 O/U | 54.3 / 45.7% | 1.84/2.19 | niska |
| Total | 229.5 O/U | 50.0 / 50.0% | 2.00 | niska |
| Total | 230.5 O/U (rynek) | 47.8 / 52.2% | 2.09/1.92 | niska |
| Total | 231.5 O/U | 45.7 / 54.3% | 2.19/1.84 | niska |
| Total | 233.5 O/U | 41.4 / 58.6% | 2.41/1.71 | niska |
| Total MIN (śr. 116.8) | 114.5 O/U | 58.3 / 41.7% | 1.72/2.40 | niska |
| Total MIN | 116.5 O/U | 51.1 / 48.9% | 1.96/2.04 | niska |
| Total MIN | 118.5 O/U | 43.9 / 56.1% | 2.28/1.78 | niska |
| Total NOP (śr. 112.7) | 110.5 O/U | 57.9 / 42.1% | 1.73/2.38 | niska |
| Total NOP | 112.5 O/U | 50.7 / 49.3% | 1.97/2.03 | niska |
| Total NOP | 114.5 O/U | 43.5 / 56.5% | 2.30/1.77 | niska |
Rynki zawodnika (linia BettingPros; średnie: ESPN sezon 8-9 m. + BettingPros projection, małe próby -> pewność niska; wszystko warunkowe od składu):
| Zawodnik | Rynek | Linia | p (typ) | fair | uwagi |
| Gobert | zbiórki | 11.5 (O +115/U -101) | 50% O | 2.00 | ESPN 11.9 zb, BP proj 12; linia sprawiedliwa; O 10.5 byłoby 60% (linia niedostępna) |
| LaMelo Ball | punkty | 21.5 (U -130) | 62% U | 1.61 | sezon 17.2 pp, BP proj 21; shade do rynku (model 65%); rola wzrosła po braku Edwardsa |
| LaMelo Ball | asysty | 7.5 (U -138) | 62% U | 1.61 | sezon 5.9 ast, BP proj 7; model 66.6%, shade |
| Zion Williamson | punkty | 22.5 (U -125) | 55% U | 1.82 | sezon 21.5; rynek już wycenia (U 55.6% implied) -> brak EV |
| Zion Williamson | zbiórki | 5.5 (U -135) | 56% U | 1.79 | sezon 5.1 zb; brak EV po marży |
| Derik Queen | zbiórki | 7.5 (O -115) | 51% O | 1.95 | ESPN 7.9 zb; brak przewagi |
| Dosunmu | punkty | 17.5 (U -108) | 56% U | 1.79 | sezon 16.3 (rola 1. opcji bez Edwardsa) |
| Murray | asysty | 5.5 (U 100/O -104) | 50% | 2.00 | sezon 5.6 |
Brak typów PRA z linią >2 źródła; nie rekomenduję PRA tu.
Ryzyka: Murphy III (NOP, DTD kolano) - jeśli Out: NOP -1 do -2 pkt w różnicy -> MIN pokrywa -4.5 ok. 54%; Shannon Jr. (MIN, DTD); Edwards Out już w modelu; NOP gra na dniu po OT (zmęczenie nie liczone, 1 dzień przerwy); mała próba sezonu. NOP u siebie szybsze tempo (103.3) -> ryzyko Over.
Pewność ogólna: niska-średnia. Brak mocnego typu.

## MECZ 2: Portland Trail Blazers @ Los Angeles Lakers (07.11 04:00 CET)
Model: LAL 117.5 - POR 114.5 (LAL o 3.0, total 232.0). LAL net +8.2 regresowany do ok. +4.5, POR +10.4 do ok. +4.5 (6-1, ale bez Morant/Sharpe); HCA +2.5 -> LAL o ok. 3. Rynek -2.5 (różnica 0.5).
Typ: brak mocnego typu (p 45-55%). Najlepsze: LAL ML 57.9% (1.73) - rynek 1.63-1.67 -> brak EV.
| Rynek | Linia | p | fair | pewność |
| Zwycięzca LAL | ML | 57.9% | 1.73 | niska |
| Zwycięzca POR | ML | 42.1% | 2.38 | niska |
| Spread LAL | -1.5 / -2.5 / -3.5 / -4.5 | 54.8 / 51.6 / 48.4 / 45.2% | 1.83/1.94/2.07/2.21 | niska |
| Spread POR | +1.5 / +2.5 / +3.5 / +4.5 | 45.2 / 48.4 / 51.6 / 54.8% | 2.21/2.07/1.94/1.83 | niska |
| Total | 229.5 O/U | 55.4 / 44.6% | 1.81/2.24 | niska |
| Total | 230.5 O/U | 53.2 / 46.8% | 1.88/2.14 | niska |
| Total | 232.5 O/U (rynek) | 48.9 / 51.1% | 2.04/1.96 | niska |
| Total | 234.5 O/U | 44.6 / 55.4% | 2.24/1.81 | niska |
| Total | 236.5 O/U | 40.4 / 59.6% | 2.48/1.68 | niska |
| Total LAL (117.5) | 114.5 O | 60.7% | 1.65 | niska |
| Total LAL | 116.5 O/U | 53.6 / 46.4% | 1.86/2.16 | niska |
| Total LAL | 118.5 O/U | 46.4 / 53.6% | 2.16/1.86 | niska |
| Total POR (114.5) | 112.5 O/U | 57.2 / 42.8% | 1.75/2.34 | niska |
| Total POR | 114.5 O/U | 50 / 50% | 2.00 | niska |
| Total POR | 116.5 O/U | 42.8 / 57.2% | 2.34/1.75 | niska |
Rynki zawodnika (spread ~2.5 -> blowout ryzyko niskie):
| Zawodnik | Rynek | Linia | p (typ) | fair | uwagi |
| Doncic | punkty | 34.5 (O -133 / U +117) | 54% O | 1.85 | sezon 38.5 pp, BP proj 35; cena -133 = 57% implied -> brak EV; mean 36 |
| Doncic | zbiórki | 7.5 (O +108 / U -113 ) | 54% O | 1.87 | sezon 8.1 |
| Doncic | asysty | 7.5 (U -113 ) | 51% O | 1.98 | sezon 8.0, BP proj 7 U |
| Doncic | PRA | 50.5 (O -109) | 52% O | 1.92 | skorelowane z pkt/zb/ast, nie łączyć |
| Avdija | punkty | 23.5 (O -120) | 47% O | 2.14 | sezon 23.4 |
| Avdija | asysty | 5.5 | 51% O | 1.97 | sezon 6.4 ast; BP proj 6 O |
| Clingan | zbiórki | 10.5 (O -140) | 48% O | 2.09 | sezon 10.6; cena zawyża |
| Lillard | punkty | 21.5 (O +106/U -111) | 47% O | 2.15 | brak przewagi |
| Reaves | punkty | 21.5 (O -105) | 52% O | 1.91 | BP proj 24.3 (64% O, flaga BettingPros); moja średnia 22.5; brak potwierdzonego drugiego źródła -> nie rekomenduję |
Ryzyka: Mamukelashvili (LAL, DTD choroba), Ziaire Williams (LAL, DTD), Robert Williams III (POR, DTD - jeśli Out, Clingan +minuty/zb); POR bez Morant/Sharpe/Krejci - mała rotacja; LAL bez Reavesa? (Reaves w składzie Expected); POR wygrał H2H 136-129 (27.10) w LA; mała próba sezonu (7-9 m.); wariancja Doncica.
Pewność ogólna: niska. Brak mocnego typu.

## MECZ 3: San Antonio Spurs @ Sacramento Kings (07.11 04:00 CET)
Model surowy: SAC 108.5 - SAS 119.5 (SAS o 11.0, total 228; SD 13). Rynek SAS -15.5 (różnica 4.5 pkt <5 pp reguły? spread diff >3 pkt -> wymaga uzasadnienia). Rynek ma SAC po kontuzjach (Murray, Raynaud, Simmons Out; LaVine/Achiuwa DTD), SAC straciło 120-136 w 3 z 5 ostatnich meczów, net -12.9. Po korekcie "nie schodź pod rynek >5 pp bez konkretów" p skorygowane o -8 pp w stronę rynku (kolumna "p skoryg."). 
Typ: SAC +15.5 (p skoryg. 55%, fair 1.82; cena 1.90) - słaby edge, pewność niska; ewentualnie brak typu. SAS ML 1.20 fair vs rynek 1.09 (brak EV).
| Rynek | Linia | p surowe | p skoryg. | fair (skoryg.) | pewność |
| Zwycięzca SAS | ML | 81.2% | 83% | 1.20 | średnia (rynek ~1.09, brak EV) |
| Zwycięzca SAC | ML | 18.8% | 17% | 5.9 | średnia |
| Spread SAS | -9.5 / -11.5 / -13.5 / -14.5 / -15.5 | 54.6 / 48.5 / 42.4 / 39.4 / 36.5% | 62 / 56 / 50 / 47 / 44.5% | 1.61/1.79/2.00/2.13/2.25 | niska |
| Spread SAC | +9.5 / +11.5 / +13.5 / +14.5 / +15.5 | 45.4 / 51.5 / 57.6 / 60.6 / 63.5% | 38 / 44 / 50 / 53 / 55.5% | 2.63/2.27/2.00/1.89/1.80 | niska |
| Total | 224.5 O/U | 57.5 / 42.5% | 56 / 44% | 1.79/2.27 | niska |
| Total | 226.5 O/U | 53.2 / 46.8% | 52 / 48% | 1.92/2.08 | niska |
| Total | 228.5 O/U | 48.9 / 51.1% | 49 / 51% | 2.04/1.96 | niska |
| Total | 229.5 O/U (rynek) | 46.8 / 53.2% | 47.5 / 52.5% | 2.11/1.90 | niska |
| Total | 231.5 O/U | 42.5 / 57.5% | 44 / 56% | 2.27/1.79 | niska |
| Total SAS (119.5) | 116.5 O | 60.7% | 59% | 1.69 | niska |
| Total SAS | 118.5 O/U | 53.6 / 46.4% | 52 / 48% | 1.92/2.08 | niska |
| Total SAS | 120.5 O/U | 46.4 / 53.6% | 46 / 54% | 2.17/1.85 | niska |
| Total SAC (108.5) | 106.5 O/U | 57.2 / 42.8% | 56 / 44% | 1.79/2.27 | niska |
| Total SAC | 108.5 O/U | 50 / 50% | 50% | 2.00 | niska |
| Total SAC | 110.5 O/U | 42.8 / 57.2% | 44 / 56% | 1.79/2.27 | niska |
Rynki zawodnika (spread >=14.5 -> RYZYKO BLOWOUTU: gwiazdy SAS tracą ostatnie 6-10 min; minuty Wembanyamy obniżone do ok. 31-32):
| Zawodnik | Rynek | Linia | p (typ) | fair | uwagi |
| Wembanyama | punkty | 27.5 (O -125/U -105) | 55% U (blowout) | 1.82 | sezon 29.0 pp, BP proj 28; mean 27 po cięciu minut |
| Wembanyama | zbiórki | 11.5 (O -108/U +122) | 50% | 2.00 | sezon 12.4; mean 11.8 po cięciu |
| Wembanyama | bloki | 3.5 (O +102/U -104) | 56% O | 1.79 | sezon 4.5 bpg; mean 4.0 po cięciu; najlepszy rynek zawodnika w meczu (EV ok. +0.14 przy 2.02), pewność niska |
| Wembanyama | PRA | 44.5 (O +113/U -110) | 60% U (po cięciu) | 1.67 | mean 41; ryzyko blowout=Under; pewność niska |
| Sabonis | zbiórki | 13.5 (O +108/U +115) | 46% O | 2.20 | sezon 14.9 (ESPN), BP proj 12 (U); sprzeczność źródeł -> brak typu |
| Sabonis | PRA | 32.5 (U -114) | 57% U | 1.74 | BP proj 31, BP 54% U; mean 31.5 |
| Acuff Jr. | punkty | 22.5 (O -125) | 52% O | 1.92 | sezon 25.6 pp; BP proj 23; cena -125 |
| Acuff Jr. | asysty | 5.5 (U +127? / O -110) | 50% | 2.00 | sezon 7.0; BP proj 5 U - sprzeczne |
| Fox | punkty | 19.5 (U -112) | 52% U | 1.92 | blowout obniża minuty |
| Castle | punkty | 21.5 (O -121) | 44% O | 2.29 | |
Ryzyka: LaVine (SAC DTD) i Achiuwa (DTD) - jeśli Out SAC słabsze o 2-3 pkt -> SAS pokrywa -15.5 ok. 47-50%; blowout skraca minuty gwiazd (Under props) i podnosi wariancję; SAS grał 112-111 z DAL 04.11 (nie dominuje zawsze); SAC grało w tym tygodniu 4 mecze, tempo SAC (102.9) vs SAS (99.9) -> mniejsza liczba posiadań -> Under; SAC najgorszy bilans ligi 1-7 + pierwszy mecz bez ... (Murray out).
Pewność ogólna: niska dla spreadu; średnia dla SAS wygrana (ale brak wartości przy kursie 1.09).

## Tabela kandydatów (ze wszystkich rynków; tylko fair > 1.15; kursy znane dla ML/spread/total/props)
| Mecz | Rynek | p | fair | kurs rynkowy | EV | pewność | zależy od |
| SAS@SAC | SAC +15.5 | 55.5% | 1.80 | 1.90 (Mozzart/Tab) / 1.85-1.94 | +0.05 | niska | LaVine/Achiuwa, garbage time |
| SAS@SAC | Wembanyama bloki O 3.5 | 56% | 1.79 | ok. 2.02 (+102) | +0.13 | niska | minuty (blowout) |
| SAS@SAC | Sabonis PRA U 32.5 | 57% | 1.74 | 1.88 | +0.07 | niska | minuty, BP zgodne |
| MIN@NOP | LaMelo punkty U 21.5 | 62% | 1.61 | 1.77 | +0.10 | niska | brak Edwardsa -> użycie |
| MIN@NOP | LaMelo asysty U 7.5 | 62% | 1.61 | 1.72 | +0.07 | niska | j.w. |
| MIN@NOP | MIN -4.5 | 48.7% | 2.05 | 1.95 | -0.05 | niska | brak EV |
| POR@LAL | LAL ML | 57.9% | 1.73 | 1.64-1.67 | -0.04 | niska | brak EV |
Ranking: żaden typ nie ma wysokiej pewności; mecze 1 i 2 = "brak mocnego typu". Kursy BettingPros/ESPN (DraftKings), nie Betclic - do weryfikacji w kuponach.
BettingPros: użyty jako źródło linii/kursów i projekcji props; projekcje (bet rating) traktowane jako flaga, nie zmieniają p. Różnica >10 pp vs rynek wystąpiła tylko w spreadzie SAC (skorygowane w dół) i Reaves pkt (flaga BP 64% O, bez drugiego źródła).
To oszacowania probabilistyczne, nie gwarancje.

---

# NHL 06->07.11.2026 (data USA 06.11) - pełna analiza

Sprawdzono: 06.11.2026 (rano czasu polskiego). Źródła: nhl_standings, nhl_club_schedule (NHL API), DailyFaceoff (bramkarze: 0 z 6 potwierdzonych), Pinnacle (kursy), BettingPros (linie props; limit dzienny 429 wyczerpany po ~10 zapytaniach, brak rynków saves i `props` pustych przed meczem). Brak xG/GSAx (MoneyPuck/NST niedostępne), próba sezonu 14-17 meczów => małe próby, pewność obniżona.

## Tabela rynków
Kursy Pinnacle po usunięciu marży (BUF ML 61.2%, MIN ML 70.6%, CGY ML 53.8%). Wszystkie bramkarze NIEPOTWIERDZENI.

### 1) CBJ @ BUF (07.11 01:00 CET)
λ: BUF 3.2 - CBJ 2.9 (łącznie 6.1). Sabres 7-5-3, GF 2.93/GA 3.40, dom GF 2.1/GA 3.0; CBJ 7-7-0, GF 2.71/GA 3.00, wyjazd GF 2.2/GA 3.2. CBJ drugi dzień B2B (wczoraj 05.11 w domu 2:1 SO z DAL), BUF ostatnio 04.11 (1:2 OTT), odpoczęci.
Bramkarze (DFO): CBJ Talbot .909 / 2.44 (na B2B ryzyko rezerwowego), BUF Ellis .891 / 2.92 (wygląda na rezerwowego/zastępcę, nieznany powód).
| Rynek | Linia | p | fair | pewność |
|---|---|---|---|---|
| Moneyline (z OT) | BUF | 58% | 1.72 | niska-średnia (model 55%, rynek 61%) |
| Moneyline | CBJ | 42% | 2.38 | niska |
| 60' 3-way | BUF/X/CBJ | 46.5/22/31.5% | 2.15/4.55/3.17 | niska |
| Puck line | BUF -1.5 | 35% | 2.86 | niska |
| Puck line | CBJ +1.5 | 65% | 1.54 | średnia |
| Total (z OT) | Over 5.5 | 58% | 1.72 | niska |
| Total | Over 6.5 / Under 6.5 | 45% / 55% | 2.22 / 1.82 | niska (brak przewagi) |
| Total | Under 7.5 | 72% | 1.39 | niska-średnia |
| Obie strzelą (60') | tak | 90% | 1.11 | średnia |
Props (BettingPros, tylko linie): Thompson (BUF) SOG 3.5 -115/+115 (ok. 50%), Dahlin SOG 2.5 -106/+102, Werenski (CBJ) SOG 2.5 -140 (Over ok. 56%), Coyle gol +325 (~22%), Quinn gol +235 (~27%). Brak drugiego źródła średnich (NHL.com/NST) => BEZ rekomendacji typu zawodnika.
Saves: brak potwierdzonego bramkarza ani liczb SA => bez typu. Orientacyjnie Talbot Over 24.5 obron ok. 58% (przy 26 SA), tylko po potwierdzeniu.
Ryzyka: Talbot na B2B może nie zagrać (rezerwowy => BUF +0.2-0.3 gola), Ellis słaby (.891) - zmiana na startera BUF podnosi BUF; rynek 61% BUF vs model 55%: różnica 6 pp, p podniesione do 58%. Gol w OT/karne.

### 2) SJS @ MIN (02:00 CET)
λ: MIN 3.55 - SJS 2.45 (łącznie 6.0). Wild 11-3-3 (25 pkt), GF 3.29/GA 2.24, dom GF 3.6/GA 2.4; Sharks 7-9-1, GF 2.59/GA 3.59, wyjazd GA 3.8, ostatnio 2:7 w LAK (04.11), seria 3 porażek. MIN ostatnio 03.11, SJS 04.11 - brak B2B.
Bramkarze (DFO): MIN Wallstedt .919 / 2.06 (10-2-3, możliwy regres), SJS Askarov .887 / 3.29.
| Rynek | Linia | p | fair | pewność |
|---|---|---|---|---|
| Moneyline | MIN | 67% | 1.49 | średnia (rynek 70.6%) |
| Moneyline | SJS | 33% | 3.03 | niska |
| 60' 3-way | MIN/X/SJS | 56.5/21/22.5% | 1.77/4.76/4.44 | średnia |
| Puck line | MIN -1.5 | 45% | 2.22 | niska-średnia (rynek 49%) |
| Puck line | SJS +1.5 | 55% | 1.82 | niska |
| Total | Over 5.5 | 57% | 1.75 | niska |
| Total | Over 6.5 / Under 6.5 | 44.5% / 55.5% | 2.25 / 1.80 | niska |
| Total | Under 7.5 | 73% | 1.37 | średnia |
| Total drużyny MIN | Over 2.5 | ok. 72% | 1.39 | niska (rynek -360/264 => 73%) |
| Obie strzelą | tak | 89% | 1.12 | średnia |
Props: brak linii/danych w BettingPros (wyczerpany limit), bez typów zawodnika. Wallstedt saves/Askarov saves bez typu.
Ryzyka: Wallstedt regres, Askarov rezerwowy/zmiana, blowout MIN (puck line), pusta bramka.

### 3) ANA @ CGY (02:00 CET)
λ: CGY 3.2 - ANA 3.1 (łącznie 6.3). Ducks 8-7-1, GF 3.69/GA 3.81, seria 3 W; Flames 7-8-1, GF 2.44/GA 3.44, dom GF 3.25/GA 3.1. ANA B2B (05.11 5:4 w EDM, podróż Edmonton-Calgary krótka) => -0.1 gola i ryzyko rezerwowego; CGY odpoczęci (04.11 1:2 OT SEA).
Bramkarze (DFO): ANA Dostal .871 / 3.55, CGY Wolf .870 / 3.71 (oba poniżej normy, regres spodziewany, Wolf zwykle lepszy). Oba rynki bramkarskie bez typu.
| Rynek | Linia | p | fair | pewność |
|---|---|---|---|---|
| Moneyline | CGY | 52.5% | 1.90 | niska - brak mocnego typu |
| Moneyline | ANA | 47.5% | 2.11 | niska |
| 60' 3-way | CGY/X/ANA | 41/22.5/36.5% | 2.44/4.44/2.74 | niska |
| Puck line | CGY -1.5 | 30% | 3.33 | niska |
| Puck line | ANA +1.5 | 70% | 1.43 | średnia |
| Total | Over 5.5 | 59% | 1.69 | niska |
| Total | Over 6.5 / Under 6.5 | 47% / 53% | 2.13 / 1.89 | niska |
| Total | Under 7.5 | 71% | 1.41 | niska-średnia |
| Obie strzelą | tak | 91% | 1.10 | średnia |
Props (BettingPros, tylko linie): Carlsson SOG 2.5 +125/-133 (Over ok. 43%), Granlund 1.5 -138, Backlund 2.5 +148, Parekh 1.5 -120; brak drugiego źródła => bez rekomendacji.
Ryzyka: wyrównany mecz, bramkarze w dołku, Dostal może pauzować na B2B.

## Kalibracja (SKILL.md)
- B2B CBJ (-0.1 do -0.15 gola) i ANA (-0.1) wpisane w λ; goalie niepotwierdzeni => wszystkie pewności max średnie.
- Nie schodzę pod rynek o >5 pp (BUF ML 58 vs 61.2) ani o >3 pp na Under (totale ustawione blisko rynku; Poisson zaniża ogon, Under 4.5 pominięty).
- Poisson zaniża remis po 60': zastąpiony ok. 21-22.5% (rynek 20-22.5%).
- Fair odds <=1.15 pominięte. Słabe typy: ML CGY/ANA to "brak mocnego typu".
- Najlepsze względnie: MIN ML (67%, 1.49), MIN 60' (56.5%), Under 7.5 we wszystkich (71-73%, fair 1.37-1.41), CBJ +1.5 (65%), ANA +1.5 (70%), SJS +1.5 (55%).
