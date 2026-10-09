---
name: esports-analyst
description: Analiza meczów e-sportowych (CS2, League of Legends, Dota 2) na podstawie czterech filarów - statystyk drużyn (forma, rankingi, win rate map/stron, map pool, meta patcha, draft), statystyk poprzednich spotkań (H2H, mapy), informacji medialnych z internetu (zmiany składów, stand-iny, podróże i LAN vs online, zapowiedzi, motywacja w turnieju) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca serii, dokładny wynik serii, handicap mapowy, total map, zwycięzca mapy, total rund w CS2) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/dnia turnieju e-sportowego, pyta o szanse drużyny, formę, H2H, handicap map, value bet, kursy albo podaje same nazwy drużyn (NAVI, Vitality, T1, Gen.G, Team Spirit...), turnieju lub gry - nawet bez słowa "esport".
---

# Analiza meczów e-sportowych

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, przełożyć je na prawdopodobieństwo i uczciwie pokazać niepewność. E-sport zmienia się szybciej niż inne dyscypliny (patch, transfer składu, stand-in), więc dane starsze niż kilka tygodni często są nieaktualne. Zawsze zaczynaj od researchu (WebSearch/WebFetch), nie z pamięci.

## Serwer MCP `sportsdata` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (map pool, win rate map, stand-iny, HLTV/Liquipedia/gol.gg). Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation (PandaScore.md, OpenDota.md). Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Mecze, składy, kursy:** `pandascore_matches` (`status=upcoming`; wymaga `PANDASCORE_TOKEN`; slugi `csgo` = CS2, `lol`, `dota2`, potwierdź przez `pandascore_videogames`), `pandascore_teams` (tylko składy, bez statystyk wydajności), `pandascore_match_odds` (po ID meczu).
- **Dota 2:** `opendota_pro_matches`, `opendota_teams`, `opendota_match`, `opendota_hero_stats` (statystyki herosów/patcha).
- MCP nie ma statystyk map ani draftów CS2/LoL: te bierz z sieci. Duże odpowiedzi czytaj przez `jq`.

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki drużyn** - ostatnie 10-15 serii/meczów z przeciwnikami (nie tylko W/L), ranking (HLTV, Oracle's Elixir/gol.gg, Liquipedia), forma na LAN vs online. Zależnie od gry:
   - **CS2:** win rate i bilans rund per mapa, picks/bans (map pool, kto banuje co), strona CT/T, rating graczy, pistol rounds.
   - **LoL:** win rate per strona (blue/red), czas gry, killi/mecz, kontrola obiektywów (smoki, Baron), meta patcha i priorytety draftu, champion pool kluczowych graczy.
   - **Dota 2:** win rate per patch, heroes/draft, tempo gry, killi i czas gry.
2. **Poprzednie spotkania (H2H)** - ostatnie bezpośrednie serie i wyniki map, ale tylko w obecnych składach i z ostatnich ~6-12 miesięcy. H2H sprzed zmiany składu waż nisko.
3. **Informacje medialne** - zmiany składów, stand-iny, kontuzje/choroby, problemy z wizami i podróżą, zmiana trenera/IGL, zapowiedzi i wywiady, motywacja (faza grupowa vs playoff, już zakwalifikowani), zmiany patcha, format serii (bo1/bo3/bo5), kolejność dnia (zmęczenie po długich seriach). Plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - kursy bukmacherów, jeśli dostępne; po usunięciu marży to niezależny punkt odniesienia. Gdy Twoja liczba różni się o >10 pp, najpierw szukaj, czego nie wiesz (np. nieznany stand-in).

Jeśli brakuje kluczowych danych, napisz to i obniż pewność. Przy kluczowych faktach podaj źródło.

## Krok 2: Policz

Wyznacz prawdopodobieństwo wygrania pojedynczej mapy/gry przez drużynę A. W CS2 rozpisz je per mapa (wynik veta: lista map w grze, które padną w bo3/bo5), w LoL/Dota 2 użyj p dla gry (w LoL uwzględnij stronę). Potem:

```bash
python scripts/series.py <p_mapa1> [p_mapa2 ...] [--bo 1|3|5]
```

Jedna wartość = ta sama p na każdą mapę; lista = p dla kolejnych map. Skrypt zwraca P(zwycięstwo serii), rozkład wyniku serii (2-0, 2-1...), handicap map ±1.5 i total map Over/Under, z fair odds. W CS2 total rund oszacuj osobno: średnia rund na mapę ~ 22-23 (MR12), więcej przy wyrównanych mapach i dogrywkach; to obszar o dużej niepewności - podawaj widełki.

## Krok 3: Skalibruj

- **Każdy sygnał ryzyka musi zmienić liczbę**, nie tylko tekst. Wcześniej najczęstszym błędem w analizach sportowych było odnotowanie sygnału w opisie bez przełożenia na prawdopodobieństwo.
- **Zmiany składów i stand-iny:** drużyna po transferze lub ze stand-inem ma mniej wiarygodną historię; ściągnij p w stronę 50% i oznacz niską pewność. To zwykle ważniejsze niż ranking.
- **Bo1 jest bardziej losowe niż bo3/bo5:** faworyt bo1 powinien mieć wyraźnie niższe p niż w serii; nie przenoś p z bo3 wprost.
- **Mapa wybrana przez przeciwnika** (jego pick, nasz ban) potrafi odwrócić p mapy o 10-20 pp - użyj p per mapa, nie jednej uśrednionej wartości.
- **Online vs LAN, długi dzień turnieju, podróż** to realne czynniki dla zespołów z historią słabszej formy w takich warunkach.
- **Duża przepaść w rankingu nie jest gwarancją** - ranking opóźnia się za formą i składem; waż ostatnie 1-2 miesiące mocniej.
- **Nie schodź pod rynek o >5 pp bez konkretnej informacji** (stand-in, kontuzja, zmiana IGL). Spirit (nr 1) po dwóch porażkach w Swiss dostał 78% przy rynku 85% i wygrał 2-0: seria dwóch porażek bez zmiany składu to szum, nie sygnał, który uzasadnia korektę o 7 pp.
- **Wyrównane serie** (blisko 50%) oznacz jako "brak mocnego typu".

## Krok 4: Raport

Po polsku, zwięźle, dla każdego meczu:

```
### Drużyna A - Drużyna B (turniej, faza, format boX, data)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Statystyki drużyn:** forma, map pool/meta/strony z liczbami
**H2H:** 1-2 zdania
**Informacje medialne:** składy, stand-iny, kontekst (ze źródłem)
**Ryzyka:** scenariusze, w których typ przegrywa
**Rynek:** kurs vs fair odds (jeśli znany)
```

Przy przeglądzie dnia turnieju dodaj ranking top-N. W rankingu pomijaj typy z fair odds ≤ 1.15 (po marży bukmachera bez wartości); jeśli najlepszy typ meczu odpada, sprawdź inny rynek tego samego meczu (np. handicap map). Przypadki 1.15-1.20 oznacz jako graniczne. Na końcu jedno zdanie: to oszacowania, nie gwarancje.
