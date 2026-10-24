---
name: sports-fixtures-finder
description: Wyszukuje wydarzenia sportowe z zadanego okresu - mecze piłki nożnej, tenisa (ATP/WTA), e-sportu (CS2, LoL, Dota 2), MMA (gale UFC, KSW), koszykówki NBA i hokeja NHL - i zwraca uporządkowany terminarz z datą, godziną (czas polski), turniejem/ligą/galą i rangą meczu lub walki. Używaj zawsze, gdy użytkownik pyta co grają / jakie mecze i walki są dziś, jutro, w weekend, w danym dniu, tygodniu lub zakresie dat, prosi o terminarz, kalendarz, listę spotkań lub kartę gali, "co ciekawego do typowania" albo chce zebrać mecze przed analizą lub zestawieniem TOP - nawet gdy podaje tylko datę lub nazwę ligi/turnieju/gali. Ten skill tylko zbiera wydarzenia (dla NBA i NHL nie ma jeszcze skilla analitycznego); analizę i typy robią football-analyst, tennis-analyst, esports-analyst i mma-analyst.
---

# Wyszukiwanie wydarzeń sportowych

Cel: dla zadanego okresu zebrać prawdziwe, zweryfikowane mecze i walki z sześciu dyscyplin (piłka, tenis, e-sport, MMA, NBA, NHL) i zwrócić czytelny terminarz, który można wprost przekazać do analizy. Terminarze zmieniają się (przełożenia, zmiany godzin, wycofania), więc zawsze szukaj w sieci (WebSearch/WebFetch) i nie zgaduj z pamięci. Wymyślony mecz jest gorszy niż brak meczu.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) dają terminarze bez scrapowania stron. Dokumentacja: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation (plik per dostawca, np. ESPN.md, FootballDataOrg.md, APITennis.md, PandaScore.md). Zasady: WebSearch/WebFetch służą do weryfikacji drugim źródłem i do tego, czego MCP nie ma; kształty odpowiedzi części dostawców są nieweryfikowane, więc sprawdzaj realny payload.
- **Piłka:** `espn_scoreboard` (bez klucza; `sport=soccer`, `league` = `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`; `dates` = `YYYYMMDD`, pojedynczy dzień daje wiarygodny wynik, zakres `YYYYMMDD-YYYYMMDD` bywa odrzucany z HTTP 400; godziny w UTC, przelicz na polskie). Odpowiedź bywa ogromna (kilkadziesiąt tys. znaków) i trafia do pliku: wyciągaj `jq '.events[] | {name, date, status: .status.type.name}'`. Obecność Ekstraklasy w ESPN (`pol.1`) jest niezweryfikowana: sprawdź pojedynczą datą, a jeśli brak, terminarz Ekstraklasy bierz z sieci. Alternatywy: `footballdataorg_matches` (`dateFrom`/`dateTo`, max 10 dni, wymaga `FOOTBALL_DATA_ORG_KEY`), `openligadb_current_matchday` (Bundesliga, bez klucza), `pl_matchweek_matches`, `laliga_matches`, `seriea_matches`, `sportmonks_fixtures_by_date`.
- **Tenis:** `apitennis_fixtures` (wymaga `API_TENNIS_KEY`; łańcuch kluczy: `apitennis_events` → `apitennis_tournaments` → `apitennis_fixtures`), `wta_tournament_matches`.
- **E-sport:** `pandascore_matches` z `status=upcoming` (wymaga `PANDASCORE_TOKEN`; slugi: `csgo` dla CS2, `lol`, `dota2`; potwierdź przez `pandascore_videogames`).
- **MMA (UFC):** `ufc_events` (lista gal z datami i godzinami kart: early prelims / prelims / main card) i `ufc_event_card` (`title` = "UFC 330"; walki są w polu `included`, nie w `data`), bez klucza. Gdy zwraca bot-challenge lub puste dane (zdarzyło się 10.10.2026), karta z ufc.com, Tapology lub Sherdog przez WebFetch/WebSearch. **KSW i inne organizacje nie mają MCP:** karta z oficjalnej strony KSW, Tapology, Sherdog i polskich mediów.
- **NBA:** `espn_scoreboard` (`sport=basketball`, `league=nba`, `dates=YYYYMMDD`, pojedynczy dzień; godziny w UTC), `nba_schedule` (oficjalny terminarz NBA) i `nba_scoreboard_today` (dzisiejsze mecze), `balldontlie_nba_games` (wymaga klucza). Dla składów/kontuzji: `nba_daily_lineups`.
- **NHL:** `nhl_schedule` (oficjalne API NHL, bez klucza, terminarz tygodniowy od podanej daty), `nhl_scores` (wyniki/mecze dla dnia), `nhl_club_schedule` (terminarz klubu), alternatywnie `espn_scoreboard` (`sport=hockey`, `league=nhl`) i `sportsdataio_nhl_games_by_date`. Godziny w UTC, przelicz na polskie.
- Pusta lista `events: []` to brak meczów, nie błąd. Jeśli narzędzie zwraca błąd klucza, przejdź na kolejne źródło, nie powtarzaj w pętli.

## BettingPros (skill `bettingpros-odds`)

Dla sportów obsługiwanych przez API BettingPros (m.in. NBA, NHL, piłka) terminarz i `event_id` możesz pobrać skillem `bettingpros-odds` (`events --sport <X> --date <data>`; czasy w UTC, w wyniku podaj czas polski) i użyć go do weryfikacji kompletności listy. Skill pyta o klucz API, jeśli nie jest ustawiony; bez klucza pomiń. Nie zastępuje pozostałych źródeł.

## Krok 1: Ustal zakres

- **Okres:** przelicz "dziś/jutro/weekend" na konkretne daty (sprawdź dzisiejszą datę w kontekście). Zakres dłuższy niż ~7 dni zawęż do najważniejszych rozgrywek albo zapytaj, jak go zawęzić.
- **Dyscypliny:** domyślnie wszystkie sześć (piłka, tenis, e-sport, MMA, NBA, NHL); jeśli użytkownik wskazał jedną lub ligę/turniej, ogranicz się do tego.
- **Strefa czasowa:** podawaj godziny w czasie polskim (CET/CEST) i zaznacz to w nagłówku.
- **Ranga:** jeśli nie podano, dobierz sensowny zakres - piłka: Top 5 lig, Ekstraklasa, puchary europejskie, reprezentacje/turnieje, krajowe puchary; tenis: ATP/WTA Tour (Challengery i ITF tylko na życzenie); e-sport: tier-1 turnieje CS2/LoL/Dota 2 (tier-2 na życzenie); MMA: numerowane gale i Fight Night UFC oraz gale KSW (inne organizacje na życzenie); NBA i NHL: wszystkie mecze ligi w danym dniu (sezon zasadniczy, play-in, play-off, Puchar NBA), bo mecze są zawsze tej samej rangi, a przy dużej liczbie meczów wyróżnij najciekawsze.

## Krok 2: Wyszukaj

Dla każdej dyscypliny użyj co najmniej dwóch niezależnych źródeł dla daty i godziny, gdy to możliwe:
- **Piłka nożna:** oficjalne strony lig i UEFA, Flashscore/Sofascore, FBref, BBC Sport.
- **Tenis:** oficjalne strony ATP/WTA i turnieju (order of play), Flashscore, Tennis Explorer. Order of play często publikowany jest dzień wcześniej - dla dalszych dni podaj tylko turniej i rundę, bez wymyślania par.
- **E-sport:** Liquipedia (kalendarz turnieju i drabinka), HLTV (CS2), strony organizatorów (ESL, BLAST, PGL, Riot), gol.gg/lolesports (LoL).
- **NBA:** nba.com/schedule, ESPN, Basketball-Reference, Flashscore.
- **NHL:** nhl.com/schedule, ESPN, Hockey-Reference, Flashscore.
- **MMA:** ufc.com (karta i godziny), KSW (oficjalna strona i media społecznościowe), Tapology, Sherdog, polskie media (Sport.pl, Interia, Przegląd Sportowy).

Zasady jakości:
- Mecz bez potwierdzonej daty to "do potwierdzenia", nie pewny termin.
- Sprawdź, czy mecz nie został przełożony lub odwołany.
- W tenisie pary wyłaniają się z drabinki w trakcie turnieju; nie podawaj meczów późniejszych rund jako znanych.
- **MMA:** karta gali zmienia się do dnia ważenia (wypadnięcia, zastępstwa, walki odwołane po nieudanym ważeniu), więc zaznacz, czy karta jest potwierdzona, i wpisz godziny osobno dla bloków (early prelims, prelims, main card), a nie jedną godzinę gali. Godziny UFC z USA przelicz na czas polski (walki main card często po północy); na dole karty daj godzinę main eventu jako orientacyjną ("ok.").
- **NBA/NHL:** mecze rozgrywane są wieczorem czasu USA, więc w Polsce zaczynają się w nocy (np. 19:00 ET = 01:00 CEST następnego dnia). Przelicz godzinę na czas polski i **przypisz mecz do dnia kalendarzowego w Polsce**, a przy północnych godzinach dopisz w nawiasie datę lokalną USA, żeby uniknąć pomyłki o dzień. Uwaga na różnicę zmiany czasu USA/Europa (końcówka października i marzec: różnica 5 lub 6 h zamiast 6). Sprawdź, czy sezon już trwa (NBA i NHL startują w październiku) i czy mecz nie jest przedsezonowy (preseason oznacz wyraźnie albo pomiń). Dla meczów NBA/NHL zaznacz back-to-back oraz grę wyjazdową/domową, bo to kluczowe przy późniejszej analizie.
- Przy rozbieżności źródeł co do godziny podaj późniejszą źródłowo zweryfikowaną i zaznacz rozbieżność.
- **Ligę krajową sprawdzaj po dacie, nie po numerze kolejki.** Wniosek "liga w tym terminie nie gra" wyciągnięty z numeracji ("następna kolejka 23-25.10") jest niewiarygodny, bo przełożone kolejki bywają rozgrywane poza kolejnością. W analizach z 09.10.2026 napisano, że Ekstraklasa nie gra, a 9-12.10 odbyła się jej 10. kolejka (9 meczów). Przed napisaniem "brak meczów" sprawdź terminarz ligi dla każdej daty zakresu (strona ligi z listą meczów wg daty, Flashscore/Sofascore) i zaznacz źródło.

## Krok 3: Zwróć terminarz

Po polsku, pogrupuj według dnia, potem dyscypliny, w obrębie dyscypliny według rangi i godziny:

```
## Terminarz 07.10.2026 - 09.10.2026 (czas polski)

### Środa 07.10
**Piłka nożna**
- 21:00 Gospodarz - Goście | Liga Mistrzów, 1. kolejka
**Tenis**
- Rolex Paris Masters, 1/16 finału: Zawodnik A - Zawodnik B (ok. 13:00, kort centralny)
**E-sport**
- 18:00 Drużyna A - Drużyna B | CS2, IEM Dallas, ćwierćfinał, bo3
**NBA**
- 01:00 (wt. 07.10 USA: 19:00 ET) Gospodarz - Goście | sezon zasadniczy
**NHL**
- 01:30 (wt. 07.10 USA: 19:30 ET) Gospodarz - Goście | sezon zasadniczy
**MMA**
- UFC 330 (T-Mobile Arena, Las Vegas), karta potwierdzona: prelims 02:00, main card 04:00 (ok.)
  - Main event (5 rund, pas wagi lekkiej): Zawodnik A - Zawodnik B
  - Co-main (3 rundy, waga półśrednia): Zawodnik C - Zawodnik D
```

Dla MMA wypisz co najmniej main event, co-main i pozostałe walki main card; reszta karty w jednej linii lub na życzenie. Przy każdej walce podaj kategorię wagową i liczbę rund.

Na końcu podsumuj: liczbę meczów (walk) per dyscyplina, wskaż 3-5 najciekawszych (według rangi, wyrównania, stawki) i krótko zaznacz, czego nie udało się zweryfikować. Zapytaj, czy przekazać wybrane wydarzenia do analizy (football-analyst, tennis-analyst, esports-analyst, mma-analyst), ale nie rób analizy sam, jeśli użytkownik o to nie prosił.
