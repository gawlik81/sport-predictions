# Borussia Mönchengladbach vs 1. FSV Mainz 05
**Rozgrywki:** Bundesliga, kolejka 4 | **Termin:** 19.09.2026, 15:30 (czasu polskiego) | **Ranga meczu:** przedostatnia drużyna ligi, świeżo po zwolnieniu trenera, kontra stabilna drużyna środka tabeli

## Kontekst i forma
- **Forma Borussii Mönchengladbach**: katastrofalny start — 2. miejsce od końca tabeli, **0 punktów z 3 meczów, 3 strzelone gole, 12 straconych**. Wyniki: porażka 0-3 z RB Lipsk (otwarcie sezonu), przegrana 3-4 u siebie z beniaminkiem Elversberg po prowadzeniu 3-1, porażka 0-5 na wyjeździe z Freiburgiem (czerwona kartka Tima Kleindiensta w 52. minucie). **Klub jako pierwszy w Bundeslidze zwolnił trenera w tym sezonie** — Eugen Polanski odszedł po fatalnym początku. Jan-Moritz Lichte (były trener Mainz) przygotuje drużynę na ten mecz w roli tymczasowej, a nowy stały trener ma zostać ogłoszony w przerwie reprezentacyjnej. Kleindienst (najlepszy strzelec drużyny) pauzuje za czerwoną kartkę. Dodatkowe absencje: Zento Uno, Yukhym Konoplya, Enzo Leopold, Jens Castrop, Nicolas-Gerrit Kühn.
- **Forma Mainz 05**: 8. miejsce, 4 punkty z 3 meczów (1R-1W-1P) — nieporażony start przerwany porażką 1-3 u siebie z Eintrachtem Frankfurt w kolejce 3 (Phillip Tietz strzelił honorowego gola). Solidna, stabilna forma bez rewelacji. Absencje: Dominik Kohr, Eric Martel, Robin Zentner (bramkarz), Paul Nebel, Silvan Widmer, Silas Katompa Mvumpa — dość długa lista, ale bez oznak kryzysu wynikowego.
- **Bezpośrednie spotkania (H2H)**: w 36 dotychczasowych meczach Gladbach wygrał 14, Mainz 10, 12 remisów — historycznie względnie wyrównane. Ważniejszy sygnał: **Mainz jest niepokonany w ostatnich 6 wyjazdach do Borussia-Park (3W-3R)** — silny, świeży trend na korzyść gościa w tym konkretnym miejscu.
- **Kadra**: Gladbach traci najlepszego strzelca (Kleindienst) za czerwoną kartkę plus 5 kolejnych zawodników kontuzjowanych — bardzo okrojony, zdezorganizowany skład. Mainz ma dłuższą listę absencji, ale bez kluczowego wpływu na wynikowość dotychczas.
- **Weryfikacja "kryzysu" underdoga (Krok 2b) — KLUCZOWA FLAGA RYZYKA DLA TEGO MECZU**: Gladbach spełnia w tym meczu **dokładnie** scenariusz ostrzegawczy z metodologii skilla — świeża zmiana trenera (tymczasowy szkoleniowiec przygotowuje drużynę na ten konkretny mecz) połączona z serią bez wygranej i fatalną defensywą. To niemal lustrzane odbicie przykładu z weryfikacji historycznej (Alavés, komplet zwycięstw u siebie, 82% pewności — przegrał z Valencią 2 dni po zwolnieniu ich trenera). Zgodnie z Krokiem 2b **stosuję realną korektę w dół pewności typu na Mainz** (nie tylko opisową wzmiankę), opisaną niżej przy 1X2.

## Model bazowy (oczekiwane gole)
Sezon jest młody (3 kolejki) — bazuję głównie na formie i danych jakościowych, z odniesieniem do stonowanej średniej ligowej (~1.6 gola/drużynę/mecz).
- λ(Gladbach) = 0.70 — niska wartość uzasadniona fatalną formą ofensywną (3 gole w 3 meczach) dodatkowo obniżoną przez nieobecność najlepszego strzelca (Kleindienst, czerwona kartka) oraz przyzwoitą defensywą Mainz
- λ(Mainz) = 2.00 — podniesiona względem własnej średniej (ok. 1.3 gola/mecz) z powodu katastrofalnej defensywy Gladbach (12 straconych w 3 meczach) i pozytywnego trendu H2H na wyjeździe w Borussia-Park

## Model rożnych (priorytet analizy)
Dane sezonowe o rożnych dla obu drużyn są zbyt skąpe dla solidnych własnych współczynników na tym etapie sezonu — opieram się na średniej ligowej i profilu stylu gry (Gladbach otwarta, chaotyczna defensywa generuje dużo gry end-to-end i rożnych obu stron; Mainz solidna, zorganizowana drużyna).
- λ_rożne(Gladbach) = 5.0 — mimo kryzysu, drużyna doganiająca wynik zwykle generuje więcej rożnych (częste ataki pozycyjne przy przegrywaniu), plus przewaga własnego boiska
- λ_rożne(Mainz) = 4.3 — typowa wartość dla zorganizowanej drużyny na wyjeździe
- Flaga jakości danych: brak solidnych własnych współczynników sezonowych dla obu drużyn — to szacunek jakościowy z szerszym niż zwykle przedziałem niepewności

## Prawdopodobieństwa

### Wynik meczu (1X2)
Model bazowy (Poisson, przed korektą Krok 2b) dał: Gladbach 12.1% / Remis 20.0% / Mainz 67.5% (kurs uczciwy 8.29 / 5.00 / 1.48).

**Korekta kalibracyjna (Krok 2b)**: ten mecz to najbliższy odpowiednik scenariusza "rannego zwierzęcia z nową miotłą" z weryfikacji historycznej skilla (Alavés-Valencia) spośród wszystkich trzech analizowanych dziś meczów Bundesligi. Stosuję korektę -7.5 pp od surowej pewności faworyta, rozdzieloną głównie na "odwrotny wynik" (zgodnie z ustaleniem weryfikacji, że ok. 2/3 pudeł w tym przedziale to underdog wygrywający bez remisu w tle, a tymczasowy trener często krótkoterminowo podnosi mobilizację drużyny):

| Wynik | Prawdopodobieństwo (po korekcie) | Kurs uczciwy |
|---|---|---|
| Gladbach wygrywa | 18.0% | 5.56 |
| Remis | 22.0% | 4.55 |
| Mainz wygrywa | 60.0% | 1.67 |

*Uzasadnienie: Mainz pozostaje faworytem dzięki formie, jakości i pozytywnemu trendowi H2H, ale to najniższa pewność typu na faworyta spośród trzech analizowanych dziś meczów Bundesligi — świadomie obniżona względem surowego wyniku modelu z powodu świeżej zmiany trenera u Gladbach.*

**Kalibracja (Krok 2b)**: oba scenariusze zagrożenia są tu jednoznacznie podwyższone względem "typowego" meczu w tym przedziale. **Odwrotny wynik** (Gladbach wygrywa, 18.0%) to główne ryzyko — tymczasowy trener + desperacka motywacja przed własną publicznością to dokładnie wzorzec, który w weryfikacji historycznej generował niespodzianki. **Remis** (22.0%) jest równie realny — Mainz stracił niepokonaną passę w poprzedniej kolejce i może grać ostrożniej na wyjeździe mimo przewagi klasowej.

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Gladbach więcej rożnych | 52.5% | 1.91 |
| Remis rożny | 12.9% | 7.73 |
| Mainz więcej rożnych | 34.6% | 2.89 |
| Over 8.5 | 58.3% | 1.71 |
| Over 9.5 | 45.2% | 2.21 |
| Over 10.5 | 33.0% | 3.03 |

- Gladbach: λ = 5.0 (realny zakres ~2-9)
- Mainz: λ = 4.3 (realny zakres ~1-8)
- Łącznie: λ = 9.3, realny zakres ~5-13

*Uzasadnienie: mimo że Mainz jest faworytem wynikowym, Gladbach powinien generować więcej rożnych dzięki przewadze boiska i typowemu wzorcowi drużyny doganiającej wynik — to niezależny rynek od 1X2, więc korekta z Kroku 2b nie ma tu bezpośredniego zastosowania (nie dotyczy zachowań ofensywnych w ogóle, tylko wyniku końcowego).*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-1 | 13.4% | 7.44 |
| 0-2 | 13.4% | 7.44 |
| 1-1 | 9.4% | 10.63 |
| 1-2 | 9.4% | 10.63 |
| 0-3 | 9.0% | 11.16 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 75.1% | 1.33 |
| Over 2.5 | 50.6% | 1.97 |
| Over 3.5 | 28.6% | 3.50 |
| BTTS - Tak | 43.3% | 2.31 |
| BTTS - Nie | 56.7% | 1.76 |

*Uzasadnienie: Gladbach bez najlepszego strzelca (Kleindienst) ma ograniczony potencjał ofensywny, co obniża szansę na BTTS mimo ogólnie otwartej defensywy gospodarzy.*

### Strzały i strzały celne
- Dane szczegółowe dla obu drużyn zbyt skąpe na tym etapie sezonu — nie podaję konkretnych liczb, by nie zmyślać. Orientacyjnie: Mainz jako drużyna dominująca powinna mieć przewagę objętości, ale Gladbach broniąc wyniku po stracie bramek może generować dużo strzałów z dystansu.

### Faule i kartki (drużynowo i indywidualnie)
**Drużynowo:**
- Gladbach: sygnał podwyższonego ryzyka dyscyplinarnego — czerwona kartka Kleindiensta w poprzednim meczu (52. min, Freiburg) wskazuje na drużynę grającą nerwowo/pod presją w kryzysowej sytuacji, co może się powtórzyć przy kolejnej porażce
- Mainz: brak sygnałów o szczególnych problemach dyscyplinarnych
- Dane liczbowe (faule/mecz, kartki/mecz) zbyt skąpe dla obu drużyn w obecnym sezonie — nie podaję zmyślonych wartości

**Indywidualnie:**
- Tim Kleindienst (Gladbach) — pauzuje za czerwoną kartkę z poprzedniej kolejki; jego brak już uwzględniony w korekcie λ(Gladbach) powyżej (utrata najlepszego strzelca)
- Brak dalszych danych o profilu indywidualnym (faule/90 min) dla obecnego sezonu

## Podsumowanie
To jedyny spośród trzech analizowanych dziś meczów Bundesligi, który trafia wprost w scenariusz ostrzegawczy z metodologii skilla — underdog (Gladbach) w prawdziwym kryzysie trenerskim, nie tylko klasowym. Mimo dużej przepaści formy i tabeli (0 pkt vs 4 pkt), świadomie obniżyłem pewność typu na faworyta (Mainz) z surowych 67.5% do 60.0%, zgodnie z Krokiem 2b i bezpośrednim precedensem z weryfikacji historycznej skilla (Alavés-Valencia). To najniższa pewność z trzech analizowanych dziś meczów — traktuj ten typ jako najbardziej ryzykowny z całej trójki, mimo najbardziej efektownej różnicy w tabeli.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
