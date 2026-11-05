# Analiza piłkarska - Liga Mistrzów, 4. kolejka fazy ligowej, 03.11.2026

Gospodarze wg ESPN (sportsdata MCP) i korekty koordynatora: Galatasaray, Szachtar, Atlético, Barcelona, Bodø/Glimt, Feyenoord, LASK, Manchester United, Villarreal. Godziny polskie: 18:45 (Galatasaray, Szachtar), 21:00 (reszta).

## Jakość danych (ważne)
- Źródła: ESPN standings/scoreboard (tabela fazy ligowej po 3 kolejkach, MCP sportsdata), kickoff.co.uk (średnie goli, λ modelu serwisu, kursy Bet365; strony Galatasaray, Barcelona, Atlético, Bodø, Feyenoord), WebSearch, kursy Betclic od koordynatora (tylko kontrola, p liczone własnym modelem Poissona `poisson.py`).
- BRAK: potwierdzonych kontuzji/zawieszeń, przewidywanych składów, sędziów (nie ogłoszeni lub nie do znalezienia), xG, statystyk rożnych i kartek drużyn. Szukanie w sieci nie zwróciło aktualnych previewów (squawka 403, reszta stare sezony).
- Skutek: λ z tabeli (gole za/przeciw po 3 meczach, mała próba), średniej ligowej i kontroli z rynkiem (żadne p nie odbiega od rynku bez marży o >5 pp po korekcie). Rożne i kartki = średnie ligowe LM z lekką korektą stylu; sędzia nieznany, więc pewność maks. niska/średnia. Rynki zawodnika POMINIĘTE (brak potwierdzonych składów, reguła ze SKILL.md).
- Tabela po 3 kolejkach: PSG 9 pkt, Aston Villa 9, Stuttgart 7, Barcelona 6 (11-6), Sporting 6, Bayern 5 (10-5), Roma 4, Atlético 4, Szachtar 4, Villarreal 3 (8-8), Inter 3, Man Utd 3, Galatasaray 3 (6-9), LASK 3 (6-9), Feyenoord 3 (4-8), Bodø 3 (4-9), Lille 0 (4-10), Slovan 0 (1-13).

## Zbiorcza tabela (p / fair)

| Mecz (gosp - gość) | λ gosp/gość | 1 | X | 2 | 1X | X2 | 12 | O1.5 | O2.5 | O3.5 | BTTS tak | Rożne (śr.) | Kartki (śr.) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galatasaray - Stuttgart | 1,70/1,40 | 44,7% (2,24) | 23,6% (4,24) | 31,7% (3,15) | 68,3% (1,46) | 55,3% (1,81) | 76,4% (1,31) | 81,5% (1,23) | 59,9% (1,67) | 37,5% (2,67) | 61,6% (1,62) | 10,0 | 4,8 |
| Szachtar - Sporting | 1,00/1,45 | 26,0% (3,84) | 26,5% (3,78) | 47,5% (2,11) | 52,5% (1,90) | 74,0% (1,35) | 73,5% (1,36) | 70,2% (1,42) | 44,3% (2,26) | 23,2% (4,31) | 48,4% (2,07) | 9,4 | 4,3 |
| Atlético - Bayern | 1,50/1,65 | 35,0% (2,86) | 23,6% (4,24) | 41,4% (2,41) | 58,6% (1,71) | 65,0% (1,54) | 76,4% (1,31) | 82,2% (1,22) | 61,0% (1,64) | 38,6% (2,59) | 62,8% (1,59) | 9,6 | 4,6 |
| Barcelona - Aston Villa | 2,55/0,95 | 72,0% (1,39) | 16,2% (6,19) | 11,9% (8,41) | 88,2% (1,13) | 28,1% (3,56) | 83,9% (1,19) | 86,4% (1,16) | 67,9% (1,47) | 46,3% (2,16) | 56,5% (1,77) | 10,8 | 3,8 |
| Bodø/Glimt - Lille | 2,00/1,20 | 55,9% (1,79) | 21,6% (4,64) | 22,5% (4,44) | 77,5% (1,29) | 44,1% (2,27) | 78,4% (1,28) | 82,9% (1,21) | 62,0% (1,61) | 39,7% (2,52) | 60,4% (1,65) | 9,8 | 3,6 |
| Feyenoord - Inter | 1,25/1,75 | 27,4% (3,65) | 23,5% (4,26) | 49,1% (2,03) | 50,9% (1,96) | 72,6% (1,38) | 76,5% (1,31) | 80,1% (1,25) | 57,7% (1,73) | 35,3% (2,83) | 59,0% (1,70) | 9,6 | 4,4 |
| LASK - Slovan | 2,30/0,75 | 72,3% (1,38) | 17,2% (5,82) | 10,5% (9,50) | 89,5% (1,12) | 27,7% (3,61) | 82,8% (1,21) | 80,8% (1,24) | 58,8% (1,70) | 36,4% (2,75) | 47,5% (2,11) | 10,4 | 4,0 |
| Man Utd - Roma | 1,50/1,20 | 44,1% (2,27) | 25,5% (3,92) | 30,4% (3,29) | 69,6% (1,44) | 55,9% (1,79) | 74,5% (1,34) | 75,1% (1,33) | 50,6% (1,97) | 28,6% (3,50) | 54,3% (1,84) | 9,8 | 4,8 |
| Villarreal - PSG | 1,25/1,95 | 24,3% (4,11) | 22,0% (4,55) | 53,7% (1,86) | 46,3% (2,16) | 75,7% (1,32) | 78,0% (1,28) | 82,9% (1,21) | 62,0% (1,61) | 39,7% (2,52) | 61,2% (1,63) | 9,8 | 3,6 |

Linie rożnych/kartek: patrz sekcje meczów. Under = 1 - Over, fair wg skryptu.

---

### Galatasaray - VfB Stuttgart (RAMS Park, 18:45)
**Typ:** Over 1.5 gola (81,5%, fair 1,23) lub Galatasaray/remis nie; wynik 1X2 bez mocnego typu | **Pewność:** niska-średnia
**Rynki:** 1X2 44,7/23,6/31,7; 1X 68,3% (1,46); X2 55,3%; Over 2.5 59,9% (1,67); Under 2.5 40,1% (2,49); Over 3.5 37,5%; BTTS 61,6% (1,62). Rożne śr. 10,0: O 9.5 52,8% (1,89), O 10.5 41,6% (2,40), U 10.5 58,4%. Kartki śr. 4,8 (Stambuł, atmosfera; sędzia nieznany): O 3.5 66,5% (1,50), O 4.5 50,2% (1,99), O 5.5 35,2%.
**Statystyki:** Gala po 3 kolejkach 6-9 (słaba defensywa), Stuttgart 7-2 (najlepsza obrona fazy, 7 pkt). KickOff model: 2,0/1,7. Moje λ niżej (Stuttgart dobra obrona, wyjazd).
**H2H:** brak bezpośrednich meczów (pierwsze starcie w LM).
**Informacje medialne:** brak potwierdzonych kadr; jedna strona sugeruje kontuzję bramkarza Güvenç (niepotwierdzone).
**Ryzyka:** remis i wygrana gości w podobnej wadze (23,6% / 31,7%). Obrona Stuttgartu (2 stracone w 3 meczach) może obniżyć gole.
**Rynek:** Betclic 2,07/3,98/2,97 (po marży ok. 45/23/32, zgodne). Bet365 O2.5 1,36 (to 74%, rynek wyżej niż mój 60% - ostrożnie, to Bet365 z kickoff.co.uk i może być stary).

### Szachtar Donieck - Sporting CP (18:45)
**Typ:** Sporting lub remis (X2) 74,0% (1,35) | **Pewność:** niska-średnia
**Rynki:** 1X2 26,0/26,5/47,5; Under 3.5 76,8% (1,30); Under 2.5 55,7% (1,80); O1.5 70,2%; BTTS 48,4% (tak 2,07; nie 1,94). Rożne śr. 9,4: O 9.5 45,9% (2,18), U 9.5 54,1% (1,85), O 8.5 57,7%. Kartki śr. 4,3: O 3.5 58,8% (1,70), O 4.5 42,0%.
**Statystyki:** Szachtar 4-3 (1-1 z PSV, 3-1 z AEK, 0-1 z Interem), Sporting 7-4 (3-1 Galatasaray, 2-0 Lens, 2-3 LASK). Squawka: 38% Szachtar, 27% remis, 35% Sporting, 1-0.
**H2H:** brak danych.
**Informacje medialne:** brak składów i absencji. Sporting zagrał 2-3 u siebie z LASK (słabsza defensywa).
**Ryzyka:** niski total, remis ok. 26,5%, Szachtar u siebie (neutralne/zastępcze boisko, wartość własnego boiska ograniczona).
**Rynek:** Betclic 3,58/3,70/1,92 (po marży ok. 26/25/49) - zgodne.

### Atlético Madryt - Bayern Monachium (Metropolitano, 21:00)
**Typ:** Over 1.5 gola (82,2%, fair 1,22, graniczny 1,15-1,25) / BTTS tak 62,8% (1,59) | **Pewność:** średnia
**Rynki:** 1X2 35,0/23,6/41,4; 1X 58,6%; X2 65,0% (1,54); 12 76,4%; O2.5 61,0% (1,64); O3.5 38,6%; U3.5 61,4% (1,63). Rożne śr. 9,6: O 9.5 48,2% (2,07), U 9.5 51,8% (1,93). Kartki śr. 4,6 (Atlético faulowe, Bayern pressing): O 3.5 63,5% (1,57), O 4.5 47,0% (2,13).
**Statystyki:** Bayern 10-5 w 3 meczach (5 pkt), Atlético 4-3 (4 pkt, 16. miejsce). KickOff: Atl 1,7 / Bay 1,9; Bet365 2,70/4,00/2,30.
**H2H:** ostatnie starcia z 2020 i wcześniej (inne składy), niska waga.
**Informacje medialne:** brak aktualnych absencji Bayernu/Atlético (nie znalazłem).
**Ryzyka:** mecz zamknięty w stylu Simeone (Under 2.5 39%), remis; gospodarz u siebie przy 4 pkt w stawce.
**Rynek:** Betclic 2,65/3,88/2,30 (po marży 35,3/24,1/40,7) - zgodne w ±1 pp po korekcie.

### FC Barcelona - Aston Villa (Camp Nou, 21:00)
**Typ:** Barcelona do wygrania lub remis (1X) 88,2% (1,13, graniczny 1,10-1,15) / Over 1.5 86,4% (1,16, graniczny) / Barcelona wygrana 72,0% (1,39) | **Pewność:** średnia
**Rynki:** 1X2 72,0/16,2/11,9; O2.5 67,9% (1,47); O3.5 46,3% (2,16); BTTS tak 56,5% (1,77); BTTS nie 43,5% (2,30). Rożne śr. 10,8 (dominacja Barcelony): O 9.5 61,5% (1,63), O 10.5 50,5% (1,98), O 11.5 39,9%. Kartki śr. 3,8: O 2.5 68,7% (1,46), O 3.5 50,2%, U 4.5 66,4% (1,51).
**Statystyki:** Barça 11-6 w 3 meczach (5-1 Feyenoord, 4-1 Galatasaray, 2-4 PSG); Villa 3/3 wygrane, 12-3 (najlepsza obrona), 5 wygranych z rzędu w Europie. KickOff: Barça 3,2 gola, Villa 1,1.
**H2H:** brak danych o niedawnym H2H.
**Informacje medialne:** liga 3 dni wcześniej (rotacja możliwa), brak potwierdzonych absencji. Villa bez porażki w LM: korekta obrony Barçy (6 straconych w 3 meczach) - ryzyko BTTS.
**Ryzyka:** remis 16% i wygrana Villi 12% (obrona Barçy straciła 4 z PSG); wysoka linia Barçy może zostać skorygowana przez rotację.
**Rynek:** Betclic 1,26/6,75/7,75 (po marży 74/14/12) - zgodne.

### Bodø/Glimt - Lille (Aspmyra, 21:00)
**Typ:** Bodø/Glimt wygra lub remis (1X) 77,5% (1,29) / Bodø wygrana 55,9% (1,79) | **Pewność:** średnia
**Rynki:** 1X2 55,9/21,6/22,5; O2.5 62,0% (1,61); O3.5 39,7%; BTTS tak 60,4% (1,65). Rożne śr. 9,8: O 9.5 50,6% (1,98), O 10.5 39,4%. Kartki śr. 3,6: O 2.5 65,5% (1,53), O 3.5 46,5% (2,15).
**Statystyki:** Bodø 4-9 w LM (4-3 porażka w Napoli), ale 18/20 meczów domowych Over 1.5, gole strzelane w 16 kolejnych meczach LM; Lille 0 pkt, 4-10, 3 porażki (2-4 Gala, 0-3 Arsenal, 2-3 Betis), traci 2+ gole w 4 ostatnich meczach LM. Lille na wyjeździe średnio 0,9 gola.
**H2H:** brak.
**Informacje medialne:** Aspmyra to sztuczna murawa i chłodny klimat (w listopadzie) - korzyść Bodø; lineups niepotwierdzone. Lille w kryzysie, zmęczenie podróżą.
**Ryzyka:** underdog w kryzysie (korekta dla Lille), ale Bodø słaba defensywa (9 straconych w 3) - BTTS i remis możliwe.
**Rynek:** Betclic 1,72/4,05/4,15 (po marży 54/23/23) - zgodne.

### Feyenoord - Inter Mediolan (De Kuip, 21:00)
**Typ:** Inter lub remis (X2) 72,6% (1,38) | **Pewność:** średnia-niska
**Rynki:** 1X2 27,4/23,5/49,1; Over 1.5 80,1% (1,25); O2.5 57,7% (1,73); O3.5 35,3%; BTTS tak 59,0% (1,70). Rożne śr. 9,6: O 9.5 48,2% (2,07), U 10.5 62,8%. Kartki śr. 4,4: O 3.5 60,4% (1,65), O 4.5 43,7%.
**Statystyki:** Inter 5-6 w 3 meczach (3 pkt; wygrana 1-0 nad Szachtarem wg squawka); Feyenoord 4-8, forma ligowa Feyenoordu słaba (7W/12L ostatnich 20). KickOff: Feyenoord 1,5 / Inter 2,1.
**H2H:** poprzednie starcia 2025 (Inter wygrywał), inne składy.
**Informacje medialne:** brak potwierdzonych kadr.
**Ryzyka:** Inter ma słabą formę wyjazdową (1,4 gola/mecz), remis lub porażka (Feyenoord u siebie).
**Rynek:** Betclic 3,40/4,00/1,90 (po marży 27,5/23,4/49,2) - zgodne.

### LASK - Slovan Bratysława (Raiffeisen Arena, 21:00)
**Typ:** LASK wygra 72,3% (1,38) / LASK lub remis 89,5% (1,12, poniżej progu 1,15) / Over 1.5 80,8% (1,24) | **Pewność:** średnia
**Rynki:** 1X2 72,3/17,2/10,5; O2.5 58,8% (1,70); O3.5 36,4%; BTTS tak 47,5% (2,11); BTTS nie 52,5% (1,90). Rożne śr. 10,4: O 9.5 57,3% (1,75), O 10.5 46,1%. Kartki śr. 4,0: O 3.5 53,8%, U 4.5 63,0%.
**Statystyki:** LASK 6-9 (3 pkt, wygrana 3-2 nad Sportingiem), Slovan 1-13 (0 pkt, 1-6 z Villarreal), najsłabszy atak i obrona fazy ligowej. Squawka: 68% LASK.
**H2H:** brak.
**Informacje medialne:** brak absencji; Slovan już praktycznie odpadł z walki o awans (motywacja niska).
**Ryzyka:** LASK ma wysoką wariancję (stracił 9 w 3 meczach); BTTS 47,5% to realny scenariusz; wygrana Slovana to 10,5%.
**Rynek:** Betclic 1,33/5,60/7,00 (po marży 70/17/13). Mój model +2 pp względem rynku po korekcie λ (obcięte z 2,55 do 2,30 dla zgodności).

### Manchester United - AS Roma (Old Trafford, 21:00)
**Typ:** brak mocnego typu na wynik; najlepsze rynki: Under 3.5 71,4% (1,40) / Over 1.5 75,1% (1,33) | **Pewność:** niska
**Rynki:** 1X2 44,1/25,5/30,4; 1X 69,6% (1,44); X2 55,9%; O2.5 50,6% (1,97); U2.5 49,4% (2,03); BTTS tak 54,3% (1,84). Rożne śr. 9,8: O 9.5 50,6% (1,98), O 10.5 39,4%. Kartki śr. 4,8 (Roma: kartkowa drużyna, sędzia nieznany): O 3.5 66,5% (1,50), O 4.5 50,2% (1,99).
**Statystyki:** United 5-6 w 3 meczach (3 pkt), Roma 8-5 (4 pkt, 15. miejsce).
**H2H:** ostatnie starcie w Europa League 2021 (inne składy), niska waga.
**Informacje medialne:** nie znalazłem aktualnych absencji.
**Ryzyka:** wyrównany mecz, wyniki zbliżone (remis 25,5%, wygrana gości 30,4%).
**Rynek:** Betclic 2,17/3,88/2,85 (po marży 43/24/33) - zgodne.

### Villarreal - Paris Saint-Germain (Estadio de la Cerámica, 21:00)
**Typ:** PSG wygra 53,7% (1,86) / PSG lub remis (X2) 75,7% (1,32) / Over 1.5 82,9% (1,21) | **Pewność:** średnia
**Rynki:** 1X2 24,3/22,0/53,7; O2.5 62,0% (1,61); O3.5 39,7%; BTTS tak 61,2% (1,63). Rożne śr. 9,8: O 9.5 50,6%, O 8.5 62,1% (1,61). Kartki śr. 3,6: O 2.5 65,5% (1,53), O 3.5 46,5%.
**Statystyki:** PSG 14-5 w 3 meczach, lider fazy ligowej (9 pkt), Villarreal 8-8 (3 pkt; szczegóły wyników niezweryfikowane). Ofensywa PSG wyższa; obrona Villarreal słaba (8 straconych).
**H2H:** brak istotnego.
**Informacje medialne:** nie znalazłem aktualnych absencji PSG (w poprzednim sezonie PSG miał liczne kontuzje; brak danych na teraz).
**Ryzyka:** wyjazd PSG, rotacja (liga w weekend), remis 22% i wygrana gospodarzy 24%.
**Rynek:** Betclic 3,95/4,30/1,71 (po marży 23,6/21,7/54,6) - zgodne.

---

## Podsumowanie i uwagi
- Wszystkie wyceny oparte na modelu Poissona z λ ręcznie oszacowanymi z tabeli i średnich goli; brak danych o składach i sędziach, więc pewność maks. średnia, rożne/kartki niska.
- Najbezpieczniejsze rynki (p wysokie, ale fair graniczny): Barcelona lub remis 88,2% (1,13), LASK lub remis 89,5% (1,12), Over 1.5 w kilku meczach (fair 1,16-1,25). Bardziej wartościowe fair: Barcelona wygrana 72% (1,39), LASK wygrana 72,3% (1,38), Bodø 1X 77,5% (1,29), PSG X2 75,7% (1,32).
- Uwaga: fragmenty "Statystyki" w sekcjach Inter, Man Utd, Villarreal bazują na tabeli ESPN i wyrywkowych źródłach, a część szczegółów (np. kto kogo pokonał) pochodzi z agregatów o niepewnej dacie; traktuj jako orientacyjne.
- To oszacowania probabilistyczne, nie gwarancje.
