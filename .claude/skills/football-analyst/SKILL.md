---
name: football-analyst
description: Analiza meczów piłki nożnej na podstawie czterech filarów - statystyk drużyn (forma, gole, xG, strzały, rożne, kartki), statystyk poprzednich spotkań (H2H), informacji medialnych z internetu (kontuzje, zawieszenia, przewidywane składy, trener, motywacja, zapowiedzi) oraz kursów rynkowych - i wycena prawdopodobieństw (1X2, podwójna szansa, gole over/under, BTTS, dokładny wynik, rożne, kartki, faule meczowe, rynki zawodnika: faule, kartki, strzały, awans w pucharze) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/kolejki piłkarskiej, pyta o szanse drużyny, formę, H2H, value bet, kursy albo podaje samą nazwę meczu, drużyn, ligi lub datę - nawet bez słowa "analiza" czy "piłka nożna".
---

# Analiza meczów piłkarskich

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, połączyć je w jedno oszacowanie prawdopodobieństwa i uczciwie powiedzieć, jak bardzo jest ono niepewne. Liczby bez świeżych danych są zgadywaniem, więc zawsze zaczynaj od researchu (WebSearch/WebFetch), nie z pamięci - składy, kontuzje i trenerzy zmieniają się co tydzień.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (kontuzje, składy, konferencje, Ekstraklasa). Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation. Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Terminarz/wyniki/tabela:** `espn_scoreboard` i `espn_standings` (bez klucza; `soccer`, `eng.1`/`esp.1`/`ita.1`/`ger.1`/`fra.1`, data `YYYYMMDD` pojedynczo), `footballdataorg_standings`/`_matches` (kody `PL`, `PD`, `SA`, `BL1`, `FL1`; `FOOTBALL_DATA_ORG_KEY`; wybierz tabelę `type == "TOTAL"`), `pl_*` (Premier League: `pl_team_form`, `pl_match_stats`, `pl_match_lineups`), `laliga_*`, `seriea_*`, `openligadb_*` (Bundesliga).
- **Statystyki i H2H:** `apisports_football_fixtures`, `_fixture_statistics`, `_h2h`, `_predictions` (`API_SPORTS_KEY`), `espn_game_summary`, `sportmonks_*`, `footballdatauk_season` (historyczne wyniki i kursy).
- **Kursy (rynek, filar 4):** `pinnacle_sport_matchups_all`/`pinnacle_league_matchups` (soccer `sportId` 29, tylko `hasMarkets: true`, kursy w formacie amerykańskim, przelicz na dziesiętne, bez klucza), `theoddsapi_odds` (`THE_ODDS_API_KEY`, `h2h`/`totals`; każdy rynek × region kosztuje kredyty, sprawdź klucze przez darmowe `theoddsapi_sports`), `oddsapiio_odds`, `apisports_football_odds`. Pinnacle to dobry kurs odniesienia po usunięciu marży.
- Duże odpowiedzi zapisują się do pliku: czytaj je przez `jq`, nie wczytuj w całości.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki drużyn** - ostatnie 5-8 meczów każdej drużyny osobno u siebie / na wyjeździe: gole strzelone i stracone, xG/xGA jeśli dostępne, strzały i celne, rożne, faule/kartki, pozycja w tabeli. Forma bez kontekstu przeciwników wprowadza w błąd - zapisz, z kim grali.
2. **Poprzednie spotkania (H2H)** - ostatnie 3-6 bezpośrednich meczów, wyniki i przebieg (nie tylko kto wygrał), ale tylko z ostatnich ~3 lat i przy podobnych trenerach/składach; stare H2H waż nisko.
3. **Informacje medialne** - kontuzje i zawieszenia kluczowych zawodników, przewidywane składy, zmiana trenera, kryzys w klubie, motywacja (walka o tytuł/utrzymanie, mecz o nic), zmęczenie (puchary w środku tygodnia), rotacja, pogoda, sędzia (kartki/rożne). Preferuj konferencje prasowe i serwisy z przewidywanymi składami; plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - kursy bukmacherów, jeśli dostępne. Po usunięciu marży to niezależny punkt odniesienia: gdy Twoja liczba różni się od rynku o >10 pp, najpierw szukaj, czego nie wiesz, zanim uznasz, że to value.

Jeśli kluczowych danych nie da się znaleźć, napisz to wprost i obniż pewność zamiast wypełniać luki domysłami. Podawaj źródło (nazwa serwisu) przy każdym kluczowym fakcie.

## Krok 2: Policz

Wyznacz oczekiwane gole λ dla obu drużyn: bazuj na średniej ligi, sile ataku i obrony (gole/xG u siebie i na wyjeździe), potem skoryguj o informacje z filaru 3. Z λ policz rozkład Poissona skryptem:

```bash
python scripts/poisson.py <lambda_gospodarze> <lambda_goscie>
```

Skrypt zwraca 1X2, Over/Under 1.5/2.5/3.5, BTTS i najbardziej prawdopodobne wyniki, wraz z fair odds (1/p).

### Krok 2b: Rynki dodatkowe (nie ograniczaj się do wyniku)

Dla każdego meczu wycen też rynki poza 1X2, bo najlepszy typ meczu bywa gdzie indziej (np. rożne, kartki, BTTS). Oszacuj oczekiwaną średnią zdarzeń i policz Over/Under skryptem (rozkład ujemny dwumianowy z nadmierną wariancją):

```bash
python scripts/markets.py <rynek> <średnia> [linia ...] [--vmr X]
python scripts/markets.py corners 10.4 9.5 10.5
python scripts/markets.py cards 4.6 3.5 4.5
python scripts/markets.py player_fouls 1.8 0.5 1.5
```

Rynki: `corners`, `cards`, `fouls`, `shots`, `sot`, `offsides`, `goals` (meczowe: średnia = suma obu drużyn) oraz `player_fouls`, `player_cards`, `player_shots`, `player_sot` (jeden zawodnik). Jak szacować średnią:
- **Rożne:** średnia rożnych zdobytych przez drużynę A i przepuszczonych przez B (osobno dom/wyjazd), uśrednij ich ataki i obrony; faworyt dominujący i broniący się rywal zwiększa rożne gospodarza; mecz zamknięty i wolne tempo obniżają. Rożne korelują z golami słabo, więc nie traktuj Over goli jako sygnału na rożne.
- **Kartki:** średnia kartek sędziego (to najsilniejszy predyktor: weź ostatnie 8-10 meczów tego sędziego w tej lidze) skorygowana o styl drużyn (faule/kartki własne i wymuszone), stawkę (derby, walka o utrzymanie) i różnicę klas. Podaj, czy liczysz kartki jako liczbę (żółta = 1, czerwona = 2 lub osobno) i jak u bukmachera.
- **Faule meczowe:** średnia fauli obu drużyn skorygowana o sędziego (liberalny/surowy) i tempo.
- **Rynki zawodnika** (faule popełnione, faule na zawodniku, kartka, strzały, strzały celne): średnia na 90 min z ostatnich 8-10 meczów w lidze × spodziewane minuty × czynnik rywala (kto go kryje, jak pressuje rywal). Gdy skład nie jest znany, zawodnik nie dostaje typu (ryzyko niewejścia na boisko lub zejścia w 60. minucie). Kartka zawodnika: p z historii (kartki/mecz) × czynnik sędziego i pojedynku; rzadko przekracza 35-40%.
- **BTTS:** bierz z `poisson.py`, ale korektuj o formę ataków, kontuzje napastników i styl (BTTS tak rośnie, gdy obie drużyny tracą w ≥ 60% meczów).

Min. dwa niezależne źródła liczb do średniej (np. FBref/Sofascore/Flashscore/WhoScored + serwis sędziowski); jeśli ich brak, daj niską pewność i **nie rekomenduj typu** na kupon. Brak statystyk rożnych/fauli/kartek w MCP nie znaczy "brak typu": szukaj w sieci (WebSearch/WebFetch).

## Krok 3: Skalibruj (lekcje z weryfikacji ok. 100 poprzednich typów)

Te zasady wynikają z tego, gdzie wcześniejsze analizy realnie się myliły:

- **Ryzyko ma dwie twarze.** Dla faworyta z pewnością 50-85% wymień oba scenariusze porażki: remis i wygrana underdoga. Podobnej wagi - nie opisuj samego remisu.
- **Przepaść klas ≠ pewniak, gdy underdog jest w kryzysie** (świeża zmiana trenera, seria bez wygranej, desperacja). Wtedy realnie odejmij 5-10 pp od pewności faworyta, nie tylko wspomnij o tym w tekście. Korekta kryzysowa dotyczy wyłącznie underdoga, nigdy faworyta.
- **Puchary bez rewanżu z rotacją** (Carabao, Puchar Polski, Copa del Rey) mają więcej niespodzianek niż liga - obniż górny pułap pewności o kilka pp i napisz to w raporcie.
- **Reprezentacje:** nie schodź z λ drużyny poniżej ~0,7; łączne korekty kadrowe w dół nie więcej niż ~15%; Under 2.5 przy łącznym λ ≤ 2,0 daj najwyżej średnią pewność (gole padają często po 80. minucie).
- **Przy dużej rozbieżności z rynkiem** w meczu o dużej różnicy klas zaznacz, że rynek bywa trafniejszy.
- **Nie schodź pod rynek o >5 pp bez konkretnej informacji** (kontuzje kluczowych graczy, rotacja). Vitória - Chapecoense: moje 55% przy rynku 60,6% i λ 1,55/0,85 bez danych xG; wynik 4-0. Liczba kontuzji po obu stronach (6 vs 8) nie uzasadnia obniżenia gospodarza.
- **Wyrównane mecze** (blisko 50%) oznacz jako "brak mocnego typu" - to uczciwa informacja, nie porażka analizy.
- **Rynki dodatkowe (rożne, kartki, faule, rynki zawodnika)** mają większą wariancję niż gole i mniej danych, więc: (1) pułap pewności "wysoka" tylko przy znanym sędzi i potwierdzonych składach; (2) przy linii bukmachera rozbieżnej z Twoją średnią o >1,5 zdarzenia (rożne/faule) lub >1 (kartki) najpierw szukaj, czego nie wiesz, zanim uznasz to za value; (3) jeśli sędzia nie jest jeszcze znany (zwykle ogłaszany 2-3 dni przed meczem), policz kartki/faule ze średnią ligową i obniż pewność; (4) surowy sędzia (Over) lub łagodny (Under) to sygnał, który musi zmienić średnią kartek/fauli, nie tylko opis; (5) rynek zawodnika bez potwierdzonego składu to maksymalnie niska pewność.

Powód tych zasad: każde z tych pudeł wynikało z sygnału, który odnotowano w tekście, ale nie przełożono na liczbę. Jeśli coś wpływa na wynik, musi zmienić prawdopodobieństwo.

## Krok 4: Raport

Dla każdego meczu, po polsku, zwięźle:

```
### Gospodarz - Goście (liga, data, godzina)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Rynki dodatkowe:** tabela wszystkich wycenionych rynków (p, fair, pewność): 1X2/podwójna szansa, gole O/U 1.5-3.5, BTTS, rożne (średnia, linie), kartki (średnia, sędzia), faule, ewentualnie rynki zawodnika; zaznacz najlepszy rynek meczu (nie zawsze wynik)
**Statystyki drużyn:** 2-3 zdania z liczbami
**H2H:** 1-2 zdania
**Informacje medialne:** kluczowe absencje, skład, kontekst (ze źródłem)
**Ryzyka:** scenariusze, w których typ przegrywa
**Rynek:** kurs bukmachera vs fair odds (jeśli znany)
```

Przy przeglądzie wielu meczów dodaj na końcu ranking top-N **ze wszystkich rynków** (wynik, gole O/U, BTTS, rożne, kartki, faule, rynki zawodnika), nie tylko wyników. W rankingu pomijaj typy z fair odds ≤ 1.15 (zbyt krótkie, po marży bukmachera i tak bez wartości); jeśli najlepszy typ meczu odpada, sprawdź kolejny rynek tego samego meczu (np. rożne zamiast goli). Oznacz przypadki graniczne 1.15-1.20. Pod rankingiem daj "tabelę kandydatów na kupon": mecz, rynek, p, fair, pewność, od czego zależy (sędzia, skład) i czy kurs rynkowy jest znany, żeby `bet-slip-builder` miał gotowe wejście dla każdego rynku.

Zawsze przypomnij na końcu jednym zdaniem, że to oszacowania probabilistyczne, nie gwarancje.
