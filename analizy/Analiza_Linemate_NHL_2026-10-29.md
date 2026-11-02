# Analiza picków Linemate NHL - 29/30.10.2026

Skill: nhl-analyst (nhl_props.py). Źródła: NHL API (game-log i stats REST, sprawdzone 29.10), istniejące analizy `Analiza_NHL_cz1/cz2_2026-10-29.md`, kursy `Kursy_Betclic_2026-10-29.md`, Linemate (hit rate i kursy podane przez użytkownika). BettingPros: pominięty (HTTP 429, limit). Drugie niezależne źródło liczb zawodnika (Natural Stat Trick / Hockey-Reference) oraz potwierdzenie linii i jednostek PP (Daily Faceoff) NIE zostały pobrane, więc pewność każdego rynku zawodnika jest ograniczona (reguła skilla). Skład może się zmienić do rozpoczęcia meczu.

Definicje: **p_adj Linemate** = (trafienia+1)/(próby+2), czyli hit rate z korektą na małą próbę; **p rynku** = 1/kurs z picku (z marżą). Próba sezonu to 11-14 meczów, więc średnie regresuję do poziomu "prawdziwej" formy.

## Tabela zbiorcza

| Pick | własne p | p_adj Linemate | p rynku (z kursu) | fair | EV przy kursie Linemate | pewność | flagi |
|---|---|---|---|---|---|---|---|
| Fehervary (WSH) Over 1,5 bloków @ NSH | 68% | 90% (8/8) | 55,2% (1,81) | 1,47 | +23% | niska-średnia | b2b WSH (drugi dzień), brak drugiego źródła i potwierdzonej pary obrońców; blokady zależne od strzałów NSH |
| Connor (WPG) Over 2,5 strzałów @ TBL | 72% | 89% (7/7) | 55,2% (1,81) | 1,39 | +30% | średnia | wysoki SH% goli (9 goli, 17%) nie dotyczy strzałów; Skinner/Vasilevskiy potwierdzeni; WPG b2b dopiero jutro |
| Connor Over 3,5 strzałów | 53% | brak (sezon 7/12 = ok. 58%) | brak kursu | 1,89 | sprawdź kurs: wartość od > 1,89 | niska | wariancja strzałów; nie zbadano linii bukmachera |
| Crosby (PIT) Under 2,5 strzałów vs UTA | 63% | 89% (7/7) | 56,2% (1,78) | 1,59 | +12% | niska-średnia | niski ostatnio ice time (16-19 min) i 0-2 strzały; ryzyko regresji do jego historycznej średniej (~2,5), brak drugiego źródła |
| Kaprizov (MIN) Over 0,5 gola vs NYI | 35% | 80% (7/8) | 48,8% (2,05); Betclic 50,0% (2,00) | 2,86 | -30% (przy 2,00) | średnia | 14 goli w 14 meczach przy SH% ok. 29% - nie do utrzymania; Sorokin (.919) potwierdzony; EV ujemne |
| Marchessault (NSH) Over 1,5 strzałów vs WSH | 54% | 70% (6/8) | 65,4% (1,53) | 1,85 | -17% | niska | średnia 1,8 strzału, 15-18 min, WSH b2b, brak drugiego źródła; przy fair 1,85 kurs 1,53 to ujemne EV |
| MTL +1,5 (@DAL) | 68,1% | brak | ok. 64,5% (1,55, średnia książek) | 1,47 | +5,6% | średnia | Dobes (MTL, rookie) potwierdzony, mała próba; Oettinger regresja; Betclic bez tej linii |
| NYI +1,5 (@MIN) | 65,5% | brak | ok. 61,7% (1,62, średnia książek) | 1,53 | +6,1% | średnia | Wallstedt (MIN) niepotwierdzony; przy rezerwowym p NYI +1,5 rośnie; Sorokin potwierdzony; Betclic bez tej linii |
| BOS +1,5 (@STL) | 71,6% | brak | ok. 70% (Pinnacle -265 = 1,38) | 1,40 | ok. -1% | niska-średnia | Hofer i Swayman potwierdzeni; mecz wyrównany; brak linii +1,5 na Betclic (jest tylko "BOS lub X" 60' 1,53) |

## Zawodnicy - szczegóły

### 1) Martin Fehervary (WSH) - Over 1,5 bloków @ NSH, 01:00
- Sezon (11 meczów): bloki 5, 2, 1, 4, 4, 2, 4, 3, 2, 2, 3 (od 2.10 do 28.10), średnia 2,9; ostatnie 8 meczów wszystkie >= 2 (zgodne z Linemate 8/8). Źródło: NHL stats API (realtime).
- Rola: top-pair obrońca, TOI 18-24 min (ostatnio 22:39, 23:19), bez roli PP w punktach (0 PPP).
- Przeciwnik: NSH u siebie (Saros potwierdzony, wg cz1). WSH gra b2b (28.10 z PHI), więc więcej czasu w defensywie niż zwykle, ale też ryzyko słabszego dnia; Lindgren niepotwierdzony.
- Model: średnia regresowana do 2,6 (sezon wcześniejszy niższy niż start), VMR 1,2, `nhl_props.py blocks 2.6 1.5` daje ok. 68-70%. Przyjmuję 68%.
- Zgodność z Linemate: p_adj 90% vs moje 68% - różnica wynika z regresji i małej próby (11 meczów). Rynek 55%: przewaga ok. +13 pp, ale 1 źródło liczb, więc pewność niska-średnia.

### 2) Kyle Connor (WPG) - Over 2,5 / 3,5 strzałów @ TBL, 00:00
- 12 meczów, strzały od najnowszego: 3, 5, 3, 4, 2, 5, 3, 3, 4, 6, 5, 9 (średnia 4,33). Ostatnie 7: wszystkie >= 3 (zgodne z 7/7). Over 2,5: 11/12; Over 3,5: 7/12. TOI 17:26-24:23, PP1 (3 PPP w meczu z DET, 1 PPP z CHI). Źródło: NHL API game-log.
- Przeciwnik: TBL (Vasilevskiy potwierdzony, wg Daily Faceoff z cz1); gospodarz TBL jest faworytem (63,7%), więc WPG częściej goni wynik, co wspiera strzały.
- Model: średnia regresowana do 3,9-4,0 (start sezonu zawyżony meczem z 9 strzałami). `nhl_props.py sog 4.0 2.5 3.5`: Over 2,5 = 73,5%, Over 3,5 = 54,9%.
- Over 2,5: własne p 72%, fair 1,39; kurs 1,81 (55%) daje największą przewagę z zestawu, mimo to 1 źródło - pewność średnia.
- Over 3,5: p 53%, fair 1,89 (granica; kurs nieznany, wartość tylko powyżej ok. 1,95). Obie linie skorelowane - nie łączyć w jednym kuponie.

### 3) Sidney Crosby (PIT) - Under 2,5 strzałów vs UTA, 00:00
- 12 meczów, strzały od najnowszego: 0, 0, 1, 1, 2, 2, 1, 3, 2, 5, 2, 3 (średnia 1,8). Under 2,5 w 8/12; ostatnie 7: wszystkie <= 2 (zgodne z 7/7). TOI 16:39-23:13 (ostatnio 19:38, 16:39, 18:31).
- Model: ostatnie 12 meczów odbiega od jego historycznych ok. 2,5 strzału, więc mieszam do ok. 2,1-2,2. `nhl_props.py sog 1.95 ...` daje Under 2,5 = 69%; przy 2,2 ok. 62%. Przyjmuję 63%.
- Przeciwnik: UTA (Vejmelka niepotwierdzony). Ostatnie strzały nisko, ale może to ukryty uraz/ograniczone minuty (TOI 16:39 22.10) - sprawdzić status przed meczem. Jeśli zagra normalnie i dostanie więcej minut przy 2 niewykorzystanych PP, ryzyko Over rośnie.
- Zgodność: p_adj 89% vs 63% - duża rozbieżność, bo seria 7 meczów jest krótka i nie regresuje.

### 4) Kirill Kaprizov (MIN) - gol (Over 0,5, z OT) vs NYI, 01:00
- 14 meczów, 14 goli (lider ligi), 23 pkt. Gol w 10/14 meczów, w 7 z ostatnich 8 (zgodne z 7/8). Strzały: 4, 2, 4, 4, 3, 5, 6, 3, 4, 4, 0, 3, 3, 3 (średnia 3,6), SH% ok. 29%. TOI 17:54-24:58, PP1 (gol/pkt w PP w 6 meczach).
- Przeciwnik: NYI, Sorokin potwierdzony (.919, GAA 2,26). MIN u siebie, faworyt 60,1%.
- Model: 3,6 strzału × realistyczne SH% ok. 12% = 0,43 → regresuję do 0,38-0,42 (ze względu na Sorokina). `nhl_props.py goals 0.38 0.5` = 31,6%; 0,42 = 34,3%. Przyjmuję **35%**, fair 2,86. Zgodnie ze skillem, strzelec gola rzadko > 45%.
- Rynek: kurs Linemate 2,05 (48,8%), Betclic 2,00 (50,0%): EV ok. -30%. Brak value; hit rate 7/8 to artefakt wysokiego SH%.
- Punkty 1+ (Betclic 1,25 = 80%): punkty w 12/14 meczów (86%), ale regresowane p ok. 70-72% → EV ok. -10%. Też bez value.

### 5) Jonathan Marchessault (NSH) - Over 1,5 strzałów vs WSH, 01:00
- 12 meczów, strzały od najnowszego: 1, 2, 0, 3, 4, 2, 2, 3, 0, 2, 3, 0 (średnia 1,83). Over 1,5 w 8/12; ostatnie 8: 6/8 (zgodne z Linemate 6/8). TOI 13:17-18:06 (ostatnio ok. 17:00-17:30), 5 PPP w 12 meczach - PP1.
- Przeciwnik: WSH (b2b, Lindgren niepotwierdzony), NSH u siebie.
- Model: `nhl_props.py sog 1.95 1.5` = 55,6%; 1,8 = 51,5%. Przyjmuję 54%, fair 1,85. Kurs 1,53 (65%) - ujemne EV (ok. -17%). Przy dobrej cenie wejście dopiero od ok. 1,85.

## Trendy drużynowe (puck line +1,5, ML z OT, 60' bez wpływu na handicap z OT)

Źródło p: `Analiza_NHL_cz1/cz2_2026-10-29.md`; kursy to średnia książek (cz2) i Pinnacle (cz1), bo Betclic nie ma handicapu +1,5 dla tych meczów.

| Trend | własne p | fair | kurs rynkowy | p rynku | EV | uwagi |
|---|---|---|---|---|---|---|
| MTL +1,5 @ DAL | 68,1% | 1,47 | 1,55 (średnia) | 64,5% | +5,6% | Dobes (.847, mała próba), Oettinger (.929, regresja); DAL po 1:5 z NJD. Pewność średnia |
| NYI +1,5 @ MIN | 65,5% | 1,53 | 1,62 (średnia) | 61,7% | +6,1% | Sorokin vs Wallstedt (niepotwierdzony); MIN ML 60,1% (rynek ok. 63%), dobre bronienie obu stron |
| BOS +1,5 @ STL | 71,6% | 1,40 | ok. 1,38 (Pinnacle -265) | ok. 70% | ok. -1% | wyrównany mecz, Swayman .921 vs Hofer .917; brak value |

Uwaga: +1,5 jest tu ocenione z OT (puck line NHL); przy fair <= 1,15 pomijałbym typ, ale żaden z trzech tego progu nie przekracza. Poissonowy skrypt może zawyżać +1,5 przy niskim λ, więc EV +5-6% mieści się w niepewności modelu - to są typy o niskiej przewadze.

## Ranking (według EV × pewność)

1. Connor Over 2,5 strzałów @ 1,81 - p 72%, EV +30%, pewność średnia (jedyny z mocną przewagą).
2. Fehervary Over 1,5 bloków @ 1,81 - p 68%, EV +23%, niska-średnia.
3. Crosby Under 2,5 strzałów @ 1,78 - p 63%, EV +12%, niska-średnia.
4. NYI +1,5 i MTL +1,5 - EV +5-6%, średnia, ale małe marginesy.
5. Odrzucić: Kaprizov gol (-30% EV), Marchessault Over 1,5 @ 1,53 (-17%), BOS +1,5 (EV ~0).

## Uwagi do kuponów

- Fehervary i Marchessault grają w tym samym meczu NSH - WSH (korelacja przez tempo meczu); nie łączyć bez korekty. Connor i Crosby z meczów o 00:00, bez wspólnych zdarzeń.
- Rynki zawodnika bez drugiego źródła (reguła skilla: min. dwa) i bez potwierdzonej linii/PP z Daily Faceoff: pewność nie wyższa niż średnia. Przed obstawieniem sprawdzić status Crosby'ego (spadek minut) i parę obrońców WSH.
- To oszacowania probabilistyczne, nie gwarancje.
