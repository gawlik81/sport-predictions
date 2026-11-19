# Kupony: noc NBA/NHL 13/14.11.2026 (czas polski), wersja v2

## 1. Okres, źródło kursów, poziom luzowania
- Okres: noc NBA i NHL, mecze z 13.11 czasu USA (w Polsce 14.11, 01:00-04:30). Tylko NBA i NHL (wybór użytkownika).
- Poziomy luzowania: **tylko poziom 7** (wybór użytkownika). Poziom 7 to lista pojedynczych predykcji, nie kupony: kurs rynku > 1.14, p > 60%, ranking malejąco po p, stawka 0%.
- Analizy: `Analiza_NBA_noc_2026-11-14.md`, `Analiza_NHL_noc_2026-11-14.md` (statusy z ok. 22:45 CET; składy tylko "Expected").
- Kursy: **Superbet** (`superbet_event_odds`, pobrane po 22:45 CET) dla handicapów NBA, NYK ML, SAS ML, NYR ML, VAN ML, VGK/NSH ML. Pozostałe z jawnie oznaczonego fallbacku: FanDuel/Novibet (NBA ML z analizy), DraftKings (puck line NHL, ESPN). Superbet nie pokazał puck line ani większości ML w pobranych rynkach.
- BettingPros pominięty (brak klucza).

## 2. Skrót terminarza
- NBA: 9 meczów, NHL: 2 mecze (11 wydarzeń, wszystkie przeanalizowane). Nie ma w tym okresie innych sportów (zakres użytkownika).
- Odrzucone: HOU ML (p 90,5%, fair 1,10 ≤ 1,15).

## 3. Pula nóg po filtrach poziomu 7 (p > 60%, kurs > 1.14, fair > 1.15)
Mniej niż 20 predykcji spełnia warunki, więc lista ma **10 pozycji** (nie dobijam na siłę).

| # | Mecz (godz. PL, data USA 13.11) | Typ | p | Kurs | Źródło kursu | Fair | EV | Pewność |
|---|---|---|---|---|---|---|---|---|
| 1 | Sacramento-Portland (04:00) | Portland wygra | 84,1% | 1,217 | FanDuel | 1,19 | +2,3% | średnia |
| 2 | San Antonio-Golden State (03:30) | San Antonio wygra | 80,3% | 1,154 | Superbet | 1,25 | -7,3% | średnia |
| 3 | Orlando-Milwaukee (01:00) | Orlando wygra | 75,2% | 1,256 | FanDuel/Novibet | 1,33 | -5,5% | niska (Suggs) |
| 4 | Chicago-Atlanta (02:00) | Atlanta wygra | 75,0% | 1,364 | FanDuel | 1,33 | +2,3% | średnia/niska |
| 5 | Indiana-New York (01:00) | New York wygra | 73,1% | 1,27 | Superbet | 1,37 | -7,2% | średnia |
| 6 | LA Clippers-OKC (04:30) | OKC wygra | 72,6% | 1,345 | FanDuel | 1,38 | -2,3% | średnia |
| 7 | New Orleans-Memphis (02:00) | Memphis wygra | 68,0% | 1,602 | FanDuel | 1,47 | +8,9% | niska (Mathurin), "przewaga niepotwierdzona" |
| 8 | Vegas-Nashville (04:00) | Nashville +1.5 (puck line) | 67,4% | 1,56 | DraftKings | 1,48 | +5,1% | średnia |
| 9 | Vancouver-NY Rangers (03:00) | NY Rangers wygrają (z dogrywką) | 64,1% | 1,42 | Superbet | 1,56 | -9,0% | średnia |
| 10 | Vancouver-NY Rangers (03:00) | Vancouver +1.5 (puck line) | 60,1% | 1,74 | DraftKings | 1,66 | +4,6% | średnia (Meriläinen niepotwierdzony) |

Poz. 9 i 10 to ten sam mecz, różne rynki, bez sprzeczności (Rangers mogą wygrać o 1 gola), ale są skorelowane.

## 4. Kupony
Poziom 7 nie składa kuponów, tylko listę pojedynczych predykcji (stawka 0%). Kupony z progami bazowymi 0-2 nie powstają: żadna kombinacja nóg nie ma EV > 0 przy p > 50% i kursie zestawu 1,5-2,5 w ramach wybranych poziomów (dodatnie EV mają nogi z p 54-58% na handicapach i puck line z DK, a one są poniżej p > 60% poziomu 7).

Handicapy Superbet z dodatnim EV, ale poniżej progu p > 60% (nie wchodzą na listę poziomu 7): MEM -3.5 @1,87 (p 58%, +8,5%), ATL -7.5 @1,97 (p 54%, +6,4%), CLE +2.5 @1,90 (p 55,7%, +5,8%), POR -10.5 @1,95 (p 54%, +5,3%), HOU -15.5 @1,92 (p 54%, +3,7%).

## 5. Ostrzeżenia
- Wszystkie składy NBA "Expected", nikt niepotwierdzony; Suggs (ORL), Mathurin (NOP), Nesmith (IND), Larsson (MIA) mogą zmienić p tuż przed meczem.
- Kursy FanDuel/DraftKings są zwykle wyższe niż w Superbet; typy 1, 3, 4, 6, 7, 8, 10 nie mają potwierdzonego kursu Superbet, więc przed grą sprawdź kurs krajowy (przy niższym kursie EV spada).
- Typ 7 (Memphis): p modelu ściągnięte z 71,8% do 68%, nadal powyżej rynku o kilka pp: "przewaga niepotwierdzona".
- NHL: Vancouver ma tylko oczekiwanego bramkarza (Meriläinen), ryzyko Lankinena zmienia p.
- Założenie niezależności meczów; oszacowania probabilistyczne, nie gwarancje. Stawka 0% (poziom 7), to nie porada finansowa.
