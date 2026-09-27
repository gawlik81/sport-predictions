---
name: football-predictor
description: Ekspert od statystyk piłki nożnej, który zbiera aktualne dane (forma, H2H, kontuzje, artykuły przedmeczowe) i szacuje prawdopodobieństwa zdarzeń meczowych - wynik 1X2, rzuty rożne (kluczowy nacisk analizy, pełny model probabilistyczny), dokładny wynik, liczba goli (over/under, BTTS), strzały, strzały celne, faule i kartki (analiza drużynowa oraz indywidualna
na poziomie zawodnika, wliczona do korekty predykcji) - dla Top 5 lig europejskich (Premier League, La Liga, Serie A, Bundesliga, Ligue 1), polskiej Ekstraklasy, amerykańskiej MLS, pucharów europejskich (Liga Mistrzów, Liga Europy, Liga Konferencji), krajowych pucharów bez rewanżu (Puchar Króla/Copa del Rey, Puchar Ligi Angielskiej/EFL Cup/Carabao Cup - w tym prawdopodobieństwo awansu przy remisie i wpływ rotacji składu), reprezentacji narodowych oraz turniejów (Mistrzostwa Świata, Mistrzostwa Europy). Użyj tego skilla zawsze, gdy użytkownik pyta o typowanie/prognozę meczu, prawdopodobieństwo wyniku lub statystyk meczowych (zwłaszcza rożnych), "value bet", fair odds/kursy, przegląd kolejki ligowej, lub prosi o analizę formy drużyny/zawodnika - nawet jeśli nie pada słowo "piłka nożna", a jedynie nazwy drużyn, lig lub data meczu.
---

# Football Predictor

Ten skill łączy dwie rzeczy: **research** (aktualne dane statystyczne i
medialne) i **model statystyczny** (rozkład Poissona dla goli + szacunki
oparte na średnich dla pozostałych statystyk). Same liczby z modelu nie
wystarczą — kontuzja kluczowego napastnika albo mecz "o nic" w ostatniej
kolejce potrafi zmienić obraz bardziej niż jakikolwiek współczynnik z
poprzednich 10 meczów. Dlatego każdy raport łączy twarde dane z jakościową
korektą na podstawie świeżych artykułów.

## Krok 0: Ustal zakres

Zanim zaczniesz zbierać dane, ustal jaki scenariusz pasuje do prośby
użytkownika i wybierz odpowiedni szablon z `references/report_templates.md`:

1. **Pojedynczy mecz** — najczęstszy przypadek, pełny raport z prawdopodobieństwami
2. **Kolejka ligowa** — kilka meczów naraz, wersja skrócona per mecz
3. **Forma drużyny/zawodnika** — analiza opisowa bez konkretnego meczu, bez
   tabel prawdopodobieństw
4. **Mecz turniejowy/pucharowy** (MŚ/ME/fazy pucharowe, **Puchar Króla,
   EFL Cup/Carabao Cup, playoffy MLS**) — jak (1) plus sekcja o stawce meczu;
   jeśli to runda bez możliwości remisu (patrz niżej), dodaj też
   "Prawdopodobieństwo awansu"

Jeśli prośba jest niejednoznaczna (np. "co myślisz o starciu Lecha z
Rakowem"), domyślnie traktuj to jako pojedynczy mecz z pełnym raportem —
to najbardziej użyteczna forma odpowiedzi.

**Copa del Rey i EFL Cup mają specyficzny format**, który zmienia się między
sezonami (np. liczba rund rozgrywanych dwumeczowo, obecność dogrywki w
danej rundzie) — zawsze zweryfikuj aktualny regulamin danej rundy przez
research (Krok 1), zamiast zakładać format z pamięci. To samo dotyczy formatu
playoffów MLS (drabinka, ewentualne dwumecze) w danym sezonie.

## Krok 1: Zbierz dane (WebSearch / WebFetch)

Korzystaj z `references/data_sources.md` — tam jest lista konkretnych
serwisów per typ danych i podpowiedzi jak formułować zapytania, żeby trafić
za pierwszym razem. W skrócie potrzebujesz:

- **Rożne (priorytet tego skilla)** — średnia rożnych zdobytych i oddanych
  przez każdą drużynę, w miarę możliwości osobno dla domu i wyjazdu
  (dokładnie tak jak dla goli, bo rożne dostają w Kroku 4 pełny model
  probabilistyczny, a nie tylko szacunek "na oko")
- **Forma obu drużyn** z ostatnich 5-10 meczów: wyniki, gole strzelone/
  stracone, a jeśli dostępne — xG/xGA
- **Statystyki sezonowe per drużyna**: gole strzelone/stracone w domu i na
  wyjeździe (do policzenia siły ataku/obrony), oraz średnie strzałów,
  strzałów celnych, faulów, kartek (osobno "for" i "against")
- **Faule i kartki na poziomie zawodnika** — dla kluczowych zawodników
  (zwłaszcza defensywnych pomocników i stoperów): faule popełnione/90 min i
  faule sprowokowane (doznane)/90 min, liczba żółtych/czerwonych kartek w
  sezonie oraz dystans do zawieszenia. To dane wejściowe do Kroku 6 (profil
  dyscyplinarny), nie tylko ciekawostka na koniec raportu — patrz
  `references/data_sources.md` po konkretne źródła (FBref "Miscellaneous
  Stats" per zawodnik, Transfermarkt dla historii kartek/zawieszeń).
- **H2H** — ostatnie bezpośrednie starcia
- **Kadra** — kontuzje, zawieszenia, prawdopodobny skład
- **Świeże artykuły** (ostatnie kilka dni) — kontekst: motywacja, zmiany
  trenerskie, plotki, nastroje

Nie trzeba przeszukiwać każdego źródła dla każdego meczu — jeśli FBref albo
Sofascore dają wystarczające dane, to wystarczy. Dociągaj kolejne źródła tam,
gdzie są luki — **w szczególności dla rożnych**: to teraz kluczowa statystyka
tego skilla, więc brak pełnego rozbicia dom/wyjazd jest jedną z niewielu
sytuacji, gdzie zawsze warto sprawdzić dodatkowe źródło (patrz
`references/data_sources.md`), zamiast poprzestać na luźnym oszacowaniu.

Jeśli dla jakiejś statystyki naprawdę nie da się znaleźć danych (np. bardzo
niszowa liga albo świeżo awansowana drużyna bez historii), **zaznacz to
wprost w raporcie** zamiast podawać zmyśloną liczbę. Lepszy jest "szeroki,
ale uczciwy" przedział niż fałszywa precyzja.

## Krok 2: Policz oczekiwane gole (model bazowy)

Standardowe podejście (Dixon-Coles / Poisson w uproszczonej formie):

1. Policz średnią goli w lidze (gole/mecz, osobno dla gospodarzy i gości,
   bo gospodarze średnio strzelają więcej — tzw. home advantage)
2. **Siła ataku drużyny** = (gole strzelone przez drużynę / mecz) ÷ (średnia
   ligowa goli/mecz dla danej strony - dom/wyjazd)
3. **Siła obrony drużyny** = (gole stracone przez drużynę / mecz) ÷ (średnia
   ligowa goli/mecz)
4. **Oczekiwane gole gospodarza** (λ_home) = siła ataku gospodarza × siła
   obrony gościa × średnia ligowa goli gospodarzy
5. **Oczekiwane gole gościa** (λ_away) = analogicznie

To daje punkt wyjścia oparty na danych z całego sezonu. Następnie **skoryguj
λ jakościowo** na podstawie tego, co znalazłeś w kroku 1: brak kluczowego
napastnika może obniżyć λ o 10-20%, mecz "o nic" dla jednej drużyny może
obniżyć jej λ i podnieść przeciwnika, itd. Profil dyscyplinarny drużyny i
kluczowych zawodników (patrz Krok 6) jest tego samego typu korektą — np.
rywal regularnie kończący mecze w osłabieniu po czerwonej kartce, albo
kluczowy stoper grający "na zawieszeniu" i przez to asekuracyjnie, mogą
uzasadniać korektę λ na równi z kontuzją. Krótko opisz w raporcie, jakie
korekty zastosowałeś i dlaczego — to jest często najważniejsza część analizy,
bo surowe średnie sezonowe nie znają kontekstu.

Jeśli nie udało się policzyć solidnych współczynników z danych sezonowych
(np. za mało meczów rozegranych w sezonie, początek rozgrywek), oszacuj λ na
podstawie formy z ostatnich meczów i ogólnej jakości drużyn — zaznacz, że to
luźniejsze oszacowanie.

**Mecze międzyligowe (Puchar Króla, EFL Cup) — brak wspólnej średniej
ligowej.** Gdy drużyny pochodzą z różnych poziomów rozgrywkowych (np. klub
La Liga vs. drużyna Segunda/Segunda RFEF, klub Premier League vs. klub
Championship/League One), formuła siła ataku/obrony ÷ średnia ligowa nie ma
wspólnego mianownika. W takim wypadku:
1. Policz siłę ataku/obrony każdej drużyny względem średniej **jej własnej
   ligi**, a jako wspólny punkt odniesienia użyj ogólnej średniej goli/mecz
   w europejskim futbolu klubowym (orientacyjnie ~2.6-2.8 gola/mecz) zamiast
   jednej wspólnej ligi
2. Oprzyj się mocniej na jakościowej ocenie różnicy poziomów (a nie tylko na
   surowych średnich), bo różnica klas rozgrywkowych rzadko jest w pełni
   uchwycona przez proste współczynniki
3. Zaznacz w raporcie szerszy przedział niepewności niż przy meczu w ramach
   jednej ligi

**MLS — dodatkowe czynniki kontekstowe.** Do korekty jakościowej λ dodaj:
sezon MLS trwa luty/marzec-grudzień (inny kalendarz niż europejski, więc
"forma" i "sezon" liczy się inaczej niż w Top 5), brak spadków więc pod
koniec sezonu drużyny poza wyścigiem o playoff mogą grać "o nic", część
stadionów ma sztuczną nawierzchnię (przewaga dla gospodarza przyzwyczajonego
do niej), oraz długie przeloty międzystrefowe potrafią być realnym czynnikiem
zmęczeniowym dla drużyny gościnnej. Do liczenia średniej ligowej użyj średniej
całej MLS (obie konferencje łącznie) jako przybliżenia.

## Krok 2b: Dyscyplina pewności dla typów 1X2 (kalibracja z weryfikacji)

Dwie rundy weryfikacji predykcji względem rzeczywistych wyników (98 typów 1X2/awansu łącznie — patrz
`analizy/Weryfikacja_predykcji_kolejki1-2_2026-08.md` i
`analizy/Weryfikacja_predykcji_2026-08-27_2026-09-17.md`) dały ok. 60-70% trafień — sensowna ogólna
kalibracja, ale z dwoma powtarzalnymi wzorcami błędu, które trzeba jawnie uwzględniać w raporcie i w
finalnej liczbie, nie tylko opisowo:

1. **Remis i "odwrotny wynik" (underdog wygrywa wyraźnie) to PORÓWNYWALNE źródła ryzyka dla typów w
   przedziale 50-85% pewności — nie tylko remis.** Wcześniejsza, mniejsza próba sugerowała, że remis
   dominuje jako przyczyna pudeł; większa próba pokazała, że ok. 2/3 pudeł to w rzeczywistości underdog
   wygrywający bez remisu w tle (np. Real Betis pokonał Real Madryt, Paris FC i Monaco pokonały PSG/
   Marseille, Como pokonało Leipzig). **Przy każdym typie 1X2 w tym przedziale wymień w raporcie OBA
   scenariusze zagrożenia**, chyba że research z Kroku 1 daje konkretny, jednostronny powód faworyzować
   jeden z nich (styl gry defensywny na wyjeździe → bardziej remis; underdog z desperacką motywacją/
   nowym trenerem/kryzysem → bardziej odwrotny wynik, patrz punkt 2).
2. **Ekstremalna przepaść jakościowa NIE jest automatyczną gwarancją, gdy underdog jest w stanie
   "kryzysowym"** (seria bez zwycięstwa, świeża zmiana trenera, zero goli od wielu meczów) — to co innego
   niż zwykła "słabsza drużyna w normalnej formie". Przykład z weryfikacji: Alavés dostał 82% pewności
   (komplet zwycięstw u siebie) i przegrał z Valencią — ostatnią drużyną ligi, 2 dni po zwolnieniu
   trenera. Ekstremalne przepaście między "zdrowymi" klubami (Bayern, PSG, Barcelona) nadal trafiały
   niezawodnie. **Gdy underdog jest kryzysowy, a nie tylko słabszy klasowo, zastosuj REALNĄ korektę w dół
   pewności faworyta (np. -5 do -10 pp od "surowej" liczby z modelu)**, nie tylko opisową wzmiankę o
   ryzyku "rannego zwierzęcia"/nowej miotły bez wpływu na finalną liczbę — to ten sam błąd, co
   ignorowanie już zauważonego sygnału ostrzegawczego.
3. **Mecze pucharowe bez rewanżu z możliwą rotacją mają wyższy odsetek niespodzianek niż odpowiadające im
   mecze ligowe** (w weryfikacji: 40% trafień w rundzie Carabao Cup vs ~70% w lidze w tym samym oknie).
   Dla takich meczów obniż górny pułap pewności typu o kilka punktów procentowych względem "czystego"
   ligowego odpowiednika i zaznacz to wprost w raporcie — patrz też "Rotacje w pucharach krajowych"
   niżej.
4. **Typy rożnych/fauli są w praktyce prawie niemożliwe do zweryfikować po fakcie** (dane większości
   serwisów są renderowane przez JS, niewidoczne dla zwykłego wyszukiwania) — to nie zmienia metodologii
   liczenia (Krok 4 pozostaje priorytetem), ale oznacza, że jedyna realna kontrola jakości dla tej
   kategorii to rygor źródeł w momencie predykcji (dwa niezależne źródła przy rożnych, jak już wskazuje
   `references/data_sources.md`) — nie licz na to, że da się to później łatwo zweryfikować tak jak wynik
   meczu. Weryfikacja z 24.09 (Liga Narodów) potwierdziła to ponownie: oba typy rożnych okazały się
   niesprawdzalne. **W meczach reprezentacji, gdzie λ_rożne pochodzi z jednego źródła, typ rożny
   może mieć najwyżej średnią pewność.**
5. **Mecze reprezentacji: nie zaniżaj λ przy słabym ataku.** Weryfikacja
   `analizy/Weryfikacja_predykcji_2026-09-24.md` dała taki obraz:
   - Model zaniżył gole średnio o ok. 0,3 na mecz.
   - Najmocniej pomylił się tam, gdzie λ obniżono najbardziej. Andora dostała λ 0,55 i strzeliła w 17.
     minucie. Serbia po korekcie -20% za brak napastników strzeliła w 4. minucie. Oba typy Under 2,5
     przegrały przez gole po 80. minucie.
   - Reprezentacje częściej niż kluby rozstrzygają mecz w końcówce: 3 z 8 meczów miały gol w 90+.

   Dlatego:
   - nie schodź z λ drużyny poniżej ok. 0,7, nawet przy serii meczów bez gola;
   - nie kumuluj korekt kadrowych w dół powyżej ok. 15% łącznie;
   - typ Under 2,5 przy łącznym λ ≤ 2,0 traktuj najwyżej jako średnią pewność;
   - na rynku goli preferuj Over 1,5, który trafił 3/3 w rankingu i 6/8 we wszystkich meczach dnia.
6. **Korekta „kryzysowa” z pkt 2 dotyczy tylko underdoga, nie faworyta.** Nie obniżaj λ faworyta za jego
   własną słabą serię, jeśli rywal jest klasowo wyraźnie słabszy. Przykład: Litwa (model 64,7%, rynek
   ok. 79%) pewnie wygrała 2-0 z Liechtensteinem. Gdy w meczu o dużej różnicy klas model odbiega od rynku
   o ponad 10 pp, zaznacz to wprost i nie zakładaj, że model ma rację. W takich meczach rynek bywał
   lepiej skalibrowany.

## Krok 3: Policz prawdopodobieństwa modelem Poissona

Użyj `scripts/poisson_model.py` z wyliczonymi λ:

```bash
python3 scripts/poisson_model.py --lambda-home 1.8 --lambda-away 1.2 \
    --ou-lines 1.5,2.5,3.5 --top-scores 6
```

Skrypt zwraca JSON z gotowymi prawdopodobieństwami i "fair odds" (1/p) dla:
1X2, BTTS, over/under dla podanych progów goli, oraz ranking najbardziej
prawdopodobnych dokładnych wyników. Przepisz te liczby do tabel w raporcie —
nie licz tego ręcznie, model robi to dokładnie.

### Mecze pucharowe bez remisu (Puchar Króla, EFL Cup, playoffy MLS)

Jeśli research w Kroku 1 potwierdzi, że dana runda nie dopuszcza remisu
(rozstrzygnięcie w dogrywce/karnych zamiast replaya), zaprezentuj obok
klasycznego 1X2 tabelę **"Prawdopodobieństwo awansu"**:
1. `home` i `away` z pola `1x2` skryptu to bezpośrednio prawdopodobieństwo
   awansu w 90 minutach dla każdej drużyny
2. Prawdopodobieństwo z pola `draw` (remis w 90 minutach) rozdziel między obie
   drużyny jako szansę na awans po dogrywce/karnych — orientacyjnie 50/50,
   ewentualnie skoryguj o kilka punktów procentowych w stronę faworyta z
   1X2 (karne i dogrywka spłaszczają różnicę klas bardziej niż 90 minut, więc
   nie przenoś różnicy z 1X2 wprost)
3. Zsumuj: P(awans A) = P(A wygrywa w 90) + 0.5×P(remis w 90) [± korekta],
   analogicznie dla B — to i tak przybliżenie, zaznacz to w raporcie

## Krok 4: Policz oczekiwane rożne (priorytet — model równoległy do goli)

**Rożne to główny nacisk tego skilla, obok wyniku meczu.** Traktuj je z tym
samym rygorem metodologicznym co gole w Krokach 2-3 — pełny model z λ i
uzasadnieniem — a nie jako pobieżny dodatek na końcu raportu.

1. Policz średnią rożnych w lidze (rożne/mecz, osobno dla gospodarzy i
   gości — gospodarze zwykle mają nieco więcej rożnych dzięki przewadze
   terenu i częstszemu atakowaniu)
2. **Siła rożna ataku drużyny** = (rożne zdobyte przez drużynę / mecz) ÷
   (średnia ligowa rożnych/mecz dla danej strony - dom/wyjazd)
3. **Siła rożna obrony drużyny** = (rożne oddane przez drużynę / mecz) ÷
   (średnia ligowa rożnych/mecz)
4. **Oczekiwane rożne gospodarza** (λ_rożne_home) = siła rożna ataku
   gospodarza × siła rożna obrony gościa × średnia ligowa rożnych gospodarzy
5. **Oczekiwane rożne gościa** (λ_rożne_away) = analogicznie
6. Skoryguj jakościowo, tak jak przy golach: drużyny grające skrzydłami,
   dużo dośrodkowujące lub grające wysokim pressingiem generują więcej
   rożnych; drużyny broniące się nisko blokiem oddają więcej rożnych
   przeciwnikowi (odbite/zablokowane strzały lądują na aucie); zmiana
   trenera lub taktyki potrafi to szybko zmienić — krótko opisz zastosowane
   korekty, tak jak dla λ goli w Kroku 2

Policz prawdopodobieństwa **tym samym skryptem** `scripts/poisson_model.py`,
tym razem podstawiając λ dla rożnych zamiast goli:

```bash
python3 scripts/poisson_model.py --lambda-home 6.2 --lambda-away 4.6 \
    --ou-lines 8.5,9.5,10.5,11.5 --max-goals 15 --top-scores 5
```

Podnieś `--max-goals` względem domyślnego, bo rożnych pada więcej niż goli —
np. 15 pokrywa realny zakres dla łącznej wartości do ~20-22. Skrypt zwraca:

- **Pole `1x2`** — czytaj jako "przewaga rożna": `home` = prawdopodobieństwo,
  że gospodarz zdobędzie więcej rożnych, `draw` = taka sama liczba rożnych
  obu drużyn, `away` = analogicznie dla gościa. Zaprezentuj to w raporcie
  tabelą tak samo jak 1X2 dla goli.
- **Pole `over_under`** — over/under dla progów rożnych, dokładnie jak dla
  goli (to najczęściej najbardziej użyteczna część dla użytkownika)
- **Pole `top_scores`** — najbardziej prawdopodobne dokładne "wyniki" rożnych
  (np. "5-4") — przydatna ciekawostka, ale drugorzędna względem 1X2/over-under
  powyżej

Jeśli mimo dociągnięcia dodatkowych źródeł (Krok 1) dane o rożnych są zbyt
skąpe, żeby policzyć solidne λ (np. drużyna bez pełnej historii sezonowej),
oszacuj λ na podstawie średniej ligowej i ogólnego stylu gry drużyny, i
zaznacz wprost w raporcie, że to luźniejsze przybliżenie — ale nie pomijaj
tego kroku ani nie zastępuj go samym przedziałem bez modelu.

## Krok 5: Oszacuj strzały i strzały celne

Ta statystyka jest drugorzędna względem goli i rożnych, a jednocześnie nie ma
tak dobrego modelu probabilistycznego, więc podejście jest prostsze i
bardziej "rzemieślnicze":

1. Weź średnią drużyny A "for" (np. strzały celne/mecz) i średnią drużyny B
   "against" (strzały celne oddane/mecz) — ich połączenie (np. średnia z
   obu, lub ważona w stronę nowszych meczów) daje oczekiwaną wartość dla
   drużyny A w tym meczu. Analogicznie dla B.
2. Zsumuj oczekiwane wartości obu drużyn, żeby dostać łączną wartość
   (np. łączna liczba strzałów w meczu)
3. Podaj wynik jako **przedział wokół średniej** (np. "11-14, średnio ~12.5"),
   bo te statystyki mają dużą wariancję mecz do meczu — pojedyncza liczba
   sugerowałaby fałszywą precyzję
4. Jeśli chcesz podać konkretny % over/under, możesz analogicznie do rożnych
   przybliżyć rozkład jako Poissona z λ = oczekiwana wartość i użyć
   `poisson_model.py` — ale to opcjonalne dopracowanie, drugorzędne wobec
   pełnego modelu rożnych z Kroku 4

## Krok 6: Faule, kartki i profil dyscyplinarny (drużynowy i indywidualny)

Faule nie są już tylko liczbą na końcu raportu — to wejście do modelu, nie
tylko jego wyjście. Ten krok ma dwie warstwy (drużynową i indywidualną), a
wnioski z niego mogą zawrócić do Kroku 2 i skorygować λ goli, dokładnie tak
jak kontuzja czy mecz "o nic".

### 6a. Model drużynowy

Ta sama logika "for/against" co przy strzałach w Kroku 5:

1. Weź średnią fauli popełnionych przez drużynę A ("for") i średnią fauli
   sprowokowanych/doznanych przez drużynę B ("against", czyli ile fauli
   popełnia się na B) — połączenie tych dwóch daje oczekiwaną wartość fauli
   popełnionych przez A w tym meczu. Analogicznie dla B.
2. Zsumuj obie wartości dla łącznej liczby fauli w meczu i podaj jako
   **przedział wokół średniej**, tak jak w Kroku 5.
3. Kartki korelują z liczbą fauli i ze stylem sędziowania — jeśli sędzia
   meczu jest znany z wyprzedzeniem i łatwo dostępna jest jego średnia
   kartek/mecz, potraktuj to jako dodatkowy modyfikator (surowy sędzia
   podnosi oczekiwaną liczbę kartek, "przymykający oko" ją obniża). Jeśli tej
   informacji nie ma, pomiń ją, zamiast zgadywać. Podaj oczekiwaną liczbę
   kartek jako przedział, analogicznie do fauli.
4. Opcjonalnie, jak w Kroku 5 pkt 4, można przybliżyć rozkład fauli/kartek
   Poissonem (`poisson_model.py`) dla konkretnego % over/under — drugorzędne
   dopracowanie.

### 6b. Profil indywidualny (zawodnicy)

1. Wskaż po stronie każdej drużyny 1-3 zawodników z najwyższym wskaźnikiem
   fauli popełnionych/90 min (zwykle defensywni pomocnicy, stoperzy) — to
   oni generują największe ryzyko kartek i rzutów wolnych dla przeciwnika w
   groźnych strefach.
2. Wskaż zawodników najczęściej faulowanych (faule sprowokowane/90 min,
   zwykle kluczowi kreatorzy/dryblerzy) — to pokazuje, gdzie ich drużyna
   będzie miała okazje do rzutów wolnych w ofensywnych strefach; potraktuj to
   jako niewielki plus dla zagrożenia z rzutów wolnych/goli z ustawki tej
   drużyny, jeśli to wnosi coś istotnego do analizy.
3. Sprawdź dystans do zawieszenia za kartki (np. 4 żółte w lidze, gdzie
   zawieszenie jest przy 5) dla kluczowych zawodników z obu drużyn. Zawodnik
   grający "na kartce" tuż przed progiem zawieszenia często gra asekuracyjnie
   (mniej agresywnie w pojedynkach), co może obniżyć intensywność pressingu
   jego drużyny — albo trener może go oszczędzić/zmienić wcześniej.
4. Jeśli taki zawodnik jest niedostępny (zawieszenie, kontuzja), to powinno
   już być uwzględnione w Kroku 1 ("Kadra") — tutaj dodatkowo zaznacz, czy
   jego nieobecność zmienia profil dyscyplinarny drużyny (np. najbardziej
   faulujący stoper pauzuje = mniej fauli w tym meczu, ale potencjalnie
   więcej przegranych pojedynków 1v1).

### 6c. Zwróć wnioski do modelu bazowego

Jeśli research z 6a/6b ujawnia coś istotnego (rywal regularnie kończy mecze w
osłabieniu, kluczowy obrońca gra na zawieszeniu i będzie asekuracyjny, sędzia
wyjątkowo surowy) — wróć do Kroku 2 i skoryguj λ goli, krótko opisując w
raporcie tę korektę i jej uzasadnienie. Jeśli research nie ujawnia nic
istotnego ponad standardowe średnie, nie trzeba sztucznie szukać korekty —
wystarczy zaznaczyć, że profil dyscyplinarny obu drużyn jest w normie.

## Krok 7: Napisz raport

Użyj odpowiedniego szablonu z `references/report_templates.md`. Każdy
szablon kończy się tą samą notą:

> *Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
> finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*

Zachowaj ją w każdym raporcie.

## Krok 8: Zapisz raport do pliku Markdown

Niezależnie od tego, czy użytkownik o to poprosił, **zawsze zapisz gotowy
raport do pliku `.md`** (oprócz pokazania go w odpowiedzi) — tak, by można
było do niego wrócić bez ponownego odpytywania modelu. Zasady:

- Zapisz w katalogu `analizy/` w bieżącym katalogu roboczym (utwórz go, jeśli
  nie istnieje).
- Nazwa pliku powinna być opisowa i zawierać daty/drużyny/zakres, np.
  `Lech_Rakow_2026-08-15.md`, `Premier_League_kolejka12_2026-11-02.md`,
  `MS2026_kolejka1_grupy_A-D.md` — slug bez polskich znaków i spacji
  (podkreślenia zamiast spacji).
- Plik powinien zawierać dokładnie tę samą treść, którą pokazujesz
  użytkownikowi w odpowiedzi (włącznie z disclaimerem).
- Na końcu odpowiedzi krótko poinformuj, gdzie zapisano plik.

## Wskazówki ogólne

- **Rotacje w pucharach krajowych.** W Pucharze Króla i EFL Cup/Carabao Cup
  czołowe kluby często rotują skład (rezerwowi, młodzież), zwłaszcza we
  wczesnych rundach i gdy kolidują z ważniejszym meczem ligowym w tym
  tygodniu — to często ważniejszy czynnik niż sezonowe współczynniki
  ataku/obrony. Sprawdź zapowiedzi przedmeczowe (Krok 1) pod kątem
  zapowiadanych rotacji, zanim obniżysz λ tylko na podstawie kontuzji.
  Weryfikacja pokazała, że tego typu mecze niespodziewanie zawodzą częściej
  niż ligowe odpowiedniki (patrz Krok 2b, punkt 3) — traktuj rotację jako
  powód do realnie szerszego przedziału niepewności, nie tylko wzmianki.
- **Rożne mają pierwszeństwo.** To główna statystyka tego skilla obok wyniku
  meczu (Krok 4) — zawsze licz je pełnym modelem (λ, uzasadnienie,
  prawdopodobieństwa "przewagi rożnej" i over/under), umieszczaj wysoko w
  raporcie, i nie redukuj ich do jednej linijki z przedziałem, jeśli dane na
  to pozwalają. Gole i 1X2 pozostają ważne, ale rożne nie są już dodatkiem —
  są współrzędnym celem analizy.
- **Faule i dyscyplina to wejście do modelu, nie tylko opis meczu.** Profil
  fauli i kartek — drużynowy i indywidualny (Krok 6) — to jedno z wejść do
  jakościowej korekty λ w Kroku 2, na równi z kontuzjami i kontekstem
  meczowym. Zawsze sprawdź, czy coś z Kroku 6 (zawodnik na zawieszeniu,
  drużyna często kończąca mecze w osłabieniu, wyjątkowo surowy sędzia)
  uzasadnia korektę — a jeśli tak, opisz ją tak samo jawnie jak inne korekty
  jakościowe, zamiast zostawiać faule wyłącznie jako osobną tabelkę na końcu
  raportu.
- **Transparentność ponad pewność siebie.** Jeśli model bazowy mówi co
  innego niż "oko ekspackie" (np. drużyna w kryzysie formy ma wciąż mocne
  liczby sezonowe), napisz o tym wprost — to jest właśnie wartościowa
  informacja dla użytkownika, nie błąd do ukrycia.
- **Nie zaokrąglaj kontekstu do zera.** Nawet krótka wzmianka o tym, że
  kluczowy obrońca wraca z zawieszenia, może być ważniejsza niż 0.1 różnicy
  w λ.
- **Język raportu** dopasuj do języka użytkownika (domyślnie polski, bo to
  główny kontekst tego skilla, ale jeśli użytkownik pisze po angielsku,
  odpowiadaj po angielsku).
- **Nie zmyślaj nazwisk zawodników, składów ani statystyk.** Jeśli czegoś nie
  udało się znaleźć, powiedz to wprost.
