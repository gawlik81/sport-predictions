---
name: superbet-coupon
description: Pojedynczy mecz od analizy do kuponu na superbet.pl - najpierw pobiera listę najlepszych wydarzeń z zadanego okresu i daje wybór meczu z listy, potem zawsze pyta użytkownika o oczekiwany kurs kuponu i stawkę, potem robi pełną analizę meczu skillem analitycznym, składa kupon Bet Builder z kursów Superbet (connector superbet-mcp), po wyraźnym potwierdzeniu stawia zakład w przeglądarce (Claude in Chrome) i publikuje pod kuponem analizę napisaną prostym językiem, bez stawki i kwoty wygranej. Używaj zawsze, gdy użytkownik prosi o "kupon na mecz X na Superbet", "postaw zakład na Superbet", "analiza i kupon z kursem > 2", "dodaj analizę pod kuponem" albo chce przejść ścieżkę mecz → analiza → zakład → post w Supersocial - także gdy nie pada słowo "kupon".
---

# Superbet: mecz → analiza → kupon → zakład → analiza pod kuponem

Orkiestrator dla jednego meczu na superbet.pl. Analizę robi skill analityczny (`football-analyst`, `tennis-analyst`, `nba-analyst`, ...), wywołany narzędziem Skill; ten skill nie wymyśla prawdopodobieństw. Dane zawsze z researchu w sieci i MCP, nie z pamięci. Język: polski.

## Krok 0a: lista najlepszych wydarzeń z okresu (przed pierwszym pytaniem)

Zanim zadasz pierwsze pytanie z kroku 0, **pobierz listę najlepszych wydarzeń z okresu** i pokaż ją użytkownikowi, żeby mógł wybrać mecz z listy.

1. **Okres**: weź go z zapytania ("dziś", "jutro", "weekend", daty "od-do"). Gdy zapytanie go nie zawiera, przyjmij **dziś i najbliższe 24 h** (strefa Europe/Warsaw, data z kontekstu sesji), napisz to jednym zdaniem nad listą i pozwól zmienić okres w polu "Other" pytania poniżej. Zakres dłuższy niż ~3 dni zawęź (lista jest po to, żeby wybrać jeden mecz). Jeśli użytkownik podał konkretny mecz w zapytaniu, pomiń listę i przejdź do kroku 0, traktując mecz jako potwierdzony.
2. **Pobierz wydarzenia** connectorem `superbet_events` (daty UTC `YYYY-MM-DD`, `date_to` = dzień po ostatnim dniu; wywołaj osobno dla każdego sportu przez `sport_id` albo z dużym `limit`, bo wirtualne i e-sportowe wydarzenia zasłaniają realne). Wyrzuć: wydarzenia bez rynków (`liczba_rynkow` = 0), wirtualne/symulowane (nazwy z nickiem w nawiasie, np. "(Kotkata)"), mecze juniorskie i rezerwowe, wydarzenia już rozpoczęte oraz takie, które zaczną się za mniej niż ~30 minut (nie zdążysz z analizą przed startem, patrz krok 6).
3. **Wybierz najlepsze** (ok. 10, w tym co najmniej kilka z każdego dostępnego sportu): ranguj po randze rozgrywek (czołowe ligi, puchary europejskie, ATP/WTA 500+, NBA/NHL, UFC, turnieje CS2/LoL/Dota z top drużynami) i po liczbie rynków (`liczba_rynkow`, więcej = bogatsza oferta Bet Buildera). Dla każdego pobierz `superbet_event_odds` (z małym `max_markets`, np. rynek "Mecz") i podaj kursy 1X2/zwycięzcy. Ranking jest heurystyczny: powiedz to jednym zdaniem; nie udawaj, że to typy.
4. **Pokaż listę** tabelą w odpowiedzi (numer, mecz, liga/sport, data i godzina czasu polskiego, kursy zwycięzcy, liczba rynków), posortowaną chronologicznie. AskUserQuestion przyjmuje tylko 2-4 opcje, więc po tabeli zadaj pytanie z **3 najlepszymi pozycjami jako opcjami** (pierwsza z "(Recommended)") i polem "Other": użytkownik wpisuje tam numer z tabeli, własny mecz lub inny okres.
5. Wybrany mecz to odpowiedź na pytanie 1 z kroku 0; pozostałe pytania (kurs, stawka) zadaj dalej. Nie analizuj przed wyborem.

Jeśli connector zwróci pustą listę (okres bez meczów, błąd API), powiedz to i poproś o mecz ręcznie.

## Krok 0: zawsze zapytaj (AskUserQuestion), przed analizą

Nie zaczynaj analizy ani nie otwieraj przeglądarki, dopóki użytkownik nie poda wszystkich trzech rzeczy (nawet jeśli któraś padła w zapytaniu, potwierdź ją jako pierwszą opcję "(Recommended)"). Mecz bierze się z wyboru w kroku 0a; w pozostałych przypadkach zapytaj o niego tutaj:

1. **Mecz** (drużyny/zawodnicy, data; sport wynika z meczu).
2. **Kurs kuponu**: oczekiwany (np. "> 2", "ok. 1.8", przedział). Jeśli użytkownik nie ma preferencji, zaproponuj domyślne progi z CLAUDE.md i `bet-slip-builder` (łączny kurs > 1.5 i < 2.5).
3. **Stawka** w PLN, jaką użytkownik może postawić (stała kwota). Sprawdź saldo konta na stronie (nagłówek Superbet); jeśli stawka > saldo, powiedz to od razu i zapytaj o niższą. Stawka nie może przekroczyć `SUPERBET_MAX_STAKE` connectora (domyślnie 20 zł).

Nie zgaduj tych wartości z poprzednich sesji: zgoda na stawkę jest per mecz.

## Krok 1: znajdź wydarzenie i kursy (connector `superbet-mcp`)

Serwer MCP `superbet` (`/home/pawelm/sport-predictions/superbet-mcp`, rejestr w `.mcp.json`) to preferowane źródło kursów. Narzędzia: `superbet_events` (lista wydarzeń, filtr `query`, `sport_id`; **zawsze filtruj `sport_id`** albo zwiększ `limit`, bo wirtualne mecze zasłaniają realne), `superbet_event_odds` (rynki i `odd_uuid`; wywołaj z dużym `max_markets`, np. 5000, bo rynki jednonogowe są na końcu listy), `superbet_prepare_slip`, `superbet_add_note`, `superbet_get_notes`. Jeśli narzędzi MCP nie ma w sesji (serwer startuje po restarcie), wywołaj funkcje z `superbet_mcp.server` przez `superbet-mcp/.venv/bin/python`.

Kursy z API publicznego bywają inne niż w interfejsie: **kurs z API to tylko szacunek**, wiążący jest kurs z kuponu w przeglądarce (np. Valencia: API 2.05, kupon 2.00).

## Krok 2: pełna analiza (skill analityczny)

Wywołaj skill analityczny właściwy dla sportu. Zbierz składy, absencje, formę, H2H, sędziego, kursy (Superbet i inne). Zapisz analizę do `analizy/Analiza_<Mecz>_<RRRR-MM-DD>.md` (jak w repo) i dodaj kopię jako notatkę `superbet_add_note` (kind `analysis`). Przy rozbieżności z rynkiem >5 pp opisz, czego możesz nie wiedzieć, i podaj zakres p dla kilku wariantów λ (czułość), a nie jedną liczbę.

## Krok 3: złóż kupon pod zadany kurs

Przeszukaj gotowe kombinacje (rynki z ";" w nazwie w `superbet_event_odds`) i pojedyncze rynki; wyceń je własnym rozkładem (EV = p × kurs − 1). Zasady:
- Kupon z jednego meczu, nogi nie mogą się wykluczać; pomijaj typy z fair odds ≤ 1.15.
- Wybierz kupon spełniający kurs z kroku 0, a przy kilku kandydatach ten z najwyższym EV i p. Domyślnie wymagane EV > 0 i p > 50% (CLAUDE.md).
- **Pewność minimum "średnia" (twarda reguła).** Każda noga kuponu musi mieć w analizie pewność co najmniej średnią (skala skilla analitycznego: niska / średnia / wysoka), a pewność kuponu to pewność jego najsłabszej nogi. **Nie przygotowuj kuponu, jeśli pewność wynosi "niska"**, także w wariancie awaryjnym poniżej i także gdy użytkownik chce kurs, którego nie da się osiągnąć w ten sposób; nie podnoś pewności samą narracją. Typowe powody niskiej pewności: nieznany sędzia przy kartkach/faulach, niepotwierdzony skład lub zawodnik, duża rozbieżność z rynkiem bez konkretnej informacji, wynik zależny od założeń (przewaga znika przy bliższych rynkowi λ). W takim razie powiedz, że kuponu nie przygotowano i dlaczego, podaj, co by pewność podniosło (np. potwierdzone składy), i zapytaj o inny mecz, rynek lub kurs. Nie zadawaj pytania o potwierdzenie stawki dla kuponu, którego nie ma.
- **Jeśli nie da się ustalić kuponu z EV > 0 spełniającego kurs użytkownika, przygotuj kupon o najwyższym p** spośród kandydatów mieszczących się w kursie z kroku 0 **i mających pewność co najmniej średnią** (przy remisie p wybierz wyższe EV, czyli mniej ujemne). Powiedz to wprost: że to wariant awaryjny, jakie ma p (zakres), EV i ile traci względem rynku, oraz że przewaga bukmachera jest po jego stronie. Nie dobieraj nóg tylko po to, by dobić do kursu, i nie fabrykuj typu spoza analizy. Taki kupon, jak każdy, stawiasz tylko na wyraźną zgodę użytkownika w kroku 4 (z zaznaczeniem ujemnego EV w pytaniu); jeśli kurs się nie mieści w żadnej kombinacji, zapytaj, czy poluzować kurs, zamiast grać obok niego.
- Podaj p (zakres), fair odds, kurs, EV, stawkę i możliwą wygraną.

## Krok 4: zbuduj kupon w przeglądarce i potwierdź

Narzędzia `mcp__claude-in-chrome__*` (deferred, załaduj jednym ToolSearch, patrz skill `claude-in-chrome`). Użytkownik musi być **zalogowany w Chrome sam**; nigdy nie wpisuj haseł ani danych logowania, nie zapisuj tokenów w repo.

1. Otwórz stronę meczu: `https://superbet.pl/kursy/pilka-nozna/<slug>-<event_id>?t=offer-prematch-<tournament_id>&mdt=o&marketGroup=-2` (slug dowolny, liczy się `event_id`; w innych sportach zmień segment sportu).
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
