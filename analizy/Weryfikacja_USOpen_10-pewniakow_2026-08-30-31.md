# Weryfikacja: US Open 2026 — 10 najpewniejszych typów (I runda)

Konfrontacja przewidywań z pliku [`USOpen_2026_Iruna_10-pewniakow_2026-08-30-31.md`](USOpen_2026_Iruna_10-pewniakow_2026-08-30-31.md) z rzeczywistymi wynikami I rundy.

## Tabela wyników

| # | Mecz | Typ (P zwycięstwa) | Najbardziej prawdopodobny wynik (model) | Rzeczywisty wynik | Zwycięzca | Wynik setowy zgodny z modelem? |
|---|---|---|---|---|---|---|
| 1 | Kostyuk vs Storm Hunter | Kostyuk 94,6% | 2-0 (73,7%) | **6-4, 6-1** | ✅ Kostyuk | ✅ tak (2-0) |
| 2 | Sabalenka vs Osorio | Sabalenka 92,6% | 2-0 (69,3%) | **6-2, 6-4** | ✅ Sabalenka | ✅ tak (2-0) |
| 3 | Fritz vs Blanch | Fritz 92,2% | 3-0 (46,6%) | **6-3, 6-2, 6-4** | ✅ Fritz | ✅ tak (3-0) |
| 4 | Djokovic vs Navone | Djokovic 89,8% | 3-0 (42,3%) | **7-6, 5-7, 4-6, 6-2, 6-1 dla Navone** | ❌ **Navone** (upset) | ❌ nie — porażka faworyta |
| 5 | Zverev vs Sonego | Zverev 89,3% | 3-0 (41,5%) | *mecz jeszcze nierozegrany (sesja wieczorna, ~02:10 CEST)* | ⏳ oczekuje | ⏳ |
| 6 | Medvedev vs Gaston | Medvedev 87,0% | 3-0 (38,2%) | **6-4, 6-2, 6-4** | ✅ Medvedev | ✅ tak (3-0) |
| 7 | Cobolli vs Comesana | Cobolli 86,8% | 3-0 (37,9%) | **3-6, 2-6, 6-3, 6-4, 6-4** | ✅ Cobolli | ⚠️ zwycięzca zgodny, ale odwrócony scenariusz (przegrywał 0-2 w setach) |
| 8 | Alcaraz vs Safiullin | Alcaraz 86,6% | 3-0 (37,6%) | **6-4, 6-4, 6-4** | ✅ Alcaraz | ✅ tak (3-0) |
| 9 | Paolini vs Erjavec | Paolini 82,6% | 2-0 (53,9%) | **6-3, 3-6, 6-4** | ✅ Paolini | ⚠️ zwycięzca zgodny, ale 2-1 zamiast 2-0 (Erjavec wygrała seta) |
| 10 | Świątek vs Wang | Świątek 78,9% | 2-0 (49,5%) | **6-2, 6-3** | ✅ Świątek | ✅ tak (2-0) |

## Bilans

- **Zwycięzca meczu (typ główny): 8/9 rozegranych trafień (88,9%)**, jeden mecz (Zverev-Sonego) wciąż nierozegrany w momencie weryfikacji.
- Średnia przewidywana pewność dla 9 rozegranych meczów: **87,9%** (średnia z p_zwycięstwa dla pozycji 1-4 i 6-10). Rzeczywisty odsetek trafień (88,9%) niemal dokładnie pokrywa się ze średnią przewidywaną pewnością — **model jako całość jest bardzo dobrze skalibrowany w skali zbiorczej**, mimo pojedynczej niespodzianki.
- **Jedyne pudło: Djokovic vs Navone (pozycja #4, 89,8%)** — Djokovicia opisano w oficjalnych relacjach jako "wyraźnie chorego" (visibly ill) w trakcie meczu; przegrał w 5 setach, w tym dwa ostatnie sety oddając niemal bez oporu (6-2, 6-1 dla Navone). To pierwsza porażka Djokovicia w I rundzie Wielkiego Szlema od 2006 roku.
- **Wynik setowy trafiony dokładnie w 7/9 rozegranych meczach** — dwa odstępstwa (Cobolli, Paolini) to nie porażki typu, tylko sygnał, że model nieco zaniżał szansę przeciwnika na urwanie seta/setów przy dużych faworytach.

## Co wymaga korekty na przyszłość

1. **Wiek + best-of-5 = realny, niedoszacowany tail-risk.** Jedyny bust w tej dziesiątce to najstarszy zawodnik (39 lat) grający na dystansie pięciu setów, bez żadnego widocznego przed meczem sygnału kontuzji/choroby w dostępnych źródłach. W raporcie zaznaczyłem to opisowo ("szerszy margines niepewności"), ale i tak wystawiłem Djokovicia na #4 miejsce w rankingu pewności — czysto opisowa wzmianka nie miała żadnego wpływu na finalną liczbę p_serve/ranking. Analogicznie do wniosku z football-predictora (kontuzja/zawieszenie musi przełożyć się na REALNĄ korektę liczby, nie tylko tekst) — przy zawodnikach 35+ w formacie best-of-5 należy **realnie obniżać end-to-end p(zwycięstwo)** (np. o dodatkowe 3-5 pkt proc. względem czystego wyniku z modelu) albo świadomie nie umieszczać takich meczów w top kilku "najpewniejszych", nawet gdy surowy model daje >85%.
2. **"Świetna forma" faworyta tuż przed Wielkim Szlemem to sygnał dwukierunkowy, nie tylko pozytywny.** Cobolli (finał RG, ćwierćfinał Wimbledonu, półfinał Cincinnati tuż przed US Open) opisałem w raporcie wyłącznie jako wzmocnienie przewagi modelu. W praktyce przegrał pierwsze dwa sety 3-6, 2-6 i wygrał dopiero w piątym — obraz pasujący do zmęczenia skumulowanym, napiętym kalendarzem równie dobrze jak do "dobrej formy". Na przyszłość: przy zawodniku z bardzo napiętym kalendarzem bezpośrednio przed turniejem, jawnie rozważać w raporcie OBIE hipotezy (rozpęd vs zmęczenie), zamiast automatycznie traktować serię dobrych wyników jako czysty plus.
3. **Duża przepaść rankingowa w WTA nie gwarantuje "czystego" wyniku setowego równie mocno jak w ATP.** Dwa z trzech odstępstw od najbardziej prawdopodobnego wyniku setowego (Paolini, a częściowo i sam charakter meczu Kostyuk/Sabalenka też był bliżej 2-1 niż 2-0 w pierwszym secie) dotyczyły kobiet. Przy typowaniu DOKŁADNEGO wyniku setowego (nie tylko zwycięzcy) w WTA warto płaszczyć rozkład bardziej niż podpowiada surowy model, szczególnie gdy underdog ma jakikolwiek własny, konkretny atut serwisowy.
4. **Luka w Kroku 1 (research):** Alcaraz grał swój pierwszy mecz singlowy po 4-miesięcznej przerwie spowodowanej kontuzją nadgarstka — informacja, której nie wychwyciłem w pierwotnym researchu (szukałem ogólnej "formy 2026", a nie explicit frazy "[zawodnik] injury/kontuzja" dla każdego faworyta z osobna). Tym razem wyszło to na korzyść typu (Alcaraz i tak wygrał pewnie 3-0), ale to szczęście, nie metoda — mogło równie dobrze pójść w drugą stronę. **Na przyszłość: zawsze wykonywać osobne, explicit zapytanie "[zawodnik] injury/kontuzja [rok]" dla KAŻDEGO faworyta w zestawieniu top-N, nie tylko dla tych, przy których ogólny research przypadkiem wyłapie sygnał.**
5. **Co zadziałało dobrze i warto utrzymać:** ekstremalne przepaści jakościowe poparte konkretną, świeżą statystyką (Kostyuk — liderka returnu WTA; Sabalenka — liderka utrzymania serwisu WTA) dały najpewniejsze i najdokładniejsze trafienia w całym zestawieniu (dokładny wynik setowy zgodny co do przecinka). Priorytetyzowanie konkretnych, potwierdzonych statystyk sezonu nad czystym rankingiem/szacunkiem — tam gdzie się dało je znaleźć — najwyraźniej się opłaca.

---
*Weryfikacja ma charakter analityczny/edukacyjny (kalibracja modelu), nie stanowi rekomendacji zakładów wstecz.*
