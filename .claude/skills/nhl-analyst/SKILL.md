---
name: nhl-analyst
description: Analiza meczów NHL na podstawie czterech filarów - statystyk drużyn (gole, xG i udział w strzałach, special teams, forma, dom/wyjazd, bramkarze), statystyk poprzednich spotkań (H2H), informacji medialnych z internetu (potwierdzony bramkarz startowy, kontuzje, back-to-back, podróże, trener, skład na lodzie) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca z dogrywką i karnymi, wynik po 60 minutach, puck line ±1.5, total goli, rynki zawodnika: strzały, punkty, strzelec gola, obrony bramkarza) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/dnia NHL, pyta o szanse drużyny, puck line, total, player props, value bet, kursy albo podaje same nazwy drużyn NHL (Oilers, Bruins, Panthers...) lub zawodników (McDavid, Draisaitl, MacKinnon...) - nawet bez słowa "NHL" czy "hokej".
---

# Analiza meczów NHL

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, połączyć je w oczekiwane gole obu drużyn i uczciwie powiedzieć, jak bardzo wynik jest niepewny. Hokej ma niskie wyniki i dużą losowość (faworyt rzadko ma więcej niż ~65%), a największy pojedynczy czynnik to **bramkarz startowy**, więc zawsze potwierdzaj, kto stoi w bramce. Zawsze zaczynaj od researchu (MCP, potem WebSearch/WebFetch), nie z pamięci.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (bramkarze startowi, xG, props). Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation. Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Terminarz/wyniki:** `nhl_schedule`, `nhl_scores`, `nhl_club_schedule` (terminarz klubu, widać back-to-back), `espn_scoreboard` (`sport=hockey`, `league=nhl`, `dates=YYYYMMDD` pojedynczo; godziny w UTC), `sportsdataio_nhl_games_by_date`, `apisports_hockey_games` (klucz).
- **Tabela i statystyki:** `nhl_standings`, `espn_standings`, `nhl_boxscore`, `nhl_game_landing` (szczegóły meczu, często z zapowiedzią i statusem bramkarzy), `nhl_goalie_leaders`, `nhl_skater_leaders`, `nhl_roster`, `nhl_player` (statystyki i gamelog zawodnika).
- **Kursy (filar 4):** `pinnacle_sport_matchups_all`/`pinnacle_league_matchups` (hokej; potwierdź `sportId` przez `pinnacle_sports`, tylko `hasMarkets: true`, kursy amerykańskie przelicz na dziesiętne), `theoddsapi_odds` (`icehockey_nhl`; `h2h`, `spreads`, `totals`), `oddsapiio_odds`. Pinnacle często wycenia rynek bramkarza dopiero po jego potwierdzeniu: zmiana linii to sygnał.
- xG, udział w strzałach (CF%/xGF%) i GSAx bramkarzy zwykle trzeba wziąć z sieci (MoneyPuck, Natural Stat Trick, Evolving-Hockey, DailyFaceoff); ESPN/NHL.com dają podstawy.
- Duże odpowiedzi zapisują się do pliku: czytaj je przez `jq`, nie wczytuj w całości.

## BettingPros (skill `bettingpros-odds`)

Dla NBA/NHL/piłki (i innych sportów, które API zwraca - sprawdź `events --sport <X>`) wywołaj skill `bettingpros-odds` jako dodatkowe źródło: konsensus linii i kursów z wielu bukmacherów, `best_lines`, a przy rynkach zawodnika rekomendacje `props` (probability, EV, bet rating, forma last_N). Skill najpierw pyta o klucz API, jeśli `BETTINGPROS_API_KEY` nie jest ustawiona; bez klucza pomiń to źródło i zaznacz to w raporcie (nie blokuj analizy). To kontrola i źródło kursów, nie zamiennik własnego p: różnica >10 pp względem rynku bez marży wymaga wyjaśnienia (skład, kontuzje), a niezgodność z `props` BettingPros to flaga do sprawdzenia, nie powód do zmiany liczby bez konkretów. W raporcie oznacz "BettingPros" przy każdej użytej linii/kursie.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki drużyn** - gole strzelone i stracone na mecz, xGF%/xGA, udział w strzałach (5v5), skuteczność gry w przewadze (PP%) i gra w osłabieniu (PK%), PDO (wskaźnik szczęścia; skrajne wartości wracają do 100), ostatnie 8-10 meczów z kontekstem rywali, bilans dom/wyjazd. **Początek sezonu (pierwsze ~15 meczów): próba jest mała**, więc mieszaj bieżące liczby z ubiegłym sezonem i zmianami w składach.
2. **Poprzednie spotkania (H2H)** - ostatnie 2-4 mecze z tym rywalem; w NHL waga niska, bo skład i bramkarze zmieniają się szybko.
3. **Informacje medialne** - **bramkarz startowy** (potwierdzany zwykle rano w dniu meczu po skate; DailyFaceoff, konferencje trenerów, Twitter dziennikarzy kadrowych; w drugim dniu back-to-back często gra rezerwowy), kontuzje i status (Day-to-Day, IR), lineup/pary obrońców i skład PP, back-to-back i seria wyjazdów, podróż przez strefy czasowe, zmiana trenera, motywacja (walka o playoff vs sezon bez stawki). Plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - moneyline, puck line, total. Po usunięciu marży to niezależny punkt odniesienia; gdy Twoje prawdopodobieństwo różni się od rynku o >7 pp, najpierw szukaj, czego nie wiesz (bramkarz, kontuzja), zanim uznasz to za value.

Jeśli kluczowych danych nie da się znaleźć, napisz to wprost i obniż pewność. Podawaj źródło (nazwa serwisu) przy każdym kluczowym fakcie.

## Krok 2: Policz

Wyznacz oczekiwane gole λ obu drużyn w regulaminowych 60 minutach: bazuj na średniej ligi (~3,0 gola na drużynę), sile ataku (xGF) i obrony (xGA) obu zespołów, z przewagą własnego lodu (ok. +0,1 gola), potem skoryguj o filar 3. Skala korekt (przybliżona, zawsze zmień liczbę): bramkarz startowy vs średni bramkarz ligi ±0,2 do 0,4 gola dla drużyny rywala (rezerwowy o słabym GSAx zwykle +0,2 do +0,4 goli dla przeciwnika), brak najlepszego strzelca/centra -0,1 do -0,2 gola, drugi dzień back-to-back -0,1 do -0,15 gola (i gorsza obrona), PP/PK wpisane w λ tylko, jeśli różnica specjalnych jest duża. Z λ policz rozkłady skryptem:

```bash
python scripts/nhl_model.py <λ_gospodarze> <λ_goście> [--total L ...]
python scripts/nhl_model.py 3.1 2.8 --total 5.5 6.5
```

Skrypt zwraca wynik po 60 minutach (3-way z remisem), moneyline (z dogrywką i karnymi), puck line ±1.5 i Over/Under totalu goli (regulamin + gol w dogrywce) z fair odds. **Zawsze podaj, który rynek wyceniasz:** 60 minut (3-way) czy z dogrywką (moneyline/total); to różne zakłady. Uwaga: Poisson zaniża remisy po 60' (w lidze ok. 22-24% meczów idzie do dogrywki), więc wartości remisu i dogrywki traktuj jako szkic.

### Krok 2b: Rynki zawodnika i bramkarza

Dla każdego meczu rozważ też rynki zawodnika, bo najlepszy typ meczu bywa gdzie indziej (np. Over strzałów gwiazdy, obrony bramkarza):

```bash
python scripts/nhl_props.py <rynek> <średnia> [linia ...] [--vmr X]
python scripts/nhl_props.py sog 3.4 2.5 3.5
python scripts/nhl_props.py saves 26.5 24.5 26.5
python scripts/nhl_props.py goals 0.38 0.5     # strzelec gola w meczu
```

Rynki: `sog` (strzały zawodnika), `goals` (Over 0.5 = strzelec gola w meczu), `assists`, `points`, `hits`, `blocks`, `saves` (obrony bramkarza), `shots_against`. Jak szacować średnią zawodnika: średnia na mecz z ostatnich 8-10 meczów w lidze × spodziewany czas na lodzie (linia, PP1/PP2) × czynnik rywala (liczba strzałów rywala, jakość bramkarza). **Obrony bramkarza** = oczekiwane strzały na jego bramkę (z drużyn, tempa, gry w osłabieniu) × oczekiwany SV%; typ tylko po potwierdzeniu startującego bramkarza. Zawodnik w statusie Day-to-Day bez potwierdzenia nie dostaje typu; typ warunkowy ("jeśli zagra") nie może być wariantem głównym kuponu. Strzelec gola w meczu rzadko przekracza ~45% nawet dla najlepszych strzelców, a "pewne" 60%+ jest podejrzane.

Min. dwa niezależne źródła liczb do średniej (np. NHL.com + Natural Stat Trick/MoneyPuck/Hockey-Reference); jeśli ich brak, daj niską pewność i **nie rekomenduj typu** na kupon.

## Krok 3: Skalibruj

Brak jeszcze zweryfikowanych typów NHL w `analizy/`, więc korzystaj z ogólnych zasad wynikających z weryfikacji innych dyscyplin, a po pierwszej weryfikacji NHL dopisz tu konkretne lekcje (z datą i meczem) w stylu `football-analyst`:

- **Sygnał ryzyka musi zmienić liczbę**, nie tylko opis: bramkarz, back-to-back, kontuzja centra zmieniają λ, a nie tylko tekst.
- **Hokej to wysoka losowość:** pułap pewności na zwycięzcę meczu to ok. 65-68% (nawet dla dużej różnicy klas); wyższe liczby wymagają ekstremalnej przewagi i potwierdzonego bramkarza. Oznacz wyrównane mecze (p 45-55%) jako "brak mocnego typu".
- **Nie schodź pod rynek o >5 pp bez konkretnej informacji.** Rynek NHL jest efektywny; sama "forma" nie wystarcza.
- **Forma faworyta jest już w kursie.** Nie obniżaj p faworyta za serię słabych meczów; zmienić p może konkretna informacja (bramkarz, kontuzja). Korekta "kryzysowa" dotyczy tylko underdoga. Zwróć uwagę na PDO: seria zwycięstw przy PDO > 102 to szczęście, nie siła.
- **Puck line -1.5 nie jest "bezpieczniejszą wygraną":** faworyt wygrywa o 2+ gole tylko w ok. 30-40% meczów (gole w pustą bramkę zawyżają różnice); +1.5 ma wysokie p, ale krótki kurs - sprawdź fair odds ≤ 1.15.
- **Bramkarz niepotwierdzony = pewność najwyżej średnia** dla zwycięzcy i totalu, a rynek bramkarza bez potwierdzenia dostaje niską pewność i nie wchodzi do kuponu.
- **Total goli:** Over/Under wymaga konkretu (bramkarz, absencje, back-to-back obu drużyn); ceny ukrywają dogrywkę, więc sprawdź, czy rynek liczy gole w OT (gol z karnych zwykle nie liczy się do totalu).
- **Rynki zawodnika:** pułap pewności "wysoka" tylko przy potwierdzonym składzie, linii i roli na PP; kolejne rynki tego samego zawodnika (strzały + punkty) są skorelowane.
- **Typy z fair odds ≤ 1.15** pomijaj w rankingach.

## Krok 4: Raport

Dla każdego meczu, po polsku, zwięźle:

```
### Gospodarz - Goście (data, godzina czasu polskiego; data lokalna USA)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Rynki dodatkowe:** tabela wycenionych rynków (p, fair, pewność): moneyline, 60 minut 3-way, puck line, total goli, ewentualnie rynki zawodnika/bramkarza; zaznacz najlepszy rynek meczu i czy dotyczy 60 minut czy z dogrywką
**Statystyki drużyn:** 2-3 zdania z liczbami (gole, xG, PP/PK, forma)
**H2H:** 1-2 zdania
**Bramkarze:** potwierdzony/przewidywany startowy każdej strony (źródło, godzina sprawdzenia), SV%/GSAx
**Informacje medialne:** kontuzje, back-to-back, kontekst (ze źródłem)
**Oczekiwane gole:** gospodarze X.X - goście X.X (łącznie X.X)
**Ryzyka:** scenariusze, w których typ przegrywa (np. zmiana bramkarza, gole w dogrywce, pusta bramka)
**Rynek:** kurs bukmachera vs fair odds (jeśli znany)
```

Przy przeglądzie wielu meczów dodaj ranking top-N **ze wszystkich rynków**, bez typów z fair odds ≤ 1.15 (przypadki 1.15-1.20 oznacz), oraz "tabelę kandydatów na kupon": mecz, rynek, p, fair, pewność, od czego zależy (bramkarz, skład) i czy kurs rynkowy jest znany, żeby `bet-slip-builder` miał gotowe wejście.

Zaznacz godzinę sprawdzenia bramkarzy i że skład może się zmienić do rozpoczęcia meczu. Zawsze przypomnij na końcu jednym zdaniem, że to oszacowania probabilistyczne, nie gwarancje.
