# Manchester City vs Sunderland
**Rozgrywki:** Premier League, kolejka 5 | **Termin:** niedziela, 20.09.2026, 14:00 BST (Etihad Stadium) | **Ranga meczu:** lider vs beniaminek walczący o utrzymanie

## Kontekst i forma
- **Forma Manchester City** (sezon 2026/27, 4 mecze): 4W-0D-0L, 12 pkt, 2. miejsce w tabeli (jeden mecz mniej niż część rywali). Bilans bramkowy 8:2 (2.00 strzelonych / 0.50 straconych na mecz). Wygrał derby Manchesteru 1:0 na Old Trafford i rozbił Norwich 5:0 w Carabao Cup w tygodniu. Erling Haaland w znakomitej dyspozycji: 5 goli w 4 ligowych występach.
- **Forma Sunderlandu** (4 mecze): 1W-1D-2L, 4 pkt, 14. miejsce. Bilans bramkowy 3:5. Na wyjeździe zaledwie 1 pkt z 2 meczów (0W-1D-1L). Beniaminek z Championship, wciąż szuka stabilizacji w PL.
- **H2H**: City całkowicie dominuje serię — 21 zwycięstw, 5 remisów, 4 porażki w 30 meczach; u siebie 13W-2D-0L. Ostatni bezpośredni mecz (styczeń 2026, Etihad) zakończył się jednak niespodziewanym 0:0 — dowód, że Sunderland potrafi się defensywnie zamknąć nawet na wyjeździe u lidera.
- **Kadra City**: brak Phila Fodena (czerwona kartka w derbach, zawieszenie obejmuje też ten mecz) oraz Jeremy'ego Doku (uraz łydki, poza grą od Community Shield). Nowy nabytek Allan (z Palmeiras) zdobywa zaufanie po golu w Carabao Cup.
- **Kadra Sunderland**: brak Omara Alderete, Habiba Diarry i Romaine'a Mundle'a (uraz kolana, długa przerwa). Malick Fofana może dostać pierwszy pełny występ w PL.
- **Inne czynniki**: City gra w komplecie motywacyjnym na szczycie tabeli, Sunderland realnie broni się przed przegraniem wysoko i będzie grał bardzo defensywnie.

## Model bazowy (oczekiwane gole)
- Baza z danych sezonowych: City ~2.0 gola/mecz (siła ataku wyraźnie powyżej średniej ligowej), Sunderland ~1.25 gola straconego/mecz, na wyjeździe historycznie gorzej.
- **Korekta jakościowa w dół** względem czysto "surowego" wyliczenia (które dawałoby λ_home ~2.5): brak Fodena i Doku ogranicza szerokość gry i możliwości City na skrzydłach, a ostatni bezpośredni mecz (0:0) pokazuje, że Sunderland potrafi się zabetonować. Stąd λ_home obniżone z ~2.5 do 2.25.
- λ(City) = **2.25**, λ(Sunderland) = **0.75**

## Model rożnych
- City: bardzo wysoka aktywność ofensywna, ~6.36 rożnego/mecz w ostatnich sezonach (dane nie w pełni rozbite na dom/wyjazd dla obecnego sezonu — przybliżenie).
- Sunderland: drużyna broniąca się nisko blokiem, co zwykle generuje więcej rożnych dla przeciwnika; oddane rożne szacowane na bazie średniej ligowej i stylu gry (dane sezonowe niepełne — zaznaczam to wprost).
- λ_rożne(City) = **6.3**, λ_rożne(Sunderland) = **3.6** (łącznie ~9.9)

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| City wygrywa | 70.6% | 1.42 |
| Remis | 17.7% | 5.66 |
| Sunderland wygrywa | 10.9% | 9.17 |

*Uzasadnienie: przepaść klasowa i formy jest ogromna (lider vs 14. miejsce), ale dwa scenariusze zagrożenia są realne i porównywalne: (1) remis — Sunderland już raz zamknął City na 0:0 na tym stadionie, a dziś gra jeszcze bardziej defensywnie w obronie przed spadkiem; (2) "odwrotny wynik" jest mało prawdopodobny (Sunderland nie jest w kryzysie, ale ich ofensywa jest zbyt słaba, by liczyć na niespodziankę) — ryzyko remisu wyraźnie przeważa nad ryzykiem porażki City.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| City więcej rożnych | 75.8% | 1.32 |
| Remis rożny | 9.0% | 11.10 |
| Sunderland więcej rożnych | 15.1% | 6.61 |
| Over 8.5 | 65.6% | 1.52 |
| Over 9.5 | 53.0% | 1.89 |
| Over 10.5 | 40.5% | 2.47 |

- City: λ_rożne = 6.3 (realny zakres ~4-9)
- Sunderland: λ_rożne = 3.6 (realny zakres ~2-6)

### Najbardziej prawdopodobne wyniki
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 2-0 | 12.6% | 7.94 |
| 1-0 | 11.2% | 8.93 |
| 3-0 | 9.5% | 10.58 |
| 2-1 | 9.5% | 10.58 |
| 1-1 | 8.4% | 11.90 |
| 3-1 | 7.1% | 14.11 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 80.1% | 1.25 |
| Over 2.5 | 57.7% | 1.73 |
| Over 3.5 | 35.3% | 2.83 |
| BTTS - Tak | 46.8% | 2.14 |
| BTTS - Nie | 53.2% | 1.88 |

*Uzasadnienie: City powinno strzelić przynajmniej 1-2 gole niemal niezależnie od przebiegu, ale ofensywa Sunderlandu jest na tyle słaba (0.75 gola/mecz), że BTTS-Nie ma lekką przewagę.*

### Strzały i strzały celne
- City: strzały ~16-20, celne ~7-9 (dominacja posiadania i tworzonych okazji)
- Sunderland: strzały ~6-9, celne ~2-3 (głównie z kontr)

### Faule i kartki
**Drużynowo:** obie drużyny w normie ligowej — łącznie ~20-23 fauli, 3-5 żółtych kartek w meczu. Brak sygnałów o wyjątkowo surowym sędzim w dostępnych źródłach.
**Indywidualnie:** brak z researchu istotnych zawodników "na progu zawieszenia" po obu stronach — profil dyscyplinarny nie wymaga korekty λ.

## Podsumowanie
Przepaść klasowa (lider vs 14. drużyna walcząca o utrzymanie) i historia bezpośrednich starć (13W-2D-0L City u siebie) jasno wskazują na City jako zdecydowanego faworyta — model daje ~70-71% po korekcie w dół za brak Fodena i Doku. Największym realnym zagrożeniem dla typu nie jest niespodziewana wygrana Sunderlandu, lecz zamknięty defensywnie remis (jak w styczniu 2026). Rożne to druga mocna nić analizy — City powinno zdecydowanie dominować w tym rynku (~76% szansy na przewagę rożną, Over 9.5 blisko 53%).

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
