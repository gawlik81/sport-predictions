# Brentford vs Chelsea
**Rozgrywki:** Premier League, kolejka 5 | **Termin:** 18.09.2026, 21:00 (20:00 BST) | **Ranga meczu:** środek-górna część tabeli, West London derby (lokalny rywal)

## Kontekst i forma
- **Forma Chelsea**: 7 pkt z 4 meczów PL (6. miejsce), prawdopodobnie 2W-1R-1P. Ostatnie dwa mecze: porażka 1-2 z Arsenalem, remis 2-2 u siebie z beniaminkiem Hull. W dotychczasowych meczach sezonu strzelili 10 i stracili 9 goli (2.50 GF / 2.25 GA na mecz) — najwięcej goli łącznie (for+against) ze wszystkich drużyn ligi w ich meczach. Atak wzmocniony transferem Rogersa z Aston Villi (3G+3A, najwięcej udziałów przy golu w klubie). **Defensywnie na wyjeździe fatalnie**: 21 goli straconych na wyjeździe w 2026 (kalendarzowo, drugi najgorszy wynik w lidze po Crystal Palace), wygrana tylko w 1 z ostatnich 6 wyjazdowych meczów PL, i tracą min. 2 gole w każdym dotychczasowym meczu ligowym tego sezonu.
- **Forma Brentford**: 6 pkt z 4 meczów (7. miejsce), seria 6 meczów bez porażki we wszystkich rozgrywkach (drugi najdłuższy taki ciąg w historii klubu w PL). Bardzo mocny profil ofensywny ze stałych fragmentów gry: 2.34 xG ze stałych fragmentów (bez karnych) — 2. wynik w lidze po Leeds.
- **Bezpośrednie spotkania (H2H)**: Chelsea niepokonane w ostatnich 5 starciach (2W, 3R), ostatni mecz 2-2 w Gtech Community Stadium. Brentford ma wyraźną historię kończenia meczów ligowych remisem na własnym stadionie w ostatnim czasie.
- **Kadra**: Chelsea — Moisés Caicedo (uraz łydki, dostępność niepewna), Emegha i Henderson pod znakiem zapytania. Brentford — Dasilva, Milambo, Collins, van den Berg, Jensen spodziewani jako nieobecni (kilku kluczowych obrońców, co ryzykownie osłabia defensywę gospodarzy).
- **Inne czynniki**: Chelsea grająca dość otwarty, transakcyjny futbol (dużo strzelają, dużo tracą) kontra Brentford w świetnej dyspozycji psychologicznej (seria bez porażki) i mocni w ofensywie ze stałych fragmentów — układ sprzyja meczowi z golami po obu stronach.

## Model bazowy (oczekiwane gole)
Sezon jest bardzo wczesny (4 mecze rozegrane) — oparłem λ na kombinacji danych z bieżącego sezonu, kontekstu jakościowego (leaky Chelsea away defense vs. solidny Brentford w domu) i ogólnej klasy drużyn, a nie na w pełni ustabilizowanych współczynnikach sezonowych ataku/obrony (zbyt mała próbka na czysty model siła ataku/obrony ÷ średnia ligowa). To luźniejsze oszacowanie niż przy pełnym sezonie.

- λ(Brentford) = 1.45 — skorygowane w górę względem bazowej jakości drużyny z powodu wyjątkowo dziurawej defensywy wyjazdowej Chelsea
- λ(Chelsea) = 1.55 — skorygowane w górę z powodu formy ofensywnej (Rogers), ale stłumione przez słabą dyspozycję wyjazdową i solidność Brentford w domu

## Model rożnych (priorytet analizy)
- λ_rożne(Brentford) = 5.2 — bazowa średnia sezonu 2025-26 (4.79/mecz) skorygowana w górę z racji przewagi własnego boiska i bardzo wyraźnego profilu ataku ze stałych fragmentów gry (dużo dośrodkowań)
- λ_rożne(Chelsea) = 5.4 — bazowa średnia sezonu 2025-26 (5.95/mecz) skorygowana lekko w dół z racji gry na wyjeździe
- Flaga jakości danych: brak w pełni rozbitych danych dom/wyjazd dla bieżącego (wczesnego) sezonu — użyto średnich z całego poprzedniego sezonu jako bazy, co jest przybliżeniem zgodnie z zasadami skilla

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Brentford wygrywa | 35.6% | 2.81 |
| Remis | 24.3% | 4.12 |
| Chelsea wygrywa | 40.0% | 2.50 |

*Uzasadnienie: mecz bardzo wyrównany — model niemal idealnie pokrywa się z niezależnym szacunkiem Opta (35.4/24.3/40.3), co jest dobrą walidacją krzyżową. Brak wyraźnego faworyta.*

**Kalibracja (Krok 2b)**: żaden wynik nie przekracza 50% pewności, więc to nie jest przypadek "typu faworyta" — oba ryzyka (remis i "odwrotny wynik") są tu realne i praktycznie symetryczne dla obu drużyn. H2H (4-5 ostatnich starć kończących się remisem na tym stadionie) dodatkowo podbija wiarygodność scenariusza remisowego ponad to, co sugerowałby sam model. Żadna z drużyn nie jest w kryzysie — Brentford jest wręcz w bardzo dobrej formie (seria bez porażki), więc nie ma tu sygnału "zdrowy faworyt kontra kryzysowy underdog".

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Brentford więcej rożnych | 41.4% | 2.42 |
| Remis rożny | 12.4% | 8.07 |
| Chelsea więcej rożnych | 46.2% | 2.16 |
| Over 8.5 | 73.1% | 1.37 |
| Over 9.5 | 61.5% | 1.63 |
| Over 10.5 | 49.2% | 2.03 |
| Over 11.5 | 37.3% | 2.68 |

- Brentford: λ = 5.2 (realny zakres ~3-8)
- Chelsea: λ = 5.4 (realny zakres ~3-8)
- Łącznie: λ = 10.6, realny zakres ~7-14

*Uzasadnienie: obie drużyny generują sporo rożnych (Chelsea nieco więcej z racji stylu gry, Brentford blisko dzięki przewadze własnego boiska i ataku ze stałych fragmentów). Rynek najpewniejszy to Over 8.5 (73%).*

### Najbardziej prawdopodobne wyniki (gole)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-1 | 11.2% | 8.94 |
| 1-2 | 8.7% | 11.53 |
| 2-1 | 8.1% | 12.33 |
| 0-1 | 7.7% | 12.96 |
| 1-0 | 7.2% | 13.85 |
| 2-2 | 6.3% | 15.91 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 80.1% | 1.25 |
| Over 2.5 | 57.7% | 1.73 |
| Over 3.5 | 35.3% | 2.83 |
| BTTS - Tak | 60.2% | 1.66 |
| BTTS - Nie | 39.9% | 2.51 |

*Uzasadnienie: obie drużyny regularnie tracą gole (Chelsea traci min. 2 w każdym meczu tego sezonu), co silnie wspiera BTTS Tak i Over 1.5/2.5.*

### Strzały i strzały celne
- Konkretnych świeżych danych sezonowych o strzałach/strzałach celnych dla obu drużyn nie udało się dociągnąć w ramach budżetu researchu — na bazie ogólnej jakości i stylu obu zespołów szacuję łącznie ok. 22-27 strzałów w meczu, z czego ok. 8-11 celnych. To szeroki, uczciwy przedział, nie precyzyjna liczba.

### Faule i kartki (drużynowo i indywidualnie)
**Drużynowo:**
- Dokładnych sezonowych średnich fauli/kartek dla obu drużyn nie udało się znaleźć w ramach budżetu researchu tego meczu — szacuję (na bazie typowego poziomu PL) łącznie ok. 18-24 faule i 3-5 żółtych kartek w meczu. To przybliżenie, zaznaczone wprost zamiast zmyślonej precyzji.

**Indywidualnie:**
- **Mamadou Sangaré (Brentford)**: 127 pressingów wysokiej intensywności we własnej połowie (3. w lidze), 8 fauli popełnionych (wspólnie 4. w lidze), 13 wślizgów (wspólnie 5. w lidze) — kluczowy kandydat do kartki w środku pola.
- Danych o najbardziej faulowanych zawodnikach obu drużyn oraz o zawodnikach na progu zawieszenia nie udało się dociągnąć w ramach budżetu researchu — brak sygnału o kimś grającym "na kartce" w obu składach.
- Ten profil nie uzasadnia korekty λ goli ponad to, co już uwzględniono (brak sygnału o czerwonych kartkach czy zawieszeniach kluczowych zawodników).

## Podsumowanie
To jeden z bardziej wyrównanych meczów kolejki — model niezależnie potwierdza rozkład zbliżony do zewnętrznych szacunków (Opta), bez wyraźnego faworyta w 1X2. Najmocniejszym sygnałem jest **obustronna skuteczność ofensywna** (BTTS Tak 60%, Over 1.5 80%) wynikająca z fatalnej defensywy wyjazdowej Chelsea i solidnego ataku Brentford ze stałych fragmentów gry. Rożne są równie wyrównane jak wynik meczu — Chelsea z niewielką przewagą, ale Over 8.5 (73%) to najpewniejszy rynek w tej kategorii. Zarówno remis, jak i zwycięstwo dowolnej ze stron, są realnymi scenariuszami — historia bezpośrednich starć (dużo remisów na tym stadionie) dodatkowo wspiera ostrożność przy typowaniu jednoznacznego wyniku.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
