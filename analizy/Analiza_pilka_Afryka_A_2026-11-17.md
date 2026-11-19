# Analiza piłka - reprezentacje Afryki (A), 17.11.2026, 17:00 PL

Rozgrywki (wszystkie 6 meczów): eliminacje Pucharu Narodów Afryki 2027 (AFCON 2027, grupy po 4-5 drużyn, mecze w układzie dom-wyjazd w "okienku podwójnym"). To rewanże meczów rozegranych 12-14.11.2026, czyli rangą pełnoprawne mecze o stawkę (nie towarzyskie). Kursy: Superbet (superbet-mcp), marża ok. 8-9% na 1X2 (p rynku liczone po jej usunięciu). BettingPros: nie użyty (brak potrzeby, kraje poza zakresem).

Dane: statystyki Superbet to średnie z ok. 3 meczów sezonu (mała próba), wiele meczów Afryki nie ma xG; skład/absencje niedostępne w `superbet_missing_players` ani `superbet_lineups` (brak danych dla tych wydarzeń). Rożne i kartki: tylko jedno źródło i n=3, więc BRAK PODSTAW do wyceny (nie fabrykuję), pewność rynków dodatkowych: niska. Wszystkie mecze: pewność ogólna niska do średniej, p blisko rynku (nie schodzę pod rynek >5 pp bez konkretów).

Modele: `poisson.py` z λ własnym, skalibrowanym do rynku i kontekstu. Wynik 17:00 PL = 16:00 UTC.

---

## 1. Gambia - Wybrzeże Kości Słoniowej ("WKS"), 17:00 PL, ID 15752172
Rozgrywki: eliminacje AFCON 2027, grupa C (rewanż, pierwszy mecz 12.11: WKS 2-1 Gambia). Stadion Independence, sędzia Mehrez Melki (Tunezja).

**λ: Gambia 0,80 / WKS 1,40** (rynek bez marży ~0,70/1,50; Superbet: 1 5.75, X 3.45, 2 1.59; O2.5 2.22).

| Rynek | p | fair | kurs Superbet | uwagi |
|---|---|---|---|---|
| WKS wygra | 51,1% | 1.96 | 1.59 | brak value |
| Remis | 27,4% | 3.65 | 3.45 | |
| Gambia wygra | 21,4% | 4.67 | 5.75 | rynek 15,9%, EV ujemne/neutralne |
| X2 | 78,6% | 1.27 | 1.09 | EV -14% |
| 12 | 72,6% | 1.38 | 1.25 | EV -9% |
| Under 3.5 | 81,9% | 1.22 | 1.19 | EV -2% |
| Under 2.5 | 62,3% | 1.61 | 1.57 | EV -2% |
| Over 1.5 | 64,5% | 1.55 | 1.39 | EV -10% |
| BTTS nie | 58,5% | 1.71 | 1.57 | EV -8% |
| WKS strzeli >=1 | 75,3% | 1.33 | 1.18 | |
| Gambia strzeli >=1 | 55,1% | 1.81 | 1.85 | |

Rożne i kartki: brak podstaw (Gambia 3,7 vs WKS 9,0 rożnych/mecz z n=3, kartki 1,3/1,7; sędzia nieznana średnia). Najlepszy rynek: Under 2.5 / BTTS nie bez przewagi, mecz bez mocnego typu.
**Statystyki:** Gambia: 2:1 Somalia, 4:2 Ghana (wyjazd), 1:2 WKS; 1:3 z Senegalem i 1:3 z Iranem w sparingach; średnio strzela 2,3, traci 1,7. WKS: 2:0 Ghana, 2:0 Somalia, 0:1 Kamerun (towarzyski), 1:2 Norwegia (czerwiec); traci 0,3, strzela 2,0 (w eliminacjach).
**H2H:** WKS wygrywa 5 ostatnich bezpośrednich (1:0 2025, 2:0 2023, 2:1 12.11.2026).
**Media:** Hervé Renard przejmuje kadrę WKS z 8 debiutantami (odmłodzenie, rotacja możliwa) - CAF; WKS prowadzi w grupie C po wygranej 12.11 (Fratmat). Gambia (McKinstry) ma 6 pkt.
**Ryzyka:** rotacja/debiutanci WKS po meczu 12.11, wynik Gambii u siebie (stadion Independence) bywa bardziej otwarty; Gambia musi atakować.
**Pewność:** niska-średnia.

---

## 2. Kenia - RPA, 17:00 PL, ID 15752173
Eliminacje AFCON 2027, grupa D (RPA-Kenia 2:2 w pierwszym meczu 13.11, gol w 90. min). Nyayo Stadium Nairobi, sędzia Beida Dahane (Mauretania).
Uwaga: Kenia jest współgospodarzem AFCON 2027 (z Ugandą i Tanzanią) i już ma zapewniony udział - motywacja niższa, ale trener McCarthy chce pokazać się przeciw RPA. RPA (Mosimane) walczy o jedyne wolne miejsce w grupie.

**λ: Kenia 0,75 / RPA 1,30** (rynek ~0,7/1,35; 1 4.70, X 3.20, 2 1.76).

| Rynek | p | fair | kurs | uwagi |
|---|---|---|---|---|
| RPA wygra | 49,6% | 2.01 | 1.76 | brak value |
| X2 | 78,5% | 1.27 | 1.14 | EV -11% |
| 12 | 71,2% | 1.40 | 1.29 | EV -9% |
| Under 2.5 | 66,3% | 1.51 | 1.45 | EV -4% |
| Under 3.5 | 84,8% | 1.18 | 1.14 | EV -3% |
| Over 1.5 | 60,7% | 1.65 | 1.49 | EV -10% |
| BTTS nie | 61,6% | 1.62 | brak | |
| RPA strzeli >=1 | 72,7% | 1.38 | | |

Rożne/kartki: brak podstaw (Kenia 4,7 vs RPA 6,0 rożnych, kartki 1,0/1,0, n=3).
**Statystyki:** RPA: 5:0 Erytrea, 2:1 Gwinea, 1:0 Egipt, 2:2 Kenia (średnia 3,0 gole inflowana Erytreą). Kenia: 1:1 Erytrea, 0:1 Gwinea, 4:0 Lesotho (czerwiec).
**H2H:** 2:2 (13.11.2026); wcześniejsze mecze z 2011-12, bez wagi.
**Ryzyka:** RPA ma doświadczenie, ale u siebie Kenia broni dobrze; chłodna motywacja Kenii vs desperacja RPA; Williams/Mokoena niepewni w pierwszym meczu (EWN/Sportsmole).
**Pewność:** niska. Mecz bez mocnego typu.

---

## 3. Sierra Leone - DR Konga, 17:00 PL, ID 15752174
Eliminacje AFCON 2027 (rewanż, DR Konga 3:1 Sierra Leone 12.11). Mecz na Stade Larbi Zaouli (Casablanca - neutralny, Sierra Leone nie gra u siebie). Sędzia Jalal Jayed (Maroko).

**λ: SL 0,60 / DRK 1,70** (rynek ~0,6/1,7; 1 7.80, X 4.30, 2 1.36).

| Rynek | p | fair | kurs | uwagi |
|---|---|---|---|---|
| DR Konga wygra | 64,1% | 1.56 | 1.36 | rynek 67,1%, EV -13% |
| X2 | 87,3% | 1.15 | 1.04 | skrajnie krótki, pomijać |
| 12 | 76,8% | 1.30 | 1.16 | EV -10% |
| Under 3.5 | 79,9% | 1.25 | 1.22 | EV -3% |
| Under 2.5 | 59,6% | 1.68 | 1.63 | EV -3% |
| Over 1.5 | 66,9% | 1.49 | 1.36 | EV -9% |
| BTTS nie | 63,1% | 1.58 | brak | |
| DRK strzeli >=1 | 81,7% | 1.22 | | |
| DRK strzeli >=2 | 50,7% | 1.97 | | |

Rożne/kartki: brak podstaw (rożne SL 3,0 / DRK 2,7 z n=3 - niewiarygodne).
**Statystyki:** DRK: 2:0 Gwinea Rów., 2:1 Zimbabwe, 0:2 Uganda, 1:1 Uganda, 3:1 SL. SL: 2:3 Zimbabwe, 0:1 Gwinea Rów., 1:3 DRK (traci 2,3/mecz).
**H2H:** DRK wygrywa wszystkie ostatnie spotkania (3:1 12.11.2026).
**Ryzyka:** DRK mogło wykorzystać siły w pierwszym meczu (rotacja), strata punktów z Ugandą pokazuje, że nie jest bezbłędna; ryzyko remisu/porażki ok. 36% (remis 23% + SL 13%).
**Pewność:** średnia dla DRK jako faworyta; brak value względem kursów.

---

## 4. Libia - Tunezja, 17:00 PL, ID 15752175
Eliminacje AFCON 2027, grupa H (pierwszy mecz 13.11: Tunezja 0:2 Libia w Sfax, karny Ali Youssef + gol Hamdou El Houni). 11 June Stadium (Trypolis), sędzia Adissa Raphiou Ligali (Benin).
Przed pierwszym meczem: Uganda (współgospodarz, już zakwalifikowana) 4 pkt, Tunezja 2, Botswana 2, Libia 1. Tunezja po porażce w kryzysie (2 pkt, zagrożona seria 17 występów na AFCON, posada trenera Chaabaniego). Brak Elias Achouri (kontuzja). Libia gra z zawodnikami z lig krajowych (Dabo, 27 osób).

**λ: Libia 0,95 / Tunezja 1,15** (rynek ~0,95/1,15; 1 3.40, X 2.95, 2 2.17). Kryzys dotyczy faworyta (Tunezji) - zgodnie z regułą nie obniżam p za samą formę; uwzględniam jedynie brak Achouriego (w λ).

| Rynek | p | fair | kurs | uwagi |
|---|---|---|---|---|
| Tunezja wygra | 40,2% | 2.48 | 2.17 | rynek 42,1%, EV -12% |
| Remis | 29,8% | 3.36 | 2.95 | |
| Libia wygra | 30,0% | 3.33 | 3.40 | EV ~0 |
| 1X | 59,8% | 1.67 | 1.59 | EV -5% |
| X2 | 70,0% | 1.43 | 1.25 | EV -12% |
| 12 | 70,2% | 1.42 | 1.33 | EV -7% |
| Under 2.5 | 65,0% | 1.54 | 1.46 | EV -5% |
| Under 3.5 | 83,9% | 1.19 | 1.14 | EV -4% |
| Over 1.5 | 62,0% | 1.61 | 1.48 | EV -8% |
| BTTS nie | 58,1% | 1.72 | brak | |

Rożne/kartki: brak podstaw (Libia 5,3 vs Tunezja 8,0 rożnych; kartki 2,0/1,5; n=2-3).
**H2H:** Libia 2:0 (13.11.2026), wcześniej Tunezja 1:0 i 3:0 (2023), 5:2 (2021) - starsze mecze ważone nisko.
**Ryzyka:** bardzo wyrównany mecz, Tunezja musi wygrać (ryzyko wysokiej intensywności, ale też nerwów); Libia u siebie broni nisko. Mecz bez mocnego typu.
**Pewność:** niska.

---

## 5. Togo - Algieria, 17:00 PL, ID 15752176
Eliminacje AFCON 2027, grupa I (pierwszy mecz 14.11: Algieria 1:0 Togo, gol Bensebaini w 76. min, Tizi Ouzou). Stade de Kégué (Lomé), sędzia Pierre Jean Nguiene (Gabon).
Absencje Algierii: brak Aït-Nouri i kilku kluczowych graczy (Afrik-Foot, Mediaterranee), selekcjoner Hemdani; Togo (Neveu) ma kapitana z powrotem, kandydaci Denkey, Dakonam (lista, nie skład).

**λ: Togo 0,65 / Algieria 1,35** (rynek ~0,6/1,45; 1 5.00, X 3.40, 2 1.67). Korekta kadrowa Algierii (brak kilku graczy, 1 strona) uwzględniona w obniżeniu λ gości z ~1,45 do 1,35.

| Rynek | p | fair | kurs | uwagi |
|---|---|---|---|---|
| Algieria wygra | 53,8% | 1.86 | 1.67 | rynek 54,8%, EV -10% |
| Remis | 28,3% | 3.54 | 3.40 | |
| Togo wygra | 18,0% | 5.57 | 5.00 | |
| X2 | 82,0% | 1.22 | 1.12 | EV -8% |
| 12 | 71,7% | 1.39 | 1.26 | EV -10% |
| Under 2.5 | 67,7% | 1.48 | 1.52 | EV +3% (w granicach błędu) |
| Under 3.5 | 85,7% | 1.17 | 1.16 | EV ~-1% |
| Over 1.5 | 59,4% | 1.68 | 1.44 | EV -14% |
| BTTS nie | 64,6% | 1.55 | brak | |
| Algieria strzeli >=1 | 74,1% | 1.35 | | |

Rożne/kartki: brak podstaw (Togo 5,0 vs Algieria 5,3 rożnych; kartki 2,0/1,0, n=3).
**Statystyki:** Togo: 0:2 Zambia, 1:0 Burundi, 0:1 Algieria; 5:1 Benin i 1:1 RŚA (czerwiec); strzela tylko 0,3 w sezonie eliminacji. Algieria: 3:1 Zambia, 2:2 Burundi, 2:1 Niger, 1:0 Togo; strzela 2,0, traci 1,0.
**H2H:** Algieria wygrywa 6 z 7 (1:0 14.11.2026, 1:0 i 5:1 w 2024, 3:0 w 2024).
**Ryzyka:** Algieria bez kilku kluczowych graczy, Togo u siebie bywa zamknięte; ryzyko remisu ok. 28%, wygrana Togo 18%. Under 2.5 jedyny rynek z niewielką dodatnią EV (nie przekracza błędu modelu).
**Pewność:** średnia dla Algierii jako faworyta/Under 2.5, niska dla rynków dodatkowych.

---

## 6. Gwinea Bissau - Madagaskar, 17:00 PL, ID 15752177
Eliminacje AFCON 2027 (pierwszy mecz 12.11: Madagaskar 1:1 Gwinea Bissau). Estádio 24 de Setembro (Bissau). Sędzia nieznany (lista pusta w Superbet).

**λ: GB 1,70 / Madagaskar 0,55** (rynek ~1,75/0,6; 1 1.42, X 4.10, 2 6.70).

| Rynek | p | fair | kurs | uwagi |
|---|---|---|---|---|
| Gwinea Bissau wygra | 65,5% | 1.53 | 1.42 | rynek 64,2%, EV -7% |
| 1X | 88,5% | 1.13 | 1.06 | pomijać (fair <=1.15) |
| 12 | 77,0% | 1.30 | 1.18 | EV -9% |
| Under 3.5 | 80,9% | 1.24 | 1.23 | EV ~-1% |
| Under 2.5 | 60,9% | 1.64 | 1.65 | EV ~+0,5% |
| Over 1.5 | 65,7% | 1.52 | 1.35 | EV -11% |
| BTTS nie | 65,4% | 1.53 | brak | |
| GB strzeli >=1 | 81,7% | 1.22 | | |
| GB strzeli >=2 | 50,7% | 1.97 | ~1.7-1.9 w combo | |

Rożne/kartki: brak podstaw (GB 4,0 vs Mad. 2,3 rożnych; kartki 1,3/2,3; n=3; sędzia nieznany).
**Statystyki:** GB: 3:0 Nigeria (u siebie), 2:0 Tanzania (wyjazd), 1:1 Madagaskar; straciła 0,3/mecz, strzela 2,0; w marcu 5:0 i 1:1 z Burkina Faso. Madagaskar: 1:1 Tanzania, 1:2 Nigeria, 4:0 Maroko (porażka w sparingu), 1:1 GB; strzela 1,0, traci 1,3.
**H2H:** 1:1 (12.11.2026), brak wcześniejszych w bazie.
**Ryzyka:** wynik 1:1 w pierwszym meczu pokazuje, że Madagaskar potrafi się bronić; GB musi przełamać; remis 23% + Madagaskar 11,5%.
**Pewność:** średnia dla GB jako faworyta (wyraźnie najpewniejszy mecz z 6, ale kurs 1.42 bez value).

---

## Podsumowanie kandydatów (p >= 50% lub fair <= 2.0)
Brak typu z wyraźną dodatnią EV względem Superbet. Najlepsze (nadal bez value) wg p: GB wygra 65,5% (1.53), DRK wygra 64,1% (1.56), Under 2.5 w Togo-Algieria 67,7% (1.48, EV +3% = noise), BTTS nie ~58-65%. Wszystkie rynki rożne/kartki bez podstaw.

To są oszacowania probabilistyczne, nie gwarancje.
