# Kupony: noc NBA + NHL 04→05.11.2026 (żądane 10, powstały 2 + lista 13 predykcji)

## 1. Okres i źródła
- Okres: mecze z nocy 04→05.11.2026 (czas polski), 14 NBA + 4 NHL. Analizy: `analizy/Analiza_dnia_2026-11-04_v2.md` (skille `nba-analyst`, `nhl-analyst`).
- Poziomy luzowania wybrane przez użytkownika: 0, 1, 2 i 7.
- **Kursy NIE pochodzą z Betclic.pl ani gg397.bet.** Narzędzia przeglądarki (`mcp__claude-in-chrome__*`) nie były dostępne w sesji, więc nie sprawdzono żadnej nogi na Betclic.pl ani na gg397.bet. Fallback z The Odds API (`theoddsapi_odds`, region eu), pobrany ok. 19:30 CET 04.11:
  - **Pinnacle** (h2h, spready, totale): kursy użyte w EV i w kuponach. Pinnacle jest ostrzejszy od krajowych bukmacherów, więc kursy u polskiego bukmachera będą niższe.
  - **Betclic FR** (nie Betclic.pl): tylko kontrola h2h. Jest wyraźnie niższy niż Pinnacle (np. HOU ML 1,31 vs 1,37, MIA ML 1,43 vs 1,49). Dla żadnej z dwóch nóg NHL nie ma porównywalnego kursu (Betclic FR daje 3-way na 60').
- Rynki zawodnika i total drużyn: brak linii rynkowych, więc poza kuponami.

## 2. Terminarz (skrót)
NBA 14 meczów, NHL 4 mecze (godziny PL, 05.11). MMA, tenis, piłka, e-sport: poza zakresem prośby (tylko noc NBA + NHL). Brak back-to-back w NBA (03.11 bez meczów); CHI gra b2b (FLA 04.11, TBL 05.11).

## 3. Pula nóg po filtrach (kursy Pinnacle)
EV = p·kurs − 1. Prawie każda noga ma EV < 0 lub EV w granicach błędu, bo p modelu leży w granicach 2-3 pp od rynku.

| Mecz | Rynek | p | Kurs Pinnacle | Fair | EV | Pewność |
|---|---|---|---|---|---|---|
| SJS@LAK (04:10) | SJS +1,5 | 69,2% | 1,57 | 1,45 | +8,6% | niska-średnia, **przewaga niepotwierdzona** (p o 7,3 pp wyżej niż rynek), bramkarze niepotwierdzeni |
| OTT@BUF (01:40) | OTT +1,5 | 72% | 1,45 | 1,39 | +4,4% | niska, **przewaga niepotwierdzona** (+5,3 pp nad rynkiem) |
| CGY@SEA (04:10) | CGY +1,5 | 68,8% | 1,46 | 1,45 | +0,4% | niska-średnia, bramkarze niepotwierdzeni |
| MIN@HOU (02:30) | HOU wygra | 72% | 1,37 | 1,39 | -1,4% | średnia |
| MIL@BOS (01:40) | BOS wygra | 77,6% | 1,23 | 1,29 | -4,6% | średnia |
| MIA@LAC (04:40) | MIA wygra | 67% | 1,49 | 1,49 | -0,2% | średnia-niska (zależy od Giannisa) |
| IND@MEM (02:10) | MEM wygra | 67,5% | 1,44 | 1,48 | -2,8% | średnia |
| UTA@NOP (02:10) | NOP wygra | 67,5% | 1,43 | 1,48 | -3,5% | średnia-niska (Murphy DTD) |
| TOR@DEN (03:00) | DEN wygra | 62% | 1,56 | 1,61 | -3,3% | niska |
| CHI@FLA (01:40) | FLA wygra (z OT) | 68% | 1,39 | 1,47 | -5,5% | średnia |
| CHA@BKN (01:30) | BKN +3,5 | 53,2% | 1,99 | 1,88 | +5,9% | niska |
| CLE@OKC (02:00) | CLE +3,5 | 53% | 1,99 | 1,89 | +5,5% | niska |
| DAL@SAS (03:30) | DAL +12,5 | 54% | 1,93 | 1,85 | +4,2% | niska |
| TOR@DEN (03:00) | TOR +4,5 | 51,5% | 1,97 | 1,94 | +1,5% | niska |
| OTT@BUF (01:40) | Under 6,5 | 52% | 2,00 | 1,92 | +4,0% | niska |
| Pozostałe | NYK, LAL, SAS ML | 81-82% | 1,17-1,18 | 1,22-1,23 | -3% do -5% | średnia |

Odrzucone: nogi, których linia Pinnacle różni się od linii analizy (np. MIL +10 vs 10,5/11,5, NOP -5,5 vs -6,5, ATL -3 vs -2,5/-3,5, LAL -12 vs 12,5), bo p nie dotyczy tej linii.

## 4. Kupony

### Poziom 0 (bazowy), 2 kupony

Nazwy meczów w układzie gospodarz - gość (jak na stronach bukmacherów); godziny czasu polskiego, w nawiasie czas lokalny USA. Godziny startu z The Odds API (ESPN podaje część meczów 10 min wcześniej). Kursy: Pinnacle (fallback), 04.11 ok. 19:30 CET.

**Kupon 1: poziom 0 (bazowy)** | łączne p 53,7% | kurs 1,93 | fair 1,86 | EV +3,7% | stawka 0,1% (1/4 Kelly, z korektą "przewaga niepotwierdzona"; przy p modelu 1,0%)

| # | Data i godzina PL | Dyscyplina / liga | Mecz | Rynek (jak szukać) | Wybór | Kurs Pinnacle | Druga strona rynku | p | Fair | EV |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | czw. 05.11, 01:40 (śr. 04.11, 19:40 ET) | Koszykówka, NBA | Boston Celtics - Milwaukee Bucks | Zwycięzca meczu (moneyline, z dogrywką) | **Boston Celtics** | 1,23 | Bucks 4,60 | 77,6% | 1,29 | -4,6% |
| 2 | czw. 05.11, 04:10 (śr. 04.11, 19:10 PT) | Hokej, NHL | Los Angeles Kings - San Jose Sharks | Handicap (puck line) 1,5, z dogrywką | **San Jose Sharks +1,5** | 1,57 | Kings -1,5 2,55 | 69,2% | 1,45 | +8,6% |

Ryzyko: nogę SJS +1,5 niesie cały EV kuponu, a to "przewaga niepotwierdzona" (p o 7,3 pp nad rynkiem); bramkarze LAK i SJS niepotwierdzeni (Kuemper .878 vs Askarov .901). Boston bez Tatuma (Out), Pritchard Q.

**Kupon 2: poziom 0 (bazowy)** | łączne p 51,8% | kurs 1,99 | fair 1,93 | EV +3,0% | stawka 0,7% (1/4 Kelly, z korektą; przy p modelu 0,8%)

| # | Data i godzina PL | Dyscyplina / liga | Mecz | Rynek (jak szukać) | Wybór | Kurs Pinnacle | Druga strona rynku | p | Fair | EV |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | czw. 05.11, 02:30 (śr. 04.11, 20:30 ET) | Koszykówka, NBA | Houston Rockets - Minnesota Timberwolves | Zwycięzca meczu (moneyline, z dogrywką) | **Houston Rockets** | 1,37 (Betclic FR 1,31) | Timberwolves 3,37 | 72% | 1,39 | -1,4% |
| 2 | czw. 05.11, 01:40 (śr. 04.11, 19:40 ET) | Hokej, NHL | Buffalo Sabres - Ottawa Senators | Handicap (puck line) 1,5, z dogrywką | **Ottawa Senators +1,5** | 1,45 | Sabres -1,5 2,91 | 72% | 1,39 | +4,4% |

Ryzyko: HOU bez Adamsa, Capela DTD; OTT +1,5 to p o 5,3 pp nad rynkiem bez twardej informacji (Ersson potwierdzony, Ellis tylko "prawdopodobny"). Przy kursie Betclic FR dla HOU (1,31) kupon 2 miałby EV ok. -1,5%.

### Poziomy 1 i 2: 0 kuponów
Przy progach (p zestawu > 50%, kurs zestawu 1,5-2,5, dwie nogi z kursem > 1,2, fair nogi > 1,15, jeden typ na mecz, noga w jednym kuponie) pozostałe nogi nie składają się w kupon: po wykorzystaniu nóg z kuponów 1-2 faworyci z p > 67% mają kurs 1,17-1,44, a para z p ≈ 67% daje łączne p poniżej 50%. Poziom 1 (EV ≥ -5%) i poziom 2 (bez limitu EV) nie dodały żadnego kuponu.

### Poziom 7: lista 13 predykcji (kurs > 1,14, p > 60%, ranking po p; stawka 0%)
Lista ma 13 pozycji zamiast 20, bo tylu typów spełnia progi; nie dobijam do 20. Wszystkie kursy: Pinnacle (fallback).

| # | Data i godzina PL | Liga | Mecz | Rynek | Wybór | Kurs | p | Fair | EV | Uwagi |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 05.11, 04:10 (PT 19:10) | NBA | Sacramento Kings - Los Angeles Lakers | Zwycięzca meczu | Los Angeles Lakers | 1,18 | 82% | 1,22 | -3,2% | Doncic zdrowy |
| 2 | 05.11, 01:40 (ET 19:40) | NBA | New York Knicks - Chicago Bulls | Zwycięzca meczu | New York Knicks | 1,18 | 81,5% | 1,23 | -3,8% | Hart Out |
| 3 | 05.11, 03:30 (CT 20:30) | NBA | San Antonio Spurs - Dallas Mavericks | Zwycięzca meczu | San Antonio Spurs | 1,17 | 81% | 1,23 | -5,2% | status Irvinga niepewny |
| 4 | 05.11, 01:40 (ET 19:40) | NBA | Boston Celtics - Milwaukee Bucks | Zwycięzca meczu | Boston Celtics | 1,23 | 77,6% | 1,29 | -4,6% | Tatum Out |
| 5 | 05.11, 02:30 (ET 20:30) | NBA | Houston Rockets - Minnesota Timberwolves | Zwycięzca meczu | Houston Rockets | 1,37 | 72% | 1,39 | -1,4% | Capela DTD |
| 6 | 05.11, 01:40 (ET 19:40) | NHL | Buffalo Sabres - Ottawa Senators | Handicap 1,5 | Ottawa Senators +1,5 | 1,45 | 72% | 1,39 | +4,4% | przewaga niepotwierdzona |
| 7 | 05.11, 04:10 (PT 19:10) | NHL | Los Angeles Kings - San Jose Sharks | Handicap 1,5 | San Jose Sharks +1,5 | 1,57 | 69,2% | 1,45 | +8,6% | przewaga niepotwierdzona, po bramkarzu |
| 8 | 05.11, 04:10 (PT 19:10) | NHL | Seattle Kraken - Calgary Flames | Handicap 1,5 | Calgary Flames +1,5 | 1,46 | 68,8% | 1,45 | +0,4% | po bramkarzu |
| 9 | 05.11, 01:40 (ET 19:40) | NHL | Florida Panthers - Chicago Blackhawks | Zwycięzca meczu (z dogrywką) | Florida Panthers | 1,39 | 68% | 1,47 | -5,5% | Markstrom po przerwie |
| 10 | 05.11, 02:10 (CT 19:10) | NBA | Memphis Grizzlies - Indiana Pacers | Zwycięzca meczu | Memphis Grizzlies | 1,44 | 67,5% | 1,48 | -2,8% | |
| 11 | 05.11, 02:10 (CT 19:10) | NBA | New Orleans Pelicans - Utah Jazz | Zwycięzca meczu | New Orleans Pelicans | 1,43 | 67,5% | 1,48 | -3,5% | Murphy DTD |
| 12 | 05.11, 04:40 (PT 19:40) | NBA | Los Angeles Clippers - Miami Heat | Zwycięzca meczu | Miami Heat | 1,49 | 67% | 1,49 | -0,2% | po statusie Giannisa |
| 13 | 05.11, 03:00 (MT 19:00) | NBA | Denver Nuggets - Toronto Raptors | Zwycięzca meczu | Denver Nuggets | 1,56 | 62% | 1,61 | -3,3% | |

## 5. Ostrzeżenia
- **Kursy to Pinnacle, nie Betclic.pl.** Kursy krajowe będą niższe, więc EV obu kuponów może zmienić znak (przy Betclic FR dla HOU kupon 2 ma EV ok. -1,5%). Przed zagraniem sprawdź kursy na Betclic.pl i gg397.bet.
- Obie nogi puck line (SJS, OTT) to "przewaga niepotwierdzona": p modelu o ponad 5 pp wyżej niż rynek bez twardej informacji. W weryfikacji 26-28.10 takie nogi trafiały 53% przy średnim p 65%.
- Założenie niezależności meczów; kursy mogą się zmienić do startu; początek sezonu (6-8 meczów), więc p mają szerokie odchylenia.
- Składy i statusy do potwierdzenia przed meczem: NBA (injury report ok. 90 min przed), NHL (startujący bramkarze w LAK, SEA niepotwierdzeni; BUF Ellis "prawdopodobny").
- Poziom 3 (p zestawu > 45%, nogi p ≥ 55%) dałby jeszcze kilka kuponów z p 46-47% (np. MIA ML + CGY +1,5, MEM ML + CGY +1,5), w większości z EV < 0. Nie zastosowano go bez Twojej zgody.
- To oszacowania probabilistyczne, nie gwarancje i nie porada finansowa.
