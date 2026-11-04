# Kupony NHL, noc 03→04.11.2026 (v2: tylko NHL, poziom luzowania do 7)

## 1. Okres i źródło kursów
- Okres: wtorek 03.11.2026 (USA), mecze w Polsce w nocy 04.11 (01:00-03:00, CET). NBA tej nocy nie gra.
- **Kursy NIE z Betclic.pl ani gg397.bet** (w sesji brak przeglądarki, WebFetch nie czyta dynamicznego Betclic). Fallback: **Pinnacle direct** (kursy z `pinnacle_matchup_markets`, konwersja z amerykańskich), kontrola: TheOddsAPI (Unibet NL, Betclic FR i Unibet FR/SE jako proxy, tylko 1X2 po 60'). Pobrane 03.11 ok. 20:25 UTC. Pinnacle jest ostrzejszy od kursów krajowych, więc kursy na Betclic.pl będą zwykle niższe, a EV niższe niż poniżej.
- Analizy: `analizy/Analiza_NHL_2026-11-03.md` (skill `nhl-analyst`; grupy 1 i 3 policzone jednym wywołaniem skilla na grupę). Pełne kursy: scratchpad `nhl_odds.md`.

## 2. Terminarz
11 meczów NHL, 0 meczów NBA. Wszystkie nierozegrane w chwili składania kuponów. Bramkarze w większości niepotwierdzeni oficjalnie (stan z 03.11 rano USA).

## 3. Pula nóg po filtrach (p z analiz, kurs Pinnacle direct)
Odrzucone: rynki zawodnika (jedno źródło, brak linii), fair ≤ 1.15, ANA@VAN Over 5.5 (Pinnacle ma tylko 6.0 z push i 6.5).

| Mecz | Rynek | p | Kurs | Fair | EV | Pewność |
|---|---|---|---|---|---|---|
| EDM@NJD | EDM +1.5 | 68% | 1.54 | 1.47 | +4.7% | średnia |
| STL@NYR | STL +1.5 | 74% | 1.41 | 1.35 | +4.3% (przewaga niepotwierdzona: +5.2 pp nad rynkiem po devigu) | średnia |
| ANA@VAN | VAN +1.5 | 66% | 1.56 | 1.52 | +3.0% | średnia |
| DAL@WSH | Under 6.5 | 62% | 1.65 | 1.61 | +2.3% | średnia |
| CAR@NSH | NSH +1.5 | 60% | 1.70 | 1.67 | +2.0% | średnia |
| STL@NYR | Under 6.5 | 58% | 1.74 | 1.72 | +0.9% | niska-średnia |
| VGK@PIT | VGK +1.5 | 72.5% | 1.38 | 1.38 | 0.0% | niska-średnia (Hill niepotw.) |
| MIN@PHI | MIN +1.5 | 82% | 1.20 | 1.22 | -1.6% | średnia |
| MIN@PHI | MIN ML | 62% | 1.58 | 1.61 | -2.0% | średnia |
| COL@CBJ | CBJ +1.5 | 69% | 1.42 | 1.45 | -2.0% | średnia |
| DAL@WSH | DAL +1.5 | 72% | 1.36 | 1.39 | -2.1% | średnia |
| MIN@PHI | Under 6.5 | 58.5% | 1.67 | 1.71 | -2.3% | niska-średnia |
| WPG@MTL | MTL ML | 60% | 1.62 | 1.67 | -2.8% | średnia |
| WPG@MTL | MTL +1.5 | 80% | 1.21 | 1.25 | -3.2% | średnia |
| CAR@NSH | CAR +1.5 | 81% | 1.19 | 1.23 | -3.6% | średnia |
| ANA@VAN | Over 6.5 | 56% | 1.72 | 1.79 | -3.7% | średnia |
| EDM@NJD | Over 5.5 | 56% | 1.72 | 1.79 | -3.7% | średnia |
| VGK@PIT | Over 5.5 | 62.5% | 1.54 | 1.60 | -3.75% | niska-średnia |
| UTA@TOR | UTA +1.5 | 75% | 1.28 | 1.33 | -4.0% | niska |
| COL@CBJ | Over 5.5 | 57% | 1.67 | 1.75 | -4.8% | średnia |
| CAR@NSH | CAR ML | 63% | 1.51 | 1.59 | -4.9% | średnia |
| UTA@TOR | Over 5.5 | 63% | 1.49 | 1.59 | -6.1% | średnia |
| CAR@NSH | CAR team total Over 2.5 | 69% | 1.35 | 1.45 | -6.9% | średnia |
| DET@TBL | TBL ML | 66% | 1.36 | 1.52 | -10.2% | niska-średnia (bramkarze niepotw.) |

Tylko 5 nóg ma EV > 0 (mecze 4, 7, 9, 10, 11), a przewagi nad rynkiem Pinnacle są małe (do ~5 pp). To zgodne z analizami: rynek NHL jest wyceniony ostro.

## 4. Kupony (6 z 10: nie dobijam na siłę)
Każda noga tylko w jednym kuponie, jeden mecz w kuponie (poziom 6: ten sam mecz w innym kuponie z innej rodziny rynków). Godziny PL, data lokalna USA 03.11. Źródło każdej nogi: **Pinnacle direct, nie Betclic**.

| # | Poziom luzowania | Nogi (godz. PL) | Łączne p | Kurs | Fair | EV | Stawka (1/4 Kelly) |
|---|---|---|---|---|---|---|---|
| 1 | **0 (bazowy)** | STL +1.5 @NYR (01:00) 74% / 1.41; EDM +1.5 @NJD (01:30) 68% / 1.54 | 50.3% | 2.17 | 1.99 | **+9.3%** | **2.0%** |
| 2 | **1** (EV ≥ -5%; złamany: EV ≤ 0) | VAN +1.5 vs ANA (03:00) 66% / 1.56; MTL +1.5 vs WPG (01:00) 80% / 1.21 | 52.8% | 1.89 | 1.89 | -0.3% | 0% |
| 3 | **3** (poniżej progów: EV < -5% nieobowiązujące, p > 45%) | UTA +1.5 @TOR (01:00) 75% / 1.28 (niska); VGK +1.5 @PIT (01:00) 72.5% / 1.38 (Hill niepotw.) | 54.4% | 1.77 | 1.84 | -4.0% | 0% |
| 4 | **3** (poniżej progów) | DAL +1.5 @WSH (01:00) 72% / 1.36; CBJ +1.5 vs COL (01:00) 69% / 1.42 | 49.7% | 1.93 | 2.01 | -4.1% | 0% |
| 5 | **3** (poniżej progów, ryzykowny) | CAR team total Over 2.5 @NSH (02:00) 69% / 1.35; TBL ML vs DET (01:00) 66% / 1.36 (bramkarze niepotw.) | 45.5% | 1.84 | 2.20 | -16.4% | 0% |
| 6 | **6** (poniżej progów; mecz CAR@NSH powtórzony, inna rodzina rynków niż kupon 5) | MIN +1.5 @PHI (01:00) 82% / 1.20; CAR ML @NSH (02:00) 63% / 1.51 | 51.7% | 1.81 | 1.94 | -6.4% | 0% |

Kupony 7-10 nie powstały: po wyczerpaniu nóg spełniających progi poziomów 0-6 nie ma kolejnych zestawów. Tylko kupon 1 ma EV > 0 i stawkę; kupon 2 ma EV tuż poniżej zera (stawka 0%), kupony 3-6 poniżej progów.

## 5. Poziom 7: lista pojedynczych predykcji (kurs > 1.14, p > 60%, ranking po p)
Powstało 17 pozycji (20 nie dobijam). Kursy Pinnacle direct, EV dla informacji.

| # | Mecz (godz. PL) | Predykcja | p | Kurs | EV | Uwagi |
|---|---|---|---|---|---|---|
| 1 | MIN@PHI (01:00) | MIN +1.5 | 82% | 1.20 | -1.6% | |
| 2 | CAR@NSH (02:00) | CAR +1.5 | 81% | 1.19 | -3.6% | |
| 3 | WPG@MTL (01:00) | MTL +1.5 | 80% | 1.21 | -3.2% | Skinner niepotw. |
| 4 | UTA@TOR (01:00) | UTA +1.5 | 75% | 1.28 | -4.0% | pewność niska |
| 5 | STL@NYR (01:00) | STL +1.5 | 74% | 1.41 | +4.3% | przewaga niepotwierdzona |
| 6 | VGK@PIT (01:00) | VGK +1.5 | 72.5% | 1.38 | 0.0% | Hill niepotw., B2B VGK |
| 7 | DAL@WSH (01:00) | DAL +1.5 | 72% | 1.36 | -2.1% | |
| 8 | COL@CBJ (01:00) | CBJ +1.5 | 69% | 1.42 | -2.0% | COL B2B |
| 9 | CAR@NSH (02:00) | CAR team total Over 2.5 | 69% | 1.35 | -6.9% | |
| 10 | EDM@NJD (01:30) | EDM +1.5 | 68% | 1.54 | +4.7% | Hellebuyck próbka 2 mecze |
| 11 | ANA@VAN (03:00) | VAN +1.5 | 66% | 1.56 | +3.0% | bramkarze niepotw. |
| 12 | DET@TBL (01:00) | TBL ML | 66% | 1.36 | -10.2% | bramkarze niepotw., DET B2B |
| 13 | CAR@NSH (02:00) | CAR ML | 63% | 1.51 | -4.9% | Kochetkov niepotw. |
| 14 | UTA@TOR (01:00) | Over 5.5 | 63% | 1.49 | -6.1% | |
| 15 | VGK@PIT (01:00) | Over 5.5 | 62.5% | 1.54 | -3.75% | Hill niepotw. |
| 16 | MIN@PHI (01:00) | MIN ML | 62% | 1.58 | -2.0% | |
| 17 | DAL@WSH (01:00) | Under 6.5 | 62% | 1.65 | +2.3% | |

## 6. Ostrzeżenia
- Założenie niezależności meczów; nogi z tego samego meczu w różnych kuponach (kupon 6) są skorelowane.
- Kursy Pinnacle nie są kursami Betclic.pl: przed postawieniem sprawdź kurs w polskim kasynie, przy niższym kursie EV spada (kupon 1 ma zapas ok. 9%, czyli ok. 4% na nogę).
- Przewagi modelu nad rynkiem to ≤ 5 pp i leżą w błędzie modelu; weryfikacja 26-28.10 pokazała, że nogi z "przewagą niepotwierdzoną" trafiały ok. 53% przy modelowym 65%.
- Bramkarze: Skinner (WPG), Gibson/Vasilevskiy (TBL/DET), Hill/Hart (VGK), Kochetkov/Bussi (CAR), Dostal (ANA), Merilainen/Lankinen (VAN) niepotwierdzeni; sprawdź skład przed meczem. COL i DET grają drugi dzień z rzędu.
- Rozliczenie: moneyline, puck line i total liczą dogrywkę (karne do totalu nie); wynik 3-way po 60' nie.
- To oszacowania probabilistyczne, nie gwarancje; stawki to sugestia wielkości, nie porada finansowa.
