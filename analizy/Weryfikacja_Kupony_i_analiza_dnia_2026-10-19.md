# Weryfikacja kuponów i analizy dnia 19.10.2026 (piłka, tenis, NHL noc 19→20.10)

Zweryfikowane pliki:
- `ZWERYFIKOWANE_Kupony_10_2026-10-19.md` (dawniej `Kupony_10_2026-10-19.md`) - 0 kuponów spełniających progi; zestawy R1, R2, pojedynczy typ i 3 kupony po pominięciu EV > 0. W pełni rozliczony.
- `Analiza_dnia_2026-10-19.md` - **weryfikacja częściowa**: WTA Osaka Boulter - Sakatsume nierozliczony (ESPN pokazuje mecz jako "Scheduled" 20.10 z częściowym wynikiem 6-3 / 3-1 w setach, brak wyniku końcowego z drugiego źródła). Plik bez prefiksu do czasu uzupełnienia.

Źródła wyników: ESPN scoreboard (Premier League, La Liga, Serie A, NHL, ATP, WTA; NHL: wszystkie 4 mecze skończone w 3. tercji, więc rozliczenie po 60' i z dogrywką jest identyczne); Ekstraklasa: WebSearch, 4 zgodne źródła (Interia, gol24, cozadzien, pilkarskiswiat) - ESPN nie obsługuje ligi, Wikipedia nie była jeszcze zaktualizowana. Nie sprawdzano rynków rożnych i kartek (brak źródła, dokument i tak wykluczył je z kuponów).

## Wyniki
- Ekstraklasa: Wisła Płock 1-0 Radomiak.
- Serie A: Monza 4-0 Cagliari; Parma 0-3 Torino.
- Premier League: Tottenham 3-1 Coventry.
- La Liga: Getafe 1-1 Rayo Vallecano.
- ATP Lyon R1: Balshaw 2-1 Faria (6-2 4-6 6-3); Musetti 2-0 Arnaldi (6-1 6-4); Kouame 2-0 Sonego (7-6 6-4).
- WTA Ningbo: Sasnovich 2-0 Kasatkina (6-4 6-2); Bouzkova 2-0 Rakhimova (6-4 6-4); Eala 2-0 Parry (6-3 6-1).
- WTA Osaka: Boulter - Sakatsume: nierozliczony.
- NHL (po 60'): NYR 5-2 ANA; PHI 3-2 COL; TOR 3-1 SJS; UTA 5-4 PIT.

## Kupony i zestawy (stawka zalecana 0%, poza R1 i pojedynczym typem)

| Zestaw | Nogi | Kurs | p | EV | Wynik |
|---|---|---|---|---|---|
| R1 | Getafe U2.5 ✅ + Parma U2.5 ❌ (3 gole) | 2,37 | 44,8% | +6,0% | ❌ |
| R2 = kupon 2 sekcji 7 | Płock 1X ✅ + Getafe 1X ✅ | 1,88 | 51,3% | -3,4% | ✅ |
| Kupon 1 sekcji 7 | Monza 12 ✅ + Getafe U2.5 ✅ | 1,96 | 51,0% | -0,3% | ✅ |
| Kupon 3 sekcji 7 | Parma 12 ✅ + COL lub remis po 60' ❌ (PHI 3-2) | 1,70 | 50,9% | -13,4% | ❌ |
| Wariant ścisły | Płock 1X ✅ + Parma 12 ✅ | 1,73 | 52,8% | -8,7% | ✅ |
| Pojedynczy: Płock U2.5 @2,30 | 1 gol ✅ | 2,30 | 54,4% | +25,1% | ✅ |

Bilans zestawów dwunogowych: **3/5 przy oczekiwanych 2,51** (R2 i kupon 2 to ten sam zestaw, liczony raz). Hipotetyczny zysk przy stawce 1 na zestaw: +0,56 (bez pojedynczego typu); pojedynczy typ dodaje +1,30. Informacyjnie: R1 i pojedynczy typ miały dodatni EV, pozostałe EV ≤ 0 i stawkę Kelly 0%.

## Nogi z puli (hipotetycznie, wszystkie rynki z kursem Betclic)
Wszystkie 33 nogi (19 z kursami Betclic, tenis i NHL puck line/total 6,5 z analizy bez kursów): **19/33 przy oczekiwanych 19,44 (-0,16 odch. std.)**, Brier 0,234.

| Grupa | Trafione | Oczekiwane |
|---|---|---|
| piłka Under (2.5) | 2/5 | 2,94 |
| piłka BTTS nie | 3/4 | 2,21 |
| piłka 12 + DC | 4/4 | 2,86 |
| tenis zwycięzca | 4/6 | 3,63 |
| NHL po 60' (3-way, COL/remis) | 0/3 | 1,45 |
| NHL puck line (analiza, bez kursów) | 2/4 | 2,68 |
| NHL total 6,5 (analiza) | 2/4 | 2,27 |

Nogi z "przewagą niepotwierdzoną" (+5 pp nad rynkiem i więcej): Płock U2.5 ✅, Płock BTTS nie ✅, Getafe U2.5 ✅, Getafe 1X ✅, Parma BTTS nie ✅, Getafe BTTS nie ❌, Parma U2.5 ❌ - 5/7 przy oczekiwanych ok. 4,5.

Tenis (typy z analizy, bez kursów): Musetti ✅, Sasnovich ✅, Bouzkova ✅, Eala ✅, Faria ❌ (Balshaw wygrał), Sonego ❌ (Kouame 7-6 6-4). Boulter nierozliczony.

## Analiza pomyłek
- **Parma - Torino Under 2.5 (p 63,6%):** 0-3. Dokument opisał mecz jako niską liczbę goli (λ łączne 2,15), 3 gole to wynik w zasięgu rozkładu. **Wariancja.**
- **Monza - Cagliari Under 2.5 (p 57%, poza kuponami):** 4-0. Monza po 4 punktach w sezonie i bilansie 9:15 strzeliła 4. Dokument słusznie pominął ten typ (EV -0,8%). **Wariancja.**
- **Tottenham Under 2.5 (p 48,1%):** 3-1, **wariancja** (p < 50%, noga i tak nie weszła do kuponu). Ciekawsze: **Tottenham do wygrania** - model dawał 43%, rynek ok. 63%, mecz wygrali Spurs 3-1. Różnica 20 pp bez twardej informacji (poza zawieszeniem Bentancura i niepewnymi Porro/Kulusevskim) to klasyczny przypadek "p różne od rynku o > 5 pp"; dokument sam ostrzegał o rozjeździe i słusznie wyłączył nogi Spurs z kuponów (stawka 0%). Jeden wynik nie dowodzi błędu modelu; zapisane w "Do obserwacji".
- **Getafe BTTS nie (p 62,5%):** 1-1, **wariancja** (przewaga niepotwierdzona +6,3 pp; noga poza kuponami).
- **COL lub remis po 60' (p 72,1%, kupon 3):** PHI (1-6-3 przed meczem) wygrało 3-2 w regulaminowym czasie. Dokument wskazywał, że bramkarze niepotwierdzeni i COL gra drugi mecz z rzędu; p 72% to wynik modelu bez korekty o b2b. Jedno zdarzenie, **wariancja**, ale to drugi dzień z rzędu, w którym faworyt NHL po b2b przegrywa (wczoraj CAR, p 66%) - patrz "Do obserwacji". Kupon 3 był ostatni w rankingu EV (-13,4%) i miał stawkę 0%.
- **NHL po 60': 0/3 (ANA, PIT, COL/remis):** ANA 38,5% i PIT 34,2% to typy na underdogów (3-way), więc 0/2 przy p ~36% to wariancja.
- **Wykluczenia:** Płock Under 2.5 @2,30 (EV +25%) trafił, mimo "niepotwierdzonej przewagi" +13,7 pp; dokument słusznie nie zamienił go w kupon, a stawkę ograniczył do 0,5-1%. Jeden trafiony typ nie unieważnia reguły o przewadze niepotwierdzonej (poprzednio 07.10 takie typy przegrywały).

## Co zadziałało
- Uczciwy komunikat "0 kuponów spełnia wszystkie progi" i brak fabrykowania 10 zestawów; R1/pojedynczy typ miały EV > 0, a wynik 2/2 z nich (R1 przegrał, pojedynczy trafił) nie zmienia oceny.
- Wyłączenie nóg Tottenhamu z kuponów przy rozjeździe model-rynek 20 pp.
- Zachowawcze wybory 12/1X w piłce: 4/4.
- Usunięcie sprzecznego kuponu (Płock 12 + Getafe 12) obok kuponu 1X + 1X: remis w Getafe-Rayo (1-1) rozdzieliłby je, więc usunięcie było słuszne.

## Kalibracja skilli
**Bez zmian.** Brak błędu procesu: pudła to wynik Parma U2.5 (p 64%), Monza U2.5, Getafe BTTS nie, COL (jedno zdarzenie NHL) i dwa underdogi NHL; łączny bilans 19/33 vs 19,44 jest zgodny z oczekiwaniami. Nie zmieniam reguł po jednym dniu.

## Do obserwacji
- **Model vs rynek, duży rozjazd bez twardej informacji:** Tottenham 43% vs rynek ok. 63%, wygrali (licznik rozjazdów > 15 pp w piłce, w których rynek miał rację: 1). Jeśli takie rozjazdy znów okażą się błędem modelu, dodać do `football-analyst` regułę: p nie niżej niż rynek - 10 pp.
- **Faworyci NHL po b2b / drugi mecz z rzędu:** CAR (18.10, p 66%) i COL (19.10, p 72% na "lub remis") przegrali; 0/2. Gdy będzie ≥ 5 takich nóg z wynikiem, rozważyć w `nhl-analyst` odjęcie ok. 3-5 pp za b2b w p faworyta.
- **Piłka Under 2.5 (p 48-70%):** 2/5 dziś (oczekiwane 2,94); próba < 10, licznik startuje od dziś.
- **Piłka 12:** 12/12 łącznie (10/10 z 18.10 plus 2/2 dziś), oczekiwane ok. 9,0; licznik rośnie, reguła bez zmian do ≥ 30 nóg.
- **Do uzupełnienia:** Boulter - Sakatsume (po opublikowaniu wyniku końcowego), potem `Analiza_dnia_2026-10-19.md` dostaje prefiks `ZWERYFIKOWANE_`. Nadal otwarta noga CS2 FURIA - BetBoom Over 69,5 rund z `Kupony_10_2026-10-18.md`.
- Jakość danych: Ekstraklasa z 4 źródeł (zgodne), ESPN dla reszty (jedno źródło), tenis z ESPN (jedno źródło).

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
