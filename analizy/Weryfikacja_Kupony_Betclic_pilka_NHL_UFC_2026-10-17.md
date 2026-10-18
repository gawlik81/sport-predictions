# Weryfikacja kuponów Betclic z 17.10.2026 (piłka, NHL, UFC)

Zweryfikowane pliki:
- `ZWERYFIKOWANE_Kupon_pewniaki_Betclic_2026-10-17.md` (akumulator 5 nóg, DC/1X2)
- `ZWERYFIKOWANE_Kupony_jednomeczowe_Betclic_2026-10-17.md` (5 kuponów MyCombi)
- `Kupony_NHL_noc_Betclic_2026-10-17.md` (5 kuponów NHL/UFC + typy poza kuponami z UFC, NHL, J1)

Źródła wyników: ESPN scoreboard (piłka, NHL, J1, UFC). Wyniki UFC z jednego źródła (ESPN; API UFC zablokowane bot-challenge). Rozliczenie NHL: gole drużyn i total wg wyniku końcowego z dogrywką (zgodnie z etykietą Betclic); wszystkie nogi NHL rozstrzygają się tak samo także bez gola dogrywki/karnych (Buffalo 3 gole, San Jose 3, MTL-BUF 7 goli, bez gola OT 6 > 5,5).

**Nierozliczone:** Machida - Avispa Fukuoka (J1, 09:00 PL) według ESPN jeszcze się nie odbył; typ "Machida lub remis" (p 76%) był tylko w tabeli analizy, nie w kuponie. Buckley - Malott Over 2,5 rundy: brak źródła rundy zakończenia, nie rozliczono. Dlatego `Kupony_NHL_noc` **nie dostaje prefiksu** (weryfikacja częściowa); dwa pozostałe pliki są rozliczone w całości.

## Wyniki

- Piłka: Espanyol 0-1 Atlético; Strasbourg 1-3 PSG; Bologna 1-3 Inter; Betis 2-5 Barcelona; Bayern 6-1 Leipzig; Man City 3-2 Ipswich; Roma 2-0 Genoa.
- NHL: Florida 8-3 Seattle; Islanders 4-1 w Toronto; Montréal 4-3 Buffalo (OT); Detroit 4-3 San Jose (karne); Columbus 1-0 Rangers (OT); Chicago 0-4 Dallas; Philadelphia 3-1 Ottawa; LA 1-4 Boston; Utah 2-6 Edmonton.
- UFC Edmonton: You, Chandler, Koslow, Cerminara, Faglier, Galanti, **Boser (nad Dinizem)**, Nallo, Cuamba, Barriault, Pérez, Jasudavicius, Malott.
- J1: Okayama 0-3 Kobe.

## Kupony

| Kupon | Nogi | Kurs | p | Wynik |
|---|---|---|---|---|
| Pewniaki | 5 x DC/1X2 (wszystkie ✅) | 2,06 | 36,1% | ✅ |
| Jedn. 1 | Barcelona + Over 1,5 Barcy (5 goli) | 1,51 | 60% | ✅ |
| Jedn. 2 | Atlético wygra | 1,63 | 55% | ✅ |
| Jedn. 3 | City Over 2,5 (3 gole) | 1,69 | 52% | ✅ |
| Jedn. 4 | Inter Over 1,5 (3 gole) | 1,52 | 58% | ✅ |
| Jedn. 5 | Roma wygra | 1,57 | 58% | ✅ |
| NHL 1 | Seattle O1,5 ✅ + Boston O1,5 ✅ | 1,59 | 70,7% | ✅ |
| NHL 2 | Islanders O1,5 ✅ + Rangers O2,5 ❌ (0 goli) | 1,92 | 53,6% | ❌ |
| NHL 3 | Chicago O1,5 ❌ (0 goli) + Diniz ❌ | 1,93 | 53,4% | ❌ |
| NHL 4 | MTL-BUF O5,5 ✅ + Philadelphia O1,5 ✅ | 1,97 | 49,7% | ✅ |
| NHL 5 | Buffalo O2,5 ✅ + San Jose O1,5 ✅ | 1,92 | 50,9% | ✅ |

Bilans: **9 z 11 kuponów przy oczekiwanych 5,97** (suma p). Nogi: 16/19 przy 13,46 (+1,33 odch. std.).

Uwaga o danych: dokument NHL nie podaje p pojedynczych nóg Seattle O1,5, Islanders O1,5 i Philadelphia O1,5, więc wyprowadziłem je z p kuponu podzielonego przez p drugiej nogi (83,3%, 82,3%, 76,5%). Kupon NHL 5 rozliczono jako jedną parę (p 50,9%), bo p nóg osobno nie ma w dokumencie. Nie zmieniałem żadnych p ani kursów z dokumentów.

Hipotetyczny zysk przy stawce 1 na kupon: **+4,46** (pewniaki +1,06; jednomeczowe +2,92; NHL +0,48). Zalecane stawki: pewniaki 0%, jednomeczowe 0%, NHL 1-3: 5,2% / 0,9% / 0,8% bankrolla (1/4 Kelly), NHL 4-5: 0%. Przy tych stawkach wynik NHL 1-3 to hipotetycznie ok. +1,4% bankrolla. Wszystko to informacja, nie dowód przewagi.

## Typy spoza kuponów (hipotetycznie)

- **UFC zwycięzca: 7/13 przy oczekiwanych 8,55** (-0,9 odch. std.). Pudła: Blanchfield (72%), Croden (72%), Daukaus (63%), Jourdain (62%), Chovancek (53%), Diniz (68%). Dokument słusznie odrzucił wszystkie walki jako EV < 0 i p opierał na rynku, bez własnych statystyk.
- NHL: Seattle Over 2,5 (62,7%) ✅, Boston Over 2,5 (65,4%) ✅, Utah - Edmonton Over 5,5 (65,7%) ✅ (8 goli). 3/3 przy 1,94. Dokument oznaczył je jako EV > 0 lub EV -1,4% (UTA-EDM).
- J1: Okayama - Kobe Under 2,5 (57%) ❌ (0-3). Dokument sam nazwał go "najmniej ujemnym", EV -2%.

## Analiza pomyłek

- **Columbus - Rangers 1-0 OT (NHL 2, Rangers Over 2,5, p 65,1%):** wariancja. Wynik z jednym golem (Rangers 0) mimo λ Rangers 3,35; p 65% oznacza ok. 35% pudeł i żadna informacja przedmeczowa w dokumencie go nie zapowiadała.
- **Chicago - Dallas 0-4 (NHL 3, Chicago Over 1,5, p 78,5%):** dokument sam zaznaczył "Dallas ma najlepszą obronę ligi w próbie (13 straconych w 7 meczach), więc to najcieńszy edge", ale liczba (78,5%) została bez korekty, a EV +2,8% wynikało z tej jednej nogi. To pojedynczy przypadek "sygnał ryzyka opisany, liczba bez zmian" w nowym skillu NHL; shutout to ok. 20% scenariusz, więc samo pudło to wariancja, ale ten wzorzec jest wart licznika (patrz Do obserwacji). Noga Diniz w tym kuponie miała EV ≈ 0 i p wzięte z rynku: została dołożona tylko po to, by zbudować kupon w widełkach kursu.
- **Boser - Diniz (UFC):** Boser wygrał mimo p 32%; wariancja. Karta była bez własnych statystyk, p z rynku.
- **Okayama - Kobe 0-3 (J1):** dokument ostrzegał o rotacji Kobe (57% XI) i o poprzednim wyniku 3-0 dla Okayamy w maju; Under 2,5 przegrał przez 3 gole Kobe. Wariancja (p 57%).

## Co zadziałało

- Wszystkie 10 piłkarskich nóg (pewniaki + MyCombi) trafiło: dzień wysokich wyników (Bayern 6-1, Barcelona 5-2, City 3-2) i brak niespodzianek (remisy tylko w meczach bez typu: Villarreal - Elche, Valencia - Athletic, Lille - Brest, Union - BVB, Bremen - Paderborn).
- Odrzucone w kuponach jednomeczowych: Atlético Under 2,5 (rynek vs model λ) i BTTS Nie przegrałyby (Espanyol 0-1: Under 2,5 ✅, BTTS Nie ✅ - po fakcie trafiłyby; zasada "nie schodź pod rynek bez konkretów" nie została złamana, ale to kolejny przykład, że λ modelu poniżej rynku bywa zasadna; jedna próbka).
- Pewniaki: kupon wszedł (5/5), ale EV -25,5%, więc zgodnie z dokumentem brak zalecanej stawki; to wariancja (p całości 36%), nie dowód, że warunki były sensowne.
- Wniosek dokumentu NHL "jedyne nogi z EV > 0 to Over na gole drużyny" potwierdził się częściowo: 5/7 nóg tego typu przy oczekiwanych 5,2 oraz 3/3 typów poza kuponami.

## Kalibracja skilli

**Bez zmian w skillach.** Uzasadnienie: bilans kuponów (9/11 przy 5,97) i nóg (16/19 przy 13,46, +1,3 odch. std.) mieści się w wariancji; nadwyżka trafień pochodzi z piłki (10/10 przy 6,9; MyCombi sam +1,96 odch. std., ale p 50-60% w jednym dniu), co jest jedną kolejką bez wspólnej przyczyny. Pudła NHL i UFC to pojedyncze wyniki o p 21-47%. Skille NHL i UFC są nowe i każdy wzorzec ma po jednej próbce.

## Do obserwacji

- **Piłka: nogi MyCombi/Over i wygrane faworyta 17.10 wszystkie trafione** (5/5 przy 2,83). Poprzednie weryfikacje (16.10) miały Over'y poniżej oczekiwań; po zsumowaniu nie ma kierunkowego odchylenia. Nie zmieniać `football-analyst`.
- **NHL: sygnał ryzyka bez zmiany liczby (licznik 1):** Chicago Over 1,5 vs najlepsza obrona ligi. Jeśli powtórzy się w kolejnej weryfikacji NHL (nogi z opisanym ryzykiem rywala przy p bez korekty), dopisać do `nhl-analyst` regułę: przy rywalu z top-3 obroną w próbie obniż λ drużyny o 0,1-0,2 gola i przelicz p.
- **NHL: Over na gole drużyny** po tej kolejce 5/7 (nogi kuponów) i 3/3 (poza kuponami); próba 10 nóg, za mała na korektę globalną. Cel: po ok. 30 nogach ocenić, czy p dla tej grupy jest zawyżone/zaniżone.
- **UFC (karta bez statystyk, p z rynku):** 7/13 przy 8,55 (wszystkie walki poza kuponami + Diniz); zbyt mało do wniosków. Zapisać licznik dla UFC Fight Night: kolejna gala z "p = rynek minus marża" pokaże, czy jest systematyczny błąd.
- **Dane:** wyniki UFC z jednego źródła (ESPN); Machida - Fukuoka i Over 2,5 rundy Buckley - Malott do uzupełnienia, po czym dodać prefiks `ZWERYFIKOWANE_` do `Kupony_NHL_noc_Betclic_2026-10-17.md`.

To oszacowania, nie gwarancje; próba jednego dnia jest mała.
