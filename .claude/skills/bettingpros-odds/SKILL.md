---
name: bettingpros-odds
description: Pobiera z API BettingPros (api.bettingpros.com/v3) terminarz wydarzeń, kursy z wielu bukmacherów (offers, best lines), rynki oraz projekcje i rekomendacje prop betów (prawdopodobieństwo, EV, bet rating, forma last 5/10/15, streaki) i wykorzystuje je jako dodatkowy sygnał przy predykcjach - porównanie własnego p z konsensusem rynku, szukanie najlepszej linii, kursy do bet-slip-builder, krzyżowa kontrola player props w NBA/NHL/piłce. Używaj zawsze, gdy użytkownik wspomina BettingPros, prosi o "kursy/linie z BettingPros", "best lines", "player props z API", "prop picks", EV lub bet rating z BettingPros, albo chce wzbogacić analizę NBA/NHL/piłki o dane tego API. ZAWSZE najpierw zapytaj użytkownika o klucz API (x-api-key), jeśli nie jest ustawiony - nigdy go nie zgaduj ani nie zapisuj w repozytorium.
---

# BettingPros API jako źródło kursów i sygnałów

Cel: użyć dokumentowanego API BettingPros (Consumer API 1.0.0, tylko odczyt, użytek osobisty) do pobrania kursów i projekcji, a następnie zestawić je z własnymi analizami (`nba-analyst`, `nhl-analyst`, `football-analyst`...). API **nie zastępuje** kroku 2 flow: jego `probability`/`expected_value` to cudze modele, traktuj je jak kontrolę i źródło kursów, a własne p pochodzi z analiz.

## Krok 0: klucz API (obowiązkowo)

1. Sprawdź `echo ${BETTINGPROS_API_KEY:+ustawiony}`. Jeśli pusto - **zapytaj użytkownika o klucz API BettingPros** (AskUserQuestion lub zwykłe pytanie) i nie wywołuj API, dopóki go nie poda.
2. Klucz przekazuj tylko jako zmienną środowiskową w poleceniu (`BETTINGPROS_API_KEY=... python3 scripts/bettingpros.py ...`) albo `--key`. Nie zapisuj go w plikach repo, `analizy/`, commitach ani w odpowiedzi. Użytkownik bez klucza: dostęp wymaga zatwierdzenia na https://api.bettingpros.com/docs/ (kontakt api@fantasypros.com), konto BettingPros.
3. Limity: Free i Plus 100 zapytań/dzień (do 20 wyników na stronę), Elite 1000/dzień (do 50). Reset o północy UTC. Płatne pola projekcji i dane picków (podział pieniędzy, eksperci) tylko Plus/Elite. Oszczędzaj zapytania: filtruj `sport`, `date`/`event_id`, `market_id`, używaj `--out`, nie pobieraj wszystkich stron bez potrzeby.
4. Błędy: 403 = zły/nieaktywny klucz (poproś o nowy), 429 `Limit Exceeded` = koniec dziennej puli (powiedz użytkownikowi, nie ponawiaj), 429 `Too Many Requests` = poczekaj chwilę, 503 = ponów po `Retry-After`.

## Endpointy (base `https://api.bettingpros.com/v3`, nagłówek `x-api-key`)

Skrypt `scripts/bettingpros.py` (stdlib, uruchamiany z katalogu skilla) opakowuje wszystkie; parametry podajesz jako `--nazwa wartość`, wiele wartości przez dwukropek (`NBA:NHL`, `market_id=1:2`).

| Komenda | Endpoint | Do czego |
|---|---|---|
| `events` | `/events` | terminarz: `sport`, `date` lub `start`/`end` (YYYY-MM-DD), `event_id`, `team_id`, `status`, `comp_id` (piłka: liga), `season`, `week`, `limit`, `page` |
| `markets` | `/markets` | lista rynków sportu: `sport`, `market_category` (`game-odds`, `game-props`, `player-props`), `market_slug`, `market_period` (`game`, `1h`, `2h`) |
| `counts` | `/markets/offer-counts` | które rynki mają oferty dla `event_id`; `book_id`, `include_participants` |
| `offers` | `/offers` | kursy/linie: **wymaga `market_id`**; `event_id`, `sport`, `player_id`/`player_slug`, `team_id`, `book_id`, `best_lines=true`, `live`, `location`, `picks=true`, `limit` |
| `props` | `/props` | projekcje prop betów: `sport`, `date`, `event_id`, `market_id`, `sort` (`expected_value`, `probability`, `bet_rating`, `diff`, `performance_over_percentage`...), `recommended_side`, `bet_rating` (1-5), `probability_min`, `min_odds`/`max_odds` (amerykańskie), `performance_type_filter` (`last_5/10/15/20/season/h2h`), `player_name_filter` (≥3 znaki), `include_books`, `include_markets` |
| `books` | `/books` | bukmacherzy (`location` np. `NY`); potrzebne do mapowania `book_id` |
| `odds` | lokalnie | konwersja kursów amerykańskich/dziesiętnych, p implikowane, marża i p bez marży dla 2-3 stron |

Parametry `auth`, `user`, `key` (w query), `x-level`, `bp_partner_id`, `debug`, `fence` są dla partnerów/klientów BettingPros - nie używaj ich. Zdjęcia zawodników i loga drużyn nie są zwracane.

## Krok 1: Rozpoznaj dane (kształty odpowiedzi nie są w dokumentacji)

Dokumentacja pokazuje tylko szkielet (`events`, `offers`, `props`, `markets`, `books`, `_pagination`, `ts`), a zawartość obiektów jest pusta, więc **przy pierwszym wywołaniu w sesji obejrzyj realny payload** (`--limit 1`, `--out` do scratchpadu) i dopiero potem wyciągaj pola. Nie zakładaj nazw pól z pamięci.

Typowa kolejność:
1. `events --sport NBA --date <data>` → `event_id` (czas w odpowiedzi jest w UTC, w raporcie podaj czas polski).
2. `markets --sport NBA` (raz; zapisz `market_id` głównych rynków: moneyline, spread, total, rynki zawodnika) albo `counts --event_id ...`, żeby zobaczyć, co jest dostępne dla meczu.
3. `offers --sport NBA --event_id ... --market_id ... --best_lines true` → linie i kursy po bukmacherach; mapuj `book_id` przez `books`.
4. `props --sport NBA --date <data> --sort expected_value --limit 20` → kandydaci do porównania z własnymi p z `nba_props.py` / `nhl_props.py`.

Sporty: dokumentacja podaje m.in. `NFL`, `MLB`, `SOCCER`, `NBA`, `NHL`; dla innych (tenis, MMA, e-sport) nie ma potwierdzenia, więc sprawdź, czy `events --sport <X>` coś zwraca, zanim obiecasz pokrycie. Piłka: ligę filtruj `comp_id`.

## Krok 2: Użyj w predykcjach

- **Kursy do `bet-slip-builder`:** to kursy zagraniczne/amerykańskie (konwertuj: dodatni `1+x/100`, ujemny `1+100/|x|`; `odds` robi to automatycznie). Domyślne źródła kursów w repo zostają (Betclic → gg397.bet); BettingPros wchodzi jako trzecie źródło lub do rynków, których tam brak (np. player props), zawsze z jawnym oznaczeniem "BettingPros, book: <nazwa>". Nie podawaj go jako kursu polskiego bukmachera.
- **Kontrola własnego p:** policz p bez marży z linii konsensusu (`odds`) i porównaj z własnym p. Różnica >10 pp = obniż pewność albo znajdź powód (kontuzja, skład), jak w kroku "Wyceń" z `bet-slip-builder`.
- **Sygnał z `props`:** `probability`, `expected_value`, `bet_rating`, `recommended_side`, forma `last_N` to cudze modele. Traktuj zgodność z własną analizą jako wzmocnienie, a niezgodność jako flagę do sprawdzenia (status zawodnika, minuty, blowout), nie jako powód do zmiany p bez konkretów. Typ wyłącznie z rekomendacji BettingPros, bez własnej analizy, nie wchodzi do zestawów (reguła "zawsze pełna analiza").
- **Best line:** przy typie player prop wskaż książkę z najlepszą linią i kursem; różnica linii o 0,5 pkt zmienia p, więc przelicz p dla linii, którą faktycznie bierzesz.
- Pomijaj typy z fair odds ≤ 1.15 i stosuj progi kuponów z `bet-slip-builder`.

## Krok 3: Raport

Podaj: zapytania, które wykonałeś (bez klucza), liczbę zużytych zapytań z dziennej puli, tabelę typ / linia / kurs / book / p własne / p rynku bez marży / EV / flagi. Wyniki zapisuj w `analizy/` zgodnie z konwencją `<Opis>_<RRRR-MM-DD>.md`, jeśli użytkownik prosi o plik. Surowe JSON-y trzymaj w scratchpadzie, nie w repo.
