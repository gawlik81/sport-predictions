---
name: sports-fixtures-finder
description: Wyszukuje wydarzenia sportowe z zadanego okresu - mecze piłki nożnej, tenisa (ATP/WTA) i e-sportu (CS2, LoL, Dota 2) - i zwraca uporządkowany terminarz z datą, godziną (czas polski), turniejem/ligą i rangą meczu. Używaj zawsze, gdy użytkownik pyta co grają / jakie mecze są dziś, jutro, w weekend, w danym dniu, tygodniu lub zakresie dat, prosi o terminarz, kalendarz, listę spotkań, "co ciekawego do typowania" albo chce zebrać mecze przed analizą lub zestawieniem TOP - nawet gdy podaje tylko datę lub nazwę ligi/turnieju. Ten skill tylko zbiera mecze; analizę i typy robią football-analyst, tennis-analyst i esports-analyst.
---

# Wyszukiwanie wydarzeń sportowych

Cel: dla zadanego okresu zebrać prawdziwe, zweryfikowane mecze z trzech dyscyplin i zwrócić czytelny terminarz, który można wprost przekazać do analizy. Terminarze zmieniają się (przełożenia, zmiany godzin, wycofania), więc zawsze szukaj w sieci (WebSearch/WebFetch) i nie zgaduj z pamięci. Wymyślony mecz jest gorszy niż brak meczu.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) dają terminarze bez scrapowania stron. Dokumentacja: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation (plik per dostawca, np. ESPN.md, FootballDataOrg.md, APITennis.md, PandaScore.md). Zasady: WebSearch/WebFetch służą do weryfikacji drugim źródłem i do tego, czego MCP nie ma; kształty odpowiedzi części dostawców są nieweryfikowane, więc sprawdzaj realny payload.
- **Piłka:** `espn_scoreboard` (bez klucza; `sport=soccer`, `league` = `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`; `dates` = `YYYYMMDD`, pojedynczy dzień daje wiarygodny wynik, zakres `YYYYMMDD-YYYYMMDD` bywa odrzucany z HTTP 400; godziny w UTC, przelicz na polskie). Odpowiedź bywa ogromna (kilkadziesiąt tys. znaków) i trafia do pliku: wyciągaj `jq '.events[] | {name, date, status: .status.type.name}'`. Obecność Ekstraklasy w ESPN (`pol.1`) jest niezweryfikowana: sprawdź pojedynczą datą, a jeśli brak, terminarz Ekstraklasy bierz z sieci. Alternatywy: `footballdataorg_matches` (`dateFrom`/`dateTo`, max 10 dni, wymaga `FOOTBALL_DATA_ORG_KEY`), `openligadb_current_matchday` (Bundesliga, bez klucza), `pl_matchweek_matches`, `laliga_matches`, `seriea_matches`, `sportmonks_fixtures_by_date`.
- **Tenis:** `apitennis_fixtures` (wymaga `API_TENNIS_KEY`; łańcuch kluczy: `apitennis_events` → `apitennis_tournaments` → `apitennis_fixtures`), `wta_tournament_matches`.
- **E-sport:** `pandascore_matches` z `status=upcoming` (wymaga `PANDASCORE_TOKEN`; slugi: `csgo` dla CS2, `lol`, `dota2`; potwierdź przez `pandascore_videogames`).
- Pusta lista `events: []` to brak meczów, nie błąd. Jeśli narzędzie zwraca błąd klucza, przejdź na kolejne źródło, nie powtarzaj w pętli.

## Krok 1: Ustal zakres

- **Okres:** przelicz "dziś/jutro/weekend" na konkretne daty (sprawdź dzisiejszą datę w kontekście). Zakres dłuższy niż ~7 dni zawęż do najważniejszych rozgrywek albo zapytaj, jak go zawęzić.
- **Dyscypliny:** domyślnie wszystkie trzy; jeśli użytkownik wskazał jedną lub ligę/turniej, ogranicz się do tego.
- **Strefa czasowa:** podawaj godziny w czasie polskim (CET/CEST) i zaznacz to w nagłówku.
- **Ranga:** jeśli nie podano, dobierz sensowny zakres - piłka: Top 5 lig, Ekstraklasa, puchary europejskie, reprezentacje/turnieje, krajowe puchary; tenis: ATP/WTA Tour (Challengery i ITF tylko na życzenie); e-sport: tier-1 turnieje CS2/LoL/Dota 2 (tier-2 na życzenie).

## Krok 2: Wyszukaj

Dla każdej dyscypliny użyj co najmniej dwóch niezależnych źródeł dla daty i godziny, gdy to możliwe:
- **Piłka nożna:** oficjalne strony lig i UEFA, Flashscore/Sofascore, FBref, BBC Sport.
- **Tenis:** oficjalne strony ATP/WTA i turnieju (order of play), Flashscore, Tennis Explorer. Order of play często publikowany jest dzień wcześniej - dla dalszych dni podaj tylko turniej i rundę, bez wymyślania par.
- **E-sport:** Liquipedia (kalendarz turnieju i drabinka), HLTV (CS2), strony organizatorów (ESL, BLAST, PGL, Riot), gol.gg/lolesports (LoL).

Zasady jakości:
- Mecz bez potwierdzonej daty to "do potwierdzenia", nie pewny termin.
- Sprawdź, czy mecz nie został przełożony lub odwołany.
- W tenisie pary wyłaniają się z drabinki w trakcie turnieju; nie podawaj meczów późniejszych rund jako znanych.
- Przy rozbieżności źródeł co do godziny podaj późniejszą źródłowo zweryfikowaną i zaznacz rozbieżność.

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
```

Na końcu podsumuj: liczbę meczów per dyscyplina, wskaż 3-5 najciekawszych (według rangi, wyrównania, stawki) i krótko zaznacz, czego nie udało się zweryfikować. Zapytaj, czy przekazać wybrane mecze do analizy (football-analyst, tennis-analyst, esports-analyst), ale nie rób analizy sam, jeśli użytkownik o to nie prosił.
