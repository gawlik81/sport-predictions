# Venezia vs Lazio
**Rozgrywki:** Serie A, kolejka 5 | **Termin:** sobota, 19.09.2026, 20:45 (Stadio Pier Luigi Penzo, Wenecja) | **Ranga meczu:** ostatnia drużyna tabeli (0 pkt, 4 porażki z rzędu) przyjmuje drużynę z 3. miejsca — ale to też mecz "być albo nie być" dla trenera Wenecji

## Kontekst i forma
- **Forma Venezia** (4 mecze ligowe): 0W-0D-4L, **0 punktów, ostatnie miejsce w tabeli**. GF 4 / GA 11 (różnica -7). Cztery porażki z rzędu (m.in. 2-4 z Fiorentiną, 2-3 z Frosinone, 1-2 z Udinese, 0-2 z Milanem), do tego odpadnięcie z Pucharu Włoch (13 goli straconych w 5 meczach łącznie).
- **Forma Lazio**: 3W-1D-0L, 10 pkt, 3. miejsce (ex aequo z Como i Milanem), **niepokonana**. GF 6 / GA 3 w 4 meczach — bardzo solidna obrona (1,5 GF / 0,75 GA na mecz). W ostatnich 2 meczach wyjazdowych (Udinese, Bolonia) Lazio zachowała czyste konto ofensywne rywali w jednym i minimalną stratę w drugim.
- **Kadra — kluczowy czynnik jakościowy**: Venezia ma **siedmiu** zawodników niedostępnych (Bella-Kotchap, Sverko, Franjic, Basic, Busio, Dagasso, Adorante) — w tym prawdopodobnie kilku obrońców, co pogłębia i tak fatalną defensywę. Lazio brakuje Marusicia i Rovelli (ważni, ale niekluczowi dla podstawowego składu).
- **Czynnik trenerski — realne ryzyko dla modelu**: trener Wenecji Giovanni Stroppa jest, według wielu włoskich źródeł z ostatnich dni (12-18.09), **"na krawędzi zwolnienia"** — klub rozważa zastąpienie go D'Aversą lub Tudorem w razie kolejnej porażki. To mecz opisywany lokalnie jako "vincere o morire" (wygrać albo zginąć) dla trenera — silny motyw desperackiej mobilizacji drużyny i kibiców przed własną publicznością.

## Model bazowy (oczekiwane gole)
- Średnia ligowa Serie A 2026-27: 3,03 gola/mecz (bardzo wysoki, ofensywny sezon). Przyjęto szacunkowy podział dom/wyjazd ok. 54%/46% → **śr. ligowa dom ≈ 1,63, wyjazd ≈ 1,40**.
- Siła ataku Venezia (dom, 1 mecz u siebie: 2,0 GF) ÷ 1,63 ≈ 0,68 (szacunek na bazie sezonu ogólnego, skorygowany w dół — bardzo mała próbka domowa, n=1); siła obrony Venezia (dom) ≈ 2,8 GA/mecz ÷ 1,63 ≈ 1,72 (drużyna wyjątkowo dziurawa defensywnie, dodatkowo osłabiona 7 nieobecnościami)
- Siła ataku Lazio (wyjazd, śr. sezonowa skorygowana in minus z uwagi na małą próbkę n=2: ~1,4 GF/mecz) ÷ 1,40 ≈ 1,00; siła obrony Lazio (wyjazd, ~0,9 GA/mecz, regresja w stronę średniej sezonowej z małej próbki 0,5) ÷ 1,63 ≈ 0,64
- λ_home(Venezia) = 0,68 × 0,64 × 1,63 ≈ 0,71; λ_away(Lazio) = 1,00 × 1,72 × 1,40 ≈ 2,40 → **model surowy: Lazio wygrywa 73,7%** (kurs uczciwy 1,36)
- **Korekta jakościowa pewności (Krok 2b skilla)**: Venezia to autentycznie kryzysowy underdog — seria porażek + mecz "o posadę trenera" + desperacka motywacja domowej publiczności to dokładnie scenariusz, w którym historyczna weryfikacja predykcji pokazała powtarzalne niespodzianki (por. przypadek Alavés-Valencia). Jednocześnie 7 nieobecności ogranicza realną zdolność Venezii do "buntu" wynikowego. Stosuję realną korektę w dół: **-7 pkt proc. z prawdopodobieństwa Lazio**, rozłożone głównie na remis (najbardziej prawdopodobny scenariusz "desperackiej, zorganizowanej obrony" gospodarzy) i nieco na zwycięstwo Venezii.
- **Finalne, skorygowane 1X2**: Venezia 12%, Remis 22%, Lazio 66% (patrz tabela niżej) — to jest wynik użyty jako rekomendacja, nie surowy wynik modelu.

## Model rożnych (priorytet analizy)
- Venezia: dane wskazują na najniższą w lidze liczbę rożnych w swoich meczach (~6,5 łącznie) — drużyna broniąca się nisko i rzadko atakująca skrzydłami.
- Lazio: ok. 5,0 rożnych zdobytych/mecz — poniżej średniej ligowej, zespół preferujący grę przez środek.
- **Uwaga o jakości danych**: źródła dla obu klubów są niejednoznaczne (niejasne, czy podane liczby to "zdobyte", czy łączne w meczu) — oszacowano ostrożnie na bazie stylu gry i ogólnej średniej ligowej (9,15/mecz: dom 4,82 / wyjazd 4,32).
- λ_rożne(Venezia, dom) = 3,10, λ_rożne(Lazio, wyjazd) = 6,70 — **szacunek z podwyższoną niepewnością, dane źródłowe niejednoznaczne.**

## Prawdopodobieństwa

### Wynik meczu (1X2) — po korekcie jakościowej
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Venezia wygrywa | 12,0% | 8,33 |
| Remis | 22,0% | 4,55 |
| Lazio wygrywa | 66,0% | 1,52 |

*Uzasadnienie: model surowy dawał Lazio aż 73,7%, ale to typowy scenariusz "kryzysowego underdoga" (seria porażek + mecz o posadę trenera + desperacka mobilizacja przed własną publicznością) — zgodnie z metodologią skilla (Krok 2b) zastosowano realną korektę w dół o 7 pkt proc. Jednocześnie 7 nieobecności w kadrze Venezii ogranicza ryzyko pełnego "buntu wynikowego", więc korekta jest umiarkowana, a nie drastyczna. Lazio pozostaje wyraźnym faworytem, ale to typ do traktowania ze średnią, nie maksymalną pewnością.*

### Rożne — przewaga i over/under (sekcja priorytetowa)
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Venezia więcej rożnych | 9,0% | 11,07 |
| Remis rożny | 6,8% | 14,80 |
| Lazio więcej rożnych | 84,1% | 1,19 |
| Over 7,5 | 76,1% | 1,31 |
| Over 8,5 | 64,4% | 1,55 |
| Over 9,5 | 51,7% | 1,93 |
| Over 10,5 | 39,2% | 2,55 |

- Venezia: λ = 3,10 (realny zakres ~1-6)
- Lazio: λ = 6,70 (realny zakres ~4-10)
- Łącznie: λ ≈ 9,8, realny zakres ~6-14

*Uzasadnienie: przewaga rożna Lazio jest bardzo wyraźna w modelu, ale kurs uczciwy (1,19) jest już bardzo krótki i dane źródłowe dla obu klubów są niepewne — traktować jako sygnał kontekstowy, nie jako najmocniejszy typ meczu.*

### Najbardziej prawdopodobne wyniki (gole, model surowy)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-2 | 12,9% | 7,79 |
| 0-1 | 10,7% | 9,34 |
| 0-3 | 10,3% | 9,73 |
| 1-2 | 9,1% | 10,96 |
| 1-1 | 7,6% | 13,16 |
| 1-3 | 7,3% | 13,71 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 81,7% | 1,22 |
| Over 2,5 | 60,1% | 1,66 |
| Over 3,5 | 37,7% | 2,65 |
| BTTS - Tak | 45,6% | 2,19 |
| BTTS - Nie | 54,4% | 1,84 |

*Uzasadnienie: dziurawa defensywa Venezii (2,75 GA/mecz w sezonie) w połączeniu z solidnym atakiem Lazio sprzyja Over 2,5, ale BTTS-Nie jest lekko faworyzowane — Venezia może nie strzelić wcale, biorąc pod uwagę 7 nieobecności w ataku/pomocy.*

### Strzały i strzały celne
- Brak wystarczająco wiarygodnych, jawnych danych sezonowych o strzałach dla obu klubów — pominięto zamiast zgadywać.

### Faule i kartki
**Drużynowo:** brak precyzyjnych, jawnych danych sezonowych o faulach/kartkach per drużyna. Kontekstowo: drużyna w kryzysie, grająca "o wszystko" przed własną publicznością, często generuje podwyższone ryzyko kartek (faule taktyczne, nerwowość) — sygnał jakościowy, nie potwierdzony liczbami.

**Indywidualnie:** brak wiarygodnych danych per zawodnik dla obu klubów — nie podajemy zmyślonych liczb. Brak potwierdzonych sygnałów o zawodnikach na progu zawieszenia.

**Wniosek dla modelu:** kryzys trenerski i kadrowy Wenecji już uwzględniono jako korektę jakościową 1X2 powyżej (Krok 2b) — to najważniejszy czynnik pozastatystyczny całej analizy.

## Podsumowanie
Lazio jest wyraźnym faworytem dzięki formie, jakości obrony i fatalnej sytuacji kadrowej Venezii (7 nieobecnych), ale to mecz z podwyższonym ryzykiem niespodzianki — Venezia gra "o posadę trenera" przed własną publicznością, co w historycznej weryfikacji tego typu predykcji bywało źródłem zaskoczeń. Dlatego rekomendowana pewność typu Lazio to 66% (po korekcie), a nie surowe 73,7% z modelu — traktować jako typ o średniej, nie maksymalnej pewności. Najmocniejszym liczbowo sygnałem pozostaje przewaga rożna Lazio (84,1%), ale przy bardzo krótkim kursie i niepewnych danych źródłowych.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
