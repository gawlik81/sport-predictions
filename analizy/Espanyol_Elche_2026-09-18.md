# RCD Espanyol vs Elche CF
**Rozgrywki:** LaLiga EA Sports, kolejka 7 | **Termin:** piątek, 18.09.2026, 21:00 (RCDE Stadium) | **Ranga meczu:** Espanyol goni strefę europejską, Elche szuka pierwszego zwycięstwa w sezonie — ostatni mecz przed pierwszą przerwą reprezentacyjną

## Kontekst i forma
- **Forma Espanyol** (ostatnie 5 LaLiga): 2W-1D-2L, 8 goli strzelonych/5 straconych, 8. miejsce w tabeli, 3 pkt od strefy europejskiej. Przed ostatnią porażką z Rayo Vallecano (1-2) notował dobrą serię: wygrana na wyjeździe z Osasuną, remis z Sevillą. W domu bardzo mocny (2,2 pkt/mecz średnio), zaczął sezon od 3-0 z Levante. **Silne uzależnienie od jednego strzelca: Roberto Fernández ma 6 z 9 goli drużyny w tym sezonie** — istotny czynnik ryzyka koncentracji ataku.
- **Forma Elche**: **prawdziwy kryzys** — 0 zwycięstw w 5 meczach pod wodzą Martína Anselmiego (2D-3L), 6 goli strzelonych, **13 straconych** (2,6 GA/mecz), najgorszy start klubu w historii ligi, w mediach określany jako trener "na krawędzi" (bez świeżej dymisji, ale pod realną presją). Ostatni mecz: porażka 2-3 z Realem Madryt, przegrana po prowadzeniu w końcówce.
- **H2H**: w ostatnich 12 spotkaniach Espanyol 4W, Elche 3W, 5D — historycznie wyrównane, ale nieadekwatne do obecnej dysproporcji formy.
- **Kadra Espanyol**: brak El Hilaliego, Javiego Puado, Kike Garcíi; Gorosabel pod znakiem zapytania. Reszta składu dostępna.
- **Kadra Elche**: brak Yago Santiago, poza tym drużyna kompletna kadrowo — problem leży w organizacji gry i defensywie, nie w brakach personalnych.

## Model bazowy (oczekiwane gole)
- Espanyol (dom): szacunkowo ~1,9 GF / ~0,8 GA na podstawie silnej formy domowej i solidnej defensywy sezonowej (5 straconych w 5 meczach ogółem, mniej w domu).
- Elche (wyjazd): szacunkowo ~1,1 GF / ~2,8 GA na wyjeździe — ekstremalnie dziurawa defensywa (13 straconych w 5 meczach).
- Surowy model multiplikatywny (siła ataku/obrony względem średniej ligowej ~1,5 dom / ~1,2 wyjazd) dawał bardzo wysokie λ dla Espanyol (>3,5) — **skorygowano w dół**, bo przy tak małej próbce (5-6 meczów) skrajne wskaźniki obronne Elche (kilka meczów z dużą liczbą straconych goli, np. mecz z Realem Madryt) zawyżają iloczyn ponad realistyczny poziom. Zastosowano tłumienie w stronę bardziej wiarygodnego zakresu.
- λ(Espanyol) = 2,30, λ(Elche) = 0,85

## Model rożnych (priorytet analizy)
- Dane zagregowane (mecz-total, nie czysto per drużyna) wskazują ~8,84 rożnych łącznie w domowych meczach Espanyol i ~7,8 łącznie w wyjazdowych meczach Elche — rozbito je na komponenty dom/wyjazd przy typowym podziale ~55/45.
- Espanyol: solidne posiadanie w domu, dużo gry skrzydłami → rożne w normie ligowej.
- Elche: słabsza defensywa oznacza więcej gry pod własnym polem karnym (więcej rożnych dla Espanyol z zablokowanych/odbitych ataków), ale też ograniczone możliwości budowania własnych ataków pozycyjnych na wyjeździe (mniej własnych rożnych).
- λ_rożne(Espanyol) = 4,70, λ_rożne(Elche) = 3,70 — **przybliżenie z podwyższonym marginesem niepewności z uwagi na dane zagregowane, a nie czysto per-drużynowe.**

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo (surowa) | Kurs uczciwy |
|---|---|---|
| Espanyol wygrywa | 69,0% | 1,45 |
| Remis | 17,8% | 5,63 |
| Elche wygrywa | 12,3% | 8,15 |

*Uzasadnienie i kalibracja (Krok 2b): surowy model daje Espanyol wysoką pewność (69%), co mieści się w przedziale 50-85%, gdzie kalibracja historyczna każe explicite rozważyć ryzyko remisu i "odwrotnego wyniku" — Elche jest w wyraźnym kryzysie (0 zwycięstw, najgorszy start klubu w historii, trener pod presją), co **przypomina wzorzec z weryfikacji (Alavés 82% pewności → porażka z ostatnią w tabeli Valencią tuż po zmianie trenera)**. Elche nie miało świeżej zmiany trenera (Anselmi jest od czerwca), ale presja na wynik + zespół "walczący o przetrwanie" bywa źródłem niespodzianek podobnie jak "nowa miotła". Dodatkowo atak Espanyol jest mocno skoncentrowany na jednym zawodniku (Roberto Fernández, 6/9 goli) — jego wyłączenie z gry obniżyłoby realne szanse. **Zastosowano realną korektę w dół (~5-6 pp)** względem surowego wyniku modelu: skorygowane prawdopodobieństwo Espanyol ≈ 63-64%. Ze względu na to ryzyko, rekomendowanym "najbezpieczniejszym" typem jest podwójna szansa 1X (86,8% z modelu surowego), z czystym "1" jako typem o wyższym ryzyku, ale nadal uzasadnionym fundamentalnie.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Espanyol więcej rożnych | 56,7% | 1,76 |
| Remis rożny | 13,2% | 7,56 |
| Elche więcej rożnych | 30,1% | 3,33 |
| Over 8,5 | 46,3% | 2,16 |
| Over 9,5 | 33,4% | 2,99 |
| Over 10,5 | 22,6% | 4,43 |

- Espanyol: λ = 4,70 (realny zakres ~3-7)
- Elche: λ = 3,70 (realny zakres ~2-6)
- Łącznie: λ ≈ 8,4, realny zakres ~6-11

*Uzasadnienie: przewaga rożna Espanyol jest wyraźna, ale nie ekstremalna — Elche mimo słabej gry zbiorowej potrafi generować rożne z kontrataków i stałych fragmentów w desperackich sytuacjach. Under 9,5 (66,6%) jest solidniejszym sygnałem niż jakikolwiek pojedynczy próg "over".*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 2-0 | 11,3% | 8,82 |
| 1-0 | 9,9% | 10,15 |
| 2-1 | 9,6% | 10,38 |
| 3-0 | 8,7% | 11,51 |
| 1-1 | 8,4% | 11,94 |
| 3-1 | 7,4% | 13,54 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 82,2% | 1,22 |
| Over 2,5 | 61,0% | 1,64 |
| Over 3,5 | 38,6% | 2,59 |
| BTTS - Tak | 51,0% | 1,96 |
| BTTS - Nie | 49,0% | 2,04 |

*Uzasadnienie: Elche mimo kryzysu strzela regularnie (gole w większości meczów), ale przewaga jakościowa Espanyol w domu przekłada się na wyraźną skłonność do czystego konta gospodarzy w wielu scenariuszach — BTTS jest praktycznie remisowe (51/49), Over 2,5 solidniejszym sygnałem.*

### Strzały i strzały celne
- Brak wystarczająco precyzyjnych, jawnie dostępnych danych sezonowych per drużyna dla obu klubów w tym sezonie — pominięto zamiast zgadywać.

### Faule i kartki
**Drużynowo:** brak wiarygodnych, kompletnych danych sezonowych 2026-27 per drużyna w dostępnych źródłach — nie podajemy zmyślonych liczb.

**Indywidualnie:** brak wiarygodnych danych per zawodnik. Brak sygnałów o zawodnikach na progu zawieszenia po obu stronach.

**Wniosek dla modelu:** brak nowych sygnałów dyscyplinarnych wykraczających poza już uwzględnioną korektę jakościową (kryzys formy Elche, koncentracja ataku Espanyol na jednym zawodniku).

## Podsumowanie
Espanyol jest wyraźnym faworytem dzięki mocnej formie domowej i przepaści klasowej wobec pogrążonego w kryzysie Elche (0 zwycięstw, najgorszy start klubu w historii), ale zgodnie z kalibracją modelu (wzorzec Alavés-Valencia z weryfikacji) zastosowano realną korektę w dół pewności typu "1" i rekomendowanym najbezpieczniejszym typem jest podwójna szansa 1X (86,8%) zamiast czystego zwycięstwa gospodarzy. W rożnych przewaga Espanyol jest umiarkowana (56,7%), a Under 9,5 to solidniejszy sygnał niż strona "over". Warto pamiętać o dużej koncentracji ataku Espanyol na jednym zawodniku (Roberto Fernández) jako dodatkowym czynniku ryzyka.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
