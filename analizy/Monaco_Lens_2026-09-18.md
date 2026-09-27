# AS Monaco vs RC Lens
**Rozgrywki:** Ligue 1, kolejka 5 | **Termin:** piątek, 18.09.2026, 20:45 (Stade Louis-II) | **Ranga meczu:** starcie środka/czoła tabeli — Monaco walczy o czołówkę, Lens ratuje start sezonu

## Kontekst i forma
- **Forma Monaco** (ostatnie 4 Ligue 1): 3W-1D, niepokonane, 2. miejsce w tabeli z 10 pkt. Dom: 2 mecze, 2,0 gola strzelone/mecz, 0 straconych (bardzo mała próbka, ale wyjątkowo solidna defensywa). Szerszy zestaw danych sezonowych (mieszający więcej meczów) daje ~2,25 GF / 0,75 GA w domu.
- **Forma Lens**: 1W-1D-2L, 10. miejsce z 4 pkt. **Tydzień temu zwolniono trenera Dino Toppmöllera** — drużyną tymczasowo kieruje Yannick Cahuzac. Braki kadrowe: Nawrocki, Baidoo, Chávez, Titraoui niedostępni; wracają Abdulhamid, Ganiou, Gradit. Na wyjeździe Lens traci sporo (1,5-2,0 GA/mecz w różnych próbkach).
- **H2H**: bilans historyczny Monaco 17W-16D-12L (inne źródło: 10-8-6 w ostatnich 24 starciach). W ostatnich 5 bezpośrednich: Monaco 2W-1D-2L, Lens 2W-1D-2L — bardzo wyrównane, ostatni mecz wygrało Monaco 3-2 na wyjeździe u Lens.
- **Kadra Monaco**: pełna dyspozycyjność kluczowych zawodników w ataku (Ansu Fati, Balogun, Akliouche, Golovin).
- **Inne czynniki**: zmiana trenera u Lens tuż przed wyjazdowym meczem z mocniejszym rywalem to klasyczny czynnik ryzyka — może wywołać krótkotrwały "nowy-trener bounce" (większa mobilizacja), ale też oznacza niestabilność taktyczną i osłabioną kadrę.

## Model bazowy (oczekiwane gole)
- Dane sezonowe są jeszcze bardzo skąpe (4-5 kolejek), więc współczynniki ataku/obrony liczone czysto z average'ów sezonowych miałyby szeroki margines błędu. Oparto się na średniej ważonej dostępnych danych (2 różne okna: ostatnie 2 mecze domowe vs szersza próbka) oraz jakościowej ocenie formy/kadry.
- Korekta w dół dla Lens: brak 4 zawodników + tymczasowy trener = mniejsza spójność defensywna i ofensywna.
- Korekta w górę dla Monaco: fenomenalna forma domowa (0 straconych w 2 meczach), pełna kadra.
- λ(Monaco) = 1,90, λ(Lens) = 1,10

## Model rożnych (priorytet analizy)
- Dane o rożnych za ten sezon są zastrzeżone (premium) na głównych serwisach — oszacowano na bazie stylu gry i średniej ligowej (Ligue 1 ~9,5-10 rożnych/mecz łącznie).
- Monaco: drużyna grająca szeroko (Vanderson, Nazinho jako wahadłowi, Golovin kreujący z boku), dużo posiadania w domu → powyżej średniej.
- Lens: mimo formy, styl pressingujący generuje rożne nawet na wyjeździe, ale osłabiona defensywa może oznaczać więcej gry pod własnym polem karnym Monaco (więcej okazji rożnych dla gospodarzy z odbitych/zablokowanych dośrodkowań).
- λ_rożne(Monaco) = 5,60, λ_rożne(Lens) = 4,20 — **przybliżenie, oznaczone jako mniej pewne z powodu braku publicznie dostępnych danych rożnych per drużyna.**

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Monaco wygrywa | 55,7% | 1,80 |
| Remis | 22,3% | 4,49 |
| Lens wygrywa | 21,7% | 4,61 |

*Uzasadnienie: model bazowy daje Monaco wyraźną, ale niedrastyczną przewagę. **Kalibracja (Krok 2b):** to typ w przedziale 50-85% pewności, gdzie zarówno remis, jak i "odwrotny wynik" (Lens wygrywa) są porównywalnym ryzykiem — Lens ma świeżą zmianę trenera tuż przed wyjazdem do silniejszego rywala, co historycznie bywało źródłem niespodzianek (efekt "nowej miotły"/desperackiej mobilizacji), mimo wyraźnej różnicy klasy i formy. Dlatego zamiast typować czyste "1", bezpieczniejszym typem jest podwójna szansa 1X.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Monaco więcej rożnych | 61,2% | 1,63 |
| Remis rożny | 11,7% | 8,52 |
| Lens więcej rożnych | 27,0% | 3,70 |
| Over 8,5 | 64,4% | 1,55 |
| Over 9,5 | 51,7% | 1,93 |
| Over 10,5 | 39,2% | 2,55 |

- Monaco: λ = 5,60 (realny zakres ~4-7)
- Lens: λ = 4,20 (realny zakres ~3-6)
- Łącznie: λ ≈ 9,8, realny zakres ~7-13

*Uzasadnienie: gospodarz dominujący terytorialnie w ataku pozycyjnym generuje najwięcej rożnych; Over 8,5 to najsolidniejszy sygnał w tej sekcji.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-1 | 10,4% | 9,61 |
| 2-1 | 9,9% | 10,12 |
| 1-0 | 9,5% | 10,57 |
| 2-0 | 9,0% | 11,13 |
| 3-1 | 6,3% | 15,97 |
| 1-2 | 5,7% | 17,47 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 80,1% | 1,25 |
| Over 2,5 | 57,7% | 1,73 |
| Over 3,5 | 35,3% | 2,83 |
| BTTS - Tak | 56,5% | 1,77 |
| BTTS - Nie | 43,5% | 2,30 |

*Uzasadnienie: obie drużyny mają ofensywny potencjał (Monaco 2,25 GF/mecz w domu w szerszej próbce, Lens z Thauvin/Édouard), stąd solidne BTTS i Over 2,5.*

### Strzały i strzały celne
- Brak wystarczająco świeżych, publicznie dostępnych danych sezonowych 2026-27 (zbyt mała próbka meczów) — pominięto zamiast zgadywać.

### Faule i kartki
**Drużynowo:**
- Monaco: ~10,5 fauli/mecz popełnionych, ~10,0 sprowokowanych
- Lens: ~11,5 fauli/mecz popełnionych, ~13,25 sprowokowanych (drużyna częściej faulowana — możliwe więcej rzutów wolnych w ich strefach ofensywnych)
- Łącznie: przedział ~21-23 fauli, średnio ~22

**Indywidualnie:** brak świeżych, wiarygodnych danych per zawodnik dla obu klubów w tym sezonie (zbyt wczesny etap) — nie zgadujemy nazwisk/liczb. Brak sygnałów o zawodnikach na progu zawieszenia.

**Wniosek dla modelu:** profil dyscyplinarny w normie, bez podstaw do dodatkowej korekty λ goli.

## Podsumowanie
Monaco jest wyraźnym faworytem dzięki fenomenalnej formie domowej i pełnej kadrze, ale świeża zmiana trenera u Lens (zwolnienie Toppmöllera, tymczasowy sztab) to realny czynnik niepewności — w przedziale pewności 50-85% ryzyko remisu i "odwrotnego wyniku" są porównywalne, dlatego rekomendowanym typem jest podwójna szansa 1X (77,9%) zamiast czystego "1". W rożnych Monaco ma wyraźną przewagę terytorialną — Over 8,5 to najmocniejszy sygnał tej sekcji, choć dane bazowe są przybliżone z uwagi na ograniczoną dostępność statystyk rożnych.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
