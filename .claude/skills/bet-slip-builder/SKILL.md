---
name: bet-slip-builder
description: Na podstawie gotowych analiz z football-analyst, tennis-analyst, esports-analyst, mma-analyst, nba-analyst i nhl-analyst oraz kursów bukmacherskich wybiera najbardziej prawdopodobne typy i składa z nich zestawy (kupony) kilku predykcji, w których typy się nie wykluczają i nie są wzajemnie sprzeczne. Liczy łączne prawdopodobieństwo, fair odds, kurs rynkowy i wartość oczekiwaną każdego zestawu. Używaj zawsze, gdy użytkownik prosi o kupon, zestaw typów, akumulator, "złóż typy z tych analiz", "wybierz najpewniejsze i połącz", TOP typów z kursami albo podsumowanie kilku analiz meczów w gotowe zestawy - także gdy nie pada słowo "kupon". Ten skill nie analizuje meczów od zera; jeśli brakuje analiz, najpierw uruchom odpowiednie skille analityczne.
---

# Składanie zestawów typów

Cel: z analiz meczów wybrać typy o największym prawdopodobieństwie, zestawić je z kursami i ułożyć w kilka zestawów, które można sensownie zagrać razem. Najpierw zadbaj o dane wejściowe, potem selekcję, potem zestawy.

## Serwer MCP `sportsdata` (kursy)

Kursy pobieraj w pierwszej kolejności z narzędzi `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch), a dopiero potem z WebSearch. Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation. Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload.
- `pinnacle_sport_matchups_all`/`pinnacle_league_matchups` → `pinnacle_matchup_markets` (bez klucza; tylko `hasMarkets: true`; kursy amerykańskie, przelicz na dziesiętne), `theoddsapi_odds` (`THE_ODDS_API_KEY`; rynki `h2h`, `totals`, `spreads`; kosztuje kredyty), `oddsapiio_odds`, `apisports_football_odds`, `unibet_kambi_call`, `pandascore_match_odds` (e-sport); NBA/NHL: `nba_odds_today`, Pinnacle (koszykówka, hokej; potwierdź `sportId` przez `pinnacle_sports`) i `theoddsapi_odds` (`basketball_nba`, `icehockey_nhl`; `h2h`, `spreads`, `totals`; rynki zawodnika osobno i drożej); MMA: Pinnacle (zwycięzca, często total rund) oraz `apisports_mma_fights`/`theoddsapi_odds` (`mma_mixed_martial_arts`), rynki sposobu wygranej zwykle trzeba wziąć ze stron bukmacherów lub od użytkownika.
- To są kursy zagraniczne (Pinnacle jest ostrzejszy od krajowych bukmacherów), więc kurs kuponu u polskiego bukmachera będzie zwykle niższy. Zaznacz w raporcie, z którego źródła pochodzi kurs, i nie podawaj go jako kursu krajowego bukmachera. Nigdy nie wpisuj kursu z pamięci.

## Krok 1: Zbierz wejście

Potrzebujesz dla każdego kandydata: mecz, rynek, **własne prawdopodobieństwo** (z analizy), fair odds, pewność. Rozważ **wszystkie rynki** z analiz, nie tylko wynik meczu: gole Over/Under, BTTS, podwójną szansę, rożne, kartki, faule meczowe i rynki zawodnika (faule, kartki, strzały), a w tenisie/e-sporcie odpowiednio total gemów/map, handicap, wynik setowy, a w MMA zwycięzcę walki, sposób wygranej (KO/TKO, submission, punkty), walkę na dystans oraz Over/Under rund, w NBA zwycięzcę, spread, total punktów, total drużyny i rynki zawodnika (punkty, zbiórki, asysty, trójki, PRA), a w NHL moneyline, wynik po 60 minutach, puck line ±1.5, total goli i rynki zawodnika (strzały, punkty, strzelec gola, obrony bramkarza). Źródło: raporty `football-analyst`, `tennis-analyst`, `esports-analyst`, `mma-analyst`, `nba-analyst`, `nhl-analyst` z tej rozmowy lub pliki w `analizy/`. Jeśli analiz brakuje dla meczów, które użytkownik chce uwzględnić, uruchom odpowiedni skill analityczny - nie wymyślaj prawdopodobieństw.

Kursy (kolejność źródeł, od 20.10.2026): 1) **https://www.betclic.pl/** jako źródło główne; 2) **https://gg397.bet/pl** do weryfikacji/potwierdzenia kursu z Betclic (kurs z Betclic liczy się w EV; jeśli na gg397.bet kurs tej samej selekcji różni się o więcej niż 0,10 lub nogi nie ma na Betclic, zaznacz rozbieżność, a w drugim przypadku użyj kursu z gg397.bet z jawnym oznaczeniem źródła); 3) dopiero gdy żadna z tych stron nie ma rynku: `mcp__sportsdata__*`, WebSearch lub kursy od użytkownika, także z jawnym oznaczeniem źródła. Strony czytaj przez MCP przeglądarki (`mcp__claude-in-chrome__*`). Zapytanie użytkownika z własnymi kursami ma pierwszeństwo. Bez kursu typ nadal może wejść do zestawu, ale oznacz go "kurs nieznany" i nie licz dla niego wartości oczekiwanej. Nigdy nie wpisuj kursu z pamięci.

Dostępność kursów zależy od rynku: ESPN scoreboard (DraftKings) daje tylko 1X2 i główny total goli. Rynki rożnych, kartek, fauli, BTTS i rynki zawodnika wymagają innego źródła (Pinnacle/The Odds API/oddsapi.io przez `mcp__sportsdata__*`, strony bukmacherów, WebSearch) albo kursów od użytkownika. Kursy podwójnej szansy, które wyliczasz z moneyline, oznacz jako przybliżone. Typ z rynku dodatkowego bez znanego kursu nie wchodzi do zestawu jako noga z "kursem"; pokaż go z fair odds i prośbą o kurs, żeby kurs zestawu (np. >1.6) nie był zgadywany.

## Krok 2: Wyceń każdy typ

Dla typu z prawdopodobieństwem p i kursem rynkowym k policz:
- fair odds = 1/p,
- wartość oczekiwaną EV = p·k − 1,
- prawdopodobieństwo implikowane przez rynek 1/k (bez marży rynek bywa trafniejszy, gdy Twoje p różni się o >10 pp - wtedy obniż pewność).

Odrzuć kandydatów:
- z fair odds ≤ 1.15 (zbyt krótkie, po marży bukmachera bez wartości),
- z EV wyraźnie ujemnym (k < fair odds), chyba że to jedyna "bezpieczna" noga zestawu zachowawczego i jawnie to zaznaczysz,
- z niską pewnością z analizy (np. brak statystyk, stand-in, powrót po kontuzji), gdy da się je zastąpić pewniejszym.

**Domyślne progi kuponu** (stosuj, jeśli użytkownik nie podał innych w danym zapytaniu): kurs nogi > 1.2 wymagany tylko dla co najmniej dwóch nóg w kuponie (pozostałe nogi mogą mieć kurs ≤ 1.2, ale z fair odds > 1.15), łączny kurs zestawu > 1.5 i < 2.5 (zmiana z 20.10.2026, wcześniej < 2.0), EV > 0, własne p > 50% (łączne p kuponu i p każdej nogi). Noga, która nie spełnia pozostałych warunków, nie wchodzi do zestawu; dodatkowe krótkie nogi obniżają łączne p, więc sprawdź, czy kupon nadal ma p > 50%. Jeśli przy progach bazowych nie powstaje żądana liczba zestawów (typowe przy marży 5-9%, bo EV>0 przy p>50% wymaga realnej przewagi nad rynkiem, nie tylko zgodności z nim), zastosuj poniższe poziomy luzowania zamiast fabrykować typ, który formalnie spełnia progi.

**Poziomy luzowania progów** (od 20.10.2026; stosuj po kolei, każdy poziom dodaje się do poprzednich, i zatrzymaj się na najniższym, który daje żądaną liczbę zestawów):

| Poziom | Co luzujesz | Nowy próg | Stawka |
|---|---|---|---|
| 0 | Bazowe | EV > 0, p > 50%, kurs zestawu 1.5-2.5, 2 nogi > 1.2 | Kelly 1/4-1/2 |
| 1 | EV | EV ≥ -5% (tylko marża); ranking po EV, przy remisie po p | 0% |
| 2 | EV | bez limitu EV; ranking malejąco po p | 0% |
| 3 | p zestawu | p > 45%, nogi pojedyncze nadal z p ≥ 55% | 0% |
| 4 | kurs nogi | > 1.2 tylko dla jednej nogi (zamiast dwóch); sprawdź, czy krótka noga nie zbija p | 0% |
| 5 | dolny kurs zestawu | > 1.4 (zamiast 1.5) | 0% |
| 6 | powtórzenia | ten sam mecz w 2 zestawach, tylko z różnych rodzin rynków (nigdy dwie nogi z rynku wyniku) | 0% |

- **Poziomy 0-2 stosuj automatycznie**, po kolei i tylko do najniższego poziomu, który daje żądaną liczbę zestawów. **Poziomy 3-6 tylko za zgodą użytkownika** (decyzja z 22.10.2026, wcześniej 20.10 wszystkie były automatyczne): gdy poziomy 0-2 nie dają żądanej liczby zestawów, zatrzymaj się, pokaż co powstało, powiedz ile zestawów dałby poziom 3 (i kolejne) i zapytaj, czy luzować dalej. Poziomy 3-6 obniżają jakość (w weryfikacji 07.10 pozycje z p 55-66% przegrywały często); po zgodzie oznaczaj je wyraźnie jako "poniżej progów" z podanym poziomem.
- Przy każdym zestawie podaj poziom luzowania i które progi złamano. Zestawy poniżej progów pokaż osobno, pod bazowymi.
- Kupon z EV ≤ 0 ma stawkę 0%.
- Przy p > 50% i EV ≤ 0 górna granica kursu 2.5 i tak nie działa (kurs wychodzi < 2.0); faktycznie ogranicza dolna granica 1.5.
- **Nie luzuj nigdy:** fair odds nogi > 1.15, brak sprzeczności i powtórzeń tej samej nogi, kurs musi pochodzić z Betclic, gg397.bet lub jawnie oznaczonego fallbacku (nigdy z pamięci), noga z niską pewnością tylko w zestawie ryzykownym, "przewaga niepotwierdzona" nie podnosi EV.
- Jeśli i poziom 6 nie wystarcza, pokaż, ile zestawów jest, i nie dobijaj na siłę.

Dodatkowo (weryfikacja 07-08.10.2026, pudła Norrie/Griekspoor/Simakin/Munar):
- **EV dodatnie, które bierze się tylko z p wyższego od rynku o >5 pp, bez twardej informacji w analizie, to podejrzenie błędu, nie value.** Oznacz taki typ "przewaga niepotwierdzona" i nie ufaj jego EV (Kupon 1 z EV +4,9% przegrał przez takiego faworyta).
- **Nie dobijaj TOP-N na siłę.** Jeśli typów z p ≥ 70% i twardymi danymi jest mniej niż N, pokaż mniej pozycji. W TOP 10 z 07.10 pozycje 6-10 miały p 55-66% i 3 z 5 przegrały.
- **Tenisowe nogi z p < 70% w R1 turnieju lub z kwalifikantem po drugiej stronie** nie wchodzą do zestawu zachowawczego ani zrównoważonego (tylko do oznaczonego jako ryzykowny).

Jeśli najlepszy typ meczu odpada, sprawdź inny rynek tego samego meczu (np. handicap zamiast zwycięzcy, Under goli, rożne, kartki), tylko pod warunkiem, że ma sensowny kurs. Nie ograniczaj się do wyniku: w kolejce 9-12.10.2026 wszystkie 5 kuponów powstało z samych wyników 1X2/podwójnej szansy, co wynikało z braku wyceny innych rynków, a nie z ich braku wartości.

## Krok 3: Zasady spójności (typy nie mogą się wykluczać)

Zestaw jest poprawny tylko wtedy, gdy spełnia wszystkie warunki:
1. **Jeden typ na mecz w obrębie zestawu.** To najprostszy sposób, żeby typy się nie wykluczały i nie były silnie skorelowane (bukmacherzy zwykle i tak nie przyjmują kombinacji z jednego meczu w akumulatorze).
1a. **Żadna predykcja nie powtarza się w kilku kuponach.** Przy składaniu kilku zestawów naraz (np. "5 kuponów") każda noga (mecz + rynek + wybór, np. "Deportivo Over 1.5") trafia do dokładnie jednego kuponu, więc zestawy nie dzielą ryzyka jednej nogi i nie padają razem przez jeden wynik. Potrzebujesz więc co najmniej (liczba kuponów × liczba nóg) różnych nóg; gdy nie starcza kandydatów spełniających progi, zmniejsz liczbę kuponów albo nóg i powiedz to wprost, zamiast powtarzać nogę. Ten sam mecz z innym rynkiem w innym kuponie dopuszczaj tylko wtedy, gdy brakuje innych meczów, i sprawdź sprzeczności (reguła 2). Ten sam mecz w różnych kuponach tylko z nogami z różnych rodzin rynków (wynik / gole / BTTS), nigdy dwie nogi z rynku wyniku (np. 1X w jednym kuponie i 12 w drugim to przeciwne pokrycie remisu). Wymaganie użytkownika z 16.10.2026.
2. **Brak sprzeczności logicznych**, jeśli ten sam mecz jednak występuje w kilku zestawach z różnymi rynkami - sprawdź, czy typy mogą być jednocześnie prawdziwe. Przykłady sprzeczności: zwycięzca A + zwycięzca B; Over 2.5 + wynik 1-0; BTTS tak + wynik 2-0; handicap A −1.5 + wygrana B; Under 2.5 + Over 3.5; wynik serii 2-0 + total map Over 2.5; MMA: walka na dystans + wygrana przez KO/TKO/submission, Under rund + walka na dystans, zwycięzca A + sposób wygranej B; NBA: zwycięzca A + spread B +1.5 wyłączający wygraną A, Under totalu + Over punktów zawodnika wymagający wysokiego wyniku drużyny; NHL: gospodarze wygrywają po 60' + wygrana gości w dogrywce, puck line gospodarzy −1.5 + wygrana gości.
3. **Różnorodność:** nie buduj zestawu z samych typów od jednego czynnika (np. pięciu faworytów, którzy wszyscy "wygrają, bo są lepsi") - jedna niespodzianka niszczy wszystko. Rozdziel typy między ligi, dyscypliny i **rynki**. Przy kilku zestawach z jednego dnia (np. "5 kuponów") nie rób wszystkich kuponów samymi wynikami 1X2/podwójną szansą: wymieszaj rynki (wynik, gole O/U, BTTS, rożne, kartki, faule, rynki zawodnika), o ile analiza ma dla nich p i pewność co najmniej średnią. Kupon w całości z jednego rynku wyjaśnij tylko wtedy, gdy innych typów o sensownej pewności brak.
3a. **Typy niezależne od siebie w obrębie kuponu:** rynki powiązane z tym samym czynnikiem (np. Over goli + rożne tych samych drużyn, kartki + faule w tym samym meczu, kartka zawodnika + kartki meczowe Over) liczy się jako skorelowane; dlatego jeden mecz = jedna noga (reguła 1). Jeśli dwa kupony zawierają ten sam mecz z różnymi rynkami, sprawdź sprzeczności (np. Under 2.5 gola + BTTS tak + wygrana 3-0 itd.).
3b. **Rynki o dużej wariancji** (rożne, kartki, faule, zawodnik) wchodzą do zestawu zachowawczego tylko przy pewności średniej lub wysokiej i znanym sędzim/składzie; typ zawodnika wchodzi tylko po potwierdzeniu składu (zwykle ~1 h przed meczem), więc pokaż go z adnotacją "po składach".
3c. **MMA:** walka może odpaść lub zmienić rywala do dnia gali (kontuzja, ścięcie wagi, zastępstwo z krótkim wyprzedzeniem), więc nogę z walki oznacz "po ważeniu", a przy zastępstwie lub niepotwierdzonej karcie nie dawaj jej do zestawu zachowawczego. Rynki sposobu wygranej i Over/Under rund mają pewność co najwyżej średnią (zgodnie z `mma-analyst`) i nie wchodzą do zestawu zachowawczego. Walki z jednej gali nie są w pełni niezależne tylko wtedy, gdy dotyczą tego samego zawodnika lub kolejności karty; zwykle traktuj je jak osobne mecze.
3d. **NBA/NHL:** mecze zaczynają się w Polsce w nocy, więc przy każdej nodze podaj godzinę czasu polskiego i datę lokalną USA. Noga zawodnika (NBA: punkty/zbiórki/asysty; NHL: strzały/punkty/strzelec gola) wchodzi tylko po potwierdzeniu składu i statusu (injury report NBA, skład NHL), a typ zależny od bramkarza NHL (zwycięzca, total, obrony) tylko po potwierdzeniu startującego, inaczej oznacz "po bramkarzu" i nie dawaj do zestawu zachowawczego. W NHL **pilnuj rozliczenia:** moneyline i total liczą dogrywkę (karne nie liczą się do totalu), wynik 3-way i "po 60 minutach" nie; nie mieszaj p z jednego rynku z kursem z drugiego. W NBA rynki zawodnika przy spreadzie ≥ 10 punktów mają ryzyko blowoutu (mniej minut), więc nie wchodzą do zestawu zachowawczego. Mecze z jednego wieczoru NBA/NHL traktuj jak niezależne, ale kilka rynków jednego zawodnika lub drużyny jest skorelowanych (reguła 1).
4. **Mecze niezależne w czasie i stawce:** unikaj meczów, których wynik wpływa na siebie (ten sam turniej, ta sama drabinka, ostatnia kolejka grupy ze wspólnym awansem).
5. **Typy z flagą "niska pewność" lub "brak mocnego typu"** nie wchodzą do zestawów, poza wyraźnie oznaczonym zestawem ryzykownym.

## Krok 4: Złóż zestawy

Domyślnie trzy zestawy (zmień, jeśli użytkownik poprosi inaczej), każdy po 2-5 typów:
- **Zachowawczy:** 2-3 typy o najwyższym p (łączne p zwykle >50%).
- **Zrównoważony:** 3-4 typy, mieszanka dyscyplin, łączny kurs w sensownym przedziale.
- **Ryzykowny:** 4-5 typów albo wyższe kursy, wyraźnie oznaczony jako większa niepewność.

Im więcej nóg, tym niższe łączne p; pokaż to wprost. Policz zestaw skryptem:

```bash
python scripts/slip.py "Arsenal-Chelsea 1" 0.62 1.85 "Sinner-Alcaraz Sinner" 0.58 1.70 ...
```

Argumenty to trójki: opis, p, kurs rynkowy (kurs 0 lub "-" = nieznany). Skrypt zwraca łączne p (zakładając niezależność meczów), fair odds zestawu, łączny kurs rynkowy i EV, a ostrzega, gdy któraś noga ma fair odds ≤ 1.15 albo EV < 0.

## Krok 5: Raport

Po polsku, zwięźle:

```
## Zestaw 1 - Zachowawczy
| Mecz | Typ | p | Kurs | Fair | EV | Pewność |
Łączne p: XX% | Fair odds: X.XX | Łączny kurs: X.XX | EV: +X%
Stawka: X% bankrolla (ułamek Kelly'ego)
Ryzyko: który element jest najsłabszy i co go zabija
```

**Zawsze podawaj przy każdym zestawie:** EV, łączne p i proponowaną wielkość stawki jako % bankrolla. Stawkę licz ułamkiem Kelly'ego dla całego zestawu: f = (p·kurs − 1)/(kurs − 1), i rekomenduj 1/4 do 1/2 tej wartości (pełne Kelly jest zbyt agresywne przy niepewnym p) - zaznacz, że to sugestia wielkości stawki, nie porada finansowa, i że przy EV ≤ 0 nie proponujesz stawki (0%).

Pod zestawami dodaj krótkie zastrzeżenia: założenie niezależności meczów, to że kursy mogą się zmienić do czasu postawienia, oraz że to oszacowania probabilistyczne, nie gwarancje. Jeśli żaden zestaw nie ma dodatniego EV, powiedz to wprost zamiast na siłę rekomendować - brak wartości to uczciwy wynik.

**Gdy wszystkie zestawy mają EV ≤ 0** (typowe, gdy własne p to p rynku po devigu): nie dobieraj zestawów pod najmniejszą stratę, tylko pod **najwyższe łączne p** przy zachowaniu pozostałych progów (kurs nogi, kurs zestawu, brak powtórzeń nóg z reguły 1a). Kupony ułóż malejąco według p, a przy każdym i tak podaj EV i stawkę 0%. Wymaganie użytkownika z 16.10.2026.
