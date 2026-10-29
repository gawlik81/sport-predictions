# Weryfikacja kuponów i analiz z 28.10.2026 (dzień i noc 28→29.10), weryfikacja 29.10, ok. 07:30 CET

**Pliki:**
- `ZWERYFIKOWANE_Kupony_10_2026-10-28.md` (kupony 1-4, puck line NHL; nogi rozliczone już 28.10, uzupełnione singlami), `ZWERYFIKOWANE_Kupony_10_2026-10-28_v2.md` (singles poziomu -2; brakowały nr 5, 6, 14, teraz rozliczone), `ZWERYFIKOWANE_Kupony_10_2026-10-28_v3.md` (8 kuponów, puchary, Serie A, kursy Betclic), `ZWERYFIKOWANE_Kupony_10_2026-10-28_v4.md` (NBA, kursy Betclic) oraz `ZWERYFIKOWANE_Analiza_nocy_2026-10-28.md` (NBA 12, NHL 4, LoL IG - LYON): wszystko rozstrzygnięte, **po weryfikacji z prefiksem `ZWERYFIKOWANE_`**. W analizie nocnej rynków zawodnika NBA sprawdzono tylko dla meczu IND - PHI (Maxey, Siakam, Embiid), reszty nie rozliczano.
- `Analiza_dnia_2026-10-28_v2.md`: rozliczona (Serie A, Carabao, DFB-Pokal, Puchar Polski, ATP Wiedeń i Bazylea, CS2, LoL, Dota 2), ale **bez prefiksu**: brak Morrow - VIT.A (ESEA bo1, nie ma w PandaScore) i nie sprawdzono rożnych/kartek/fauli ani total gemów.
- `Analiza_dnia_2026-10-28.md` (wersja z 27.10): **bez prefiksu**. Osaka - Pohankova (WTA Tokio, 1/8) przełożona na 29.10, 05:40 UTC (ESPN: Scheduled), więc nierozegrana. Reszta jej meczów pokrywa się z `_v2`.
- Ekstraklasa 25.10 i El Clásico zostały uzupełnione później: patrz `Weryfikacja_Uzupelnienie_Clasico_Ekstraklasa_2026-10-25.md` (oba pliki mają już prefiks).

**Źródła wyników:** ESPN scoreboard (**jedno źródło**) dla Serie A, Carabao Cup, DFB-Pokal, NBA, NHL, ATP i boxscore'u IND - PHI; PandaScore (MCP `sportsdata`, **jedno źródło**) dla CS2, LoL, Dota 2; Puchar Polski z WebSearch (igol.pl, gol24.pl, sportowefakty.wp.pl, interia.pl; wyniki spójne w kilku źródłach). Wynik po 90 minutach dla Tychy - Siedlce (2-2, dogrywka 4-2) i Puszcza - Wisła (1-1, dogrywka 1-2) z relacji. Kiel - Hoffenheim: 1-1 (karne 4-3), wyniku po 90' nie ustalono, rozliczono tylko awans.

## Wyniki (skrót)
- **Serie A:** Milan 2-4 Bologna; Parma 0-0 Udinese; Venezia 0-2 Inter; Genoa 2-0 Juventus; Monza 1-4 Napoli.
- **Carabao (90'):** City 2-2 Brighton (karne, awans City); Bournemouth 3-0 Villa; Fulham 0-1 Palace; Sunderland 3-2 Brentford; Liverpool 1-1 Chelsea (karne 6-5, awans Liverpool).
- **DFB-Pokal:** Dresden 2-0 Schalke; Freiburg 3-2 Wolfsburg; Paderborn 0-1 Stuttgart; Jeddeloh II 0-2 Hertha; Leverkusen 5-2 Nürnberg; Bayern 6-1 Magdeburg; Hannover 0-2 Kaiserslautern; Kiel 1-1 Hoffenheim (karne 4-3).
- **Puchar Polski 1/16:** Puszcza 1-2 Wisła Płock (po dogr.); Znicz 0-1 Ruch; Tychy 4-2 Siedlce (po dogr., 2-2 po 90'); Lechia 0-6 Jagiellonia.
- **ATP:** Wiedeń: Musetti 7-6 7-5 Tiafoe; Mannarino 6-4 7-5 Mensik; Basilashvili 7-6 6-1 Rodionov; De Minaur 6-4 6-2 Tien. Bazylea: Djokovic 4-6 6-3 6-4 Humbert; Fritz 6-4 7-6 Hijikata; Rune 3-6 6-3 7-6 Hurkacz.
- **E-sport:** CS2 PGL: FURIA 2-0 Liquid, NAVI 2-1 Spirit. LoL Worlds: T1 2-0 KOI, IG 2-1 LYON. Dota 2 PARI Universe: OG 2-1 Spirit, GamerLegion 2-1 LEGION. Niższe tiery w skrypcie bilansu (nie wypisuję wszystkich wyników).
- **NBA (noc 28/29.10):** MIA 129-117 ATL; CLE 121-111 WAS; DET 97-89 CHA; PHI 114-109 IND; TOR 129-99 ORL; NYK 133-127 CHI; HOU 132-100 MIL; GSW 119-114 MIN; DEN 104-91 NOP; SAS 117-111 UTA; DAL 120-96 OKC; LAL 103-87 LAC.
- **NHL:** WSH 5-2 PHI; EDM 4-0 CGY; COL 5-2 NJ; SEA 5-4 TOR (wszystkie w regulaminowym czasie).

## Bilans (skrypt `verify.py`, 168 nóg, 15 kuponów; typy z kuponów 1-4 i singli 7-13 z 28.10 były rozliczone w poprzedniej weryfikacji i nie są tu liczone drugi raz)
| | Trafione | Oczekiwane |
|---|---|---|
| Nogi (wszystkie) | 108/168 | 106,8 (+0,19 odch. std.), Brier 0,223 |
| Kupony (v3 x8, v4 x2, singles 5, 6, 14, Maxey, SAS U122,5) | 10/15 | 8,27 |
| w tym v3 (Betclic, 2 nogi) | 4/8 | ok. 4,3 |
| v4 (NBA, Betclic) | 2/2 | 1,08 |

Pasma p: 50-60% 35/66 (36,3); 60-70% 30/42 (26,9); 70-80% 29/44 (32,4; -1,15 odch. std.); 80%+ 11/11 (9,1).

| Grupa | Trafione | Oczekiwane |
|---|---|---|
| Piłka DC/12 w kuponach | 10/12 | 8,9 |
| Piłka Under / BTTS nie ("przewaga niepotwierdzona") | 13/19 | 10,6 |
| Piłka analiza bez kursu (1X2, gole, awans) | 32/54 | 36,6 (-1,36 odch. std.) |
| Tenis (zwycięzca, set, gemy) | 10/18 | 11,1 |
| NBA zwycięzca | 9/11 | 7,6 |
| NHL ML / puck line +1,5 / total | 3/4 / 1/4 / 1/2 | 2,35 / 2,48 / 1,07 |
| E-sport tier A/S (CS2 PGL, LoL, Dota A) | 8/10 | 6,3 |
| CS2 tier B-D (bo3) | 4/11 | 6,2 (-1,33 odch. std.) |
| CS2 ESEA bo1 | 5/6 | 3,7 |
| Dota tier D | 4/5 | 2,9 |

Hipotetyczny zysk przy stawce 1 na kupon: **+1,95** (informacyjnie; kursy Betclic, BettingPros). Rozbicie: v3 -1,67 (4 wygrane po 1,54-1,61 przy 4 przegranych), v4 +1,26, singles 5, 6, 14, Maxey, SAS +2,35. Zalecana stawka większości kuponów: 0% (EV < 0 lub skorygowane EV ≈ 0), więc to nie jest zysk z rekomendacji.

## Kupony
| Kupon | Nogi (Betclic) | Kurs | p | Wynik |
|---|---|---|---|---|
| v3 K1 (poz. 0) | ManCity-Brighton 1X + Tychy-Siedlce U2,5 | 2,46 | 50,2% | ❌ (Tychy 2-2 po 90') |
| v3 K2 (poz. 1) | Liverpool-Chelsea U3,5 + Hannover-K 1X | 2,25 | 51,8% | ❌ (Hannover 0-2) |
| v3 K3 (poz. 2) | Monza-Napoli 12 + Lechia-Jagiellonia 12 | 1,54 | 57,7% | ✅ |
| v3 K4 | Bournemouth-Villa 12 + Dresden-Schalke 12 | 1,61 | 55,1% | ✅ |
| v3 K5 | Fulham-Palace 12 + Puszcza-Wisła 12 | 1,57 | 54,8% | ❌ (Puszcza 1-1 po 90') |
| v3 K6 | Milan-Bologna 12 + Sunderland-Brentford 12 | 1,57 | 54,0% | ✅ |
| v3 K7 | Genoa-Juve 12 + Leverkusen 1 | 1,61 | 52,5% | ✅ |
| v3 K8 | Kiel-Hoffenheim awans gość + Znicz-Ruch 12 | 1,55 | 51,6% | ❌ (Hoffenheim odpadł w karnych) |
| v4 K1 | CLE + HOU ML | 1,52 | 58,1% | ✅ |
| v4 K2 | PHI + NYK ML | 1,74 | 50,1% | ✅ |
| Single 5 / 6 / 14 (v2) | Milan-Bologna U2,5 / Genoa-Juve U2,5 / Monza-Napoli O2,5 | 1,99 / 1,73 / 1,67 | 55,7% / 63,6% / 61,0% | ❌ (6 goli) / ✅ / ✅ |
| Single v4 | Maxey Over 24,5 pkt / SAS Under 122,5 | 1,90 / 2,05 | 59,8% / 51,0% | ✅ (27) / ✅ (117) |

Zestawy v3 K3-K8 i v4 miały EV ujemne (od -11% do -20% względem Betclic) i stawkę 0%; wynik 6/10 przy 5,1 oczekiwanych to wariancja, nie dowód przewagi. Kupony z dodatnim EV "z modelu" (v3 K1, K2) miały nogę oznaczoną jako "przewaga niepotwierdzona", EV skorygowane +0,4% i -3,7%, stawka 0,1% i 0%: obie przegrały.

## Typy spoza kuponów (hipotetycznie)
- **Under / BTTS nie z puli v3 (flaga "niepotwierdzona", p 5-17 pp ponad rynek):** 13/19 przy 10,6 oczekiwanych. Dobrze trafiły Paderborn-Stuttgart, Znicz-Ruch, Hannover-K, Dresden-Schalke, Fulham-Palace, Liverpool-Chelsea, Parma-Udinese, ManCity-Brighton U3,5; przegrały Tychy-Siedlce BTTS nie, Lechia-Jagiellonia U2,5 (0-6), Sunderland-Brentford U2,5 (5 goli), Puszcza BTTS nie, Milan-Bologna U2,5.
- **Tenis:** Fritz (2-0, -2,5 gema, 1. set) i Djokovic (-1,5 gema) trafili, Hurkacz (65%), Mensik (78%, rynek 82%) i Tiafoe 1. set nie.
- **E-sport:** T1 2-0, FURIA 2-0, GamerLegion i LYON +1,5 trafione; Spirit w CS2 (67,7%) i w Dota (73,2%) przegrali.
- **NBA zwycięzca:** MIN (59,5%) i OKC (66%, DAL wygrało +24) przegrali; pozostałe 9/11 (DET, TOR, DEN, SAS, LAL oprócz kuponów). Rynki zawodnika IND - PHI: Maxey ✅, Embiid zb. ✅, Siakam zb. U7,5 (65%) ❌ (11 zb.).
- **NHL:** puck line +1,5 PHI, CGY, NJ przegrały (różnice 3, 4, 3 bramki), SEA +1,5 trafiło; ML WSH, EDM, COL trafione, TOR (53%) nie. NHL puck line +1,5 razem z poprzednimi kolejkami: ok. 21/32 przy ok. 22,5.

## Analiza pomyłek
- **Wszystkie istotne pudła mieszczą się w wariancji, żadnego błędu procesu nie ustalono.** Bilans nóg 108/168 przy 106,8 oczekiwanych.
- **Milan - Bologna 2-4 (Milan wygra 53%, 1X 79,5%, Under 3,5 78%):** p Milanu już obniżone o 3 pp za 8 nieobecnych; 6 goli to ogon rozkładu. Kupony z tym meczem: K6 (12 ✅) i single 5 (U2,5 ❌). **Wariancja.**
- **Mensik - Mannarino 4-6 5-7 (78%, rynek 82%):** analiza zważyła zmęczenie Mannarino i porażkę w H2H; p było poniżej rynku. **Wariancja** (Mannarino wygrał 4. mecz w 6 dni).
- **Hurkacz (65%) przegrał z Rune 6-3 3-6 6-7, Tiafoe 1. set (54,5%):** zbliżone do p; **wariancja.**
- **Tychy - Siedlce (U2,5 63,6%, v3 K1) i Puszcza - Wisła (12, v3 K5):** oba kupony przegrały przez wyniki po 90' (2-2 i 1-1) w meczach, które potem rozstrzygnęła dogrywka. Puchar Polski z dogrywką ma wyższy udział remisów po 90' niż p w analizie (Puszcza-Wisła: DC 12 74%, remis w 90' ok. 26%). **Wariancja**; nie wystarcza do reguły (dwa mecze). W "Do obserwacji".
- **Kiel - Hoffenheim awans gość (72%, v3 K8):** Hoffenheim odpadł w karnych po 1-1; to dokładnie ryzyko awansu w pucharze, które analiza wyceniła (28% dla Kiela). **Wariancja.**
- **Spirit - NAVI 1-2 (67,7%) i Dota Spirit - OG 1-2 (73,2%):** Spirit przegrał obie serie, w CS2 p było 2 pp pod rynkiem, w Dota brak kursów. Razem z CS2 tier B-D (4/11) dziś ciemniejsza strona e-sportu, ale ESEA bo1 5/6 i tier A/S 8/10 równoważą ją (patrz niżej).
- **OKC - DAL 96-120 (OKC 66%), MIN - GSW (59,5%):** p ≈ rynek (66%, 59-61%); **wariancja.**
- **NHL puck line +1,5 (PHI, CGY, NJ przegrały, SEA wygrało):** 1/4 przy 2,5. Przegrane o 3-4 bramki (WSH 5-2, EDM 4-0, COL 5-2) przy wszystkich trzech faworytach u siebie; w analizie PHI b2b i niepewny Thompson, CGY Cooley vs słaby Jarry. Bez nowej informacji, która zapowiadałaby wynik. **Wariancja**, jednak 3 z 4 puck linów +1,5 w tej kolejce to gospodarze-faworyci, którzy wygrali wysoko.
- **Błąd budowy kuponu:** żadnego nowego. Kupony v3 K3-K8 złożone na poziomie 2 z oznaczeniem EV < 0 i stawką 0%, zgodnie z regułami.

## Co zadziałało
- **Reguła korekty "przewagi niepotwierdzonej" w v3:** obie nogi Under 2,5 w kuponach z EV "z modelu" (K1, K2) miały stawkę 0,1%/0%. Kupony przegrały; przy stawce proporcjonalnej do EV z modelu strata byłaby większa.
- **Piłka DC/12 z p 70-77% (poziom 2):** 10/12 w kuponach i 3/4 poza nimi (oczekiwane 8,9 i 2,3). Pudła to wyłącznie karne i dogrywki w pucharach (Puszcza-Wisła 12 po 90' remis).
- **p 80%+:** 11/11 (9,1 oczekiwanych), brak ryzyka z tej strony.
- **NBA zwycięzca:** 9/11; wszystkie 4 nogi kuponów v4 trafione. Reguła B2B (DET -4,4 pp, NYK) zadziałała w dobrym kierunku (oba wygrały), ale p nadal poniżej rynku.
- **LoL / Dota GL / IG:** T1 2-0, IG, LYON +1,5 i GL trafione.

## Kalibracja skilli
- **Bez zmian.** Bilans nóg +0,19 odch. std., brak ustalonego błędu procesu. Warunek z poprzedniej weryfikacji dla CS2 (≥ 30 nóg i poniżej -1,5 odch. std.) jest formalnie osiągnięty, ale dzisiejsza próba jest neutralna (CS2 11/19 przy 11,2: tier B-D 4/11, ESEA bo1 5/6, PGL 1/2); łącznie z wcześniejszymi seriami 19/37 przy 23,3 (ok. -1,5 odch. std.). Wprowadzenie reguły po jednej kolejce, która sama nie potwierdza wzorca, byłoby dopasowaniem do wcześniejszych wyników, więc zostawiam ją w "Do obserwacji".
- **`bet-slip-builder` (korekta z 26-28.10: Kelly z p ściągniętym do rynku + 5 pp dla "przewagi niepotwierdzonej"):** bez zmian. Dzisiejsze nogi Under/BTTS nie trafiły 13/19 przy p modelu 55,8% (rynek ok. 45%), co jest zgodne z modelem, ale razem z poprzednią kolejką (9/17 przy 65%) to 22/36 (61%) przy p modelu ok. 60%: za mało, żeby osłabiać regułę (to jest zasada konserwatywna przy stawce, nie zmiana p).

## Do obserwacji
- **CS2 zwycięzca serii (cały zbiór):** 19/37 przy ok. 23,3 (ok. -1,5 odch. std.); dzisiaj 11/19 (11,2). Warunek zmiany: kolejne ≥ 20 nóg i odchylenie poniżej -1,5 odch. std. (wtedy ściągnąć p faworytów CS2 bez rynku i veto o 3-5 pp i pewność "niska").
- **Tier B-D CS2 bo3:** 4/11 (6,2); ESEA bo1 5/6 (3,7). Dane cienkie, p 52-62%; nie ma sensu liczyć osobnej poprawki.
- **Puchary krajowe z dogrywką, remis po 90':** Puszcza-Wisła 1-1, Tychy-Siedlce 2-2, ManCity-Brighton 2-2, Liverpool-Chelsea 1-1 po 90' oraz Kiel-Hoffenheim 1-1 (po 90' lub w dogrywce): 4-5 remisów w 17 meczach pucharowych 28.10 (Carabao 5, DFB 8, PP 4). Przy DC/12 z p 72-77% (remis ok. 23-28%) to nie odbiega od oczekiwań; sprawdzić po kolejnych kolejkach, jeśli remisów w pucharach > 30% po ≥ 30 meczach.
- **DFB-Pokal, gole:** 28.10 bramek 2, 5, 1, 2, 7, 7, 2, 2 (w sumie 28 w 8 meczach), bez porównania z λ modelu; powiązanie z uwagą z poprzedniej weryfikacji (+1,0 odch. std.) do dalszego śledzenia po kolejnych rundach.
- **NHL puck line +1,5:** ok. 21/32 przy ok. 22,5; ostatnie 4: 1/4. Bez sygnału (zasięg próby).
- **NBA zwycięzca:** 9/11 (7,6) w tej kolejce; razem z poprzednią 16/22 przy 15,1. Bez zmian.
- **Osaka - Pohankova (29.10) i Morrow - VIT.A:** uzupełnić i dopiero wtedy dodać prefiks do `Analiza_dnia_2026-10-28.md` i `Analiza_dnia_2026-10-28_v2.md`.
- **Jakość danych:** piłka, NBA, NHL, tenis z jednego źródła (ESPN), e-sport z jednego źródła (PandaScore). Puchar Polski z kilku portali (WebSearch). Kursy v3/v4 z Betclic (przeglądarka), singles i kupony 1-4 z BettingPros; gg397.bet nie sprawdzano.

Propozycja commita: "Weryfikacja kuponów i analiz z 28.10.2026 (puchary, tenis, NBA/NHL, e-sport)".

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
