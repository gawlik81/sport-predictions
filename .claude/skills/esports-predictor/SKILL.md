---
name: esports-predictor
description: Ekspert od statystyk e-sportowych: zbiera aktualne dane (forma, rankingi, statystyki map/stron, map pool i veto, meta patcha, draft, zmiany składów/stand-iny, H2H, zapowiedzi) i szacuje prawdopodobieństwa - zwycięzca serii, dokładny wynik serii, handicap mapowy (±1.5), total map, zwycięzca mapy/gry, w CS2 total rund i handicap rundowy (kluczowy nacisk, model rundowy MR12 z dogrywkami), w LoL/Dota 2 total killi i czas gry - dla CS2 (Major, IEM, BLAST, ESL Pro League, PGL), LoL (Worlds, MSI, LCK, LPL, LEC, LTA, LCP) i Dota 2 (TI, Riyadh/EWC, PGL, DreamLeague, BLAST Slam, ESL One), na żądanie także tier-2. Użyj zawsze, gdy użytkownik pyta o typowanie/prognozę meczu e-sportowego, szanse drużyny, handicap map, total rund/killi, "value bet", fair odds/kursy, przegląd dnia turnieju lub analizę formy drużyny/gracza - nawet bez słowa "e-sport", gdy padają tylko nazwy drużyn (np. NAVI, Vitality, T1, Gen.G, Team Spirit), graczy, turnieju lub gry.
---

# Esports Predictor

Ten skill łączy dwie rzeczy: **research** (aktualne dane statystyczne i
medialne) i **model statystyczny** (hierarchiczny model runda→mapa→seria
dla CS2 oraz gra→seria dla LoL i Dota 2, plus rozkłady totali killi/czasu
gry). Same liczby z modelu nie wystarczą. Stand-in za kluczowego gracza,
nowy patch zmieniający metę albo mecz "o nic" w fazie grupowej potrafią
zmienić obraz bardziej niż jakikolwiek rating z ostatnich 3 miesięcy.
Dlatego każdy raport łączy twarde dane z jakościową korektą na podstawie
świeżych informacji.

Skill jest zbudowany na tym samym szkielecie co `football-predictor` i
`tennis-predictor`: odpowiednikiem λ goli / p_serve jest tu
**p_map** (szansa drużyny A na wygranie pojedynczej mapy/gry), a
odpowiednikiem rożnych / total gemów jest **total rund w CS2** (pełny
model rundowy) oraz **handicap mapowy** we wszystkich trzech grach.

## Krok 0: Ustal zakres i format

Najpierw ustal grę, turniej i scenariusz, potem wybierz szablon z
`references/report_templates.md`:

1. **Pojedynczy mecz (seria)**: najczęstszy przypadek, pełny raport.
2. **Przegląd dnia turnieju**: kilka serii naraz, wersja skrócona.
3. **Forma drużyny/gracza**: analiza opisowa bez tabel prawdopodobieństw.
4. **Mecz fazy pucharowej / finał dużego turnieju** (Major, Worlds, TI,
   playoffy): jak (1) plus sekcja o stawce, formacie i drabince.

Prośbę niejednoznaczną (np. "co myślisz o Vitality vs NAVI") traktuj
domyślnie jako pojedynczy mecz z pełnym raportem.

**Format serii zawsze weryfikuj researchem, nie zakładaj z pamięci.**
Formaty zmieniają się między turniejami, a nawet między fazami jednego
turnieju:
- BO1 (fazy szwajcarskie CS2, część lig LoL), BO2 (grupy Dota 2, remis 1-1
  możliwy), BO3, BO5 (finały, playoffy LoL).
- Advantage w finale górnej drabinki (np. drużyna z górnej drabinki startuje
  od 1-0 w wielkim finale Doty). Skrypt tego nie modeluje wprost; policz
  serię od stanu 1-0 ręcznie przez `--best-of` i odpowiednio krótszą listę
  map albo opisz to jakościowo.
- **LoL: fearless draft** (bohater użyty w serii jest zablokowany w
  kolejnych grach) działa w wielu ligach od 2025. Zweryfikuj, czy obowiązuje
  w danym turnieju. Jeśli tak, głębokość puli bohaterów zaczyna się liczyć
  w grach 3-5.
- **CS2: MR12** (do 13 rund), dogrywka MR3 przy 12-12 (do 4 w dogrywce,
  kolejna dogrywka przy 3-3). Sprawdź w regulaminie turnieju, zwłaszcza
  przy mniejszych rozgrywkach online.

## Krok 1: Zbierz dane (WebSearch / WebFetch)

Korzystaj z `references/data_sources.md`: tam jest lista serwisów per gra
i typ danych oraz wskazówki, jak formułować zapytania. W skrócie
potrzebujesz:

**Wspólne dla wszystkich gier**
- **Skład (priorytet)**: aktualna piątka obu drużyn, stand-iny, świeże
  transfery, zmiana trenera/IGL-a. W e-sporcie to odpowiednik kontuzji w
  piłce, tylko częstszy i bardziej wpływowy.
- **Rating/ranking**: ranking HLTV/Valve (CS2), ratingi Elo/Glicko drużyn
  (Dota: datdota; LoL: zestawienia Elo z gol.gg/Oracle's Elixir, jeśli
  dostępne), pozycja w lidze.
- **Forma**: ostatnie 10-15 serii i 20-30 map/gier, najlepiej z podziałem
  na LAN/online i na poziom rywali (tier-1 vs tier-2).
- **H2H**: ostatnie bezpośrednie serie, z zastrzeżeniem zmian składów od
  tamtego czasu.
- **Kontekst**: stawka (awans, eliminacja, mecz "o nic"), LAN vs online,
  podróż i jet lag (turnieje w Azji/Arabii Saudyjskiej), bootcamp, napięty
  kalendarz (kilka turniejów z rzędu).
- **Świeże artykuły** (ostatnie kilka dni): wywiady, zapowiedzi, komunikaty
  o składach, informacje o problemach zdrowotnych/wizowych.

**CS2 (priorytet: mapy i rundy)**
- Pula map obu drużyn: win rate per mapa (ostatnie 3 miesiące), liczba
  rozegranych map, **stałe bany i picki** (do przewidzenia veto).
- Statystyki stron: % rund wygranych po CT i po T per mapa, % pistoletówek.
- Średnia rund na mapę dla obu drużyn (czy ich mapy są zwykle wyrównane,
  czy jednostronne).
- Aktualna pula map aktywnego pooli (Valve zmienia ją co jakiś czas).

**LoL**
- Win rate po stronie niebieskiej/czerwonej, GD@15 (różnica złota w 15.
  min), first blood/first dragon/first tower %, średni czas gry, kille na
  minutę (KPM), liczba killi na grę (za i przeciw).
- Patch turnieju i stan mety; pule bohaterów kluczowych graczy (ważne przy
  fearless draft).

**Dota 2**
- Win rate Radiant/Dire, średni czas gry, kille na grę, styl (tempo/
  late-game), pierwsza krew, Roshan.
- Patch turnieju (duże patche literowe potrafią wywrócić hierarchię),
  pule bohaterów i draft (first pick vs last pick).

Nie trzeba przeszukiwać każdego źródła dla każdego meczu. Dociągaj kolejne
tam, gdzie są luki, **szczególnie dla statystyk map w CS2**: to kluczowy
input tego skilla. Jeśli nie da się znaleźć danych (tier-2/tier-3, nowy
skład bez historii), **zaznacz to wprost w raporcie** zamiast zmyślać
liczby. Szeroki, ale uczciwy przedział jest lepszy niż fałszywa precyzja.

## Krok 2: Oszacuj p_map (model bazowy)

p_map to szansa drużyny A na wygranie pojedynczej mapy (CS2) lub gry
(LoL/Dota). Buduj ją warstwami:

1. **Punkt wyjścia z ratingu.** Jeśli masz ratingi Elo/Glicko w tej samej
   skali, przelicz je skryptem:
   ```bash
   python3 scripts/esports_model.py elo --rating-a 1720 --rating-b 1610
   ```
   Jeśli nie ma ratingu, oszacuj p_map z rankingu, bilansu map z ostatnich
   3 miesięcy przeciw podobnym rywalom i win rate'u w H2H. Zaznacz, że to
   luźniejsze oszacowanie.
2. **CS2: p_map osobno dla każdej mapy.** Przewidź veto (w BO3 zwykle: ban
   A, ban B, pick A, pick B, ban, ban, decider). Dla każdej prawdopodobnej
   mapy skoryguj bazowe p_map o różnicę win rate'ów obu drużyn na tej mapie,
   ważoną liczbą rozegranych map (5 map to mała próba, nie przesuwaj o
   więcej niż kilka pp). Pick drużyny to zwykle jej najlepsza mapa, więc
   p_map na picku A jest wyższe niż bazowe. Jeśli veto jest niepewne, podaj
   2-3 scenariusze albo uśrednij.
3. **LoL/Dota: strona i draft.** Strona niebieska w LoL i Radiant w Docie
   mają zwykle niewielką przewagę (sprawdź aktualne dane dla patcha). Przy
   serii zmieniającej strony (przegrany wybiera stronę) efekt się uśrednia,
   więc zwykle wystarczy jedno p_map dla całej serii. Przy fearless draft
   obniż p_map w grach 4-5 drużynie z płytszą pulą bohaterów.
4. **Korekty jakościowe** (opisz każdą w raporcie):
   - stand-in za kluczowego gracza: zwykle -5 do -12 pp p_map (więcej za
     IGL-a/snajpera w CS2 lub mid/carry w LoL/Dota, mniej za support);
   - świeża zmiana składu (<1 miesiąc): szerszy przedział, lekka korekta w
     dół, bo zgranie jest jeszcze słabe;
   - nowy duży patch (LoL/Dota): zmniejsz wagę formy sprzed patcha, spłaszcz
     p_map w stronę 50%;
   - LAN vs online: drużyny z dobrymi wynikami tylko online często tracą na
     LAN-ie;
   - jet lag i napięty kalendarz: niewielka korekta w dół;
   - motywacja: mecz "o nic" (awans już zapewniony), wyścig o punkty RMR/
     kwalifikację.

Krótko opisz w raporcie, jakie korekty zastosowałeś i dlaczego. Często to
najważniejsza część analizy.

## Krok 2b: Dyscyplina pewności (wstępne reguły kalibracji)

Poniższe reguły to **wstępne założenia** przeniesione z weryfikacji skilli
piłkarskiego i tenisowego oraz ze specyfiki e-sportu. Nie zostały jeszcze
zweryfikowane na wynikach e-sportowych. Po pierwszej rundzie weryfikacji
zapisz wnioski w `analizy/Weryfikacja_esport_...md` i zaktualizuj tę sekcję,
tak jak w pozostałych skillach.

Każdy sygnał ostrzegawczy musi **realnie obniżyć liczbę użytą do rankingu
pewności**. Sama wzmianka w opisie nie wystarcza.

1. **BO1 to rzut monetą z przewagą.** Nawet przy dużej różnicy klas nie
   dawaj faworytowi w BO1 więcej niż ~80% (CS2) lub ~82% (LoL/Dota). Upsety
   w BO1 są w e-sporcie znacznie częstsze niż w BO3.
2. **Stand-in lub zmiana składu u faworyta.** Obniż p_map (Krok 2) i nie
   umieszczaj takiego meczu wyżej niż ~75% w rankingu top-N.
3. **Pierwszy mecz po długiej przerwie (≥3 tygodnie) przeciw drużynie w
   rytmie meczowym.** Obniż p_map faworyta o 3-5 pp (analogia do tenisowej
   reguły o wolnym losie). Dotyczy też pierwszego meczu na nowym patchu.
4. **Kryzys faworyta to trafna flaga.** Seria przegranych serii, konflikt w
   drużynie, publiczne plotki o zmianach składu: traktuj taki mecz jak
   bliższy 50/50, niezależnie od rankingu.
5. **Kryzys underdoga podnosi ryzyko niespodzianki tylko w określonych
   przypadkach** (świeży nowy gracz/trener = "nowa miotła", mecz o
   przetrwanie w turnieju). Zwykła słaba forma underdoga nie jest powodem
   do obniżania faworyta (reguła z weryfikacji piłkarskiej).
6. **Model vs rynek.** Gdy p_series z modelu odbiega od kursów rynkowych
   (po zdjęciu marży) o ponad 10 pp, zaznacz to wprost i szukaj przyczyny
   (skład? patch? informacja, której nie masz?). Nie zakładaj, że model ma
   rację. Rynki e-sportowe szybko reagują na informacje o składach.
7. **Tier-2 i niżej: bez totali w rankingu.** Gdy p_map lub p_round są
   szacowane z rankingu (brak solidnych statystyk map/stron), pokaż total
   rund/killi z zastrzeżeniem, ale **nie umieszczaj go w rankingu
   najlepszych typów** (reguła z tenisowego total gemów).
8. **Tier-3 i ryzyko integralności.** W bardzo niskich rozgrywkach zdarzały
   się ustawione mecze. Przy nietypowych ruchach kursów i nieznanych
   drużynach zaznacz to ryzyko i nie umieszczaj takiego meczu w top-N.
9. **Dla każdego faworyta w zestawieniu top-N wykonaj osobne zapytanie
   „[drużyna] roster / stand-in [miesiąc rok]”.** Nie polegaj na tym, że
   ogólny research formy wyłapie zmianę składu.
10. **Filtr kursów:** w rankingach top-N pokazuj tylko typy z fair odds
    >1.15 (stała preferencja użytkownika, jak w pozostałych skillach). Gdy
    zwycięzca serii odpada, szukaj innego rynku z tego meczu (handicap -1.5,
    total map, total rund).

## Krok 3: Policz serię (wszystkie gry)

Użyj `scripts/esports_model.py series`. W CS2 podaj p_map per mapa w
kolejności veto (pick A, pick B, decider):

```bash
python3 scripts/esports_model.py series --map-probs 0.68,0.47,0.58 --best-of 3
```

W LoL/Dota zwykle jedno p_map dla całej serii:

```bash
python3 scripts/esports_model.py series --p-map 0.62 --best-of 5
python3 scripts/esports_model.py series --p-map 0.55 --best-of 2   # grupy Doty, remis możliwy
```

Skrypt zwraca JSON z prawdopodobieństwami i fair odds (1/p) dla:
zwycięzcy serii (w BO2 także remisu 1-1), dokładnego wyniku serii, totalu
map (np. Over/Under 2.5 w BO3, 3.5 i 4.5 w BO5), handicapu mapowego
(A -1.5 = A wygrywa 2-0 w BO3; A +1.5 = A wygrywa co najmniej jedną mapę)
oraz szansy rozegrania każdej mapy (`p_map_played`, przydatne do typów na
konkretną mapę 3). Przepisz liczby do tabel, nie licz ręcznie.

Pamiętaj, że BO3 i BO5 **wzmacniają** przewagę faworyta względem pojedynczej
mapy (p_map 0.60 daje ok. 65% w BO3 i ok. 68% w BO5). Dlatego błąd w p_map
przenosi się na serię z nawiązką. Korekty z Kroku 2/2b wprowadzaj na
poziomie p_map, a nie na końcowym wyniku serii.

## Krok 4: Total rund i handicap rundowy w CS2 (priorytet)

**Total rund to główny rynek statystyczny tego skilla w CS2**, tak jak
rożne w piłce i total gemów w tenisie. Traktuj go z pełnym rygorem modelu.

1. Dla każdej prawdopodobnej mapy zamień p_map na prawdopodobieństwo
   wygrania rundy. Najprościej: niech skrypt sam to rozwiąże:
   ```bash
   python3 scripts/esports_model.py cs-map --p-map-target 0.64 --ct-bias 0.03 \
       --round-lines 19.5,20.5,21.5,22.5 --handicap-lines 2.5,3.5,4.5
   ```
   Jeśli masz statystyki stron obu drużyn na tej mapie, podaj je wprost
   (`--p-a-ct 0.58 --p-a-t 0.47`) zamiast `--p-map-target`.
2. `--ct-bias` opisuje, na ile mapa sprzyja stronie CT (win rate CT w
   rundach minus 0.5). Orientacyjne wartości są w
   `references/data_sources.md`, ale zawsze sprawdź aktualne dane
   (zmieniają się z aktualizacjami map).
3. **Obowiązkowa korekta na ekonomię.** Model zakłada stałe p rundy i nie
   widzi ekonomii (pistoletówki, eco, force-buy), która w praktyce tworzy
   serie rund i czyni mapy bardziej jednostronnymi. Dlatego model
   **zawyża** oczekiwany total rund (o ok. 0,5-1,5 rundy) i szansę na
   dogrywkę. Przy typach Over rund żądaj wyraźnego marginesu nad linią
   (np. model ≥60% na Over 21.5, zanim uznasz to za typ), a oczekiwany total
   w raporcie podawaj po korekcie w dół, z adnotacją.
4. Uzupełnij kontekst jakościowy: drużyny z silną stroną CT i słabym T
   dają więcej wyrównanych połówek (więcej rund); duża różnica klas i
   silne pistoletówki faworyta dają mapy typu 13-5 (mniej rund).
5. Dla serii podaj total rund dla mapy 1 i 2 (pewnie rozegranych) oraz
   ewentualnie decidera z adnotacją `p_map_played`.

## Krok 5: LoL i Dota 2 — total killi i czas gry

1. **Oczekiwane kille na grę**: połącz średnią killi drużyny A (za) z
   średnią killi traconych przez B (przeciw), analogicznie dla B, i zsumuj.
   Skoryguj o styl (tempo vs skalowanie), patch (niektóre patche podnoszą
   KPM) i różnicę klas (mecze jednostronne w LoL są zwykle krótsze i mają
   mniej killi przegrywającego; w Docie jednostronne stompy bywają krwawe).
2. **Odchylenie standardowe**: z danych historycznych, a jeśli ich brak,
   przyjmij ok. 25-30% średniej. Policz O/U:
   ```bash
   python3 scripts/esports_model.py totals --mean 27.5 --sd 7.5 --lines 24.5,26.5,28.5
   ```
3. **Czas gry** (minuty): średnia obu drużyn, skorygowana o różnicę klas
   (duża przepaść = krótsze gry) i patch:
   ```bash
   python3 scripts/esports_model.py totals --mean 32.5 --sd 5.5 --continuous --lines 30.5,32.5
   ```
4. Podaj wyniki jako tabelę O/U plus przedział (np. "22-32 kille, średnio
   ~27"). To statystyki drugorzędne wobec zwycięzcy i handicapu mapowego,
   ale przy wyrównanych seriach bywają lepszym rynkiem.
5. Opcjonalnie dodaj rynki "first blood", "first dragon/Baron" (LoL),
   "first Roshan" (Dota) jako proste procenty z danych sezonowych obu
   drużyn (średnia z % drużyny A i 1 − % drużyny B), bez modelu.

## Krok 6: Gracze (opcjonalnie, gdy użytkownik pyta)

Kille gracza na mapę (CS2) lub K/D/A na grę (LoL/Dota): weź średnią gracza
z ostatnich 2-3 miesięcy, przelicz na oczekiwaną liczbę map/rund w tej
serii (z Kroku 3-4) i skoryguj o siłę rywala. Podaj przedział i ewentualnie
O/U przez `totals` (kille gracza są mocno rozproszone, sd ≈ 30-40%
średniej). Rola gracza (entry, AWP, support) mocno zmienia rozkład.

## Krok 7: Napisz raport

Użyj szablonu z `references/report_templates.md`. Każdy szablon kończy się
tą samą notą:

> *Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
> finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*

Zachowaj ją w każdym raporcie.

## Krok 8: Zapisz raport do pliku Markdown

Niezależnie od tego, czy użytkownik o to poprosił, **zawsze zapisz gotowy
raport do pliku `.md`** (oprócz pokazania go w odpowiedzi):

- Katalog `analizy/` w bieżącym katalogu roboczym (utwórz, jeśli nie
  istnieje).
- Nazwa opisowa, z grą, drużynami/turniejem i datą, np.
  `CS2_Vitality_NAVI_IEM-Cologne_2026-08-10.md`,
  `LoL_Worlds2026_Swiss_dzien1_2026-10-05.md`,
  `Dota2_TI2026_Spirit_Falcons_2026-09-12.md`. Bez polskich znaków i spacji
  (podkreślenia zamiast spacji).
- Plik zawiera dokładnie tę samą treść co odpowiedź (włącznie z
  disclaimerem).
- Na końcu odpowiedzi krótko poinformuj, gdzie zapisano plik.

## Wskazówki ogólne

- **Skład ponad wszystko.** W e-sporcie jeden gracz to 20% drużyny. Zawsze
  potwierdź aktualne piątki tuż przed meczem (Liquipedia, oficjalne social
  media drużyn). Stand-in ogłoszony w dniu meczu zmienia typ bardziej niż
  cokolwiek innego.
- **Patch i pula map zmieniają wszystko.** Forma sprzed dużego patcha
  (LoL/Dota) lub sprzed zmiany active duty (CS2) ma ograniczoną wartość.
- **Handicap mapowy i total rund mają pierwszeństwo obok zwycięzcy.** Przy
  wyraźnych faworytach zwycięzca serii często ma fair odds ≤1.15; wtedy
  najciekawsze rynki to -1.5 map i total rund.
- **Transparentność ponad pewność siebie.** Jeśli model mówi co innego niż
  ranking albo rynek, napisz to wprost.
- **Nie zaokrąglaj kontekstu do zera.** Informacja o bootcampie, chorobie
  gracza czy problemach z wizą może ważyć więcej niż 3 pp różnicy w
  ratingu.
- **Język raportu** dopasuj do języka użytkownika (domyślnie polski).
- **Nie zmyślaj drużyn, składów, wyników ani terminów.** Jeśli nie udało
  się potwierdzić, że mecz się odbędzie (drabinka nieogłoszona, drużyna
  rozwiązana, gracz na emeryturze lub w innej drużynie), powiedz to wprost.
