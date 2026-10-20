# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Charakter repozytorium

Brak aplikacji, buildu i testów. Repo służy do analizy i typowania wydarzeń sportowych (piłka nożna, tenis ATP/WTA, e-sport CS2/LoL/Dota 2, MMA UFC/KSW, koszykówka NBA, hokej NHL). Całość pracy odbywa się przez skille Claude Code w `.claude/skills/`, a wyniki zapisują się jako pliki Markdown w `analizy/`. Język pracy i raportów: polski.

## Flow przetwarzania

Standardowy przebieg pracy, w tej kolejności; każdy krok korzysta z wyników poprzedniego:

1. **Wyszukiwanie wydarzeń sportowych** (`sports-fixtures-finder`) - mecze piłkarskie, tenisowe, e-sportowe, NBA i NHL oraz walki MMA (UFC, KSW) z zadanego okresu; sam terminarz, bez analizy.
2. **Dokładna analiza wyszukanych wydarzeń** (`football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst`) - dla każdego meczu statystyki drużyn/zawodników, H2H, informacje medialne z sieci; wynik: prawdopodobieństwa i fair odds.
3. **Analiza kursów i wybór najbardziej prawdopodobnych predykcji** (wszystkie rynki, nie tylko wynik: gole, BTTS, rożne, kartki, faule, spread i total w NBA, puck line w NHL, rynki zawodnika) (`bet-slip-builder`) - zestawienie wyników analiz z kursami bukmacherskimi (EV), wybór typów o największym prawdopodobieństwie i złożenie zestawów bez sprzecznych typów. Wynik zapisuj w `analizy/` (np. `Top10_predykcje_<data>.md`).

4. **Weryfikacja** (`predictions-verifier`) - po rozegraniu wydarzeń porównanie typów, TOP-N i kuponów z rzeczywistymi wynikami: bilans trafień vs oczekiwane, rozdzielenie wariancji od błędu procesu, podsumowanie dla użytkownika i - tylko przy konkretnym błędzie procesu - poprawki reguł w skillach (analitycznych, `bet-slip-builder`, `sports-fixtures-finder`). Wynik zapisuj jako `Weryfikacja_*` w `analizy/`.

Nie przeskakuj kroku 2: krok 3 nie wymyśla prawdopodobieństw, tylko korzysta z gotowych analiz.

## Skille i ich zależności

Dziewięć skilli realizuje powyższy flow; każdy ma `SKILL.md`, a niektóre skrypt Pythona (bez zewnętrznych zależności) i `evals/evals.json`. Dane zawsze z researchu w sieci, nie z pamięci.

Skrypty liczą rozkłady z parametrów wejściowych (uruchamiane z katalogu skilla):
- `football-analyst/scripts/poisson.py <λ_gospodarze> <λ_goście>` - 1X2, O/U, BTTS, wyniki.
- `football-analyst/scripts/markets.py <rynek> <średnia> [linie]` - rożne, kartki, faule, strzały, rynki zawodnika (Over/Under, rozkład NB).
- `tennis-analyst/scripts/tennis_model.py <p_serve_A> <p_serve_B> [--bo 3|5] [--tiebreak 7|10]` - model punkt→gem→set→mecz.
- `esports-analyst/scripts/series.py <p_mapa...> [--bo 1|3|5]` - wynik serii, handicap ±1.5, total map.
- `mma-analyst/scripts/mma_model.py <fa> <fb> <da> [--rounds 2|3|5]` - zwycięzca, sposób wygranej, dystans, Over/Under rund.
- `nba-analyst/scripts/nba_model.py <pkt_gospodarze> <pkt_goście> [--spread L] [--total L]` - zwycięzca, spread, total (rozkład normalny).
- `nba-analyst/scripts/nba_props.py <rynek> <średnia> [linie]` - punkty, zbiórki, asysty, trójki, PRA, total drużyny.
- `nhl-analyst/scripts/nhl_model.py <λ_gospodarze> <λ_goście> [--total L]` - wynik po 60', moneyline z dogrywką, puck line ±1.5, total goli.
- `nhl-analyst/scripts/nhl_props.py <rynek> <średnia> [linie]` - strzały, punkty, strzelec gola, obrony bramkarza.
- `bet-slip-builder/scripts/slip.py "opis" p kurs ...` - łączne p, fair odds, EV zestawu.
- `predictions-verifier/scripts/verify.py <plik.json>` - bilans trafień vs oczekiwane, Brier, kupony, zysk hipotetyczny (format JSON w nagłówku skryptu).

**Używaj skilli, gdy zadanie ich wymaga.** Każde zadanie z zakresu flow (terminarz, analiza meczu, TOP/kupon, weryfikacja typów) realizuj przez odpowiedni skill (`sports-fixtures-finder`, `football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst`, `bet-slip-builder`, `predictions-verifier`), wywołując go narzędziem Skill, zamiast robić to ad hoc. Dotyczy to też próśb bez słów kluczowych (same nazwy drużyn/zawodników, data, "co grają"). Skilli nie uruchamiaj do zadań spoza flow (np. edycja CLAUDE.md, git).

**Używaj serwerów MCP, jeśli to możliwe.** Do researchu w sieci i pobierania danych (terminarze, statystyki, kursy, newsy) korzystaj w pierwszej kolejności z dostępnych narzędzi MCP (np. `mcp__claude-in-chrome__*` do stron wymagających przeglądarki), a dopiero potem z innych metod. Przed użyciem sprawdź, jakie serwery MCP są dostępne w sesji (deferred tools załaduj przez ToolSearch).

Stare skille `*-predictor` zostały zastąpione przez `*-analyst` (usunięcie nie jest zacommitowane); nie przywracaj ich bez prośby.

## Zasady, które wynikają z weryfikacji poprzednich typów

Są wpisane w `SKILL.md` skilli analitycznych (krok "Skalibruj"); zmieniając je, zachowaj uzasadnienia:
- Sygnał ryzyka musi zmienić liczbę, nie tylko opis.
- W rankingach i kuponach pomijaj typy z fair odds ≤ 1.15.
- Domyślne progi kuponu, jeśli użytkownik nie poda innych w zapytaniu (`bet-slip-builder`): kurs > 1.2 wymagany tylko dla dwóch nóg w kuponie (reszta może być ≤ 1.2), łączny kurs zestawu > 1.5 i < 2.5, EV > 0, własne p > 50%. Przy każdym zestawie podawaj EV, p i proponowaną stawkę jako % bankrolla (ułamek Kelly'ego). Jeśli bazowe progi nie dają kuponów, stosuj poziomy luzowania 0-6 z `bet-slip-builder` (wszystkie automatycznie, po kolei, z oznaczeniem poziomu); nie fabrykuj typu.
- Piłka: ryzyko to remis ORAZ wygrana underdoga; kryzys dotyczy tylko underdoga; puchary z rotacją i reprezentacje (λ ≥ ~0,7) mają osobne korekty.
- Tenis: 35+ w bo5, zmęczenie vs forma, faworyt po wolnym losie/przerwie; bez total gemów przy p_serve oszacowanym z rankingu.
- NBA i NHL: skille są nowe i nie mają jeszcze zweryfikowanych typów, więc sekcje "Skalibruj" opierają się na ogólnych zasadach; po pierwszej weryfikacji dopisz tam konkretne lekcje. NBA: status zawodnika z injury reportu i blowout w rynkach zawodnika. NHL: potwierdzony bramkarz startowy, rozliczenie 60 minut vs dogrywka.

## Wyniki w analizy/

Pliki nazywane `<Opis>_<RRRR-MM-DD>.md` (analizy meczów, `Top10_predykcje_*`, `Weryfikacja_predykcji_*`). Weryfikacje porównują typy z rzeczywistymi wynikami i są źródłem kalibracji skilli.

**Oznaczanie zweryfikowanych plików:** po pełnej weryfikacji dodaj do nazwy zweryfikowanego pliku prefiks `ZWERYFIKOWANE_` (np. `ZWERYFIKOWANE_Top10_predykcje_2026-10-08.md`) i popraw odwołania do starej nazwy w plikach `Weryfikacja_*`. Przy weryfikacji częściowej (część meczów jeszcze nie rozegrana) nie oznaczaj; zrób to po uzupełnieniu.

## Git

Commity po polsku, w stylu istniejącej historii (np. "TOP 10 predykcji 27.09.2026 (...)", "Weryfikacja predykcji z ... i kalibracja skilli"). Praca przez gałęzie `claude/*` i pull requesty do `main`.
