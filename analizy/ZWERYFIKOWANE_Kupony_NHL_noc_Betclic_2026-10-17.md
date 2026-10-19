# Analiza i kupony: noc 17→18.10.2026 i poranek 18.10 (kursy Betclic.pl, czas polski)

Zakres: NHL (12 meczów), UFC Fight Night Edmonton (13 walk), J1 League (2 mecze rano). Pominięte: VAN-TBL i CAR-WPG (już trwały przy pobieraniu kursów), NBA (brak meczów, sezon od 20.10), tenis i CS2 (nie dało się zweryfikować par ani godzin).

## Wniosek wstępny

Betclic ma marżę ok. 6-10% na wszystkich trzech sportach i niemal zawsze wycenia gorzej niż konsensus rynkowy (DraftKings/FanDuel). Po analizie **jedyne typy spełniające wszystkie warunki (kurs nogi > 1,2, p > 50%, EV > 0) to Over na gole drużyny w NHL**. W UFC i J1 nie znalazłem nogi z EV > 0 i p > 50%, więc żadna z nich nie weszła do kuponów. Kupony mają po 2 nogi i **bez powtórzeń predykcji między kuponami**. Przy tym warunku tylko kupony 1-3 mają EV > 0; kupony 4 i 5 mają EV ujemne (patrz niżej i sekcja "Co zrelaksować").

## Kupony (min. 2 nogi, łączny kurs 1,5-2,0)

| # | Nogi | Kurs | p | EV | Stawka (1/4 Kelly) |
|---|---|---|---|---|---|
| 1 | Seattle Over 1,5 gola (1,28) + Boston Over 1,5 gola (1,24) | 1,59 | 70,7% | +12,2% | 5,2% bankrolla |
| 2 | NY Islanders Over 1,5 gola (1,21) + NY Rangers Over 2,5 (1,59) | 1,92 | 53,6% | +3,2% | 0,9% |
| 3 | Chicago Over 1,5 (1,31) + Diniz wygra z Boserem (UFC, 1,47) | 1,93 | 53,4% | +2,8% | 0,8% |
| 4 | Montréal-Buffalo Over 5,5 gola w meczu (1,53) + Philadelphia Over 1,5 (1,29) | 1,97 | 49,7% | -1,9% | 0% (EV < 0) |
| 5 | Buffalo Over 2,5 (1,57) + San Jose Over 1,5 (1,22) | 1,92 | 50,9% | -2,4% | 0% (EV < 0) |

- Zasada: żadna predykcja nie występuje w dwóch kuponach (8 nóg w kuponach 2-5 różni się od siebie i od nóg kuponu 1). Ponieważ w NHL jest tylko kilka nóg z EV > 0, a kupon 1 zajął Seattle i Boston, kupony 4 i 5 **nie spełniają warunków EV > 0 (kupon 4 także p > 50%)**. Zostawiłem je, bo prosiłeś o 5 kuponów bez powtórzeń; sugerowana stawka to 0%, a jeśli chcesz je grać, traktuj jako rozrywkę, nie typy z przewagą.
- Wszystkie "Over X gola" dotyczą bramek danej drużyny lub meczu z dogrywką (zgodnie z etykietą Betclic: "Dogrywka i rzuty karne są wliczane do zakładu").
- Kupon 2: NY Islanders Over 1,5 ma kurs 1,21 i EV -0,3% jako pojedyncza noga; razem z Rangers Over 2,5 zestaw ma EV +3,2% (Rangers to główne źródło przewagi).
- Kupon 3 łączy NHL z UFC (Diniz wygra z Boserem, p 68%, kurs 1,47, EV ≈ 0%; walka o 01:00, rynek bez edge, noga to głównie "neutralna" dla zestawu). Kupon 3 jest jedynym z wejściem z UFC, bo Diniz jest jedyną nogą UFC/J1 z EV ≥ 0.
- Kupon 1 (Seattle + Boston) bez zmian; kupony 4 i 5 używają tego samego meczu (Montréal-Buffalo) z różnymi rynkami.
- Ekspozycja kuponów 1-3 przy 1/4 Kelly to ok. 10% bankrolla.
- Pewność wszystkich typów: niska do średniej (bramkarze niepotwierdzeni, próba sezonu 5-9 meczów).

## NHL (12 meczów)

Metoda: λ z bilansu sezonu (GF/GA) ściągnięte w 80% do średniej ligi 3,15, przewaga własnego lodu +0,1, back-to-back PIT (grał z COL 16.10) i BOS (grał w ANA 16.10) -0,12 gola, rywalowi +0,08. Zwycięzcę uśredniłem z rynkiem 30/70 (rynek efektywny; odchylenia modelu 8-14 pp w FLA-SEA, LAK-BOS i CBJ-NYR to szum małej próby, a nie value). Remis po 60' podniesiony do min. 21%.

| Mecz (godz. PL) | λ gosp./gość | 60' 1/X/2 (blend) | Najlepszy rynek Betclic |
|---|---|---|---|
| Florida - Seattle (00:00) | 3,12 / 3,24 | 47/22/32 | Seattle Over 2,5 gola: p 62,7%, kurs 1,81, EV +13,5% |
| NY Islanders @ Toronto (01:00) | 3,17 / 3,16 | 43/22/35 | brak EV > 0 |
| Montréal - Buffalo (01:00) | 3,40 / 3,26 | 44/22/35 | Over 5,5 gola: p 65%, kurs 1,53, EV 0% |
| Detroit - San Jose (01:00) | 3,16 / 3,03 | 45/22/34 | brak EV > 0 |
| Columbus - NY Rangers (01:00) | 3,10 / 3,35 | 41/22/37 | Rangers Over 2,5: p 65,1%, kurs 1,59, EV +3,5% |
| Chicago - Dallas (01:00) | 2,90 / 3,14 | 29/21/50 | Chicago Over 1,5: p 78,5%, kurs 1,31, EV +2,8% |
| Philadelphia - Ottawa (01:00) | 2,75 / 3,20 | 32/23/45 | brak EV > 0 |
| Nashville - St. Louis (02:00) | 3,16 / 3,23 | 39/22/39 | brak EV > 0 |
| LA Kings - Boston (03:00) | 2,97 / 3,37 | 41/22/37 | Boston Over 2,5: p 65,4%, kurs 1,70, EV +11,2%; Over 1,5: p 84,9%, 1,24, +5,3% |
| Vegas - Pittsburgh (04:00) | 3,55 / 2,93 | 51/21/28 | brak EV > 0 (PIT na B2B, Vegas -1,36 DNB bez EV) |
| Utah - Edmonton (04:00) | 3,39 / 3,29 | 43/22/35 | brak EV > 0 (Over 5,5: p 65,7%, 1,50, EV -1,4%) |

Ryzyka NHL: bramkarze startowi niepotwierdzeni (DailyFaceoff: 1 z 28 przy sprawdzeniu); totale meczu (Over 4,5/5,5) są wycenione drożej niż moje p; Dallas ma najlepszą obronę ligi w próbie (13 straconych w 7 meczach), więc Chicago Over 1,5 to najcieńszy edge.

## UFC Fight Night Edmonton (Rogers Place)

Karta zmieniona względem pierwotnej (zastępstwa: Galanti za Urbinę, Faglier, Stiller za Horth; źródło RG, Hard Rock). Ważenie: według nagłówków Yahoo wszyscy zawodnicy zrobili wagę. Statystyk uderzeń/obaleń brak dla większości walk (UFC MCP zablokowane przez bot-challenge, strony z kartą nie mają danych), więc **p opieram na konsensusie rynku (DraftKings/Hard Rock po zdjęciu marży)** z korektami tylko tam, gdzie mam konkret. Pewność: niska dla wszystkich walk poza main eventem (średnia).

Godziny Betclic (PL): Chovancek-You 23:00, Croden-Chandler 23:20, Koslow-Anheliger 23:40, Cerminara-Stiller 00:00, Faglier-Mahjoub 00:20, Galanti-Leblanc 00:40, Boser-Diniz 01:00, Nallo-Landwehr 02:00, Jourdain-Cuamba 02:20, Daukaus-Barriault 02:40, Nelson-Perez 03:00, Blanchfield-Jasudavicius 03:20, Buckley-Malott 03:40 (Yahoo: main event ok. 04:45).

| Walka | Mój p (zwycięzca) | Kurs Betclic | EV | Uwagi |
|---|---|---|---|---|
| Buckley - Malott (5 rund, półśr.) | Malott 55% | Malott 1,76 | -3% | Malott lepszy w stójce (+1,4 vs +0,8 różnicy uderzeń/min, celność 48% vs 36%, kontrola 82%), Buckley miał 3 porażki przez KO/TKO, ale 2 przegrane z rzędu na punkty z zapaśnikami; linia otwarcia Buckley -300 odwróciła się. Over 2,5 rundy: p 68-70%, kurs 1,34, EV -6% |
| Blanchfield - Jasudavicius (co-main) | Blanchfield 72% | 1,28 | -8% | 11 miesięcy przerwy, wcześniej wycofana kontuzją; Jasudavicius wygrała 6 z 7 |
| Nallo - Landwehr | Nallo 71% | 1,32 | -6% | Landwehr 38 lat, 3 porażki z rzędu przez finisz, schodzi z piórkowej; Nallo przegrał przez finisz z Herbertem |
| Daukaus - Barriault | Daukaus 63% | 1,47 | -7% | Barriault 36 lat, 1 wygrana w 6 |
| Perez - Nelson | Perez 74% | 1,27 | -6% | Perez debiutant (15-2, 12 finiszy), Nelson KO w 2 ostatnich porażkach; RG: pass |
| Jourdain - Cuamba | Jourdain 62% | 1,54 | -5% | debiut Jourdaina w UFC |
| Boser - Diniz | Diniz 68% | 1,47 | ≈ 0% | rynek wyrównany, brak edge |
| Cerminara - Stiller | Cerminara 66% | 1,38 | -9% | Cerminara 37 lat, 2+ lata przerwy (obniżyłem względem rynku 71%), Stiller debiutantka w zastępstwie |
| Croden - Chandler | Croden 72% | 1,28 | -8% | brak danych poza rynkiem |
| Chovancek - You | Chovancek 53% | 1,75 | -7% | brak danych poza rynkiem |
| Koslow - Anheliger | Koslow 60% | 1,59 | -4% | brak danych poza rynkiem |
| Faglier - Mahjoub | Faglier 56% | 1,72 | -3% | zastępstwo Faglier; brak danych |
| Galanti - Leblanc | Galanti 83% | 1,13 | -6% | kurs < 1,15, odpada; Leblanc 17% @ 5,75 ma EV +4,6%, ale p < 50% |

Wniosek UFC: żadna noga nie spełnia warunków; Betclic wycenia zwycięzców o 3-9% gorzej niż konsensus.

## J1 League (rano 18.10)

Dane: ESPN (forma, kursy DraftKings), Betclic. Składy i kontuzje niepotwierdzone (nie znalazłem raportów).

| Mecz (godz. PL) | λ | Moje p | Najlepszy rynek | EV |
|---|---|---|---|---|
| Fagiano Okayama - Vissel Kobe (06:55) | 1,15 / 1,25 | 34/28/38 | Under 2,5: p 57%, kurs 1,72 | -2% |
| Machida Zelvia - Avispa Fukuoka (09:00) | 1,50 / 0,95 | 50/26/24 | Machida lub remis: p 76%, kurs 1,21 | -8% |

Okayama wygrała z Kobe 3:0 w maju (10.05.2026), a Kobe rotuje składem (57% XI z ostatnich 5 meczów); Machida grała w AFC CL Two 3 dni wcześniej, więc możliwa rotacja (Machida 1. w tabeli, Fukuoka 18. według zapisu z września, dane mogą być nieaktualne). Under 2,5 w Okayama-Kobe to najmniej ujemny typ z J1, ale EV < 0.

## Co zrelaksować, żeby kupony objęły UFC i J1

Gdyby kupony miały zawierać nogi z UFC lub J1, trzeba zrelaksować warunek EV > 0. Najmniej ujemne nogi: Okayama-Kobe Under 2,5 (1,72, EV -2%), Faglier ML (1,72, -3%), Malott ML (1,76, -3%), Diniz ML (1,47, ≈ 0%). Nie dodawałem ich do kuponów bez Twojej zgody.

To oszacowania probabilistyczne, nie gwarancje; stawki to sugestia, nie porada finansowa.
