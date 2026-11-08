# Manchester United - Aston Villa (Premier League, 08.11.2026, 17:30 czasu polskiego)

Analiza pod kupon Bet Builder na Superbet (event_id 14438723). Warunki użytkownika: łączny kurs 1.5-2.5, stawka 5 zł.

## Podsumowanie

**Brak mocnego typu.** Mecz jest wyrównany, a rynek wycenia go wyżej na gole niż mój model. Jedyny typ z EV > 0 w moim wariancie bazowym to **Poniżej 3.5 gola** (kurs 1.63, p ok. 66%, EV ok. +7%). Ta przewaga bierze się wyłącznie z tego, że liczę o ok. 0,3 gola mniej niż rynek. Dla wariantu rynkowego (λ 1,75 / 1,50) EV wynosi -4%. Szczegóły w sekcji "Kupon".

## Dane (źródła)

- **Tabela** (`pl_standings`, Premier League 2026/27, 9-10 kolejek): Man Utd 18. miejsce, 7 pkt z 9 meczów, bramki 10:15; u siebie 4 mecze, 4 pkt, 6:7. Aston Villa 12. miejsce, 12 pkt z 9 meczów, bramki 10:13; na wyjeździe 4 mecze, 7 pkt, 4:6.
- **Absencje Man Utd** (Yahoo Sports, LiveScore, Brit Brief): Šeško (uraz piszczeli, do nowego roku), Baleba (ścięgno podkolanowe), Ugarte (ACL), Shaw, Lisandro Martínez (zawieszony po czerwonej kartce z Chelsea); Maguire czeka na test sprawności; Rashford i Dorgu to rozbieżne doniesienia (doubt / poza kadrą). Z kontekstu: United po 9 meczach bez wygranej wygrali we wtorek 3-2 z Romą w Lidze Mistrzów (po 0-2), trener Carrick pod presją.
- **Absencje Aston Villi** (te same źródła): Cash (zawieszony za kartki), Onana (więzadła), Ruggeri; Wan-Bissaka blisko powrotu. Villa przegrała ostatnio 3-0 z Barceloną, wcześniej pokonała Man City.
- **Sędzia**: Anthony Taylor (jedno źródło, LiveScore; nieobejrzana oficjalna nominacja, brak jego statystyk kartek w tej analizie).
- **H2H**: tylko jedno pewne spotkanie z wyszukiwania: 25.05.2025 Man Utd 2-0 Villa (czerwona kartka dla Martíneza w Villi). Za mało na wnioski, waga niska.
- **Godzina**: Superbet podaje 16:30 UTC (17:30 PL); jedno źródło wspomina 18:00 GMT. Przyjmuję Superbet i LiveScore.
- **Nie znalazłem** (więc nie wyceniam z pewnością): xG i strzałów obu drużyn, średnich rożnych i kartek, potwierdzonych składów, statystyk sędziego. Dane zostały zebrane z wyszukiwarki i MCP; BettingPros nie użyty (brak klucza w sesji).

## Model

Rynek (Superbet, po usunięciu marży): 1X2 43,7 / 25,6 / 30,6%; BTTS tak 64%; Over 2.5 ok. 62%; z kursów drużynowych wychodzi λ ok. 1,75 (United) i 1,50 (Villa), łącznie ok. 3,25.

Mój bazowy: **λ 1,60 / 1,35 (suma 2,95)**. Uzasadnienie: obie drużyny strzelają po ok. 1,1 gola na mecz, liga ma niski średni bilans goli, a Villa jedzie na wyjazd ze słabą skutecznością (4 gole w 4 meczach). Przeciwwaga: dziura w obronie United (Martínez, Shaw, Baleba) i brak Cash u Villi, więc nie schodzę niżej niż do tych wartości. Zakres wrażliwości: λ 1,45/1,25 do 1,75/1,50.

| Rynek | p bazowe | zakres p (3 warianty λ) | fair | kurs Superbet | EV bazowe |
|---|---|---|---|---|---|
| 1 (United) | 43,4% | 41,8-43,8% | 2.31 | 2.17 | -6% |
| X | 24,3% | 23,0-25,7% | 4.11 | 3.70 | -10% |
| 2 (Villa) | 32,3% | 32,3-33,2% | 3.09 | 3.10 | 0% |
| 1X | 67,7% | 66,8-67,5% | 1.48 | 1.37 | -7% |
| X2 | 56,6% | 55,6-56,2% | 1.77 | 1.68 | -5% |
| Over 2.5 gola | 56,6% | 50,6-63,0% | 1.77 | 1.53 | -13% |
| Under 2.5 | 43,4% | 37,0-49,4% | 2.30 | 2.50 | +9% |
| Over 3.5 | 34,2% | 28,6-40,9% | 2.93 | 2.27 | -22% |
| **Under 3.5** | **65,8%** | **59,1-71,4%** | **1.52** | **1.63** | **+7%** |
| Under 4.5 | 82,4% | 77,2-86,3% | 1.21 | 1.25 | +3% |
| BTTS tak | 59,1% | 54,6-64,2% | 1.69 | 1.46 | -14% |
| BTTS nie | 40,9% | 35,8-45,4% | 2.45 | 2.62 | +7% |

Najczęstsze wyniki: 1-1 (11%), 2-1, 1-0, 1-2, 0-1.

Rożne i kartki: **nie wyceniam**. Skrypt dał szkic (średnia rożnych 10,6, kartek 4,8), ale bez dwóch niezależnych źródeł średnich i bez statystyk sędziego Taylora zasada z `football-analyst` zabrania rekomendowania takiego typu. Kursy Superbet dla porównania: rożne O/U 10.5 = 2.07 / 1.68, kartki O/U 4.5 = 1.71 / 2.02.

## Kupon (kurs 1.5-2.5, EV > 0, p > 50%)

Przeszukałem 100+ kombinacji i pojedynczych rynków Bet Buildera, które da się wycenić rozkładem wyniku (wynik, podwójna szansa, gole, BTTS, gole drużynowe). Kombinacje z rożnymi, kartkami i strzałami zawodników pominąłem, bo nie mam do nich danych.

| Kandydat | Kurs | p (zakres) | EV (zakres) | Uwaga |
|---|---|---|---|---|
| **Poniżej 3.5 gola** | **1.63** | 59-71% (bazowo 66%) | -4% do +16% (bazowo +7%) | najlepszy pojedynczy typ |
| 12 & Poniżej 4.5 gola | 1.67 | 56-62% | -6% do +3% | EV bazowe ok. 0 |
| Villa wygra lub zremisuje & Poniżej 5.5 gola | 1.85 | 50-55% | -7% do +2% | EV bazowe -3% |
| Poniżej 2.5 gola | 2.50 | 37-49% | -8% do +23% | p < 50%, poza progami |
| Wszystkie z BTTS tak / Over 2.5 | - | - | ujemne we wszystkich wariantach | rynek wycenia te typy lepiej niż mój model |

**Najlepszy kandydat: Poniżej 3.5 gola @ 1.63 (jedna noga).**
- p bazowe 66%, fair 1.52, EV +7%. Kryteria domyślne (kurs 1.5-2.5, p > 50%, EV > 0) spełnione w wariancie bazowym.
- Stawka wg Kelly'ego: pełny Kelly 11% bankrolla, 1/4 Kelly ok. 2,7% (kwotę w zł wyznaczy bankroll użytkownika; przy 5 zł nie przekraczamy limitu connectora).
- **Zastrzeżenie:** p modelowe jest o 7-8 pp wyższe niż rynek bez marży (58%). Powód (niski bilans goli obu drużyn) jest realny, ale nie jest "konkretną informacją kadrową", a kadrowo mecz przemawia raczej za większą liczbą goli (osłabiona obrona United, brak Cash). Przy p rynkowym 58% EV = -5%. Pewność typu: **niska**.
- Ryzyka: mecz otwarty z błędami w obronie (United stracili dwa gole z Romą i wygrali 3-2, co pokazuje podatność obrony), 4+ goli (ok. 34% w modelu bazowym, 41% w wariancie rynkowym), czerwona kartka (kurs 4.20 na przynajmniej jedną w meczu, czyli ok. 20% wg rynku).
- Kurs z API to tylko szacunek; wiążący jest kurs z kuponu w przeglądarce.

Przy takim EV i niskiej pewności uczciwa rekomendacja to: **zagrać tylko za wyraźną zgodą użytkownika** albo odpuścić mecz.

## Dodatek: rożne i kartki (dalsze poszukiwania)

Dane z wyszukiwarki są cząstkowe i miejscami sprzeczne, więc to szkic, nie podstawa typu.
- **Kartki**: średnia ligi 2026/27 to 4,31 kartki na mecz (388 w 90 meczach). Anthony Taylor: ok. 3,9-4,2 żółtej na mecz w 2025/26 (StatBunker, ValueStats; Squawka podaje inną próbę). Dla meczu przyjmuję 4,1-4,3. Brak per-team statystyk kartek obu klubów; fauli: Man Utd 12,5, Villa 9,75 na mecz (Footystats).
  - Under 4.5 kartki @ 2.02: p modelowe 58-61%, rynek bez marży 46%. Rozjazd 12-15 pp (kursy drużynowe Superbet sugerują łącznie ok. 5 kartek), czyli nie wiem, czego nie wiem. **Brak typu** (zasada: rozbieżność > 1 kartka bez wyjaśnienia).
- **Rożne**: CornerValue/Footiqo dają Man Utd ok. 6,2 i Villa ok. 3,8 rożnych na mecz (suma ok. 10,0), próbki 9 meczów. Under 10.5 @ 1.68: p 58%, EV ok. -2%; Over 10.5 @ 2.07: p 42%, EV -14%. **Brak przewagi.**
- Rynki zawodnika (strzały celne Mbeumo, Cunha, Jacksona itd.) nie wyceniane: brak potwierdzonych składów (zasada: bez składu maksymalnie niska pewność, nie wariant główny).

**Wniosek końcowy: żaden rynek tego meczu nie daje wiarygodnej przewagi. Rekomendacja: nie grać.**

*Oszacowania probabilistyczne, nie gwarancje.*

---

## Aktualizacja 17:10 (po oficjalnych składach, superbet-mcp)

- **Składy oficjalne.** United 4-2-3-1: Lammens; Mazraoui, Yoro, Maguire, Dalot; Tielemans, Mainoo; Amad, Fernandes, Cunha; Mbeumo. Villa 4-2-3-1: Suzuki; Lindelöf, Harwood-Bellis, Torres, Maatsen; Kamara, Goretzka; Alysson, McGinn, Manzambi; Jackson. Nieobecni (connector): United - Dorgu, Ugarte, Shaw, Baleba, Šeško, Martínez (zaw.); Villa - Ruggeri, Onana, Wan-Bissaka. Maguire gra.
- **Sędzia: Chris Kavanagh** (connector `superbet_stats`), a nie Taylor ze wcześniejszego researchu; wiążący jest connector. Statystyk kartek Kavanagha nie zebrano, więc rynki kartek nadal bez typu.
- **Średnie sezonu (connector):** United 1.1 gola strzelonego / 1.7 straconego, xG 1.6, SoT 5.0, rożne 6.1; Villa 1.1 / 1.4, xG 1.2, SoT 3.0, rożne 3.7.
- **Wnioski:** oficjalne składy nie dają konkretnej informacji, która uzasadniałaby p Under 3.5 o 8 pp powyżej rynku, więc Under 3.5 zostaje z niską pewnością (poza kuponem). Skład United ma pełny atak (Fernandes, Cunha, Mbeumo, Amad).
- **Wycena nóg (kurs z API, 3 warianty λ: 1.6/1.35, 1.75/1.5, 1.5/1.3):**

| Noga | Kurs | p (zakres) | EV (zakres) | Pewność |
|---|---|---|---|---|
| **X2 (Villa wygra lub zremisuje)** | 1.77 | 56,2-58,0% (bazowo 56,6%) | -0,5% do +2,7% (bazowo +0,2%) | średnia |
| 12 & Poniżej 4.5 | 1.66 | 56,4-61,0% | -6,3% do +1,3% | średnia |
| X2 & Poniżej 4.5 | 2.10 | 45,4-50,8% | -4,7% do +6,6% | p < 50% w bazie |

Wybór: **X2 @ 1.77**, jedna noga. EV praktycznie zerowe (p blisko rynku bez marży ok. 56%), bez realnej przewagi. Zakład niemal "fair", ale nie wartościowy.
