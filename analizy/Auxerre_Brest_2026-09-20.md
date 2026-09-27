# AJ Auxerre vs Stade Brestois
**Rozgrywki:** Ligue 1, kolejka 5 | **Termin:** niedziela, 20.09.2026, 15:00 (Stade de l'Abbé-Deschamps, Auxerre) | **Ranga meczu:** środek/dół tabeli — Brest chce potwierdzić miejsce w górnej połowie, Auxerre szuka punktów po trudnym starcie sezonu

## Kontekst i forma
- **Forma Auxerre** (ostatnie 4 Ligue 1): 1W-0D-3L, 15. miejsce z 3 pkt. Najgorsza defensywa ligi — **2,75 gola straconego/mecz (11 w 4 meczach)**. Wyniki: przegrane z Lens 2-5, z Angers 1-3, z Lyonem 1-3, ale **wygrana 1-0 z Nice** w ostatniej kolejce — pierwsze zwycięstwo nowego trenera Willa Stilla w Ligue 1 (jego pierwsze w L1 od sezonu 2024-25 w Lens). Latem klub stracił kilku kluczowych zawodników (bramkarz Donovan Léon, kapitan Elisha Owusu, najlepszy strzelec Lassine Sinayoko), a kadra jest dodatkowo przetrzebiona kontuzjami: Okoh, Senaya, Siwe, Dioussé, Coulibaly, Fofana — wszyscy nieobecni od dłuższego czasu.
- **Forma Brest**: 1W-2D-1L, 7. miejsce z 5 pkt — solidnie, ale bez fajerwerków. Ostatni mecz to **porażka 0-1 z PSG u siebie** (gol Ferrana Torresa w 5. minucie) — to koryguje wcześniejsze (błędne) założenie, że Brest jest "w gorącej formie po pokonaniu PSG": w rzeczywistości to Brest przegrał to starcie. Bilans sezonu: wygrana 2-1 na wyjeździe z Le Havre, prawdopodobnie 2 remisy (Le Mans, Toulouse) i porażka z PSG.
- **H2H — kluczowy czynnik ryzyka dla Brestu**: Auxerre **wygrało oba ostatnie spotkania domowe z Brestem** i **nie przegrało z Brestem u siebie od 2018 roku**; ostatni bezpośredni mecz zakończył się wygraną Auxerre 3-0. To silny, powtarzalny wzorzec przeciwny modelowi opartemu na bieżących statystykach sezonowych.
- **Kadra**: Brest bez Brendana Chardonneta, Noaha Edjoumy i Mamady'ego Diambou; źródła sygnalizują też niejasność wokół dyspozycyjności Ludovica Ajorque (jedne źródła: zawieszony, inne: w wyjściowym składzie) — **nie udało się jednoznacznie zweryfikować**, zaznaczone jako niepewność.
- **Inne czynniki**: Auxerre gra u siebie z impetem po pierwszym zwycięstwie sezonu i pod nowym trenerem, który właśnie odblokował wynik — możliwy efekt zwiększonej motywacji/pewności siebie. Brest przyjeżdża po rozczarowującej porażce z PSG.

## Model bazowy (oczekiwane gole)
- Surowe współczynniki z 4 kolejek (Auxerre atak/obrona, Brest atak/obrona) zostały **zregresowane (shrinkage) w kierunku średniej ligowej** (waga ok. 40% dane / 60% średnia) z uwagi na małą próbę.
- Średnia ligowa: ~1,55 gospodarz / 1,21 gość (na bazie ~2,76 gola/mecz łącznie w tym sezonie Ligue 1).
- Surowy model (przed korektą H2H) dawał wyraźniejszą przewagę Brestu (λ ok. 1,51 / 1,94) głównie dzięki fatalnej defensywie Auxerre. **Zastosowano korektę w dół dla Brestu** (z 1,94 do 1,75) i lekko w górę dla Auxerre (z 1,51 do 1,55) w oparciu o silny, powtarzalny wzorzec H2H (2 zwycięstwa domowe Auxerre z rzędu, seria bez porażki od 2018) oraz świeży impuls motywacyjny (pierwsze zwycięstwo sezonu, nowy trener).
- λ(Auxerre) = 1,55, λ(Brest) = 1,75

## Model rożnych
- Brak publicznie dostępnych, aktualnych danych o rożnych dla obu klubów w tym sezonie (Auxerre — strona ze statystykami niedostępna/404; Brest — dane zastrzeżone premium) — **oszacowano wyłącznie na bazie średniej ligowej i ogólnego stylu gry, z wyraźnie szerszym marginesem niepewności niż zwykle**.
- Auxerre u siebie zwykle broni się głęboko przy tak słabej defensywie sezonowej, co może generować rożne dla przeciwnika z zablokowanych sytuacji; Brest gra częściej przez środek/kontry niż szerokością boiska.
- λ_rożne(Auxerre) = 5,0, λ_rożne(Brest) = 4,3 — **przybliżenie o niskiej pewności, jawnie oznaczone jako mniej wiarygodne z powodu braku danych źródłowych.**

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Auxerre wygrywa | 34,2% | 2,92 |
| Remis | 22,9% | 4,37 |
| Brest wygrywa | 42,5% | 2,35 |

*Uzasadnienie: to **nie jest typ o wysokiej pewności** — surowa przewaga statystyczna Brestu (lepsza forma sezonowa, dużo słabsza defensywa Auxerre) jest realnie osłabiona przez silny wzorzec H2H (Auxerre niepokonane u siebie z Brestem od 2018, 2 zwycięstwa domowe z rzędu) oraz świeży impuls motywacyjny gospodarzy. **Kalibracja (Krok 2b):** przy tak wyrównanym rozkładzie (34/23/43) zarówno remis, jak i zwycięstwo Auxerre są realnymi scenariuszami — żaden wynik 1X2 nie kwalifikuje się tu jako "pewniak".*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Auxerre więcej rożnych | 52,5% | 1,91 |
| Remis rożny | 12,9% | 7,73 |
| Brest więcej rożnych | 34,6% | 2,89 |
| Over 8,5 | 58,3% | 1,71 |
| Over 9,5 | 45,2% | 2,21 |
| Over 10,5 | 33,0% | 3,03 |

- Auxerre: λ = 5,0 (realny zakres ~3-8, dane niepewne)
- Brest: λ = 4,3 (realny zakres ~3-7, dane niepewne)
- Łącznie: λ ≈ 9,3, realny zakres ~7-13

*Uzasadnienie: bez solidnych danych źródłowych to najsłabiej ugruntowana sekcja tego raportu — traktować jako orientacyjną.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-1 | 10,0% | 10,00 |
| 1-2 | 8,8% | 11,42 |
| 2-1 | 7,8% | 12,90 |
| 2-2 | 6,8% | 14,74 |
| 0-1 | 6,5% | 15,49 |
| 1-0 | 5,7% | 17,49 |
| 0-2 | 5,7% | 17,71 |
| 1-3 | 5,1% | 19,58 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1,5 | 84,1% | 1,19 |
| Over 2,5 | 64,1% | 1,56 |
| Under 2,5 | 35,9% | 2,78 |
| BTTS - Tak | 64,8% | 1,54 |
| BTTS - Nie | 35,2% | 2,84 |

*Uzasadnienie: dwie drużyny ze słabymi defensywami sezonowymi (Auxerre najgorsza w lidze, Brest przeciętna) i regularnie strzelające dają solidne, spójne sygnały Over 1,5, Over 2,5 i BTTS Tak — to najmocniejsza część tej analizy.*

### Strzały i strzały celne
- Brak wiarygodnych danych sezonowych dla Auxerre (źródło niedostępne) — pominięto zamiast zgadywać.
- Brest: ~21-23 strzały/mecz (średnio ~22), konwersja ~7% — dużo objętości gry, ale niska skuteczność.

### Faule i kartki
**Drużynowo:**
- Brest: ~14-16 fauli popełnionych/mecz (średnio ~15), ~12,5-14 sprowokowanych
- Auxerre: brak wiarygodnych danych sezonowych — pominięto zamiast zgadywać
- Łącznie: brak podstaw do solidnego przedziału przy braku danych jednej ze stron

**Indywidualnie:** brak wiarygodnych, publicznie dostępnych danych per zawodnik dla obu klubów na tym etapie sezonu — nie zgadujemy nazwisk ani liczb. Status Ajorque (zawieszenie vs dostępność) pozostaje niepewny — jeśli faktycznie zawieszony, to ubytek dla ataku Brestu, ale nie zmienia to kierunku modelu na tyle, by uzasadnić dodatkową korektę λ bez jednoznacznego potwierdzenia.

**Wniosek dla modelu:** brak wystarczających danych do dodatkowej korekty dyscyplinarnej ponad już zastosowaną korektę H2H/motywacyjną.

## Podsumowanie
To **nie jest mecz z wyraźnym faworytem** w kategorii 1X2 — surowa przewaga statystyczna Brestu (lepsza forma, dużo słabsza defensywa Auxerre) jest w dużej mierze zneutralizowana przez silny wzorzec H2H (Auxerre niepokonane u siebie z Brestem od 2018) i świeży impuls motywacyjny gospodarzy po pierwszym zwycięstwie sezonu. Rozkład 1X2 (34%/23%/43%) jest zbyt płaski, by rekomendować typ wynikowy z wysoką pewnością. **Najmocniejszy, najbardziej spójny sygnał w tym meczu to rynek bramkowy: Over 1,5 (84,1%, kurs uczciwy 1,19) oraz BTTS Tak (64,8%, kurs uczciwy 1,54)** — obie drużyny mają słabe defensywy i regularnie strzelają, co czyni ten typ znacznie solidniejszym niż jakikolwiek typ na wynik meczu. Sekcja rożnych oparta jest na słabych danych źródłowych i powinna być traktowana z ograniczonym zaufaniem.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
