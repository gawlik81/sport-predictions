# Kupon wieczorny 12.10.2026 (poniedziałek)

Założenia: każda noga > 1.2, łączny kurs > 1.6; mecze niezależne (brak bet buildera - jedna noga na mecz). Wieczorne mecze: Radomiak - Motor Lublin (18:00), Venezia... Atalanta - Venezia (17:30), Udinese... Torino - Udinese (14:45, już rozegrany wcześniej dziś - uwzględniony tylko jako punkt odniesienia do bieżącego, ale kickoff wg ESPN 18:45 CEST, wieczorny), GKS Katowice - Wieczysta Kraków (20:30), Newcastle - Coventry (21:00), Sevilla - Levante (21:00).

## Dane
- **Torino - Udinese (Serie A, 6. kolejka, 18:45 CEST):** obie drużyny po 4 pkt z 5 meczów. Torino: 7 straconych i 4 strzelone w 5 ostatnich; Adams wraca do składu, zespół bliski kompletu. Udinese: 10 straconych w 5 ostatnich (słabsza defensywa), bez Zaniolo, Gueye i Piotrowskiego. (Bleacher Nation, Sportskeeda, Sportsgambler) Rynek (DraftKings): Torino 2.40 / remis 3.00 / Udinese 3.05; O2.5 2.20, U2.5 1.667 (kursy zagraniczne, nie krajowe).
- **GKS Katowice - Wieczysta Kraków (Ekstraklasa, 20:30 CEST):** GKS niepokonany w 10 ostatnich meczach domowych. Wieczysta wygrała 2 ostatnie, strzelając w nich 7 goli (dobra forma ofensywna). Kursy polskich bukmacherów: GKS 2.02-2.19, remis ok. 3.4-3.5 (szacowane), Wieczysta 2.81-3.05; O2.5 1.48, U2.5 2.44, BTTS tak 1.43, BTTS nie 2.56. (weszlo.com, mecze24.pl)
- **Atalanta - Venezia (17:30 CEST):** Atalanta 11. w tabeli, 3 porażki z rzędu, atak "zamrożony" (1 gol w 5 meczach we wszystkich rozgrywkach), ale broni się solidnie (7 straconych w 5 ligowych). Venezia ostatnia w tabeli, 0 pkt z 5 meczów, bilans goli -9, broni się bardzo słabo (2,1-2,6 gola straconego/mecz), nie strzeliła gola w ostatnich 5 wizytach u Atalanty. (Footballwhispers, Bleacher Nation) Rynek (DraftKings): Atalanta -185 (1.54) / remis +310 (4.10) / Venezia +425 (5.25); linia totalu przesunięta na 3.5 (Over +125 / Under -160), co sugeruje wyższy oczekiwany total niż wskazywałby sam "atak zamrożony" Atalanty. **Mój model (λ 1.6/0.45) daje Under 3.5 na 76-85%, czyli >10 pp powyżej rynku (58% po usunięciu marży) - zbyt duży rozjazd bez konkretnej informacji, więc ten typ odrzucam, mimo wysokiej pewności modelu.**
- **Radomiak Radom - Motor Lublin (18:00 CEST):** obie drużyny w środku tabeli, forma zbliżona (4 pkt vs 3 pkt z 5 ostatnich). Kursy: Radomiak 2.15-2.38, remis ok. 3.48-3.50, Motor 2.90. Brak wyraźnej przewagi żadnej ze stron - pomijam.

## Wycena
| Mecz | Typ | Kurs | Moje p | Fair | EV | Pewność |
|---|---|---|---|---|---|---|
| Torino - Udinese | Torino wygra | 2.40 | 43,4% | 2.30 | +4,2% | średnia (personalia potwierdzają przewagę) |
| GKS - Wieczysta | Under 2.5 gola | 2.44 | 42,3% | 2.36 | +3,2% | niska-średnia (model vs rynek rozjeżdżają się na BTTS/O2.5 o ~5-7 pp) |
| Udinese - Torino | Under 2.5 gola | 1.667 | 59,6% | 1.68 | -0,6% | średnia |

## Kupon
**Wariant główny: Torino wygra (2.40) + GKS-Wieczysta Under 2.5 (2.44) = 5.86**, łączne p 18,4%, fair 5.45, EV +7,5%. Wysoki kurs, niska szansa trafienia - typowy "value", nie "bezpieczny" kupon.

**Wariant bezpieczniejszy: Udinese-Torino Under 2.5 (1.667) + GKS-Wieczysta Under 2.5 (2.44) = 4.07**, łączne p 25,2%, fair 3.97, EV +2,5%.

## Wariant bezpieczny (na życzenie - niższe, krótsze kursy niż warianty powyżej)
Po sygnale, że Wieczysta strzeliła 7 goli w 2 ostatnich meczach (realna, mocna forma ofensywna), skorygowałem λ GKS-Wieczysta w górę (1,65/1,5 zamiast 1,6/1,4), żeby nie schodzić >5 pp pod rynek bez uzasadnienia: Over 2.5 61,0% (rynek 62,2%), BTTS tak 62,8% (rynek 64,1%) - teraz blisko rynku.

| Mecz | Typ | Kurs | Moje p | Fair | EV |
|---|---|---|---|---|---|
| Udinese - Torino | Under 2.5 gola | 1.667 | 59,6% | 1.68 | -0,6% |
| GKS - Wieczysta | BTTS tak | 1.43 | 62,8% | 1.59 | -10,2% |

**Kupon: 1.667 x 1.43 = 2.38**, łączne p 37,4%, fair 2.67, EV -10,8%. Krótsze kursy niż w wariantach "głównym" (5.86) i "bezpieczniejszym" (4.07) wyżej - wyższa szansa trafienia (37% vs 18-25%), ale żadna noga nie ma przewagi nad rynkiem (obie ujemne EV, bo kursy odzwierciedlają marżę bukmachera przy uczciwie wycenionym meczu). To typowy kompromis "niższy kurs = mniejsza wariancja, nie większa wartość".

## Zastosowanie nowych domyślnych kryteriów (kurs nogi >1.2, kupon >1.6, EV>0, p>50%)
Pełny przegląd całego dnia 12.10.2026: piłka (6 meczów, realne kursy Unibet) + sprawdzone tenis/e-sport/MMA (brak solidnie zweryfikowanych wydarzeń - patrz uzasadnienie w odpowiedzi).

Systematyczna wycena wszystkich rynków (1X2, podwójna szansa, gole O/U, BTTS) w 6 meczach piłkarskich: EV liczone z rynkowego "fair" p (po usunięciu marży) jest matematycznie ujemne dla każdego rynku (marża Unibet ~5-9%) - to tautologia, nie błąd modelu (patrz [[feedback_kupon_default_criteria]]). Jedyny typ z uzasadnioną, własną korektą ponad rynek (konkretna informacja, nie tylko zgodność z rynkiem):

**Udinese - Torino: Under 2.5 gola, kurs 1.65 (Unibet).** Udinese gra bez 3 zawodników, w tym Zaniolo (ofensywny pomocnik/skrzydłowy) - uzasadnia to niższe λ gości (0,9 zamiast 1,0 z wcześniejszego modelu). λ 1,3/0,9 → Under 2.5 = 62,3% (rynek po usunięciu marży: 56,9% - różnica +5,4 pp, w granicach dopuszczalnej korekty, bo oparta na konkretnej informacji kadrowej).

| | |
|---|---|
| **p** | 62,3% |
| **Fair odds** | 1.61 |
| **Kurs** | 1.65 |
| **EV** | +2,8% |
| **Stawka (Kelly)** | 4,3% pełne / **2,1% (1/2 Kelly, polecane)** / 1,1% (1/4 Kelly) |

Ten jeden typ sam spełnia wszystkie cztery kryteria (kurs 1.65 > 1.2 i > 1.6 jednocześnie, p 62,3% > 50%, EV +2,8% > 0) - nie trzeba go łączyć w zestaw; dokładanie innej nogi (ujemne EV) tylko obniżyłoby łączne EV.

Pozostałe sprawdzone rynki (najbliższe progom, żadny nie kwalifikuje się - EV liczone z rynkowego fair p):
| Mecz | Typ | Kurs | p (rynek) | EV |
|---|---|---|---|---|
| Coventry - Newcastle | Under 3.5 | 1.46 | 64,5% | -5,8% |
| Levante - Sevilla | Under 2.5 | 1.74 | 54,1% | -5,9% |
| GKS - Wieczysta | Over 2.5 | 1.46 | 61,0% | -10,9% |
| GKS - Wieczysta | BTTS tak | 1.43 | 62,8% | -10,2% |
| Radomiak - Motor | Under 2.5 | 2.20 | 41,8% (rynek faworyzuje Over) | - (odrzucone - mój model 58% vs rynek 42% to >15 pp rozjazdu, nie ufam) |

## Wniosek
Oba warianty spełniają wymogi (nogi > 1.2, łącznie > 1.6), ale żaden nie jest "pewniakiem" - najlepsza szansa trafienia (GKS-Wieczysta Under 2.5, 42%) ma mniej niż 50%. Kursy zagraniczne (DraftKings) dla Torino-Udinese potraktuj jako punkt odniesienia, nie kurs krajowego bukmachera. Oszacowania probabilistyczne, nie gwarancje.
