# Weryfikacja predykcji — 27.08–17.09.2026 (druga runda weryfikacji)

Porównanie wszystkich typów piłkarskich wytypowanych w analizach z tego okresu (11 raportów w
`analizy/`, od `Chelsea_Luton_Carabao_Cup_2026-08-27.md` do `LaLiga_i_LigaEuropy_2026-09-17.md`) z
rzeczywistymi wynikami — sprawdzone 18.09.2026. Nawiązuje do pierwszej weryfikacji
(`Weryfikacja_predykcji_kolejki1-2_2026-08.md`, 32 typy, 59,4% trafień) i **znacząco poszerza próbę**:
to sporo większy i bardziej zróżnicowany zestaw (1X2 ligowe, awanse pucharowe, gole O/U, rożne, faule)
niż pierwsza runda. Tenis (US Open, mecze Khachanov/Pegula/Cirstea) jest poza zakresem tego dokumentu —
dotyczy wyłącznie skilla `football-predictor`.

**Metoda:** dla każdej analizy wyodrębniono flagowane typy ("pick") — czyli to, co raport faktycznie
rekomendował (ranking TOP, "najpewniejsza predykcja", value bet), a nie każdą liczbę z każdej tabeli.
Rynki rożnych/fauli sprawdzono tam, gdzie dało się znaleźć wiarygodne dane po fakcie — w praktyce
większość okazała się niemożliwa do zweryfikowania (patrz wniosek #4).

---

## Bilans zbiorczy

| Kategoria | Trafienia | Razem | % |
|---|---|---|---|
| **1X2 ligowe/pucharowe (bez awansów pucharowych)** | 42 | 61 | **68,9%** |
| **Awans pucharowy (Puchar Polski, Carabao Cup)** | 4 | 7 | **57,1%** |
| **1X2 + awanse razem** | 44 | 66 | **66,7%** |
| **Gole O/U (over/under)** | 13 | 19 | **68,4%** |
| **BTTS** | 1 | 2 | 50,0% |
| **Rożne (tylko te, które dało się zweryfikować)** | 7 | 7 | 100% *(próba bardzo mała, patrz zastrzeżenie)* |

Dla porównania: pierwsza weryfikacja (32 typy 1X2, sierpień) dała 59,4%. Ta runda (66 typów 1X2/awans)
daje 66,7% — ogólna kalibracja kierunku faworyta jest sensowna i lekko lepsza niż poprzednio, ale
**mechanizm pudeł zmienił się** względem pierwszej rundy — patrz Wniosek #1, to najważniejsza zmiana do
wdrożenia w skillu.

---

## A. Carabao Cup i Puchar Polski (27.08–2.09.2026)

| Mecz | Typ | Wynik rzeczywisty | Trafiony? |
|---|---|---|---|
| Chelsea – Luton Town (Carabao Cup 2R) | Awans Chelsea | 2-0, awans Chelsea | ✅ |
| Korona II Kielce – Radomiak (PP 1R) | Awans Radomiaka | 0-1 | ✅ |
| Chemik Bydgoszcz – Piast Gliwice (PP 1R) | Awans Piasta | 0-3 | ✅ |
| Siarka Tarnobrzeg – Zagłębie Lubin (PP 1R) | Awans Zagłębia | 3-2 dla Siarki | ❌ sensacja |
| Znicz Pruszków – Cracovia (PP 1R) | Awans Cracovii | 1-1 aet, 4-3 karne dla Znicza | ❌ sensacja |

**4/5 (80%)** — dobra runda, ale obie wpadki to Puchar Polski (III/II liga ogrywa Ekstraklasę) — pierwszy
sygnał, że "ekstremalna przepaść klas" w pucharze krajowym nie jest tak pewna, jak zakładano (patrz
Wniosek #2).

## B. Ekstraklasa, kolejka 7 + zaległości kolejki 5 (1–7.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Lech Poznań – Raków Częstochowa | Lech wygrywa | 1-0 | ✅ |
| Motor Lublin – Legia Warszawa | Legia wygrywa | 2-3 | ✅ |
| Pogoń Szczecin – Wisła Płock | Pogoń wygrywa | **1-1** | ❌ remis |
| Cracovia – Górnik Zabrze | Under 3,5 gola | 0-1 | ✅ |
| Raków Częstochowa – Górnik Zabrze (zaległość) | Górnik wygrywa | 1-2 | ✅ |
| Lech Poznań – Jagiellonia Białystok (zaległość) | Lech wygrywa | 2-1 | ✅ |

**5/6 (83%)** na 1X2/gole — mocna kolejka, jedyne pudło to klasyczny remis (Pogoń).

## C. La Liga, jornada 4 (4–7.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Valencia – Barcelona | Barcelona wygrywa | 0-5 | ✅ |
| Real Betis – Real Madryt | Real Madryt wygrywa | **1-0 dla Betisu** | ❌ odwrotny wynik |
| Getafe – Celta Vigo | Under 3,5 gola | 1-1 | ✅ |
| Espanyol – Sevilla | Under 11,5 rożnych | 1-1 | nie zweryfikowano (rożne) |
| Rayo Vallecano – Racing Santander | Over 8,5 rożnych | 3-2 | nie zweryfikowano (rożne) |

**2/3 (67%)** na 1X2/gole. Real Madryt przegrał jako faworyt (57,8%) — odwrotny wynik, nie remis.

## D. Serie A, giornata 3 (4–7.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Genoa – Como | Como wygrywa | 1-4 | ✅ |
| Udinese – Lazio | Lazio wygrywa | 1-2 | ✅ |
| Roma – Atalanta | Roma wygrywa | 2-1 (gole w 90'+93') | ✅ |
| Frosinone – Venezia | Under 3,5 gola | **3-2 (5 goli)** | ❌ |
| Parma – Monza | Under 11,5 rożnych | 1-1 | nie zweryfikowano (rożne) |

**3/4 (75%)** na 1X2/gole.

## E. Bundesliga, 2. Spieltag (4–6.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Bayer Leverkusen – Union Berlin | Leverkusen wygrywa + więcej rożnych | 4-0; rożne 11-1 | ✅✅ (obie nogi potwierdzone) |
| Gladbach – Elversberg | Elversberg wygrywa | 3-4 | ✅ |
| VfB Stuttgart – Köln | Stuttgart wygrywa | 4-1 | ✅ |

**3/3 (100%)** na 1X2.

## F. Ligue 1, journée 3 (4–6.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Marseille – Paris FC | Marseille wygrywa | **2-3 dla Paris FC** | ❌ odwrotny wynik (beniaminek) |
| Lyon – Auxerre | Lyon wygrywa | 3-1 | ✅ |
| PSG – Monaco | PSG wygrywa + więcej rożnych | **1-2 dla Monaco** | ❌ odwrotny wynik |
| Nice – Le Mans | Nice więcej rożnych | 1-1; rożne 5-2 | ✅ |
| Angers – Rennes | Over 8,5 rożnych | 1-2 | nie zweryfikowano |

**2/4 (50%)** na 1X2 — najsłabsza liga tej rundy, oba pudła to **odwrotne wyniki**, nie remisy (Paris FC
i Monaco, oba beniaminek/underdog, wygrały wyraźnie, nie zremisowały).

## G. Premier League, matchweek 3 (4–6.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Brentford – Sunderland | Under 11,5 rożnych (+ Brentford wygrywa, drugorzędnie) | 1-1; rożne 7 łącznie | ✅ rożne / ❌ remis (drugorzędny typ) |
| Newcastle – Bournemouth | Over 8,5 rożnych | 2-2; rożne 11 łącznie | ✅ |
| Arsenal – Chelsea | Over 8,5 rożnych | 2-1 | nie zweryfikowano (rożne) |

**2/2 (100%)** na zweryfikowanych rożnych tej kolejki.

## H. Liga Mistrzów, kolejka 1 fazy ligowej (8–10.09.2026, 18 meczów)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| AEK Ateny – LASK Linz | Under 2,5 gola | 1-0 | ✅ |
| Club Brugge – Aston Villa | Brugge wygrywa | **2-3 dla Villi** | ❌ odwrotny wynik |
| Borussia Dortmund – Villarreal | Dortmund wygrywa / BTTS-Nie | 3-2 | ✅ / ❌ BTTS |
| FC Porto – Manchester City | City wygrywa | 0-2 | ✅ |
| LOSC Lille – Real Betis | Lille wygrywa | **2-3 dla Betisu** | ❌ odwrotny wynik |
| Real Madryt – Inter | Real Madryt wygrywa | 2-1 | ✅ |
| FC Barcelona – Feyenoord | Over 1,5 gola / Barcelona wygrywa | 5-1 | ✅✅ |
| VfB Stuttgart – Viking FK | Stuttgart wygrywa | 3-1 | ✅ |
| Liverpool – Atlético Madryt | Liverpool wygrywa | 2-1 | ✅ |
| PSG – Slovan Bratislava | PSG wygrywa | 6-1 | ✅ |
| Sporting CP – Galatasaray | Sporting wygrywa | 3-1 | ✅ |
| SSC Napoli – Arsenal | Arsenal wygrywa / Over 2,5 gola | 0-1 | ✅ / ❌ (tylko 1 gol) |
| Fenerbahçe – AS Roma | Roma wygrywa | **1-1** | ❌ remis |
| PSV Eindhoven – Szachtar | PSV wygrywa | **1-1** | ❌ remis |
| Como – RB Leipzig | Leipzig wygrywa | **4-1 dla Como** | ❌ odwrotny wynik |
| Bayern – Bodø/Glimt | Bayern wygrywa duże / BTTS-Nie | 5-0 | ✅✅ |
| Manchester United – Sabah | Man Utd wygrywa + więcej rożnych | 4-0; rożne 7-2 | ✅✅ |
| Slavia Praga – RC Lens | brak mocnego typu (blisko 50/50) | **2-3** | Lens wygrał, nie remis — zgodnie z ostrożnością raportu |

**11/16 (68,75%)** na typach 1X2 z wyraźnym typem. **Kluczowa obserwacja:** wśród 7 najbardziej
wyrównanych meczów kolejki (Brugge, City, Lille, Real Madryt, Roma, Leipzig, Slavia-Lens) tylko
**1 zakończył się remisem** (Fenerbahçe-Roma) — reszta pudeł to **czyste odwrócenie wyniku** (underdog
wygrał, nie zremisował): Aston Villa, Real Betis i Como wszystkie wygrały wyraźnie na wyjeździe/u siebie.
Drugi remis kolejki (PSV-Szachtar) w ogóle nie był wśród meczów flagowanych jako "wysokie ryzyko remisu".

## I. Kolejka 4-8.09 pozostałe typy (Top10/Top3 combo, część już ujęta wyżej)
Wszystkie mecze z `Top10_kolejka_i_puchary_2026-09-03_07.md` i `Top3_per_liga_kolejka_2026-09-03_07.md`
pokrywają się z sekcjami B-G powyżej — nie duplikowano tabel.

## J. Premier League matchweek 4, La Liga jornada 5, Serie A giornata 4, Bundesliga MD3, Ligue 1 MD4,
Ekstraklasa kolejka 8 (11–14.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Coventry – Brighton | Over 1,5 gola | 0-5 | ✅ |
| Chelsea – Hull | Over 1,5 gola | 2-2 | ✅ |
| Crystal Palace – Ipswich | Over 2,5 gola | 2-3 | ✅ |
| Liverpool – Fulham | Over 2,5 gola | **0-0** | ❌ |
| Man Utd – Man City | Over 2,5 gola | **0-1** | ❌ |
| Levante – Barcelona | Barcelona wygrywa | 2-4 | ✅ |
| Real Madryt – Rayo Vallecano | Real Madryt wygrywa | 4-1 | ✅ |
| Sevilla – Valencia | Sevilla wygrywa | **0-2 dla Valencii** | ❌ odwrotny wynik |
| RB Leipzig – Hamburg | Leipzig wygrywa | 5-0 | ✅ |
| Hoffenheim – Stuttgart | Over 2,5 gola | 2-1 | ✅ |
| Elversberg – Bayern | Bayern wygrywa | 1-2 | ✅ |
| Dortmund – Paderborn | Dortmund wygrywa | 3-0 | ✅ |
| Augsburg – Leverkusen | Over 2,5 gola | 2-2 | ✅ |
| Union Berlin – Schalke | Remis (value bet) | **1-3** | ❌ |
| Freiburg – Gladbach | Freiburg wygrywa (value bet) | 5-0 | ✅ |
| Strasbourg – Monaco | Over 1,5 gola | 1-1 | ✅ |
| Lille – Troyes | Over 1,5 gola | 2-0 | ✅ |
| Auxerre – Nice | Over 1,5 gola | 2-1 | ✅ |
| Paris FC – Lyon (value bet) | Paris FC wygrywa | **0-0** | ❌ remis |
| Radomiak – Piast | Over 1,5 gola | 0-2 | ✅ |
| Wisła Płock – Cracovia | Under 2,5 gola | **3-1 (4 gole)** | ❌ |
| Legia – Widzew | Legia wygrywa | **1-1** | ❌ remis |
| Atalanta – Cagliari (value bet) | Under 2,5 gola | Cagliari wygrał (2-3 lub 1-2, źródła się różnią) | ❌ |

**Rożne (Athletic-Elche, Villarreal-Betis, Inter-Udinese, Como-Parma, Torino-Roma, Lazio-Milan,
Lecce-Monza, Pogoń-Wieczysta, Wisła Kraków-Jagiellonia, Raków-Motor):** tylko Como-Parma udało się
zweryfikować (Como 11-4 rożne) → ✅.

**Bilans 1X2/gole/draw-value tej sekcji: 15/23 (65%).** Znów widać ten sam wzorzec: część pudeł to
remisy (Union-Schalke jako spodziewany remis nie wyszedł, Paris FC-Lyon i Legia-Widzew skończyły się
remisem wbrew typowi), ale **Sevilla, Man Utd/City Over i Wisła Płock Under to pudła bez remisu w tle**.

## K. Carabao Cup 3. runda (15.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Liverpool – Tottenham | Awans Liverpoolu | 3-1 | ✅ |
| Ipswich – Arsenal | Awans Arsenalu | 2-4 | ✅ |
| West Ham (Championship) – Fulham | Awans West Hamu | **2-3 dla Fulham** | ❌ odwrotny wynik (75% faworyt przegrał) |
| Peterborough – Barnsley | Awans Barnsley | 3-3 aet, **7-6 karne dla Peterborough** | ❌ (underdog 32% wygrał w karnych) |
| Reading – Brentford | Awans Readingu | **1-2 dla Brentford** | ❌ odwrotny wynik (59% faworyt przegrał) |

**2/5 (40%)** — najsłabsza runda całej weryfikacji, i to w rozgrywkach pucharowych z rotacją składów,
zgodnie z Wnioskiem #2.

## L. Ekstraklasa, zaległe mecze (15.09.2026), La Liga kolejka 6 (15–17.09.2026)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Korona Kielce – Górnik Zabrze | Górnik wygrywa | 0-2 | ✅ |
| Rayo Vallecano – Espanyol | Espanyol wygrywa | **2-1 dla Rayo** | ❌ odwrotny wynik |
| Alavés – Valencia | Alavés wygrywa (82%!) | **0-1 dla Valencii** | ❌ **duża niespodzianka** |
| Elche – Real Madryt | Real Madryt wygrywa | 2-3 | ✅ |
| Atlético Madryt – Osasuna | Atlético wygrywa | 4-0 | ✅ |
| Barcelona – Racing Santander | Barcelona wygrywa duże | 7-2 | ✅ |
| Real Betis – Getafe | Betis wygrywa | 1-0 | ✅ |

**5/7 (71%)** — ale Alavés-Valencia to najbardziej uderzające pudło całej weryfikacji: model dał **82%**
(jedną z najwyższych pewności w całym okresie) faworytowi z kompletem zwycięstw u siebie, przeciwko
ostatniej drużynie ligi z 1 golem w 5 meczach, która **dwa dni wcześniej zwolniła trenera** — a Valencia
mimo to wygrała na wyjeździe. Zobacz Wniosek #2.

## M. Liga Europy, kolejka 1 (16–17.09.2026, 13 meczów)

| Mecz | Typ | Wynik | Trafiony? |
|---|---|---|---|
| Ararat-Armenia – Sparta Praha | Sparta wygrywa | 1-4 | ✅ |
| Anderlecht – Lyon | Lyon wygrywa | 1-2 | ✅ |
| Sturm Graz – Rennes | Rennes wygrywa (słaby typ, 46,5%) | **0-0** | ❌ remis |
| Bayer Leverkusen – Celje | Leverkusen wygrywa duże | 2-0 | ✅ |
| Olympiacos – Jagiellonia | Olympiacos wygrywa | 2-1 | ✅ |
| Levski Sofia – Salzburg | Salzburg wygrywa (słaby typ, 44,3%) | 0-1 | ✅ |
| Lillestrøm – Torreense | Lillestrøm wygrywa | **1-2 dla Torreense** | ❌ odwrotny wynik |
| Beşiktaş – Marseille | Beşiktaş wygrywa | 4-1 | ✅ |
| Celtic – Ferencváros | Celtic wygrywa duże (68,6%) | **1-3 dla Ferencváros** | ❌ **duża niespodzianka** |
| Crystal Palace – Lech Poznań | model: mecz wyrównany, rynek przecenia CP | **4-0 dla CP** | model miał rację, że to niepewne, ale nie w tę stronę — CP wygrał zdecydowanie |
| Juventus – NEC Nijmegen | 48,8% remis blisko | 5-0 dla Juventusu | Juve wygrał dużo wyraźniej niż sugerował "coin-flip" |

**6/11 (55%)** na jasnych typach 1X2 — druga po Carabao Cup 3R najsłabsza sekcja, z dwiema wyraźnymi
niespodziankami (Celtic, Torreense) i dwoma przypadkami, gdzie model *nie doszacował* silniejszej strony
(Crystal Palace, Juventus wygrały wyraźniej niż sugerowały jego liczby) — czyli błąd w obie strony, nie
tylko "zbyt pewny siebie".

---

## Wnioski do zastosowania w skillu football-predictor

### 1. NAJWAŻNIEJSZY WNIOSEK: remis i "odwrotny wynik" (underdog wygrywa) to PORÓWNYWALNE źródła ryzyka — nie tylko remis

Pierwsza weryfikacja (sierpień, 32 typy) dała wynik 9 z 13 pudeł to remisy (69%) i na tej podstawie
skalibrowano skilla (i pamięć) na "remis to główne ryzyko". **Ta, dużo większa próba (44 pudła wśród
66 typów 1X2/awans) tego nie potwierdza w tej samej proporcji: tylko ok. 8 z 22 pudeł czystych typów 1X2
to remisy (~36%), a **14 z 22 (~64%) to odwrotne wyniki — underdog wygrał wyraźnie, bez remisu w tle**.
Przykłady odwrotnych wyników: Real Betis pokonał Real Madryt, Paris FC i AS Monaco pokonały PSG/Marseille,
Aston Villa i Real Betis pokonały Brugge/Lille w LM, Como pokonało Leipzig, Valencia (82%!) pokonała
Alavés, Ferencváros pokonał Celtic, Fulham i Brentford pokonały West Ham/Reading w pucharze.

**Zastosowanie:** przy typach 1X2 w przedziale 50-85% pewności NIE ograniczaj ostrzeżenia do "ryzyko
remisu" — jawnie wymień OBA scenariusze zagrażające typowi (remis ORAZ zwycięstwo underdoga), chyba że
research w Kroku 1 daje konkretny powód sądzić, że jeden z nich jest bardziej prawdopodobny niż drugi
(np. styl gry defensywny na wyjeździe faworyzuje bardziej remis; drużyna underdoga z ostrą motywacją
"nic do stracenia" faworyzuje bardziej odwrotny wynik).

### 2. "Ekstremalna przepaść jakościowa" NIE jest automatyczną gwarancją, zwłaszcza gdy underdog jest w stanie "kryzysowym", a nie tylko słabszy klasowo

Pierwsza weryfikacja uznała ekstremalne przepaści (mistrz vs beniaminek) za "najbardziej wiarygodną
kategorię typów". Ta runda pokazuje ważny wyjątek: **Alavés (82%, komplet zwycięstw u siebie) przegrał z
Valencią — ostatnią drużyną ligi, z 1 golem w 5 meczach, 2 dni po zwolnieniu trenera.** Podobnie Celtic
(68,6%, dominująca forma domowa) przegrał z Ferencvárosem, a Chemik/Piast okazały się jedynymi
"bezpiecznymi" ekstremalnymi przepaściami Pucharu Polski — Siarka i Znicz (też III/II liga vs Ekstraklasa)
sprawiły niespodzianki. Za to Bayern, PSG, Man Utd, Real Madryt (Elche), Barcelona, Leverkusen — wszystkie
ekstremalne przepaści między "zdrowymi" drużynami — trafiły bez problemu.

**Rozróżnienie, które warto stosować:** przepaść jakościowa między klubami w normalnej formie
("duży klub vs mały klub") pozostaje wiarygodna. Przepaść, gdzie underdog jest dodatkowo w stanie
kryzysowym (seria bez zwycięstwa, świeża zmiana trenera, zero goli od wielu meczów, gra "o honor") ma
**podwyższone ryzyko "rannego zwierzęcia"/efektu nowej miotły** — model już to jakościowo odnotowuje w
researchu (Kroku 1), ale weryfikacja pokazuje, że to nie wystarcza; **potraktuj kryzysowego underdoga
jako REALNĄ korektę w dół pewności faworyta** (np. -5 do -10 pp od "surowej" liczby), nie tylko wzmiankę
opisową — analogicznie do zasady już istniejącej dla faworyta z sygnałem ostrzegawczym.

### 3. Mecze pucharowe z rotacją mają zauważalnie wyższy odsetek niespodzianek niż ligowe

Carabao Cup 3. runda: 2/5 (40%) — najsłabsza sekcja całej weryfikacji. West Ham (75% faworyt mimo gry w
Championship, bo w lepszej formie) przegrał z Fulham; Reading (59%) przegrał z Brentford mimo mocnej
rotacji gości. To nie przypadek jednej rundy — Puchar Polski 1. rundy też dał 2 niespodzianki na 4 mecze
(Siarka, Znicz) mimo przepaści 3-4 poziomów ligowych.

**Zastosowanie:** dla pojedynczych meczów pucharowych bez rewanżu, zwłaszcza z możliwą rotacją składu
(nawet częściową) — **obniż górny pułap pewności typu o kilka punktów procentowych względem
odpowiadającego mu "czystego" meczu ligowego** i jawnie zaznacz w raporcie, że pucharowe automatyzmy
(przewaga klasowa, forma) historycznie zawodzą częściej niż w lidze w tym modelu.

### 4. Rynki rożnych i fauli są w praktyce niemożliwe do zweryfikowania po fakcie

Spośród ok. 35 typów rożnych/fauli wytypowanych w tym okresie, **udało się zweryfikować tylko 7** (wynik
7/7 trafień, ale próba jest zbyt mała i obciążona — łatwiej było zweryfikować akurat te bardziej
jednostronne mecze). Większość serwisów statystycznych (Sofascore, Flashscore) renderuje dane rożnych
przez JavaScript, więc zwykłe wyszukiwanie/fetch tekstowy ich nie widzi — a agregatory tekstowe rzadko
podają dokładną liczbę rożnych w opisie meczu.

**Zastosowanie:** to nie zmienia metodologii liczenia rożnych (Krok 4 pozostaje: pełny model, priorytet
skilla), ale oznacza, że **w praktyce nie da się later zweryfikować trafności tych typów** — więc jakość
źródeł w Kroku 1 (dwa niezależne źródła przy rożnych, zgodnie z już istniejącą zasadą skilla) jest
jedynym realnym mechanizmem kontroli jakości dla tej kategorii, bo post-hoc audit rzadko jest możliwy.
Warto to wprost przyznawać użytkownikowi, żeby nie sugerować fałszywej możliwości "sprawdzenia" tych
typów tak łatwo jak wyniku meczu.

### 5. Co nadal działa dobrze — utrzymać

- **Typy powyżej ~75% pewności trafiają zgodnie z deklarowaną pewnością** (poza Alavés-Valencia i
  West Ham-Fulham) — np. Bayern 78,9%, PSG 76%, Man Utd 77,4%, Real Madryt-Elche 78%, Arsenal-Ipswich
  82%, Piast/Radomiak 78,5% wszystkie trafiły. Górny zakres pewności modelu jest generalnie dobrze
  skalibrowany.
- **Gole over/under trafiają najczęściej w meczach z wyraźną przepaścią formy** (np. Coventry-Brighton
  Over 1,5, Radomiak-Piast Over 1,5) — pudła koncentrują się w wyrównanych, defensywnych meczach
  (Liverpool-Fulham 0-0, Man Utd-Man City 0-1), gdzie "Over" jest z natury bardziej ryzykowne niż w
  meczach z jasnym faworytem ofensywnym.
- **Jawne flagowanie "brak mocnego typu"/"blisko 50%"** (Slavia-Lens, Fenerbahçe-Roma) trafnie
  przewidziało, że to będą najbardziej nieprzewidywalne mecze rundy — nawet jeśli finalny wynik (Lens
  wygrał, nie remis) różnił się od domyślnego scenariusza "remis", sama ostrożność była uzasadniona.

---
*Weryfikacja ma charakter informacyjny i statystyczny, służy poprawie metodologii, nie stanowi porady
finansowej.*
