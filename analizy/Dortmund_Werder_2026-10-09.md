# Borussia Dortmund - Werder Brema (Bundesliga, pt 09.10.2026, 20:30)

Źródła: ESPN (tabela, forma, H2H), Pinnacle (kursy, linie goli i gole drużynowe), DraftKings (kursy ESPN). Model: Poisson z λ dopasowaną do rynku Pinnacle (Dortmund 2.50, Werder 0.90, suma 3.4).
**Brak** potwierdzonych składów, kontuzji i sędziego (wyszukiwarki nie zwróciły aktualnych zapowiedzi). Zmieniają one wyceny, dlatego nie ma typów na kartki, rożne, faule ani rynki zawodnika.

## Dane
- **Dortmund**: 1. w tabeli, 12 pkt z 4 meczów, bilans goli 9:2. Ostatnie 5 meczów: 5 wygranych (5-0 Puchar, 3-2 Hoffenheim, 3-2 Villarreal LM, 3-0 Paderborn, 1-0 Stuttgart). W lidze 3 czyste konta na 4 mecze, gole stracone tylko z Hoffenheim. Nie grał od 19.09, więc bez zmęczenia po pucharach.
- **Werder**: 8. miejsce, 7 pkt z 4 meczów, bilans 8:8. Wyniki: 1-4 Freiburg, 3-1 Leipzig, 1-1 Köln, 3-2 Augsburg. Strzelił w każdym z 4 meczów ligowych i w każdym stracił (BTTS 4/4).
- **H2H** (5 ostatnich): Dortmund bez porażki (2-0 w Bremie 16.05.2026, 3-0 w Dortmundzie 13.01.2026, 2-2, 0-0, 2-1). Werder strzelił w nich 3 gole w 5 meczach.
- **Rynek (Pinnacle, bez marży)**: Dortmund 70.7%, remis 17.6%, Werder 11.7%. Główna linia goli 3.25 (Over/Under po -105).
- **Data**: ESPN i Pinnacle podają 9.10 o 18:30 UTC (20:30 CEST). Niektóre serwisy sugerują 10.10 - sprawdź na stronie Bundesligi.

## Wycena (model dopasowany do rynku)
| Rynek | p | Fair | Kurs Pinnacle | Pewność |
|---|---|---|---|---|
| Dortmund lub remis | 88% | 1.13 | - | wysoka (zbyt krótki) |
| Dortmund bez remisu (DNB) | 86% | 1.16 | 1.26 | wysoka |
| Over 1.5 gola | 85% | 1.17 | - | wysoka |
| **Dortmund wygra** | 71-72% | 1.38 | 1.37 | średnia/wysoka |
| Dortmund strzeli 2+ gole | 71% | 1.40 | 1.30 | średnia |
| **Over 2.5** | 66% | 1.51 | 1.455 | średnia |
| Werder strzeli | 59% | 1.69 | 1.62 | średnia |
| Under 3.5 | 56% | 1.79 | 1.75 | średnia |
| BTTS tak | 54% | 1.84 | n/d | średnia |
| Dortmund wygra 2+ (AH -1.5) | 50% | 1.99 | 1.94 | średnia |
| Over 3.5 | 44% | 2.26 | 2.17 | niska |
| Dortmund strzeli 3+ gole | 46% | 2.19 | 2.04 | niska |
| Remis | 16-17% | 6.1 | 5.50 | - |
| Werder wygra | 11-12% | 8.7 | 8.25 | - |

Najczęstsze wyniki: 2-0 (10%), 2-1 (9%), 3-0 (9%), 1-0 (8%), 3-1 (8%), 1-1 (7.5%).
Najpewniejsze typy to 1X, DNB i Over 1.5, ale mają fair <= 1.17 i samodzielnie nie opłacają się. Dortmund wygra i Over 2.5 to pierwsze typy z sensownym kursem.

## Ryzyka
- Remis lub wygrana Werderu (łącznie ok. 28%): Dortmund stracił 4 gole w ostatnich 5 meczach (2 z Hoffenheim, 2 z Villarreal), a Werder strzela regularnie.
- Dortmund ma czyste konta w 3 z 4 meczów ligowych. To obniża BTTS (Werder 59% na gola) i ryzykuje typy z BTTS.
- Brak składów: absencja napastnika lub rotacja po przerwie reprezentacyjnej obniża λ Dortmundu.

## Kupon (kurs > 3, typy niesprzeczne, jeden mecz)
Ponieważ nie ma wyceny kursów łączonych w tym samym meczu, p liczone jest z siatki wyników (uwzględnia korelację). Kurs u bukmachera sprawdź w kreatorze zakładów na ten mecz.

**Kupon A - Dortmund wygra różnicą 2+ (handicap -1.5) + Over 3.5 gola**
- Wyniki: 3-1, 4-0, 4-1, 4-2, 5-0, 5-1 i wyższe.
- p ok. 31% (zakres 25-38% przy zmianie λ), fair 3.2. Kurs musi być >= 3.0 (przy 2.8 jest to zakład ze stratą).
- Brak sprzeczności: obie nogi wymagają wysokiej wygranej Dortmundu.

**Kupon B (pewniejszy co do progu 3.0) - Dortmund wygra + BTTS tak + Over 3.5**
- Wyniki: 3-1, 3-2, 4-1, 4-2 i wyższe.
- p ok. 25% (zakres 20-31%), fair 3.9, szacowany kurs 3.4-3.7.

Oba kupony mają EV bliskie zera lub ujemne: p pochodzi z rynku, więc nie ma przewagi nad bukmacherem. To zakłady na wysoką wygraną gospodarzy, nie "pewniaki".

Oszacowania probabilistyczne, nie gwarancje.

## Aktualizacja po ogłoszeniu składów (09.10, ok. 20:10)

Źródła: ESPN (oficjalne składy i statystyki zawodników), 90min.de. Sędziego nadal nie znam.

**Dortmund (3-4-2-1):** Kobel; Gadou, Anton, Schlotterbeck; Svensson, Nmecha, Bellingham, Sabitzer/Beier (źródła różnią się co do ustawienia Beiera); Nwaneri; Guirassy. Nie grają: Ryerson i Chukwuemeka (kontuzje). Schlotterbeck wraca po urazie. Silva (2 gole w 3 meczach) i Karetsas na ławce.
**Werder (4-3-3):** Hein; Arthur, Pieper, Friedl, Deman; Regeer, Chuki, Reis; Grüll, Füllkrug, Dinkci. Ten sam skład czwarty mecz z rzędu, Hein wraca do bramki.

**Statystyki zawodników (4 mecze ligowe):** Guirassy 2 gole, 2 asysty, 13 strzałów (3.25/mecz). Beier 10 strzałów. Nmecha 2 gole. Füllkrug 3 gole, 11 strzałów, trafiał w 3 ostatnich kolejkach. Grüll 2 gole, 3 asysty, 10 strzałów. Chuki 2 asysty.

**Reakcja rynku:** DraftKings przed składami -300 / remis +425 / Werder +650, po składach -290 / +400 / +600. Over 3.5 z +110 na +120. Rynek lekko osłabił Dortmund i obniżył oczekiwaną liczbę goli.

**Nowa wycena** (λ Dortmund 2.35, Werder 0.95):
| Typ | p | Fair |
|---|---|---|
| Dortmund wygra | 69% | 1.46 |
| Remis | 18% | 5.6 |
| Werder wygra | 14% | 7.4 |
| Over 2.5 | 64% | 1.56 |
| Over 3.5 | 42% | 2.38 |
| BTTS tak | 56% | 1.80 |
| Guirassy strzeli gola | ok. 42% | 2.4 |
| Füllkrug strzeli gola | ok. 30% | 3.4 |
| Guirassy Over 2.5 strzału | ok. 65% | 1.54 |
| Füllkrug Over 1.5 strzału | ok. 68% | 1.48 |

Rynki zawodnika to przybliżenie (udział w golach drużyny i strzały na mecz), bez kursów rynkowych i bez sędziego, więc pewność niska/średnia.

**Kupony (kurs > 3, bez sprzeczności):**
1. **Dortmund wygra 2+ (AH -1.5) + Over 3.5:** p ok. 28% (zakres 22-34%), fair 3.6, kurs musi być >= 3.0. Typy z Pinnacle.
2. **Dortmund wygra + Over 2.5 + Guirassy strzeli gola:** p ok. 29%, fair 3.5, kurs szacunkowo 3.0-3.3. Wymaga kursu na Guirassy u bukmachera.
3. Dortmund wygra + BTTS + Over 3.5: p ok. 24%, fair 4.2.

Bez zmian: żaden kupon nie ma dodatniego EV (p pochodzi z rynku).
