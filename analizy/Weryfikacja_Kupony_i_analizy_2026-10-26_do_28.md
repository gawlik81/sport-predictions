# Weryfikacja analiz i kuponów z 26.10, 27.10 i 28.10 (noc) oraz uzupełnienie 25.10 wieczór (weryfikacja 28.10, ok. 15:00 CET)

**Pliki:**
- `ZWERYFIKOWANE_Kupony_10_2026-10-26.md`, `ZWERYFIKOWANE_Kupony_10_2026-10-26_v2.md` (NBA/NHL, poziomy 3, 4, -1), `ZWERYFIKOWANE_Analiza_dnia_2026-10-26.md`, `ZWERYFIKOWANE_Analiza_NBA_NHL_2026-10-26.md`: wszystko rozstrzygnięte, **po weryfikacji z prefiksem `ZWERYFIKOWANE_`**.
- `ZWERYFIKOWANE_Kupony_10_2026-10-27.md` (2 kupony + poziomy -1 i -2), `ZWERYFIKOWANE_Analiza_dnia_2026-10-27.md`: wszystko rozstrzygnięte, **z prefiksem**.
- `ZWERYFIKOWANE_Analiza_dnia_2026-10-25_wieczor.md`: uzupełnienie brakujących e-sportu (LoL Worlds Swiss R3 x4, CS2 PGL R2 x2) i PSG - Lyon (przełożony na 26.10), **z prefiksem**.
- `Kupony_10_2026-10-28.md`, `Kupony_10_2026-10-28_v2.md`, `Analiza_dnia_2026-10-28.md`: **weryfikacja częściowa, bez prefiksu.** Rozliczono noc NBA/NHL (27/28.10 USA) i poranną część tenisa. **Nie rozegrane lub w toku w chwili weryfikacji:** Serie A (5 meczów, od 18:30), Carabao Cup (5), DFB-Pokal (8), wieczór ATP (Bazylea, Wiedeń), e-sport, kupony pojedyncze 5, 6 i 14 (Milan - Bologna, Genoa - Juventus, Monza - Napoli), Osaka - Pohankova (brak w ESPN).
- `Analiza_dnia_2026-10-25.md`: nadal **bez prefiksu**, brakuje Śląsk - Wieczysta, Jagiellonia - Wisła Płock, Legia - Lech (WebSearch nie zwraca wyników Ekstraklasy z 25.10; ESPN nie obsługuje ligi). `ElClasico_...` bez zmian (nie sprawdzono kartek, fauli i strzałów meczowych).

**Źródła wyników:** ESPN scoreboard i summary (**jedno źródło**) dla piłki, NBA, NHL, tenisa i boxscore'ów (Tatum, Wembanyama, Cunningham, Sabonis, Booker, SGA, Jokic, Jarry); PandaScore (MCP `sportsdata`, **jedno źródło**) dla CS2 i LoL. Wszystkie mecze NHL/NBA rozliczono z wyniku końcowego: puck line i ML z dogrywką/karnymi, total NHL po 60 minutach plus bramki w dogrywce (karne się nie liczą). Nie sprawdzano rożnych, kartek, fauli, total gemów ani handicapów gemowych (poza wyjątkami). Krecz Fearnley - Fery (Wiedeń 26.10) bez typu w analizie.

## Wyniki (skrót)
- **26.10 piłka:** Santa Clara 1-2 Benfica; PSG 2-0 Lyon; Sevilla 2-0 Osasuna. **CS2 PGL R3:** MOUZ 2-0 MongolZ, Aurora 2-0 Nemiga, FUT 2-1 Vitality, TYLOO 2-1 9z, Spirit 2-1 FURIA, Liquid 2-0 Legacy, BetBoom 2-0 NAVI, DENDELE 2-1 G2.
- **26.10 NBA (USA):** CHA 110-103 WAS; CLE 127-125 MIN (OT); BOS 134-99 CHI; DAL 113-109 MIA; MIL 110-102 IND; OKC 125-114 PHX; HOU 120-110 ATL; MEM 110-105 UTA; GSW 134-114 DEN. **NHL:** LAK 6-3 NYR; CGY 5-2 TOR; DET 4-3 EDM (karne, 3-3 po 60').
- **27.10 DFB-Pokal (90'):** HSV 1-3 Frankfurt; Essen 1-2 Leipzig; Großaspach 2-4 Augsburg; Bochum 2-0 Mainz; BVB 3-2 Werder; Gladbach 2-0 KSC; Köln 5-0 Union; Elversberg 0-2 Darmstadt. **Carabao:** Bradford 2-0 Peterborough; Fleetwood 1-1 Arsenal (Arsenal w karnych). **Tenis:** Alcaraz, Zverev, Norrie, Cobolli, Hurkacz, Jodar, Michelsen, Fils, Shelton, Lehecka, Paul, Mannarino, Kym wygrali.
- **28.10 noc NBA:** BOS 125-124 BKN (OT); NYK 111-97 DET; SAS 130-103 SAC; POR 136-129 LAL. **NHL:** CBJ 4-3 PHI (OT); CAR 2-1 BOS; CHI 2-1 LAK; MTL 2-0 STL; NYI 4-3 NSH (karne); NJ 5-1 DAL; FLA 5-1 WPG; MIN 3-1 UTA; VGK 4-1 OTT; VAN 6-5 ANA (OT); BUF 2-0 SJ. **Tenis rano:** Struff, Shnaider, Eala, Siniakova, Badosa, Rakhimova, Joint, Dart, Shi wygrali.
- **25.10 uzupełnienie:** PSG 2-0 Lyon. LoL: IG pokonało HLE, TES pokonało G2, DK 2-0 MKOI, Gen.G 2-1 LYON. CS2 R2: NAVI 2-0 FURIA, Legacy 2-0 DENDELE.

## Bilans (skrypt `verify.py`, 170 nóg, 39 kuponów; dubletty i single'e liczą te same nogi, więc bilansu kuponów nie traktować jako niezależnych zdarzeń)
| | Trafione | Oczekiwane |
|---|---|---|
| Nogi (wszystkie) | 108/170 | 107,5 (+0,08 odch. std.), Brier 0,220 |
| Kupony poziomów 0-4 (2 nogi; 26.10 A-D, NBA/NHL p3 i p4, 27.10 K1-K2, 28.10 K1-K4) | 5/16 | 8,1 |
| Poziom -1 (dublety 27.10, Under x2 26.10) | 0/6 | 2,5 |
| Poziom -2 single (27.10 / 28.10, rozstrzygnięte) | 5/10 / 5/7 | 6,5 / 4,2 |
Pasma p: 50-60% 39/71 (38,8); 60-70% 33/52 (33,6); 70-80% 21/28 (20,3); 80%+ 14/16 (13,4): kalibracja prawie idealna.

| Grupa | Trafione | Oczekiwane |
|---|---|---|
| Tenis zwycięzca | 22/32 | 19,95 |
| Piłka 1X2/90' / awans / DC | 8/11 / 8/10 / 4/5 | 6,75 / 6,97 / 3,80 |
| Piłka Over / Under | 4/6 / 6/10 | 4,26 / 6,78 |
| NBA zwycięzca / spread / total / zawodnik | 7/11 / 6/11 / 6/12 / 5/8 | 7,49 / 5,81 / 6,40 / 4,56 |
| NHL puck line +1,5 / zwycięzca / total | 12/15 / 3/8 / 5/6 | 10,49 / 4,48 / 3,41 |
| **CS2 zwycięzca** | **4/10** | 6,81 (-1,9 odch. std.) |
| **LoL (zwycięzca, mapy)** | **3/8** | 5,08 (-1,6 odch. std.) |
| CS2 handicap/total | 4/6 | 3,88 |

Hipotetyczny zysk przy stawce 1 na kupon: **-11,55** (informacyjnie; kursy Betclic, BettingPros, Pinnacle i fallbacki; stawki zalecone 0% poza wymienionymi poniżej). Rozbicie: kupony p0-4 ok. -6,6 (część zestawów to alternatywy tych samych nóg), dublety -1 -5,0, single'e 27.10 -1,2, single'e 28.10 +2,2.

## Kupony (najważniejsze)
| Kupon | Nogi | Kurs | p | Wynik |
|---|---|---|---|---|
| 26.10 A / B / C / D | Benfica O1,5 + PSG O2,5 / Sevilla 12 + BetBoom +1,5 / G2 + Sevilla O1,5 / Vitality + De Minaur | 1,71 / 1,81 / 1,70 / 1,60 | ok. 51% | ❌ / ✅ / ❌ / ❌ |
| 26.10 NBA/NHL p3 #1, #2 | OKC + DEN; MIA + HOU | 1,73; 1,97 | 53,2%; 46,1% | ❌ (DEN); ❌ (MIA) |
| 26.10 p4 #1-#4 | BOS + IND; OKC + TOR O5,5; DEN + HOU; MIA + CLE | 1,74-2,01 | 45-53% | ❌ (IND); ✅; ❌ (DEN); ❌ (MIA) |
| 26.10 -1 | Under 221,5 PHX@OKC + Under 240,5 DAL@MIA (Betclic 1,82 / 1,89) | 3,44 | 33,9% | ❌ (239 pkt; drugi Under trafiony: 222) |
| 27.10 K1 / K2 | Alcaraz + Bradford U3,5 / Lehecka + Mainz awans | 1,79 / 1,64 | 58,4% / 51,2% | ✅ / ❌ (Mainz) |
| 27.10 -1 D1-D5 | pięć dubletów Under 3,5/2,5 i Dimitrov | 2,69-5,54 | 32-54% | 0/5 (każdy z jedną przegraną nogą) |
| 27.10 -2 | 10 singli (9 Under + Dimitrov) | 1,46-2,69 | 49-80% | 5/10 (Essen, Fleetwood, Bradford, Gladbach, Bochum) |
| 28.10 K1-K4 | puck line +1,5: MTL + SJ; NYI + MIN; PHI + WPG; NJ + CHI | 1,88-2,08 | 51-53% | ❌ (SJ 0-2) / ✅ / ❌ (WPG 1-5) / ✅ |
| 28.10 -2 (rozstrzygnięte 7) | VAN +1,5 ✅, Tatum zb. U8,5 ✅ (5), Wembanyama pkt U26,5 ❌ (29), BOS +1,5 ✅, Cunningham ast U8,5 ✅ (8), OTT +1,5 ❌ (1-4), LAK@CHI U5,5 ✅ | 1,55-2,12 | 48-67% | 5/7 |

Poziomy -1, -2 i część nóg to nogi z "przewagą niepotwierdzoną" (p modelu o 5-20 pp ponad rynek bez twardej informacji). **Te nogi trafiły 9/17 (53%) przy średnim p modelu ok. 65%** (27.10: 5/10; 26.10 Under 221,5/240,5: 1/2; 28.10 MTL, SJ, VAN, BOS, OTT: 3/5). Kupony nie były zalecane do gry; kupon 27.10 K1 miał stawkę 0% właśnie z tego powodu.

## Typy spoza kuponów (hipotetycznie)
- Zwycięzcy NBA 26.10: BOS, CLE, CHA, OKC, HOU trafieni; DEN (-20 u siebie z GSW bez Butlera i Porzingisa), MIA, IND przegrali. NBA spread i total z liniami rynkowymi (6/11 i 6/12) wokół 50%: wykluczanie ich z kuponów było słuszne.
- Rynki zawodnika (tylko analiza, bez rekomendacji): 26.10 SGA PRA U44,5 ✅ (32), Jokic ast O8,5 ✅ (11), Booker pkt O22,5 ❌ (3 pkt), Jarry obrony U26,5 ✅ (26); 28.10 Sabonis zb. O12,5 ✅ (14), Tatum pkt U26,5 ❌ (40 w dogrywce). Brak rekomendacji był słuszny (jedno źródło średnich), wynik 4/6 w granicach wariancji.
- NHL ML poza kuponami: CAR, VGK, FLA ✅, ANA ❌ (VAN wygrało w dogrywce).
- PSG - Lyon: PSG wygrana, 1X, Over 1,5 i Lyon Under 1,5 ✅; Lyon Over 0,5 ❌ (0 goli). Over 2,5 (p modelu 59,9% wobec ok. 68% rynku, niepolecany) nie padło (2 gole).
- DFB-Pokal 27.10: awans 8/10 (Mainz i Elversberg przegrali), 90' 8/11.

## Analiza pomyłek
- **CS2 zwycięzca 4/10 (-1,9 odch. std.) i LoL 3/8:** 26.10 przegrali Vitality (74%), 9z (71%), G2 (72%), Legacy (64%), NAVI (58%); 25.10 FURIA (60%), HLE (66%), G2 (55%). Analizy 26.10 powstały **bez veto, map poolu i bez kursów** (HLTV i Liquipedia 403), a pewność zapisano jako "średnia". Pojedyncze pudła mieszczą się w wariancji (Bo1, serie 2-1), ale **cały zestaw faworytów o p 64-74% wygrał 3/8**. To jeszcze nie ustalony błąd procesu (próba mała, reguła "nie schodź pod rynek" nie dotyczyła, bo rynku nie znano): zapis w "Do obserwacji".
- **Mainz awans (p 66%, kupon 27.10 K2) i Elversberg awans (71%):** obaj faworyci przegrali z drużynami 2. ligi (Mainz bez bramkarza Zentnera; analiza to opisała i p było poniżej rynku, ok. 70%). **Wariancja.** Typy Under 3,5/2,5 z 27.10 (HSV 4 gole, Großaspach-Augsburg 6, BVB-Werder 5, Köln-Union 5): łącznie 33 gole wobec 27,8 z λ modelu (+1,0 odch. std.), rynek (linie 3,25-3,75) był bliżej. To właśnie "przewaga niepotwierdzona" (10-20 pp ponad rynek) przeszła w fałszywe EV.
- **Błąd budowy/sugerowanej stawki (jedyny błąd procesu w tej kolejce):** `bet-slip-builder` w trybach -1/-2 każe dawać Kelly 1/4, a jednocześnie "przewaga niepotwierdzona nie podnosi EV". Dokumenty z 27.10 i 28.10 podały stawki 3,7-9,1% dla nóg, które same opisały jako podejrzane; takie nogi trafiły 9/17, single'e Under z 27.10 -12% przy stałej stawce. Dokument 27.10 zastrzegał, że stawki są "górną granicą", ale reguły nie było. Zmiana opisana niżej.
- **NBA 26.10:** DEN (71%, rynek ok. 72%), MIA (71%), IND (62%): p zgodne z rynkiem, statusy zawodników uwzględnione. **Wariancja.** OKC/PHX Under 221,5 (p 58,8% vs rynek ok. 51%) przegrało (239 pkt), a MIA/DAL Under 240,5 trafiło: ten sam typ przewagi niepotwierdzonej, wynik 1/2.
- **WTA 28.10:** Alexandrova (64%), Tjen (62%), Yastremska (66%) przegrały, Shnaider (68%) wygrała, p_serve z modelu bez statystyk: 1/4 przy 2,6. Mała próba (do obserwacji).
- **NHL 26.10:** NYR (55,5%), TOR (57%), EDM (59,5%) jako gospodarze/faworyci przegrali, p ≈ rynek: **wariancja** (ML 3/8 vs 4,5). Puck line +1,5: 12/15 (10,5).
- **Arsenal wygrana w 90' (81%) ❌:** remis 1-1 z Fleetwood, awans w karnych. Reguła o rotacji w pucharach (p już ścięte o 7 pp względem rynku) zadziałała w dobrym kierunku, ale nie dość; poza kuponami (fair 1,23 ale p>81% i "odpada" w analizie). **Wariancja.**
- **Wembanyama pkt U26,5 (p 58%):** 29 pkt w 27 minut (14/21) w meczu +27: **wariancja**, ale to kolejny Under zawodnika oparty na jednym źródle średnich z 3 meczów (p nie powinno przekraczać ok. 55% przy takim źródle).

## Co zadziałało
- Kalibracja pasm p: 108/170 przy 107,5 oczekiwanych; tenis 22/32, piłka awans 8/10.
- Puck line +1,5 w NHL: 12/15 (10,5); łącznie z poprzednimi kolejkami ok. 20/28 przy ok. 20 oczekiwanych (próba rośnie, bez sygnału błędu).
- Odmowa wejścia do kuponów (v2 26.10, K1 27.10 stawka 0%): Under 221,5/240,5 i Under 3,5 z "przewagą niepotwierdzoną" okazały się loterią; decyzja o stawce 0% w zestawie bazowym była słuszna.
- Wykluczenie spreadów i totali NBA z p ok. 50%, wykluczenie Over 2,5 PSG z rekomendacji: wynik ok. 50%.
- NHL total: 5/6 w tej kolejce (łącznie z 24-25.10 ok. 17/29 przy 18,7, odchylenie spadło z -1,4 do -0,9 odch. std.).

## Kalibracja skilli
- **`bet-slip-builder` (zmiana):** w opisie poziomu -1/-2 dopisano, że stawkę Kelly'ego dla nogi z "przewagą niepotwierdzoną" liczy się z p ściągniętym do p rynku + 5 pp, a przy EV ≤ 0 po tej korekcie stawka wynosi 0% (uzasadnienie: weryfikacja 26-28.10, 17 nóg, 9 trafień przy p modelu ok. 65%; single'e 27.10 ok. -12%).
- **Skille analityczne, `sports-fixtures-finder`:** bez zmian. Bilans nóg (+0,08 odch. std.) i pasm p mieści się w wariancji; pudła mają p blisko rynku; CS2 poniżej oczekiwań (-1,9 odch. std.) to wzorzec do obserwacji, nie ustalony błąd.

## Do obserwacji
- **CS2 zwycięzca serii:** 25-26.10 4/10 przy 6,8, razem z wcześniejszą weryfikacją (4/8 przy 5,3) **8/18 przy ok. 12,1 (-2,1 odch. std.)**. Faworyci o p 64-74% bez veto i bez rynku przegrywają zbyt często. Warunek zmiany: próba ≥ 30 nóg i odchylenie nadal poniżej -1,5 odch. std.; wtedy w `esports-analyst` ściągnąć p faworytów CS2 o 3-5 pp, gdy brak rynku i veto, i oznaczać pewność "niska".
- **LoL Bo1/Bo3:** 3/8 (5,1) w tej kolejce; w wcześniejszych weryfikacjach m.in. 3/4 (2,64) i 4/7. Brak spójnego sygnału, warunek jak dla CS2 (≥ 30 nóg).
- **DFB-Pokal, gole:** 33 faktyczne vs 27,8 z modelu (10 meczów, +1,0 odch. std.); analizy znów mniej bramkowe niż rynek. Warunek: kolejne rundy pucharów, jeśli wynik > +1,5 odch. std. po ≥ 20 meczach, podnieść bazowe λ w pucharach krajowych.
- **WTA, p_serve szacowane (28.10):** faworyci z p ≥ 62%: 1/4. Warunek: ≥ 15 meczów WTA z takim p i bilans < -1,5 odch. std.
- **NHL:** puck line +1,5 20/28 (ok. 20,0); total 17/29 (18,7); ML 3/8 w tej kolejce. Bez zmian.
- **NBA spread z linią rynkową:** 6/11 (5,8); z linią szacowaną przez model wcześniej 3/11 (6,8). Wariant z linią rynkową działa, warto wymagać linii rynkowej (próba ≥ 15).
- **Nogi "przewagi niepotwierdzonej":** 9/17 (p modelu 65%, rynek ok. 55%); sprawdzić po kolejnych 20-30 nogach, czy trafiają jak rynek. Jeśli tak, rozważyć ograniczenie p w analizach do rynku + 5 pp także dla stawek poziomów 0-2.
- **Kolejne uzupełnienia:** po rozegraniu 28.10 (Serie A, Carabao, DFB-Pokal, wieczorny tenis, e-sport, singli 5, 6, 14) zweryfikować pliki 28.10 i dodać prefiks; Ekstraklasa 25.10 do uzupełnienia z Flashscore/ekstraklasa.org.
- **Jakość danych:** piłka, NBA, NHL, tenis z jednego źródła (ESPN), e-sport z jednego źródła (PandaScore). Kursy w kuponach z BettingPros, Pinnacle i Betclic (częściowo od użytkownika), nie z jednego bukmachera.

Propozycja commita: "Weryfikacja kuponów i analiz z 26-28.10.2026 i stawki Kelly'ego dla nóg z przewagą niepotwierdzoną".

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
