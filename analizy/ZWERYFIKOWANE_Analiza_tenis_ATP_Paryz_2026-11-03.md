# Analiza tenisowa: Rolex Paris Masters (ATP 1000, hala, twardy), 03.11.2026

Godziny polskie, terminarz ESPN (niezweryfikowany). Wszystkie mecze bo3, tie-break do 7.

## Jakość danych i ograniczenia (czytaj najpierw)

- **MCP sportsdata:** `apitennis_*` nie działa (konto API-Tennis bez opłaty, błąd 1006), więc brak rankingów, H2H i statystyk serwisu/returnu z tego źródła. Kursy: **Pinnacle** (`pinnacle_league_matchups` liga 2957 = ATP Paris R1, 2959 = R2; `pinnacle_matchup_markets`), przeliczone z kursów amerykańskich na dziesiętne i oczyszczone z marży (marża ok. 2,9-3,4%).
- **Sieć:** WebSearch zwraca głównie rok 2025, więc 2026 udało się potwierdzić tylko pojedyncze fakty (niżej). Brak statystyk sezonu (% pkt przy serwisie, SGW, RPW) i H2H dla żadnej pary. Skutek: **p_serve jest w całości oszacowane** (stała baza 0,65 hala + różnica dobrana tak, by dać zadane p), a nie wyliczone ze statystyk.
- **Wniosek obowiązkowy z "Skalibruj":** total gemów i handicap gemowy **nie są podane jako typy** (p_serve oszacowane, błąd ~5 gemów). Przy rynkach setowych (zwycięzca seta, 2-0) rozkład z modelu jest pochodną p meczu, nie niezależnym źródłem, więc pewność "niska".
- **p meczu** = punkt wyjścia rynek Pinnacle bez marży, skorygowany tylko o twarde sygnały z Skalibruj (rotacja po finale/półfinale, bye, kwalifikant, forma). Tam, gdzie brak twardego sygnału, p ≈ rynek lub lekko poniżej (R1 Masters: "brak mocnego typu" przy p 60-68%).
- **Data meczów R2:** Pinnacle ma Shelton-Norrie i Ruud-Jodar z cutoffem 05.11 10:00 UTC (ten sam cutoff mają inne mecze R2, np. Zverev-Musetti), ESPN podaje 03.11 19:00 i 20:30. Prawdopodobnie placeholder w Pinnacle, ale **zweryfikuj datę** przed typowaniem.

## Potwierdzone fakty 2026 (z sieci i MCP)

- Wycofani: Sinner (kolano, koniec sezonu), Auger-Aliassime (kolano), Fonseca (brzuch), Bublik (kolano z Ałmaty); wskoczyli m.in. Berrettini, Mérida, Van Assche, Navone (tennistourcalendar.com, aktualizacja 30.10).
- Dzikie karty główna drabinka: Droguet, Gea, Halys, Jacquet; Bonzi i Kouamé dostali WC do kwalifikacji (tennistourcalendar.com), a w tabeli ESPN grają w R1, więc to **kwalifikanci** (dwa mecze w Paryżu za sobą, jeśli ESPN/Pinnacle są właściwe; do potwierdzenia).
- Rune: protected ranking po długiej przerwie (Achilles); wygrał R1 w Bazylei (ATP/Swiss Indoors).
- Basel 2026 (26.10-01.11): półfinaliści Vacherot, Fritz, Lehecka, Struff (thedailyguardian, 31.10); **finał: Vacherot d. Lehecka 2-6, 6-3, 6-3** (atptour.com). Djokovic przegrał w Bazylei ze Struffem (Tennis Nerd); w Szanghaju przegrał pierwszy mecz. Shelton: 2-4 od finału US Open, w Bazylei przegrał z WC Kym. Fils skreczował w Bazylei z Fritzem (plecy). Berrettini: ćwierćfinał Wiednia, pokonał Cobolliego; w Roland Garros skreczował w ćwierćfinale (zdrowie jako znak zapytania). Paul: w ćwierćfinale Wiednia przegrał z Alcarazem 4-6, 6-7(2). Fery: pokonał Musettiego w Wiedniu.
- Nie znaleziono 2026: kontuzji Tsitsipasa, Tiena, Rublewa, Etcheverry, Cerúndola, Rinderknecha, Nakashimy, Michelsena, Davidovicha, Gea, Halysa, Ferego, Bonziego, Kouamé, Norrie, Jodara, Ruuda. **Brak wzmianki nie znaczy brak urazu**; pewność obniżona.

## Podsumowanie (mecz | rynek | p | fair | pewność)

| Mecz (PL godz.) | Rynek | p | fair | Kurs Pinnacle (dz.) | Pewność |
|---|---|---|---|---|---|
| F. Cerúndolo - Rinderknech (11:00) | Cerúndolo wygra | 60% | 1,67 | 1,57 | niska |
| Etcheverry - Rublev (11:00) | Rublev wygra | 66% | 1,52 | 1,43 | średnia |
| Fery - Halys (11:00) | Halys wygra | 57% | 1,75 | 1,66 | niska |
| Berrettini - Nakashima (12:30) | Nakashima wygra | 57% | 1,75 | 1,64 | niska |
| Kouamé - Davidovich Fokina (12:30) | Davidovich wygra | 68% | 1,47 | 1,35 | średnia |
| Tien - Tsitsipas (12:30) | Tien wygra | 54% | 1,85 | 1,76 | niska |
| Rune - Paul (14:00) | Paul wygra | 65% | 1,54 | 1,50 | niska |
| Vacherot - Djokovic (14:00) | Djokovic wygra | 63% | 1,59 | 1,47 | niska |
| Lehečka - Michelsen (15:00) | Lehečka wygra | 53% | 1,89 | 1,70 | niska |
| Fritz - Bonzi (15:30) | Fritz wygra | 71% | 1,41 | 1,25 | niska/średnia |
| Gea - Struff (17:00) | Struff wygra | 51% | 1,96 | 2,04 | niska (moneta) |
| Norrie - Shelton (19:00, R2) | Shelton wygra | 66% | 1,52 | 1,36 | niska |
| Jodar - Ruud (20:30, R2) | Jodar wygra | 62% | 1,61 | 1,56 | niska |

Kurs Pinnacle w tabeli dotyczy zawodnika z kolumny "Rynek". Żaden typ meczowy nie ma fair odds <= 1,15. Brak typu z wyraźnym EV (patrz sekcja "Rynek vs model" na końcu).

## Rozkład setowy i zwycięzca 1. seta (model `tennis_model.py`, p_serve oszacowane, baza 0,65)

Dla zadanego p meczu dobrano różnicę p_serve (skrypt pomocniczy w scratchpadzie wywołujący `set_dist` z `tennis_model.py`). Wartości są pochodną p meczu, nie niezależną prognozą.

| Mecz | P(1. set faworyta) | fair | 2-0 fav | 2-1 fav | 1-2 | 0-2 | P(3 sety) |
|---|---|---|---|---|---|---|---|
| Cerúndolo - Rinderknech | 56,7% | 1,76 | 32,2% | 27,8% | 21,3% | 18,7% | 49,1% |
| Rublev - Etcheverry | 60,8% | 1,64 | 37,0% | 29,0% | 18,7% | 15,3% | 47,7% |
| Halys - Fery | 54,7% | 1,83 | 29,9% | 27,1% | 22,5% | 20,5% | 49,6% |
| Nakashima - Berrettini | 54,7% | 1,83 | 29,9% | 27,1% | 22,5% | 20,5% | 49,6% |
| Davidovich - Kouamé | 62,2% | 1,61 | 38,7% | 29,3% | 17,7% | 14,3% | 47,0% |
| Tien - Tsitsipas | 52,7% | 1,90 | 27,7% | 26,3% | 23,6% | 22,4% | 49,9% |
| Paul - Rune | 60,1% | 1,66 | 36,2% | 28,8% | 19,1% | 15,9% | 47,9% |
| Djokovic - Vacherot | 58,8% | 1,70 | 34,5% | 28,5% | 20,0% | 17,0% | 48,5% |
| Lehečka - Michelsen | 52,0% | 1,92 | 27,0% | 26,0% | 24,0% | 23,0% | 49,9% |
| Fritz - Bonzi | 64,4% | 1,55 | 41,5% | 29,5% | 16,3% | 12,7% | 45,9% |
| Struff - Gea | 50,7% | 1,97 | 25,7% | 25,3% | 24,7% | 24,3% | 50,0% |
| Shelton - Norrie | 60,8% | 1,64 | 37,0% | 29,0% | 18,7% | 15,3% | 47,7% |
| Jodar - Ruud | 58,1% | 1,72 | 33,7% | 28,3% | 20,4% | 17,6% | 48,7% |

Uwaga: model z jednym wspólnym p_serve zaniża rozrzut względem realnych meczów hali (duże serwisy, tie-breaki), więc P(3 sety) ~48-50% to wartość z modelu, nie obserwacja. Linie total gemów Pinnacle dla orientacji (bez typu): Djokovic-Vacherot 23,5, Fritz-Bonzi 23,0, Cerúndolo-Rinderknech 23,0, Rublev-Etcheverry 22,5, Paul-Rune 22,5, Nakashima-Berrettini 25,0 (wysoka linia, serwisy), Halys-Fery 23,5, Tsitsipas-Tien 23,0, Davidovich-Kouamé 22,0, Struff-Gea 23,5, Lehečka-Michelsen 22,5, Shelton-Norrie 23,5, Ruud-Jodar 22,5.

## Analiza meczów

### F. Cerúndolo - Rinderknech (R1, 11:00)
**Typ:** Cerúndolo | **p:** 60% | **Fair:** 1,67 | **Pewność:** niska
- Rynek Pinnacle: Cerúndolo 62,1% bez marży (1,57), Rinderknech 2,56.
- Statystyki/H2H: brak danych 2026. Rinderknech to zawodnik hali i ma przewagę serwisu, grający u siebie (Francuz, publiczność); Cerúndolo lepszy z returnu i gry z głębi, ale z natury lepszy na mączce.
- Ryzyka: Rinderknech serwuje w hali, dużo tie-breaków (wariancja wyniku seta). Brak 2026 informacji o kontuzjach obu.
- Korekta: p -2 pp względem rynku za brak statystyk (R1 Masters 60-68% = "brak mocnego typu").
- 1. set: Cerúndolo 56,7%. Wynik: 2-0 32%, 2-1 28%.

### Etcheverry - Rublev (R1, 11:00)
**Typ:** Rublev | **p:** 66% | **Fair:** 1,52 | **Pewność:** średnia
- Rynek: Rublev 68,1% bez marży (1,43), Etcheverry 3,05.
- Etcheverry to typowy zawodnik mączki (forhend z głębi), na hali twardej mniej groźny; Rublev gra płasko i ma więcej mocy w hali. Brak H2H i formy 2026 z sieci.
- Ryzyka: forma Rublewa bywa nierówna (huśtawki emocjonalne), brak danych o jego kondycji; Etcheverry ma doświadczenie z 5-setowymi walkami, ale tu bo3.
- Korekta: -2 pp względem rynku (R1 Masters bez statystyk: p >= 70% niedozwolone).
- 1. set: Rublev 60,8%. 2-0 37%.

### Fery - Halys (R1, 11:00)
**Typ:** Halys (WC, gospodarz) | **p:** 57% | **Fair:** 1,75 | **Pewność:** niska
- Rynek: Halys 58,6% bez marży (1,66), Fery 2,35.
- Fery pokonał Musettiego w Wiedniu (świeża forma), Halys gra z dziką kartą w Paryżu przy własnej publiczności. Brak statystyk serwisu, H2H nieznane.
- Ryzyka: Halys wolnostojący serwis-wolej-agresja, duża zmienność; mecz bliski rzutu monetą. Typ 57% to niemal rynek, **nie traktować jako mocnego typu**.
- 1. set: Halys 54,7%.

### Berrettini - Nakashima (R1, 12:30)
**Typ:** Nakashima | **p:** 57% | **Fair:** 1,75 | **Pewność:** niska
- Rynek: Nakashima 59,4% bez marży (1,64), Berrettini 2,39.
- Berrettini wskoczył z listy rezerwowej (za Auger-Aliassime'a), ale ma rytm: ćwierćfinał Wiednia z wygraną nad Cobollim. Jego serwis w hali "robi dużo szkód" (Tennis Nerd), lecz skreczował w ćwierćfinale RG, więc ryzyko zdrowotne jest realne. Nakashima solidny z returnu i ruchu w hali.
- Korekta: -2,5 pp względem rynku (ryzyko dwustronne: kondycja Berrettiniego vs jego serwis w hali). Total Pinnacle 25,0 (najwyższa linia dnia) wskazuje na dużo tie-breaków.
- 1. set: Nakashima 54,7%.

### Kouamé - Davidovich Fokina (R1, 12:30)
**Typ:** Davidovich | **p:** 68% | **Fair:** 1,47 | **Pewność:** średnia
- Rynek: Davidovich 72,2% bez marży (1,35), Kouamé 3,49.
- Kouamé jest kwalifikantem/gospodarzem z dwoma meczami w Paryżu i rytmem; Davidovich z TOP ~20-25, ale niestabilny mentalnie i bywa bardzo nierówny.
- Korekta: **-4 pp względem rynku** (kwalifikant po drugiej stronie, Davidovich poza top 10; pełne -4-6 z reguły stosujemy dla faworyta spoza top 30, tu mniejsza korekta, bo przepaść rankingowa jest duża).
- 1. set: Davidovich 62,2%. 2-0 38,7%.

### Tien - Tsitsipas (R1, 12:30)
**Typ:** Tien | **p:** 54% | **Fair:** 1,85 | **Pewność:** niska
- Rynek: Tien 55,2% bez marży (1,76), Tsitsipas 2,17.
- Tien: dobre wyniki w hali (w poprzednim sezonie ok. 73% wygranych w hali, dane z 2025, przestarzałe). Tsitsipas: w 2026 brak informacji o stanie zdrowia, historia kontuzji (plecy, łokieć). H2H nieznane.
- Ryzyka: Tsitsipas w dobrym dniu ma wyższy sufit w hali; "bilans Tiena z 2025" nie jest statystyką sezonu 2026.
- Typ właściwie moneta; nie stawiać.
- 1. set: Tien 52,7%.

### Rune - Paul (R1, 14:00)
**Typ:** Paul | **p:** 65% | **Fair:** 1,54 | **Pewność:** niska
- Rynek: Paul 64,7% bez marży (1,50), Rune 2,75.
- Rune wraca po długiej przerwie (Achilles, protected ranking): **obniżona pewność, powrót po długiej kontuzji**; wygrał R1 w Bazylei, więc ma 1-2 mecze w nogach. Paul: ćwierćfinał Wiednia (4-6, 6-7(2) z Alcarazem, mecz na poziomie), lecz w 2025 wycofał się z Paryża przez stopę. Obaj "z kontuzją w tle".
- Korekta: p = rynek (kontuzja Rune'a częściowo uwzględniona przez bukmachera).
- 1. set: Paul 60,1%.

### Vacherot - Djokovic (R1, 14:00)
**Typ:** Djokovic | **p:** 63% | **Fair:** 1,59 | **Pewność:** niska
- Rynek: Djokovic 66,4% bez marży (1,47), Vacherot 2,89.
- Vacherot wygrał dopiero co turniej w Bazylei (finał 01.11 d. Lehečka 2-6, 6-3, 6-3; 5 meczów w tygodniu, 2 dni przed tym meczem, podróż do Paryża). **Krótki odpoczynek po finale = -3-5 pp dla Vacherota.** Jednocześnie jest w rytmie i wyciągnął mecz po przegranym secie. Pokonał Djokovicia w półfinale Szanghaju 2025.
- Djokovic (39 lat, nr 10, bez bye): forma słaba (porażka w pierwszym meczu Szanghaju, porażka ze Struffem w Bazylei), siedem tytułów w Paryżu, ale hala po 3 tygodniach przerwy bez wygranych. Reguła 35+ dotyczy bo5, tu bo3, więc bez odjęcia.
- Korekta: -3 pp względem rynku (słaba forma Djokovicia i Vacherot w świetnej formie, częściowo równoważone zmęczeniem Vacherota). Dwa mocne sygnały przeciwstawne, stąd pewność niska.
- 1. set: Djokovic 58,8%. 2-0 34,5%.

### Lehečka - Michelsen (R1, 15:00)
**Typ:** Lehečka | **p:** 53% | **Fair:** 1,89 | **Pewność:** niska
- Rynek: Lehečka 57,0% bez marży (1,70), Michelsen 2,26.
- Lehečka grał finał Bazylei (01.11, porażka z Vacherotem po trzech setach), 5 meczów w tygodniu, mniej niż 3 dni odpoczynku i podróż. **Krótki odpoczynek po finale: -4 pp.** Michelsen: brak danych o jego ostatnich turniejach i formie.
- Ryzyka: Lehečka lepszy zawodnik w hali (serwis, forhend), więc zmęczenie może nie zadziałać; Michelsen nierówny.
- Typ w praktyce moneta z lekkim wskazaniem na Lehečkę.
- 1. set: Lehečka 52,0%.

### Bonzi - Fritz (R1, 15:30)
**Typ:** Fritz | **p:** 71% | **Fair:** 1,41 | **Pewność:** niska/średnia
- Rynek: Fritz 77,5% bez marży (1,25), Bonzi 4,32 (**różnica 6,5 pp**).
- Fritz był w półfinale Bazylei (31.10, wynik półfinału nie potwierdzony: przegrał z Vacherotem lub Lehečką), ma 3 dni odpoczynku, sezon: finał Lyonu. Fils skreczował z nim w Bazylei. **Krótki odpoczynek po półfinale (<=3 dni): -3-5 pp.**
- Bonzi: kwalifikant (WC w kwalifikacjach), dwa mecze w Paryżu za sobą, gospodarz. Fritz jest w top 10, więc pełnej reguły "kwalifikant" (-4-6 pp, faworyt spoza top 30) nie stosuję, ale połowę uwzględniam.
- Korekta: -6,5 pp względem rynku (rotacja + kwalifikant z rytmem; p nie przekracza 75%, o czym mówi reguła dla wysokiego p w R1 Masters bez własnych statystyk).
- 1. set: Fritz 64,4%. 2-0 41,5%.
- Kurs 1,25 poniżej progu wartości (fair 1,41): nie stawiać.

### Gea - Struff (R1, 17:00)
**Typ:** Struff | **p:** 51% | **Fair:** 1,96 | **Pewność:** niska (moneta)
- Rynek: Gea 52,4% bez marży (1,85), Struff 47,6% (2,04).
- Struff: półfinał Bazylei (pokonał tam Djokovicia), 36 lat, 3 dni odpoczynku, w dobrej formie. Gea: dzika karta, Francuz, gra u siebie; brak danych o jego sezonie (poziom niższy rankingowo niż Struffa, a mimo to rynek stawia go na delikatnego faworyta, co świadczy o niepewności rynku co do kondycji Struffa).
- Korekta: odwrócenie faworyta względem rynku o 1,4 pp, bez twardego sygnału poza formą Struffa; **brak typu**.
- 1. set: Struff 50,7%.

### Norrie - Shelton (R2, 19:00)
**Typ:** Shelton | **p:** 66% | **Fair:** 1,52 | **Pewność:** niska
- Rynek: Shelton 71,0% bez marży (1,36), Norrie 3,34.
- Shelton (nr z bye) rozpoczyna turniej meczem z rywalem po wygranej R1: **faworyt po wolnym losie: -4 pp**. Do tego kryzys formy: 2-4 od finału US Open i porażka z WC Kymem w Bazylei: dodatkowe -1 pp (reszta już w rynku). Norrie pokonał Alcaraza w pierwszym meczu w Paryżu w 2025, wygrał R1 (rytm), nierówny serwis.
- Rynek jest o 5 pp wyżej niż mój p, a mój p wynika wyłącznie z reguł rotacji i znanej formy, **bez statystyk serwisu**: nie traktować jako value, tylko jako uwagę, że Shelton nie jest pewniakiem 71%.
- 1. set: Shelton 60,8%.

### Jodar - Ruud (R2, 20:30)
**Typ:** Jodar | **p:** 62% | **Fair:** 1,61 | **Pewność:** niska
- Rynek: Jodar 61,9% bez marży (1,56), Ruud 2,54. Ruud jest wyżej notowany, ale rynek faworyzuje Jodara, co sugeruje, że bukmacher ceni jego formę (finał Masters w Szanghaju, ostatnie miejsce w Turynie na 3209 pkt wg Tennis Nerd) i słabość Ruuda w hali.
- Ruud (nr z bye) w pierwszym meczu po wolnym losie przeciw rywalowi z rytmem: **-3-5 pp dla Ruuda**, już częściowo w rynku. Jodar: młody, bardzo mocny w ostatnich tygodniach, ale gra drugi mecz w Paryżu (zmęczenie nieznane).
- Korekta: p = rynek (konfliktujące sygnały: bye po stronie Ruuda +, młody Jodar bez doświadczenia w halach Masters -).
- 1. set: Jodar 58,1%.

## Rynek vs model: gdzie jestem poniżej/powyżej Pinnacle

| Mecz | Mój p | Pinnacle bez marży | Różnica | Komentarz |
|---|---|---|---|---|
| Fritz - Bonzi (Fritz) | 71% | 77,5% | -6,5 pp | rotacja po półfinale + kwalifikant; rynek zbyt pewny |
| Shelton - Norrie (Shelton) | 66% | 71,0% | -5,0 pp | bye + forma; brak statystyk, nie value |
| Lehečka - Michelsen (Lehečka) | 53% | 57,0% | -4,0 pp | rotacja po finale |
| Davidovich - Kouamé (Davidovich) | 68% | 72,2% | -4,2 pp | kwalifikant po drugiej stronie |
| Djokovic - Vacherot (Djokovic) | 63% | 66,4% | -3,4 pp | forma vs zmęczenie Vacherota |
| Pozostałe | w granicach 2 pp | | | brak twardego sygnału |

Najbardziej wiarygodne rozjazdy z rynkiem (twardy sygnał, nie sama intuicja): **Fritz** (rotacja po półfinale, kwalifikant) i **Lehečka** (finał dwa dni wcześniej). Mimo to rynek jest realnym punktem odniesienia, a mój p nie wynika ze statystyk serwisu, więc żaden z nich nie jest rekomendacją value. Dla Michelsena (47%, fair 2,13 vs kurs 2,26, EV ok. +6%) i Norrie (34%, fair 2,94 vs kurs 3,34, EV ok. +14%) przewaga wynika wyłącznie z reguł rotacji, nie ze statystyk, więc zgodnie z kalibracją ("przewaga nad rynkiem >5 pp bez twardej informacji = najpewniej własny błąd") **nie wchodzą do TOP-N**.

## Wnioski do rankingu top-N (zgodnie z kalibracją)

- Brak typu o p >= 70% poza Fritzem (71%, ale po półfinale i z kursem 1,25 bez wartości).
- Najwyższe p: Davidovich 68%, Rublev 66%, Shelton 66%, Paul 65%. W żadnym nie ma statystyk serwisu/returnu, a Rublev i Davidovich grają R1 Masters (reguła: 60-68% w R1 trafiło 4/8, "brak mocnego typu").
- Jeśli użytkownik wymaga rankingu: Rublev (średnia pewność, fair 1,52) i Davidovich (średnia, fair 1,47) to jedyne typy bez konkretnych korekt rotacyjnych w dół. Do kuponu ostrożnie.
- Rozkład 2-0 w tabeli nie jest typem (patrz ograniczenie p_serve).

To oszacowania, nie gwarancje.
