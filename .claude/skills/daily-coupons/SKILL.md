---
name: daily-coupons
description: Pełny pipeline dnia jednym poleceniem - najpierw zawsze pyta użytkownika o okres (dzień lub zakres dat), potem wyszukuje wydarzenia sportowe z tego okresu, robi dokładną analizę każdego z nich skillami analitycznymi, pobiera kursy z Superbet (connector superbet-mcp) i składa 10 najlepszych kuponów skillem bet-slip-builder, według jego progów i zasad spójności. Używaj zawsze, gdy użytkownik prosi o "kupony na dziś", "10 kuponów", "przygotuj kupony na jutro/weekend/od-do", "zrób cały research i kupony", "typy na dziś z Superbet" albo chce przejść całą ścieżkę terminarz → analiza → kupony bez prowadzenia jej krok po kroku - także gdy nie pada słowo "kupon".
---

# Dzienne kupony (terminarz → analiza → 10 kuponów)

Orkiestrator flow z CLAUDE.md (kroki 1-3). Sam nie wyszukuje wydarzeń, nie analizuje meczów ani nie składa kuponów: każdy z tych kroków **musi** przejść przez istniejący skill, wywołany narzędziem Skill (`sports-fixtures-finder`, skille `*-analyst`, `bet-slip-builder`). Nie powielaj ich logiki ad hoc ani nie zastępuj ich własnymi obliczeniami. Ten skill pilnuje tylko kolejności, kompletności, źródła kursów (Superbet) i ograniczeń kuponu. Subagent uruchamiany do analizy też ma wywołać właściwy skill analityczny, a nie analizować samodzielnie. Dane zawsze z researchu w sieci i narzędzi MCP, nie z pamięci.

## Parametry

- **Okres**: **zawsze zapytaj o niego przed krokiem 1**, narzędziem AskUserQuestion, i nie zaczynaj terminarza przed odpowiedzią (wymaganie użytkownika z 22.10.2026; wcześniej domyślnie był dzień dzisiejszy). Opcje: dziś, jutro, najbliższy weekend, z konkretnymi datami (strefa Europe/Warsaw, data z kontekstu sesji); inny dzień lub zakres "od-do" użytkownik poda w polu "Other". Jeśli zapytanie zawiera już okres (np. "kupony na jutro", "weekend 24-25.10"), też zapytaj, ale jako potwierdzenie: ten okres z rozwiniętymi datami pokaż jako pierwszą opcję "(Recommended)". Zakres dłuższy niż ~3 dni zaproponuj zawęzić w tym samym pytaniu, bo pełna analiza każdego meczu jest kosztowna.
- **Poziomy luzowania**: **zawsze zapytaj o nie przed krokiem 4** (budową kuponów), narzędziem AskUserQuestion, i nie wywołuj `bet-slip-builder` przed odpowiedzią (wymaganie użytkownika z 04.11.2026); pytanie można zadać razem z pytaniem o okres. Wybrane poziomy przekaż do `bet-slip-builder`. Jeśli użytkownik podał poziomy w zapytaniu, nie pytaj.
- **Bukmacher**: Superbet przez connector `superbet-mcp` (serwer MCP `superbet`); chyba że użytkownik poda innego.
- **Liczba kuponów**: 10, chyba że podano inną.
- **Ograniczenia kuponu**: jeden zestaw warunków, zdefiniowany wyłącznie w `bet-slip-builder` (progi domyślne: kurs nogi, kurs zestawu, EV, p; zasady spójności; stawka Kelly'ego; poziomy luzowania, gdy progi nie dają kuponów). Ten skill nie ma własnych progów ani odstępstw i niczego nie nadpisuje. Zapytanie użytkownika nadpisuje progi domyślne. Zmiany progów wprowadzaj tylko w `bet-slip-builder/SKILL.md`.

## Krok 1: Terminarz

Wywołaj skill `sports-fixtures-finder` dla okresu. Wymagaj pełnego zakresu sportów: piłka, tenis ATP/WTA, e-sport (CS2/LoL/Dota 2), MMA (UFC/KSW), NBA, NHL. Wynik: lista wydarzeń z godziną (czas polski) i rangą. Pomiń wydarzenia już rozegrane lub trwające (sprawdź godzinę względem teraz). Jeśli którejś kategorii nie ma w danym dniu, zapisz to jednym zdaniem.

## Krok 2: Dokładna analiza każdego wydarzenia

Dla **każdego** wydarzenia z terminarza wywołaj właściwy skill analityczny (`football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst`). Nie skracaj: statystyki, H2H, informacje medialne (składy, kontuzje, bramkarz, injury report), skrypty prawdopodobieństw i kalibracja z `SKILL.md` analityka.
- Wydarzeń jest zwykle dużo: równolegle uruchamiaj analizy niezależnych meczów (subagenty `general-purpose`, jeden na mecz lub sport; w prompcie podaj nazwę skilla, mecz, datę i wymóg zwrotu: rynki z p, fair odds, pewność, ryzyka). Nie pomijaj meczów dla oszczędności - jeśli coś odrzucasz (np. niskie ligi bez danych), wymień to w raporcie z powodem.
- Z każdej analizy zbierz **wszystkie rynki** z p i fair odds (wynik, gole, BTTS, rożne, kartki, total gemów, handicap, spread, total, puck line, rynki zawodnika), nie tylko zwycięzcę.
- Zapisz analizy w `analizy/` jako `<Opis>_<RRRR-MM-DD>.md` (np. `Analiza_dnia_2026-10-18.md`, jeden plik zbiorczy z sekcją na mecz).

## Krok 3: Kursy z Superbet (superbet-mcp)

Kursy bierz z connectora `superbet-mcp` (narzędzia deferred - załaduj jednym ToolSearch: `superbet_events` do listy wydarzeń i `superbet_event_odds` do rynków i kursów danego meczu). Connector obsługuje piłkę nożną, NBA, NHL i siatkówkę.
- Dla każdej kandydackiej nogi zapisz kurs dziesiętny dokładnie tak, jak zwraca `superbet_event_odds`, wraz z rynkiem i linią. Rynki dodatkowe (BTTS, rożne, kartki, handicap, total) bierz z pełnej listy rynków meczu.
- **BettingPros:** dla rynków zawodnika i nóg bez kursu w Superbet oraz do kontroli własnego p użyj skilla `bettingpros-odds` (pyta o klucz API, jeśli `BETTINGPROS_API_KEY` nie jest ustawiona; bez klucza pomiń). Kurs z jawnym oznaczeniem źródła "BettingPros, book: <nazwa>".
- Jeśli connector nie ma rynku lub sportu (tenis, MMA, e-sport) albo jest niedostępny, użyj fallbacku: narzędzia `mcp__sportsdata__*` (Pinnacle, The Odds API, Unibet/Kambi) i **jawnie oznacz źródło** przy tej nodze (kurs spoza Superbet jest zwykle wyższy niż krajowy; nie przedstawiaj go jako Superbet). Brak kursu = noga nie wchodzi do kuponu, nigdy nie wpisuj kursu z pamięci.

## Krok 4: Wycena, selekcja nóg i 10 kuponów (skill `bet-slip-builder`)

Wywołaj narzędziem Skill `bet-slip-builder` i przekaż mu analizy (ścieżka pliku z kroku 2), kursy Superbet z kroku 3 (z rynkiem, linią i źródłem) oraz polecenie złożenia 10 kuponów (liczba kuponów z parametrów). Cała wycena (fair odds, EV), filtrowanie nóg, progi, zasady spójności i niepowtarzalności nóg między kuponami, wielkość stawki oraz skrypt `slip.py` należą do `bet-slip-builder`; nie licz ich ani nie filtruj ad hoc w tym skillu. Ranking kuponów, format prezentacji i postępowanie, gdy progi bazowe nie dają 10 kuponów, są takie, jak w `bet-slip-builder`: stosuj jego poziomy luzowania (poziomy 0-2 automatycznie, 3-7 tylko za zgodą użytkownika), oznacz poziom przy każdym kuponie i nie dobijaj do 10 na siłę.

Do wyniku `bet-slip-builder` dodaj przy każdym kuponie godzinę każdej nogi i źródło kursu (Superbet / fallback).

## Krok 5: Zapis i raport

Zapisz wynik w `analizy/Kupony_10_<RRRR-MM-DD>.md` (dla zakresu dat: data początkowa). Jeśli plik już istnieje, nie nadpisuj go bez pytania - użyj sufiksu (`_v2`). Struktura pliku:
1. Okres, źródło kursów (Superbet / fallback), godzina pobrania kursów.
2. Skrót terminarza (liczba wydarzeń na sport, pominięte i dlaczego).
3. Tabela pul nóg po filtrach (mecz, rynek, p, kurs, fair, EV, pewność).
4. 10 (lub mniej) kuponów w formacie `bet-slip-builder`.
5. Ostrzeżenia: założenie niezależności, nogi z niepotwierdzoną przewagą, kursy mogące zmienić się do startu, składy do potwierdzenia przed meczem.

**Zawsze na samym końcu odpowiedzi** (także po aktualizacji kuponów, luzowaniu poziomów czy zmianie kursów) zaprezentuj podsumowanie: liczba wydarzeń, liczba spełnionych kuponów, ścieżka pliku i **tabela wszystkich kuponów** (nie tylko 3 najlepsze; wymaganie użytkownika z 26.10.2026) z nogami (godzina PL), p, kursem, EV, stawką i **poziomem luzowania, dla którego kupon został przygotowany** (-2 do 7; przy kuponie z poziomu 0 także wpisz "0 (bazowy)"). Kupony z różnych poziomów pokaż razem w jednej tabeli, także gdy EV ujemne i stawka 0%. Podsumowanie jest ostatnim elementem odpowiedzi, po nim nie dopisuj dalszych sekcji. Weryfikacją po meczach zajmie się `predictions-verifier` (osobno, na prośbę).
