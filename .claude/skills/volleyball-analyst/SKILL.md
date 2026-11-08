---
name: volleyball-analyst
description: Analiza meczów siatkarskich (PlusLiga, TAURON Liga, Superlega, Serie A1, CEV Liga Mistrzów/Puchar CEV, Liga Narodów i mecze reprezentacji, kluby i kobiety) na podstawie czterech filarów - statystyk drużyn (bilans meczów i setów, atak, blok, zagrywka, przyjęcie, forma, dom/wyjazd), statystyk poprzednich spotkań (H2H, wyniki w setach), informacji medialnych z internetu (kontuzje, rozgrywający, zagraniczni zawodnicy, rotacja, zmęczenie po pięciosetowcach i pucharach, motywacja, powołania w kadrach) oraz kursów rynkowych - i wycena prawdopodobieństw (zwycięzca meczu, dokładny wynik w setach, handicap setowy, total setów) z fair odds. Używaj zawsze, gdy użytkownik prosi o analizę, typ, prognozę lub przegląd meczu/dnia siatkarskiego, pyta o szanse drużyny, formę, H2H, handicap setowy, value bet, kursy albo podaje same nazwy drużyn (Resovia, Zaksa, Jastrzębski, Skra, Perugia, Civitanova, Trentino...), ligi lub turnieju - nawet bez słowa "siatkówka".
---

# Analiza meczów siatkarskich

Cel: dla każdego meczu zebrać aktualne dane z czterech źródeł, przełożyć je na prawdopodobieństwo wygrania seta, a z niego policzyć rozkład meczu, i uczciwie pokazać niepewność. Siatkówka ma wysoką przewagę silniejszej drużyny w pojedynczym secie, ale mało zdarzeń punktowych na mecz (kilkadziesiąt akcji na set), więc o wyniku decydują zmiany składu, rozgrywający i forma dnia. Dane zawsze z researchu w sieci i MCP, nie z pamięci: składy, kontuzje i transfery zmieniają się co sezon i co kolejkę.

## Serwer MCP `sportsdata` i connector `superbet` (używaj w pierwszej kolejności)

Narzędzia `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch) to preferowane źródło danych; WebSearch/WebFetch uzupełniają to, czego nie ma (statystyki atak/blok/zagrywka, składy, kontuzje). Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload; błąd klucza = przejdź do następnego źródła.
- **Mecze, wyniki:** `apisports_volleyball_games` (wymaga `API_SPORTS_KEY` i co najmniej jednego parametru: `date` `YYYY-MM-DD`, `league` ID, `season` w formacie `2026-2027`, `team` ID; użyj do ostatnich wyników i H2H po ID drużyn).
- **Kursy:** connector `superbet-mcp` (`superbet_events` z `sport_id` 1, `superbet_event_odds`) jako główne źródło kursów Superbet; kursy innych bukmacherów i BettingPros tylko jako punkt odniesienia.
- Narzędzia `superbet_lineups`, `superbet_stats`, `superbet_h2h` **nie działają dla siatkówki** (API zwraca 404): składy, kontuzje i statystyki bierz z sieci (serwisy ligowe: plusliga.pl, tauronliga.pl, legavolley.it, cev.eu, volleyballworld.com; Flashscore/Sofascore; strony i media klubowe).
- Duże odpowiedzi MCP czytaj przez `jq`, nie wczytuj w całości.

## BettingPros (skill `bettingpros-odds`)

Dla siatkówki BettingPros zwykle nie ma pokrycia: sprawdź `events --sport <X>` i jeśli nie zwraca meczów, pomiń to źródło i zaznacz to w raporcie (nie blokuj analizy). Gdy jest pokrycie, to kontrola i źródło kursów, nie zamiennik własnego p: różnica >10 pp względem rynku bez marży wymaga wyjaśnienia (skład, kontuzje).

## Krok 1: Zbierz dane (cztery filary)

1. **Statystyki drużyn** - tabela i bilans meczów i setów w sezonie, ostatnie 5-8 meczów z przeciwnikami (nie tylko W/L, ale i wyniki w setach: 3:0 a 3:2 to różne sygnały), punkty zdobyte/stracone na set, skuteczność ataku, bloki i asy serwisowe na set, błędy własne w zagrywce, jakość przyjęcia, forma u siebie i na wyjeździe. Forma bez kontekstu przeciwników wprowadza w błąd: zapisz, z kim grali.
2. **Poprzednie spotkania (H2H)** - ostatnie 3-5 bezpośrednich meczów z wynikami w setach, ale tylko z ostatnich ~2-3 lat i przy podobnych składach (rozgrywający, zagraniczni zawodnicy). Starsze H2H waż nisko; siatkarskie składy zmieniają się co sezon.
3. **Informacje medialne** - kontuzje i niedyspozycje (szczególnie **rozgrywającego**, atakującego i libero), zagraniczni zawodnicy i limity kontyngentu, zmiana trenera, zmęczenie (pięciosetowce, mecze europejskie w środku tygodnia, podróże), rotacja przy meczach bez stawki (koniec fazy zasadniczej, ustalone rozstawienie), motywacja (walka o play-offy, o utrzymanie, o finał). W kadrach: lista powołanych, kto odpoczywa, stawka turnieju (towarzyski, VNL, kwalifikacje), mecze w krótkich odstępach. Plotki oznaczaj jako niepotwierdzone.
4. **Rynek** - kursy Superbet (i inne jako odniesienie); po usunięciu marży to niezależny punkt odniesienia. Gdy Twoja liczba różni się o >10 pp, najpierw szukaj, czego nie wiesz (skład, kontuzja), zanim uznasz to za value.

Jeśli kluczowych danych nie da się znaleźć (a w siatkówce częste są braki statystyk poza top ligami), napisz to wprost i obniż pewność zamiast wypełniać luki domysłami. Podawaj źródło przy każdym kluczowym fakcie.

## Krok 2: Policz

Wyznacz prawdopodobieństwo wygrania pojedynczego seta przez drużynę A. Punktem wyjścia jest rynek: weź P(A wygra mecz) z kursów bez marży i odwróć je na p seta skryptem, a potem koryguj własnymi danymi z filaru 3 (patrz "Skalibruj"):

```bash
python scripts/volleyball_model.py --from-match <P_meczu_A> --bo 3|5
python scripts/volleyball_model.py <p_seta> [p_seta2 ...] [--bo 3|5] [--p-decider P]
```

Jedna wartość = ta sama p w każdym secie; lista = p dla kolejnych setów; `--p-decider` pozwala wycenić set decydujący osobno (zwykle bliżej 50%). Skrypt zwraca P(zwycięstwo meczu), dokładny wynik w setach, handicap setowy (±1.5, a w bo5 także ±2.5) i total setów Over/Under, z fair odds. Format: do 2 wygranych setów (bo3) w części lig kobiecych i niższych klasach, do 3 wygranych setów (bo5) w PlusLidze, Superlidze, Serie A1, TAURON Lidze, CEV i większości turniejów kadrowych; sprawdź format w konkretnych rozgrywkach.

Skrypt nie wycenia punktów w secie, total punktów ani rynków zawodnika: takich typów **nie rekomenduj** (brak modelu i danych), chyba że masz dwa niezależne źródła liczb i podasz niską pewność.

## Krok 3: Skalibruj

Skill jest nowy i **nie ma jeszcze zweryfikowanych typów**, więc poniższe zasady wynikają z ogólnych reguł pozostałych skilli i z natury siatkówki; po pierwszej weryfikacji dopisz tu konkretne lekcje (zachowując uzasadnienia).

- **Każdy sygnał ryzyka musi zmienić liczbę**, nie tylko opis. Wcześniej najczęstszym błędem w analizach sportowych było odnotowanie sygnału w tekście bez przełożenia na prawdopodobieństwo.
- **Rozgrywający to klucz.** Brak lub kontuzja podstawowego rozgrywającego albo jego pierwszy mecz po urazie obniża p seta drużyny o kilka pp i podnosi niepewność; oznacz niską pewność. To zwykle ważniejsze niż pozycja w tabeli.
- **Nie schodź pod rynek o >5 pp bez konkretnej informacji** (kontuzja kluczowego gracza, rotacja, niepewny rozgrywający). Forma z kilku ostatnich meczów jest już w kursie.
- **Set decydujący to loteria:** nie przenoś p z pierwszych setów wprost; użyj `--p-decider` bliżej 50% (np. ściągnij różnicę od 50% o ok. jedną trzecią), zwłaszcza gdy drużyny są wyrównane. To heurystyka, nie zweryfikowana reguła: oznacz ją w raporcie.
- **Duża przepaść klas** wydłuża serię faworyta do 3:0 (mniej setów, Under setów), ale pojedynczy set bywa wygrywany przez słabszą drużynę serią zagrywek; nie wyceniaj 3:0 powyżej tego, co daje model.
- **Mecze bez stawki i po pucharach:** zmęczenie po pięciu setach lub podróży z pucharu europejskiego w środku tygodnia oraz rotacja na koniec fazy zasadniczej obniżają p faworyta o kilka pp.
- **Reprezentacje i VNL:** składy rotują, a statystyki klubowe nie przekładają się wprost; obniż pewność o jeden poziom i sprawdź listę powołanych oraz stawkę turnieju. Łączne korekty kadrowe w dół nie więcej niż ok. 15%.
- **Wyrównane mecze** (blisko 50%) oznacz jako "brak mocnego typu" - to uczciwa informacja, nie porażka analizy.
- **Pewność "wysoka" tylko** przy potwierdzonych składach (kontuzje i rozgrywający znani), dwóch zgodnych źródłach statystyk i różnicy do rynku do ~5 pp. Brak statystyk spoza wyników (częsty w niższych ligach) lub niepotwierdzony skład = pewność niska.

## Krok 4: Raport

Po polsku, zwięźle, dla każdego meczu:

```
### Drużyna A - Drużyna B (liga/turniej, kolejka, format boX, data, godzina)
**Typ:** <rynek> | **Prawdopodobieństwo:** XX% | **Fair odds:** X.XX | **Pewność:** niska/średnia/wysoka
**Rynki dodatkowe:** tabela wycenionych rynków (zwycięzca, dokładny wynik, handicap setowy ±1.5/±2.5, total setów): p, fair, pewność, kurs Superbet
**Statystyki drużyn:** bilans meczów i setów, forma, atak/blok/zagrywka z liczbami
**H2H:** 1-2 zdania
**Informacje medialne:** kontuzje, rozgrywający, rotacja, kontekst (ze źródłem)
**Ryzyka:** scenariusze, w których typ przegrywa (kontuzja rozgrywającego, set decydujący)
**Rynek:** kurs vs fair odds (jeśli znany); p seta użyte w modelu i skąd
```

Przy przeglądzie dnia dodaj ranking top-N **ze wszystkich rynków** (zwycięzca, handicap setowy, total setów, dokładny wynik). W rankingu pomijaj typy z fair odds ≤ 1.15 (po marży bukmachera bez wartości); jeśli najlepszy typ meczu odpada, sprawdź inny rynek tego samego meczu (np. handicap setowy zamiast zwycięzcy). Przypadki 1.15-1.20 oznacz jako graniczne. Pod rankingiem daj "tabelę kandydatów na kupon": mecz, rynek, p, fair, pewność, od czego zależy (skład, rozgrywający) i czy kurs rynkowy jest znany, żeby `bet-slip-builder` miał gotowe wejście. Na końcu jedno zdanie: to oszacowania, nie gwarancje.
