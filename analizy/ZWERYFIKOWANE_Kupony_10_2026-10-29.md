# Kupony 29.10.2026 wieczór/noc (wydarzenia od 21:30) - wynik: 6 kuponów (poziom luzowania 1-2), wszystkie EV < 0

**Kursy:** Betclic.pl, pobrane ok. 20:15-20:45 (źródło: `Kursy_Betclic_2026-10-29.md` i strony meczów NHL). **Nie sprawdzano gg397.bet** (kupony mają EV < 0 i stawkę 0%, więc weryfikacja nic nie zmienia; do zrobienia, jeśli wejdziemy w tryb EV).
**Analizy:** `Analiza_pilka_`, `Analiza_NBA_`, `Analiza_NHL_cz1_`, `Analiza_NHL_cz2_`, `Analiza_esport_2026-10-29.md`.
**Zakres:** 18 meczów (piłka 3, LoL 1, NBA 3, NHL 11). Poza kuponami: Vancouver-San Jose (brak na Betclic), TES-BLG (brak kursów Betclic). Wykluczone na życzenie: wszystko przed 21:30.

## Wynik wyceny

- Poziom 0 (EV>0, p>50%, kurs 1.5-2.5, 2 nogi >1.2): **0 kuponów**. Wszystkie 87 nóg z p>50% i fair>1.15 mają EV ujemne (najlepsza: MEM +17,5 EV -0,6%).
- Poziom 1 (EV ≥ -5%): **1 kupon**.
- Poziom 2 (bez limitu EV, ranking po p): **6 kuponów** łącznie. Więcej nie powstaje bez łamania zasad (jeden mecz = jedna noga w kuponie, każda noga w jednym kuponie).
- Żadna noga nie ma przewagi nad Betclic. Marża Betclic (5-9%) zjada różnicę. Stawka każdego kuponu: **0%**.

## Kupony

| # | Poziom | Nogi (godz. PL, kurs Betclic) | p | Kurs | EV | Stawka |
|---|---|---|---|---|---|---|
| 1 | 1 (EV ≥ -5%) | CLE +11,5 (ATL-CLE, 01:00) @1,23 + MEM +16,5 (POR-MEM, 03:00) @1,24 | 63,9% | 1,53 | -2,5% | 0% |
| 2 | 2 | VAS-FLA X2 (00:00) @1,21 + SAC +14,5 (NO-SAC, 01:00) @1,24 | 59,8% | 1,50 | -10,3% | 0% |
| 3 | 2 | CAR lub remis 60' (CAR-CBJ, 00:00) @1,22 + ATM-CRU 12 (23:30) @1,27 | 55,8% | 1,55 | -13,5% | 0% |
| 4 | 2 | TB lub remis 60' (TBL-WPG, 00:00) @1,26 + GRE-CAP 12 (01:30) @1,28 | 52,9% | 1,61 | -14,8% | 0% |
| 5 | 2 | STL-BOS Over 4,5 gola (01:00) @1,24 + LAK-OTT Over 4,5 gola (03:00) @1,25 | 51,1% | 1,55 | -20,8% | 0% |
| 6 | 2 | TBL-WPG Over 4,5 gola (00:00) @1,22 + VAS-FLA Over 1,5 gola (00:00) @1,24 | 51,0% | 1,51 | -22,9% | 0% |

Źródło wszystkich kursów: Betclic.pl. Kupony 2 i 6 używają VAS-FLA (rynki z różnych rodzin: wynik / gole).

## Ostrzeżenia

- **Poziomy 3-6** nie były stosowane. Tryb EV (-1/-2) zastosowano za zgodą użytkownika, patrz sekcja poniżej; nogi z dodatnim EV leżą po stronie p < 50% i część jest oznaczona "przewaga niepotwierdzona".
- Handicapy NBA (p z modelu normalnego, SD 12,5 / 18,5; próba 3-5 meczów, pewność niska). Linie Betclic nietypowe względem DraftKings.
- p w NHL: ML i total z `nhl_model.py` (Poisson), totale z λ analityka (dla cz1 odtworzone z p Over 5,5/6,5). 60' w cz2 ma remisy 16-17% (Poisson zaniża), w cz1 skorygowane do 19%.
- Niepotwierdzeni bramkarze: Wallstedt (MIN), Husso (ANA), Ellis (BUF), Vejmelka (UTA), Lindgren (WSH), Kochetkov (CAR), Knight (CHI). Nogi CAR/TBL/STL-BOS/LAK-OTT zależą od bramkarza.
- Handicap TB ±1,5 na Betclic (2,57 / 1,75) jest niejednoznaczny, więc pominięty.
- Założenie niezależności meczów; kursy mogą się zmienić do startu.

---

# Tryb EV (poziomy -1 i -2) - za zgodą użytkownika, 29.10.2026

Zasady: EV > 0 każdej nogi (kursy Betclic z 20:15-20:45), bez progów p i kursu, fair nogi > 1.15. Nogi z p > p rynku (po devigu) o ponad 5 pp bez twardej informacji = **"przewaga niepotwierdzona"**; ich stawka Kelly 1/4 liczona z p ściągniętego do p rynku + 5 pp. **gg397.bet nie sprawdzano** - kursy do potwierdzenia przed postawieniem.

| # | Poziom | Noga(i) (godz. PL, kurs Betclic) | p (po korekcie) | Kurs | EV (po korekcie) | Stawka (Kelly 1/4) |
|---|---|---|---|---|---|---|
| E1 | -1 | ANA-BUF Under 4,5 gola (03:00) @4,75* + TBL-WPG Under 4,5 gola (00:00) @3,85* | 7,8% (7,1%) | 18,29 | +41,8% (+30,2%) | 0,44% |
| E2 | -1 | CAR-CBJ Under 4,5 gola (00:00) @3,70* + DAL-MTL Under 4,5 gola (01:00) @3,70 | 9,1% (9,0%) | 13,69 | +24,9% (+23,1%) | 0,46% |
| E3 | -1 | DET-CHI Under 4,5 gola (00:30) @3,50* + MIN-NYI Under 4,5 gola (01:00) @3,50* | 12,0% (9,9%) | 12,25 | +46,5% (+21,3%) | 0,47% |
| E4 | -2 | NSH-WSH Under 4,5 gola (01:00) @4,25 | 25,9% | 4,25 | +10,1% | 0,78% |
| E5 | -2 | NO-SAC Suma pkt Under 226,5 (01:00) @3,10* | 36,4% (35,2%) | 3,10 | +13,0% (+9,1%) | 1,08% |
| E6 | -2 | STL-BOS Under 4,5 gola (01:00) @3,60 | 29,2% | 3,60 | +5,1% | 0,49% |
| E7 | -2 | POR-MEM MEM wygra z ML (03:00) @3,18 | 33,0% | 3,18 | +4,9% | 0,57% |
| E8 | -2 | ATL-CLE Suma pkt Under 227,5 (01:00) @3,16 | 32,5% | 3,16 | +2,7% | 0,32% |
| E9 | -2 | ATM-CRU BTTS Nie (23:30) @2,32* | 46,0% (44,3%) | 2,32 | +6,7% (+2,7%) | 0,51% |
| E10 | -2 | VAS-FLA BTTS Nie (00:00) @1,93 | 52,0% | 1,93 | +0,4% | 0,10% |

`*` = przewaga niepotwierdzona (p modelu > p rynku + 5 pp).

## Ostrzeżenia trybu EV

- **7 z 10 pozycji to jedna hipoteza:** Under 4,5 gola w NHL z modelu Poissona (λ sum 5,6-6,2). Model daje 26-35% przy 20-27% implikowanych przez Betclic. Jeśli NHL w tę noc rzuci 5+ goli, padną razem (korelacja). Poisson może zawyżać ogon dolny; weryfikacje 26-28.10 dla nóg "przewaga niepotwierdzona": 53% trafień przy p modelu ok. 65%.
- E1-E3 to dwunogowe z łącznym p 8-12% (wariancja bardzo wysoka). Ich kurs 12-18.
- NBA: p z modelu normalnego (SD 12,5 / 18,75, próba 3-5 meczów, pewność niska); linie Betclic niższe od DraftKings o ok. 10 pkt, więc Under zależy od poprawnej linii.
- Niepotwierdzeni bramkarze: Wallstedt (MIN), Husso (ANA), Ellis (BUF), Vejmelka (UTA), Lindgren (WSH).
- Suma stawek ok. 5% bankrolla przy zakładanym EV ok. +5-10%; przy tej wariancji to wartość oczekiwana, nie prognoza.
