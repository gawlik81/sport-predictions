---
name: tennis-predictor
description: Ekspert od statystyk tenisowych, który zbiera aktualne dane (forma, ranking ATP/WTA, statystyki serwisu i returnu na danej nawierzchni, H2H, kontuzje/zmęczenie, artykuły przedmeczowe) i szacuje prawdopodobieństwa zdarzeń meczowych - zwycięzca meczu, dokładny wynik setowy, total gemów (over/under, kluczowy nacisk analizy, pełny model probabilistyczny), handicap gemowy, zwycięzca pierwszego seta, asy, podwójne błędy, break pointy - dla ATP Tour i WTA Tour (Wielki Szlem, Masters 1000/WTA 1000, ATP 500/250, WTA 500/250), a na żądanie także Challenger/ITF World Tennis Tour. Użyj tego skilla zawsze, gdy użytkownik pyta o typowanie/prognozę meczu tenisowego, prawdopodobieństwo wygranej zawodnika lub statystyk meczowych (zwłaszcza total gemów), "value bet", fair odds/kursy, przegląd dnia turniejowego, lub prosi o analizę formy zawodnika/zawodniczki - nawet jeśli nie pada słowo "tenis", a jedynie nazwiska zawodników, nazwa turnieju lub data meczu.
---

# Tennis Predictor

Ten skill łączy dwie rzeczy: **research** (aktualne dane statystyczne i
medialne) i **model statystyczny** (hierarchiczny model punkt→gem→set→mecz
dla szansy na zwycięstwo i total gemów + szacunki oparte na średnich dla
pozostałych statystyk). Same liczby z modelu nie wystarczą — świeża kontuzja,
powrót z przerwy albo mecz na nielubianej nawierzchni potrafi zmienić obraz
bardziej niż jakikolwiek współczynnik z ostatnich 10 meczów. Dlatego każdy
raport łączy twarde dane z jakościową korektą na podstawie świeżych artykułów.

## Krok 0: Ustal zakres

Zanim zaczniesz zbierać dane, ustal jaki scenariusz pasuje do prośby
użytkownika i wybierz odpowiedni szablon z `references/report_templates.md`:

1. **Pojedynczy mecz** — najczęstszy przypadek, pełny raport z prawdopodobieństwami
2. **Przegląd dnia turniejowego** — kilka meczów naraz (np. cały dzień
   drabinki), wersja skrócona per mecz
3. **Forma zawodnika/zawodniczki** — analiza opisowa bez konkretnego meczu,
   bez tabel prawdopodobieństw
4. **Mecz w ramach Wielkiego Szlema / Masters 1000 (WTA 1000)** — jak (1)
   plus sekcja o stawce meczu, format best-of-5 (mężczyźni w Wielkim Szlemie)
   i weryfikacja aktualnego regulaminu tiebreaka w secie decydującym

Jeśli prośba jest niejednoznaczna (np. "co myślisz o starciu Sinner -
Alcaraz"), domyślnie traktuj to jako pojedynczy mecz z pełnym raportem — to
najbardziej użyteczna forma odpowiedzi.

**Format seta decydującego zmienia się między turniejami i sezonami** (przy
6-6: standardowy tiebreak do 7, tiebreak "mistrzowski" do 10 punktów, a na
Wimbledonie tiebreak dopiero przy 12-12) — zawsze zweryfikuj aktualny
regulamin danego turnieju przez research (Krok 1), zamiast zakładać format
z pamięci. To samo dotyczy formatu meczu (best-of-3 vs best-of-5) — kobiety
grają best-of-3 we wszystkich rozgrywkach, mężczyźni best-of-3 poza Wielkim
Szlemem (gdzie grają best-of-5).

## Krok 1: Zbierz dane (WebSearch / WebFetch)

Korzystaj z `references/data_sources.md` — tam jest lista konkretnych
serwisów per typ danych i podpowiedzi jak formułować zapytania. W skrócie
potrzebujesz:

- **Statystyki serwisu i returnu (priorytet tego skilla)** — % punktów
  wygranych na serwisie i % punktów wygranych returnem dla obu zawodników,
  **w miarę możliwości osobno dla danej nawierzchni** (twarda/mączka/trawa —
  różnice bywają duże, ten sam zawodnik może wygrywać 68% punktów na
  serwisie na trawie i 58% na mączce), bo te statystyki karmią pełny model
  probabilistyczny w Kroku 2-3, a nie tylko szacunek "na oko"
- **Forma obu zawodników** z ostatnich 10-15 meczów: wyniki, ewentualnie
  Elo rating (ogólny i per nawierzchnia, jeśli dostępny)
- **Ranking ATP/WTA** — aktualny i trend (awans/spadek w ostatnich miesiącach)
- **H2H** — ostatnie bezpośrednie starcia, najlepiej z rozbiciem per
  nawierzchnia, jeśli grali na różnych
- **Kondycja i zmęczenie** — liczba rozegranych meczów/setów w ostatnich
  1-2 tygodniach, długie/wyczerpujące mecze, świeże kontuzje lub powrót po
  przerwie, aklimatyzacja do nawierzchni/wysokości/strefy czasowej po długiej
  podróży
- **Kontekst turnieju** — ranga (Wielki Szlem/Masters/ATP 500 itd.), runda,
  format seta decydującego (patrz Krok 0), oraz czy któryś zawodnik ma
  historię wycofań/kontuzji w trakcie meczu (retirement risk)
- **Świeże artykuły** (ostatnie kilka dni) — kontekst: forma psychiczna,
  zmiana trenera, komunikaty o kontuzji, plany startowe

Nie trzeba przeszukiwać każdego źródła dla każdego meczu — jeśli Tennis
Abstract albo Ultimate Tennis Statistics dają wystarczające dane, to
wystarczy. Dociągaj kolejne źródła tam, gdzie są luki — **w szczególności
dla statystyk serwisu/returnu per nawierzchnia**: to kluczowy input tego
skilla, więc brak rozbicia per nawierzchnia jest jedną z niewielu sytuacji,
gdzie zawsze warto sprawdzić dodatkowe źródło (patrz
`references/data_sources.md`), zamiast poprzestać na ogólnej średniej
sezonowej.

Jeśli dla jakiejś statystyki naprawdę nie da się znaleźć danych (np. bardzo
młody zawodnik bez pełnej historii, turniej ITF z ograniczonym pokryciem),
**zaznacz to wprost w raporcie** zamiast podawać zmyśloną liczbę. Lepszy jest
"szeroki, ale uczciwy" przedział niż fałszywa precyzja.

## Krok 2: Oszacuj prawdopodobieństwo wygrania punktu na serwisie (model bazowy)

To jest kluczowy input modelu — odpowiednik oczekiwanych goli (λ) w piłce
nożnej, tylko że tutaj bazową jednostką jest punkt, nie gol. Podejście
analogiczne do siły ataku/obrony w piłce:

1. Ustal **średnią turową (tour average) % punktów wygranych na serwisie**
   dla danej nawierzchni (orientacyjne wartości w
   `references/data_sources.md` — zawsze staraj się zweryfikować aktualną
   wartością z Kroku 1, bo różni się między ATP/WTA i sezonami)
2. **Siła serwisu zawodnika A** = (% punktów wygranych na serwisie przez A) ÷
   (średnia turowa % serwisu dla danej nawierzchni)
3. **Siła returnu zawodnika B** = (% punktów wygranych returnem przez B) ÷
   (średnia turowa % returnu dla danej nawierzchni, czyli 1 − średnia
   turowa serwisu)
4. **p_a_serve** (prawdopodobieństwo, że A wygra punkt na swoim serwisie w
   tym meczu) = średnia turowa % serwisu × siła serwisu A × siła returnu B
5. **p_b_serve** = analogicznie (siła serwisu B × siła returnu A × średnia
   turowa % serwisu)

To daje punkt wyjścia oparty na danych sezonowych/nawierzchniowych.
Następnie **skoryguj p_a_serve/p_b_serve jakościowo** na podstawie tego, co
znalazłeś w Kroku 1: świeża kontuzja nadgarstka może obniżyć % serwisu o
kilka punktów procentowych, powrót po długiej przerwie zwykle obniża
skuteczność returnu (mniej meczowego rytmu), zmęczenie po długim
poprzednim meczu obniża oba, wiatr na kortach otwartych może obniżyć %
pierwszego serwisu. Krótko opisz w raporcie, jakie korekty zastosowałeś i
dlaczego — to często najważniejsza część analizy, bo surowe średnie
sezonowe nie znają kontekstu.

Jeśli nie udało się policzyć solidnych współczynników z danych sezonowych
(np. debiutant na touree, zbyt mało meczów w bieżącym sezonie), oszacuj
p_a_serve/p_b_serve na podstawie ogólnego rankingu, formy z ostatnich meczów
i stylu gry — zaznacz, że to luźniejsze oszacowanie.

**Różnice ATP vs WTA i między nawierzchniami są duże** — nie przenoś
wartości p_serve wyliczonej dla jednego kontekstu (np. ATP na trawie, gdzie
serwis dominuje bardziej, %serwisu bywa >65%) do innego (np. WTA na mączce,
gdzie wymiany są dłuższe, %serwisu bywa <55%) bez ponownego odniesienia do
właściwej średniej turowej.

## Krok 2b: Dyscyplina pewności (kalibracja z weryfikacji)

Reguły wynikają z weryfikacji predykcji względem rzeczywistych wyników (patrz
`analizy/Weryfikacja_USOpen_10-pewniakow_2026-08-30-31.md` i
`analizy/Weryfikacja_predykcji_2026-09-24.md`). Każdy sygnał ostrzegawczy musi
**realnie obniżyć liczbę użytą do rankingu pewności**. Sama wzmianka w opisie nie wystarcza.

1. **Pierwszy mecz faworyta po wolnym losie lub po przerwie ≥2 tygodni, gdy rywal ma rytm meczowy.**
   Przykład: Eala (nr 18, rozstawiona z nr 3) w Singapurze grała pierwszy mecz od US Open. Model dał jej
   90,8%, a przegrała z nr 180 Prozorovą, choć prowadziła 1 set i 4-2. Obniż p faworyta o 5-8 pp.
   W WTA nie umieszczaj takiego meczu wyżej niż na poziomie ~85% w rankingu top-N.
2. **Zmęczenie underdoga po maratonie w poprzedniej rundzie to słaby argument za faworytem.**
   Prozorova miała za sobą 2 h 51 min z poprzedniej rundy i wygrała. Rytm meczowy i pewność siebie
   po wygranym maratonie często równoważą zmęczenie, zwłaszcza w best-of-3 przy dniu przerwy.
   Nie podnoś p faworyta z tego powodu.
3. **Kryzys formy faworyta to trafna flaga.** Ostapenko (9-13 na twardej w 2026) przegrała 4-6 1-6
   z rozpędzoną Preston. Faworyta z ujemnym bilansem sezonu na danej nawierzchni i serią porażek
   traktuj jak mecz bliski 50/50, niezależnie od rankingu.
4. **Total gemów tylko przy rzeczywistych statystykach serwisu i returnu.** Przy p_serve oszacowanych
   z rankingu (brak danych z Tennis Abstract, UTS lub ATP/WTA stats) model dobrze wskazywał
   zwycięzcę (6/8), ale total gemów mylił się średnio o ~5 gemów. W takiej sytuacji pokaż total gemów
   w raporcie z wyraźnym zastrzeżeniem, ale **nie umieszczaj go w rankingu najlepszych typów**.
5. **Wiek 35+ w best-of-5** to systematycznie niedoszacowane ryzyko nagłej choroby lub kontuzji
   w trakcie meczu. Przykład: Djokovic przy 89,8% przegrał I rundę US Open. Przy rankowaniu obniż p
   o 3-5 pp albo nie umieszczaj takiego meczu w ścisłej czołówce.
6. **Seria dobrych wyników tuż przed turniejem działa w obie strony: rozpęd albo zmęczenie.** Przy
   napiętym kalendarzu (finał, półfinał lub ćwierćfinał w 2-3 turniejach z rzędu) jawnie rozważ obie
   hipotezy. Nie traktuj takiej serii automatycznie jako plusa.
7. **WTA: przepaść rankingowa gwarantuje czysty wynik setowy słabiej niż w ATP.** Przy typach na
   dokładny wynik setowy spłaszczaj rozkład modelu. Ruse (74,7%) wygrała z nr ~180 Ku dopiero
   po stracie seta i przy stanie 2-4 w drugim.
8. **Dla każdego faworyta w zestawieniu top-N wykonaj osobne zapytanie
   „[zawodnik] injury [rok]”.** Nie polegaj na tym, że ogólny research formy przypadkiem wyłapie
   kontuzję.

**Co działa:** duże przepaści jakościowe poparte konkretną, świeżą statystyką sezonu (RPW, SGW) dają
najpewniejsze trafienia, łącznie z dokładnym wynikiem setowym. Dlatego w Kroku 1 priorytetem jest
dociągnięcie tych statystyk, a szacunek z samego rankingu to ostateczność.

## Krok 3: Policz prawdopodobieństwa modelem hierarchicznym punkt→gem→set→mecz

Użyj `scripts/tennis_model.py` z wyliczonymi p_a_serve / p_b_serve:

```bash
python3 scripts/tennis_model.py --p-a-serve 0.64 --p-b-serve 0.60 --best-of 3 \
    --game-lines 20.5,21.5,22.5 --top-set-scores 5
```

Dla meczów best-of-5 (Wielki Szlem, mężczyźni) ustaw `--best-of 5` i
`--final-set-tiebreak-to` zgodnie z aktualnym regulaminem turnieju
zweryfikowanym w Kroku 1 (np. `10` dla Australian Open / Roland Garros,
`7` dla US Open):

```bash
python3 scripts/tennis_model.py --p-a-serve 0.68 --p-b-serve 0.60 --best-of 5 \
    --final-set-tiebreak-to 10 --game-lines 37.5,38.5,39.5 --handicap-lines 3.5,4.5
```

**Wimbledon jest wyjątkiem** — tiebreak w secie decydującym pojawia się
dopiero przy 12-12, czego skrypt nie modeluje dokładnie (obsługuje tylko
"tiebreak przy 6-6"). Dla meczów na Wimbledonie w decydującym secie potraktuj
liczby ze skryptu jako przybliżenie i zaznacz w raporcie szerszy przedział
niepewności zamiast fałszywej precyzji.

Skrypt zwraca JSON z gotowymi prawdopodobieństwami i "fair odds" (1/p) dla:
zwycięzcy meczu, dokładnego wyniku setowego, zwycięzcy pierwszego seta (plus
ranking najbardziej prawdopodobnych wyników pierwszego seta), oraz — patrz
Krok 4 — total gemów i handicapu gemowego. Przepisz te liczby do tabel w
raporcie — nie licz tego ręcznie, model robi to dokładnie (pełna enumeracja,
nie symulacja).

## Krok 4: Total gemów i handicap gemowy (priorytet — analogicznie do rożnych w piłce nożnej)

**Total gemów to główny nacisk tego skilla, obok zwycięzcy meczu** —
dokładnie tak jak rożne w skillu piłkarskim. W przeciwieństwie do piłki nie
trzeba tu osobnego wywołania modelu z innymi λ — pole `total_games` i
`games_handicap` w JSON-ie z Kroku 3 pochodzą z **tej samej, w pełni
policzonej dystrybucji meczu** (liczba gemów w każdym możliwym przebiegu
seta jest już częścią modelu). Mimo to potraktuj tę sekcję w raporcie z tym
samym rygorem co zwycięzcę meczu, a nie jako pobieżny dodatek na końcu:

1. Zaprezentuj `total_games.expected` (oczekiwana liczba gemów) oraz tabelę
   `total_games.over_under` dla progów przekazanych w `--game-lines` —
   dobierz progi w okolicy oczekiwanej wartości (np. jeśli oczekiwane ~22
   gemy, sprawdź 20.5/21.5/22.5/23.5)
2. Jeśli użytkownik pyta o handicap gemowy, dolicz `--handicap-lines` (np.
   `3.5,4.5`) i zaprezentuj `games_handicap` analogicznie
3. Skomentuj jakościowo: styl gry wpływa na total gemów silniej niż na
   samego zwycięzcę — dwóch serwujących z dużą przewagą serwisu (mało
   breaków) generuje więcej gemów per set (bliżej 6-4/7-6) niż mecz dwóch
   returnerów z wieloma breakami (bliżej 6-2/6-3); podobnie długi,
   wyrównany mecz (więcej setów w best-of-5, więcej tiebreaków) podnosi
   total gemów
4. Jeśli mimo dociągnięcia dodatkowych źródeł (Krok 1) dane o % serwisu/
   returnu są zbyt skąpe, żeby policzyć solidne p_a_serve/p_b_serve,
   zaznacz wprost w raporcie, że total gemów jest luźniejszym
   przybliżeniem — ale nie pomijaj tej sekcji ani nie zastępuj jej samym
   przedziałem bez modelu

## Krok 5: Oszacuj pozostałe statystyki (asy, podwójne błędy, break pointy)

Te statystyki są drugorzędne względem zwycięzcy i total gemów, a jednocześnie
nie mają tak dokładnego modelu probabilistycznego w skrypcie, więc podejście
jest prostsze i bardziej "rzemieślnicze":

1. Weź średnią asów/meczu zawodnika A i przelicz na oczekiwaną liczbę gemów
   serwisowych w tym meczu (w przybliżeniu połowa `total_games.expected`,
   skorygowana o to, kto serwuje częściej przy nieparzystej liczbie gemów) —
   to daje oczekiwaną liczbę asów A w tym meczu; analogicznie dla B i dla
   podwójnych błędów
2. Podaj wynik jako **przedział wokół średniej** (np. "8-12 asów, średnio
   ~10"), bo te statystyki mają dużą wariancję mecz do meczu — pojedyncza
   liczba sugerowałaby fałszywą precyzję
3. **Break pointy**: oszacuj liczbę gemów serwisowych każdego zawodnika (z
   `match_score`/`total_games`) i jego % obrony break pointów z danych
   sezonowych, żeby oszacować oczekiwaną liczbę przełamań — to samo w sobie
   dobrze koresponduje z `games_handicap` z Kroku 4, więc traktuj je jako
   uzupełnienie tej samej historii, nie osobny wątek
4. **Ryzyko wycofania (retirement)**: jeśli w Kroku 1 znalazłeś sygnały
   (świeża kontuzja, historia wycofań, sygnały fizycznego dyskomfortu w
   poprzednich meczach), wspomnij o tym wprost jako czynniku ryzyka — to
   specyficzne dla tenisa (mecz może się skończyć przed czasem) i nie ma
   odpowiednika w piłce nożnej

## Krok 6: Napisz raport

Użyj odpowiedniego szablonu z `references/report_templates.md`. Każdy
szablon kończy się tą samą notą:

> *Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
> finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*

Zachowaj ją w każdym raporcie.

## Krok 7: Zapisz raport do pliku Markdown

Niezależnie od tego, czy użytkownik o to poprosił, **zawsze zapisz gotowy
raport do pliku `.md`** (oprócz pokazania go w odpowiedzi) — tak, by można
było do niego wrócić bez ponownego odpytywania modelu. Zasady:

- Zapisz w katalogu `analizy/` w bieżącym katalogu roboczym (utwórz go,
  jeśli nie istnieje).
- Nazwa pliku powinna być opisowa i zawierać daty/zawodników/zakres, np.
  `Sinner_Alcaraz_2026-09-05.md`, `AustralianOpen_runda3_2026-01-20.md`,
  `WTA_Indian-Wells_dzien3_2026-03-12.md` — slug bez polskich znaków i
  spacji (podkreślenia zamiast spacji).
- Plik powinien zawierać dokładnie tę samą treść, którą pokazujesz
  użytkownikowi w odpowiedzi (włącznie z disclaimerem).
- Na końcu odpowiedzi krótko poinformuj, gdzie zapisano plik.

## Wskazówki ogólne

- **Nawierzchnia zmienia wszystko.** Ten sam zawodnik może być zupełnie inną
  propozycją na trawie niż na mączce — zawsze sprawdzaj statystyki serwisu/
  returnu i formę specyficzne dla nawierzchni danego turnieju (Krok 1-2),
  zamiast opierać się na ogólnej średniej sezonowej, gdy tylko dane na to
  pozwalają.
- **Total gemów ma pierwszeństwo.** To główna statystyka tego skilla obok
  zwycięzcy meczu (Krok 4) — zawsze prezentuj `total_games` i (jeśli
  proszone) `games_handicap` z pełnym uzasadnieniem modelu, umieszczaj
  wysoko w raporcie, i nie redukuj tego do jednej linijki z przedziałem,
  jeśli dane na to pozwalają.
- **Format meczu i seta decydującego zawsze weryfikuj researchem** (Krok 0),
  nie zakładaj z pamięci — zmieniał się w ostatnich latach na kilku Wielkich
  Szlemach i różni się między turniejami.
- **Transparentność ponad pewność siebie.** Jeśli model bazowy mówi co
  innego niż "oko ekspackie" (np. zawodnik w kryzysie formy ma wciąż mocne
  statystyki sezonowe serwisu), napisz o tym wprost — to jest właśnie
  wartościowa informacja dla użytkownika, nie błąd do ukrycia.
- **Nie zaokrąglaj kontekstu do zera.** Nawet krótka wzmianka o tym, że
  zawodnik wraca po kontuzji nadgarstka albo przeleciał właśnie przez kilka
  stref czasowych, może być ważniejsza niż 0.02 różnicy w p_serve.
- **Język raportu** dopasuj do języka użytkownika (domyślnie polski, ale
  jeśli użytkownik pisze po angielsku, odpowiadaj po angielsku).
- **Nie zmyślaj nazwisk, wyników meczów ani statystyk.** Jeśli czegoś nie
  udało się znaleźć, powiedz to wprost — w szczególności nie zmyślaj, że
  jakiś mecz się odbędzie/odbył, jeśli nie udało się tego potwierdzić
  (np. zawodnik zakończył karierę, turniej jest w innym terminie niż
  zakładasz z pamięci, drabinka jeszcze nie została ogłoszona).
