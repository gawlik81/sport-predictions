# Lech Poznań vs Radomiak Radom
**Rozgrywki:** PKO Ekstraklasa, kolejka 9 | **Termin:** niedziela, 20.09.2026, 20:15, Enea Stadion, Poznań | **Ranga meczu:** mistrz Polski (obecnie 3-4. miejsce po serii wyjazdowych potknięć) u siebie kontra drużyna z dolnej połowy tabeli, ostatni mecz przed przerwą reprezentacyjną

## Uwaga wstępna: triage i korekta wstępnej hipotezy
Ten mecz był jednym z typów wstępnie sugerowanych jako "pewniak" (Lech u siebie
przeciw słabszemu Radomiakowi). Weryfikacja formy pokazała, że to nadal
sensowny wybór, ale **nie tak oczywisty, jak sugerowałaby sama pozycja w
tabeli** — Lech ma za sobą dwie porażki z rzędu (2:1 w Zabrzu z Górnikiem w
9. kolejce, 4:0 na wyjeździe w Europie z Crystal Palace) oraz sygnalizowane w
prasie ubytki kadrowe. Obie ostatnie porażki padły **na wyjeździe** — domowa
forma Lecha w tym sezonie pozostaje nietknięta tą serią (6:1 w bramkach u
siebie w dotychczasowych meczach domowych) — ale sam fakt dwóch porażek z
rzędu i napięty terminarz uzasadniają pewną ostrożność względem "surowych"
liczb z modelu. Alternatywą w triage był Jagiellonia-Legia, odrzucony na
rzecz tego meczu głównie z powodu: (a) Legia ma aż 6 nieobecnych zawodników
w kadrze meczowej (w tym kluczowy środkowy obrońca Piątkowski), (b)
Jagiellonia nie przegrała żadnego z ostatnich 3 bezpośrednich starć z Legią —
te dwa czynniki razem czynią Jagiellonię-Legię wyraźnie mniej pewnym typem niż
Lech-Radomiak mimo własnych problemów kadrowych Lecha.

## Kontekst i forma
- **Forma Lech Poznań**: 3-4. miejsce, 16 pkt po 7-8 kolejkach (5W-1R-1P wg
  danych sprzed 8. kolejki), bilans bramkowy 12:6 (1.71 strzelonych/0.86
  straconych na mecz). **W domu: 6 bramek strzelonych, tylko 1 stracona**
  (dotychczasowe mecze domowe) — bardzo solidna forma gospodarza, niezależnie
  od ostatnich wyjazdowych potknięć. Ostatnie 2 mecze: porażka 1:2 w Zabrzu z
  Górnikiem (lider tabeli) i porażka 0:4 w Europie z Crystal Palace (Liga
  Konferencji) — oba na wyjeździe.
- **Forma Radomiak Radom**: 14. miejsce, 8 pkt po 8 kolejkach (2W-2R-4P),
  bilans bramkowy fatalny: 6:15 (0.75 strzelonych/1.88 straconych na mecz).
  **Na wyjeździe: zaledwie 0.33 gola strzelonego/mecz i aż 2.67 gola
  straconego/mecz** (próba 3 mecze — mała, ale spójna z ogólnie słabą formą).
  xGA (oczekiwane stracone gole) = 11.39 — trzecia najgorsza defensywa w
  lidze. Aktualna forma opisywana jako "słaba" (1.0 pkt/mecz).
- **H2H**: historyczna dominacja Lecha — Radomiak wygrał tylko 1 z ostatnich
  ~13 bezpośrednich starć w Ekstraklasie, Lech przegrał z Radomiakiem tylko
  raz w historii ligowych spotkań (2021/22). Średnio 2.6 gola/mecz w
  dotychczasowych starciach, BTTS w 70% przypadków.
- **Kadra**: Lech ma długoterminowo wykluczonego napastnika Kamila
  Jakóbczyka (kontuzja od wielu miesięcy) oraz sygnalizowane w mediach
  dodatkowe ubytki kadrowe (dokładna lista niepotwierdzona z wysoką
  pewnością w dostępnych źródłach na dziś) — **zaznaczam to wprost jako
  niepewność**, warto zweryfikować oficjalny skład przed meczem. Radomiak
  również zgłaszany jako "poważnie osłabiony" z powodu kontuzji kluczowego
  zawodnika (konkretne nazwisko niepotwierdzone z pewnością w dostępnych
  źródłach).
- **Inne czynniki**: Lech ma przed sobą bardzo zagęszczony terminarz (9 meczów
  na 3 frontach między 10.10 a 8.11), co może skłaniać trenera do pewnej
  rotacji już teraz, choć to ostatni mecz przed przerwą reprezentacyjną, więc
  presja o "uspokojenie sytuacji" zwycięstwem jest wysoka. Radomiak nie ma
  zgłoszonych czynników motywacyjnych ponad standardową walkę o punkty w
  dolnej strefie tabeli.

## Model bazowy (oczekiwane gole)
Średnia ligowa: liga_dom ≈ 1.57, liga_wyjazd ≈ 1.29 gola/mecz (przybliżenie
opisane w metodologii — patrz raport Motor-Górnik dla szczegółów).

Policzono dwa warianty:
1. **Na bazie splitu dom/wyjazd** (Lech dom: 6 strzelonych/1 stracona w ok. 4
   meczach → 1.5/0.25 na mecz; Radomiak wyjazd: 0.33/2.67 na mecz, 3 mecze) →
   λ_Lech ≈ 3.10, λ_Radomiak ≈ 0.05. Ekstremalne wartości — efekt bardzo
   małej próby (Lech stracił zaledwie 1 gola w ~4 meczach domowych, co
   statystycznie nie jest trwałe w dłuższym okresie).
2. **Na bazie ogólnych średnich sezonowych** (Lech 1.71/0.86 łącznie,
   Radomiak 0.75/1.88 łącznie), skalowane do średniej ligowej dom/wyjazd →
   λ_Lech ≈ 2.47, λ_Radomiak ≈ 0.41.

**Blend obu wariantów**: λ_Lech ≈ 2.79, λ_Radomiak ≈ 0.23.

**Korekta jakościowa**: surowy blend jest zawyżony przez efekt małej próby
(1 stracony gol w 4 meczach domowych Lecha to nietrwały wynik — regresja do
średniej jest tu uzasadniona) oraz nie uwzględnia świeżej serii 2 porażek z
rzędu i sygnalizowanych ubytków kadrowych. Obniżam λ_Lech z 2.79 do **2.30**
i podnoszę λ_Radomiak z 0.23 do **0.55** (żeby uniknąć fałszywej precyzji
"prawie zero goli" wynikającej z małej próby) — łącznie: **λ(Lech) = 2.30,
λ(Radomiak) = 0.55**.

## Model rożnych (priorytet analizy)
Podobnie jak w poprzednim raporcie, **dane sezonowe o rożnych są niedostępne
publicznie** (FootyStats płatne, brak pełnego rozbicia na FBref dla tego
sezonu Ekstraklasy) — szacunek szerszy, oparty na średniej ligowej i stylu
gry.

Punkty odniesienia:
- Średnia ligowa: 10.85 rożnych/mecz łącznie (5.15 dom / 5.69 wyjazd, mała
  próba 13 meczów).
- Lech ma wysokie posiadanie piłki (52%) i dużą liczbę strzałów (18/mecz,
  6.14 celnych) — sygnał typowy dla drużyny generującej sporo rożnych z gry
  pozycyjnej.
- Radomiak ma stosunkowo dużo strzałów jak na słabą drużynę (15/mecz), ale
  niską skuteczność (4.13 celnych) i grę bardziej z kontry/defensywną
  (48% posiadania) na wyjeździe — mniej rożnych z własnej inicjatywy, ale
  możliwe rożne z zablokowanych/odbitych ataków Lecha.

**Szacunek (szeroki)**: λ_rożne(Lech) ≈ **6.0**, λ_rożne(Radomiak) ≈ **3.8** —
podniesione względem średniej ligowej w stronę Lecha z uwagi na dominację
terytorialną i wysokie posiadanie piłki. Realny zakres: Lech 4-8, Radomiak
2-6.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| **Lech Poznań wygrywa** | **76.1%** | **1.31** |
| Remis | 15.8% | 6.34 |
| Radomiak Radom wygrywa | 7.2% | 13.85 |

*Uzasadnienie: ogromna przepaść jakościowa i formy (mistrz Polski u siebie z
solidnym bilansem domowym vs drużyna z trzecią najgorszą defensywą w lidze i
fatalną formą wyjazdową) uzasadnia wysoką pewność faworyta. Zgodnie z
kalibracją z Kroku 2b, mimo ekstremalnej przepaści, obniżyłem liczbę z
surowego modelu (~85%+) do 76% z powodu: dwóch porażek Lecha z rzędu,
sygnalizowanych ubytków kadrowych i efektu małej próby w statystykach
domowych Lecha — to nie jest automatyczna gwarancja mimo jakościowej
przepaści.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Lech więcej rożnych | 70.6% | 1.42 |
| Remis rożny | 10.2% | 9.81 |
| Radomiak więcej rożnych | 19.2% | 5.22 |
| Over 8.5 | 64.4% | 1.55 |
| Over 9.5 | 51.7% | 1.93 |
| Over 10.5 | 39.2% | 2.55 |

- Lech: λ_rożne ≈ 6.0 (zakres 4-8)
- Radomiak: λ_rożne ≈ 3.8 (zakres 2-6)
- Łącznie: λ ≈ 9.8 (zakres ~7-13)

*Uzasadnienie: dominacja terytorialna Lecha w grze pozycyjnej przekłada się
na wyraźną przewagę rożną. Podobnie jak w poprzednim raporcie, sekcja oparta
na szerszym niż zwykle oszacowaniu z powodu braku publicznych danych
sezonowych o rożnych — traktuj z dodatkową ostrożnością.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 2-0 | 15.3% | 6.54 |
| 1-0 | 13.3% | 7.52 |
| 3-0 | 11.7% | 8.53 |
| 2-1 | 8.4% | 11.88 |
| 1-1 | 7.3% | 13.67 |
| 4-0 | 6.7% | 14.83 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 77.7% | 1.29 |
| Over 2.5 | 54.2% | 1.84 |
| Over 3.5 | 31.9% | 3.13 |
| BTTS - Tak | 37.7% | 2.65 |
| BTTS - Nie | 62.3% | 1.60 |

*Uzasadnienie: rozkład wyraźnie skoncentrowany na czystym koncie Lecha (2-0,
1-0, 3-0 to trzy najbardziej prawdopodobne wyniki) — spójne z solidną
defensywą Lecha w domu i ofensywną niemocą Radomiaka na wyjeździe.*

### Strzały i strzały celne
- Lech: strzały ~15-20/mecz, celne ~5-7/mecz (średnia sezonowa 18 / 6.14)
- Radomiak: strzały ~12-17/mecz, celne ~3-5/mecz (średnia sezonowa 15 / 4.13)
- Lech wyraźnie bardziej efektywny mimo podobnej objętości strzałów — spójne
  z przepaścią jakościową.

### Faule i kartki
**Drużynowo:**
- Lech: ~12.43 fauli/mecz (sezonowa średnia)
- Radomiak: ~13.63 fauli/mecz (sezonowa średnia, nieco wyżej niż Lech —
  typowe dla drużyny broniącej się więcej i grającej z kontry)
- Łącznie fauli w meczu: przedział ~23-27, średnio ~26.1 — obie drużyny w
  normie ligowej, Radomiak nieznacznie bardziej faulujący jako spodziewany
  defensywny underdog na wyjeździe
- Dane o kartkach zablokowane w publicznie dostępnych źródłach — pomijam
  szczegółową tabelę zamiast zgadywać.

**Indywidualnie:** nie udało się potwierdzić z wystarczającą pewnością
konkretnych nazwisk zawodników na progu zawieszenia ani liderów fauli/90 min
dla żadnej z drużyn w dostępnych źródłach na dziś — zaznaczam to wprost.
Profil dyscyplinarny drużynowy w normie ligowej, brak dodatkowej korekty λ.

## Podsumowanie
Lech Poznań pozostaje wyraźnym faworytem u siebie przeciwko Radomiakowi,
który ma trzecią najgorszą defensywę ligi i fatalną formę wyjazdową (0.33
gola strzelonego, 2.67 straconego na mecz w gościach). Model po korektach
jakościowych daje Lechowi 76.1% szans na zwycięstwo — wysoki, ale świadomie
niższy niż surowy wynik modelu (~85%+), z powodu dwóch ostatnich porażek
Lecha z rzędu (obie na wyjeździe, więc mniej bezpośrednio przekładają się na
mecz domowy, ale to wciąż sygnał ostrzegawczy) i sygnalizowanych, w pełni
niepotwierdzonych ubytków kadrowych. **Ryzyko remisu i "odwrotnego wyniku"
są tu niższe niż typowo dzięki ogromnej przepaści jakościowej**, ale nie
zerowe — Radomiak nie jest w typowym "kryzysie desperacji" (zmiana trenera,
seria bez gola), więc nie zastosowano dodatkowej korekty z tego tytułu poza
już wspomnianą ostrożnością po stronie Lecha. W rożnych przewaga Lecha jest
wyraźna, ale oparta na szerszym niż zwykle oszacowaniu z powodu braku
publicznych danych sezonowych.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
