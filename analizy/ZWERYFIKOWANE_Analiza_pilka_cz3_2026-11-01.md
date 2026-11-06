# Analiza piłkarska cz. 3 - 01.11.2026 (Bundesliga, Ligue 1)

Czas polski (CET). 6 meczów. Rynki: model Poissona (`poisson.py`, λ z danych sezonu) skalibrowany do rynku (kursy ESPN: DraftKings dla 5 meczów, Bet365 dla Frankfurt - HSV; kursy amerykańskie przeliczone na dziesiętne i oczyszczone z marży). Rożne/kartki/faule: `markets.py`. BettingPros nie użyto (brak klucza w sesji). Kursy Betclic: brak, więc "kurs rynkowy" = DK/Bet365 po usunięciu marży.

## Ograniczenia danych (ważne)
WebSearch nie zwrócił aktualnych zapowiedzi, składów, kontuzji ani sędziów dla żadnego z 6 meczów (wyniki dotyczyły starszych sezonów, nieużyte). Skutek: brak korekt kadrowych, sędziowie nieznani, rożne/kartki/faule to szkic ze średnich ligowych (BL ok. 24 faule; L1 ok. 25), pewność rynków dodatkowych maks. niska, **bez rekomendacji na kupon**; rynki zawodnika pominięte (brak potwierdzonych składów). Brak xG i H2H z ostatnich 3 lat (H2H BL tego sezonu: Frankfurt - Köln 1-0 (16.10) i HSV - Köln 2-1 (19.09) to mecze z innymi rywalami niż ta para; bezpośrednie H2H nieustalone). Źródła liczb: openligadb (wyniki BL 2026/27), ESPN (tabela Ligue 1, forma, kursy DK/Bet365).

## Tabela rynków (p = po kalibracji, fair = 1/p)

| Mecz | 1 / X / 2 | 1X | X2 | 12 | O1.5 | O2.5 | O3.5 | BTTS tak | Pewność |
|---|---|---|---|---|---|---|---|---|---|
| Union Berlin - Köln (15:30) | 35,5 / 27 / 37,5 (2.82/3.70/2.67) | 62,5 (1.60) | 64,5 (1.55) | 73 (1.37) | 75 (1.33) | 52 (1.92) | 29 (3.45) | 54 (1.85) | niska |
| Frankfurt - HSV (17:30) | 59 / 22 / 19 (1.69/4.55/5.26) | 81 (1.23) | 41 (2.44) | 78 (1.28) | 79 (1.27) | 56 (1.79) | 34 (2.94) | 54 (1.85) | średnia |
| Strasbourg - Auxerre (15:00) | 48 / 24 / 28 (2.08/4.17/3.57) | 72 (1.39) | 52 (1.92) | 76 (1.32) | 82 (1.22) | 61 (1.64) | 38 (2.63) | 61 (1.64) | niska |
| Lyon - Angers (17:15) | 66 / 20 / 14 (1.52/5.00/7.14) | 86 (1.16) | 34 (2.94) | 80 (1.25) | 78 (1.28) | 56 (1.79) | 33 (3.03) | 50 (2.00) | średnia |
| Paris FC - Monaco (17:15) | 39 / 27 / 34 (2.56/3.70/2.94) | 66 (1.52) | 61 (1.64) | 73 (1.37) | 74 (1.35) | 50 (2.00) | 28 (3.57) | 53 (1.89) | niska |
| Marseille - Toulouse (20:45) | 50 / 23 / 27 (2.00/4.35/3.70) | 73 (1.37) | 50 (2.00) | 77 (1.30) | 82 (1.22) | 62 (1.61) | 39 (2.56) | 58 (1.72) | średnia/niska |

Under (dopełnienie): U2.5 Union-Köln 48% (2.08), Frankfurt-HSV 44% (2.27), Strasbourg 39% (2.56), Lyon 44% (2.27), PFC-Monaco 50% (2.00), OM-Toulouse 38% (2.63). DNB: Union 49 / Köln 51; Frankfurt 73 / HSV 27; Strasbourg 63 / Auxerre 37; Lyon 82 / Angers 18; PFC 53 / Monaco 47; OM 65 / Toulouse 35.

## Rynki dodatkowe (szkic: średnie ligowe, sędziowie nieznani, pewność niska, bez typu na kupon)

| Mecz | Rożne (śr.) O9.5 / O10.5 | Kartki (śr.) O3.5 / O4.5 | Faule (śr.) O24.5 |
|---|---|---|---|
| Union - Köln | 9,6: 48% (2.07) / 37% (2.69) | 4,4: 60% (1.65) / 44% (2.29) | 24: 45% (2.24) |
| Frankfurt - HSV | 10,2: 55% (1.82) / 44% (2.28) | 4,2: 57% (1.75) / 40% (2.48) | 24: 45% (2.24) |
| Strasbourg - Auxerre | 9,8: 51% (1.98) / 39% (2.54) | 4,8: 67% (1.50) / 50% (1.99) | 25: 52% (1.92) |
| Lyon - Angers | 10,4: 57% (1.75) / 46% (2.17) | 4,4: 60% (1.65) / 44% (2.29) | 25: 52% (1.92) |
| Paris FC - Monaco | 9,6: 48% (2.07) / 37% (2.69) | 4,6: 64% (1.57) / 47% (2.13) | 25: 52% (1.92) |
| Marseille - Toulouse | 10,0: ok. 53% (1.89) / ok. 42% (2.38) | 5,0: 69% (1.44) / 53% (1.87) | 25: 52% (1.92) |

Korekty: rożne Frankfurt (+0,6, dominacja gospodarza) i Lyon (+0,8, faworyt 66% kontra Angers); kartki OM-Toulouse (+0,6, Marseille zwykle wysoka liczba kartek, niepotwierdzone danymi), Strasbourg-Auxerre (+0,4, mecz o punkty, 17. vs 12. miejsce). Kartki liczone: żółta = 1 (czerwona do uzgodnienia z linią bukmachera).

## Szczegóły meczów

### Union Berlin - 1. FC Köln (Bundesliga, nd 01.11, 15:30, An der Alten Försterei)
**Typ:** brak mocnego typu (3-way ok. 35/27/38). Najlepszy rynek: Köln lub remis X2 64,5% (1.55); Over 1.5 75% (1.33). **Pewność:** niska.
**Statystyki:** Union 18. (6 pkt, bilans 1-3-3, bramki 6:18; forma DDDWL; porażki 0-7 Bayern, 0-4 Leverkusen, ale 0-0 Dortmund, 1-1 Augsburg, 1-0 Elversberg). Köln 14. (8 pkt, 8:11; forma DDLWL; 0-0 Schalke, 2-1 Gladbach). Oba ataki słabe (0,86 i 1,14 gola/mecz), Union traci 2,6/mecz (zawyżone przez Bayern/Leverkusen).
**H2H:** brak ustalonych bezpośrednich meczów z ostatnich 3 lat w sesji; waga zero.
**Rynek (DK, bez marży):** Union 35,8 / X 27,0 / Köln 37,2; O2.5 56% (-145/+115). Model Over 2.5 47% vs rynek 56% (różnica 9 pp > 5), bez konkretów nie schodzę do modelu: p=52% (kompromis). Remis i obie wygrane o podobnej wadze.
**Ryzyka:** 1-1/0-0 (remis 27%), Union u siebie wygrywa 35,5%, Köln 37,5% - mecz bez faworyta; niskie ataki podważają Over.

### Eintracht Frankfurt - Hamburger SV (Bundesliga, 17:30, Deutsche Bank Park)
**Typ:** Frankfurt 1X 81% (1.23) lub Frankfurt DNB 73% (1.37); Frankfurt wygrana 59% (1.69). **Pewność:** średnia.
**Statystyki:** Frankfurt 15. (8 pkt, 10:17, 2-2-3; forma DLWLD; 0-6 Leipzig, 0-1 Dortmund, 1-0 Köln, 1-4 Augsburg). HSV 13. (9 pkt, 6:16, 3-0-4; forma DLWWW, ale 2-3 wygrane skromne: 1-0 Stuttgart, 2-3 u Hoffenheim; 0-1 Paderborn). Oba tracą ponad 2,2 gola/mecz; HSV strzela 0,86.
**H2H:** poprzedni sezon 2025/26: Frankfurt - HSV 1-2 w lidze (Aytekin) i HSV - Frankfurt 0-3 (inny skład; waga niska).
**Informacje medialne:** brak aktualnych zapowiedzi i listy absencji (Bundesliga.com: skład 60 min przed meczem). Nie wprowadzam korekt kadrowych.
**Rynek (Bet365, bez marży):** 61,7 / 20,1 / 18,2; model 57,3 / 22,6 / 20,1; finalnie 59 / 22 / 19 (różnica do rynku 2,7 pp, w normie).
**Ryzyka (obie twarze):** remis 22% (HSV zdobywa mało, ale Frankfurt ma słabą formę) i wygrana HSV 19% (forma 3 z 5 wygranych, kontratak vs defensywa Frankfurtu 2,4/mecz).

### Strasbourg - Auxerre (Ligue 1, 15:00)
**Typ:** Over 2.5 61% (1.64) / BTTS tak 61% (1.64); wynik: Strasbourg 1X 72% (1.39). **Pewność:** niska.
**Statystyki:** Strasbourg 16. (7 pkt, 8 meczów, 12:18, forma DLLLD, 2-1-5). Auxerre 12. (10 pkt, 12:18, forma DWLWW, 3-1-4). Oba tracą ok. 2,25 gola/mecz, strzelają 1,5. Średnia ligi (z tabeli) ok. 3,2 gola/mecz.
**H2H:** brak danych w sesji.
**Rynek (DK):** 1 54,5% (bez marży 52) / X 24 / 2 24; linia goli 3,5 (O3.5 +140, rynek ok. 39% bez marży - model 37,5%). Model wyniku 44,7/23,6/31,7 vs rynek 52/24/24: różnica 7 pp u gospodarza; Strasbourg jest faworytem rynkowym mimo słabej formy, a reguła zabrania obniżać p faworyta za forma bez konkretów, więc finalnie 48 (kompromis, nie 44,7). Auxerre w lepszej formie jest realnym zagrożeniem.
**Ryzyka:** wygrana Auxerre 28% i remis 24% (podobna waga); mecz otwarty (Under 2.5 39%).

### Lyon - Angers (Ligue 1, 17:15)
**Typ:** Lyon 1X 86% (1.16, graniczny); Lyon wygrana 66% (1.52). **Pewność:** średnia.
**Statystyki:** Lyon 5. (14 pkt, 8 meczów, 13:7, forma DLWWL, 4-2-2). Angers 14. (8 pkt, 9:15, forma DLLWD, 2-2-4); Lyon traci 0,9/mecz, Angers strzela 1,1.
**H2H:** brak danych w sesji.
**Rynek (DK):** 67,4 / 19,0 / 13,6; O2.5 58% (-160/+125). Model 64,2/20,7/15,1; finalnie 66/20/14 (w normie). Over 2.5 56% (model 54%, rynek 58%).
**Ryzyka (obie twarze):** remis 20% i wygrana Angers 14% (underdog bez wygranej serii, bez informacji o trenerze/kryzysie, korekta kryzysowa nie zastosowana); Lyon czasem gubi punkty (L w 2 z ostatnich 5).

### Paris FC - AS Monaco (Ligue 1, 17:15)
**Typ:** brak mocnego typu (39/27/34). Najlepszy rynek: Over 1.5 74% (1.35) lub 12 (bez remisu) 73% (1.37). **Pewność:** niska.
**Statystyki:** Paris FC 6. (14 pkt, 13:9, forma DWLWD, 4-2-2). Monaco 4. (15 pkt, 8 meczów, 11:7, forma DWLWD, 4-3-1). Oba z silną defensywą (ok. 1,1 straconego/mecz) i umiarkowanym atakiem.
**H2H:** brak danych w sesji.
**Rynek (DK):** 38,8 / 27,2 / 34,0 (model identyczny); O2.5 54% vs model 46%: finalnie 50% (zbliżenie do rynku o 4 pp, bez konkretów nie schodzę poniżej).
**Ryzyka:** wyrównany mecz, remis 27%; obie drużyny skuteczne w defensywie, Under 2.5 50%.

### Marseille - Toulouse (Ligue 1, 20:45, Vélodrome)
**Typ:** Marseille 1X 73% (1.37); Marseille wygrana 50% (2.00). Over 1.5 82% (1.22, graniczny). **Pewność:** średnia/niska.
**Statystyki:** Marseille 9. (12 pkt, 8 meczów, 18:13, forma DLWLW, 4-0-4: wyniki bardzo zmienne). Toulouse 11. (10 pkt, 12:11, forma DWDWD, 2-4-2: dużo remisów). Marseille strzela 2,25/mecz.
**H2H:** brak danych w sesji.
**Rynek (DK):** 48,9 / 23,9 / 27,3 (moneyline -105/+300/+250); linia goli 3,5 (O3.5 +120, rynek ok. 43% bez marży; wartość linii 3,5 zweryfikować, ESPN mógł podać złą linię). Model O3.5 37,5%; finalnie 39%.
**Ryzyka (obie twarze):** remis 23% (Toulouse 4 remisy w 8) i wygrana Toulouse 27%; niestabilna forma Marseille (4 porażki w 8).

## Najlepsze rynki wg meczu (kandydaci; wszystkie z pewnością niską/średnią, bez rynków dodatkowych)

| Mecz | Rynek | p | fair | Pewność | Zależy od | Kurs rynkowy |
|---|---|---|---|---|---|---|
| Frankfurt - HSV | Frankfurt wygrana | 59% | 1.69 | średnia | składy (brak informacji) | Bet365 1.55 (EV ujemne, rynek 61,7%) |
| Frankfurt - HSV | Frankfurt 1X | 81% | 1.23 | średnia | składy | nieznany (Betclic) |
| Lyon - Angers | Lyon wygrana | 66% | 1.52 | średnia | składy | DK ok. 1.41 (-245) |
| Lyon - Angers | Lyon 1X | 86% | 1.16 | średnia | graniczny kurs | nieznany |
| Strasbourg - Auxerre | Over 2.5 | 61% | 1.64 | niska | skład, brak linii 2.5 w DK (linia 3.5) | nieznany |
| Marseille - Toulouse | Marseille 1X | 73% | 1.37 | średnia/niska | skład | nieznany |
| Marseille - Toulouse | Over 1.5 | 82% | 1.22 | niska | - | nieznany |
| Union - Köln | Over 1.5 | 75% | 1.33 | niska | - | nieznany |
| Paris FC - Monaco | Over 1.5 | 74% | 1.35 | niska | - | nieznany |

Wniosek: brak typu z wyraźną przewagą nad rynkiem (modele w 2-3 pp od rynku); najpewniejsze wyniki to Lyon i Frankfurt, a Union - Köln i Paris FC - Monaco to "brak mocnego typu".

To są oszacowania probabilistyczne, nie gwarancje.
