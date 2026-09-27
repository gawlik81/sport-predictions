# Dzisiejsze mecze — 18.09.2026

Cztery mecze piątkowe w zasięgu skilla: **Championship** (Bristol City – Watford),
**Eredivisie** (FC Groningen – PEC Zwolle) oraz **Ekstraklasa, 9. kolejka**
(Widzew Łódź – Wieczysta Kraków, Wisła Kraków – Śląsk Wrocław). Dla każdego
meczu policzono pełny model Poissona dla goli i rożnych (λ + uzasadnienie),
z korektami jakościowymi z researchu i kalibracją z Kroku 2b (remis i
"odwrotny wynik" jako porównywalne ryzyka w przedziale 50-85% pewności,
korekta w dół gdy underdog jest w realnym kryzysie a nie tylko słabszy
klasowo).

**Uwaga o jakości danych dla rożnych**: żadna z trzech lig (Championship,
Eredivisie, Ekstraklasa) nie ma w pełni publicznie dostępnego rozbicia
rożnych dom/wyjazd per drużyna z tego sezonu — FootyStats ma te dane za
paywallem dla Championship, dla Eredivisie i Ekstraklasy próbki per drużyna
są bardzo małe (kilkanaście z kilkudziesięciu-kilkuset rozegranych meczów
ligi) i dały niewiarygodnie niskie liczby przy weryfikacji krzyżowej. Dlatego
λ rożnych we wszystkich czterech meczach oparto o **średnią ligową** (przybliżoną
z dostępnych źródeł) skorygowaną jakościowo o styl gry i dominację
terytorialną, a nie o twarde współczynniki per drużyna — zaznaczone wprost
przy każdym meczu.

---

## NAJPEWNIEJSZE TYPY DNIA (ranking wg prawdopodobieństwa modelu)

| # | Mecz | Typ | Prawdopodobieństwo | Kurs uczciwy | Uzasadnienie |
|---|---|---|---|---|---|
| 1 | Widzew Łódź – Wieczysta Kraków | Over 1,5 gola | **88,8%** | 1,13 | Obie drużyny mają dziurawe defensywy (Widzew 1,38 GA/mecz, Wieczysta 2,14 GA/mecz) — rynek odporny na to, kto wygra |
| 2 | FC Groningen – PEC Zwolle | Over 1,5 gola | **85,3%** | 1,17 | Zwolle traci bramki seryjnie (2,83/mecz, w tym 0:7 z Feyenoordem), Groningen strzela regularnie w każdym meczu (BTTS 100%) |
| 3 | Wisła Kraków – Śląsk Wrocław | Wisła wygrywa (1) | **70,5%** | 1,42 | Wisła: komplet zwycięstw u siebie (4/4, 8:2 w bramkach), Śląsk: 0 zwycięstw na wyjeździe (0-1-3) — ⚠ mimo to przedział 50-85%, patrz sekcja meczu |
| 4 | Bristol City – Watford | Over 1,5 gola | **70,2%** | 1,42 | Obie drużyny tracą gole w niemal każdym meczu sezonu (City 8/8, Watford 8/9 wg mediów) |
| 5 | FC Groningen – PEC Zwolle | Groningen wygrywa (1) | **61,3%** | 1,63 | Wspiera to samo co #2, ale ⚠ Zwolle ma lepszy bilans na wyjeździe niż u siebie w tym sezonie — realne ryzyko niespodzianki, patrz sekcja meczu |

Żaden mecz dnia nie ma ekstremalnej przepaści jakościowej między "zdrowymi"
klubami (jak np. lider vs outsider w Top 5) — wszystkie typy 1X2 powyżej
mieszczą się w przedziale 50-75%, więc zgodnie z kalibracją z Kroku 2b
**remis i zwycięstwo underdoga to porównywalne ryzyka** przy każdym z nich;
opisano je przy każdym meczu osobno.

---

# Bristol City vs Watford
**Rozgrywki:** EFL Championship | **Termin:** piątek 18.09.2026, 20:00 (Ashton Gate, Bristol) | **Ranga meczu:** środek tabeli (13. vs 17. miejsce)

## Kontekst i forma
- **Forma Bristol City** (7 meczów ligowych): 3W-1D-3L, 10:12 bramek (1,43 GF / 1,71 GA na mecz). Ostatnio seria 2 porażek z rzędu, w tym 0:1 z Lincoln City w środku tygodnia (przeciwnik z League One — prawdopodobnie puchar ligi, nie liga, ale sygnalizuje zmęczenie/rotacje). xG 1,46 / xGA 1,39 — wyniki mniej więcej odpowiadają jakości gry.
- **Forma Watford** (7 meczów ligowych): 2W-2D-3L, 7:9 bramek (1,00 GF / 1,29 GA). 17. miejsce. xG 1,30 / xGA 1,61.
- **Kluczowy sygnał**: Watford **nie wygrało na wyjeździe w 9 kolejnych meczach** i strzeliło zaledwie **1 gola w 3 ligowych meczach wyjazdowych** tego sezonu (0,33/mecz) — to bardzo silny i spójny sygnał (nie pojedynczy wynik), więc potraktowano go jako realną korektę, nie tylko ciekawostkę.
- **Kadra**: Bristol City — jedyny znaczący brak to Luke McNally (kontuzja więzadeł, poza grą od stycznia 2025, długoterminowo). Watford — kilka nowych kontuzji po ostatnim meczu ze Stoke City (konkretne nazwiska niepotwierdzone w dostępnych źródłach — zaznaczam brak precyzji zamiast zgadywać).
- **H2H**: Bristol City rozbiło Watford 5:1 w styczniu 2026 na tym samym stadionie, Watford odpowiedziało 2:1 w lutym 2026 na wyjeździe — starcia bezpośrednie nie dają jednoznacznego wzorca.

## Model bazowy (oczekiwane gole)
Championship, przybliżona średnia ligowa: ~2,60 gola/mecz (gospodarze ~1,43, goście ~1,17;
szacunek orientacyjny, nie znaleziono precyzyjnej oficjalnej średniej sezonu 2026/27).
Siłę ataku/obrony policzono jako średnią ważoną (60% sezon ogółem, dane home/away zbyt
małe próby — 3-4 mecze — by liczyć je samodzielnie), następnie skorygowano:
- Watford: **-15% do siły ataku na wyjeździe** za udokumentowaną, wieloźródłową słabość
  wyjazdową (9 meczów bez zwycięstwa, 1 gol w 3 meczach)
- Bristol City: lekka korekta w dół za serię 2 porażek z rzędu, ale bez przesady — jedna
  z porażek to prawdopodobnie mecz pucharowy, nie ligowy

λ(Bristol City) = **1,45** | λ(Watford) = **1,00**

## Model rożnych
Brak wiarygodnego rozbicia dom/wyjazd per drużyna (FootyStats płatne dla Championship).
Jedyny znaleziony punkt odniesienia: mecze z udziałem Bristol City mają średnio ~9,95
rożnych łącznie w sezonie — użyto go jako kotwicy dla łącznej wartości, z lekkim
przechyłem w stronę gospodarza (typowe dla ligi angielskiej).

λ_rożne(Bristol City) = **5,4** | λ_rożne(Watford) = **4,6** — **oszacowanie szerokie, nie
oparte o pełne dane sezonowe obu drużyn.**

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Bristol City wygrywa | 47,4% | 2,11 |
| Remis | 26,5% | 3,78 |
| Watford wygrywa | 26,0% | 3,84 |

*Żaden wynik nie przekracza 50% — mecz wyrównany mimo przewagi Bristol City w modelu;
obie drużyny słabe akurat na swoim terenie (City: 1W-2L u siebie w 3 meczach, Watford:
fatalny bilans wyjazdowy), co ogranicza pewność typu 1X2 bardziej niż standardowo.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Bristol City więcej rożnych | 53,7% | 1,86 |
| Remis rożny | 12,4% | 8,06 |
| Watford więcej rożnych | 33,9% | 2,95 |
| Over 8,5 | 66,7% | 1,50 |
| Over 9,5 | 54,2% | 1,84 |
| Over 10,5 | 41,7% | 2,40 |

*Przewaga rożna gospodarza blisko rzutu monetą — spójne z ogólnie wyrównanym charakterem
meczu; dane wejściowe niepewne (patrz wyżej), więc traktuj te liczby jako orientacyjne.*

### Najbardziej prawdopodobne wyniki (gole)
1-0 i 1-1 (po 12,5%), 2-0 i 2-1 (po 9,1%), 0-0 i 0-1 (po 8,6%)

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 70,2% | 1,42 |
| Over 2,5 | 44,3% | 2,26 |
| BTTS - Tak | 48,3% | 2,07 |

*Obie drużyny tracą bramki praktycznie w każdym meczu sezonu (City: gol stracony w 8/8
meczów wg mediów, Watford: 8/9) — stąd wysoki Over 1,5 mimo niskiego BTTS/Over 2,5.*

### Strzały i strzały celne
Brak precyzyjnych, aktualnych danych strzałów celnych dla obu drużyn z tego sezonu w
dostępnych źródłach — orientacyjnie 10-13 strzałów na drużynę (typowe dla Championship),
Bristol City z lekką przewagą objętości gry (561 strzałów w poprzednim sezonie, ~12/mecz).

### Faule i kartki
Brak szczegółowych, aktualnych danych fauli/kartek per drużyna i per zawodnik w dostępnych
źródłach dla tego meczu — nie znaleziono wiarygodnych liczb, więc pomijam zamiast zgadywać.
Nic w researchu nie wskazuje na nietypowy profil dyscyplinarny żadnej ze stron.

## Podsumowanie
Mecz dwóch drużyn w słabej, ale symetrycznej formie — Bristol City ma przewagę jako
gospodarz i w modelu bazowym, ale to nie jest pewniak: sam broni się słabo u siebie, a
Watford, mimo katastrofalnej formy wyjazdowej, potrafi strzelać (BTTS 48%, Over 1,5 na
poziomie 70% to najsolidniejszy rynek dnia dla tego meczu). Rożne wypadają blisko remisowo
i przy niepewnych danych wejściowych nie polecam ich jako mocnego typu tego meczu.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani
zachęty do zakładów. Graj odpowiedzialnie.*

---

# FC Groningen vs PEC Zwolle
**Rozgrywki:** Eredivisie | **Termin:** piątek 18.09.2026, 20:00 (Euroborg, Groningen) | **Ranga meczu:** dolna połowa tabeli (9. vs 16. miejsce)

## Kontekst i forma
- **Forma Groningen** (6 meczów): 8 pkt, 9. miejsce, seria 4 meczów bez zwycięstwa (ostatnio
  remis 1:1 z Go Ahead Eagles). Gole: 2,00 GF / 2,17 GA na mecz. xG 1,61 / xGA 1,82 — obie
  drużyny (Groningen w każdym swoim meczu) mają BTTS 100% w tym sezonie.
- **Forma PEC Zwolle** (6 meczów): 4 pkt, 16. miejsce. Gole: 1,00 GF / 2,83 GA na mecz —
  najgorsza defensywa w tej parze, w tym dotkliwe 0:7 u siebie z Feyenoordem w ostatniej
  kolejce. xG 1,22 / xGA 2,27.
- **Ciekawy niuans**: Zwolle ma w tym sezonie **lepszy bilans na wyjeździe (1W-1D, ~1,33
  pkt/mecz) niż u siebie (0-0-3, 0 pkt/mecz)** — klęska z Feyenoordem to skrajny wynik u
  siebie, nie na wyjeździe, więc nie należy go wprost ekstrapolować na dzisiejszy mecz
  wyjazdowy. Zastosowano złagodzenie (shrinkage) siły obronnej Zwolle z tego powodu.
- **Kadra**: Groningen bez Stije Resinka (kontuzja). Zwolle bez kilku zawodników: Filip
  Krastev, Ryan Thomas, Sherel Floranus, Younes Namli — realne osłabienie kadrowe drużyny
  broniącej się i tak najsłabiej w lidze.
- **H2H**: Groningen prowadzi 11-8 (7 remisów) w 26 dotychczasowych starciach, ostatni mecz
  (listopad 2025) zakończył się remisem 2:2.

## Model bazowy (oczekiwane gole)
Eredivisie, przybliżona średnia ligowa ~3,00 gola/mecz (gospodarze ~1,62, goście ~1,38 —
liga tradycyjnie ofensywna; szacunek orientacyjny). Siłę ataku/obrony policzono z sezonowych
GF/GA, z shrinkage (30% wagi w stronę średniej ligowej) ze względu na małą próbę (6 meczów)
i wspomniany wyżej outlier 0:7 w defensywie Zwolle.

λ(Groningen) = **2,25** | λ(Zwolle) = **1,15**

## Model rożnych
Liga: ~5,3 rożnego/drużynę/mecz w sezonie 2026/27 (≈10,3-10,6 łącznie), bez wiarygodnego
rozbicia per drużyna dla obu klubów w dostępnych źródłach. Groningen jako gospodarz
dominujący terytorialnie (więcej posiadania, atakująca postawa) dostaje przechył w górę.

λ_rożne(Groningen) = **5,8** | λ_rożne(Zwolle) = **4,5** — **oszacowanie szerokie**, oparte
o średnią ligową i styl gry, nie o twarde dane per drużyna.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Groningen wygrywa | 61,3% | 1,63 |
| Remis | 19,5% | 5,14 |
| Zwolle wygrywa | 18,4% | 5,45 |

*⚠ 61,3% mieści się w przedziale 50-85% z Kroku 2b — zarówno remis, jak i niespodzianka
Zwolle to realne, porównywalne ryzyka (nie tylko remis). Zwolle nie jest w pełnym "kryzysie
kryzysowym" (brak zmiany trenera), ale ma osłabioną kadrę i traumatyczny ostatni wynik u
siebie — nie stosuję dodatkowej korekty w dół poza już wykonanym shrinkage λ, ale nie
polecam tego typu jako "pewniaka".*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Groningen więcej rożnych | 59,7% | 1,67 |
| Remis rożny | 11,6% | 8,59 |
| Zwolle więcej rożnych | 28,6% | 3,50 |
| Over 8,5 | 70,0% | 1,43 |
| Over 9,5 | 57,9% | 1,73 |
| Over 10,5 | 45,4% | 2,20 |

### Najbardziej prawdopodobne wyniki (gole)
2-1 (9,7%), 1-1 (8,6%), 2-0 (8,5%), 1-0 (7,5%), 3-1 (7,3%)

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 85,3% | 1,17 |
| Over 2,5 | 66,0% | 1,51 |
| BTTS - Tak | 60,5% | 1,65 |

*Najmocniejszy rynek meczu — Zwolle nie utrzymało czystego konta w żadnym z 6 meczów
(0% clean sheets), a Groningen strzela w każdym swoim spotkaniu.*

### Strzały i strzały celne
Brak precyzyjnych danych z dostępnych źródeł — orientacyjnie Groningen 11-14 strzałów,
Zwolle 8-11 (defensywa Zwolle ustawia się nisko po serii ciężkich porażek).

### Faule i kartki
Brak szczegółowych danych per zawodnik w dostępnych źródłach. Drużynowo nic nie wskazuje na
nietypowy profil dyscyplinarny — nie stosuję korekty.

## Podsumowanie
Groningen jest wyraźnym faworytem modelu, głównie za sprawą fatalnej defensywy Zwolle
(2,83 GA/mecz, 0% czystych kont), ale to nie ekstremalna przepaść klasowa — obie drużyny są
w dolnej połowie tabeli i w słabej formie. Najbezpieczniejszy typ to **Over 1,5 gola (85%)**,
odporny na to, która drużyna wygra. Typ "1" (61%) wymaga świadomości ryzyka remisu i
niespodzianki Zwolle, którego lepszy bilans wyjazdowy niż domowy jest nietypowym, ale realnym
sygnałem ostrzegawczym.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani
zachęty do zakładów. Graj odpowiedzialnie.*

---

# Widzew Łódź vs Wieczysta Kraków
**Rozgrywki:** PKO BP Ekstraklasa, 9. kolejka | **Termin:** piątek 18.09.2026, 18:00 (Stadion Widzewa, Łódź) | **Ranga meczu:** dolna połowa tabeli (11. vs 17./ostatnie miejsce), pierwszy oficjalny mecz między klubami

## Kontekst i forma
- **Forma Widzewa** (8 meczów): 1W-5D-2L, 8 pkt, 11. miejsce. Gole: 11:11 (1,38/mecz w obie
  strony). Ostatnio remis 1:1 z Legią Warszawa — debiut nowego trenera **Mateusza
  Stolarskiego** (były szkoleniowiec Motoru Lublin), który zastąpił Aleksandara Vukovicia i
  zapowiada "nieprzewidywalność i odwagę w grze ofensywnej". **Widzew nie wygrał żadnego
  meczu u siebie w tym sezonie (0W-2D-2L, 1,25 GF / 1,75 GA w domu)** — istotny kontrast z
  lepszym bilansem na wyjeździe (1W-3D-0L).
- **Forma Wieczystej** (7 meczów): 1W-1D-5L, 4 pkt, przedostatnie miejsce. Gole: 9:15
  (1,29 GF / 2,14 GA) — najgorsza defensywa w tej parze i jedna z najgorszych w lidze.
  Ostatni mecz: porażka 0:2 z Pogonią Szczecin na wyjeździe. Jedyne zwycięstwo sezonu —
  nad Piastem Gliwice.
- **Sygnał kryzysowy u Wieczystej**: "w kuluarach coraz częściej mówi się o zmianie trenera"
  (Željko Kopić wciąż na stanowisku, ale presja rośnie), drużyna szuka ratunku przed przerwą
  reprezentacyjną — klasyczny profil "rannego zwierzęcia" z Kroku 2b, choć bez potwierdzonej
  jeszcze zmiany szkoleniowca (w odróżnieniu od przypadku Valencia/Alavés z weryfikacji).
- **Kadra**: brak potwierdzonych kluczowych nieobecności po żadnej ze stron w dostępnych
  źródłach poza wcześniejszymi, niepewnymi wzmiankami o kontuzjach; Wieczysta spodziewana w
  zbliżonym składzie do poprzedniego meczu.

## Model bazowy (oczekiwane gole)
Ekstraklasa, przybliżona średnia ligowa ~2,75 gola/mecz (gospodarze ~1,50, goście ~1,25).
Siłę ataku/obrony liczono jako średnią ważoną 60% dane venue-specific / 40% sezon ogółem
(próby 4-5 meczów per venue są małe). Korekta jakościowa: **neutralna** — argumenty w obie
strony się równoważą (nowy trener Widzewa może podbić atak, ale to dopiero debiut; desperacja
Wieczystej może oznaczać zarówno większą mobilizację, jak i załamanie) — nie zastosowano
dodatkowej korekty poza już wykonanym ważeniem venue/sezon.

λ(Widzew) = **2,35** | λ(Wieczysta) = **1,40**

## Model rożnych
Średnia ligowa Ekstraklasy z dostępnych źródeł: ~10,2-10,9 rożnych łącznie na mecz (dwa
niezależne odczyty z FootyStats, oba z bardzo małych prób 13-69 z kilkuset meczów sezonu —
**dane wyraźnie niepełne**). Próby policzenia współczynników per drużyna dały wartości
statystycznie niewiarygodne (np. <3 rożne łącznie na mecz dla Widzewa — sprzeczne z każdym
realnym meczem ligowym), więc odrzucono je i oparto λ o średnią ligową skorygowaną stylem
gry: Widzew jako gospodarz z przewagą terytorialną i Wieczysta broniąca się nisko jako
beniaminek walczący o utrzymanie (typowo oddaje więcej rożnych).

λ_rożne(Widzew) = **6,0** | λ_rożne(Wieczysta) = **4,3** — **oszacowanie szerokie, jakościowe,
nie oparte o wiarygodne dane per drużyna.**

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Widzew wygrywa | 57,6% | 1,74 |
| Remis | 19,3% | 5,17 |
| Wieczysta wygrywa | 22,0% | 4,55 |

*⚠ Kalibracja z Kroku 2b: 57,6% mieści się w przedziale 50-85%, więc **zarówno remis, jak i
zwycięstwo Wieczystej (odwrotny wynik) to porównywalne ryzyka**. Dodatkowo Wieczysta nosi
cechy underdoga "kryzysowego" (rosnąca presja na trenera, desperacja przed przerwą
reprezentacyjną), a Widzew nie wygrał żadnego meczu u siebie w tym sezonie — to razem
uzasadnia praktyczne obniżenie pewności typu "1" o kilka punktów poniżej surowej liczby z
modelu, mimo że formalnie nie zmieniam samej liczby 57,6%. Nie polecam "1" jako najlepszego
typu tego meczu.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Widzew więcej rożnych | 64,5% | 1,55 |
| Remis rożny | 11,0% | 9,08 |
| Wieczysta więcej rożnych | 24,5% | 4,09 |
| Over 8,5 | 70,0% | 1,43 |
| Over 9,5 | 57,9% | 1,73 |
| Over 10,5 | 45,4% | 2,20 |

### Najbardziej prawdopodobne wyniki (gole)
2-1 (9,1%), 1-1 (7,7%), 3-1 (7,1%), 2-0 (6,5%), 2-2 (6,4%)

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 88,8% | 1,13 |
| Over 2,5 | 72,3% | 1,38 |
| BTTS - Tak | 67,3% | 1,49 |

*Najmocniejszy i najbezpieczniejszy rynek meczu — obie drużyny mają dziurawe defensywy
(łącznie 1,38 + 2,14 = 3,52 GA/mecz), więc bramki powinny paść niezależnie od tego, kto
wygra.*

### Strzały i strzały celne
Brak precyzyjnych aktualnych danych — orientacyjnie 9-12 strzałów na drużynę, bez wyraźnej
przewagi jakościowej którejś ze stron w tym wskaźniku.

### Faule i kartki
Brak szczegółowych danych per zawodnik dla obu drużyn w dostępnych źródłach (Ekstraklasa ma
tu słabsze pokrycie niż Top 5) — nie znaleziono wiarygodnych liczb, pomijam zamiast zgadywać.
Nic w researchu nie wskazuje na nietypowy profil dyscyplinarny.

## Podsumowanie
Model faworyzuje Widzew, ale to typowy przykład sytuacji z Kroku 2b: tabela sugeruje wyraźną
przewagę (11. vs 17. miejsce), lecz forma i kontekst (Widzew niepokonany u siebie tylko w
sensie "bez porażki", ale też bez zwycięstwa; Wieczysta w realnym kryzysie trenerskim i
desperacko szukająca punktów) każą traktować typ "1" ostrożniej niż surowa liczba 57,6%
sugeruje. Najbezpieczniejszy i najlepiej uzasadniony typ to **Over 1,5 gola (88,8%)** —
odporny na to, kto wygra, i mocno wspierany przez dane obu defensyw.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani
zachęty do zakładów. Graj odpowiedzialnie.*

---

# Wisła Kraków vs Śląsk Wrocław
**Rozgrywki:** PKO BP Ekstraklasa, 9. kolejka | **Termin:** piątek 18.09.2026, 20:30 (Synerise Arena, Kraków) | **Ranga meczu:** górna połowa vs dolna połowa tabeli (5. vs 15. miejsce)

## Kontekst i forma
- **Forma Wisły** (8 meczów): 4W-2D-2L, 14 pkt, 5. miejsce. Gole: 15:11 (+4). Ostatnie 5
  meczów: L-D-W-D-W. **U siebie komplet zwycięstw: 4W-0D-0L, 8:2 w bramkach (2,00 GF /
  0,50 GA na mecz)** — najlepszy bilans domowy w lidze wg zapowiedzi przedmeczowych. Na
  wyjeździe wyraźnie słabsza: 0W-2D-2L, 7:9.
- **Forma Śląska** (8 meczów): 1W-3D-4L, 6 pkt, 15. miejsce. Gole: 10:13. Ostatnie 5 meczów:
  L-D-D-L-L (bez zwycięstwa). Na wyjeździe: **0W-1D-3L, 4:7 (1,00 GF / 1,75 GA)** — słaby
  bilans, ale nie skrajny (żadnej klęski wysokim wynikiem, 3 remisy w sezonie pokazują, że to
  drużyna trudna do rozbicia, nie kompletnie rozbita).
- **Kadra**: Wisła sprzedała latem lidera strzelców Jordi Sáncheza do Pogoni Szczecin, ale w
  jedynym dotychczasowym meczu bez niego zastępujący go Angel Rodado strzelił 2 gole
  decydujące o zwycięstwie — na razie brak sygnału osłabienia ataku. Możliwe absencje:
  Raoul Giger, Jakub Stępak (kontuzje), Jeremy Guillemenot (potrzebuje więcej czasu do formy);
  Maxence Maisonneuve (Wisła) ma 3 żółte kartki w sezonie — obserwować dystans do
  zawieszenia (zwykle 4-5 kartek w Ekstraklasie), realne ryzyko pauzy w kolejnych kolejkach,
  ale nie na ten mecz. Po stronie Śląska brak potwierdzonych kluczowych nieobecności w
  dostępnych źródłach.
- **H2H / kontekst**: Śląsk szuka drugiego zwycięstwa sezonu po porażce z Koroną Kielce.

## Model bazowy (oczekiwane gole)
Ekstraklasa, przybliżona średnia ligowa ~2,75 gola/mecz (gospodarze ~1,50, goście ~1,25).
Siła ataku/obrony liczona jako średnia ważona 60% venue-specific / 40% sezon ogółem, z lekkim
złagodzeniem (shrinkage) skrajnie dobrego bilansu domowego Wisły (4 mecze to wciąż mała
próba na samodzielne wyliczenie) oraz z uwzględnieniem sprzedaży Sáncheza jako czynnika
niepewności (nie zastosowano obniżki λ, bo dotychczasowe dane po transferze są pozytywne).

λ(Wisła) = **2,40** | λ(Śląsk) = **0,85**

## Model rożnych
Średnia ligowa Ekstraklasy: ~10,2-10,9 rożnych łącznie na mecz (dane niepełne, patrz uwaga na
początku raportu). Wisła jako drużyna dominująca w domu terytorialnie (najlepszy bilans
domowy w lidze, wysoki xG) dostaje wyraźny przechył w górę, Śląsk broniący się w gorszej
formie na wyjeździe — przechył w dół.

λ_rożne(Wisła) = **6,3** | λ_rożne(Śląsk) = **4,0** — **oszacowanie szerokie, jakościowe**,
z tych samych powodów co w pozostałych meczach Ekstraklasy w tym raporcie.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Wisła wygrywa | 70,5% | 1,42 |
| Remis | 16,9% | 5,93 |
| Śląsk wygrywa | 11,4% | 8,74 |

*⚠ Mimo silnych argumentów za Wisłą (komplet zwycięstw u siebie, najlepsza defensywa domowa
w lidze), 70,5% wciąż mieści się w przedziale 50-85% z Kroku 2b — **remis i zwycięstwo
Śląska to realne, porównywalne ryzyka**, których nie eliminuje nawet duża przewaga w danych.
Śląsk nie jest jednak w pełnym "kryzysie" w rozumieniu Kroku 2b (3 remisy w sezonie, brak
zmiany trenera, brak serii klęsk wysokimi wynikami) — to zwykła słabsza forma, nie "ranne
zwierzę" — dlatego nie stosuję dodatkowej korekty w dół poza standardowym zastrzeżeniem.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Wisła więcej rożnych | 71,2% | 1,40 |
| Remis rożny | 9,8% | 10,17 |
| Śląsk więcej rożnych | 18,9% | 5,29 |
| Over 8,5 | 70,0% | 1,43 |
| Over 9,5 | 57,9% | 1,73 |
| Over 10,5 | 45,4% | 2,20 |

### Najbardziej prawdopodobne wyniki (gole)
2-0 (11,2%), 2-1 (9,5%), 1-0 (9,3%), 3-0 (8,9%), 1-1 (7,9%)

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 83,5% | 1,20 |
| Over 2,5 | 63,0% | 1,59 |
| BTTS - Tak | 51,4% | 1,95 |

### Strzały i strzały celne
Brak precyzyjnych aktualnych danych celnych strzałów — orientacyjnie Wisła 12-15 strzałów
(13,57/mecz wg ogólnych statystyk ligowych), Śląsk 10-13; Wisła powinna mieć wyraźną
przewagę objętości gry jako dominujący gospodarz.

### Faule i kartki
**Indywidualnie**: Maxence Maisonneuve (Wisła) — 3 żółte kartki w sezonie, obserwować
dystans do zawieszenia w kolejnych meczach (nie wpływa na dzisiejszy mecz). Poza tym brak
szczegółowych danych fauli/kartek per zawodnik dla obu drużyn w dostępnych źródłach —
pomijam resztę zamiast zgadywać. Nic nie wskazuje na nietypowy profil drużynowy.

## Podsumowanie
Najsilniejszy fundament danych spośród czterech dzisiejszych meczów — Wisła ma komplet
zwycięstw u siebie z bardzo solidną defensywą (0,5 GA/mecz), a Śląsk jest realnie słabszy na
wyjeździe. Mimo to formalnie pozostajemy w strefie 50-85%, więc typ "1" (70,5%) wymaga
standardowego zastrzeżenia o ryzyku remisu/niespodzianki, choć bez dodatkowej korekty w dół
(Śląsk nie jest w kryzysie). **Rożna przewaga Wisły (71,2%)** i **Over 1,5 gola (83,5%)** to
alternatywne, dobrze uzasadnione typy o zbliżonej lub wyższej pewności.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani
zachęty do zakładów. Graj odpowiedzialnie.*
