# OGC Nice vs LOSC Lille
**Rozgrywki:** Ligue 1, kolejka 5 | **Termin:** niedziela, 20.09.2026, 17:15 (Allianz Riviera, Nice) | **Ranga meczu:** starcie skrajów tabeli — lider (Lille) kontra ostatnie miejsce (Nice)

## Kontekst i forma
- **Forma Nice** (ostatnie 4 Ligue 1): 0W-2D-2L, 18. (ostatnie) miejsce z 2 pkt, najsłabszy atak ligi — **tylko 1 gol strzelony w 4 meczach** (0,25/mecz), 5 straconych. Bilans: 0-0 z Lorient (dom), 1-1 z Le Mans (dom), 0-3 u Paris FC, 0-1 u Auxerre. Ciekawy rozjazd dom/wyjazd: w domu Nice broni się solidnie (1 stracony w 2 meczach, 2 remisy), ale na wyjeździe katastrofa (0 strzelonych, 4 stracone w 2 meczach). Trener Olivier Pantaloni (latem z Lorient) pod presją, start sezonu trudniejszy niż zakładano.
- **Forma Lille**: 3W-1D-0L, niepokonane, 2. miejsce z 10 pkt, najlepsza defensywa ligi (2 stracone w 4 meczach, 3 czyste konta na 4 mecze). Atak solidny (7 strzelonych, 1,75/mecz), na wyjeździe wyjątkowo skuteczny: 1,5 gola/mecz strzelone, **0 straconych w 2 meczach wyjazdowych** (mała próbka, potraktowana z rezerwą w modelu).
- **H2H**: historycznie wyrównane (Nice 11W, remisy 15, Lille 7W w całej historii — mało miarodajne dla obecnej formy). Istotniejsze: **w ostatnim bezpośrednim spotkaniu (29.10.2025) Nice wygrało 2-0 u siebie** — sygnał, że Nice potrafi się zmobilizować akurat przeciw Lille na własnym stadionie, mimo ogólnie fatalnej formy. To realny czynnik ryzyka dla czystego typu "Lille wygrywa".
- **Kadra**: Nice — kontuzjowani Mendy, Abergel, Bombito (w fazie powrotu), Ben Idder (sprawy administracyjne), Sanson niepewny. Lille — brak Igamane (kontuzja, świeży letni transfer) oraz Nianzou i Srdanovic niedostępni, co osłabia opcje ofensywne/rotacyjne, ale podstawowy skład (Özer, Alexsandro, E. Mbappé, Haraldsson, Ueda) do dyspozycji.
- **Inne czynniki**: Nice gra u siebie z pełną desperacją (ostatnie miejsce, presja na trenera), co historycznie bywa czynnikiem podbijającym intensywność underdoga w pierwszej połowie. Lille nie ma jeszcze presji strefowej (2. miejsce), ale to wciąż wczesny etap sezonu.

## Model bazowy (oczekiwane gole)
- Dane sezonowe pochodzą z zaledwie 4 kolejek — surowe współczynniki (Nice atak vs Lille obrona) dałyby ekstremalnie niską wartość (rząd 0,1 gola) przez złożenie dwóch skrajnych wskaźników z małej próby. Zastosowano więc **regresję (shrinkage) współczynników siły ataku/obrony w kierunku średniej ligowej** (wagi ok. 40% dane surowe / 60% średnia), żeby uniknąć fałszywej precyzji przy n=4 meczach.
- Średnia ligowa (Ligue 1, ten sezon, ok. 37 rozegranych meczów): ~2,76 gola/mecz łącznie, przyjęto ok. 1,55 gospodarz / 1,21 gość.
- Korekta jakościowa w dół dla Lille (z 1,60 do 1,50): ostatnie bezpośrednie starcie wygrane przez Nice 2-0 u siebie + brak Igamane w ataku.
- λ(Nice) = 0,70, λ(Lille) = 1,50

## Model rożnych
- Publiczne dane o rożnych są w większości zastrzeżone (premium) dla obu klubów w tym sezonie — oszacowano na bazie średniej ligowej (Ligue 1 ~9,5-10 rożnych/mecz łącznie) i stylu gry.
- Lille wg dostępnych (częściowo nieaktualnych, mieszających poprzedni sezon) danych zajmuje dopiero 16. miejsce w lidze pod względem liczby rożnych — drużyna gra bardziej zwarcie/kontratakująco (45% posiadania średnio) niż przez skrzydła, więc nie generuje rożnych masowo nawet przy przewadze.
- Nice broniące się nisko i pod ciągłą presją może oddawać rożne z zablokowanych dośrodkowań/strzałów, ale też sam ma ograniczony potencjał ofensywny do zdobywania rożnych.
- λ_rożne(Nice) = 4,2, λ_rożne(Lille) = 4,6 — **przybliżenie, oznaczone jako mniej pewne** z powodu ograniczonej dostępności publicznych danych o rożnych dla obu klubów.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Nice wygrywa | 17,4% | 5,75 |
| Remis | 26,2% | 3,82 |
| Lille wygrywa | 56,4% | 1,77 |

*Uzasadnienie: model oparty na przepaści klasowej (18. vs 2. miejsce, najgorszy atak ligi vs najlepsza obrona ligi) daje Lille wyraźną przewagę, ale nie ekstremalną. **Kalibracja (Krok 2b):** to typ w przedziale 50-85%, gdzie zarówno remis, jak i "odwrotny wynik" są realnym ryzykiem — Nice ma solidną obronę domową (1 stracony w 2 meczach u siebie) i pokonało akurat Lille 2-0 w ostatnim bezpośrednim spotkaniu. Dlatego zamiast czystego "2", solidniejszym typem jest podwójna szansa X2.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Nice więcej rożnych | 37,9% | 2,64 |
| Remis rożny | 13,5% | 7,39 |
| Lille więcej rożnych | 48,5% | 2,06 |
| Over 7,5 | 65,2% | 1,53 |
| Over 8,5 | 51,8% | 1,93 |
| Over 9,5 | 38,6% | 2,59 |

- Nice: λ = 4,2 (realny zakres ~3-6)
- Lille: λ = 4,6 (realny zakres ~3-6)
- Łącznie: λ ≈ 8,8, realny zakres ~6-12

*Uzasadnienie: bez wyraźnej dominacji rożnej żadnej ze stron (Lille niski-corner styl, Nice ograniczony potencjał) — over/under bliżej średniej ligowej niż wyraźna przewaga jednej ze stron.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-1 | 16,6% | 6,02 |
| 0-2 | 12,5% | 8,02 |
| 1-1 | 11,6% | 8,60 |
| 0-0 | 11,1% | 9,03 |
| 1-2 | 8,7% | 11,46 |
| 1-0 | 7,8% | 12,89 |
| 0-3 | 6,2% | 16,04 |
| 1-3 | 4,4% | 22,92 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 64,5% | 1,55 |
| Over 2,5 | 37,7% | 2,65 |
| Under 2,5 | 62,3% | 1,61 |
| BTTS - Tak | 39,1% | 2,56 |
| BTTS - Nie | 60,9% | 1,64 |

*Uzasadnienie: mecz najgorszego ataku ligi z najlepszą obroną ligi wskazuje na niską liczbę goli i podwyższone ryzyko "czystego konta" dla Lille — Under 2,5 i BTTS Nie to spójne, wzajemnie potwierdzające się sygnały.*

### Strzały i strzały celne
- Nice: ~10-13 strzałów/mecz (średnio ~11 w domu), ale konwersja tragiczna (~2%) — bardzo mało realnych sytuacji bramkowych mimo objętości gry
- Lille: ~9-12 strzałów/mecz (średnio ~10,75), konwersja ~16% — mniej strzałów niż Nice, ale znacznie skuteczniejsze wykończenie

### Faule i kartki
**Drużynowo:**
- Nice: ~11-12 fauli popełnionych w tym meczu (kombinacja średniej domowej Nice ~9,5 i średniej "sprowokowanych" Lille ~13,5)
- Lille: ~9-11 fauli popełnionych (kombinacja średniej Lille ~11 i średniej "sprowokowanych" Nice ~8,75)
- Łącznie: przedział ~18-24 fauli, średnio ~21,4

**Indywidualnie:** brak wiarygodnych, publicznie dostępnych danych per zawodnik dla obu klubów na tym etapie sezonu (2026-27) — nie zgadujemy nazwisk ani liczb. Brak sygnałów o zawodnikach na progu zawieszenia w znalezionych źródłach.

**Wniosek dla modelu:** profil dyscyplinarny w normie, bez podstaw do dodatkowej korekty λ goli ponad już zastosowane korekty jakościowe.

## Podsumowanie
Lille to najwyraźniejszy faworyt tej kolejki Ligue 1 dzięki połączeniu najlepszej obrony ligi i najsłabszego ataku ligi po stronie Nice, ale surowy model (56,4% na "2") nie uzasadnia ekstremalnej pewności — Nice broni się przyzwoicie u siebie i pokonało akurat Lille w ostatnim H2H. **Rekomendowany typ to podwójna szansa X2 (Lille wygra lub remis) — 82,6%, kurs uczciwy 1,21** — to znacznie bezpieczniejsza konstrukcja niż czyste zwycięstwo Lille, przy wciąż atrakcyjnym kursie. Alternatywnie Under 2,5/BTTS Nie (ok. 61-63%) dobrze oddają charakter starcia najgorszego ataku z najlepszą obroną ligi. W rożnych brak wyraźnej przewagi którejkolwiek ze stron — dane są przybliżone z uwagi na ograniczoną dostępność statystyk.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
