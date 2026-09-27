# Sevilla vs Barcelona
**Rozgrywki:** La Liga (jornada 7) | **Termin:** sobota 19.09.2026, 21:00 (Estadio Ramón Sánchez-Pizjuán) | **Ranga meczu:** starcie liderów tabeli — Barcelona (1. miejsce) na wyjeździe u Sevilli (4. miejsce), ostatni mecz Barcy przed przerwą reprezentacyjną

## Kontekst i forma
- **Forma Barcelony**: komplet 6W-0D-0L w lidze (28:6), 7 zwycięstw z rzędu we wszystkich rozgrywkach — nowy rekord klubowy na start sezonu. Lamine Yamal 8 goli i 4 asysty w 7 występach, Raphinha 11 goli i 3 asysty w 7 występach. Absolutnie wyjątkowe tempo strzeleckie (4,67 gola/mecz w lidze).
- **Forma Sevilli**: 13 pkt z 6 meczów (4W-1D-1L, 9:6), Luis García Plaza. 7 punktów z ostatnich 3 spotkań — remis z Espanyolem, zwycięstwa nad Valencią i Deportivo (dobra passa, solidna obrona).
- **H2H**: Barcelona wygrała 8 z ostatnich 9 starć, a w ostatnich 30 meczach ma bilans 22W-5D-3L (72:26 bramek) — dominacja generalna. **Ale konkretnie na Pizjuánie Sevilla ma swój "straszak"**: pokonała tu Barcelonę 4-1 w październiku ubiegłego sezonu i wygrała u siebie z Barçą 3 razy od 2019 roku. To realny czynnik ryzyka specyficzny dla tego stadionu.
- **Kadra**: Sevilla bez Rubéna Vargasa (poważny uraz kolana) i Arouny Sangante (kostka), Lucas Stassin wątpliwy. Barcelona bez Frenkiego de Jonga i Roony'ego Bardghjiego — ubytki drugoplanowe, nie osłabiają linii ataku.
- **Inne czynniki**: to ostatni mecz Barcelony przed przerwą reprezentacyjną — niewielkie ryzyko rotacji/spadku koncentracji, ale przy takiej serii zwycięstw trener raczej nie eksperymentuje z kluczowym składem.

## Model bazowy (oczekiwane gole)
Siła ataku/obrony liczona względem średniej ligowej tego młodego sezonu (6-7 kolejek, ok. 1,65 gola/mecz gospodarzy, 1,40 gola/mecz gości, 1,53 ogółem). Surowy model dawał λ(Barcelona) ≈ 3,05 — uznałem to za nierealistyczne przeszacowanie napędzane wyjątkowo gorącym otwarciem sezonu (28 goli w 6 meczów to tempo trudne do utrzymania) i **skorygowałem w dół** o typowe zjawisko regresji do średniej oraz specyficzny opór Sevilli na własnym stadionie wobec Barçy (H2H w Pizjuánie). λ(Sevilla) lekko podniesione względem surowego wyliczenia z uwagi na dobrą bieżącą formę gospodarzy.

- λ(Sevilla) = 1,05, λ(Barcelona) = 2,35

## Model rożnych
λ liczone z połączenia średnich "for"/"against": Barcelona ~8,0 rożnych/mecz (zdobywanych) — bardzo wysoko, odzwierciedla przewagę w posiadaniu i grze pod polem karnym rywala. Sevilla ~3,7 rożnego/mecz (zdobywanych) — wyraźnie mniej. **Dane o rożnych oddanych przez obie drużyny są niepełne w tak młodym sezonie — to przybliżenie, nie precyzyjny model "for/against"**, dlatego szerszy margines niepewności niż zwykle.

- λ_rożne(Sevilla) = 3,8, λ_rożne(Barcelona) = 6,5

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Sevilla | 15,4% | 6,49 |
| Remis | 18,3% | 5,47 |
| Barcelona | 65,3% | 1,53 |
| **Barcelona — podwójna szansa (X2)** | **83,5%** | **1,20** |

*Uzasadnienie: przepaść klasowa i formy jest wyraźna, ale nie ekstremalna — Sevilla to zdrowa, dobrze prowadzona drużyna w dobrej passie (nie żaden kryzysowiec), a konkretnie na tym stadionie ma udokumentowaną historię psucia Barcelonie serii (4-1 w ub. sezonie, 3 domowe zwycięstwa od 2019). Podwójna szansa X2 znacząco redukuje to ryzyko przy nadal solidnym kursie.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Sevilla więcej rożnych | 15,6% | 6,40 |
| Remis rożny | 8,9% | 11,18 |
| Barcelona więcej rożnych | 75,3% | 1,33 |
| Over 8,5 | 70,0% | 1,43 |
| Over 9,5 | 57,9% | 1,73 |
| Over 10,5 | 45,4% | 2,20 |

*Uzasadnienie: Barcelona dominuje w posiadaniu i grze w polu karnym rywala niemal w każdym meczu tego sezonu — przewaga rożna to jeden z najbardziej stabilnych sygnałów w tym meczu.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-2 | 9,7% | 10,33 |
| 0-2 | 9,2% | 10,85 |
| 1-1 | 8,2% | 12,14 |
| 0-1 | 7,8% | 12,75 |
| 1-3 | 7,6% | 13,19 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 85,3% | 1,17 |
| Over 2,5 | 66,0% | 1,51 |
| Over 3,5 | 44,2% | 2,26 |
| BTTS — Tak | 58,1% | 1,72 |
| BTTS — Nie | 41,9% | 2,39 |

*Uzasadnienie: przy ataku Barcelony strzelającym średnio niemal 5 goli/mecz, Over 1,5 to praktycznie formalność niezależnie od wyniku — jeden z najbezpieczniejszych rynków w całej analizie.*

### Strzały i strzały celne
- Sevilla: ok. 9-12 strzałów, 3-5 celnych
- Barcelona: ok. 15-19 strzałów, 7-10 celnych — zdecydowanie dominująca objętość gry ofensywnej

### Faule i kartki
**Drużynowo (dane orientacyjne, sezon 2026/27 wciąż krótki):** obie drużyny dyscyplinarnie w normie — Sevilla i Barcelona historycznie należą do drużyn z mniejszą liczbą fauli/kartek w lidze (Barcelona jedna z najbardziej zdyscyplinowanych w ub. sezonie: 42 żółte/29 meczów). Nie znaleziono sygnału uzasadniającego korektę λ goli z tego tytułu — profil dyscyplinarny w normie.

## Podsumowanie
Barcelona jest wyraźnym faworytem w formie życia (7 zwycięstw z rzędu, 28 goli w 6 kolejkach), ale to mecz przeciwko zdrowej, dobrze grającej Sevilli z udokumentowaną historią psucia Barçy dokładnie na tym stadionie — dlatego zamiast czystego zwycięstwa Barcelony rekomendowany typ to **podwójna szansa X2 (83,5%, kurs 1,20)** lub, jako bezpieczna alternatywa bramkowa, **Over 1,5 gola (85,3%, kurs 1,17)**. Rożne to drugi mocny wątek — przewaga Barcelony (75,3%) i Over 8,5 (70,0%) to solidne, stabilne sygnały napędzane przewagą w posiadaniu.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
