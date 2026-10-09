---
name: tennis-analyst
description: Analiza meczów tenisowych ATP/WTA na podstawie czterech filarów - statystyk zawodników (ranking, forma, serwis i return na danej nawierzchni), statystyk poprzednich spotkań (H2H, także na tej nawierzchni), informacji medialnych z internetu (kontuzje, zmęczenie, długość ostatnich meczów, przerwy, zapowiedzi, warunki) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca meczu, wynik setowy, zwycięzca seta, total gemów, handicap gemowy) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/dnia turniejowego w tenisie, pyta o szanse zawodnika, formę, H2H, value bet, kursy albo podaje same nazwiska, turniej lub datę - nawet bez słowa "tenis".
---

# Analiza meczów tenisowych

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, przełożyć je na prawdopodobieństwo i uczciwie pokazać niepewność. Tenis jest wrażliwy na świeże informacje (kontuzja, choroba, zmęczenie po maratonie), więc zawsze zaczynaj od researchu (WebSearch/WebFetch), a nie od rankingu z pamięci.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (kontuzje, czas trwania meczów, zapowiedzi). Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation (APITennis.md, WTA.md, Pinnacle.md, TheOddsAPI.md). Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Zawodnicy, ranking, H2H, nawierzchnia:** `apitennis_standings` (rankingi ATP/WTA, daje `player_key`), `apitennis_players` (profil i bilans per nawierzchnia), `apitennis_h2h` (H2H + forma obu), `apitennis_fixtures` (wyniki setowe z poprzednich rund); wymaga `API_TENNIS_KEY`, limit 2 zapytania/s. WTA: `wta_rankings`, `wta_player_matches`, `wta_tournament_matches`.
- **Kursy (filar 4):** `theoddsapi_odds` (`THE_ODDS_API_KEY`, `h2h`; klucze sportów z darmowego `theoddsapi_sports`), `pinnacle_sports` sprawdź, czy oferuje tenis, potem `pinnacle_league_matchups` i `pinnacle_matchup_markets` (kursy amerykańskie, przelicz na dziesiętne).
- MCP nie dostarcza gotowego % punktów przy serwisie ani informacji o kontuzjach: te nadal ustalaj w sieci (Tennis Abstract, ATP/WTA, osobne zapytanie o kontuzję każdego zawodnika). Duże odpowiedzi czytaj przez `jq`.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki zawodników** - ranking, bilans sezonu i ostatnich 5-10 meczów (z kim), bilans na danej nawierzchni, a przede wszystkim statystyki sezonu: % punktów wygranych przy własnym serwisie, % utrzymanych gemów serwisowych (SGW), % punktów przy returnie (RPW), asy, break pointy. Konkretne statystyki sezonu są dużo lepsze niż sam ranking.
2. **Poprzednie spotkania (H2H)** - bilans i przebieg (wyniki setowe, nawierzchnia, kiedy). H2H sprzed kilku lat albo z innej nawierzchni waż nisko.
3. **Informacje medialne** - dla KAŻDEGO zawodnika wykonaj osobne zapytanie "[nazwisko] injury / kontuzja [rok]" (ogólne szukanie formy tego nie wyłapuje); do tego: czas trwania meczów w poprzednich rundach, dni odpoczynku, przerwa w grach, zmiana trenera, wywiady, warunki (kryty/otwarty kort, upał, wiatr, szybkość kortu). Plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - kursy bukmacherów, jeśli dostępne; po usunięciu marży to niezależny punkt odniesienia. Gdy Twoja liczba różni się o >10 pp, najpierw szukaj, czego nie wiesz.

Jeśli brakuje kluczowych danych, napisz to i obniż pewność. Przy każdym kluczowym fakcie podaj źródło.

## Krok 2: Policz

Ustal dla każdego zawodnika p_serve (prawdopodobieństwo wygrania punktu przy własnym serwisie) z jego statystyk sezonu, skorygowane o jakość przeciwnika (serwis A vs return B), nawierzchnię i formę. Potem:

```bash
python scripts/tennis_model.py <p_serve_A> <p_serve_B> [--bo 3|5] [--tiebreak 7|10]
```

Skrypt zwraca P(zwycięstwo meczu), rozkład wyniku setowego, P(zwycięstwo seta 1), oczekiwany total gemów z rozkładem Over/Under w kilku liniach, i fair odds. Jeśli p_serve nie ma z czego wyliczyć (brak statystyk, tylko ranking), oznacz je jako oszacowane - patrz zasady niżej.

## Krok 3: Skalibruj (lekcje z weryfikacji poprzednich typów)

Model punkt→gem→set→mecz był dobrze skalibrowany (np. 8/9 przy średniej pewności ~88%), ale pudła miały powtarzalne wzorce. Każdy sygnał ryzyka musi zmienić liczbę, nie tylko tekst - opisowa wzmianka bez wpływu na wynik była dotąd najczęstszym błędem.

- **Wiek 35+ w best-of-5** to niedoszacowane ryzyko ogonowe (choroba/uraz w trakcie meczu, którego nie widać przed). Odejmij 3-5 pp od p przy rankingu "najpewniejszych" albo nie stawiaj takiego meczu w czołówce.
- **Forma vs zmęczenie:** zawodnik po finale/półfinale w 2-3 ostatnich turniejach z rzędu przed Szlemem - rozważ obie hipotezy (rozpęd i zmęczenie), nie traktuj serii jako czystego plusa.
- **Faworyt po wolnym losie lub przerwie ≥2 tygodni** przeciw rywalowi z rytmem meczowym to realne ryzyko (faworytka 90% przegrała z nr 180). Zmęczenie underdoga po maratonie nie jest wystarczającym argumentem za faworytem.
- **Kryzys formy faworyta** (np. bilans 9-13) to ważny sygnał - nie ignoruj go dla rankingu.
- **WTA:** przy dokładnym wyniku setowym spłaszcz rozkład bardziej niż daje model; duża przepaść rankingowa nie gwarantuje "czystego" wyniku.
- **Powrót po długiej kontuzji:** wyraźnie obniż pewność i napisz o tym wprost.
- **p_serve oszacowane z rankingu (bez prawdziwych statystyk):** zwycięzca meczu wychodzi dobrze, ale total gemów myli się średnio o ~5 gemów - nie podawaj go jako pewnego typu ani nie wpisuj do rankingu top-N.
- **Kwalifikant po drugiej stronie** (weryfikacja Szanghaj R1, 07-08.10: Norrie 40. vs Svrcina 126., Griekspoor 58. vs Kotov 187. - oba pudła): kwalifikant ma za sobą 2 mecze na miejscu, aklimatyzację i rytm. Faworytowi spoza top 30 odejmij 4-6 pp od p, gdy przewaga rankingowa jest mniejsza niż ~100 miejsc albo H2H przemawia za kwalifikantem; przy obu naraz nie typuj go do rankingu.
- **Bilans z Challengerów nie liczy się jak bilans ATP:** zawodnik z wysokim win% na Challengerach (np. 45-17) przeciw rywalowi z touru nie jest faworytem tylko z tego powodu. Nie typuj niżej notowanego zawodnika powyżej ~55% bez statystyk serwisu/returnu z poziomu ATP; sama zła forma rywala nie wystarcza.
- **Krótki odpoczynek po półfinale/finale** (Munar: półfinał Tokio 5.10, mecz w Szanghaju 8.10 - pudło): jeśli zawodnik grał półfinał/finał ≤3 dni przed pierwszym meczem kolejnego turnieju (zwłaszcza po podróży), odejmij 3-5 pp i nie wpisuj go do TOP-N. Wzmianka "korekta w dół" bez zmiany liczby to ten sam błąd co wcześniej.
- **Nie uśredniaj mechanicznie model / zewnętrzne modele / rynek.** Gdy rozstęp między nimi wynosi >8 pp (Borges: model 57,5%, inne 73-76%), p jest niepewne - przyjmij dolną część rozstępu i oznacz pewność "niska", zamiast brać wartość pośrednią. Dotyczy to zwłaszcza p_serve z rankingu.
- **Przewaga nad rynkiem >5 pp bez twardej informacji** (kontuzja, stand-in, konkretna statystyka) to najpewniej własny błąd, nie value. Norrie 68% vs rynek 62-64% dawał EV +3% i przegrał.
- **R1 turnieju Masters/ATP: p ≥ 70% tylko przy przepaści potwierdzonej statystykami sezonu.** Typy 60-68% z R1 trafiły 4/8 - w TOP-N traktuj je jako "brak mocnego typu".
- Najlepsze trafienia: ekstremalna przepaść potwierdzona świeżymi statystykami sezonu (lider returnu/serwisu vs słabsza rywalka), nie samym rankingiem.

## Krok 4: Raport

Po polsku, zwięźle, dla każdego meczu:

```
### Zawodnik A - Zawodnik B (turniej, runda, nawierzchnia, data)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Statystyki zawodników:** serwis/return/forma z liczbami
**H2H:** 1-2 zdania
**Informacje medialne:** kontuzje, zmęczenie, odpoczynek, warunki (ze źródłem)
**Ryzyka:** scenariusze, w których typ przegrywa
**Rynek:** kurs vs fair odds (jeśli znany)
```

Przy przeglądzie dnia dodaj ranking top-N. W rankingu pomijaj typy z fair odds ≤ 1.15 (po marży bukmachera bez wartości); jeśli najlepszy typ meczu odpada, sprawdź inny rynek tego samego meczu. Przypadki 1.15-1.20 oznacz jako graniczne. Na końcu jedno zdanie: to oszacowania, nie gwarancje.
