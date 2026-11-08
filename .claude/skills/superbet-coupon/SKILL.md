---
name: superbet-coupon
description: Pojedynczy mecz od analizy do kuponu na superbet.pl (piłka nożna, koszykówka NBA, hokej NHL, siatkówka) - najpierw pobiera listę wydarzeń o najbliższym starcie z zadanego okresu i daje wybór meczu z listy (z możliwością pokazania kolejnych), potem zawsze pyta użytkownika o oczekiwany kurs kuponu i stawkę, potem robi pełną analizę meczu skillem analitycznym, składa kupon Bet Builder z kursów Superbet (connector superbet-mcp), po wyraźnym potwierdzeniu stawia zakład w przeglądarce (Claude in Chrome) i publikuje pod kuponem analizę napisaną prostym językiem, bez stawki i kwoty wygranej. Używaj zawsze, gdy użytkownik prosi o "kupon na mecz X na Superbet", "postaw zakład na Superbet", "analiza i kupon z kursem > 2", "dodaj analizę pod kuponem" albo chce przejść ścieżkę mecz → analiza → zakład → post w Supersocial - także gdy nie pada słowo "kupon".
---

# Superbet: mecz → analiza → kupon → zakład → analiza pod kuponem

Orkiestrator dla jednego meczu na superbet.pl, w piłce nożnej, NBA, NHL i siatkówce (patrz "Zakres sportów"). Analizę robi skill analityczny (`football-analyst`, `nba-analyst`, `nhl-analyst`, ...), wywołany narzędziem Skill; ten skill nie wymyśla prawdopodobieństw. Dane zawsze z researchu w sieci i MCP, nie z pamięci. Język: polski.

## Hierarchia źródeł danych (twarda reguła)

**Głównym źródłem danych jest connector `superbet-mcp`; wszystkie pozostałe źródła są tylko rezerwą.** Dotyczy to każdego kroku: lista wydarzeń, kursy i rynki, składy, nieobecni, sędzia, statystyki, H2H, forma.
1. **Najpierw zawsze connector** (`superbet_events`, `superbet_event_odds`, `superbet_lineups`, `superbet_missing_players`, `superbet_stats`, `superbet_h2h`). Nie zaczynaj od WebSearch, MCP `sportsdata` ani serwisów zewnętrznych, dopóki nie sprawdzisz, co zwraca connector.
2. **Rezerwa tylko dla luk**: gdy connector zwraca błąd "Brak danych", puste pole (np. brak średnich przedmeczowych), dane nieobsługiwane przez connector (sport inny niż piłka nożna, mecz juniorski/wirtualny, wiadomości, konferencje prasowe, wypowiedzi trenerów, pogoda) albo wyraźnie nieaktualne. Wtedy użyj reszty: skillowych źródeł skilla analitycznego (MCP `sportsdata`, WebSearch/WebFetch, serwisy lokalne), a w raporcie zaznacz, które dane pochodzą z rezerwy.
3. **Rozbieżność źródeł**: nie uśredniaj. Dla składów, nieobecności i sędziego wiążące jest to, co connector pokazuje na dany moment, chyba że rezerwa jest wyraźnie świeższa (np. oficjalny komunikat klubu po godzinie odczytu); wtedy opisz rozbieżność i wybierz świeższe, z podaniem źródła i godziny.
4. **Kursy i rynki do kuponu wyłącznie z Superbet** (connector, a wiążący jest kurs z kuponu w przeglądarce); kursy innych bukmacherów służą tylko jako punkt odniesienia dla modelu, nigdy do wyceny kuponu.
5. **Własne prawdopodobieństwa nadal liczy skill analityczny.** Connector dostarcza dane wejściowe (składy, średnie, H2H), nie gotowe p; jego statystyki nie zastępują analizy ani skryptów (`poisson.py` itd.).
6. W raporcie krótko wymień, z jakich źródeł pochodzą kluczowe dane (connector vs rezerwa).

## Zakres sportów

Skill obsługuje cztery sporty (identyfikatory `sport_id` w Superbet sprawdzone na ofercie z 08.11.2026):

| Sport | `sport_id` | Rozpoznanie | Skill analityczny | Skrypt modelu |
|---|---|---|---|---|
| Piłka nożna | 5 | wszystkie ligi i puchary oraz **mecze reprezentacji seniorskich** (pomiń juniorskie, rezerwowe, wirtualne) | `football-analyst` | `poisson.py`, `markets.py` |
| Koszykówka NBA + reprezentacje | 4 | NBA: `tournament_id` 164; **mecze reprezentacji seniorskich** (kwalifikacje, turnieje FIBA); inne ligi klubowe tylko na prośbę | `nba-analyst` | `nba_model.py`, `nba_props.py` |
| Hokej NHL + reprezentacje | 3 | NHL: `tournament_id` 139; **mecze reprezentacji seniorskich** (turnieje międzynarodowe, np. Euro Hockey Tour; widziano turniej 1888); inne ligi klubowe tylko na prośbę | `nhl-analyst` | `nhl_model.py`, `nhl_props.py` |
| Siatkówka | 1 | ligi seniorskie (np. PlusLiga, SuperLega) **i mecze reprezentacji seniorskich** (Liga Narodów, kwalifikacje, turnieje); mecze (K) to kobiety | `volleyball-analyst` | `volleyball-analyst/scripts/volleyball_model.py` |

**Mecze reprezentacyjne.** We wszystkich czterech dyscyplinach na listę wchodzą także mecze **reprezentacji seniorskich** (kobiecych i męskich), a filtr "tylko NBA/NHL" dotyczy wyłącznie lig klubowych. Rozpoznajesz je po tym, że obie strony to nazwy państw (np. "Łotwa · Austria", "Czechy · Szwajcaria"); wydarzenia juniorskie i młodzieżowe reprezentacji (U18, U20, U21, olimpijskie U23) nadal odrzucaj. Zasady analizy:
- **Piłka nożna:** `football-analyst` ma osobne korekty dla reprezentacji (λ drużyny nie niżej niż ok. 0,7, łączne korekty kadrowe w dół nie więcej niż ok. 15%, Under 2.5 przy łącznym λ ≤ 2,0 najwyżej średnia pewność); nie obchodź ich.
- **Koszykówka, hokej, siatkówka:** skille `nba-analyst`/`nhl-analyst` są skalibrowane na ligi klubowe, a dla siatkówki nie ma skilla, więc przy reprezentacjach korzystaj z nich jako z modelu, ale **obniż pewność o jeden poziom** (kadry zmieniają się z meczu na mecz, a mecze towarzyskie i grupowe mają rotację i niepewną motywację) i ostrzeż o tym w raporcie. Szczególnie sprawdź: skład powołań (kto zagra, kto odpoczywa), stawkę meczu (towarzyski, kwalifikacje, turniej), zmęczenie po okienku (podróże) i H2H tylko z ostatnich 2-3 lat.
- Rynki zawodnika w meczach reprezentacji pomijaj, dopóki skład nie jest potwierdzony.
- **Narzędzia statystyczne connectora** dla reprezentacji piłkarskich nie były sprawdzone: gdy `superbet_lineups`/`superbet_stats` zwracają "Brak danych", użyj rezerwy.

Tenis, MMA i e-sport: tylko gdy użytkownik wyraźnie o nie poprosi (mają skille analityczne, ale nie są domyślnym zakresem).

**Co dostarcza connector poza piłką.** `superbet_events` i `superbet_event_odds` działają dla wszystkich sportów. **Narzędzia `superbet_lineups`, `superbet_missing_players`, `superbet_stats` i `superbet_h2h` działają tylko dla piłki nożnej** (sprawdzone: dla koszykówki, hokeja i siatkówki API zwraca 404). Dla NBA, NHL i siatkówki składy, kontuzje, statystyki i H2H pochodzą więc z rezerwy (to dozwolone przez hierarchię źródeł: dane nieobsługiwane przez connector), i trzeba to zaznaczyć w raporcie. Rezerwa: NBA - injury report i starting five (MCP `nba_daily_lineups`, `nba_boxscore`, `balldontlie_nba_*`, `espn_*`, BettingPros); NHL - potwierdzony bramkarz startowy i składy (`nhl_*`, `espn_*`, BettingPros); siatkówka - WebSearch/WebFetch (serwisy ligowe, Flashscore/Sofascore, zapowiedzi klubów).

**NBA i NHL.** Wydarzenia nocne (start 00:00-04:00 czasu polskiego) mają w ofercie rynki dopiero po ich otwarciu i znikają po starcie; sprawdzaj `liczba_rynkow` > 0. Rynki NBA/NHL (spread, total, rynki zawodnika, puck line) wyceniaj skryptami z skilla analitycznego, a kupon składaj z rynków, które Superbet faktycznie ma (nie zakładaj, że rynek zawodnika istnieje).

**Siatkówka.** Analizę robi `volleyball-analyst` (cztery filary, p seta z rynku przez `volleyball_model.py --from-match`, wynik w setach, handicap setowy, total setów). Skill jest nowy i **nie ma jeszcze zweryfikowanych typów**, a statystyki atak/blok/zagrywka są dostępne tylko dla topowych lig, więc pewność "wysoka" jest tam rzadka, a "niska" przy braku danych o składach i formie (wtedy kuponu nie przygotowuj, patrz krok 3). Rynki totalu punktów i rynki zawodnika w siatkówce pomijaj. Po pierwszej weryfikacji typów dopisz lekcje do `volleyball-analyst`.

## Krok 0a: lista wydarzeń o najbliższym starcie (przed pierwszym pytaniem)

Zanim zadasz pierwsze pytanie z kroku 0, **pobierz listę wydarzeń, do których rozpoczęcia jest najbliżej**, i pokaż ją użytkownikowi, żeby mógł wybrać mecz z listy. Jeśli żaden z nich mu nie pasuje, może poprosić o kolejne (stronicowanie, patrz punkt 5).

1. **Okres**: weź go z zapytania ("dziś", "jutro", "weekend", daty "od-do"). Gdy zapytanie go nie zawiera, przyjmij **od teraz do końca najbliższej doby** (strefa Europe/Warsaw, data i godzina z kontekstu sesji), napisz to jednym zdaniem nad listą i pozwól zmienić okres w polu "Other" pytania poniżej. Zakres dłuższy niż ~3 dni zawęź. Jeśli użytkownik podał konkretny mecz w zapytaniu, pomiń listę i przejdź do kroku 0, traktując mecz jako potwierdzony.
2. **Pobierz wydarzenia** connectorem `superbet_events` dla sportów z "Zakresu sportów" (osobno `sport_id` 5, 4, 3, 1; daty UTC `YYYY-MM-DD`, `date_to` = dzień po ostatnim dniu; duży `limit`, bo wirtualne i e-sportowe wydarzenia zasłaniają realne). Dla koszykówki i hokeja zostaw `tournament_id` 164 (NBA) i 139 (NHL) oraz mecze reprezentacji seniorskich (obie strony to nazwy państw); pozostałe ligi klubowe pomiń. Wyrzuć: wydarzenia bez rynków (`liczba_rynkow` = 0), wirtualne/symulowane (nazwy z nickiem w nawiasie, np. "(Kotkata)"), mecze juniorskie i rezerwowe (U21, II, młodzieżowe, także reprezentacje juniorskie i olimpijskie), wydarzenia już rozpoczęte oraz takie, które zaczną się za mniej niż ~30 minut (nie zdążysz z analizą przed startem, patrz krok 6). Wydarzenia z bardzo małą ofertą (np. `liczba_rynkow` < 15) pomiń, bo Bet Builder nie ma z czego złożyć kuponu.
3. **Posortuj wg godziny rozpoczęcia, od najbliższej** (rosnąco, jedna lista dla wszystkich sportów). To jest jedyne kryterium kolejności: nie ustawiaj wyżej "lepszych" lig ani wydarzeń ze znanymi składami. Dla każdego wydarzenia z pierwszej strony (patrz punkt 5) dołącz kursy zwycięzcy z `superbet_event_odds` (rynek "Mecz", mały `max_markets`) i **status składu jako informację w tabeli**, nie jako kryterium: piłka - `superbet_lineups` ("oficjalny" / "przewidywany" / "brak"; oficjalne składy pojawiają się ok. 60-75 min przed startem); NBA - injury report i starting five; NHL - potwierdzony bramkarz; siatkówka - "brak danych" lub skład ze źródła klubowego. Tam, gdzie connector nie obsługuje sportu, sprawdź rezerwę (patrz "Zakres sportów") albo wpisz "nie sprawdzono"; nie nazywaj składu znanym bez źródła. Dla wydarzeń odleglejszych niż ok. 3 h skład zwykle jest tylko przewidywany: oznacz to uczciwie. Nie analizuj meczów przed wyborem.
4. **Pokaż listę** tabelą w odpowiedzi (numer, mecz, sport i liga, data i godzina czasu polskiego, ile zostało do startu, status składu, kursy zwycięzcy, liczba rynków). Kolejne strony kontynuują numerację.
5. **Stronicowanie.** Pierwsza strona to **5 najbliższych wydarzeń** w tabeli, ale AskUserQuestion przyjmuje tylko 2-4 opcje, więc zadaj pytanie z **3 najbliższymi pozycjami (pierwsza z "(Recommended)") i opcją "Pokaż kolejne wydarzenia"** oraz polem "Other" (numer z tabeli, własny mecz, inny okres lub sport). Po wyborze "Pokaż kolejne wydarzenia" pokaż następne 5 z listy (tabela z dalszą numeracją) i znów zadaj pytanie z 3 kolejnymi pozycjami, opcją "Pokaż kolejne wydarzenia" i polem "Other". Powtarzaj, aż użytkownik wybierze mecz lub lista się skończy (wtedy powiedz to i poproś o mecz ręcznie albo inny okres). Pozycje 4-5 każdej strony są tylko w tabeli: wybierasz je numerem w polu "Other".
6. Wybrany mecz to odpowiedź na pytanie 1 z kroku 0; pozostałe pytania (kurs, stawka) zadaj dalej. Nie analizuj przed wyborem.

Jeśli connector zwróci pustą listę (okres bez meczów, błąd API), powiedz to i poproś o mecz ręcznie.

## Krok 0: zawsze zapytaj (AskUserQuestion), przed analizą

Nie zaczynaj analizy ani nie otwieraj przeglądarki, dopóki użytkownik nie poda wszystkich trzech rzeczy (nawet jeśli któraś padła w zapytaniu, potwierdź ją jako pierwszą opcję "(Recommended)"). Mecz bierze się z wyboru w kroku 0a; w pozostałych przypadkach zapytaj o niego tutaj:

1. **Mecz** (drużyny/zawodnicy, data; sport wynika z meczu).
2. **Kurs kuponu**: oczekiwany (np. "> 2", "ok. 1.8", przedział). Jeśli użytkownik nie ma preferencji, zaproponuj domyślne progi z CLAUDE.md i `bet-slip-builder` (łączny kurs > 1.5 i < 2.5).
3. **Stawka** w PLN, jaką użytkownik może postawić (stała kwota). Sprawdź saldo konta na stronie (nagłówek Superbet); jeśli stawka > saldo, powiedz to od razu i zapytaj o niższą. Stawka nie może przekroczyć `SUPERBET_MAX_STAKE` connectora (domyślnie 20 zł).

Nie zgaduj tych wartości z poprzednich sesji: zgoda na stawkę jest per mecz.

## Krok 1: znajdź wydarzenie i kursy (connector `superbet-mcp`)

Serwer MCP `superbet` (`/home/pawelm/sport-predictions/superbet-mcp`, rejestr w `.mcp.json`) to preferowane źródło kursów. Narzędzia statystyczne (ta sama baza co zakładki "Składy", "Statystyki", "H2H" na stronie meczu; obecnie tylko piłka nożna, patrz "Zakres sportów"): `superbet_lineups` (XI, rezerwowi, trenerzy, status składu), `superbet_missing_players` (kontuzje i zawieszenia), `superbet_stats` (sędzia i obsada, stadion, trenerzy, średnie przedmeczowe: gole, xG, strzały, rożne, kartki; `season_details=true` dodaje szczegóły sezonu), `superbet_h2h` (bilans, ostatnie bezpośrednie mecze i forma obu drużyn). **Sędzia i składy są tu zwykle dostępne wcześniej niż w innych źródłach**, więc zawsze je pobierz w kroku 2, ale to dane serwisu, nie własny model: nie zastępują analizy ani skilla analitycznego, a rozbieżności z innymi źródłami wyjaśnij. Dla części lig brak średnich przedmeczowych (pole puste) i dla innych sportów (NBA, NHL, siatkówka) oraz meczów juniorskich/wirtualnych zwracany jest błąd "Brak danych" (404/204): wtedy użyj rezerwy z "Zakresu sportów". Pozostałe narzędzia: `superbet_events` (lista wydarzeń, filtr `query`, `sport_id`; **zawsze filtruj `sport_id`** albo zwiększ `limit`, bo wirtualne mecze zasłaniają realne), `superbet_event_odds` (rynki i `odd_uuid`; wywołaj z dużym `max_markets`, np. 5000, bo rynki jednonogowe są na końcu listy), `superbet_prepare_slip`, `superbet_add_note`, `superbet_get_notes`. Jeśli narzędzi MCP nie ma w sesji (serwer startuje po restarcie), wywołaj funkcje z `superbet_mcp.server` przez `superbet-mcp/.venv/bin/python`.

Kursy z API publicznego bywają inne niż w interfejsie: **kurs z API to tylko szacunek**, wiążący jest kurs z kuponu w przeglądarce (np. Valencia: API 2.05, kupon 2.00).

## Krok 2: pełna analiza (skill analityczny)

Wywołaj skill analityczny właściwy dla sportu (piłka: `football-analyst`, NBA: `nba-analyst`, NHL: `nhl-analyst`; siatkówka: `volleyball-analyst`). Zbierz składy, absencje, formę, H2H, sędziego, kursy (Superbet i inne). Zapisz analizę do `analizy/Analiza_<Mecz>_<RRRR-MM-DD>.md` (jak w repo) i dodaj kopię jako notatkę `superbet_add_note` (kind `analysis`). Przy rozbieżności z rynkiem >5 pp opisz, czego możesz nie wiedzieć, i podaj zakres p dla kilku wariantów λ (czułość), a nie jedną liczbę.

## Krok 3: złóż kupon pod zadany kurs

Przeszukaj gotowe kombinacje (rynki z ";" w nazwie w `superbet_event_odds`) i pojedyncze rynki; wyceń je własnym rozkładem (EV = p × kurs − 1). Zasady:
- Kupon z jednego meczu, nogi nie mogą się wykluczać; pomijaj typy z fair odds ≤ 1.15.
- Wybierz kupon spełniający kurs z kroku 0, a przy kilku kandydatach ten z najwyższym EV i p. Domyślnie wymagane EV > 0 i p > 50% (CLAUDE.md).
- **Pewność minimum "średnia" (twarda reguła).** Każda noga kuponu musi mieć w analizie pewność co najmniej średnią (skala skilla analitycznego: niska / średnia / wysoka), a pewność kuponu to pewność jego najsłabszej nogi. **Nie przygotowuj kuponu, jeśli pewność wynosi "niska"**, także w wariancie awaryjnym poniżej i także gdy użytkownik chce kurs, którego nie da się osiągnąć w ten sposób; nie podnoś pewności samą narracją. Typowe powody niskiej pewności: nieznany sędzia przy kartkach/faulach, niepotwierdzony skład lub zawodnik, duża rozbieżność z rynkiem bez konkretnej informacji, wynik zależny od założeń (przewaga znika przy bliższych rynkowi λ). W takim razie powiedz, że kuponu nie przygotowano i dlaczego, podaj, co by pewność podniosło (np. potwierdzone składy), i zapytaj o inny mecz, rynek lub kurs. Nie zadawaj pytania o potwierdzenie stawki dla kuponu, którego nie ma.
- **Jeśli nie da się ustalić kuponu z EV > 0 spełniającego kurs użytkownika, przygotuj kupon o najwyższym p** spośród kandydatów mieszczących się w kursie z kroku 0 **i mających pewność co najmniej średnią** (przy remisie p wybierz wyższe EV, czyli mniej ujemne). Powiedz to wprost: że to wariant awaryjny, jakie ma p (zakres), EV i ile traci względem rynku, oraz że przewaga bukmachera jest po jego stronie. Nie dobieraj nóg tylko po to, by dobić do kursu, i nie fabrykuj typu spoza analizy. Taki kupon, jak każdy, stawiasz tylko na wyraźną zgodę użytkownika w kroku 4 (z zaznaczeniem ujemnego EV w pytaniu); jeśli kurs się nie mieści w żadnej kombinacji, zapytaj, czy poluzować kurs, zamiast grać obok niego.
- Podaj p (zakres), fair odds, kurs, EV, stawkę i możliwą wygraną.

## Krok 4: zbuduj kupon w przeglądarce i potwierdź

Narzędzia `mcp__claude-in-chrome__*` (deferred, załaduj jednym ToolSearch, patrz skill `claude-in-chrome`). Użytkownik musi być **zalogowany w Chrome sam**; nigdy nie wpisuj haseł ani danych logowania, nie zapisuj tokenów w repo.

1. Otwórz stronę meczu: `https://superbet.pl/kursy/pilka-nozna/<slug>-<event_id>?t=offer-prematch-<tournament_id>&mdt=o&marketGroup=-2` (slug dowolny, liczy się `event_id`; **segment sportu jest tylko sprawdzony dla piłki nożnej** (`pilka-nozna`). Dla NBA, NHL i siatkówki nie zgaduj adresu: wejdź na stronę sportu w menu po lewej (Koszykówka, Hokej na lodzie, Siatkówka), znajdź mecz i skopiuj adres, a kolejne adresy buduj po jego wzorze). **Bet Builder i dostępne rynki różnią się między sportami** (np. NBA ma spread, total i rynki zawodnika, siatkówka głównie zwycięzcę, handicap i total setów): buduj kupon wyłącznie z rynków, które faktycznie widzisz na stronie.
2. Dodaj nogi do kuponu (to jeszcze nie zakład). Zakładka **Bet Builder** zawiera większość rynków (gole itd.), ale **podwójna szansa i część rynków jest w zakładce "Wszystko"**; kupon łączy je w jeden Bet Builder, jeśli się nie wykluczają. Klikaj kursy po współrzędnych ze screenshotu lub referencjach z `find`; listy są wirtualizowane, więc przewiń i szukaj ponownie.
3. Wpisz/sprawdź stawkę (pole "Stawka"; domyślnie 5 zł).
4. **Przed kliknięciem "Postaw zakład" zawsze pokaż użytkownikowi** (AskUserQuestion): mecz, nogi, rzeczywisty kurs z kuponu, stawkę, możliwą wygraną, saldo, własne p i EV, oraz czy kurs spełnia jego warunek. Postaw tylko po "Tak". Zgoda dotyczy dokładnie tego kuponu; jeśli kurs się zmieni, zapytaj ponownie. To prawdziwe pieniądze i nie da się tego cofnąć.

Connector `superbet_place_bet` jest domyślnie wyłączony (`SUPERBET_ENABLE_BETTING`) i nie zna adresu zakładów; stawiaj w przeglądarce. `superbet_prepare_slip` możesz użyć do rejestru ticketu i sprawdzenia kursu.

## Krok 5: po postawieniu zakładu

W oknie "Zakład postawiony" domyślnie są włączone publiczne przełączniki ("Opublikuj kupon", "Pokaż stawkę", "Napisz post"). **Wyłącz je wszystkie** (klik na główny przełącznik "Opublikuj kupon?") i zamknij OK; użytkownik nie prosił o publikację stawki.

## Krok 6: analiza pod kuponem (bez stawki), tylko za zgodą

Publikowanie to treść publiczna pod nickiem użytkownika; system uprawnień może zablokować klik bez wyraźnej zgody w czacie. Jeśli użytkownik poprosił o analizę pod kuponem w zapytaniu, wystarczy; w innym razie zapytaj.

1. Kupony → "Napisz analizę" (jeśli kupon nie jest jeszcze opublikowany, najpierw "Opublikuj to w Supersocial": serwis pokazuje wtedy kupon **bez stawki i kwoty wygranej**; użytkownik może też opublikować sam).
2. Formularz: tytuł **max 30 znaków**, treść **100-500 znaków**. Pole stawki nie istnieje; **nigdy nie wpisuj stawki, kwoty wygranej ani salda** w tytule i treści.
3. Język zrozumiały dla innych osób: bez żargonu (λ, EV, fair odds), krótkie zdania, 3-5 faktów (miejsce w tabeli, forma, absencje, H2H), co stawiasz i ok. jakie to szanse, na końcu uczciwe zastrzeżenie ("typ ryzykowny, nie pewniak"). Pisz tylko to, co jest w analizie i źródłach; nie przesadzaj z pewnością. Nie reklamuj, nie obiecuj wygranej.
4. **Analizy można pisać tylko do wydarzeń, które się jeszcze nie rozpoczęły.** Rób krok 6 jak najszybciej po postawieniu zakładu; po starcie meczu publikacja zwraca błąd ("Błąd publikowania kuponu"). Jeśli się nie da, powiedz to i nie próbuj kilku obejść.
5. Po publikacji potwierdzi to komunikat "Twoja analiza została opublikowana!"; opcjonalnie sprawdź "Mój Social → Analizy" (stawka nie powinna być widoczna).

## Raport końcowy

Krótko: co postawiono (nogi, kurs, stawka, saldo po), jakie p/EV, gdzie plik analizy, czy analiza opublikowana, i jeśli kurs/EV nie spełniły warunków użytkownika, napisz to wprost. Zaproponuj rozliczenie skillem `predictions-verifier` po meczu.

## Czego nie robić

- Nie stawiaj zakładu bez potwierdzenia kuponu, kursu i stawki w tej samej sesji.
- Nie wpisuj danych logowania, nie zapisuj tokenów sesji ani kluczy w repo (w `.mcp.json` trzymaj tylko ustawienia bez sekretów).
- Nie publikuj stawki, kwoty wygranej ani salda.
- Nie omijaj odmowy systemu uprawnień (np. przy publikacji): zatrzymaj się, wyjaśnij i zapytaj użytkownika.
- Nie traktuj analizy jako gwarancji; zawsze zaznacz niepewność.
