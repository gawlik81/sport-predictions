# Weryfikacja kuponów z 04.11.2026 (Liga Mistrzów, ATP Paryż, noc NBA + NHL 04→05.11) i uzupełnienie 03.11

**Zweryfikowane pliki:** `Kupony_10_2026-11-04.md` (kupony K1-K3, lista 20 predykcji poziomu 7, 2 nogi poza kuponami z EV+; **w całości**, po zmianie nazwy `ZWERYFIKOWANE_`), `ZWERYFIKOWANE_Kupony_10_2026-11-04_v2.md` (noc NBA + NHL: kupony 1-2, lista 13, pula nóg; **częściowo**), uzupełnienie `Kupony_10_2026-11-03.md` (nogi #19).
**Nie oznaczone:** `ZWERYFIKOWANE_Kupony_10_2026-11-04_v2.md` (noga #12 Miami Heat w LAC - MIA nie rozstrzygnięta w chwili weryfikacji, 05.11 ok. 07:00 CET, Clippers prowadzili 104-103 w 4. kwarcie; kupony 1-2 rozliczone, bo nie zawierają tej nogi) i `ZWERYFIKOWANE_Kupony_10_2026-11-02.md` (brak wyników Ekstraklasy: Radomiak - Śląsk, Raków - Pogoń, Zagłębie - Korona; ESPN nie ma polskiej ligi, WebSearch bez wyniku).
**Źródła wyników:** ESPN scoreboard (LM, NBA, NHL, tenis ATP; jedno źródło), NHL API (`nhl_scores`) dla LAK - SJS (7-2, `OVER`) i pozostałych NHL. Piłka po 90 minutach; puck line z dogrywką/karnymi.
**Uwaga o danych:** (1) feed NBA ESPN/NBA CDN dla LAC - MIA stał w miejscu, dlatego ta noga jest nierozliczona. (2) Kouamé - Davidovich Fokina z `Kupony_10_2026-11-03.md` nie ma w drabince ESPN: Kouamé grał w R1 z Borgesem (3-6 1-6), a Davidovich Fokina nie występuje w żadnej rundzie ani w kwalifikacjach. Noga #19 opierała się na meczu, którego nie było (**błąd danych wejściowych**, noga unieważniona, jedno źródło), więc `Kupony_10_2026-11-03.md` jest oznaczony jako zweryfikowany.

## Wyniki
- **LM 04.11:** AEK 2-3 Real, Fenerbahçe 3-2 Liverpool, BVB 2-1 Betis, Porto 4-1 Napoli, Lens 1-9 Como, PSV 1-2 Brugge, Lipsk 2-3 City, Slavia 1-2 Arsenal, Viking 4-1 Sabah.
- **ATP Paryż R2 (04.11):** Paul - Merida 6-1 6-1, Hijikata - Djokovic 2-6 6-3 6-3, Fritz - Molcan 6-7 7-5 7-6, Musetti - Zverev 7-6 6-2, Etcheverry - de Minaur 7-6 6-3, Buse - Medvedev 6-4 6-4, Borges - Khachanov 6-3 6-4.
- **NBA:** Pistons 106-112 76ers, Wizards 105-120 Hawks, Celtics 109-102 Bucks, Nets 114-104 Hornets, Knicks 135-105 Bulls, Grizzlies 103-107 Pacers, Pelicans 120-113 Jazz (dogr.), Thunder 124-116 Cavaliers, Rockets 107-117 Timberwolves, Nuggets 128-109 Raptors, Suns 119-132 Trail Blazers, Spurs 112-111 Mavericks, Kings 103-116 Lakers; Clippers - Heat trwa.
- **NHL:** Sabres 1-2 Senators, Panthers 5-3 Blackhawks, Kings 7-2 Sharks, Kraken 2-1 Flames (dogr.).

## Bilans (skrypt `verify.py`, 40 nóg, 1 nierozliczona)
| | Trafione | Oczekiwane |
|---|---|---|
| Wszystkie nogi | 27/40 | 27,6 (-0,21 odch.) |
| Lista 20 (LM + tenis) | 15/20 | 14,6 |
| Tenis zwycięzca (5 + Khachanov) | 2/6 | 4,29 (-2,09 odch.) |
| Lista NBA/NHL (12 rozliczonych z 13) | 9/12 | 8,7 |
| Kupony (5) | 2/5 | 2,71 |

Kupony: **K1 LM** Porto 1X + Arsenal trafiony (kurs 1,55), **K2 LM** Real + Lens X2 trafiony (1,59), K3 LM BVB + PSV 1X przegrany przez PSV - Brugge 1-2. NBA/NHL kupon 1 (BOS + SJS +1,5) przegrany przez Kings 7-2, kupon 2 (HOU + OTT +1,5) przegrany przez Rockets 107-117. Hipotetyczny zysk przy stawce 1 na kupon: -1,86 (tylko informacja; stawki zalecone 0-0,7%).

## Typy spoza kuponów (hipotetycznie)
- **Real - AEK BTTS nie** (p 56%, kurs 2,23, "przewaga niepotwierdzona" +11 pp): przegrane (2-3). **Porto Under 2,5** (p 50,6%, 2,13, +6,6 pp): przegrane (5 goli). Wykluczenie z kuponów było słuszne.
- Pula NBA/NHL: BKN +3,5 trafione (+10), DAL +12,5 trafione (-1), OTT - BUF Under 6,5 trafione (3 gole), CLE +3,5 przegrane (-8), TOR +4,5 przegrane (-19); CGY +1,5 (lista #8) trafione (1-2 w dogr.).
- Khachanov (remis #20, p 63%, 1,41): przegrał z Borgesem, pominięcie słuszne.

## Analiza pomyłek
- **Tenis: de Minaur (77%), Zverev (64%), Djokovic (75%), 0/3.** Dokument zastosował korektę z `tennis-analyst` (rynek bez marży 81,7/68,2/78,4% → p 77/64/75, czyli -3,4 do -4,7 pp), więc reguła została wykonana, ale okazała się za słaba: de Minaur i Zverev to faworyci po wolnym losie w R2 przeciw rywalom po wygranym R1 (Etcheverry, Musetti), Djokovic po trzech setach dzień wcześniej. Ten sam wzorzec co Wuhan R2 14.10 (Sabalenka, Pegula) i Almaty 21.10 (Rublev): od 14.10 faworyci po wolnym losie w R2 mają **1 trafienie z 6 przy ok. 4,4 oczekiwanych** (Świątek jedyna wygrana). Nie dotyczy kuponów (żadnego z nich nie było w K1-K3), ale lista 20 i jej kolejność przy zbyt małej korekcie dalej ich zawiera. **Błąd procesu (wzorzec potwierdzony w 3 weryfikacjach) → zmiana `tennis-analyst`.**
- **Real - AEK BTTS nie i Porto Under 2,5**, p modelu 11 i 6,6 pp ponad rynkiem bez twardej informacji, obie przegrane. Dokument sam je oznaczył jako "przewagę niepotwierdzoną" i wykluczył z kuponów, więc ostatni krok zadziałał; sama wycena `football-analyst` dla Under/BTTS nie powyżej rynku jest do obserwacji (2 przypadki, ale 02.11 Under 2,5: 2/3 trafione).
- **SJS +1,5 (p 69,2%, kupon 1), 2-7:** Askarov (wcześniej .901) wpuścił 7; dokument oznaczył "przewaga niepotwierdzona +7,3 pp" i skorygował stawkę do 0,1%. Reguła z 02.11 zadziałała; samo pudło to **wariancja**. Obserwacja z 04.11 (stawka z p modelu przy przewadze > 5 pp) nie powtórzyła się: stawka była już korygowana.
- **HOU ML (72%, kupon 2), 107-117:** dokument opisał Adamsa out i Capelę DTD, p ≈ rynek (fair 1,39 vs kurs 1,37), więc nie błąd wyceny; **wariancja**. Kupon 2 miał EV zależne od kursu Pinnacle (u Betclic FR EV ujemny).
- **MEM ML (67,5%), 103-107; PSV 1X (70,3%), 1-2; Liverpool (63%), 2-3 w Stambule:** **wariancja**, p blisko rynku, nic znanego przed meczem.
- **Wykluczenia:** Over 1,5 w LM 3/3 i Over 2,5 2/2 (9 goli Como, 5 w Lipsku) to zgodne z listą trafienia; brak błędnych wykluczeń.

## Co zadziałało
- Piłka DC i 1X2: 7/8 w LM (DC 4/5, 1X2 3/4), Over 1,5 3/3 (p 74-81%), Over 2,5 2/2, BTTS tak 1/1; oba kupony LM z K1-K2 trafione.
- NBA moneyline faworytów 6/8 (oczekiwane 5,9), p 80%+ 5/5 (LAL, NYK, SAS, Lipsk DC 12, Lens Over 1,5).
- Puck line +1,5 NHL 2/3 (OTT, CGY trafione), razem od 29.10 dalej powyżej oczekiwań.
- Korekty "przewaga niepotwierdzona" w stawce (0,1%/0,7%) ograniczyły skutek dwóch przegranych kuponów.

## Kalibracja skilli
- **`tennis-analyst` (Skalibruj, punkt "Faworyt po wolnym losie"):** dopisano regułę z liczbą: w Masters/WTA 1000 R2 bez statystyk serwisu odejmij **6-8 pp** (zamiast 3-5), ogranicz p do ~68% i nie dawaj takiego faworyta do kuponów. Uzasadnienie w nawiasie: weryfikacja 05.11 (de Minaur 77%, Zverev 64% przegrali mimo korekty 4-5 pp) i bilans 1/6 od 14.10 (Sabalenka, Pegula, Rublev, de Minaur, Zverev przegrali, Świątek wygrała).
- Pozostałe skille: **bez zmian**. Pudła piłkarskie i NBA/NHL to wariancja lub nogi już oznaczone ostrzeżeniem i ściągnięte w stawce; `bet-slip-builder` zadziałał zgodnie z regułą 02.11.

## Do obserwacji
- **Tenis po wolnym losie w R2 po nowej korekcie 6-8 pp:** czy faworyci z p ≤ 68% wracają do oczekiwanych wyników; warunek ponownej zmiany: kolejne 4+ takich nóg z trafieniem < 40%.
- **`football-analyst`: p dla Under/BTTS nie powyżej rynku o > 5 pp bez twardej informacji:** 04.11 0/2 (Real BTTS nie +11 pp, Porto U2,5 +6,6 pp), 02.11 Under 2,5 2/3. Warunek: kolejna seria < 40% przy ~10 nogach → ściągnięcie p do rynku +5 pp w `football-analyst` także poza trybem EV.
- **Nogi "przewaga niepotwierdzona":** 04.11 1/4 (OTT trafione, SJS, Real BTTS nie, Porto U2,5 przegrane); razem z 26-28.10 (53% przy 65%) i 03.11 (STL +1,5 ✗) jest to stały wzorzec niższy od p, ale ujęty w stawkach 0-0,7%.
- **Dane:** wyniki z jednego źródła (ESPN, NHL API); do uzupełnienia: LAC - MIA (noga #12 listy) oraz Ekstraklasa 02.11; Kouamé - Davidovich Fokina unieważnione (sprawdzić, skąd błędny rywal w terminarzu tenisowym).

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
