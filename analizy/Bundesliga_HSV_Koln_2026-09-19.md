# Hamburger SV vs FC Köln
**Rozgrywki:** Bundesliga, kolejka 4 | **Termin:** 19.09.2026, 15:30 (czasu polskiego) | **Ranga meczu:** ostatnia drużyna ligi (0 pkt, 0 goli strzelonych) kontra stabilna drużyna środka tabeli

## Kontekst i forma
- **Forma Hamburger SV**: katastrofalny start sezonu — 18. (ostatnie) miejsce w tabeli, **0 punktów, 0 strzelonych goli, 12 straconych w 3 meczach**. Wyniki: porażka 0-2 z Borussią Dortmund (wyjazd), 0-5 z Mainz (u siebie!), 0-5 z RB Lipsk (wyjazd). To nie jest "zwykła" słabsza drużyna — HSV nie strzelił gola w żadnym z 3 meczów sezonu, co jest jednym z konkretnych sygnałów "kryzysu" wymienionych w metodologii tego skilla (Krok 2b). Trener Merlin Polzin pozostaje na stanowisku — **nie znaleziono sygnału o zmianie trenera** (kluczowe rozróżnienie, patrz niżej). Timo Hübers (kluczowy środkowy obrońca) przeszedł kolejną operację kolana i czeka go długa przerwa — obrona jeszcze bardziej osłabiona. Możliwe powroty: Terem Moffi, Fabio Vieira, Warmed Omari (siła ofensywna), Otto Stange i Kofi Amoako wracają do pełnych treningów.
- **Forma FC Köln**: 9. miejsce w tabeli, 4 punkty z 3 meczów (1W-1R-1P). Porażka 1-4 na wyjeździe ze Stuttgartem, remis u siebie z Werder Bremen w kolejce 3 — rozsądna, stabilna forma środka tabeli, bez rewelacji, ale bez kryzysu. Ragnar Ache i Said El Mala mają wrócić do wyjściowego składu.
- **Bezpośrednie spotkania (H2H)**: na Volksparkstadion HSV ma historyczną przewagę (31 zwycięstw w 57 meczach vs 12 Kölna), ale to statystyka wieloletnia, sprzed obecnego kryzysu — mało istotna w obliczu aktualnej formy obu drużyn.
- **Kadra**: HSV traci długoterminowo Hübersa (obrona); Köln bez istotnych absencji sygnalizowanych w researchu.
- **Weryfikacja "kryzysu" underdoga (Krok 2b)**: HSV nie miał świeżej zmiany trenera (jak w przypadku Alavés/Valencia z weryfikacji skilla), więc formalnie nie jest to scenariusz "nowej miotły"/desperackiej motywacji po roszadzie szkoleniowej — analogicznie do Union Berlin z piątkowej analizy (Bayern-Union), gdzie taki "wynikowy" kryzys bez zmiany trenera nadal trafiał niezawodnie jako typ na faworyta. **Jednak** HSV trafia dosłownie w drugi z wymienionych w Kroku 2b sygnałów ostrzegawczych — "zero goli od wielu meczów" — nawet bardziej dobitnie niż Union (które strzeliło gole w 2 z 3 meczów). To rozróżnia ten przypadek od czysto "zdrowego faworyta vs słabszy klub" i uzasadnia umiarkowaną (nie drastyczną) korektę w dół pewności typu na Köln, opisaną niżej.

## Model bazowy (oczekiwane gole)
Sezon jest młody (3 kolejki), więc bazuję głównie na formie i danych jakościowych, zgodnie z zaleceniem skilla dla wczesnego sezonu, z lekkim odniesieniem do stonowanej średniej ligowej (~1.6 gola/drużynę/mecz).
- λ(HSV) = 0.55 — ekstremalnie niska wartość uzasadniona kompletnym brakiem goli w 3 meczach sezonu (w tym przeciw zróżnicowanym rywalom: Dortmund, Mainz, Lipsk), lekko podniesiona względem "zera" dzięki przewadze własnego boiska i możliwym powrotom ofensywnym (Moffi, Vieira)
- λ(Köln) = 2.1 — podniesiona względem własnej średniej sezonowej (ok. 1.3 gola/mecz) z powodu fatalnej, wielokrotnie testowanej defensywy HSV (12 straconych w 3 meczach, kolejna długoterminowa absencja w obronie)

## Model rożnych (priorytet analizy)
Wykorzystuję dostępne dane sezonowe (częściowo z ubiegłego sezonu jako przybliżenie, bo obecny sezon ma zbyt małą próbę): HSV ma jeden z najniższych wskaźników zdobywanych rożnych w Bundeslidze (śr. 3.75/mecz "for", aż 5.84/mecz "against" — drużyna broniąca się nisko i oddająca dużo pola). Köln zdobywa średnio 4.62 rożnego/mecz.
- λ_rożne(HSV) = 3.9 — zgodne z niskim wskaźnikiem własnym, lekko podniesione za przewagę boiska
- λ_rożne(Köln) = 5.1 — połączenie własnej średniej ataku rożnego Kölna i wysokiej podatności HSV na oddawanie rożnych (5.84/mecz), spodziewana dominacja terytorialna Kölna przy słabej defensywie i niskim bloku gospodarzy
- Flaga jakości danych: część danych HSV/Kölna pochodzi z sezonu 2025/26 jako przybliżenie (obecny sezon zbyt młody dla solidnych własnych współczynników) — kierunek (przewaga rożna Kölna) jest jednak spójny z ogólnym obrazem formy

## Prawdopodobieństwa

### Wynik meczu (1X2)
Model bazowy (Poisson, przed korektą Krok 2b) dał: HSV 8.5% / Remis 17.9% / Köln 73.1% (kurs uczciwy 11.84 / 5.58 / 1.37).

**Korekta kalibracyjna (Krok 2b)**: ponieważ HSV trafia w sygnał "zero goli od wielu meczów" (nawet dobitniej niż w precedensie Union Berlin), stosuję umiarkowaną korektę w dół pewności faworyta (Köln), mniejszą niż przy typowym scenariuszu "nowej miotły" (tam nie było zmiany trenera), ale nie zerową — głównie z ostrożności, bo tak ekstremalna, testowana wobec 3 różnych rywali seria daje też margines na "przełamanie" akurat w tym meczu (regresja do średniej, efekt "musi się kiedyś zdarzyć").

| Wynik | Prawdopodobieństwo (po korekcie) | Kurs uczciwy |
|---|---|---|
| HSV wygrywa | 11.0% | 9.09 |
| Remis | 19.5% | 5.13 |
| Köln wygrywa | 69.5% | 1.44 |

*Uzasadnienie: Köln pozostaje wyraźnym faworytem dzięki fundamentalnej, wielokrotnie potwierdzonej słabości defensywnej i ofensywnej HSV, ale finalna liczba jest świadomie niżej niż surowy wynik modelu (73.1%), by uwzględnić ryzyko regresji do średniej po serii ekstremów.*

**Kalibracja (Krok 2b)**: mimo korekty w dół, typ nadal mieści się blisko górnej granicy przedziału 50-85%, więc oba scenariusze zagrożenia warto wymienić: **remis** (19.5%) jest bardziej prawdopodobny niż wygrana HSV, bo drużyna gospodarzy może w końcu ustabilizować defensywę na tyle, by nie przegrać, nawet bez zdobycia gola. **Odwrotny wynik** (HSV wygrywa, 11.0%) jest mało prawdopodobny, ale nie zerowy — to wciąż mecz u siebie, z powracającymi zawodnikami ofensywnymi.

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| HSV więcej rożnych | 28.4% | 3.52 |
| Remis rożny | 12.5% | 7.99 |
| Köln więcej rożnych | 59.1% | 1.69 |
| Over 8.5 | 54.4% | 1.84 |
| Over 9.5 | 41.3% | 2.42 |
| Over 10.5 | 29.4% | 3.40 |

- HSV: λ = 3.9 (realny zakres ~1-7)
- Köln: λ = 5.1 (realny zakres ~2-9)
- Łącznie: λ = 9.0, realny zakres ~5-13

*Uzasadnienie: Köln powinien dominować terytorialnie dzięki fatalnej defensywie i niskiemu blokowi HSV — spójne z sezonowym profilem obu drużyn (HSV wśród najsłabszych generatorów rożnych w lidze).*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 0-2 | 15.6% | 6.42 |
| 0-1 | 14.8% | 6.74 |
| 0-3 | 10.9% | 9.17 |
| 1-2 | 8.6% | 11.67 |
| 1-1 | 8.2% | 12.25 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 74.2% | 1.35 |
| Over 2.5 | 49.4% | 2.02 |
| Over 3.5 | 27.5% | 3.64 |
| BTTS - Tak | 36.9% | 2.71 |
| BTTS - Nie | 63.1% | 1.58 |

*Uzasadnienie: BTTS-Nie jest tu naturalnie wysokie — HSV nie strzelił gola w żadnym z 3 dotychczasowych meczów, więc "czyste konto" Kölna jest bardziej prawdopodobne niż wymiana goli po obu stronach.*

### Strzały i strzały celne
- HSV: bardzo niska objętość ofensywna — śr. 8.67 strzału/mecz, 2.67 celnego/mecz w obecnym sezonie
- Köln: dane szczegółowe skąpe, orientacyjnie średnia ligowa lub nieco powyżej
- Komentarz: HSV wyróżnia się negatywnie zarówno liczbą, jak i skutecznością strzałów — spójne z zerowym bilansem bramkowym

### Faule i kartki (drużynowo i indywidualnie)
**Drużynowo:**
- HSV: w poprzednim sezonie najwyższa liczba czerwonych kartek w całej Bundeslidze (6) — sygnał drużyny grającej pod presją/nerwowo, co może się utrzymywać w obecnym kryzysie; podnosi to nieznacznie ryzyko gry w osłabieniu, co dodatkowo pogłębiałoby przewagę Kölna w drugiej połowie meczu
- Köln: śr. 8.3 faula/mecz, 49 żółtych i 3 czerwone kartki w poprzednim sezonie — w normie
- Dane te pochodzą częściowo z sezonu 2025/26 (zbyt mała próba w obecnym) — kierunek (HSV bardziej skłonny do czerwonych kartek) traktuję jako user informacyjny, nie twardy sezonowy współczynnik

**Indywidualnie:**
- Brak wystarczających danych o profilu indywidualnym (faule/90 min per zawodnik) dla obecnego sezonu — nie zmyślam liczb.
- Żaden zawodnik nie jest zgłoszony jako grający "na zawieszeniu" w tym meczu.
- **Powiązanie z modelem bazowym**: wysoka skłonność HSV do czerwonych kartek (z zeszłego sezonu) to dodatkowy, choć drugorzędny czynnik wspierający przewagę Kölna — nie zmienił bezpośrednio λ, ale wzmacnia jakościowo kierunek modelu.

## Podsumowanie
To najbardziej wyrazisty przypadek "kryzysu" wśród trzech analizowanych dziś meczów Bundesligi — HSV nie strzelił gola w żadnym z 3 meczów sezonu i ma najgorszy bilans bramkowy w lidze (0-12). Mimo to, zgodnie z metodologią Kroku 2b, zastosowałem umiarkowaną (nie drastyczną) korektę w dół surowej pewności modelu (73.1% → 69.5%), bo brak zmiany trenera odróżnia ten przypadek od najbardziej ryzykownego scenariusza "nowej miotły" z weryfikacji skilla. Model rożnych spójnie wskazuje na dominację terytorialną Kölna. To najbardziej "solidny" pod względem struktury danych typ z trzech analizowanych dziś meczów, choć wciąż nie na poziomie ekstremalnej pewności (jak np. piątkowy Bayern-Union).

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
