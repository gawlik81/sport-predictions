# VfB Stuttgart vs Borussia Dortmund
**Rozgrywki:** Bundesliga, kolejka 4 | **Termin:** 19.09.2026, 18:30 (czasu polskiego) | **Ranga meczu:** drużyna w dolnej połowie tabeli, osłabiona kontuzjami, kontra lider formy z kompletem punktów

## Kontekst i forma
- **Forma VfB Stuttgart**: 14. miejsce w tabeli, 3 punkty z 3 meczów (1W-0R-2P). Porażki z Bayernem Monachium (kolejka 1) i z Hoffenheim 1-2 (kolejka 3, 12.09). Bardzo obszerna lista kontuzji: brak Tiago Tomasa, Luki Jaqueza, Jeremy'ego Arevalo, **Dana-Axela Zagadou** (kluczowy środkowy obrońca, uraz ścięgna udowego), Justina Diehla, Dennisa Seimena i Lorenza Assignona — aż 7 zawodników poza kadrą meczową. Brak Zagadou wymusza defensywę w formacji trzech obrońców (Jeltsch, Chabot, Mittelstadt) złożoną z zawodników bez ugranej pozycji w tej roli. Klub przekazuje też sygnały o mocnej dyspozycji na własnym stadionie w ostatnich występach (do zweryfikowania na żywo w dniu meczu — dane z niektórych źródeł mieszały się z poprzednim sezonem).
- **Forma Borussii Dortmund**: 2. miejsce w tabeli, komplet punktów — 9 pkt z 3 meczów (3W-0R-0P), jedyna drużyna ligi z pełnym bilansem po 3 kolejkach. Średnio 2.5 gola/mecz w Bundeslidze, xGA 1.53/mecz (solidna, choć nie elitarna defensywa). W ostatnich 5 meczach we wszystkich rozgrywkach (łącznie z pucharami) 16 strzelonych goli — bardzo gorąca forma ofensywna, choć ta liczba miesza rozgrywki, więc traktuję ją jako sygnał jakościowy, nie wprost do λ ligowego. Młody napastnik Konstantinos Karetsas wraca do kadry po problemach krążeniowych — bez istotnego wpływu na wyjściowy skład.
- **Bezpośrednie spotkania (H2H)**: zdecydowana przewaga Dortmundu — w ostatnich 38 meczach Dortmund wygrał 20, Stuttgart 10, 8 remisów. W ostatnich 30 starciach Dortmund 16W-7R-7P, śr. 3.87 gola/mecz łącznie. Ostatni mecz: Stuttgart 0-3 Dortmund.
- **Kadra**: patrz wyżej — asymetria kontuzji wyraźnie na niekorzyść Stuttgartu (7 nieobecności, w tym kluczowy stoper), Dortmund praktycznie bez istotnych absencji.
- **Weryfikacja "kryzysu" underdoga (Krok 2b)**: Stuttgart nie ma świeżej zmiany trenera ani serii bez gola — to klasyczny scenariusz "słabszej klasowo/kadrowo drużyny", a nie "rannego zwierzęcia" z desperacką motywacją po roszadzie szkoleniowej. Nie stosuję więc dodatkowej korekty w dół pewności faworyta z tego tytułu, ale ryzyko remisu/niespodzianki i tak wymaga wzmianki, bo mecz mieści się w przedziale 50-85% (patrz niżej).

## Model bazowy (oczekiwane gole)
Sezon jest wciąż bardzo młody (3 kolejki), więc pełne współczynniki siły ataku/obrony względem średniej ligowej są oparte na małej próbie — opieram się głównie na formie i jakościowej ocenie, zgodnie z zaleceniem skilla dla wczesnego sezonu. Średnia ligowa w tym sezonie jest podwyższona (3.85 gola/mecz łącznie po 27 meczach, ale to częściowo efekt kilku skrajnych wyników, np. serii rozgromień HSV) — użyłem bardziej stonowanego, długoterminowego baseline'u Bundesligi (~1.6 gola/drużynę/mecz w среднim otoczeniu) jako punktu odniesienia, skorygowanego jakościowo:
- λ(Stuttgart) = 1.15 — solidny bonus za własne boisko, ale wyraźnie obniżony przez osłabioną, prowizoryczną obronę (nie wpływa bezpośrednio na λ własne ataku, ale ogranicza tempo gry drużyny broniącej prowadzenia) oraz ogólnie słabszy start sezonu
- λ(Dortmund) = 2.15 — silny atak w doskonałej formie, kompletny skład, dodatkowo premiowany fatalnym stanem defensywy rywala (brak kluczowego stopera)

**Flaga niepewności**: to szacunek jakościowy oparty na małej próbie (3 mecze), nie w pełni "twardy" współczynnik sezonowy — traktuj przedział wynikowy jako orientacyjny.

## Model rożnych (priorytet analizy)
Dane sezonowe o rożnych dla obu drużyn są na tym etapie sezonu zbyt skąpe, by policzyć solidne współczynniki z pełnym rozbiciem dom/wyjazd — opieram się na średniej ligowej i kontekście jakościowym, w tym zaskakującym sygnale z H2H: w dwóch ostatnich bezpośrednich starciach **to Stuttgart wygrał liczbę rożnych** (4-2 i 5-2), mimo ogólnej przewagi klasowej Dortmundu w tych meczach. Może to odzwierciedlać styl Dortmundu (gra przez środek, mniej dośrodkowań) kontra Stuttgart częściej kończący akcje dośrodkowaniami/rożnymi przy grze pod własnym błokiem.
- λ_rożne(Stuttgart) = 5.3 — premia za przewagę własnego boiska i powtarzalny wzorzec z H2H
- λ_rożne(Dortmund) = 4.3 — mimo ogólnej dominacji w grze, słabszy generator rożnych w tym konkretnym zestawieniu
- Flaga jakości danych: to jeden z niewielu przypadków w tym sezonie, gdzie sezonowa próba jest zbyt mała nawet dla przybliżenia — szacunek oparty głównie na 2-meczowym H2H i średniej ligowej, przedział niepewności szerszy niż zwykle

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Stuttgart wygrywa | 19.5% | 5.12 |
| Remis | 20.3% | 4.94 |
| Dortmund wygrywa | 59.5% | 1.68 |

*Uzasadnienie: Dortmund jako wyraźny faworyt dzięki formie, kompletowi kadry i przewadze klasowej, ale to najniższy raw-probability wśród trzech analizowanych dziś meczów Bundesligi — mimo najbardziej "efektownej" na oko różnicy w tabeli (komplet punktów vs 3 pkt). Model uwzględnia, że pojedynczy mecz wyjazdowy zachowuje realną wariancję, a Stuttgart wciąż ma jakość ofensywną w składzie.*

**Kalibracja (Krok 2b)**: typ mieści się w przedziale 50-85%, więc oba scenariusze zagrożenia wymagają wzmianki. **Remis** (20.3%) jest realny — Stuttgart, mimo słabej defensywy, generował gole w domu i może utrzymać kontakt wynikowy. **Odwrotny wynik** (Stuttgart wygrywa, 19.5%) jest równie realny — Dortmund gra na wyjeździe, a Stuttgart historycznie potrafił zaskoczyć w tym starciu przewagą rożnych/set-pieców. Nie ma tu jednostronnego sygnału "kryzysu" underdoga (Stuttgart to zwykła, słabsza kadrowo drużyna, nie klub w panice trenerskiej), więc nie zastosowałem dodatkowej korekty w dół dla Dortmundu, ale też nie ma podstaw do podbicia pewności powyżej tego, co pokazuje model.

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Stuttgart więcej rożnych | 56.3% | 1.78 |
| Remis rożny | 12.4% | 8.05 |
| Dortmund więcej rożnych | 31.3% | 3.20 |
| Over 8.5 | 62.0% | 1.61 |
| Over 9.5 | 49.1% | 2.04 |
| Over 10.5 | 36.7% | 2.72 |

- Stuttgart: λ = 5.3 (realny zakres ~2-9)
- Dortmund: λ = 4.3 (realny zakres ~1-8)
- Łącznie: λ = 9.6, realny zakres ~6-13

*Uzasadnienie: wzorzec z H2H (Stuttgart wygrywał rożne w obu ostatnich starciach) plus przewaga własnego boiska przeważają nad ogólną dominacją Dortmundu w jakości gry — ale przy tak małej próbie to najsłabiej "utwardzony" model rożnych z trzech dzisiejszych analiz.*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-2 | 9.8% | 10.20 |
| 1-1 | 9.1% | 10.97 |
| 0-2 | 8.5% | 11.73 |
| 0-1 | 7.9% | 12.61 |
| 1-3 | 7.0% | 14.23 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 84.1% | 1.19 |
| Over 2.5 | 64.1% | 1.56 |
| Over 3.5 | 42.0% | 2.38 |
| BTTS - Tak | 59.9% | 1.67 |
| BTTS - Nie | 40.1% | 2.49 |

*Uzasadnienie: obie drużyny mają realny potencjał ofensywny (Stuttgart u siebie, Dortmund w formie), a defensywa Stuttgartu jest osłabiona — sprzyja to golom po obu stronach.*

### Strzały i strzały celne
- Dane sezonowe zbyt skąpe dla solidnego szacunku (wczesny sezon) — orientacyjnie, biorąc pod uwagę styl obu drużyn: łącznie ok. 22-28 strzałów w meczu, z czego Dortmund powinien mieć wyraźną przewagę objętości (silniejszy atak, więcej posiadania), a Stuttgart będzie polegać na kontrach i stałych fragmentach gry.

### Faule i kartki (drużynowo i indywidualnie)
**Drużynowo:**
- Dane szczegółowe (faule/mecz, kartki/mecz) zbyt skąpe dla obu drużyn na tym etapie sezonu — zaznaczam to wprost zamiast zgadywać liczby.
- Nie znaleziono sygnału o wyjątkowo surowym/łagodnym sędzim tego meczu.

**Indywidualnie:**
- Brak wystarczających danych o profilu indywidualnym (faule popełnione/sprowokowane na 90 min) dla kluczowych zawodników obu drużyn w obecnym sezonie — nie zmyślam liczb.
- Jedyny istotny sygnał dyscyplinarny z researchu: żaden zawodnik nie jest wskazany jako grający "na zawieszeniu" w tym meczu.

### Inne istotne statystyki
- Kluczowy czynnik pozastatystyczny: prowizoryczna defensywa Stuttgartu (3 zawodników grających poza swoimi naturalnymi rolami/parami) to główne źródło niepewności w tym meczu — trudne do uchwycenia w czystych liczbach.

## Podsumowanie
Dortmund jest wyraźnym faworytem dzięki formie, kompletowi kadry i słabości defensywnej Stuttgartu (7 nieobecności, w tym kluczowy stoper), ale to najbardziej "stonowany" z trzech analizowanych dziś meczów Bundesligi pod względem surowej liczby z modelu (59.5%) — mimo najbardziej efektownej różnicy w tabeli. Ciekawostką jest model rożnych: wzorzec H2H sugeruje przewagę Stuttgartu w tej konkretnej kategorii, mimo ogólnej przewagi Dortmundu w jakości gry — potencjalna nisza wartości, choć oparta na małej próbie.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
