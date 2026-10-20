---
name: daily-coupons
description: Pełny pipeline dnia jednym poleceniem - wyszukuje wydarzenia sportowe (domyślnie dzisiejsze, można podać inny dzień lub zakres dat), robi dokładną analizę każdego z nich skillami analitycznymi, pobiera kursy z Betclic.pl i składa 10 najlepszych kuponów z twardymi ograniczeniami (min. 2 typy, kurs nogi > 1.2, kurs kuponu > 1.5 i < 2.5, p kuponu > 50%, bez powtórzeń i sprzeczności typów). Używaj zawsze, gdy użytkownik prosi o "kupony na dziś", "10 kuponów", "przygotuj kupony na jutro/weekend/od-do", "zrób cały research i kupony", "typy na dziś z Betclic" albo chce przejść całą ścieżkę terminarz → analiza → kupony bez prowadzenia jej krok po kroku - także gdy nie pada słowo "kupon".
---

# Dzienne kupony (terminarz → analiza → 10 kuponów)

Orkiestrator flow z CLAUDE.md (kroki 1-3). Sam nie wyszukuje wydarzeń, nie analizuje meczów ani nie składa kuponów: każdy z tych kroków **musi** przejść przez istniejący skill, wywołany narzędziem Skill (`sports-fixtures-finder`, skille `*-analyst`, `bet-slip-builder`). Nie powielaj ich logiki ad hoc ani nie zastępuj ich własnymi obliczeniami. Ten skill pilnuje tylko kolejności, kompletności, źródła kursów (Betclic) i ograniczeń kuponu. Subagent uruchamiany do analizy też ma wywołać właściwy skill analityczny, a nie analizować samodzielnie. Dane zawsze z researchu w sieci i narzędzi MCP, nie z pamięci.

## Parametry

- **Okres**: domyślnie dzień dzisiejszy (data z kontekstu sesji, strefa Europe/Warsaw). Użytkownik może podać jutro, weekend, konkretną datę albo zakres "od-do" - użyj go zamiast domyślnego. Zakres dłuższy niż ~3 dni zawęź lub zapytaj, bo pełna analiza każdego meczu jest kosztowna.
- **Bukmacher**: Betclic.pl (https://www.betclic.pl/), chyba że użytkownik poda innego.
- **Liczba kuponów**: 10, chyba że podano inną.
- **Ograniczenia kuponu** (domyślne dla tego skilla; nadpisują domyślne progi z `bet-slip-builder`, a zapytanie użytkownika nadpisuje je oba):
  - min. 2 predykcje na kuponie,
  - kurs pojedynczej predykcji > 1.2,
  - kurs całego kuponu > 1.5 i < 2.5,
  - własne p kuponu > 50%,
  - predykcje nie powtarzają się między kuponami (ta sama noga = ten sam mecz + ten sam rynek + ta sama selekcja, tylko w jednym kuponie),
  - predykcje **między kuponami** też nie są sprzeczne: ten sam mecz w różnych kuponach tylko z nogami z różnych rodzin rynków (wynik / gole / BTTS), nigdy dwie nogi z rynku wyniku (np. 1X w jednym kuponie i 12 w drugim to przeciwne pokrycie remisu: remis wygrywa jeden kupon i przegrywa drugi); gdy zestaw ma być maksymalnie niezależny, każdy mecz tylko w jednym kuponie (podaj obie wersje, jeśli różnią się liczbą kuponów),
  - predykcje w obrębie kuponu nie są sprzeczne i nie wykluczają się (jeden typ na mecz; wyjątek tylko dla w pełni zgodnych rynków tego samego meczu, np. wygrana faworyta + Over 1.5, jeśli analiza nie widzi korelacji obniżającej p - domyślnie unikaj).

## Odstępstwa warunkowe od kryteriów

Stosuj **tylko wtedy, gdy przy pełnych kryteriach nie powstaje ani jeden kupon** (lub mniej niż żądana liczba), w tej kolejności, i wyraźnie oznacz w raporcie, które odstępstwo użyto:
1. **Pominięcie EV > 0.** Nogi i kupony z EV ≤ 0 są dopuszczone; pozostałe warunki (min. 2 nogi, kurs kuponu 1.5-2.5, p kuponu > 50%, bez powtórzeń nóg i sprzeczności) zostają. Ranking po EV (najmniej ujemne pierwsze), przy remisie po p. Kupony z EV ≤ 0 mają stawkę Kelly 0%; podaj to wprost i zaznacz, że są poniżej progu EV. Nadal pomijaj nogi z fair odds ≤ 1.15.
2. **Kurs nogi > 1.2 tylko dla dwóch nóg na kuponie.** Na kuponie muszą wystąpić co najmniej dwie predykcje z kursem > 1.2; pozostałe nogi mogą mieć kurs ≤ 1.2 (nadal z fair odds > 1.15, p > 50% kuponu, kurs kuponu 1.5-2.5). Dodatkowe krótkie nogi obniżają p kuponu, więc często nie zwiększają liczby kuponów; sprawdź to i napisz, jeśli nic nie dodały.

Jeśli i po odstępstwach brakuje kuponów, nie dobijaj ich na siłę: pokaż ile jest i zaproponuj dalsze luzowanie (p 45-50%, dłuższy terminarz).

## Krok 1: Terminarz

Wywołaj skill `sports-fixtures-finder` dla okresu. Wymagaj pełnego zakresu sportów: piłka, tenis ATP/WTA, e-sport (CS2/LoL/Dota 2), MMA (UFC/KSW), NBA, NHL. Wynik: lista wydarzeń z godziną (czas polski) i rangą. Pomiń wydarzenia już rozegrane lub trwające (sprawdź godzinę względem teraz). Jeśli którejś kategorii nie ma w danym dniu, zapisz to jednym zdaniem.

## Krok 2: Dokładna analiza każdego wydarzenia

Dla **każdego** wydarzenia z terminarza wywołaj właściwy skill analityczny (`football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst`). Nie skracaj: statystyki, H2H, informacje medialne (składy, kontuzje, bramkarz, injury report), skrypty prawdopodobieństw i kalibracja z `SKILL.md` analityka.
- Wydarzeń jest zwykle dużo: równolegle uruchamiaj analizy niezależnych meczów (subagenty `general-purpose`, jeden na mecz lub sport; w prompcie podaj nazwę skilla, mecz, datę i wymóg zwrotu: rynki z p, fair odds, pewność, ryzyka). Nie pomijaj meczów dla oszczędności - jeśli coś odrzucasz (np. niskie ligi bez danych), wymień to w raporcie z powodem.
- Z każdej analizy zbierz **wszystkie rynki** z p i fair odds (wynik, gole, BTTS, rożne, kartki, total gemów, handicap, spread, total, puck line, rynki zawodnika), nie tylko zwycięzcę.
- Zapisz analizy w `analizy/` jako `<Opis>_<RRRR-MM-DD>.md` (np. `Analiza_dnia_2026-10-18.md`, jeden plik zbiorczy z sekcją na mecz).

## Krok 3: Kursy z Betclic.pl

Kursy bierz z Betclic.pl, w pierwszej kolejności przez MCP przeglądarki (`mcp__claude-in-chrome__*`, deferred - załaduj jednym ToolSearch, zacznij od `tabs_context_mcp`, otwórz nową kartę; czytaj stronę przez `get_page_text`/`read_page`). Betclic ładuje kursy dynamicznie, więc po nawigacji poczekaj i zweryfikuj, że widzisz właściwy mecz i rynek.
- Dla każdej kandydackiej nogi zapisz kurs dziesiętny dokładnie tak, jak jest na Betclic, wraz z rynkiem i linią. Rynki dodatkowe (BTTS, rożne, kartki, total gemów, handicap) otwieraj na stronie meczu.
- Jeśli Betclic jest niedostępny (blokada, logowanie, brak rynku), użyj fallbacku: narzędzia `mcp__sportsdata__*` (Pinnacle, The Odds API, Unibet/Kambi) i **jawnie oznacz źródło** przy tej nodze (kurs nie-Betclic jest zwykle wyższy niż krajowy; nie przedstawiaj go jako Betclic). Brak kursu = noga nie wchodzi do kuponu, nigdy nie wpisuj kursu z pamięci.
- Przy dłuższym pobieraniu pilnuj zasad przeglądarki: bez dialogów, po 2-3 nieudanych próbach tej samej akcji zatrzymaj się i zapytaj użytkownika.

## Krok 4: Wycena i selekcja nóg

Wywołaj skill `bet-slip-builder`, przekazując analizy i kursy Betclic. Dla każdej nogi policz fair odds = 1/p i EV = p·k − 1. Stosuj reguły z CLAUDE.md i `bet-slip-builder`:
- odrzuć nogi z fair odds ≤ 1.15 i z kursem ≤ 1.2,
- EV > 0; EV oparte wyłącznie na p wyższym od rynku o >5 pp bez twardej informacji oznacz "przewaga niepotwierdzona" i nie ufaj mu,
- sygnały ryzyka z analiz muszą być już w liczbie p (nie tylko w opisie).

## Krok 5: 10 kuponów

Złóż kupony skryptem `bet-slip-builder/scripts/slip.py "opis" p kurs ...` (z katalogu skilla `bet-slip-builder`), zakładając niezależność nóg z różnych meczów i zaznaczając to w raporcie.

Procedura:
1. Z puli nóg spełniających kryteria zbuduj kandydatów-kupony (2-4 nogi; więcej nóg obniża p, więc 2-3 zwykle wystarcza do p > 50% przy kursie 1.5-2.5).
2. Sprawdź twardo każdy kupon: ≥ 2 nogi; każda noga > 1.2; kurs kuponu w (1.5; 2.5); p kuponu > 50%; brak sprzeczności.
3. Wybierz zestaw 10 kuponów **bez powtórzeń nóg** (przydział zachłanny od kuponu o najwyższym EV; nogę użytą raz usuń z puli). Rankinguj po EV, a przy remisie po p.
4. Przy każdym kuponie podaj: nogi (mecz, rynek, godzina), kurs każdej nogi i źródło, p nogi, kurs kuponu, p kuponu, fair odds, EV, proponowaną stawkę jako % bankrolla (ułamek Kelly'ego, np. ¼ Kelly, z limitem 2% bankrolla).

**Warunek uczciwości:** 10 kuponów bez powtórzeń wymaga co najmniej 20 różnych nóg spełniających kryteria. Przy marży Betclic (5-9%) kupon z p > 50% i EV > 0 jest rzadki. Jeśli da się złożyć mniej niż 10 kuponów spełniających wszystkie warunki, pokaż tylko te, które je spełniają, powiedz wprost ile ich jest, a następnie zastosuj "Odstępstwa warunkowe" (pominięcie EV > 0, potem kurs > 1.2 tylko dla dwóch nóg) i pokaż wynik osobno; dalsze luzowanie (p 45-50%, dopuszczenie 1 powtórzenia) tylko zaproponuj. Nie fabrykuj typów ani nie dobijaj do 10 na siłę (w weryfikacji 07.10 pozycje 6-10 z p 55-66% przegrały 3 z 5). Kupony z relaksacją oznacz osobno jako "poniżej progów".

## Krok 6: Zapis i raport

Zapisz wynik w `analizy/Kupony_10_<RRRR-MM-DD>.md` (dla zakresu dat: data początkowa). Jeśli plik już istnieje, nie nadpisuj go bez pytania - użyj sufiksu (`_v2`). Struktura pliku:
1. Okres, źródło kursów (Betclic / fallback), godzina pobrania kursów.
2. Skrót terminarza (liczba wydarzeń na sport, pominięte i dlaczego).
3. Tabela pul nóg po filtrach (mecz, rynek, p, kurs, fair, EV, pewność).
4. 10 (lub mniej) kuponów w formacie z kroku 5.
5. Ostrzeżenia: założenie niezależności, nogi z niepotwierdzoną przewagą, kursy mogące zmienić się do startu, składy do potwierdzenia przed meczem.

W odpowiedzi dla użytkownika podaj krótkie podsumowanie: liczba wydarzeń, liczba spełnionych kuponów, 3 najlepsze kupony, ścieżka pliku. Weryfikacją po meczach zajmie się `predictions-verifier` (osobno, na prośbę).
