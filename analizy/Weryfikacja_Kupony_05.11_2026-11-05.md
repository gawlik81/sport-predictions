# Weryfikacja kuponów z 05.11.2026 (Liga Europy/Konferencji, noc NBA + NHL 05→06.11, tenis ATP Paryż)

**Zweryfikowane pliki:** `Kupony_10_2026-11-05.md` (piłka: kupony 1-7 poziomu 2, lista 20 poziomu 7, 3 nogi puli z EV+; **w całości**) i `Kupony_10_2026-11-05_v2.md` (noc NBA + NHL: kupony 1-4, lista 20, 2 nogi puli; **w całości**), po zmianie nazwy na `ZWERYFIKOWANE_`. Analizy źródłowe (`Analiza_dnia_2026-11-05.md`, `Analiza_NBA_NHL_noc_2026-11-05.md`) **nie oznaczone**: zawierają LoL Dplus KIA - Bilibili (bo5, 22:00 UTC), którego wyniku nie znalazłem (WebSearch bez wyniku), oraz typy spoza kuponów rozliczane tylko hipotetycznie.
**Źródła wyników:** ESPN scoreboard (Liga Europy, Liga Konferencji, NBA, NHL, ATP; jedno źródło), boxscore ESPN dla Lendeborga. Piłka po 90 minutach; NHL: zwycięzca z dogrywką/karnymi, total bez karnych (liczą się gole z gry i dogrywki).
**Uwaga o danych:** (1) tenis: Alcaraz - Berrettini rozstrzygnięty walkowerem, nogi nie rozliczono. (2) Kursy kuponów to Betclic z 05.11 (gg397.bet niezweryfikowany); p i kursów z dokumentów nie poprawiano.

## Wyniki
- **Liga Europy (18:45):** Milan 0-2 Ferencváros, Anderlecht 2-0 Salzburg, Palace 1-1 Hoffenheim, Levski 1-0 Jagiellonia, Lillestrøm 0-1 Plzeň, NEC 3-1 Omonia, Real Sociedad 1-1 Lyon, Sparta 1-3 Bournemouth. **(21:00):** AZ 1-2 Juventus, Leverkusen 0-1 Marseille, Benfica 3-1 Lech, Celta 1-2 Union SG, Celtic 3-2 Beşiktaş, Hapoel 0-2 OFI, Sturm 2-3 Celje, Sunderland 0-2 Dinamo Zagreb, Torreense 3-2 Ararat.
- **Liga Konferencji (18:45):** AGF 0-0 Braga, Atalanta 1-1 Kairat, Midtjylland 1-6 Ajax, Thun 3-1 Hearts, KuPS 0-0 Gent, Lincoln 1-0 Hajduk, Mjällby 2-0 Borac, Zvezda 2-1 Inter Escaldes, Trabzonspor 0-1 Freiburg. **(21:00):** Monaco 2-0 Nordsjælland, Craiova 2-0 Egnatia, FCK 2-1 Iberia, Lugano 3-0 Žalgiris, Twente 3-1 Pafos, Getafe 0-1 Brighton, Panathinaikos 2-1 CSKA, Riga 1-1 Jablonec, Sint-Truiden 1-1 Brann.
- **NBA:** Suns 117-104 Magic, Warriors 120-100 Heat (Giannis zagrał: 31 min, 20 pkt).
- **NHL:** Canadiens 5-4 Mammoth (dogr.), Red Wings 1-2 Golden Knights, Lightning 4-1 Blackhawks, Devils 5-4 Blues (dogr.), Islanders 3-5 Hurricanes, Rangers 3-2 Flyers, Penguins 2-6 Bruins, Blue Jackets 2-1 Stars (karne), Jets 6-2 Canucks, Oilers 4-5 Ducks, Avalanche 2-3 Predators (dogr.).
- **ATP Paryż R3:** Paul 7-6 6-4 Halys, Shelton 3-6 6-4 7-6 Rinderknech, Van Assche 7-5 3-6 6-4 Musetti, Hijikata 2-6 6-3 7-5 Etcheverry, Borges 6-0 6-2 Buse, Ruud 6-3 6-3 Struff, Fritz 6-3 6-4 Fils, Alcaraz - Berrettini walkower.

## Bilans (skrypt `verify.py`)
| | Trafione | Oczekiwane |
|---|---|---|
| Piłka: lista 20 (poziom 7) | 15/20 | 14,81 (+0,09 odch.) |
| Piłka: kupony 1-7 | 5/7 | 3,78 |
| Piłka: nogi (28 z puli i kuponów) | 20/28 | 20,22 (-0,10 odch.) |
| NBA/NHL: lista 20 (poziom 7) | 15/20 | 14,10 (+0,45 odch.) |
| NBA/NHL: kupony 1-4 | 2/4 | 2,09 |
| NBA/NHL: nogi (22) | 16/22 | 15,23 (+0,36 odch.) |

Kupony piłkarskie: K1 NEC + Levski O1,5 przegrany (Levski 1-0), K2 trafiony (Benfica O2,5 + AGF X2), K3 trafiony, K4 przegrany (KuPS-Gent 0-0), K5, K6, K7 trafione. NBA/NHL: kupon 1 (GSW ML + ANA@EDM O5,5; poziom 0, p 52,2%, kurs 2,10) **trafiony**, kupon 2 (NYR O4,5 + MTL O5,5) trafiony, kupon 3 przegrany przez DAL-CBJ (3 gole), kupon 4 przegrany przez VGK-DET (3 gole).
Hipotetyczny zysk przy stawce 1 na kupon: piłka +0,80, NBA/NHL -0,05 (tylko informacja; piłka i kupony 2-4 NBA/NHL miały zalecaną stawkę 0%; jedyny kupon z dodatnim EV, NBA/NHL kupon 1, zalecał 2,1% bankrolla, co przy trafieniu dałoby hipotetycznie +2,3% bankrolla).

## Typy spoza kuponów (hipotetycznie)
- **Pula piłkarska z EV+:** Anderlecht - Salzburg X2 (p 56,9%, 1,78) przegrany (2-0), Levski - Jagiellonia X2 (p 59,5%, 1,72) przegrany (1-0), Benfica - Lech BTTS tak (p 54,4%, 1,88) trafiony. 1/3 przy 1,71 oczekiwanych; dokument oznaczył je jako "przewaga niepotwierdzona" i nie wpuścił do kuponów, wykluczenie było słuszne.
- **Pula NBA:** GSW Over 118,5 (p 59%, 1,72) trafiony (120 pkt), Lendeborg pkt O19,5 (p ok. 54%, 1,90) przegrany (17 pkt; pewność niska, poza kuponami słusznie).
- **PHX - ORL (bez nóg w kuponach):** PHX ML (p 53,2%) trafiony 117-104, ORL +4,5 (59,5%) przegrany, Under 221,5 (52,2%) trafiony o 0,5 (221 pkt), Over 219,5 trafiony. Wszystkie "niska pewność, bez przewagi", nic z tego nie było rekomendacją.
- **Tenis (analiza dnia, bez kursów Betclic, więc bez nóg):** 4/7 rozliczonych przy 4,42 oczekiwanych: Paul (73%) ✓, Shelton (71,5%) ✓, Ruud (65%) ✓, Borges (57%) ✓, Musetti (70%) ✗, Etcheverry (51,5%) ✗, Fils (53,5%) ✗; Alcaraz (80%) bez rozliczenia (walkower).

## Analiza pomyłek
- **Piłka Over 1,5 w Lidze Europy/Konferencji: 4/8 przy 6,0 oczekiwanych (-1,64 odch.).** Przegrane: Levski 1-0 (p 74,2%), Lillestrøm 0-1 (78,5%), Lincoln 1-0 (75%), KuPS 0-0 (71%). Sygnały w analizach były, ale nie ukryte: KuPS miało Over 2,5 w 20% z 15 meczów, sztuczną murawę i rotację Gent (p 71% już obniżone), Lillestrøm ledwo strzela (nigdy > 1 gola w 7 meczach LE), Plzeň 2 gole w 3 meczach. Modele (Poisson na λ z rynku) dają 78-79% dla λ ok. 2,9, więc liczba wynikała z rynku, nie z pominięcia sygnału; rynek (kursy 1,15-1,24) wyceniał te nogi podobnie. **Ocena: wariancja z lekkim sygnałem "słabo strzelające zespoły niższych lig w jesieni", bez dowodu błędu procesu.** Czwórka to cztery różne mecze, w dodatku jedną bramką od trafienia (3 z 4 dały dokładnie 1 gola).
- **K1 (Levski O1,5) i K4 (KuPS O1,5):** pudła w kuponach to dokładnie te dwa mecze z listy Over 1,5; K1 i K4 były najsłabsze p-owo (56,8% i 51,3%), a K4 dokument sam opisał "p tuż nad 50%". **Wariancja**, wpisane w ostrzeżeniu.
- **Anderlecht X2 i Levski X2 (pula EV+):** oba p z "przewagą niepotwierdzoną" ok. +4 pp bez twardej informacji, oba przegrane. To trzeci kolejny weryfikowany dzień, w którym nogi z "przewagą niepotwierdzoną" trafiają poniżej p (patrz "Do obserwacji"); zadziałał ostatni krok procesu (nie weszły do kuponów).
- **DAL-CBJ O4,5 (73,4%) 2-1 po karnych, VGK-DET O4,5 (70,6%) 1-2:** oba mecze 3 gole. DAL grał rezerwowym DeSmithem, VGK vs Tarasov (.938) mały zestaw danych; dokument oznaczył niskie-średnie pewności i zastrzegł skorelowanie nóg z jednego wieczoru NHL. Przy zachowaniu "bez Under 4,5" (reguła z 29-30.10) to **wariancja**: łączny bilans NHL total 10/13.
- **COL ML (62%) 2-3 w dogr., EDM ML (61%) 4-5:** p zbliżone do rynku, niskie pewności, **wariancja**.
- **Musetti (70%), Fils (53,5%), Etcheverry (51,5%):** wszystkie p ≈ rynek minus 1-3 pp, żaden nie był po wolnym losie w R2 (reguła 6-8 pp nie dotyczy), **wariancja**. Etcheverry po dwóch ciężkich meczach (tie-break z Rublevem, de Minaur) to jedyny sygnał zmęczenia; dokument zastosował -3 pp i pewność niską.
- **Brak błędów danych wejściowych:** wszystkie 35 meczów piłkarskich, 13 NBA/NHL i 8 tenisowych odbyło się w zapisanych terminach (poprzedni błąd z Kouamé nie powtórzył się).

## Co zadziałało
- **Podwójna szansa i 1X2 w pucharach: 13/13 przy 9,84 oczekiwanych (+2,05 odch.)**, wszystkie p 71-81%: Anderlecht, Plzeň, NEC, Trabzonspor, Thun, Midtjylland, Getafe, Celta, Sparta, Real Sociedad, Gent, AGF, Palace.
- Kupony 2, 3, 5, 6, 7 piłki trafione (EV ujemne, stawki 0%), kupon 1 NBA/NHL (jedyny z EV+) trafiony.
- Wykluczenie nóg "przewaga niepotwierdzona" z kuponów (2/3 puli przegranych), wykluczenie Lendeborga (rynek zawodnika, jedno źródło).
- NHL total Over 4,5/5,5: 10/13 przy 9,53 oczekiwanych; NBA ML GSW trafiony mimo niepewności co do Giannisa (zagrał, GSW i tak +20).

## Kalibracja skilli
**Bez zmian.** Podstawa: jedyne odchylenie > 1,5 odch. to Over 1,5 4/8 (-1,64), ale to cztery różne mecze trafione o jedną bramkę, w poprzedniej weryfikacji ta sama grupa była 3/3 w Lidze Mistrzów, a w analizach nie ma pominiętego sygnału ani naruszonej reguły. DC 13/13 (+2,05) wskazuje, że korekta "remis ORAZ wygrana underdoga" mogłaby być zbyt ostrożna, ale to jedna kolejka z kilkoma remisami w trafionych nogach (1X/X2); łagodzić regułę dopiero przy powtórzeniu.

## Do obserwacji
- **`football-analyst`: Over 1,5 w niższych ligach pucharowych przy λ całkowitej < ~3,0 i słabo strzelających drużynach:** 05.11 4/8 (Levski, Lillestrøm, Lincoln, KuPS). Warunek zmiany: kolejne ≥ 6 takich nóg z trafieniem < 60% → odejmij 3-4 pp od Over 1,5 przy λ < 3,0 i drużynach strzelających < 1 gola na mecz w ostatnich 15; osobno LM/duże ligi (3/3 04.11) bez zmian.
- **`football-analyst`: podwójna szansa i 1X2 u faworyta z p 71-81%:** 05.11 lista 13/13 (+3,2), 04.11 LM DC 4/5. **Sprostowanie (zbiorcza weryfikacja 06.11):** hipoteza "korekta zbyt ostrożna" nie utrzymała się, bo pełny zbiór meczów 05.11 (wynik/DC, 26 nóg) wypadł 16/26 przy 18,9; 13/13 dotyczyło wybranej listy. Bez zmian.
- **Nogi "przewaga niepotwierdzona":** 05.11 1/3 pule piłkarskie (Anderlecht X2, Levski X2 ✗, Benfica BTTS ✓) + Lendeborg ✗; razem z 04.11 (1/4), 26-28.10 (53% przy 65%) wciąż stały wzorzec poniżej p, ujęty w stawkach 0-0,7%.
- **NHL total po 04.11/05.11:** Over 4,5 zachowuje się zgodnie z p (10/13), Under 4,5 nadal poza ofertą (0/8 z 29-30.10).
- **Tenis po wolnym losie w R2:** brak nowych przypadków w R3, więc reguła 6-8 pp (z 05.11) wciąż niesprawdzona.
- **Dane:** wyniki z jednego źródła (ESPN); do uzupełnienia: LoL Dplus KIA - Bilibili (analiza dnia, bez nóg w kuponach), po czym oznaczyć `Analiza_dnia_2026-11-05.md`.

To oszacowania, nie gwarancje; próba jest mała (jedna kolejka pucharowa i jedna noc NBA/NHL), a hipotetyczny zysk to tylko informacja.
