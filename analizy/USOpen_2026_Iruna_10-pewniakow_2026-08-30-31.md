> **Aktualizacja:** wyniki tych typów zostały zweryfikowane względem rzeczywistego przebiegu I rundy —
> zobacz [`Weryfikacja_USOpen_10-pewniakow_2026-08-30-31.md`](Weryfikacja_USOpen_10-pewniakow_2026-08-30-31.md)
> (8/9 rozegranych trafień, jedno pudło: Djokovic–Navone, plus wnioski do kalibracji modelu na przyszłość).

# US Open 2026 — 10 najpewniejszych typów (I runda, 30–31 sierpnia)

**Turniej:** US Open 2026 (Nowy Jork, Wielki Szlem, nawierzchnia twarda) | **Runda:** I runda (mecze rozłożone na dwie sesje dziennie i wieczorne, 30–31.08) | **Format:** mężczyźni best-of-5, kobiety best-of-3

## Metodologia i ważne zastrzeżenia

- Turniej główny wystartował dokładnie dziś, **30 sierpnia 2026** — to dzień 1. drabinki, a 31 sierpnia to dzień 2. (dokończenie I rundy). Zakres tej analizy: obie sesje z obu dni.
- **Ważna zmiana regulaminu na 2026 rok**: US Open ujednolicił zasady tiebreaka w secie decydującym z pozostałymi Wielkimi Szlemami — od 2026 roku przy 6-6 w secie decydującym gra się tiebreak **do 10 punktów** (wcześniej był to standardowy tiebreak do 7). Zweryfikowałem to bezpośrednio przez research, a nie z pamięci — model poniżej używa `--final-set-tiebreak-to 10` dla wszystkich meczów.
- **Jannik Sinner (ranking ATP #1) wycofał się z turnieju** z powodu kontuzji kolana — to pierwsza nieobecność Sinnera na Wielkim Szlemie od debiutu w 2019 roku. Zniknięcie lidera rankingu przesunęło numerację siewu o jedno miejsce w górę dla wszystkich pozostałych zawodników.
- Spośród kilkunastu meczów I rundy z dużą różnicą jakości między zawodnikami przepuściłem każdy przez pełny model punkt→gem→set→mecz (`tennis_model.py`), a następnie **posortowałem wszystkie po obliczonym prawdopodobieństwie zwycięstwa faworyta** — to jest kryterium "najpewniejszy typ" w tym zestawieniu, nie sama różnica w rankingu.
- **Zastrzeżenie co do precyzji danych wejściowych**: dla topowych zawodników (Sabalenka, Kostyuk) udało się znaleźć konkretne, aktualne statystyki sezonu 2026 (opisane przy każdym meczu). Dla większości przeciwników z dalszych miejsc rankingu (np. Blanch, Navone, Comesana, Storm Hunter, Osorio, Sonego, Erjavec, Gaston, Wang, Safiullin) nie znalazłem publicznie dostępnego rozbicia % serwisu/returnu na nawierzchni twardej w bieżącym sezonie — `p_a_serve`/`p_b_serve` dla tych zawodników są więc **szacunkiem opartym na randze/rankingu, stylu gry i średnich turowych** (ATP twarda ~64%/36%, WTA twarda ~56%/44%), a nie na twardych statystykach point-by-point. Zaznaczam to przy każdym meczu, gdzie dotyczy.
- Ta wersja skupia się — zgodnie z priorytetami tego skilla — na **zwycięzcy meczu** i **total gemów** dla każdego meczu; statystyki drugorzędne (asy, podwójne błędy, break pointy) pomijam w tym zbiorczym zestawieniu 10 meczów, żeby nie rozdmuchać raportu ponad miarę — chętnie dociągnę je na żądanie dla konkretnego meczu.

---

## Ranking 10 najpewniejszych typów

### 1. Marta Kostyuk [11] vs Storm Hunter — 94,6%
**Niedziela 30.08, Grandstand, sesja dzienna | WTA, best-of-3**

- Kostyuk to obecnie **liderka returnu na WTA Tour** (48,7% wygranych punktów returnem po sezonie 2026) — to konkretna, potwierdzona statystyka, nie szacunek.
- Storm Hunter (ranking singlowy ok. #186–193) to przede wszystkim **specjalistka deblowa** (była liderka rankingu deblowego WTA), wracająca do gry singlowej po **operacji ścięgna Achillesa**. To jeden z największych realnych rozjazdów jakości w całej drabince.
- p_serve: Kostyuk 58% / Hunter 46% (Hunter — szacunek luźniejszy, dane serwisowe z touru singlowego skąpe).
- **Zwycięzca meczu:** Kostyuk 94,6% (kurs uczciwy 1,06) / Hunter 5,4% (18,58)
- **Dokładny wynik:** 2-0 — 73,7% | 2-1 — 20,9%
- **Total gemów** (priorytet analizy): oczekiwane **~20,1**; Under 17,5 — 40,1% / Over — 59,9%; Under 19,5 — 58,1% / Over — 41,9%
- Pierwszy set: Kostyuk 85,9% / Hunter 14,1%

### 2. Aryna Sabalenka [1] vs Camila Osorio — 92,6%
**Poniedziałek 31.08, kort i godzina do potwierdzenia w oficjalnym Order of Play | WTA, best-of-3**

- Sabalenka to lider WTA w utrzymywaniu serwisu (86,6% wygranych gemów serwisowych w sezonie 2026) — konkretna, świeża statystyka.
- Osorio (ranking ok. #58) to solidna kontrpunkterka, ale wyraźnie niższej klasy niż liderka rankingu.
- p_serve: Sabalenka 63% / Osorio 52% (Osorio — szacunek na bazie rankingu i stylu, bez precyzyjnych splitów na twardej).
- **Zwycięzca meczu:** Sabalenka 92,6% (1,08) / Osorio 7,4% (13,49)
- **Dokładny wynik:** 2-0 — 69,3% | 2-1 — 23,3%
- **Total gemów:** oczekiwane **~21,0**; Under 18,5 — 43,7% / Over — 56,4%; Under 20,5 — 57,8% / Over — 42,2%
- Pierwszy set: Sabalenka 83,2% / Osorio 16,8%

### 3. Taylor Fritz [9] vs Darwin Blanch — 92,2%
**Poniedziałek 31.08, Arthur Ashe Stadium, ok. 16:30 (sesja dzienna) | ATP, best-of-5**

- Blanch to **18-letni dziki kart**, ranking ok. #228, debiutant na tym poziomie — jeden z największych rozjazdów jakości w drabince męskiej.
- **Ważny kontekst obniżający pewność:** Fritz zmaga się z przewlekłym zapaleniem ścięgna w kolanie (nawrót pod koniec marca, przerwa w sezonie na turniejach Masters na mączce) i w Cincinnati tuż przed US Open przegrał wcześnie z Nakashimą, wyraźnie sfrustrowany formą. To nie zagraża faworytyzmowi w tym konkretnym meczu, ale lekko podnosi ryzyko gorszej dyspozycji/kontuzji w trakcie meczu best-of-5 — warto to mieć z tyłu głowy.
- p_serve: Fritz 67% / Blanch 58% (Blanch — szacunek luźny, młody zawodnik bez pełnej historii serwisowej na turze).
- **Zwycięzca meczu:** Fritz 92,2% (1,08) / Blanch 7,8% (12,83)
- **Dokładny wynik:** 3-0 — 46,6% | 3-1 — 31,4% | 3-2 — 14,2%
- **Total gemów:** oczekiwane **~35,9** (best-of-5 znacząco podbija total względem meczów kobiet); Under 28,5 — 25,9% / Over — 74,1%; Under 32,5 — 43,2% / Over — 56,8%
- Pierwszy set: Fritz 77,5% / Blanch 22,5%

### 4. Novak Djokovic [4] vs Mariano Navone — 89,8%
**Niedziela 30.08, Arthur Ashe Stadium, sesja wieczorna (ok. północy) | ATP, best-of-5**

- Djokovic wciąż ma jeden z najlepszych returnów na turze nawet w wieku 39 lat; Navone (ranking ok. #38–48) to zawodnik wyraźnie mocniejszy na mączce niż na twardej.
- **Kontekst do obserwacji:** wiek i wytrzymałość Djokovicia na dystansie best-of-5 to naturalny czynnik ryzyka w każdym jego meczu na Wielkim Szlemie — nie znalazłem żadnych świeżych sygnałów kontuzji przed turniejem, ale to jedyny mecz w tym zestawieniu, gdzie warto mentalnie doliczyć nieco szerszy margines niepewności z tego powodu.
- p_serve: Djokovic 66% / Navone 58% (Navone — szacunek na bazie rankingu/stylu, słabszy na twardej niż na mączce).
- **Zwycięzca meczu:** Djokovic 89,8% (1,11) / Navone 10,2% (9,77)
- **Dokładny wynik:** 3-0 — 42,3% | 3-1 — 31,6% | 3-2 — 15,9%
- **Total gemów:** oczekiwane **~36,7**; Under 29,5 — 27,5% / Over — 72,5%; Under 33,5 — 42,1% / Over — 57,9%
- Pierwszy set: Djokovic 75,1% / Navone 24,9%

### 5. Alexander Zverev [1] vs Lorenzo Sonego — 89,3%
**Poniedziałek 31.08, Arthur Ashe Stadium, sesja wieczorna (ok. północy) | ATP, best-of-5**

- Zverev jako lider siewu ma za sobą udany sezon 2026 (finał Roland Garros, w którym pokonał Cobollego w 5 setach) i jest w formie sprzyjającej dominacji serwisowej. Sonego (ranking wahał się w tym roku między #40 a #91 zależnie od okresu) to solidny, ale niższej klasy przeciwnik na twardej.
- p_serve: Zverev 68% / Sonego 60% (Sonego — szacunek na bazie rankingu/stylu).
- **Zwycięzca meczu:** Zverev 89,3% (1,12) / Sonego 10,7% (9,35)
- **Dokładny wynik:** 3-0 — 41,5% | 3-1 — 31,6% | 3-2 — 16,2%
- **Total gemów:** oczekiwane **~37,5**; Under 29,5 — 24,6% / Over — 75,4%; Under 33,5 — 39,7% / Over — 60,3%
- Pierwszy set: Zverev 74,6% / Sonego 25,4%

### 6. Daniil Medvedev [7] vs Hugo Gaston — 87,0%
**Niedziela 30.08, Arthur Ashe Stadium, ok. 17:00 (sesja dzienna) | ATP, best-of-5**

- Medvedev (ranking ok. #8–9) ma nietypowy, ale bardzo skuteczny na twardej styl gry oparty na returnie. Gaston (ranking ok. #88–99) to niski, kreatywny zawodnik lepiej czujący się na mączce/kortach halowych niż na szybkiej twardej nawierzchni US Open.
- p_serve: Medvedev 64% / Gaston 57% (Gaston — szacunek na bazie rankingu/stylu).
- **Zwycięzca meczu:** Medvedev 87,0% (1,15) / Gaston 13,0% (7,68)
- **Dokładny wynik:** 3-0 — 38,2% | 3-1 — 31,5% | 3-2 — 17,3%
- **Total gemów:** oczekiwane **~37,2**; Under 29,5 — 25,5% / Over — 74,6%; Under 33,5 — 39,4% / Over — 60,6%
- Pierwszy set: Medvedev 72,6% / Gaston 27,4%

### 7. Flavio Cobolli [5] vs Francisco Comesana — 86,8%
**Poniedziałek 31.08, Louis Armstrong Stadium, ok. 16:00 (sesja dzienna) | ATP, best-of-5**

- Cobolli przeżywa najlepszy sezon kariery: wszedł do Top 10 po finale Roland Garros, doszedł do ćwierćfinału Wimbledonu i półfinału Cincinnati tuż przed US Open — silny sygnał formy wzmacniający przewagę modelu. Comesana (ranking ok. #102) to zawodnik bardziej mączkowy, słabszy na szybkiej twardej.
- p_serve: Cobolli 65% / Comesana 58% (Comesana — szacunek na bazie rankingu/stylu).
- **Zwycięzca meczu:** Cobolli 86,8% (1,15) / Comesana 13,2% (7,56)
- **Dokładny wynik:** 3-0 — 37,9% | 3-1 — 31,4% | 3-2 — 17,4%
- **Total gemów:** oczekiwane **~37,5**; Under 29,5 — 24,4% / Over — 75,6%; Under 33,5 — 38,4% / Over — 61,6%
- Pierwszy set: Cobolli 72,4% / Comesana 27,6%

### 8. Carlos Alcaraz [2] vs Roman Safiullin — 86,6%
**Poniedziałek 31.08, Arthur Ashe Stadium, sesja dzienna (drugi mecz sesji) | ATP, best-of-5**

- Alcaraz broni tytułu z 2025 roku i wchodzi w turniej jako jeden z dwóch głównych faworytów do tytułu (obok Zvereva) po nieobecności Sinnera. Safiullin (ranking ok. #142–144) to solidny, ale wyraźnie niżej notowany rywal.
- p_serve: Alcaraz 66% / Safiullin 59% (Safiullin — szacunek na bazie rankingu/stylu).
- **Zwycięzca meczu:** Alcaraz 86,6% (1,16) / Safiullin 13,5% (7,43)
- **Dokładny wynik:** 3-0 — 37,6% | 3-1 — 31,4% | 3-2 — 17,5%
- **Total gemów:** oczekiwane **~37,9**; Under 28,5 — 19,2% / Over — 80,8%; Under 32,5 — 34,7% / Over — 65,3%
- Pierwszy set: Alcaraz 72,2% / Safiullin 27,8%

### 9. Jasmine Paolini [19] vs Veronika Erjavec — 82,6%
**Niedziela 30.08, Louis Armstrong Stadium, ok. 16:00 (sesja dzienna) | WTA, best-of-3**

- Paolini to solidna, wszechstronna zawodniczka rozstawiona z 19. numerem. Erjavec (ranking wahał się w 2026 między #86 a #109) to zawodniczka niższego pułapu, w tym meczu wyraźna outsiderka.
- p_serve: Paolini 57% / Erjavec 50% (Erjavec — szacunek na bazie rankingu/stylu).
- **Zwycięzca meczu:** Paolini 82,6% (1,21) / Erjavec 17,4% (5,75)
- **Dokładny wynik:** 2-0 — 53,9% | 2-1 — 28,7%
- **Total gemów:** oczekiwane **~22,5**; Under 18,5 — 31,7% / Over — 68,3%; Under 20,5 — 45,8% / Over — 54,3%
- Pierwszy set: Paolini 73,4% / Erjavec 26,6%

### 10. Iga Świątek [8] vs Xiyu Wang — 78,9%
**Poniedziałek 31.08, Louis Armstrong Stadium, kort/godzina w ramach sesji dziennej lub wieczornej — do potwierdzenia | WTA, best-of-3**

- Świątek, była liderka rankingu i mistrzyni US Open 2022, mierzy się z solidną, ale wyraźnie niżej notowaną Xiyu Wang. To najniższa pozycja w tej dziesiątce — różnica klasy jest realna, ale mniejsza niż w pozostałych dziewięciu meczach, więc mimo miejsca w rankingu "10 najpewniejszych" traktuj to jako najmniej jednostronny z tej grupy.
- p_serve: Świątek 57% / Wang 51% (obie wartości — szacunek na bazie rankingu/stylu, bez precyzyjnych splitów serwisowych na twardej w 2026).
- **Zwycięzca meczu:** Świątek 78,9% (1,27) / Wang 21,1% (4,74)
- **Dokładny wynik:** 2-0 — 49,5% | 2-1 — 29,4%
- **Total gemów:** oczekiwane **~23,0**; Under 19,5 — 36,3% / Over — 63,7%; Under 21,5 — 47,8% / Over — 52,2%
- Pierwszy set: Świątek 70,4% / Wang 29,6%

---

## Podsumowanie

Najpewniejszy typ w tym zestawieniu to **Kostyuk – Storm Hunter (94,6%)**, gdzie o przewadze decyduje nie tylko ranking, ale też konkretna, potwierdzona statystyka: Kostyuk jest liderką returnu na całym torze WTA, a Hunter wraca do gry singlowej po poważnej kontuzji, będąc przede wszystkim specjalistką deblową. Warto zwrócić uwagę, że **best-of-5 u mężczyzn systematycznie podbija total gemów** (oczekiwane ~36–38 gemów) względem meczów kobiecych (oczekiwane ~20–23) — to efekt samego formatu, a nie różnicy w stylu gry, i tłumaczy, dlaczego linie Over/Under w tabelach różnią się tak mocno między dwiema grupami meczów. Jedyne dwa realne czynniki ryzyka w tej dziesiątce to: kontuzja kolana Fritza (pozycja 3) oraz wiek/wytrzymałość Djokovicia na dystansie pięciu setów (pozycja 4) — żaden z nich nie zagraża faworytyzmowi, ale oba warto mieć na uwadze przy ewentualnych zakładach na dokładny wynik czy total gemów, gdzie krótszy mecz jest mniej prawdopodobny przy nagłym spadku formy.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
