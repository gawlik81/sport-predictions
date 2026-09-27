# Dzisiejsze mecze — 15.09.2026

Trzy rozgrywki w zasięgu skilla mają dziś mecze: **Puchar Ligi Angielskiej
(Carabao Cup), 3. runda** (5 spotkań), **Ekstraklasa** (2 spotkania) oraz
**La Liga** (3 spotkania, kolejka śródtygodniowa 6). Poniżej pełna analiza
każdego meczu — rożne, zgodnie z priorytetem tego skilla, dostają wszędzie
pełny model probabilistyczny.

**Format 3. rundy Carabao Cup 2026/27 (zweryfikowany researchem):** brak
dogrywki i brak rewanżu — remis po 90 minutach oznacza od razu rzuty karne.
Dlatego przy każdym meczu pucharowym obok klasycznego 1X2 (90 min) podana
jest tabela "Prawdopodobieństwo awansu".

---

## NAJPEWNIEJSZE PREDYKCJE DNIA

Ranking oparty na dwóch kryteriach, które historycznie najlepiej kalibrują
się z rzeczywistymi wynikami dla tego modelu: (1) **ekstremalna przepaść
jakościowa** między drużynami to najbardziej wiarygodna kategoria typów —
znacznie pewniejsza niż typy z przedziału 50-75%, gdzie remis bywa głównym,
niedoszacowanym ryzykiem; (2) brak istotnych sygnałów ostrzegawczych w
researchu (kontuzje kluczowych zawodników, forma przeciwna modelowi).

| # | Typ | Prawdopodobieństwo | Uzasadnienie |
|---|---|---|---|
| 1 | **Alavés wygrywa z Valencią** (1X2) | **82%** | Najostrzejsza przepaść formy dnia: Alavés 3/3 zwycięstw u siebie w sezonie, Valencia 1 gol strzelony w 5 meczach, dopiero co zwolniła trenera. Jedyne ryzyko: efekt "nowej miotły" po zmianie szkoleniowca dwa dni przed meczem — uwzględnione w λ, ale to nadal czynnik niepewności, nie powód do obniżenia typu. |
| 2 | **Real Madryt wygrywa z Elche** (1X2) | **78%** | Real Madryt niepokonany z Elche od 1978 r., różnica klas ligowych ogromna (2. vs 19. miejsce). Realne ryzyko obniżające pewność: osłabiona defensywa gości (Militão, Mendy, Rodrygo poza grą) — to jedyna luka w argumentacji, ale atak Realu (Mbappé, 14 goli w 5 meczach) i tak powinien przeważyć. |
| 3 | **Awans Arsenalu** (Puchar Ligi, Ipswich vs Arsenal) | **~90%** | Arsenal wygrał 5 z rzędu (9:1 w bramkach), Ipswich ma najgorszą defensywę wśród beniaminków PL i planuje kolejną falę rotacji młodzieżowej. Nawet przy spodziewanej rotacji Arsenalu przepaść jest zbyt duża. |
| 4 | **Over 1.5 gola: Elche vs Real Madryt** | **94%** | Pochodna typu #2 — przy λ_away=3,7 szansa na mniej niż 2 gole w meczu jest statystycznie znikoma. |
| 5 | **Rożna przewaga Górnika nad Koroną** | **82%** | Zbieżny sygnał dwóch niezależnych wskaźników: fatalny bilans rożny Korony u siebie (4,0 zdobyte/6,3 stracone) i świetna forma wyjazdowa lidera tabeli. |

**Zdecydowanie odradzane jako "pewniaki"** (mimo z pozoru wysokiego
prawdopodobieństwa w modelu): rożne w Ipswich–Arsenal (96% dla Arsenalu) i
w Elche–Real Madryt (86% dla Realu) — liczby są matematycznie poprawne, ale
dane wejściowe o rożnych dla obu meczów są w tym raporcie wprost oznaczone
jako niepewne/sprzeczne między źródłami, więc końcowa pewność jest niższa,
niż sugeruje sam procent. Podobnie ostrożnie potraktuj Peterborough–Barnsley
i Reading–Brentford (League One) — to najbardziej wyrównane i najsłabiej
udokumentowane mecze dnia.

---

## PUCHAR LIGI ANGIELSKIEJ — 3. RUNDA

### 1. Liverpool vs Tottenham Hotspur
**Anfield, wtorek 15.09.2026, 20:00 BST**

**Kontekst i forma**
- Liverpool (trener Andoni Iraola od czerwca 2026) — niepokonany w ostatnich
  6 meczach wszystkich rozgrywek (m.in. 2:1 z Atlético w LM, 2:2 z Newcastle
  i Nottingham Forest w PL). Kadra mocno przetrzebiona: brak Ekitikego,
  Chiesy, Gomeza, Bradleya, Leoniego; wątpliwy Gakpo — spodziewana spora
  rotacja.
- Tottenham (trener Roberto De Zerbi od marca 2026) — kryzys formy: **0
  bramek w 4 kolejnych meczach ligowych**, 17. miejsce w tabeli. Brak
  Kulusevskiego, Xaviego Simonsa, Mudryka, Odoberta (czterech kluczowych
  ofensywnych zawodników); wątpliwi Porro, Udogie, Maddison. Robertson
  (latem odszedł z Liverpoolu do Spurs) typowany do gry przeciw byłemu
  klubowi.
- H2H: Liverpool niepokonany w 6 z ostatnich 8 starć, **Spurs nie wygrali na
  Anfield od maja 2011** (15 lat, 17 wizyt bez zwycięstwa), a Liverpool
  wygrał wszystkie ostatnie 4 starcia w Pucharze Ligi między tymi klubami.
- **Uwaga o jakości danych**: sezon 2026/27 to dopiero 4-5 meczów ligowych
  na drużynę (nowi trenerzy) — statystyki sezonowe są bardzo niestabilne.
  Dane o rożnych są sprzeczne między źródłami (część zablokowana za
  paywallem) — potraktuj poniższe liczby rożnych jako orientacyjne, z
  szerszym marginesem błędu niż zwykle.

**Model bazowy (gole)** — z powodu małej próby oparto się głównie na jakości
drużyn i bieżącej formie, a nie na czystym ilorazie względem średniej PL
(2,75 gola/mecz, sezon 2025/26). Korekty: -15% dla ataku Liverpoolu (rotacja,
brak napastników), +30% dla ataku Tottenhamu względem suchej średniej z
sezonu (0 goli w 4 meczach to zbyt ekstremalna wartość, by ekstrapolować
wprost — oczekiwana częściowa regresja do średniej, ale wciąż wyraźnie
poniżej normy klubu tej klasy).
- λ(Liverpool) = **1,75** | λ(Tottenham) = **0,70**

**Model rożnych** — dane niepełne i częściowo sprzeczne (patrz uwaga wyżej);
przyjęto orientacyjną historyczną średnią PL (~10,5 rożnych/mecz łącznie) i
umiarkowane szacunki dla obu drużyn.
- λ_rożne(Liverpool) = **6,0** | λ_rożne(Tottenham) = **4,5**

**Wynik po 90 minutach (1X2)**
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Liverpool wygrywa | 62% | 1.60 |
| Remis | 23% | 4.36 |
| Tottenham wygrywa | 14% | 6.90 |

**Prawdopodobieństwo awansu** (remis w 90 min → od razu karne, rozdzielone
~55/45 na korzyść Liverpoolu jako lekkiego faworyta karnych)
| Scenariusz | Prawdopodobieństwo |
|---|---|
| **Liverpool awansuje** | **~75%** |
| **Tottenham awansuje** | **~25%** |

**Rożne — przewaga i over/under**
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Liverpool więcej rożnych | 62% | 1.61 |
| Remis rożny | 11% | 8.89 |
| Tottenham więcej rożnych | 27% | 3.74 |
| Over 9.5 | 60% | 1.66 |
| Over 10.5 | 48% | 2.09 |
| Over 11.5 | 36% | 2.77 |

**Gole**
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 2.5 | 44% | 2.26 |
| BTTS - Tak | 41% | 2.41 |

**Najbardziej prawdopodobne wyniki**: 1-0 (15%), 2-0 (13%), 1-1 (11%)

*Podsumowanie: Liverpool wyraźnym faworytem mimo rotacji — historia na
Anfield i kryzys strzelecki Tottenhamu ważą więcej niż same rotacje kadrowe.
Awans Liverpoolu ok. 3:1, ale nie jest to pewniak — Spurs grają "o coś" po
serii rozczarowań.*

---

### 2. Ipswich Town vs Arsenal

**Kontekst**: Arsenal wygrał 5 ostatnich meczów wszystkich rozgrywek (9:1 w
bramkach), goni pierwszy triumf w tych rozgrywkach od 1993 r. — spodziewana
częściowa, ale nie drastyczna rotacja (Gyokeres, Madueke, Merino, Zubimendi
w składzie; Kepa zamiast Rai). Ipswich (awans z Championship latem) ma
katastrofalną defensywę (xGA 2,34/mecz) i w poprzedniej rundzie wystawił 9
zmienionych zawodników (debiuty akademii) — trener O'Neil zapowiada podobny
schemat wobec przepaści klasowej.
- λ (gole): Ipswich **0,35** | Arsenal **2,45**
- **Rożne** (Arsenal ma najlepszy bilans rożnych w PL: 8 zdobytych / 2
  stracone na mecz — ekstremalna przewaga, dodatkowo wzmocniona słabą
  defensywą Ipswich; wartość "przeciw" dla Ipswich jest szacunkiem, brak
  pewnych danych źródłowych — **niska pewność tej liczby**):
  λ_rożne Ipswich **1,5** | Arsenal **7,0**

| Rynek | Ipswich | Remis | Arsenal |
|---|---|---|---|
| Wynik po 90 min | 4% (26.81) | 13% (7.98) | 82% (1.21) |
| **Rożne — przewaga** | 1% (73.24) | 2% (47.06) | 96% (1.04) |

**Prawdopodobieństwo awansu** (rozdział remisu ~40/60 na korzyść Arsenalu —
mimo przepaści klasowej karne spłaszczają różnicę, więc nie przenoszę pełnej
proporcji z 1X2): **Arsenal ~90%** / **Ipswich ~9%**

- Over 9.5 rożnych: 35% | Over 2.5 gola: 53% | BTTS: 27%
- Najbardziej prawdopodobny wynik: 0-2 (18%)

*Uwaga: skala przewagi Arsenalu w modelu rożnych (1,5 vs 7,0) jest bardzo
duża — to efekt nałożenia się dwóch ekstremów (najlepszy bilans rożnych w
lidze + najgorsza defensywa rywala), więc traktuj to jako górny pułap
oczekiwań, nie pewnik.*

---

### 3. West Ham United vs Fulham

**Kontekst — ważna korekta względem założeń wyjściowych**: West Ham **nie
gra już w Premier League** — spadli do Championship i są tam liderem tabeli
(4 zwycięstwa z rzędu, seria 6 meczów bez porażki, w tym 6:0 z Wrexham).
Fulham (PL) jest w kryzysie: 18. miejsce, bez zwycięstwa w 4 meczach, ostatnio
0:0 z Liverpoolem. To odwraca typowy scenariusz "duży klub rotuje przeciw
maluczkim" — to West Ham jest w lepszej dyspozycji, choć to oni planują
rotację (~9 zmian) z myślą o sobotnim derbowym starciu z Millwall; Fulham ma
wystawić w miarę mocny skład (Cairney i Andersen niedostępni). Mecz
międzyligowy — zastosowano normalizację względem odrębnych średnich lig
(Championship i PL są jednak zbliżone, ~2,86 vs ~2,75 gola/mecz).
- λ (gole): West Ham **1,60** | Fulham **0,60**
- **Rożne**: West Ham ma solidny bilans w Championship (~10,4 rożnych/mecz
  łącznie). Dane o rożnych Fulham w bieżącym sezonie PL nie zostały
  znalezione — użyto szacunku opartego na średniej ligowej (**niska
  pewność**): λ_rożne West Ham **5,5** | Fulham **4,3**

| Rynek | West Ham | Remis | Fulham |
|---|---|---|---|
| Wynik po 90 min | 62% (1.62) | 25% (4.07) | 14% (7.30) |
| **Rożne — przewaga** | 59% (1.70) | 12% (8.30) | 29% (3.42) |

**Prawdopodobieństwo awansu**: **West Ham ~75%** / **Fulham ~25%**

- Over 9.5 rożnych: 52% | Over 2.5 gola: 38% | BTTS: 36%
- Najbardziej prawdopodobny wynik: 1-0 (18%)

---

### 4. Peterborough United vs Barnsley

**Kontekst**: obie drużyny z League One — brak potrzeby normalizacji
międzyligowej. Peterborough przechodzi kryzys (4 mecze bez zwycięstwa, aż 6
zawodników kontuzjowanych, w tym najlepsi obrońcy) i ma najgorszy atak w
lidze (0,67 gola/mecz). Barnsley ma korzystną historię h2h (4 zwycięstwa w
ostatnich 5 starciach z Peterborough, w tym 3 z rzędu bez straty gola), choć
ostatnio traci dużo bramek (8 w 2 meczach). Lokalna prasa sugeruje, że
Peterborough potrzebuje punktów bardziej niż odpoczynku — nie oczekuj
drastycznej rotacji mimo pucharowej rangi meczu.
- λ (gole): Peterborough **0,60** | Barnsley **1,20**
- **Rożne — istotna luka danych**: nie udało się znaleźć wiarygodnych,
  porównywalnych stawek rożnych na mecz dla żadnej z drużyn (tylko niejasne
  sumy sezonowe). Poniższe λ to **luźne szacunki** oparte na ogólnym stylu
  gry i średniej dla League One, a nie solidny model — traktuj je jako
  orientacyjny, szeroki przedział, zgodnie z zasadą "uczciwy szeroki
  przedział zamiast fałszywej precyzji": λ_rożne Peterborough **5,0** |
  Barnsley **4,3**

| Rynek | Peterborough | Remis | Barnsley |
|---|---|---|---|
| Wynik po 90 min | 19% (5.40) | 31% (3.25) | 51% (1.97) |
| **Rożne — przewaga** (niska pewność) | 52% (1.91) | 13% (7.73) | 35% (2.89) |

**Prawdopodobieństwo awansu**: **Barnsley ~68%** / **Peterborough ~32%**

- Over 2.5 gola: 27% | BTTS: 32%
- Najbardziej prawdopodobny wynik: 0-1 (20%)

---

### 5. Reading vs Brentford

**Kontekst**: mecz międzyligowy (League One vs Premier League) — zastosowano
normalizację z Kroku 2 (własna średnia ligowa dla siły ataku/obrony każdej
drużyny + wspólny europejski punkt odniesienia dla finalnego mnożnika).
Reading ma najlepszy atak w pierwszej połowie w całej League One i najwięcej
bramek u siebie w lidze (lider strzelców Jack Marriott). Brentford
niepokonany w 5 meczach, ale zapowiada mocną rotację: Furo kontuzjowany,
nowy nabytek Diouf w pierwszym składzie, Carvalho pierwszy mecz od listopada,
Kelleher w bramce. To klasyczny układ "słabszej ligowo, ale głodnej sensacji"
drużyny gospodarzy kontra mocno przebudowany zespół z wyższej ligi.
- λ (gole): Reading **1,25** | Brentford **0,90**
- **Rożne — luka danych**: brak wiarygodnych stawek na mecz dla obu drużyn w
  bieżącym sezonie; λ oparte na stylu gry (Reading = drużyna grająca dużo
  dośrodkowań/wrzutek, stąd wyżej) — **niska pewność**: λ_rożne Reading
  **5,5** | Brentford **4,0**

| Rynek | Reading | Remis | Brentford |
|---|---|---|---|
| Wynik po 90 min | 44% (2.26) | 29% (3.46) | 27% (3.75) |
| **Rożne — przewaga** (niska pewność) | 63% (1.60) | 12% (8.53) | 26% (3.90) |

**Prawdopodobieństwo awansu**: **Reading ~59%** / **Brentford ~41%**

- Over 2.5 gola: 36% | BTTS: 42%
- Najbardziej prawdopodobny wynik: 1-0 (15%)

*To najbardziej wyrównany typ dnia — mocna rotacja Brentford realnie daje
Reading szansę na sensację.*

---

## EKSTRAKLASA

### 6. Raków Częstochowa vs Zagłębie Lubin
**18:00**

**Kontekst i forma**
- Raków w głębokim kryzysie: 1 zwycięstwo w 7 meczach, 18. (ostatnie)
  miejsce, zero czystych kont w sezonie. 8.09 zwolniono trenera Kroczka —
  nowym szkoleniowcem został Tomasz Kaczmarek (z Radomiaka). Ostatni mecz:
  wygrana 2:1 z Motorem Lublin przerwała serię 4-5 porażek.
- Zagłębie w dobrej dyspozycji ligowej (8. miejsce, seria W-D-D-D-W), ale
  wyraźnie słabsze na wyjeździe (2 gole w 3 meczach) i osłabione psychicznie
  po kompromitującej porażce 2:3 w Pucharze Polski z III-ligową Siarką
  Tarnobrzeg.
- H2H: w ostatnich 4 starciach 2 zwycięstwa Rakowa, 2 remisy, Zagłębie bez
  wygranej.
- **Luka danych**: brak potwierdzonych informacji o kontuzjach/zawieszeniach
  dla żadnej z drużyn.

**Model bazowy (gole)** — dane sezonowe z pełnym rozbiciem dom/wyjazd
(Raków dom: 1,5 strzelonych/2,5 straconych na mecz; Zagłębie wyjazd: 0,67/1,33).
Korekty jakościowe: +10% dla ataku Rakowa (efekt nowego trenera, odbudowa po
zwycięstwie), -10% dla ataku Zagłębia (spadek pewności siebie po
pucharowej wpadce).
- λ(Raków) = **1,00** | λ(Zagłębie) = **0,90**

**Model rożnych** — dane w miarę spójne z obserwowanymi średnimi meczowymi
(Raków u siebie ~10,0 rożnych łącznie/mecz, Zagłębie na wyjeździe ~9,7-12,0
łącznie — mała próbka 3 mecze).
- λ_rożne(Raków) = **6,5** | λ_rożne(Zagłębie) = **3,5**

**Wynik meczu (1X2)**
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Raków wygrywa | 37% | 2.72 |
| Remis | 32% | 3.15 |
| Zagłębie wygrywa | 31% | 3.18 |

**Rożne — przewaga i over/under**
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Raków więcej rożnych | 79% | 1.27 |
| Remis rożny | 8% | 12.10 |
| Zagłębie więcej rożnych | 13% | 7.66 |
| Over 9.5 | 54% | 1.84 |
| Over 10.5 | 42% | 2.40 |

**Gole**: Over 2.5 — 30% | BTTS - Tak — 38%

**Najbardziej prawdopodobne wyniki**: 0-0 i 1-0 (po 15%), 0-1 i 1-1 (po 13%)

*Podsumowanie: mecz bardzo wyrównany w 1X2 (efekt Boost dla nowego trenera
Rakowa neutralizuje przewagę tabelaryczną Zagłębia), ale zdecydowanie
przechylony w stronę Rakowa w rożnych — słaba gra wyjazdowa Zagłębia to
kluczowy czynnik tej różnicy.*

---

### 7. Korona Kielce vs Górnik Zabrze
**20:30 — zaległy mecz 2. kolejki**

**Kontekst i forma**
- Korona (7. miejsce) niepokonana w 5 meczach (W-D-W-D-W), ale zaskakująco
  słabsza u siebie niż na wyjeździe (3 remisy w 3 domowych meczach, bilans
  bramkowy 3:3, wobec 6:3 na wyjeździe).
- Górnik (lider tabeli) w świetnej formie wyjazdowej — 100% zwycięstw na
  wyjeździe (3/3), 6:2 w bramkach. Niepokonany w ostatnich 12 bezpośrednich
  starciach z Koroną (8 zwycięstw, 4 remisy). Mecz pierwotnie przełożony z
  powodu gry Górnika w pucharach europejskich — klub odpadł już ze
  wszystkich 3 europejskich pucharów, więc dziś gra bez rozproszenia.
- Wątek poboczny: Patrik Hellebrand (Korona) to letni transfer z Górnika.
- **Niepotwierdzony sygnał**: możliwe zawieszenie kartkowe Sondre Lisetha
  (Górnik) — informacja niejasna co do terminu, wymaga weryfikacji
  bezpośrednio przed meczem.

**Model bazowy (gole)** — pełne dane dom/wyjazd (Korona dom: 1,0/1,0 na
mecz; Górnik wyjazd: 2,0/0,67 na mecz — bardzo mocna forma wyjazdowa).
Korekty: +5% dla obu drużyn (Korona - pewność siebie z serii bez porażki;
Górnik - pełna koncentracja na lidze po odpadnięciu z pucharów).
- λ(Korona) = **0,85** | λ(Górnik) = **1,25**

**Model rożnych** — dane spójne z obserwowanymi średnimi (Korona ~10,3
łącznie/mecz z ujemnym bilansem 4,0/6,3; Górnik ~9,9 łącznie z dodatnim
bilansem 6,0/3,9).
- λ_rożne(Korona) = **3,3** | λ_rożne(Górnik) = **6,7**

**Wynik meczu (1X2)**
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Korona wygrywa | 25% | 3.96 |
| Remis | 29% | 3.43 |
| Górnik wygrywa | 46% | 2.19 |

**Rożne — przewaga i over/under**
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Korona więcej rożnych | 10% | 9.58 |
| Remis rożny | 7% | 13.75 |
| Górnik więcej rożnych | 82% | 1.22 |
| Over 9.5 | 54% | 1.84 |
| Over 10.5 | 42% | 2.40 |

**Gole**: Over 2.5 — 35% | BTTS - Tak — 41%

**Najbardziej prawdopodobne wyniki**: 0-1 (15%), 1-1 (13%), 0-0 (12%)

*Podsumowanie: Górnik wyraźnym faworytem zarówno w 1X2, jak i (jeszcze
mocniej) w rożnych — słaba forma rożna Korony u siebie i świetna forma
wyjazdowa lidera to zbieżny sygnał w obu modelach.*

---

## LA LIGA — KOLEJKA 6 (ŚRÓDTYGODNIOWA)

### 8. Rayo Vallecano vs Espanyol
**Estadio Ontime Butarque (Leganés), 19:00**

**Kontekst i forma**
- Rayo od początku sezonu gra "u siebie" poza Vallecas — władze regionalne
  cofnęły klubowi licencję na użytkowanie stadionu (28.07.2026, względy
  bezpieczeństwa/sanitarne), tymczasowym domem jest Butarque w Leganés.
  Realna erozja przewagi własnego boiska, nie tylko formalność.
- Rayo: 16. miejsce, 4 pkt (1Z-1R-3P, 8:14), forma fatalna — 0 punktów na
  wyjeździe w tym sezonie, seria: P1:4 (Real Madryt), R1:1, P2:5 (Barcelona),
  Z3:2, P1:2. Brak Isiego Palazóna (kluczowy kreator) i De Frutosa
  (czerwona kartka, zawieszenie) — osłabiony atak.
- Espanyol: 8. miejsce, 7 pkt (2Z-1R-2P, 8:5) — najlepsza defensywa spośród
  dzisiejszych "słabszych" drużyn. Braki: Gorosabel, Kike García, Puado,
  Roca.
- H2H: ostatni mecz wygrał Rayo 1:0; historycznie Rayo nieco lepszy bilans.
- **Uwaga**: to NIE jest ekstremalny mecz — obie drużyny osłabione
  kadrowo, żadna nie ma gorącej serii. Najsłabiej udokumentowany pod
  względem pewności typ dnia z tej trójki La Liga.

**Model bazowy (gole)** — Espanyol wyraźnie solidniejszy defensywnie (5
straconych w 5 meczów), Rayo koszmarnie dziurawy z tyłu (14 straconych) —
zastosowano spore ściągnięcie (shrinkage) tego skrajnego wskaźnika w stronę
średniej ligowej ze względu na małą próbę (5 meczów). Dodatkowa korekta w
dół dla Rayo za brak Isiego Palazóna i erozję "przewagi własnego boiska"
(gra poza Vallecas).
- λ(Rayo) = **1,00** | λ(Espanyol) = **2,40**

**Model rożnych** — dane o rożnych Rayo są sprzeczne między źródłami (6 vs
12,8 na mecz) — przyjęto niższą, bardziej wiarygodną wartość.
- λ_rożne(Rayo) = **6,5** | λ_rożne(Espanyol) = **4,2**

| Wynik meczu (1X2) | % | kurs |
|---|---|---|
| Rayo wygrywa | 14% | 7.13 |
| Remis | 18% | 5.67 |
| Espanyol wygrywa | 67% | 1.49 |

**Rożne — przewaga i over/under**
| Rynek | % | kurs |
|---|---|---|
| Rayo więcej rożnych | 71% | 1.41 |
| Remis rożny | 10% | 10.28 |
| Espanyol więcej rożnych | 19% | 5.16 |
| Over 9.5 | 63% | 1.60 |
| Over 10.5 | 50% | 1.98 |

**Gole**: Over 2.5 — 66% | BTTS - Tak — 57%
**Najbardziej prawdopodobny wynik**: 0-2 / 1-2 (po 10%)

*Podsumowanie: Espanyol wyraźny faworyt, ale to typ z "ryzykownego"
przedziału 50-75% — remis (18%) i niespodzianka Rayo nie są tu
zaniedbywalne, zwłaszcza że Espanyol też gra bez kilku ważnych zawodników.*

---

### 9. Alavés vs Valencia
**Estadio de Mendizorrotza, 20:00**

**Kontekst i forma**
- Alavés: 3-4. miejsce, 10 pkt (3Z-1R-1P, 11:5) — komplet 3 zwycięstw u
  siebie w tym sezonie, niepokonany na tym stadionie z Valencią od 2017 r.
- Valencia: **ostatnie miejsce w tabeli**, 1 pkt (0Z-1R-4P, **1:10** w
  bramkach — tylko 1 gol strzelony w 5 meczach). 13.09 (dwa dni przed
  meczem) klub zwolnił trenera Carlosa Corberána i CEO Rona Gourlaya;
  tymczasowo prowadzi Óscar Sánchez (trener Mestalli, pierwszy mecz).
  Sześciu zawodników kontuzjowanych (Sadiq, Caños, Copete, D. López,
  Diakhaby, Foulquier) + Tárrega zawieszony.
- Alavés bez Facundo Garcésa (zawieszenie).
- Żadna z drużyn nie gra w pucharach europejskich w tym tygodniu.

**Model bazowy (gole)** — ekstremalna przepaść formy. Zastosowano mocne
ściągnięcie skrajnie niskiego wskaźnika ataku Valencii (0,2 gola/mecz to
zbyt ekstremalna wartość jak na 5 meczów) w stronę średniej ligowej, plus
umiarkowaną korektę w górę (+20%) za możliwy "efekt nowego trenera", którą
jednak w dużej mierze niweluje lista sześciu nieobecnych zawodników.
- λ(Alavés) = **2,80** | λ(Valencia) = **0,50**

**Model rożnych** — dane obu drużyn względnie spójne między źródłami.
- λ_rożne(Alavés) = **5,0** | λ_rożne(Valencia) = **4,0**

| Wynik meczu (1X2) | % | kurs |
|---|---|---|
| Alavés wygrywa | **82%** | 1.22 |
| Remis | 11% | 9.12 |
| Valencia wygrywa | 4% | 23.18 |

**Rożne — przewaga i over/under**
| Rynek | % | kurs |
|---|---|---|
| Alavés więcej rożnych | 56% | 1.77 |
| Remis rożny | 13% | 7.81 |
| Valencia więcej rożnych | 31% | 3.26 |
| Over 9.5 | 41% | 2.42 |

**Gole**: Over 2.5 — 64% | BTTS - Tak — 36%
**Najbardziej prawdopodobny wynik**: 2-0 (14%), 3-0 (13%)

*Podsumowanie: jeden z dwóch najpewniejszych typów dnia (patrz ranking na
górze raportu) — ekstremalna przepaść formy i tabeli, jedyne ryzyko to
nieprzewidywalny "nowy trener efekt" u Valencii.*

---

### 10. Elche vs Real Madrid
**Estadio Martínez Valero, 21:30**

**Kontekst i forma**
- Real Madryt: 2. miejsce, 12 pkt (4Z-0R-1P, 14:4) — jedyna porażka w
  sezonie na wyjeździe z Betisem. Mbappé liderem klasyfikacji strzelców
  ligi (6 goli). Braki kadrowe: **Militão, Mendy, Rodrygo** (długoterminowo,
  Rodrygo może wrócić dopiero w 2027), wątpliwy Alaba — realnie cienka
  ławka środkowych obrońców. 3. mecz w 8 dniach (środa: 2:1 z Interem w LM),
  ale najbliższy mecz europejski dopiero w połowie października, więc presja
  kalendarza umiarkowana.
- Elche: 19. miejsce, 2 pkt (0Z-2R-3P, 6:13) — jedna z najgorszych
  defensyw ligi, wciąż bez zwycięstwa w sezonie. Pierwszy gol ligowy z gry
  dopiero w 5. kolejce (z karnego). Prowadzili do późnych minut z Athletic
  Bilbao, zanim stracili wynik — sygnał, że drużyna potrafi postawić się
  przez odcinki meczu.
- H2H: Real Madryt niepokonany z Elche od marca 1978 r. (!) — 17 kolejnych
  meczów bez porażki.

**Model bazowy (gole)** — ekstremalna przepaść, ale ze świadomą korektą w
górę dla Elche (+15%) za realną słabość defensywy Realu (3 kluczowych
środkowych obrońców poza grą) — to jedyna sensowna rysa na tym typie.
Korekta w dół dla Realu (-10%) za obciążenie kalendarzowe (3. mecz w 8
dniach).
- λ(Elche) = **0,90** | λ(Real Madrid) = **3,70**

**Model rożnych** — **dane wyjątkowo niespójne** między źródłami (Real
Madryt: 8,4 vs 3,6 rożnych/mecz w zależności od źródła, ponad 2x
rozbieżność) — potraktuj poniższe liczby jako orientacyjny środek
przedziału, nie precyzyjny szacunek.
- λ_rożne(Elche) = **2,8** | λ_rożne(Real Madrid) = **6,6**

| Wynik meczu (1X2) | % | kurs |
|---|---|---|
| Elche wygrywa | 5% | 20.24 |
| Remis | 8% | 11.88 |
| Real Madryt wygrywa | **78%** | 1.27 |

**Rożne — przewaga i over/under** (niska pewność danych wejściowych)
| Rynek | % | kurs |
|---|---|---|
| Elche więcej rożnych | 8% | 13.34 |
| Remis rożny | 6% | 16.14 |
| Real Madryt więcej rożnych | 86% | 1.16 |
| Over 9.5 | 47% | 2.15 |

**Gole**: Over 1.5 — 94% | Over 2.5 — 84% | BTTS - Tak — 53%
**Najbardziej prawdopodobny wynik**: 0-3 (8%), 0-4 (8%)

*Podsumowanie: drugi z najpewniejszych typów dnia. Historia (niepokonani
od 1978 r.) i różnica klas przeważają nad realnym, ale wciąż drugorzędnym
osłabieniem defensywy Realu.*

---

## Uwaga ogólna o jakości danych

Dla czterech spotkań (Liverpool–Tottenham, Peterborough–Barnsley, Reading–
Brentford, Rayo–Espanyol) statystyki rożnych są niepełne lub sprzeczne
między źródłami, a dla Elche–Real Madryt dane były wyjątkowo rozbieżne
(ponad 2x różnica między źródłami) — podane liczby potraktuj jako
orientacyjne, szersze niż zwykle przedziały niepewności, a nie precyzyjny
model. Dla meczów Ekstraklasy, Ipswich–Arsenal oraz Alavés–Valencia dane
były znacznie solidniejsze.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
