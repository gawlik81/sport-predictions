# Analiza piłkarska cz. 2 - 30.10-31.10.2026 (Bundesliga, Serie A, Ekstraklasa)

Czas polski (CET, UTC+1 od 25.10). Analiza zbiorcza 16 meczów. Rynki: model Poissona (`poisson.py`) z λ ustalonymi z danych sezonu, skorygowany do rynku (DraftKings przez ESPN, kursy amerykańskie przeliczone na dziesiętne i oczyszczone z marży). BettingPros: nie użyto (brak klucza w sesji).

## Weryfikacja wydarzeń (ważne)
- **Elversberg - Mainz: to BUNDESLIGA (kolejka 8 sezonu 2026/27), nie puchar.** Pt 30.10, 20:30, Ursapharm-Arena, Spiesen-Elversberg (ESPN, Bundesliga.com). Elversberg grał w DFB-Pokal we wtorek 27.10 (Darmstadt) - mniej odpoczynku, wynik nieustalony.
- Serie A i Bundesliga (31.10): wszystkie godziny z listy zgodne z ESPN (Bologna 15:00, Udinese 18:00, Milan 20:45; Bundesliga 15:30 x5, Bayern 18:30). Uwaga: ESPN pokazuje Monza jako gościa, mecz w Bolonii; Inter jest gościem (Milan gospodarz).
- **Ekstraklasa - oficjalny terminarz 13. kolejki (ekstraklasa.org, gornikzabrze.pl) różni się od listy z zapytania:**
  - Pt 30.10: **Cracovia - Motor 18:00** (może już trwać lub być rozegrany - sprawdź godzinę przed użyciem), **Górnik - Legia 20:30** (to piątek, nie 31.10).
  - Sob 31.10: Wisła Płock - Piast 12:15; Wieczysta - Jagiellonia 14:45; **Lech - Wisła Kraków 17:30 (NIE Lech - Zagłębie)**; GKS Katowice - Widzew 20:15.
  - Pn 2.11 (pominięte): Radomiak - Śląsk 18:00, Zagłębie - Korona 18:00, Raków - Pogoń 20:30. Pary "Radomiak-Śląsk", "Raków-Pogoń" z zapytania są poprawne, ale grają 2.11; "Lech-Zagłębie" nie istnieje w tej kolejce.

## Ograniczenia danych
WebSearch nie zwrócił aktualnych zapowiedzi, składów, kontuzji ani sędziów dla żadnego meczu (wyniki dotyczyły starszych sezonów, nie używam ich). Jedyna informacja kadrowa: Elversberg bez Darvicha i Campbella (Starting11, niepotwierdzone oficjalnie). Źródła liczb: openligadb (wyniki Bundesligi 2026/27, 63 mecze), ESPN (tabela Serie A, kursy DK), ekstraklasa.org (tabela). Brak xG, rożnych, kartek, fauli drużyn, sędziów, H2H z 3 lat (H2H ligowe: Elversberg-Mainz pierwsze w lidze; pozostałe nie ustalono). Skutek: pewność maks. średnia, rynki rożne/kartki/faule i rynki zawodnika to szkic ze średnimi ligowymi, bez rekomendacji na kupon; rynki zawodnika pominięte (brak składów).

Średnie sezonu: Bundesliga 3,38 gola/mecz (gospodarze 2,11), Over 2.5 68%, Over 3.5 51%, BTTS 54% (63 mecze). Serie A ok. 3,16 gola/mecz (ESPN). Ekstraklasa ok. 3,0 (tabela).

## Tabela rynków (p = końcowe prawdopodobieństwo po kalibracji, fair = 1/p)

| Mecz | 1 / X / 2 | 1X | X2 | 12 | Over 1.5 | Over 2.5 | Over 3.5 | BTTS tak | Pewność |
|---|---|---|---|---|---|---|---|---|---|
| Elversberg - Mainz (30.10 20:30) | 30,5 / 24 / 45,5 (3.28/4.17/2.20) | 54,5 (1.83) | 69,5 (1.44) | 76 (1.32) | 82 (1.22) | 60 (1.67) | 41 (2.44) | 61 (1.64) | średnia |
| Bologna - Monza (31.10 15:00) | 55 / 24,5 / 20,5 (1.82/4.08/4.88) | 79,5 (1.26) | 45 (2.22) | 75,5 (1.32) | 74 (1.35) | 51 (1.96) | 27 (3.70) | 50 (2.00) | średnia |
| Udinese - Roma (31.10 18:00) | 18,5 / 24,5 / 57 (5.41/4.08/1.75) | 43 (2.33) | 81,5 (1.23) | 75,5 (1.32) | 76 (1.32) | 53 (1.89) | 29 (3.45) | 48 (2.08) | średnia |
| Milan - Inter (31.10 20:45) | 27,5 / 26 / 46,5 (3.64/3.85/2.15) | 53,5 (1.87) | 72,5 (1.38) | 74 (1.35) | 77 (1.30) | 55 (1.82) | 32 (3.13) | 56 (1.79) | średnia |
| Leverkusen - Stuttgart (15:30) | 51 / 22 / 27 (1.96/4.55/3.70) | 73 (1.37) | 49 (2.04) | 78 (1.28) | 86 (1.16) | 66 (1.52) | 46 (2.17) | 65 (1.54) | średnia |
| Gladbach - Paderborn (15:30) | 44 / 26 / 30 (2.27/3.85/3.33) | 70 (1.43) | 56 (1.79) | 74 (1.35) | 75 (1.33) | 51 (1.96) | 34 (2.94) | 54 (1.85) | niska |
| Augsburg - Freiburg (15:30) | 32 / 25 / 43 (3.13/4.00/2.33) | 57 (1.75) | 68 (1.47) | 75 (1.33) | 78 (1.28) | 55 (1.82) | 33 (3.03) | 58 (1.72) | niska |
| Schalke - RB Leipzig (15:30) | 22 / 25 / 53 (4.55/4.00/1.89) | 47 (2.13) | 78 (1.28) | 75 (1.33) | 74 (1.35) | 52 (1.92) | 31 (3.23) | 49 (2.04) | niska/średnia |
| Werder - Hoffenheim (15:30) | 34 / 24 / 42 (2.94/4.17/2.38) | 58 (1.72) | 66 (1.52) | 76 (1.32) | 83 (1.20) | 64 (1.56) | 43 (2.33) | 64 (1.56) | niska |
| Bayern - Dortmund (18:30) | 69 / 17,5 / 13,5 (1.45/5.71/7.41) | 86,5 (1.16) | 31 (3.23) | 82,5 (1.21) | 85 (1.18) | 67 (1.49) | 47 (2.13) | 57 (1.75) | średnia |
| Cracovia - Motor (30.10 18:00) | 38 / 26 / 36 (2.63/3.85/2.78) | 64 (1.56) | 62 (1.61) | 74 (1.35) | 74 (1.35) | 49 (2.04) | 27 (3.70) | 54 (1.85) | niska |
| Górnik - Legia (30.10 20:30) | 41 / 26 / 33 (2.44/3.85/3.03) | 67 (1.49) | 59 (1.69) | 74 (1.35) | 73 (1.37) | 48 (2.08) | 26 (3.85) | 52 (1.92) | niska |
| Wisła Płock - Piast (31.10 12:15) | 34 / 27 / 39 (2.94/3.70/2.56) | 61 (1.64) | 66 (1.52) | 73 (1.37) | 71 (1.40) | 46 (2.17) | 24 (4.17) | 51 (1.96) | niska |
| Wieczysta - Jagiellonia (14:45) | 40 / 26 / 34 (2.50/3.85/2.94) | 66 (1.52) | 60 (1.67) | 74 (1.35) | 74 (1.35) | 49 (2.04) | 27 (3.70) | 54 (1.85) | niska |
| Lech - Wisła Kraków (17:30) | 64 / 20 / 16 (1.56/5.00/6.25) | 84 (1.19) | 36 (2.78) | 80 (1.25) | 81 (1.24) | 59 (1.69) | 36 (2.78) | 54 (1.85) | średnia |
| GKS Katowice - Widzew (20:15) | 50 / 26 / 24 (2.00/3.85/4.17) | 76 (1.32) | 50 (2.00) | 74 (1.35) | 75 (1.33) | 50 (2.00) | 28 (3.57) | 52 (1.92) | niska |

Zakłady bez remisu (DNB, p): Elv 40/Mainz 60; Bologna 72; Roma 77; Milan 38/Inter 62; Leverkusen 64; Gladbach 59; Augsburg 44/Freiburg 56; Leipzig 72; Werder 46/Hoffenheim 54; Bayern 83; Górnik 56/Legia 44; Lech 80; GKS 68.

## Szczegóły meczów

### Elversberg - Mainz (Bundesliga, pt 30.10, 20:30)
Tabela po 7 kol.: Mainz 7. (10 pkt, 16:13), Elversberg 8. (10 pkt, 12:15). Elversberg: 3:2 Lev, 4:3 Gladbach(wyj), 1:2 Bayern, 0:0 S04, 0:1 Union, 4:3 Aug, 0:4 Leipzig (traci 2,1 gola/mecz). Mainz: 0:0, 5:0 HSV, 1:3, 4:3 Gladbach(wyj), 3:4 Lev, 1:0 S04(wyj), 2:3 Bremen (mecze Mainz średnio 3,3 gola). Rynek DK: 30/25/45 (zgodne z modelem), Over 3.5 +115 (44% - wyższe od mojego 41%). Skład: brak Darvicha i Campbella (niepotwierdzone), Pokal we wtorek.
**Typ:** Mainz DNB 60% (1.67), lub Over 2.5 60% / BTTS 61%. **Ryzyka:** remis 24% i wygrana Elversberga 30,5% (podobna waga), zmęczenie Elversberga zmniejsza ich ofensywę, ale przy 2,1 straconych gola Elversberga i tak mecz otwarty.

### Bologna - Monza (Serie A, sob 15:00)
Bologna 11. (11 pkt, 12:12), Monza 16. (7 pkt, 16:22, szczyt: Varela 8 goli). Monza traci 2,4/mecz, ale atakuje (1,8/m). Rynek DK: Bologna -150, X +280, Monza +360 (55,5/24,4/20,1) - zgodne z modelem. Over 2.5 -125: rynek 52%, model 51%.
**Typ:** Bologna 1X 79,5% (1.26) lub Bologna DNB 72%. **Ryzyka:** remis 24,5% i wygrana Monzy 20,5%; kontuzje nieznane.

### Udinese - Roma (Serie A, sob 18:00)
Roma 3. (21 pkt, 23:8), Udinese 17. (5 pkt, 9:18, forma DLLLL, 1-2-6). Rynek DK: Roma -195 (61%), X +330, Udinese +425. Korekta: Udinese na serii czterech porażek (underdog w kryzysie, brak informacji o zmianie trenera) - p Romy obniżona z 60 do 57% (-3 pp, w granicy 5 pp od rynku); Over 2.5 model 49 -> 53% (rynek 59%). Malen 7 goli w Romie.
**Typ:** Roma lub remis (X2) 81,5% (1.23); Roma DNB 77% (1.30). **Ryzyka (obie twarze):** remis 24,5% i wygrana Udinese 18,5% (desperacja po serii porażek).

### Milan - Inter (Serie A, sob 20:45, San Siro)
Inter 1. (25 pkt, 25:10), Milan 5. (18 pkt, 18:11). Rynek DK: Milan +245, X +255, Inter -105 (26,7/26,0/47,3), Over 2.5 -165 (59%). Mecz bez wyraźnego faworyta: Inter minimalny, p 46,5% - **brak mocnego typu**. Derby podnosi kartki (szkic średniej 5,2: Over 4.5 56%, Under 4.5 44%, bez znanego sędziego, niska pewność).
**Typ (najlepszy rynek):** Inter lub remis X2 72,5% (1.38); Over 1.5 77% (1.30). **Ryzyka:** wygrana Milanu 27,5% i remis 26% o podobnej wadze; składy i absencje nieznane.

### Leverkusen - Stuttgart (Bundesliga, sob 15:30)
Leverkusen 4. (13 pkt, 16:12): 2:1 Freiburg, 0:3 Hoffenheim (wyj, ostatni). Stuttgart 15. (6 pkt, 10:13): 2:3 z Gladbach (ostatni), seria 4 porażek w 5. Rynek DK: Lev -130 (52,3%), X +320, Stu +260. Model zgodny. Over 3.5 -135 (rynek 54%) vs model 45-46%: nie schodzę, ale zostawiam 46%.
**Typ:** Over 2.5 66% (1.52); Leverkusen 1X 73% (1.37). **Ryzyka:** Stuttgart w kryzysie wymusza otwartą grę; Leverkusen po 0:3.

### Gladbach - Paderborn (Bundesliga, sob 15:30)
Gladbach 18. (3 pkt, 11:22 - najgorsza obrona, 3,1 straconych/m). Paderborn 12. (8 pkt, 6:9; wygrał 1:0 z HSV, remisuje często). Rynek DK: Glad -105 (47,5%), X 24,4%, Pad 28,1%; Under 3.5 -150 (60%). Model Under 3.5 71% -> 66% (rynek i średnia ligi sugerują więcej goli). Gladbach to gospodarz w kryzysie (1-6): nie wolno obniżać faworyta za formę, ale tu faworyt jest cienki.
**Typ:** brak mocnego typu; najlepszy: Under 3.5 66% (1.52) lub Gladbach 1X 70% (1.43). **Ryzyka:** wygrana Paderborna 30%, remis 26%.

### Augsburg - Freiburg (Bundesliga, sob 15:30)
Freiburg 3. (13 pkt, 16:9), ale 1:3 z Bayernem; Augsburg 9. (9 pkt, 17:13, trzy remisy). Rynek DK: Aug 31%, X 25%, Fri 44%. Model 33/25/42 - zgodne.
**Typ:** brak mocnego typu; Freiburg X2 68% (1.47), Over 1.5 78% (1.28). **Ryzyka:** wygrana Augsburga 32% (bardzo ofensywny dom, remisy z Bayernem i Lev).

### Schalke - RB Leipzig (Bundesliga, sob 15:30)
Schalke 16. (6 pkt, 4:7 - najmniej goli w lidze, 3 remisy 0:0 w 7). Leipzig 5. (12 pkt, 20:11; ostatnio 4:0 z Elversbergiem, 1:6 z Bayernem). Rynek DK: Schalke 24%, X 25%, Leipzig 51%. Korekta: model 56 -> 53% Leipzig (do rynku). Over 3.5 rynek 45% vs model 26%: zbieżności brak - mecze Schalke średnio 1,6 gola, Leipzig 3-4; ustawiam 31% (nie schodzę do rynku bez danych o składach).
**Typ:** Leipzig DNB 72% (1.39) / X2 78% (1.28); Under 3.5 69% (1.45). **Ryzyka:** wygrana Schalke 22%, remis 25% (Schalke remisuje 3 razy), kontuzje nieznane.

### Werder - Hoffenheim (Bundesliga, sob 15:30)
Werder 6. (12 pkt, 15:14; mecze 3,2 gola/m), Hoffenheim 10. (9 pkt, 14:14; 3:0 z Lev). Rynek DK: Werder 33,6%, X 24,3%, Hoffenheim 42,1% (goście faworytem). Over 3.5 49%. Model zgodny. 
**Typ:** Over 2.5 64% (1.56) / BTTS 64% (1.56). **Ryzyka:** zero goli po jednej stronie; wynik 1X2 bliski 50/50 - brak mocnego typu wyniku.

### Bayern - Dortmund (Bundesliga, sob 18:30)
Bayern 1. (17 pkt, 25:6; 5-2-0), Dortmund 2. (17 pkt, 12:4; 5-2-0, 1:0 Frankfurt). Rynek DK: Bayern -310 (69%), X 17%, BVB 13%, Over 3.5 -155 (58%) vs model 44 -> 47%. Dortmund broni bardzo szczelnie (0,6 straconych/m), ale Bayern stracił gola w 5 z 7 meczów. Informacje o Kane/Neuer: wyniki wyszukiwania bez daty, nie użyte; nie znaleziono składów.
**Typ:** Bayern 69% (1.45); Over 2.5 67% (1.49). Bayern 1X 86,5% (1.16, graniczny). **Ryzyka (obie twarze):** remis 17,5% (BVB nie przegrał w 7) i wygrana BVB 13,5%.

### Ekstraklasa (tabela ekstraklasa.org po 11-12 kolejkach; brak kursów, brak składów, brak sędziów, forma niedostępna)
Wszystkie pewności niskie, bo brak informacji kadrowych; średnia ligi ok. 3,0 gola/mecz.
- **Cracovia - Motor (pt 18:00, trwa/rozegrany?)** 13. (12 pkt, 14:19) vs 12. (13 pkt, 17:21). Mecz równy. Brak mocnego typu. Najlepszy: Over 1.5 74% (1.35); BTTS 54%.
- **Górnik - Legia (pt 20:30)** 2. (27 pkt, 21:11) vs 4. (23 pkt, 23:11), obie z mocną defensywą. Brak mocnego typu. Najlepszy: Górnik 1X 67% (1.49); Under 3.5 74%.
- **Wisła Płock - Piast (sob 12:15)** 11. (14 pkt, 10:16) vs 6. (20 pkt, 22:18). Brak mocnego typu. Najlepszy: Under 3.5 76% (1.32).
- **Wieczysta - Jagiellonia (sob 14:45)** 16. (8 pkt, 16:23) vs 10. (15 pkt, 14:17). Brak mocnego typu. Najlepszy: Over 1.5 74% (1.35).
- **Lech - Wisła Kraków (sob 17:30)** 1. (28 pkt, 29:10, 2,6 gola/m u siebie) vs 5. (21 pkt, 19:15). Lech 64% (1.56), DNB 80% (1.25), 1X 84% (1.19, graniczny). Ryzyka: remis 20% i wygrana Wisły 16%.
- **GKS Katowice - Widzew (sob 20:15)** 8. (18 pkt, 22:17) vs 14. (11 pkt, 15:16; 8 remisów w 12 meczach - remis podbity do 26%). GKS 50%, GKS DNB 68% (1.47), 1X 76% (1.32).

## Rynki dodatkowe (rożne, kartki, faule) - szkic bez danych
Brak średnich drużynowych i sędziów (zob. ograniczenia), więc stosowane średnie ligowe, **bez rekomendacji i bez wejścia na kupon**:
- Rożne (średnia 9,8-10,2): Over 9.5 51-55% (1.8-2.0), Over 8.5 62% (1.61), Over 10.5 39%. Bayern-Dortmund i Leverkusen-Stuttgart: bliżej 10,5 (faworyt dominuje) - niezweryfikowane.
- Kartki Bundesliga (średnia 4,0): Over 3.5 54% (1.86), Over 4.5 37%. Serie A (4,8): Over 3.5 66% (1.50), Over 4.5 50% (1.99); Milan-Inter 5,2: Over 4.5 56% (1.77).
- Faule (24): Over 22.5 60% (1.67), Over 24.5 45% (2.24).
- Rynki zawodnika: pominięte (brak składów i potwierdzonych absencji).

## Najlepsze rynki (fair > 1.15; graniczne 1.15-1.20 oznaczone)
| Mecz | Rynek | p | Fair | Pewność |
|---|---|---|---|---|
| Bayern - Dortmund | Bayern wygra | 69% | 1.45 | średnia |
| Bayern - Dortmund | Over 2.5 | 67% | 1.49 | średnia |
| Leverkusen - Stuttgart | Over 2.5 | 66% | 1.52 | średnia |
| Udinese - Roma | Roma lub remis | 81,5% | 1.23 | średnia |
| Bologna - Monza | Bologna 1X | 79,5% | 1.26 | średnia |
| Schalke - Leipzig | Leipzig lub remis | 78% | 1.28 | niska/średnia |
| Lech - Wisła Kraków | Lech DNB | 80% | 1.25 | średnia |
| Elversberg - Mainz | Over 1.5 | 82% | 1.22 | średnia |
| Werder - Hoffenheim | Over 2.5 / BTTS | 64% | 1.56 | niska |
| Milan - Inter | Inter lub remis | 72,5% | 1.38 | średnia |
| Leverkusen - Stuttgart | Over 1.5 (graniczny) | 86% | 1.16 | średnia |

## Odrzucone / bez typu
- Radomiak - Śląsk, Zagłębie - Korona, Raków - Pogoń: gra 2.11 (poza zakresem). Lech - Zagłębie: para nie istnieje.
- Milan - Inter, Gladbach - Paderborn, Augsburg - Freiburg, Werder - Hoffenheim (wynik), Cracovia - Motor, Górnik - Legia, Płock - Piast, Wieczysta - Jagiellonia: wyrównane, brak mocnego typu wyniku (wszystkie rynki 1X2 < 50%).
- Cracovia - Motor: sprawdzić godzinę (start 18:00, może być w trakcie).
- Rynki rożne/kartki/faule/zawodnika: brak sędziów i danych drużynowych, bez rekomendacji.
- Bayern 1X (1.16) i Leverkusen Over 1.5 (1.16): graniczne, zbyt krótkie kursy po marży.

Wszystko to oszacowania probabilistyczne, nie gwarancje.
