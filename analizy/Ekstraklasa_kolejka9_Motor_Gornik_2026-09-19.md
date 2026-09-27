# Motor Lublin vs Górnik Zabrze
**Rozgrywki:** PKO Ekstraklasa, kolejka 9 | **Termin:** sobota, 19.09.2026, 20:15, Motor Lublin Arena | **Ranga meczu:** lider tabeli (Górnik) na wyjeździe kontra drużyna w strefie spadkowej (Motor) — mecz o kluczowe znaczenie dla obu: Górnik broni fotela lidera, Motor walczy o ucieczkę z dołu tabeli

## Uwaga wstępna: weryfikacja terminarza kolejki 9
Kolejka 9 obejmuje mecze rozgrywane 18-20.09.2026. Dwa mecze tej kolejki —
**Widzew Łódź 2:2 Wieczysta Kraków** i **Wisła Kraków 2:1 Śląsk Wrocław** —
zostały już rozegrane w piątek 18.09 i są pominięte w tej analizie (podane
wyniki potwierdzone na ekstraklasa.org). Niniejszy raport dotyczy jednego z
dwóch meczów wytypowanych w triage jako mające obecnie największą szansę na
wysoko prawdopodobnego faworyta spośród pozostałych meczów kolejki 9.

**Wynik triage:** wstępna hipoteza zakładała Raków (wyjazd) lub Lech (dom vs
Radomiak) jako czołowych kandydatów, ale bieżąca forma tego każe zweryfikować:
Raków Częstochowa jest w historycznym kryzysie (18./ostatnie miejsce, zaledwie
3 pkt po 7 kolejkach, "najgorsza seria od ćwierćwiecza") — to czyni Koronę-
Raków meczem wysoce niepewnym, a nie pewniakiem faworyta. Lech Poznań ma za
sobą dwie porażki z rzędu (2:1 z Górnikiem, 4:0 z Crystal Palace w Europie) —
ryzyko zmęczenia/rotacji po meczu pucharowym obniża pewność typu na Lecha.
W zamian wyłoniły się dwa mocniejsze kandydaty: **Motor Lublin – Górnik
Zabrze** (ten raport) oraz **Jagiellonia Białystok – Legia Warszawa** (raport
osobny).

## Kontekst i forma
- **Forma Górnik Zabrze**: lider tabeli, 21 pkt po 8 kolejkach (7W-0R-1P),
  bilans bramkowy 16:8. Passa 5 zwycięstw z rzędu na wyjeździe i 10 meczów
  wyjazdowych bez porażki. Ostatnio pokonał Lecha Poznań (hit 8. kolejki) i
  Koronę Kielce 2:0 na wyjeździe. Sezon na wyjeździe: 2.00 gola
  strzelonego/mecz, zaledwie 0.50 gola straconego/mecz (4 mecze wyjazdowe —
  mała próba, ale bardzo spójny sygnał).
- **Forma Motor Lublin**: 15-16. miejsce, 5 pkt po 7-8 meczach, bilans
  bramkowy 8-9:13-15 (rozjazd w źródłach o 1 mecz, rząd wielkości ten sam).
  Trzy ostatnie ligowe mecze bez zdobyczy punktowej, ostatnio przegrał 2:3 z
  Legią. W domu: ok. 1.0-1.13 gola strzelonego/mecz, 1.75-1.88 gola
  straconego/mecz — forma opisywana jako "bardzo słaba".
- **H2H**: Motor nie stracił bramki w 5 z ostatnich 6 ligowych starć z
  Górnikiem i w ostatnich 3 meczach u siebie z Górnikiem z rzędu zachował
  czyste konto — istotny kontrargument wobec surowego modelu (patrz korekta
  niżej). Ostatni bezpośredni mecz (03.2025): 0:0.
- **Kadra**: brak potwierdzonych, aktualnych na dziś informacji o
  kontuzjach/zawieszeniach kluczowych zawodników dla żadnej z drużyn — starsze
  wzmianki o Luce Zahoviciu i Michalu Sacku (Górnik) mogą być nieaktualne.
  **Zaznaczam to wprost**: warto zweryfikować oficjalny skład tuż przed
  meczem, nie było możliwe potwierdzenie stanu kadry z wysoką pewnością.
- **Inne czynniki**: Górnik gra wyłącznie w lidze (brak pucharów, świeży,
  wypoczęty), Motor bez potwierdzonych obciążeń pucharowych. Presja
  motywacyjna korzystna dla obu w różny sposób — Górnik broni pozycji
  lidera, Motor gra "pod ścianą" u siebie, co bywa czynnikiem mobilizującym
  underdoga (patrz Krok 2b, ryzyko "odwrotnego wyniku" niżej).

## Model bazowy (oczekiwane gole)
Średnia ligowa Ekstraklasy 2026/27: ~2.86 gola/mecz łącznie. Rozbicie
dom/wyjazd nie było możliwe do zweryfikować precyzyjnie dla całej ligi w tym
sezonie (mała próba wczesnego sezonu) — przyjąłem typowy dla piłki
europejskiej rozkład ok. 55/45, tj. **liga_dom ≈ 1.57, liga_wyjazd ≈ 1.29**
gola/mecz. To przybliżenie, zaznaczam szerszy margines niepewności z tego
powodu.

Policzono dwa warianty siły ataku/obrony:
1. **Na bazie splitu dom/wyjazd** (Górnik wyjazd: 2.00 strzelone/0.50
   stracone; Motor dom: 1.00 strzelone/1.75 stracone) → λ_Motor ≈ 0.39,
   λ_Górnik ≈ 2.23. Próba tylko 4 mecze na stronę — wysoka wariancja.
2. **Na bazie ogólnych średnich sezonowych** (Górnik: 2.00/1.00 łącznie;
   Motor: 1.13/1.88 łącznie), skalowane do średniej ligowej dom/wyjazd →
   λ_Motor ≈ 0.87, λ_Górnik ≈ 2.37.

**Blend obu wariantów**: λ_Motor ≈ 0.63, λ_Górnik ≈ 2.30.

**Korekta jakościowa**: H2H pokazuje, że Motor broni się przeciwko Górnikowi
systematycznie lepiej niż przeciwko przeciętnemu rywalowi (czyste konto w 5/6
ostatnich starć) — prawdopodobnie kwestia ustawienia taktycznego pod tego
konkretnego przeciwnika. Obniżam λ_Górnik o ok. 13% (2.30 → **2.00**),
pozostawiając λ_Motor bez zmian, bo H2H mówi o obronie Motoru, nie o jego
ataku: **λ(Motor) = 0.70, λ(Górnik) = 2.00**.

## Model rożnych (priorytet analizy)
Dane sezonowe o rożnych dla obu drużyn są **niedostępne publicznie**
(FootyStats blokuje tę statystykę za paywallem, FBref nie miał pełnego
rozbicia dla Ekstraklasy w momencie research). To jedna z sytuacji opisanych
w SKILL.md, gdzie trzeba oszacować szerzej zamiast zmyślać precyzyjną liczbę.

Dostępne punkty odniesienia:
- Średnia ligowa Ekstraklasy 2026/27 (mała próba, 13 meczów): **10.85
  rożnych/mecz łącznie**, z rozbiciem 5.15 dla gospodarzy / 5.69 dla gości —
  nietypowy układ (goście więcej niż gospodarze), potencjalnie artefakt małej
  próby, ale odnotowuję to jako sygnał.
- Jedyny znaleziony konkretny punkt danych dla tego starcia: ostatni H2H
  (03.2025) zakończył się 3 rożne Motor – 6 rożnych Górnik.
- Górnik ma wyższą skuteczność strzałów (4.88 celnych z 13.5 prób) i jest
  zespołem dominującym terytorialnie na wyjeździe (0.50 gola straconego/mecz
  away = bardzo niska ekspozycja defensywna, dużo czasu w ataku pozycyjnym).
  Motor ma więcej strzałów ogółem (14.75/mecz) ale niższą skuteczność (4.38
  celnych) — może to generować pewną liczbę rożnych z zablokowanych strzałów.

**Szacunek (szeroki, z zaznaczoną niepewnością)**: λ_rożne(Motor) ≈ **4.2**,
λ_rożne(Górnik) ≈ **5.8** — oparte na średniej ligowej skorygowanej w stronę
przewagi terytorialnej Górnika (spójne z jedynym znalezionym H2H 3:6) i
ogólnym stylu obu drużyn. Realny zakres: Motor 3-6, Górnik 4-8.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Motor Lublin wygrywa | 12.1% | 8.29 |
| Remis | 20.0% | 5.00 |
| **Górnik Zabrze wygrywa** | **67.5%** | **1.48** |

*Uzasadnienie: przepaść formy (lider vs 15./16. miejsce), dominująca passa
wyjazdowa Górnika i słaby domowy bilans Motoru dają wyraźną przewagę
Górnikowi. Korekta w dół z surowego modelu (byłoby ~70-75% bez korekty H2H)
odzwierciedla to, że Motor historycznie "zamyka" Górnika defensywnie lepiej
niż przeciętny rywal.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Motor więcej rożnych | 25.2% | 3.97 |
| Remis rożny | 11.3% | 8.84 |
| Górnik więcej rożnych | 63.5% | 1.58 |
| Over 8.5 | 66.7% | 1.50 |
| Over 9.5 | 54.2% | 1.84 |
| Over 10.5 | 41.7% | 2.40 |

- Motor: λ_rożne ≈ 4.2 (zakres 3-6)
- Górnik: λ_rożne ≈ 5.8 (zakres 4-8)
- Łącznie: λ ≈ 10.0 (zakres ~8-13)

*Uzasadnienie: przewaga terytorialna Górnika przekłada się też na rożne, choć
nie tak jednoznacznie jak na gole — Motor mimo słabej formy generuje sporo
strzałów (14.75/mecz), co utrzymuje jego udział w rożnych na rozsądnym
poziomie. Ze względu na brak twardych danych sezonowych o rożnych, traktuj tę
sekcję jako solidny, ale szerszy niż zwykle przedział niepewności.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-1 | 13.4% | 7.44 |
| 0-2 | 13.4% | 7.44 |
| 1-1 | 9.4% | 10.63 |
| 1-2 | 9.4% | 10.63 |
| 0-3 | 9.0% | 11.16 |
| 0-0 | 6.7% | 14.88 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 75.1% | 1.33 |
| Over 2.5 | 50.6% | 1.97 |
| Over 3.5 | 28.6% | 3.50 |
| BTTS - Tak | 43.3% | 2.31 |
| BTTS - Nie | 56.7% | 1.76 |

*Uzasadnienie: rozkład skoncentrowany wokół zwycięstwa Górnika 1-2 bramkami
różnicy, BTTS lekko poniżej 50% — spójne z solidną obroną Górnika na wyjeździe
i historycznie twardą obroną Motoru akurat przeciwko temu rywalowi.*

### Strzały i strzały celne
- Motor: strzały ~13-16/mecz, celne ~3-6/mecz (średnia sezonowa 14.75 / 4.38)
- Górnik: strzały ~11-16/mecz, celne ~4-6/mecz (średnia sezonowa 13.5 / 4.88)
- Górnik jest bardziej efektywny (wyższy % celności mimo mniejszej liczby
  prób) — spójne z lepszą jakością ataku pozycyjnego lidera tabeli.

### Faule i kartki
**Drużynowo:**
- Motor: ~12.25 fauli/mecz (sezonowa średnia)
- Górnik: ~12.13 fauli/mecz (sezonowa średnia)
- Łącznie fauli w meczu: przedział ~22-26, średnio ~24.4 — obie drużyny w
  normie ligowej, brak istotnej asymetrii dyscyplinarnej
- Dane o kartkach (żółte/czerwone) są zablokowane w publicznie dostępnych
  źródłach (FootyStats premium) — nie udało się potwierdzić z wystarczającą
  pewnością, pomijam szczegółową tabelę kartek zamiast zgadywać

**Indywidualnie:** nie udało się znaleźć wiarygodnych, aktualnych danych o
zawodnikach na progu zawieszenia ani liderach fauli per 90 minut dla żadnej z
drużyn w dostępnych źródłach — zaznaczam to wprost zamiast zmyślać nazwiska.
Profil dyscyplinarny drużynowy obu zespołów jest w normie ligowej, więc nie
zastosowano dodatkowej korekty λ z tego tytułu.

## Podsumowanie
Górnik Zabrze jako lider tabeli z imponującą serią wyjazdową (5 zwycięstw z
rzędu, 10 meczów bez porażki na wyjeździe, tylko 0.5 gola straconego/mecz w
gościach) jest wyraźnym faworytem przeciwko Motorowi, który jest w kryzysie
formy (3 kolejne mecze bez punktu, 15./16. miejsce). Model daje Górnikowi
67.5% szans na zwycięstwo — solidny, ale nie ekstremalny poziom pewności,
świadomie skorygowany w dół względem surowych 70-75% z powodu specyficznego
H2H (Motor broni się przeciwko Górnikowi wyraźnie lepiej niż przeciętnie).
**Ryzyko "odwrotnego wyniku"** (Motor wygrywa) jest realne, choć niższe niż
ryzyko remisu — historia bezpośrednich starć i desperacka motywacja gospodarza
"pod ścianą" tabeli to czynniki warte odnotowania, nawet jeśli model wciąż
wyraźnie faworyzuje gościa. W rożnych przewaga Górnika jest wyraźna, ale
oparta na szerszym niż zwykle oszacowaniu z powodu braku publicznych danych
sezonowych — traktuj tę część z dodatkową ostrożnością.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
