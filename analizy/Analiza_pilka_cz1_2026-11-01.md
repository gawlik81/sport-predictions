# Analiza piłka nożna cz.1, 01.11.2026 (niedziela)

Mecze: Getafe - Sevilla, Racing Santander - Real Madrid, Liverpool - Arsenal, Elche - Valencia, Athletic Club - Real Sociedad (godziny polskie).
Źródła: Pinnacle (MCP sportsdata, kurs odniesienia po usunięciu marży), ESPN standings (MCP), Comuniate (bajas, sędziowie, forma dom/wyjazd), liverpoolfc.com i Sky Sports (Liverpool - Arsenal). Skrypty: `poisson.py`, `markets.py`. BettingPros: pominięte (brak klucza w sesji). Betclic: nie pobierano (ten plik to krok 2, bez EV).

Uwagi ogólne:
- Tabela ESPN bywa opóźniona (Liverpool 8 meczów, Arsenal 8), więc liczby sezonowe traktuj orientacyjnie.
- Rożne i kartki: jedyne źródło liczb to linie Pinnacle (rożne meczowe i "bookings" w punktach), brak niezależnego drugiego źródła i brak statystyk sędziów. Zgodnie z regułą SKILL.md: pewność niska, bez rekomendacji na kupon.
- Faule meczowe i rynki zawodnika: niewycenione (brak danych o średnich i brak potwierdzonych składów).
- Sygnały ryzyka zmieniły liczby (λ), opis przy każdym meczu.

---

### Getafe - Sevilla (LaLiga, J11, 01.11 14:00, Coliseum; sędzia García Verdura)
**Typ:** brak mocnego typu wynikowego; najlepszy rynek: Under 3.5 (82,9%, fair 1.21) | **Pewność:** średnia

λ Getafe 0,90 / Sevilla 1,25 (suma 2,15). Rynek Pinnacle: 1X2 devig 28,4 / 31,5 / 40,1%, O2.5 ok. 37%.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| Getafe | 26,7% | 3.75 | średnia |
| Remis | 28,9% | 3.46 | średnia |
| Sevilla | 44,4% | 2.25 | średnia (rynek 40,1%) |
| 1X | 55,6% | 1.80 | średnia |
| X2 | 73,3% | 1.36 | średnia |
| 12 | 71,1% | 1.41 | średnia |
| Over 1.5 | 63,3% | 1.58 | średnia |
| Under 1.5 | 36,7% | 2.73 | średnia |
| Over 2.5 | 36,4% | 2.75 | średnia |
| Under 2.5 | 63,6% | 1.57 | średnia |
| Over 3.5 | 17,1% | 5.85 | średnia |
| Under 3.5 | 82,9% | 1.21 | średnia |
| BTTS tak | 42,3% | 2.36 | średnia |
| BTTS nie | 57,7% | 1.73 | średnia |
| Rożne (średnia ok. 8,8; linia Pin 8.5) O/U 8.5 | 50,6% / 49,4% | 1.98 / 2.02 | niska |
| Rożne Over 7.5 / Under 9.5 | 62,8% / 61,2% | 1.59 / 1.64 | niska |
| Kartki: Pinnacle "bookings" 5.5 pkt (tt 2.5/2.5), średnia ok. 5,0 | Over 3.5 69,3% / Over 4.5 53,4% | 1.44 / 1.87 | niska (sędzia bez statystyk) |

Faule, rynki zawodnika: niewycenione.

**Statystyki drużyn:** Getafe 18. (9 pkt, 5 GF / 15 GA w 10 meczach), u siebie 2W-3D-0L, 5:3 (ESPN/Comuniate). Sevilla 6. (17 pkt, 16:16), na wyjeździe 2W-2D-1L, 9:9.
**H2H:** ostatni mecz 22.02.2026 Getafe 0-1 Sevilla (Comuniate).
**Informacje medialne:** Getafe bez Mojici (5 żółtych) i Mario Martína (czerwona), Zaid Romero kontuzja (duże ryzyko absencji, w tekście sprzeczne wskazówki), Uche (więzadła) do kwietnia, Juanmi niepewny. Sevilla bez Marcão i Miguela Sierry. Osłabiona obrona Getafe podniosła λ Sevilli (1,25).
**Ryzyka:** Getafe broni się nisko i ma najgorszy atak w lidze (zamyka mecz, remis/Under); z drugiej strony Sevilla w tabeli wyżej, ale wyjazdowa średnia 1 gol na mecz. Wygrana Getafe 26,7% (rynek 28,4%).
**Rynek:** Pinnacle 1X2 3.43 / 3.10 / 2.43, total 2.0 (-110/-100), O2.5 2.59, U2.5 1.535; różnica z modelem < 5 pp.

---

### Racing Santander - Real Madrid (LaLiga, J11, 01.11 16:15, El Sardinero; sędzia Munuera Montero)
**Typ:** Real Madrid wygra 74,9% (fair 1.34), alternatywnie Over 1.5 (85,9%, fair 1.16, granica) | **Pewność:** średnia

λ Racing 0,85 / Real 2,60 (suma 3,45). Rynek Pinnacle: devig 8,4 / 11,9 / 79,6%, total 4.0 (50/50), tt Real 2.5 over -179. Mój p Realu jest o 4,7 pp pod rynkiem: powód to konkretny sygnał (rotacja przed Ligą Mistrzów za 3 dni wg Starting11, Vinícius zawieszony J9-12, Valverde wątpliwy, Mendy/Asencio/Rodrygo kontuzjowani).

| Rynek | p | fair | Pewność |
|---|---|---|---|
| Racing | 9,9% | 10.06 | średnia |
| Remis | 15,2% | 6.59 | średnia |
| Real Madrid | 74,9% | 1.34 | średnia (rynek 79,6%) |
| 1X | 25,1% | 3.98 | średnia |
| X2 | 90,1% | 1.11 | średnia (fair <= 1.15, pomijać w rankingach) |
| 12 | 84,8% | 1.18 | średnia |
| Over 1.5 | 85,9% | 1.16 | średnia (granica 1.15-1.20) |
| Under 1.5 | 14,1% | 7.08 | średnia |
| Over 2.5 | 67,0% | 1.49 | średnia |
| Under 2.5 | 33,0% | 3.03 | średnia |
| Over 3.5 | 45,2% | 2.21 | średnia |
| Under 3.5 | 54,8% | 1.83 | średnia |
| BTTS tak | 53,0% | 1.89 | średnia |
| BTTS nie | 47,0% | 2.13 | średnia |
| Rożne (średnia ok. 11,1; linia Pin 11.0, tt Real 6.5, Racing 3.5) O/U 10.5 | 53,8% / 46,2% | 1.86 / 2.16 | niska |
| Rożne Over 9.5 | 64,6% | 1.55 | niska |
| Kartki: Pinnacle "bookings" 4.0 pkt, średnia ok. 4,0 (Munuera, brak statystyk) | Over 3.5 53,8% / Over 4.5 37,0% | 1.86 / 2.70 | niska |

Faule, rynki zawodnika: niewycenione (skład Realu niepewny przez rotację).

**Statystyki drużyn:** Racing 15. (11 pkt, 15:26 w 10 meczach), u siebie 3W-2D-0L, 11:8 (średnio 3,8 gola na mecz w Sardinero). Real 3. (24 pkt, 25:10), na wyjeździe 3W-0D-2L, 8:7 (Comuniate/ESPN).
**H2H:** brak istotnych ostatnich meczów (Racing świeży beniaminek).
**Informacje medialne:** Racing bez Andrésa Martína (uraz) i Salinasa (5 żółtych). Real: Vinícius zawieszony, Valverde wątpliwy, Mendy do grudnia, Asencio do stycznia, Rodrygo do grudnia. Starting11 sygnalizuje rotację przed meczem LM.
**Ryzyka:** dwie twarze: remis (15%) i wygrana Racingu (10%) wzmocnione rotacją Realu i dobrą formą Racingu u siebie (bez porażki w 5 meczach); wyniki wyjazdowe Realu 2 porażki w 5.
**Rynek:** Pinnacle 1X2 11.48 / 8.11 / 1.215 (ML), O/U 4.0 po -106. Brak kursów Betclic w tej analizie.

---

### Liverpool - Arsenal (Premier League, 01.11 17:30, Anfield)
**Typ:** brak mocnego typu (mecz wyrównany); najlepszy rynek: Under 3.5 (75,8%, fair 1.32) | **Pewność:** średnia

λ Liverpool 1,28 / Arsenal 1,22 (suma 2,50). Rynek Pinnacle: devig 34,2 / 28,5 / 37,3% (Arsenal minimalnym faworytem mimo Anfield), O2.5 51,6%, O1.5 ok. 76%. Mój O2.5 (45,6%) jest 6 pp pod rynkiem: obniżenie uzasadnione brakiem Saki i najlepszą obroną ligi po stronie Arsenalu (5 straconych w 8), ale podniosłem λ względem pierwszej wersji (2,40 -> 2,50), żeby nie schodzić zbyt głęboko pod rynek.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| Liverpool | 37,9% | 2.64 | niska-średnia |
| Remis | 27,0% | 3.71 | średnia |
| Arsenal | 35,1% | 2.85 | niska-średnia |
| 1X | 64,9% | 1.54 | średnia |
| X2 | 62,1% | 1.61 | średnia |
| 12 | 73,0% | 1.37 | średnia |
| Over 1.5 | 71,3% | 1.40 | średnia |
| Under 1.5 | 28,7% | 3.48 | średnia |
| Over 2.5 | 45,6% | 2.19 | średnia |
| Under 2.5 | 54,4% | 1.84 | średnia |
| Over 3.5 | 24,2% | 4.13 | średnia |
| Under 3.5 | 75,8% | 1.32 | średnia |
| BTTS tak | 50,9% | 1.97 | średnia |
| BTTS nie | 49,1% | 2.04 | średnia |
| Rożne (średnia ok. 9,7; linia Pin 9.5 po -102/-116) O/U 9.5 | 49,4% / 50,6% | 2.02 / 1.98 | niska |
| Rożne Over 8.5 / Under 10.5 | 61,0% / 61,7% | 1.64 / 1.62 | niska |
| Kartki: Pinnacle "bookings" 4.0 pkt (Over -136), średnia ok. 4,3; Sky: mecz "foul-heavy" | Over 3.5 58,8% / Over 4.5 42,0% | 1.70 / 2.38 | niska (sędzia nieznany) |

Faule, rynki zawodnika: niewycenione (Szoboszlai i Muñoz niepewni, Tzolis/Madueke do potwierdzenia; typ warunkowy nie może być wariantem głównym).

**Statystyki drużyn:** Liverpool 5. (15 pkt, 11:8 w 8 meczach), 5 meczów bez porażki we wszystkich rozgrywkach (w tym karne z Chelsea w Carabao Cup). Arsenal 2. (21 pkt, 13:5), po wpadce z Fleetwood w Carabao Cup (Sky/ESPN).
**H2H:** poprzedni sezon: Liverpool 1-0 u siebie, 0-0 na Emirates (Sky Sports). Oba mecze to Under 2.5.
**Informacje medialne:** trener Liverpoolu Andoni Iraola (wg liverpoolfc.com, 30.10): Frimpong, Bradley, Ekitike, Leoni out; Szoboszlai i Muñoz "mają szansę"; Jacquet wątpliwy. Arsenal: Saka out (udo/czworogłowy), Dowman zawieszony 3 mecze, Calafiori, Rice i Tzolis trenują i powinni grać, Madueke do oceny. Sky typuje 1-1, NBC 2-1 dla Liverpoolu.
**Ryzyka:** faworyt nieoczywisty: remis 27% i obie wygrane po ok. 35-38%; niepewny skład ofensywny Liverpoolu (Szoboszlai), brak Saki ogranicza Arsenal, ale jego defensywa jest najmocniejsza w lidze.
**Rynek:** Pinnacle 1X2 2.85 / 3.43 / 2.61, O/U 2.5 1.89 / 2.02, O1.5 1.27, U1.5 4.01, O3.5 3.15, U3.5 1.39.

---

### Elche - Valencia (LaLiga, J11, 01.11 18:30, Martínez Valero; sędzia Bestard Servera)
**Typ:** brak mocnego typu; najlepszy rynek: Under 3.5 (75,8%, fair 1.32) | **Pewność:** średnia

λ Elche 1,35 / Valencia 1,15 (suma 2,50). Rynek Pinnacle: devig 40,8 / 28,9 / 30,4%, O2.5 48,8%, O1.5 ok. 74%. Pierwotne λ (1,30/1,05) podniosłem, bo O2.5 byłoby 7 pp pod rynkiem bez konkretnej informacji kadrowej po stronie ataków; wśród kontuzji Valencii są obrońcy i napastnik Sadiq (wątpliwy), więc korekta ataku w dół Valencii zostaje, ale mała.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| Elche | 41,3% | 2.42 | średnia |
| Remis | 26,8% | 3.73 | średnia |
| Valencia | 31,8% | 3.14 | średnia |
| 1X | 68,1% | 1.47 | średnia |
| X2 | 58,6% | 1.71 | średnia |
| 12 | 73,2% | 1.37 | średnia |
| Over 1.5 | 71,3% | 1.40 | średnia |
| Under 1.5 | 28,7% | 3.48 | średnia |
| Over 2.5 | 45,6% | 2.19 | średnia |
| Under 2.5 | 54,4% | 1.84 | średnia |
| Over 3.5 | 24,2% | 4.13 | średnia |
| Under 3.5 | 75,8% | 1.32 | średnia |
| BTTS tak | 50,6% | 1.98 | średnia |
| BTTS nie | 49,4% | 2.03 | średnia |
| Rożne (średnia ok. 9,2; linia Pin 9.0, tt Elche 5.5, Valencia 3.5) O/U 9.5 | 43,6% / 56,4% | 2.30 / 1.77 | niska |
| Rożne Over 8.5 / Under 10.5 | 55,3% / 67,2% | 1.81 / 1.49 | niska |
| Kartki: Pinnacle "bookings" 5.0 pkt (Over -120), średnia ok. 4,8 (Bestard bez statystyk) | Over 3.5 66,5% / Over 4.5 50,2% | 1.50 / 1.99 | niska |

Faule, rynki zawodnika: niewycenione.

**Statystyki drużyn:** Elche 16. (10 pkt, 14:17 w 10 meczach), u siebie 0W-1D-3L, 4:11. Valencia 19. (6 pkt, 7:17), na wyjeździe 1W-1D-2L, 4:6 (Comuniate/ESPN).
**H2H:** ostatnia wizyta Valencii (sezon 25/26) wygrana przez Elche 1-0.
**Informacje medialne:** Elche bez Marca Aguado (kostka), Bigas wątpliwy. Valencia: kontuzjowani Van Oevelen, Foulquier (sprzeczne dane), Diego López, Canós, Otorbi; Sadiq wątpliwy; Harvey Elliott zawieszony (2 żółte wg Comuniate).
**Ryzyka:** oba kluby w dole tabeli, mecz walki o punkty: remis 27%; Elche słabe u siebie (żadnej wygranej w 4 meczach, 11 straconych), więc "gospodarz faworytem" wynika głównie z jakości Valencii, która ma najgorszy atak w lidze po Getafe.
**Rynek:** Pinnacle 1X2 2.39 / 3.38 / 3.21, O/U 2.5 2.00 / 1.91, O1.5 1.305, O3.5 3.41.

---

### Athletic Club - Real Sociedad (LaLiga, J11, 01.11 21:00, San Mamés; sędzia Alejandro Hernández)
**Typ:** brak mocnego typu wynikowego; najlepszy rynek: Over 1.5 (74,2%, fair 1.35) | **Pewność:** średnia

λ Athletic 1,50 / Real Sociedad 1,15 (suma 2,65). Rynek Pinnacle: devig 46,4 / 27,2 / 26,4%, total 2.75 (Over 2.11 / Under 1.82), O2.5 ok. 52%.

| Rynek | p | fair | Pewność |
|---|---|---|---|
| Athletic | 45,3% | 2.21 | średnia |
| Remis | 25,6% | 3.90 | średnia |
| Real Sociedad | 29,1% | 3.44 | średnia |
| 1X | 70,9% | 1.41 | średnia |
| X2 | 54,7% | 1.83 | średnia |
| 12 | 74,4% | 1.34 | średnia |
| Over 1.5 | 74,2% | 1.35 | średnia |
| Under 1.5 | 25,8% | 3.88 | średnia |
| Over 2.5 | 49,4% | 2.02 | średnia |
| Under 2.5 | 50,6% | 1.98 | średnia |
| Over 3.5 | 27,5% | 3.64 | średnia |
| Under 3.5 | 72,5% | 1.38 | średnia |
| BTTS tak | 53,1% | 1.88 | średnia |
| BTTS nie | 46,9% | 2.13 | średnia |
| Rożne (średnia ok. 10,0; linia Pin 10.0, tt Athletic 5.5, RS 3.5) O/U 9.5 | 52,8% / 47,2% | 1.89 / 2.12 | niska |
| Rożne Over 8.5 / Under 10.5 | 64,2% / 58,4% | 1.56 / 1.71 | niska |
| Kartki: Pinnacle "bookings" 6.0 pkt (derby, 50/50), średnia ok. 5,4 | Over 3.5 74,3% / Over 4.5 59,4% / Over 5.5 44,3% | 1.35 / 1.68 / 2.26 | niska (Hernández bez statystyk) |

Faule, rynki zawodnika: niewycenione.

**Statystyki drużyn:** Athletic 7. (12 pkt, 12:9 w 9 meczach), u siebie 2W-2D-1L, 9:4. Real Sociedad 5. (19 pkt, 19:18), na wyjeździe 3W-0D-2L, 12:11 (Comuniate/ESPN).
**H2H:** 01.02.2026 Athletic 1-1 Real Sociedad; wcześniej RS 3-2 u siebie (11.2025); w Pucharze Króla 2026 dwumecz półfinałowy (wynik nieweryfikowany).
**Informacje medialne:** Athletic bez Egiluza (więzadła), Ruiza de Galarrety (do połowy listopada), Guruzety (więzadła, do czerwca); Sancet wątpliwy (łydka). Real Sociedad: Odriozola out, Zakharyan out, Beitia wątpliwy; Comuniate wymienia też Oyarzabala i Guedesa wśród kontuzjowanych w kadrze (niepotwierdzone, informacja z listy kadry bez daty; jeśli się potwierdzi, λ RS spadnie do ok. 1,0, a p Athleticu wzrośnie o ok. 3 pp).
**Ryzyka:** derby (remis 26%), podwójna twarz: wygrana RS 29%; Athletic ma wąski środek pola i atak (Guruzeta out).
**Rynek:** Pinnacle 1X2 2.10 / 3.58 / 3.70, O2.5 1.87 / 2.02, O/U 2.75 2.11 / 1.82.

---

## Ranking kandydatów (fair odds > 1.15)

| # | Mecz | Rynek | p | fair | Pewność | Od czego zależy | Kurs rynkowy |
|---|---|---|---|---|---|---|---|
| 1 | Racing - Real Madrid | Real Madrid wygra | 74,9% | 1.34 | średnia | skład Realu (rotacja przed LM, Valverde) | Pinnacle 1.215 (rynek 79,6%); Betclic nieznany |
| 2 | Racing - Real Madrid | Over 1.5 | 85,9% | 1.16 | średnia (granica) | rotacja, skład | Pinnacle nieznany dla 1.5 |
| 3 | Getafe - Sevilla | Under 3.5 | 82,9% | 1.21 | średnia | Zaid Romero, początek meczu | Betclic nieznany |
| 4 | Liverpool - Arsenal | Under 3.5 | 75,8% | 1.32 | średnia | Szoboszlai, Madueke, Tzolis | Pinnacle U3.5 1.39 (ok. 71,8% devig; EV modelu +) |
| 5 | Elche - Valencia | Under 3.5 | 75,8% | 1.32 | średnia | Sadiq, Aguado | Pinnacle U3.5 1.346 |
| 6 | Athletic - Real Sociedad | Over 1.5 | 74,2% | 1.35 | średnia | Sancet, Oyarzabal (niepotw.) | Pinnacle nieznany |
| 7 | Getafe - Sevilla | X2 | 73,3% | 1.36 | średnia | skład obrony Getafe | Betclic nieznany |
| 8 | Racing - Real Madrid | Over 2.5 | 67,0% | 1.49 | średnia | rotacja | Pinnacle (O3.5 ok. 60%) |

Pominięte (fair <= 1.15): Racing - Real Madrid X2 (1.11). Rożne i kartki: niska pewność (jedno źródło), nie rekomendowane na kupon.

Przypomnienie: to oszacowania probabilistyczne, nie gwarancje wyniku.
