---
name: nba-analyst
description: Analiza meczów NBA na podstawie czterech filarów - statystyk drużyn (net rating, tempo, ofensywa/defensywa, forma, dom/wyjazd), statystyk poprzednich spotkań (H2H, mecze sezonu), informacji medialnych z internetu (injury report, status zawodników Out/Questionable/GTD, load management, back-to-back, podróże, rotacje, trener, motywacja) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca meczu, spread, total punktów, total drużyny, rynki zawodnika: punkty, zbiórki, asysty, trójki, PRA) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/dnia NBA, pyta o szanse drużyny, spread, total, player props, value bet, kursy albo podaje same nazwy drużyn NBA (Lakers, Celtics, Warriors...) lub zawodników (Jokić, Doncić, Wembanyama...) - nawet bez słowa "NBA" czy "koszykówka".
---

# Analiza meczów NBA

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, połączyć je w oczekiwane punkty obu drużyn i uczciwie powiedzieć, jak bardzo wynik jest niepewny. W NBA jedna informacja kadrowa (gwiazda poza grą) potrafi zmienić spread o 4-8 punktów, więc liczby bez świeżego injury reportu są zgadywaniem. Zawsze zaczynaj od researchu (MCP, potem WebSearch/WebFetch), nie z pamięci.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (injury report, konferencje, props). Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation. Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Terminarz/wyniki:** `nba_schedule`, `nba_scoreboard_today`, `espn_scoreboard` (`sport=basketball`, `league=nba`, `dates=YYYYMMDD` pojedynczo; godziny w UTC), `balldontlie_nba_games` (klucz).
- **Tabela i statystyki drużyn:** `espn_standings`, `balldontlie_nba_standings`, `nba_stats_call` (endpointy stats.nba.com, np. zestawienia drużyn z net/off/def rating i pace), `balldontlie_nba_season_averages`.
- **Zawodnicy i składy:** `nba_daily_lineups` (przewidywane/potwierdzone składy i statusy), `mysportsfeeds_injuries`, `balldontlie_nba_stats`/`_players`, `nba_boxscore` (minuty i statystyki z ostatnich meczów), `espn_game_summary`.
- **Kursy (filar 4):** `nba_odds_today`, `pinnacle_sport_matchups_all`/`pinnacle_league_matchups` (koszykówka; potwierdź `sportId` przez `pinnacle_sports`, tylko `hasMarkets: true`, kursy amerykańskie przelicz na dziesiętne), `theoddsapi_odds` (`basketball_nba`; `h2h`, `spreads`, `totals`; rynki zawodnika osobno i drożej), `oddsapiio_odds`. Pinnacle to dobry kurs odniesienia po usunięciu marży.
- Duże odpowiedzi zapisują się do pliku: czytaj je przez `jq`, nie wczytuj w całości.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki drużyn** - net rating, offensive/defensive rating, tempo (pace), eFG%, zbiórki, straty, ostatnie 8-10 meczów z kontekstem rywali, bilans dom/wyjazd. **Początek sezonu (pierwsze ~15 meczów): próba jest mała**, więc mieszaj bieżące liczby z ubiegłym sezonem i projekcjami (np. win totals rynku) po zmianach w składach, a nie ufaj 3-5 meczom.
2. **Poprzednie spotkania (H2H)** - ostatnie 2-4 mecze z tym rywalem, ale tylko przy podobnych składach; w NBA H2H waży mało (dużo bardziej ważny jest skład niż historia).
3. **Informacje medialne** - **injury report** (statusy Out / Doubtful / Questionable / Probable / GTD; raport publikowany dzień wcześniej i aktualizowany do ok. 90 min przed meczem), load management i oszczędzanie gwiazd w drugim dniu back-to-back, minuty po powrocie z kontuzji, zmiana trenera, trade, tanking (drużyny bez stawki), podróż i strefy czasowe, mecz u siebie po serii wyjazdów, pierwszy mecz po przerwie. Preferuj konferencje trenerów i dziennikarzy kadrowych; plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - spread, total i moneyline. Po usunięciu marży to niezależny punkt odniesienia; gdy Twoje prawdopodobieństwo różni się od rynku o >8 pp lub Twój spread o >3 punkty, najpierw szukaj, czego nie wiesz (status zawodnika, zmiana linii po injury report), zanim uznasz to za value.

Jeśli kluczowych danych nie da się znaleźć, napisz to wprost i obniż pewność. Podawaj źródło (nazwa serwisu) przy każdym kluczowym fakcie.

## Krok 2: Policz

Wyznacz oczekiwane punkty obu drużyn: tempo meczu (średnia pace obu drużyn, skorygowana o styl) × skuteczność ofensywna drużyny względem defensywy rywala (ORtg/DRtg), z przewagą własnego parkietu (ok. +2 do +3 pkt, to jest już w spreadzie), potem skoryguj o filar 3. Skala korekt (przybliżona, zawsze zmień liczbę): absencja gwiazdy (top-1/top-2 drużyny) -3 do -7 pkt w różnicy meczu, starter średniej klasy -1 do -2, drugi dzień back-to-back -1 do -2 w różnicy meczu (i -1 do -3 w sumie punktów, gdy drużyna gra wolniej), rywal po dniu wolnym kontra drużyna po back-to-back to dodatkowe -1 do -2. Z oczekiwanych punktów policz rozkład skryptem:

```bash
python scripts/nba_model.py <pkt_gospodarze> <pkt_goście> [--spread L ...] [--total L ...] [--sd-margin 12] [--sd-total 18]
python scripts/nba_model.py 114.5 110 --spread -4.5 -2.5 --total 222.5 225.5
```

Skrypt zwraca zwycięzcę, pokrycie spreadu i Over/Under totalu z fair odds (rozkład normalny; SD różnicy ~12, SD sumy ~18; zwiększ je o ok. 1-2 punkty, gdy status 2+ kluczowych graczy jest niejasny).

### Krok 2b: Rynki dodatkowe (nie ograniczaj się do zwycięzcy)

Dla każdego meczu wycen też total, spread i rynki zawodnika, bo najlepszy typ meczu bywa gdzie indziej (np. Under totalu przy dwóch drużynach z wolnym tempem, Over zbiórek przy brakach podkoszowych rywala). Skrypt do rynków zawodnika i drużyny:

```bash
python scripts/nba_props.py <rynek> <średnia> [linia ...] [--vmr X] [--sd X]
python scripts/nba_props.py points 24.8 22.5 24.5
python scripts/nba_props.py rebounds 8.9 7.5 8.5
python scripts/nba_props.py team_points 113 110.5 --sd 11
```

Rynki: `points`, `rebounds`, `assists`, `threes`, `steals`, `blocks`, `turnovers`, kombinacje `pra`/`pr`/`pa`/`ra` oraz `team_points`. Jak szacować średnię zawodnika: średnia na minutę z ostatnich 8-10 meczów × **spodziewane minuty** × czynnik rywala (pace, obrona pozycji, kto go kryje) × korekta o skład (brak innego strzelca podnosi użycie piłki, brak centra zbiórki). **Ryzyko blowoutu:** przy spreadzie ≥ 10 punktów gwiazdy obu drużyn tracą ostatnie 6-10 minut, obniż minuty (i średnią) zanim policzysz Over. Zawodnik w statusie Questionable/GTD bez potwierdzenia nie dostaje typu; typ warunkowy ("jeśli zagra") nie może być wariantem głównym kuponu.

Min. dwa niezależne źródła liczb do średniej (np. NBA.com stats + Basketball-Reference/ESPN/Cleaning the Glass); jeśli ich brak, daj niską pewność i **nie rekomenduj typu** na kupon.

## Krok 3: Skalibruj

Brak jeszcze zweryfikowanych typów NBA w `analizy/`, więc korzystaj z ogólnych zasad wynikających z weryfikacji innych dyscyplin, a po pierwszej weryfikacji NBA dopisz tu konkretne lekcje (z datą i meczem) w stylu `football-analyst`:

- **Sygnał ryzyka musi zmienić liczbę**, nie tylko opis: injury report, back-to-back, blowout, tanking zmieniają oczekiwane punkty lub minuty, a nie tylko tekst.
- **Nie schodź pod rynek o >5 pp bez konkretnej informacji** (status zawodnika, rotacja). NBA ma jeden z najefektywniejszych rynków: linia zamknięcia jest bardzo trafna, więc sama "forma" nie uzasadnia dużej rozbieżności.
- **Forma faworyta jest już w kursie.** Nie obniżaj p faworyta za serię słabych meczów; zmienić p może konkretna informacja kadrowa. Korekta "kryzysowa" dotyczy tylko underdoga.
- **Wygrana to nie pokrycie spreadu.** Faworyt z p = 75% na zwycięstwo ma zwykle ok. 50-55% na pokrycie spreadu; nie mieszaj tych rynków w ocenie pewności.
- **Wyrównane mecze** (p 45-55%, spread poniżej 3 pkt) oznacz jako "brak mocnego typu" - to uczciwa informacja, nie porażka analizy.
- **Early season i pierwszy mecz po zmianie składu:** podnieś SD i obniż pewność; nie wyciągaj mocnych wniosków z 3-5 meczów.
- **Wolne tempo + dwie świetne obrony** nie wystarczą do Under, jeśli rynek już to uwzględnia; potrzebujesz konkretu (brak strzelca, back-to-back obu drużyn, sędzia o niskiej liczbie rzutów wolnych).
- **Rynki zawodnika:** pułap pewności "wysoka" tylko przy potwierdzonym składzie i minutach; spread ≥ 10 = ryzyko blowoutu, który obniża minuty; kolejne rynki tego samego zawodnika (punkty + PRA) są skorelowane, nie traktuj ich jak niezależnych.
- **Typy z fair odds ≤ 1.15** pomijaj w rankingach.

## Krok 4: Raport

Dla każdego meczu, po polsku, zwięźle:

```
### Gospodarz - Goście (data, godzina czasu polskiego; data lokalna USA)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Rynki dodatkowe:** tabela wycenionych rynków (p, fair, pewność): zwycięzca, spread, total, total drużyny, ewentualnie rynki zawodnika; zaznacz najlepszy rynek meczu
**Statystyki drużyn:** 2-3 zdania z liczbami (net rating, pace, forma)
**H2H:** 1-2 zdania
**Informacje medialne:** injury report ze statusami, back-to-back, kontekst (ze źródłem i godziną sprawdzenia)
**Oczekiwane punkty:** gospodarze XXX - goście XXX (spread, total)
**Ryzyka:** scenariusze, w których typ przegrywa (np. gwiazda wypadnie ze składu, blowout)
**Rynek:** kurs bukmachera vs fair odds (jeśli znany)
```

Przy przeglądzie wielu meczów dodaj ranking top-N **ze wszystkich rynków**, bez typów z fair odds ≤ 1.15 (przypadki 1.15-1.20 oznacz), oraz "tabelę kandydatów na kupon": mecz, rynek, p, fair, pewność, od czego zależy (status zawodnika, minuty) i czy kurs rynkowy jest znany, żeby `bet-slip-builder` miał gotowe wejście.

Zaznacz godzinę sprawdzenia injury reportu i że status może się zmienić do rozpoczęcia meczu. Zawsze przypomnij na końcu jednym zdaniem, że to oszacowania probabilistyczne, nie gwarancje.
