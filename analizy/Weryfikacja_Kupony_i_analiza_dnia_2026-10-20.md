# Weryfikacja kuponów i analizy dnia 20.10.2026 (LM, NBA, NHL, tenis ATP)

**Zweryfikowane pliki:**
- `ZWERYFIKOWANE_Kupony_10_2026-10-20.md` (dawniej `Kupony_10_2026-10-20.md`) - 5 kuponów, wszystkie nogi rozstrzygnięte -> prefiks `ZWERYFIKOWANE_`.
- `ZWERYFIKOWANE_Analiza_dnia_2026-10-20.md` (dawniej `Analiza_dnia_2026-10-20.md`; uzupełnione 22.10 w `Weryfikacja_Kupony_i_analiza_dnia_2026-10-21.md`) - **weryfikacja częściowa**: NHL VGK - TBL w chwili weryfikacji nierozstrzygnięty (TBL 6-2, 3. tercja, ok. 7 min do końca; Under 6.5 przegrany już po 7 golach, ale ML, wynik po 60' i puck line otwarte). Plik bez prefiksu do czasu uzupełnienia.
- Uzupełnienie z 19.10: WTA Osaka Boulter - Sakatsume 6-3 6-1 (Boulter) -> typ trafiony, `Analiza_dnia_2026-10-19.md` dostaje prefiks.

**Źródła wyników:** ESPN scoreboard (LM, NBA, NHL, tenis), NHL API (api-web.nhle.com) dla NHL. Wszystko z 1-2 źródeł (NHL: ESPN + NHL API zgodne); tenis i NBA tylko ESPN (jedno źródło). Gospodarze wg pola `homeAway`.

## Wyniki
- **LM (90'):** Roma 4-0 Slovan; Porto 0-1 PSV; Liverpool 4-3 Villarreal; Man City 5-1 AEK; Napoli 4-3 Bodo/Glimt; PSG 4-2 Barcelona; Stuttgart 1-1 Atlético. (Pominięte w analizie: Fenerbahce 2-2 Slavia, Sabah 1-2 Dortmund.)
- **NBA:** DET 121-113 BOS; NY 100-106 PHI; SA 104-116 OKC.
- **NHL (po 60'):** MTL-SJ 3-3 (SJ 4-3 w dogr.); NJ 4-3 COL; NYI 3-2 ANA; WSH 2-5 LAK; CBJ 2-6 TOR; STL 2-1 WPG; DAL-BOS 2-2 (DAL 3-2 w dogr.); EDM-MIN 3-3 (EDM 4-3 w dogr.); SEA-DET 3-3 (SEA 4-3 po karnych); VAN 3-6 CAR; VGK-TBL nierozstrzygnięty.
- **Tenis ATP:** Collignon d. Basavareddy 3-6 6-3 6-4; Jacquet d. Berrettini 7-6 7-5; Nakashima d. Medjedovic 7-6 6-7 6-2.

## Kupony (stawka 0% wszędzie)
| Kupon | Nogi | Kurs | p | EV | Wynik |
|---|---|---|---|---|---|
| 1 | Atlético lub remis ✅ (1-1) + WSH lub remis 60' ❌ (LAK 5-2) | 1,78 | 54,6% | -2,7% | ❌ |
| 2 | PHI +9.5 ✅ + NJ-COL 12 ✅ + EDM-MIN 12 ❌ (3-3 po 60') | 2,05 | 47,4% | -2,7% | ❌ |
| 3 | OKC +6.5 ✅ + DAL-BOS 12 ❌ + SEA-DET 12 ❌ (oba po 60' remis) | 2,00 | 47,0% | -6,1% | ❌ |
| 4 | PSG lub Barca ✅ + STL-WPG 12 ✅ + CBJ-TOR 12 ✅ | 1,70 | 54,2% | -7,9% | ✅ |
| 5 | VAN-CAR U6.5 ❌ (9 goli) + NYI-ANA 12 ✅ | 2,24 | 54,5% | +21,9% (niepotw.) | ❌ |

**Kupony: 1/5 przy oczekiwanych 2,58.** Hipotetyczny zysk przy stawce 1: -3,30 (informacyjnie; zalecana stawka 0%).

## Nogi (skrypt verify.py)
**18/25 przy oczekiwanych 18,24 (-0,11 odch. std.), Brier 0,201** (13 nóg z puli kuponów + 12 hipotetycznych poza kuponami).
- Pula kuponów (13): 8/13, oczekiwane ok. 10,4.
- NHL "12 po 60'": **4/7 przy 5,83 (-1,86 odch. std.)**; NBA spread 2/2 (1,35).
- Hipotetycznie poza kuponami: piłka 1X2/DC/BTTS/Over 7/7 (przy oczekiwanych 5,4; kursy 1,08-1,21, fair ≤ 1,15 lub EV mocno ujemny - wykluczenia słuszne ze względu na kurs); piłka Under 2.5 1/2 (Napoli ❌ 4-3, Stuttgart ✅); tenis (strona z p ≥ 52%) 2/3 (Basavareddy ❌); CAR ML ✅.

## Analiza pomyłek
- **NHL "12 po 60'" (nogi g, h, i):** trzy remisy po 60' (EDM-MIN, DAL-BOS, SEA-DET) w jednym dniu; razem z MTL-SJ 4 z 11 meczów skończyło się remisem po 60' (36%) przy modelu ~16-17% (oczekiwane ok. 1,8). P(≥4 z 11 przy 16,5%) to ok. 8%. **Wariancja**, bez wiarygodnego sygnału przed meczami; model remisu pochodzi z rozkładu goli, więc jeden dzień niczego nie dowodzi. Ale wszystkie trzy porażki kuponów 2-3 to ta sama korelowana klasa nóg (każdy kupon miał 1-2 takie nogi), a seria kuponów z "12" w NHL ma strukturalnie p ≈ 0,83^n.
- **WSH lub remis 60' (p 73,8%):** LAK 5-2 wygrało w regulaminowym czasie. Dokument sam opisywał przewagę +8 pp nad rynkiem jako "niepotwierdzoną" i Kuemper był niepotwierdzony; kupon 1 miał EV -2,7% i stawkę 0%. **Wariancja z elementem ryzyka znanego** (p wyższe od rynku o 8 pp bez twardej informacji, dokument to oznaczył, ale noga i tak weszła do kuponu). Licznik: nogi "przewaga niepotwierdzona" 19.10: 5/7; dziś: WSH ❌, VAN-CAR U6.5 ❌ (0/2).
- **VAN-CAR Under 6.5 (p 65,9%, kurs z gg397.bet, +16 pp nad rynkiem):** 9 goli. Dokument ostrzegał, że EV pochodzi z p wyższego od rynku o 16 pp, i nie rekomendował stawki. **Wariancja + ostrzeżenie zadziałało** (stawka 0%), ale noga to też przykład reguły "p różne od rynku o > 5 pp bez twardej informacji" (zastosowanej w opisie, nie w liczbie; patrz Do obserwacji).
- **Gole w LM:** w 7 meczach padły 33 gole (średnio 4,7 na mecz vs suma λ w analizie 2,6-3,6). Over 2.5 trafił 5/7 przy oczekiwanych 4,03; Napoli U2.5 (4-3) przegrał. Analiza sama pisała, że Betclic wycenia 2.5+ goli wyżej niż model ("λ mogą być zaniżone") - **jeden dzień, wariancja**, zapisane w obserwacjach.
- **Basavareddy (p 52%):** Collignon wygrał w 3 setach, niska pewność, bez kursu i poza kuponami. Wariancja.

## Co zadziałało
- Uczciwy komunikat "5 kuponów, nie 10; poziom 0 daje 0 kuponów", wszystkie stawki 0%; kupon 5 z EV +21,9% przegrał, a dokument słusznie nie ufał temu EV.
- Odrzucenie typów z fair ≤ 1,15 i EV ujemnym (Roma, City itd. trafiły, ale po kursach 1,08-1,11 to nie value).
- NBA: PHI +9.5 i OKC +6.5 trafione (2/2, obie linie przeliczone na linię Betclic, a nie z DraftKings).
- Kupon 4 (p 54%) trafił.

## Kalibracja skilli
**Bez zmian.** Brak konkretnego błędu procesu: bilans nóg 18/25 vs 18,24 jest zgodny z oczekiwaniami, a pudła to remisy po 60' w NHL (wariancja, p remisu ok. 16-17% w każdym meczu) i dwie nogi z nieujętą w liczbie przewagą nad rynkiem, które dokument sam oznaczył jako niepotwierdzone.

## Do obserwacji
- **NHL remis po 60':** licznik startuje 20.10: 4/11 meczów z remisem po 60' (oczekiwane ok. 1,8). Jeśli w kolejnych weryfikacjach łącznie ≥ 30 meczów pokaże częstość remisu > 24% (oczekiwane ~16-17%), podnieść P(remis) w `nhl-analyst` (skrypt nhl_model.py) i obniżyć p dla "12 po 60'". Do tego czasu w kuponach nie łączyć więcej niż 2 nóg "12 po 60'" (korelacja przez wspólny wzorzec remisu) - rozważyć w `bet-slip-builder`, jeśli się powtórzy.
- **Nogi "przewaga niepotwierdzona" (+5 pp i więcej nad rynkiem) w kuponach:** 19.10: 5/7, 20.10: 0/2 (WSH lub remis, VAN-CAR U6.5) -> łącznie 5/9 przy oczekiwanych ok. 6,2. Za mało, by zmieniać regułę.
- **Faworyci NHL po b2b:** COL w NJ-COL (b2b, p modelu na COL+1.5 70%) przegrał 3-4 w regulaminowym czasie (dla "12" noga trafiła); licznik z 19.10 (0/2) bez nowego przypadku wymagającego p wyżej.
- **Gole w LM (faza ligowa, kol. 3):** Over 2.5 5/7 (oczekiwane 4,03), średnia 4,7 gola/mecz; zbadać po kolejnych kolejkach LM, czy λ faworytów (Roma 3,0, City 2,9) są zaniżone.
- **Do uzupełnienia:** NHL VGK - TBL (po zakończeniu) -> prefiks `ZWERYFIKOWANE_` dla `Analiza_dnia_2026-10-20.md` (zrobione 22.10). Nadal otwarta noga CS2 FURIA - BetBoom Over 69,5 rund z `Kupony_10_2026-10-18.md`.
- Jakość danych: ESPN (jedno źródło) dla NBA, LM i tenisa; NHL: ESPN + NHL API.

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
