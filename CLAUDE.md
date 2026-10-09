# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Charakter repozytorium

Brak aplikacji, buildu i testów. Repo służy do analizy i typowania wydarzeń sportowych (piłka nożna, tenis ATP/WTA, e-sport CS2/LoL/Dota 2). Całość pracy odbywa się przez skille Claude Code w `.claude/skills/`, a wyniki zapisują się jako pliki Markdown w `analizy/`. Język pracy i raportów: polski.

## Flow przetwarzania

Standardowy przebieg pracy, w tej kolejności; każdy krok korzysta z wyników poprzedniego:

1. **Wyszukiwanie wydarzeń sportowych** (`sports-fixtures-finder`) - mecze piłkarskie, tenisowe i e-sportowe z zadanego okresu; sam terminarz, bez analizy.
2. **Dokładna analiza wyszukanych wydarzeń** (`football-analyst`, `tennis-analyst`, `esports-analyst`) - dla każdego meczu statystyki drużyn/zawodników, H2H, informacje medialne z sieci; wynik: prawdopodobieństwa i fair odds.
3. **Analiza kursów i wybór najbardziej prawdopodobnych predykcji** (wszystkie rynki, nie tylko wynik: gole, BTTS, rożne, kartki, faule, rynki zawodnika) (`bet-slip-builder`) - zestawienie wyników analiz z kursami bukmacherskimi (EV), wybór typów o największym prawdopodobieństwie i złożenie zestawów bez sprzecznych typów. Wynik zapisuj w `analizy/` (np. `Top10_predykcje_<data>.md`).

Nie przeskakuj kroku 2: krok 3 nie wymyśla prawdopodobieństw, tylko korzysta z gotowych analiz.

## Skille i ich zależności

Pięć skilli realizuje powyższy flow; każdy ma `SKILL.md`, a niektóre skrypt Pythona (bez zewnętrznych zależności) i `evals/evals.json`. Dane zawsze z researchu w sieci, nie z pamięci.

Skrypty liczą rozkłady z parametrów wejściowych (uruchamiane z katalogu skilla):
- `football-analyst/scripts/poisson.py <λ_gospodarze> <λ_goście>` - 1X2, O/U, BTTS, wyniki.
- `football-analyst/scripts/markets.py <rynek> <średnia> [linie]` - rożne, kartki, faule, strzały, rynki zawodnika (Over/Under, rozkład NB).
- `tennis-analyst/scripts/tennis_model.py <p_serve_A> <p_serve_B> [--bo 3|5] [--tiebreak 7|10]` - model punkt→gem→set→mecz.
- `esports-analyst/scripts/series.py <p_mapa...> [--bo 1|3|5]` - wynik serii, handicap ±1.5, total map.
- `bet-slip-builder/scripts/slip.py "opis" p kurs ...` - łączne p, fair odds, EV zestawu.

**Używaj skilli, gdy zadanie ich wymaga.** Każde zadanie z zakresu flow (terminarz, analiza meczu, TOP/kupon) realizuj przez odpowiedni skill (`sports-fixtures-finder`, `football-analyst`, `tennis-analyst`, `esports-analyst`, `bet-slip-builder`), wywołując go narzędziem Skill, zamiast robić to ad hoc. Dotyczy to też próśb bez słów kluczowych (same nazwy drużyn/zawodników, data, "co grają"). Skilli nie uruchamiaj do zadań spoza flow (np. edycja CLAUDE.md, git).

**Używaj serwerów MCP, jeśli to możliwe.** Do researchu w sieci i pobierania danych (terminarze, statystyki, kursy, newsy) korzystaj w pierwszej kolejności z dostępnych narzędzi MCP (np. `mcp__claude-in-chrome__*` do stron wymagających przeglądarki), a dopiero potem z innych metod. Przed użyciem sprawdź, jakie serwery MCP są dostępne w sesji (deferred tools załaduj przez ToolSearch).

Stare skille `*-predictor` zostały zastąpione przez `*-analyst` (usunięcie nie jest zacommitowane); nie przywracaj ich bez prośby.

## Zasady, które wynikają z weryfikacji poprzednich typów

Są wpisane w `SKILL.md` skilli analitycznych (krok "Skalibruj"); zmieniając je, zachowaj uzasadnienia:
- Sygnał ryzyka musi zmienić liczbę, nie tylko opis.
- W rankingach i kuponach pomijaj typy z fair odds ≤ 1.15.
- Piłka: ryzyko to remis ORAZ wygrana underdoga; kryzys dotyczy tylko underdoga; puchary z rotacją i reprezentacje (λ ≥ ~0,7) mają osobne korekty.
- Tenis: 35+ w bo5, zmęczenie vs forma, faworyt po wolnym losie/przerwie; bez total gemów przy p_serve oszacowanym z rankingu.

## Wyniki w analizy/

Pliki nazywane `<Opis>_<RRRR-MM-DD>.md` (analizy meczów, `Top10_predykcje_*`, `Weryfikacja_predykcji_*`). Weryfikacje porównują typy z rzeczywistymi wynikami i są źródłem kalibracji skilli.

## Git

Commity po polsku, w stylu istniejącej historii (np. "TOP 10 predykcji 27.09.2026 (...)", "Weryfikacja predykcji z ... i kalibracja skilli"). Praca przez gałęzie `claude/*` i pull requesty do `main`.
