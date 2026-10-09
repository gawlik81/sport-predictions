---
name: bet-slip-builder
description: Na podstawie gotowych analiz z football-analyst, tennis-analyst i esports-analyst oraz kursów bukmacherskich wybiera najbardziej prawdopodobne typy i składa z nich zestawy (kupony) kilku predykcji, w których typy się nie wykluczają i nie są wzajemnie sprzeczne. Liczy łączne prawdopodobieństwo, fair odds, kurs rynkowy i wartość oczekiwaną każdego zestawu. Używaj zawsze, gdy użytkownik prosi o kupon, zestaw typów, akumulator, "złóż typy z tych analiz", "wybierz najpewniejsze i połącz", TOP typów z kursami albo podsumowanie kilku analiz meczów w gotowe zestawy - także gdy nie pada słowo "kupon". Ten skill nie analizuje meczów od zera; jeśli brakuje analiz, najpierw uruchom odpowiednie skille analityczne.
---

# Składanie zestawów typów

Cel: z analiz meczów wybrać typy o największym prawdopodobieństwie, zestawić je z kursami i ułożyć w kilka zestawów, które można sensownie zagrać razem. Najpierw zadbaj o dane wejściowe, potem selekcję, potem zestawy.

## Serwer MCP `sportsdata` (kursy)

Kursy pobieraj w pierwszej kolejności z narzędzi `mcp__sportsdata__*` (deferred, załaduj przez ToolSearch), a dopiero potem z WebSearch. Dokumentacja dostawców: https://github.com/DanielTomaro13/sportsdata-mcp/tree/main/documentation. Kształty odpowiedzi części narzędzi są nieweryfikowane, więc sprawdzaj realny payload.
- `pinnacle_sport_matchups_all`/`pinnacle_league_matchups` → `pinnacle_matchup_markets` (bez klucza; tylko `hasMarkets: true`; kursy amerykańskie, przelicz na dziesiętne), `theoddsapi_odds` (`THE_ODDS_API_KEY`; rynki `h2h`, `totals`, `spreads`; kosztuje kredyty), `oddsapiio_odds`, `apisports_football_odds`, `unibet_kambi_call`, `pandascore_match_odds` (e-sport).
- To są kursy zagraniczne (Pinnacle jest ostrzejszy od krajowych bukmacherów), więc kurs kuponu u polskiego bukmachera będzie zwykle niższy. Zaznacz w raporcie, z którego źródła pochodzi kurs, i nie podawaj go jako kursu krajowego bukmachera. Nigdy nie wpisuj kursu z pamięci.

## Krok 1: Zbierz wejście

Potrzebujesz dla każdego kandydata: mecz, rynek, **własne prawdopodobieństwo** (z analizy), fair odds, pewność. Rozważ **wszystkie rynki** z analiz, nie tylko wynik meczu: gole Over/Under, BTTS, podwójną szansę, rożne, kartki, faule meczowe i rynki zawodnika (faule, kartki, strzały), a w tenisie/e-sporcie odpowiednio total gemów/map, handicap, wynik setowy. Źródło: raporty `football-analyst`, `tennis-analyst`, `esports-analyst` z tej rozmowy lub pliki w `analizy/`. Jeśli analiz brakuje dla meczów, które użytkownik chce uwzględnić, uruchom odpowiedni skill analityczny - nie wymyślaj prawdopodobieństw.

Kursy: poproś użytkownika o kursy bukmachera albo wyszukaj je w sieci (WebSearch). Bez kursu typ nadal może wejść do zestawu, ale oznacz go "kurs nieznany" i nie licz dla niego wartości oczekiwanej. Nigdy nie wpisuj kursu z pamięci.

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

Dodatkowo (weryfikacja 07-08.10.2026, pudła Norrie/Griekspoor/Simakin/Munar):
- **EV dodatnie, które bierze się tylko z p wyższego od rynku o >5 pp, bez twardej informacji w analizie, to podejrzenie błędu, nie value.** Oznacz taki typ "przewaga niepotwierdzona" i nie ufaj jego EV (Kupon 1 z EV +4,9% przegrał przez takiego faworyta).
- **Nie dobijaj TOP-N na siłę.** Jeśli typów z p ≥ 70% i twardymi danymi jest mniej niż N, pokaż mniej pozycji. W TOP 10 z 07.10 pozycje 6-10 miały p 55-66% i 3 z 5 przegrały.
- **Tenisowe nogi z p < 70% w R1 turnieju lub z kwalifikantem po drugiej stronie** nie wchodzą do zestawu zachowawczego ani zrównoważonego (tylko do oznaczonego jako ryzykowny).

Jeśli najlepszy typ meczu odpada, sprawdź inny rynek tego samego meczu (np. handicap zamiast zwycięzcy, Under goli, rożne, kartki), tylko pod warunkiem, że ma sensowny kurs. Nie ograniczaj się do wyniku: w kolejce 9-12.10.2026 wszystkie 5 kuponów powstało z samych wyników 1X2/podwójnej szansy, co wynikało z braku wyceny innych rynków, a nie z ich braku wartości.

## Krok 3: Zasady spójności (typy nie mogą się wykluczać)

Zestaw jest poprawny tylko wtedy, gdy spełnia wszystkie warunki:
1. **Jeden typ na mecz w obrębie zestawu.** To najprostszy sposób, żeby typy się nie wykluczały i nie były silnie skorelowane (bukmacherzy zwykle i tak nie przyjmują kombinacji z jednego meczu w akumulatorze).
2. **Brak sprzeczności logicznych**, jeśli ten sam mecz jednak występuje w kilku zestawach z różnymi rynkami - sprawdź, czy typy mogą być jednocześnie prawdziwe. Przykłady sprzeczności: zwycięzca A + zwycięzca B; Over 2.5 + wynik 1-0; BTTS tak + wynik 2-0; handicap A −1.5 + wygrana B; Under 2.5 + Over 3.5; wynik serii 2-0 + total map Over 2.5.
3. **Różnorodność:** nie buduj zestawu z samych typów od jednego czynnika (np. pięciu faworytów, którzy wszyscy "wygrają, bo są lepsi") - jedna niespodzianka niszczy wszystko. Rozdziel typy między ligi, dyscypliny i **rynki**. Przy kilku zestawach z jednego dnia (np. "5 kuponów") nie rób wszystkich kuponów samymi wynikami 1X2/podwójną szansą: wymieszaj rynki (wynik, gole O/U, BTTS, rożne, kartki, faule, rynki zawodnika), o ile analiza ma dla nich p i pewność co najmniej średnią. Kupon w całości z jednego rynku wyjaśnij tylko wtedy, gdy innych typów o sensownej pewności brak.
3a. **Typy niezależne od siebie w obrębie kuponu:** rynki powiązane z tym samym czynnikiem (np. Over goli + rożne tych samych drużyn, kartki + faule w tym samym meczu, kartka zawodnika + kartki meczowe Over) liczy się jako skorelowane; dlatego jeden mecz = jedna noga (reguła 1). Jeśli dwa kupony zawierają ten sam mecz z różnymi rynkami, sprawdź sprzeczności (np. Under 2.5 gola + BTTS tak + wygrana 3-0 itd.).
3b. **Rynki o dużej wariancji** (rożne, kartki, faule, zawodnik) wchodzą do zestawu zachowawczego tylko przy pewności średniej lub wysokiej i znanym sędzim/składzie; typ zawodnika wchodzi tylko po potwierdzeniu składu (zwykle ~1 h przed meczem), więc pokaż go z adnotacją "po składach".
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
Ryzyko: który element jest najsłabszy i co go zabija
```

Pod zestawami dodaj krótkie zastrzeżenia: założenie niezależności meczów, to że kursy mogą się zmienić do czasu postawienia, oraz że to oszacowania probabilistyczne, nie gwarancje. Jeśli żaden zestaw nie ma dodatniego EV, powiedz to wprost zamiast na siłę rekomendować - brak wartości to uczciwy wynik.
