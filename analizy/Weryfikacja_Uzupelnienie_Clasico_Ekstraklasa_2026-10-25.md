# Uzupełnienie weryfikacji 25.10.2026: El Clásico (rynki dodatkowe) i Ekstraklasa (weryfikacja 29.10)

**Pliki:** `ZWERYFIKOWANE_ElClasico_Barcelona_RealMadryt_2026-10-25.md` (uzupełnione rożne, kartki, faule, strzały, rynki zawodnika i rynki golowe) oraz `ZWERYFIKOWANE_Analiza_dnia_2026-10-25.md` (uzupełnione 3 mecze Ekstraklasy). Oba pliki mają teraz prefiks; odwołania w pozostałych plikach poprawiono.

**Źródła:** Clásico: ESPN summary (boxscore, statystyki drużyn i zawodników; **jedno źródło**). Ekstraklasa: WebSearch (polsatsport.pl, interia.pl, legia.net, ekstraklasa.org, gol24.pl i inne; wyniki spójne w kilku źródłach). Rożnych, kartek i fauli w Ekstraklasie nie rozliczano (brak statystyk meczowych z wiarygodnego źródła); dotyczy to tylko typów oznaczonych w analizie jako "niska, nie rekomendować".

## Wyniki
- **Barcelona 1-2 Real Madryt.** Statystyki: rożne 6-6 (razem 12), żółte 3-3, faule 15-11 (razem 26), strzały 18-10 (28), celne 6-5 (11).
- **Śląsk 2-0 Wieczysta**, **Jagiellonia 1-0 Wisła Płock**, **Legia 1-2 Lech**.

## Bilans (`verify.py`, tylko typy bez kursu; brak rekomendowanej stawki)
| Grupa | Trafione | Oczekiwane |
|---|---|---|
| Clásico: gole i wynik (23 nogi) | 12/23 | 14,3 |
| Clásico: rożne | 10/12 | 6,0 |
| Clásico: kartki | 7/9 | 4,6 |
| Clásico: faule | 5/5 | 2,6 |
| Clásico: strzały i celne | 16/18 | 11,9 |
| Clásico: rynki zawodnika (strzały, celne, faule) | 16/29 | 18,0 |
| Clásico razem | 66/96 | 57,4 (+1,9 odch. std.) |
| Ekstraklasa 25.10 (gole/wynik, 28 nóg) | 18/28 | 18,4 |

Nogi z jednego meczu są silnie skorelowane (rynki Over rożnych, fauli i strzałów trafiają razem, gdy mecz jest intensywny), więc +1,9 odch. std. dla Clásico to jeden wynik, nie niezależne potwierdzenie.

## Analiza pomyłek
- **Clásico, gole i wynik:** Barça 1 (60,1%), 1X (78%), DNB Barça (73,2%) i Barça Over 1,5 gola (74,2%) przegrały. Wynik 1-2 przy 18-10 w strzałach i 62% posiadania to wariancja (Real: 5 celnych na 2 gole). Przed meczem p Realu wynosiło 22% (rynek zbliżony). **Wariancja.**
- **Clásico, mecz bardziej intensywny niż model:** faule 26 (średnia modelu ok. 22, linia 22,5 miała p 52%), rożne 12 (O/U 9,5 miało p 56%), strzały 28 (linia 28,5 miała p 48%). Linie fauli i rożnych mieściły się po niższej stronie, ale pojedynczy mecz niczego nie dowodzi.
- **Rynki zawodnika 16/29 (18,0):** pudła to wysokie linie Over (Mbappé 3,5 strz., Bellingham 1,5, Fermín 1,5; Yamal celne 0,5 przy 5 strzałach i 0 celnych). **Wariancja.** Camavinga wszedł z ławki, więc typ "jeśli zagra od początku" nie dotyczy (unieważniony).
- **Ekstraklasa:** Wieczysta ≥1 gola (79,8%) i BTTS tak w obu meczach z udziałem Śląska i Jagiellonii (60% i 51%) nie padły; wygrali gospodarze (Śląsk 33,5%, Jagiellonia 49%) w obu meczach z kryzysowymi gospodarzami. W analizie Śląska "kryzys dotyczy tylko underdoga" został zastosowany (λ Śląska obniżona), a mimo to wygrali: pojedynczy wynik, **wariancja**. Wzorzec "gospodarz-underdog w kryzysie wygrywa" (Śląsk 25.10) trzeba obserwować.

## Kalibracja skilli
Bez zmian: brak ustalonego błędu procesu, wszystkie pudła blisko oczekiwań lub w granicach wariancji.

## Do obserwacji
- **Kryzys underdoga (football-analyst):** Śląsk (kryzys, p wygranej 33,5%) wygrał 2-0. Zapisać jako jeden przypadek; zmieniać regułę dopiero po ≥ 3 podobnych przypadkach w kolejnych weryfikacjach.
- **Rożne/faule w meczach o wysokiej stawce (Clásico):** wszystkie linie Over trafione. Warunek: sprawdzić na kolejnych 3-5 meczach top-ligi, czy średnie rożnych/fauli w analizie są systematycznie za niskie.
- **Nadal nierozliczone:** Osaka - Pohankova (WTA Tokio, 29.10 05:45 UTC, w chwili sprawdzenia "Scheduled") i Morrow - VIT.A (ESEA bo1, 28.10; brak w PandaScore, Profilerr i esports.ru). Dopóki ich brak, `Analiza_dnia_2026-10-28.md` i `Analiza_dnia_2026-10-28_v2.md` zostają bez prefiksu.

Propozycja commita: "Uzupełnienie weryfikacji 25.10.2026 (El Clásico, Ekstraklasa) i oznaczenie plików".

Hipotetyczny zysk nie dotyczy (brak kursów). To oszacowania, nie gwarancje; mała próba.
