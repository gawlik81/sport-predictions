# Kupony 28.10.2026 (środa), wynik pipeline'u daily-coupons

## 1. Okres i źródło kursów
- Okres: 28.10.2026 (czas polski, CET = UTC+1). Mecze NBA i NHL z nocy 27/28.10 USA zaczynają się w Polsce 28.10 po północy.
- **Źródło kursów: BettingPros (konsensus, kursy zagraniczne), NIE Betclic i NIE gg397.bet.** Przeglądarka MCP (`claude-in-chrome`) i serwer `sportsdata` były niedostępne, WebFetch nie dawał pełnych kursów Betclic. Użytkownik wybrał BettingPros jako źródło (27.10, po pytaniu). Kursy krajowego bukmachera będą zwykle niższe, więc EV na Betclic będzie gorsze niż poniżej.
- Kursy pobrane 27.10 ok. 20:30-20:45 CET (przeliczone z amerykańskich na dziesiętne). W EV użyto konsensusu BettingPros.
- Pokrycie kursów: NBA (4 mecze), NHL (11) i Serie A (5: 1X2, total, BTTS). **Brak kursów** dla Carabao Cup (5), DFB-Pokal (8), tenisa (22) i e-sportu (12), więc te nogi nie weszły do kuponów (kursów nie wpisywano z pamięci).
- Analizy: `analizy/Analiza_dnia_2026-10-28.md`.

## 2. Skrót terminarza
Piłka 18 (Carabao 5, DFB-Pokal 8, Serie A 5), tenis ok. 22 single ATP/WTA, NBA 4, NHL 11, e-sport 12 serii. MMA: brak gali UFC/KSW. Pominięte: Puchar Polski 1/16 (godziny niepotwierdzone), Ekstraklasa (brak źródła), Challengery/ITF, e-sport tier c/d i pary TBD.

## 3. Pula nóg po filtrach (z kursem BettingPros, p > 50%, fair > 1,15, EV ≥ -6%)
| Mecz | Typ | p | Kurs (konsensus) | Fair | EV | Pewność analizy |
|---|---|---|---|---|---|---|
| Montreal @ St. Louis | MTL +1.5 (puck line) | 75,8% | 1,38 | 1,32 | +4,6% | niska |
| Buffalo @ San Jose | SJ +1.5 | 69,9% | 1,51 | 1,43 | +5,6% | niska |
| NY Islanders @ Nashville | NYI +1.5 | 73,4% | 1,40 | 1,36 | +2,8% | niska |
| Minnesota @ Utah | MIN +1.5 | 72,3% | 1,42 | 1,38 | +2,7% | niska |
| Columbus @ Philadelphia | PHI +1.5 | 72,6% | 1,39 | 1,38 | +0,9% | niska |
| Florida @ Winnipeg | WPG +1.5 | 69,7% | 1,43 | 1,43 | 0,0% | niska |
| New Jersey @ Dallas | NJ +1.5 | 72,6% | 1,37 | 1,38 | -0,5% | niska |
| Los Angeles @ Chicago | CHI +1.5 | 72,6% | 1,37 | 1,38 | -0,5% | niska (LA na B2B) |
| Vancouver @ Anaheim | VAN +1.5 | 62,9% | 1,75 | 1,59 | +10,1% | niska (bramkarz VAN niepotwierdzony) |
| Boston @ Carolina | BOS +1.5 | 65,9% | 1,65 | 1,52 | +8,7% | średnia (zmiana bramkarza CAR) |
| Ottawa @ Vegas | OTT +1.5 | 67,0% | 1,55 | 1,49 | +3,9% | niska/średnia |
| Genoa - Juventus | Under 2.5 | 63,6% | 1,73 | 1,57 | +10,0% | średnia (9 nieobecnych Juve) |
| Monza - Napoli | Over 2.5 | 61,0% | 1,67 | 1,64 | +1,9% | średnia |
| Milan - Bologna | Under 2.5 | 55,7% | 1,99 | 1,80 | +10,8% | niska |
| Brooklyn @ Boston (NBA) | BOS ML | 82,1% | 1,15 | 1,22 | -5,6% | średnia |
| Sacramento @ San Antonio | SAC +18,5 | 54,6% | 1,92 | 1,83 | +4,8% | niska |

(Nogi z tabeli, które nie weszły do kuponów, nie dały zestawu z p > 50% przy limitach kursu; szczegóły w sekcji 5.)

Uwaga o tabeli: wartości EV w tabeli liczone z kursu konsensusu; kolumna "Pewność" z analiz skilli (`nhl-analyst`: początek sezonu, pewność obniżona wszędzie).

## 4. Kupony (poziomy 0-2 wykorzystane automatycznie; powstały 4 z 10)

Wszystkie nogi pochodzą z jednego rynku (puck line +1.5 w NHL), bo tylko one mają przewagę nad rynkiem przy p > 70%. **Wszystkie nogi mają niską pewność analizy, więc wszystkie 4 kupony traktuj jako ryzykowne.** Mecze startują w Polsce 28.10 w nocy (godziny CET; w nawiasie data USA 27.10).

### Kupon 1 | poziom 0 (progi bazowe) | ryzykowny
| Mecz | Typ | Godz. (CET) | p | Kurs | Fair | EV | Źródło kursu |
|---|---|---|---|---|---|---|---|
| Montreal @ St. Louis | Canadiens +1.5 | 01:00 (27.10 USA 19:00 CT) | 75,8% | 1,38 | 1,32 | +4,6% | BettingPros Consensus |
| Buffalo @ San Jose | Sharks +1.5 | 03:30 (27.10 USA 19:30 PT) | 69,9% | 1,51 | 1,43 | +5,6% | BettingPros Consensus |

Łączne p: 53,0% | Fair: 1,89 | Kurs: 2,08 | EV: +10,2% | Stawka: ok. 2,4% bankrolla (1/4 Kelly 9,4%; przy "przewadze niepotwierdzonej" rozważ połowę).
Flaga: **przewaga niepotwierdzona**: p obu nóg jest o 6,6 i 6,7 pp wyższe od rynku bez marży (MTL 69,2%, SJ 63,2%), bez twardej informacji w analizie, więc EV +10,2% jest podejrzane. Ryzyko: bramkarze (przewaga MTL wynika z Binningtona w St. Louis, który ma .831; mała próbka, regresja do ok. .900), dwa outsiderzy musą przegrać maks. jedną bramką.

### Kupon 2 | poziom 0 | ryzykowny
| Mecz | Typ | Godz. (CET) | p | Kurs | Fair | EV | Źródło kursu |
|---|---|---|---|---|---|---|---|
| NY Islanders @ Nashville | Islanders +1.5 | 01:00 | 73,4% | 1,40 | 1,36 | +2,8% | BettingPros Consensus |
| Minnesota @ Utah | Wild +1.5 | 02:00 | 72,3% | 1,42 | 1,38 | +2,7% | BettingPros Consensus |

Łączne p: 53,1% | Fair: 1,88 | Kurs: 1,98 | EV: +5,1% | Stawka: ok. 1,3% bankrolla (1/4 Kelly 5,2%).
Flaga: p o 4,9 i 5,0 pp powyżej rynku (granica "przewagi niepotwierdzonej"). Ryzyko: Saros (NSH) tylko "prawdopodobny".

### Kupon 3 | poziom 0 | ryzykowny
| Mecz | Typ | Godz. (CET) | p | Kurs | Fair | EV | Źródło kursu |
|---|---|---|---|---|---|---|---|
| Columbus @ Philadelphia | Flyers +1.5 | 00:00 | 72,6% | 1,39 | 1,38 | +0,9% | BettingPros Consensus |
| Florida @ Winnipeg | Jets +1.5 | 01:00 | 69,7% | 1,43 | 1,43 | 0,0% | BettingPros Consensus |

Łączne p: 50,6% | Fair: 1,98 | Kurs: 1,99 | EV: +0,6% | Stawka: ok. 0,15% bankrolla (1/4 Kelly 0,6%), praktycznie brak przewagi.
Ryzyko: p tuż nad progiem 50%; Florida to faworyt, który może wygrać dwiema bramkami.

### Kupon 4 | poziom 1 (EV ≥ -5%) | ryzykowny | poniżej progu bazowego (EV < 0)
| Mecz | Typ | Godz. (CET) | p | Kurs | Fair | EV | Źródło kursu |
|---|---|---|---|---|---|---|---|
| New Jersey @ Dallas | Devils +1.5 | 01:00 | 72,6% | 1,37 | 1,38 | -0,5% | BettingPros Consensus |
| Los Angeles @ Chicago | Blackhawks +1.5 | 01:00 | 72,6% | 1,37 | 1,38 | -0,5% | BettingPros Consensus |

Łączne p: 52,7% | Fair: 1,90 | Kurs: 1,88 | EV: -0,9% | Stawka: 0% (EV ≤ 0).
Ryzyko: Hellebuyck (NJ) bez meczu w sezonie; Dallas z serią 5 zwycięstw (PDO do regresji); LA na back-to-back.

## 5. Dlaczego tylko 4 z 10
- Próg p zestawu > 50% przy kursach nóg ≈ 1,4 wymusza nogi z p ≥ ~71%; takich nóg z kursem jest tylko kilka (puck line +1.5 w NHL). Rynki 1X2, totale i spready w NBA/NHL/Serie A mają p w okolicach rynku (50-65%), więc po dwóch nogach p zestawu spada poniżej 50%.
- Mecze Carabao Cup, DFB-Pokal, tenis i e-sport nie mają kursów w użytym źródle.
- Poziom 3 (p zestawu > 45%) nie dodaje kuponów (wymaga nóg p ≥ 55% i dwóch nóg > 1,20). Poziom 4/5 dałby 1 kupon: OTT +1.5 + BOS ML (p 55,0%, kurs 1,78, EV -2,0%, stawka 0%). Poziom -1 (tryb EV) lub -2 (pojedyncze, EV > 0, jest co najmniej 18 nóg z p > 50% i EV > 0) wymagają zgody użytkownika.
- Nie fabrykowano nóg: pozostałe typy (np. Milan Under 2.5 +10,8% EV, Genoa-Juventus Under 2.5 +10,0%, Vancouver +1.5 +10,1%) nie złożyły się w zestaw z p > 50% przy limitach kursu.

## 6. Ostrzeżenia
- Kursy to **BettingPros (konsensus), nie Betclic**; na Betclic będą niższe i EV spadnie, możliwe że poniżej zera.
- Założenie niezależności meczów; kursy mogą zmienić się do startu; składy i bramkarze NHL (Vancouver niepotwierdzony; Forsberg, Kochetkov, Saros, Ellis "prawdopodobni") do potwierdzenia przed meczem.
- NHL: puck line +1.5 liczy dogrywkę i karne (p z analiz dla moneyline/puck line z OT).
- Cała pula ma pewność "niska" z `nhl-analyst` (początek sezonu, 9-14 meczów drużyn); EV rzędu +1-5% mieści się w błędzie modelu. To oszacowania probabilistyczne, nie gwarancje ani porada finansowa.
