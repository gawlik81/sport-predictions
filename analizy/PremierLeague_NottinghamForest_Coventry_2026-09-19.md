# Nottingham Forest vs Coventry City
**Rozgrywki:** Premier League, kolejka 5 | **Termin:** sobota, 19.09.2026, 17:30 BST (City Ground) | **Ranga meczu:** środek/dół tabeli vs beniaminek w głębokim kryzysie

## Kontekst i forma
- **Forma Nottingham Forest** (4 mecze): dopiero w ostatniej kolejce zanotował pierwsze zwycięstwo sezonu (2:1 z Aston Villą), wcześniej 2 remisy i porażka — 16. miejsce, 5 pkt po 4 meczach. Niepokonany w ostatnich 3 spotkaniach (1W-2D).
- **Forma Coventry City**: powrót do PL po 25 latach przebiega fatalnie — **0 pkt, 4 porażki, 0 goli strzelonych, 10 straconych** (w tym 0:5 z Brighton tydzień temu). To autentyczny kryzys, nie tylko słabszy poziom klasowy.
- **H2H**: Forest wygrał ostatnie 6 bezpośrednich starć z Coventry (różne rozgrywki) — silna przewaga historyczna, choć głównie sprzed awansu Coventry do PL.
- **Kadra Forest**: kontuzje w defensywie — Nikola Milenkovic (ścięgno) na pewno poza grą, Jair Cunha wątpliwy (trenował, przejdzie test), Nicolo Savona wraca po operacji kolana. Ola Aina improwizuje na środku obrony. Osłabiona, niepewna linia obrony.
- **Kadra Coventry**: Josh Eccles, Kane Cessler, Haji Wright, Aurel Amenda niedostępni. Dodatkowo Taiwo Awoniyi (latem odszedł z Forest do Coventry) pauzuje za czerwoną kartkę z Brighton — to akurat osłabia i tak już bezbramkowy atak gości.
- **Inne czynniki**: klasyczny obraz "zdrowego, ale niepewnego siebie gospodarza" kontra "kryzysowy underdog" — dokładnie scenariusz, przy którym metodologia tego skilla (Krok 2b) każe REALNIE obniżyć pewność typu na faworyta, a nie tylko wspomnieć o ryzyku opisowo.

## Model bazowy (oczekiwane gole)
- Baza: Forest jako gospodarz o umiarkowanej, ale nie dominującej formie; Coventry ze skrajnie słabą ofensywą (0 goli w 4 meczach) i dziurawą obroną (10 straconych).
- **Korekta jakościowa w dół** względem "surowego" wyliczenia (~1.75 dla Forest): Forest sam dopiero wraca do formy (2 pkt przed zwycięstwem nad Villą) i gra z osłabioną, przebudowaną obroną (Milenkovic, Savona, wątpliwy Cunha) — mimo przepaści klasowej to nie jest "zdrowy, pewny siebie" faworyt. Zgodnie z Krokiem 2b (kryzysowy underdog ≠ automatyczna gwarancja) obniżam λ_home i podnoszę nieco λ_away względem czystej ekstrapolacji "0 goli Coventry = pewna wygrana".
- λ(Forest) = **1.55**, λ(Coventry) = **0.78**

## Model rożnych
- Trend bukmacherski: "Total rożnych Under 9.5" trafiał w 12 z ostatnich 14 meczów Coventry, a Forest brał poniżej 6.5 rożnego we własnych meczach w 13 z ostatnich 14 — obie drużyny grają w niskotempowym, mało rożnym stylu.
- λ_rożne(Forest) = **4.8**, λ_rożne(Coventry) = **3.0** (łącznie ~7.8, zgodnie z trendem "Under")

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Forest wygrywa | 55.5% | 1.80 |
| Remis | 25.6% | 3.91 |
| Coventry wygrywa | 18.8% | 5.32 |

*Uzasadnienie: mimo przepaści w tabeli (5 pkt vs 0 pkt, 0 straconych goli u Coventry to fikcja — 10 straconych, 0 strzelonych), oba scenariusze zagrożenia są tu realne i wymagają jawnego wymienienia: (1) remis — Forest sam nie jest w porywającej formie i dopiero się odbudowuje; (2) "odwrotny wynik" — kryzysowe drużyny czasem grają "z niczym do stracenia" desperacko lepiej niż sugerują liczby (analogicznie do przypadku Alavés-Valencia z weryfikacji tego skilla). Dlatego finalna pewność (55.5%) jest wyraźnie niższa niż sugerowałaby sama tabela — to typ ŚREDNIEJ, nie wysokiej pewności.*

### Rożne — przewaga i over/under
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Forest więcej rożnych | 67.8% | 1.47 |
| Remis rożny | 11.9% | 8.37 |
| Coventry więcej rożnych | 20.2% | 4.95 |
| Under 6.5 | 33.8% | 2.96 |
| Under 7.5 | 48.1% | 2.08 |
| **Under 9.5** | **74.1%** | **1.35** |

- Forest: λ_rożne = 4.8 (realny zakres ~2-8)
- Coventry: λ_rożne = 3.0 (realny zakres ~1-6)

*Uzasadnienie: obie drużyny generują mało rożnych (niskie tempo, Coventry rzadko dochodzi do ataku pozycyjnego) — rynek Under 9.5 rożnych wygląda solidniej niż typ 1X2 na Forest.*

### Najbardziej prawdopodobne wyniki
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-0 | 15.1% | 6.63 |
| 1-1 | 11.8% | 8.50 |
| 2-0 | 11.7% | 8.56 |
| 0-0 | 9.7% | 10.28 |
| 2-1 | 9.1% | 10.97 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 67.6% | 1.48 |
| Over 2.5 | 41.2% | 2.43 |
| BTTS - Tak | 42.6% | 2.35 |
| BTTS - Nie | 57.4% | 1.74 |

*Uzasadnienie: Coventry nie strzelił jeszcze gola w tym sezonie PL — BTTS-Nie ma przewagę, choć Forest gra z osłabioną obroną, więc nie jest to pewniak.*

### Strzały i strzały celne
- Forest: strzały ~10-13, celne ~4-5
- Coventry: strzały ~7-10, celne ~2-3 (dużo strzałów niecelnych/blokowanych, stąd zero goli mimo względnie przyzwoitej liczby prób)

### Faule i kartki
**Drużynowo:** Coventry jako drużyna broniąca się w kryzysie zwykle generuje więcej fauli taktycznych; łącznie w meczu szacuję ~22-25 fauli, 4-6 żółtych kartek.
**Indywidualnie:** Awoniyi (Coventry) pauzuje za czerwoną z poprzedniej kolejki — usuwa jednego z niewielu realnych zagrożeń ofensywnych gości, co dodatkowo obniża λ(Coventry). Brak innych istotnych sygnałów o zawodnikach na progu zawieszenia.

## Podsumowanie
To najtrudniejszy do skalibrowania mecz z trójki: przepaść w tabeli jest ogromna, ale Coventry jest kryzysowym, a nie tylko słabszym rywalem, a Forest sam gra z przebudowaną, osłabioną obroną i dopiero wraca do formy — zgodnie z metodologią (Krok 2b) to uzasadnia realne obniżenie pewności typu na faworyta do ~55-56%, czyli ŚREDNI poziom pewności, mimo skrajnie słabych liczb Coventry. Najciekawszym rynkiem może być **Under 9.5 rożnych (74%, kurs uczciwy 1.35)** — obie drużyny grają w niskorożnym stylu, a ten trend jest bardziej stabilny niż wynik meczu.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
