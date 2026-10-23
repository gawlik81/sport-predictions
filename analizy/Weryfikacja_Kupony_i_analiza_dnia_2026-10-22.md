# Weryfikacja kuponów i analizy dnia 22.10.2026 (LE, LK, NHL/NBA, tenis) + uzupełnienie 18.10 (CS2)

**Zweryfikowane pliki:**
- `ZWERYFIKOWANE_Kupony_10_2026-10-22.md` (dawniej `Kupony_10_2026-10-22.md`): 7 kuponów (poziom 2, stawka 0%) + podgląd 3 kuponów poziomu 3-4 (hipotetycznie).
- `ZWERYFIKOWANE_Analiza_dnia_2026-10-22.md` (dawniej `Analiza_dnia_2026-10-22.md`): typy spoza kuponów rozliczone hipotetycznie.
- `ZWERYFIKOWANE_Kupony_10_2026-10-18.md` (dawniej `Kupony_10_2026-10-18.md`): domknięta ostatnia otwarta noga, CS2 FURIA - BetBoom Over 69,5 rund.

**Źródła wyników:** ESPN scoreboard (LE, LK, NBA, NHL, ATP Lyon). Wszystko z jednego źródła (ESPN); gospodarze wg pola `homeAway`. CS2: WebSearch (winio.ai, noping.com, rdy.gg) - zgodne co do serii 3-2 dla FURII; wynik Nuke podany sprzecznie (13-9 vs 9-13 dla BetBoom), co nie wpływa na rozliczenie. NHL Seattle - Utah w momencie weryfikacji trwał (3-3 w 3. tercji), ale nie występuje w żadnym typie (brak na Betclic).

## Wyniki
- **LE:** Bournemouth 3-0 Milan; Beşiktaş 2-2 Palace; Celtic 1-2 Celta; Jagiellonia 0-3 Anderlecht; Lillestrøm 0-6 Sociedad; Celje 2-2 Salzburg; Olympiakos 1-0 Sparta; Omonia 1-4 Benfica; Hoffenheim 3-0 Lyon; Pilzno 1-2 Levski.
- **LK:** AGF 1-1 Egnatia; Ajax 2-0 Atalanta; Monaco 3-0 Freiburg; Borac 2-0 KuPS; Braga 2-0 Gent; Midtjylland 0-1 St. Truiden; Thun 0-1 Hajduk; Lincoln 1-4 Twente.
- **NBA:** PHI 114-106 CLE; OKC 96-84 DEN.
- **NHL:** CGY 2-1 MIN; NJD 4-1 ANA; DAL 3-2 WPG (po dogrywce); oraz inne mecze nie występujące w typach.
- **Tenis:** Lyon 1/8: Nakashima d. Jacquet 6-4 6-3.
- **CS2 (18.10):** finał Thunderpick FURIA 3-2 BetBoom (Dust2 13-6, Ancient 16-19 po dogrywce, Nuke 9-13, Mirage 13-11, Cache 13-6); razem ok. 119 rund.

## Kupony (stawka 0%, poziom 2)
| # | Nogi | Kurs | p | EV | Wynik |
|---|---|---|---|---|---|
| 1 | Olympiakos-Sparta O1,5 ❌ (1-0) + Benfica ✅ (4-1) | 1,54 | 57,0% | -12,4% | ❌ |
| 2 | Jagiellonia-Anderlecht O1,5 ✅ (0-3) + Celtic-Celta 12 ✅ (1-2) | 1,52 | 57,0% | -13,1% | ✅ |
| 3 | Pilzno-Levski 12 ✅ (1-2) + Beşiktaş-Palace 12 ❌ (2-2) | 1,52 | 56,2% | -14,2% | ❌ |
| 4 | Hoffenheim-Lyon 12 ✅ (3-0) + Monaco-Freiburg 12 ✅ (3-0) | 1,52 | 56,2% | -14,2% | ✅ |
| 5 | Ajax-Atalanta 12 ✅ (2-0) + Braga-Gent 12 ✅ (2-0) | 1,54 | 56,2% | -13,5% | ✅ |
| 6 | Borac-KuPS 12 ✅ (2-0) + Thun-Hajduk 12 ✅ (0-1) | 1,54 | 55,0% | -15,5% | ✅ |
| 7 | Sociedad ✅ (0-6) + Midtjylland-St. Truiden 12 ✅ (0-1) | 1,66 | 52,1% | -13,7% | ✅ |

**Kupony 1-7: 5/7 przy oczekiwanych 3,90.** Nogi kuponów: 12/14 przy 10,48. Hipotetyczny zysk przy stawce 1 na kupon: +0,78 (informacyjnie; zalecana stawka 0%, EV wszystkich kuponów ujemne, więc to nie dowód przewagi). TOP 3 nie było oznaczone.

**Podgląd poziomów 3-4 (nie zastosowany, hipotetycznie):** Salzburg + Bournemouth-Milan 12 ❌ (2-2); Wild ML + AGF O1,5 ❌ (Wild 1-2 CGY; AGF 1-1 = O1,5 ✅); Stars ML + Twente ✅ (DAL po dogrywce, ML z dogrywką). 1/3 przy oczekiwanych 1,47.

## Typy spoza kuponów (hipotetycznie)
- "Przewaga niepotwierdzona" (EV > 0 tylko z p wyższego od rynku o > 5 pp): Lincoln BTTS nie 61% ❌ (1-4); Borac U2,5 53% ✅; Monaco U2,5 51% ❌ (3-0); Ajax U3,5 69% ✅; Thun U2,5 53% ✅; Braga wygra 54% ✅ → **4/6 przy 3,41**. Wykluczenie ich z kuponów było neutralne (wynik zgodny z p, nie z rynkiem, ale próba bez znaczenia).
- NHL/NBA ML (nogi nocne, poza kuponami): MIN 65% ❌, NJD 63% ✅, DAL 62% ✅ (dogrywka), OKC 71% ✅ → 3/4 przy 2,61.
- Tenis: Nakashima 62% ✅ (6-4 6-3), kurs 1,54 bez przewagi, słusznie poza kuponem.

## Nogi (skrypt verify.py)
**Wszystkie 29 nóg: 23/29 przy oczekiwanych 20,03 (+1,21 odch. std.), Brier 0,166.**
- Piłka 12/1X2 w kuponach: 11/12 (8,91); piłka Over: 2/3 (2,30); BTTS/Under: 3/5 (2,87); NHL/NBA ML: 3/4 (2,61).
- Pasma p: 70-80%: 13/16 (11,99); 60-70%: 5/8 (5,13); 50-60%: 3/4 (2,11).

## Analiza pomyłek
- **Olympiakos-Sparta O1,5 (77%, kupon 1):** 1-0. Dokument wprost wskazał "ryzyko: rotacja (liga za 2 dni), 1-0", a p wynikało z samego Poissona (λ 2,0/0,8; P(≤ 1 gol) ok. 23%), bez korekty. Przy takim p to ok. 1 na 4, czyli wynik w granicach wariancji, ale jest to **pierwszy przypadek** wzorca "sygnał rotacji opisany, liczba bez zmian" w tej kolejce dla Over. Nie wystarcza na zmianę reguły (jeden przypadek; Salzburg-Celje 2-2 i AGF 1-1 nie potwierdzają rotacyjnej niskiej liczby bramek).
- **Beşiktaş-Palace 12 (74%, kupon 3):** 2-2. Remis przy p(X) 26% i niepewnym 1X2 (analiza: "niska 1X2"). **Wariancja**; noga o niskiej pewności była w zwykłym zestawie, ale po wcześniejszej regule dotyczącej pewności nie jest to nowość (analiza oznaczała ją jako gole średnia, 1X2 niska).
- **Salzburg (63,5%, podgląd) 2-2 i AGF 1-1:** remisy faworytów; **wariancja**. Trzy remisy faworytów lub wyrównanych (Beşiktaş, Celje, AGF) w 18 meczach to 3/18 przy oczekiwanych ok. 4,3, więc remisów było mniej niż modelowo.
- **Lincoln BTTS nie (61%), Monaco U2,5 (51%):** typy bez przewagi nad rynkiem, trafiły się po jednej stronie. **Wariancja**; ich wykluczenie z kuponów było słuszne (p wyższe od rynku o > 5 pp bez twardej informacji).
- **Wild ML (65%):** CGY 2-1; bramkarz MIN był niepotwierdzony (jak w dokumencie), poza kuponem. **Wariancja.**

## Co zadziałało
- Kupony 2, 4, 5, 6, 7 trafiły; podwójna szansa bez remisu 11/12 (oczekiwane 8,9).
- Dokument uczciwie pisał, że żaden kupon nie ma EV > 0 i stawka wynosi 0%; poziom 2 użyty zgodnie z regułami, wyższe poziomy (3-6) nie zastosowane bez zgody.
- Wykluczenia: tenis p = rynek (Nakashima) i nogi "przewaga niepotwierdzona" nie zasiliły kuponów; wynik tych nóg (4/6) jest zgodny z oczekiwaniami, więc nie ma sygnału, że reguła była zbyt ostrożna.

## Kalibracja skilli
**Bez zmian.** Bilans nóg (23/29 vs 20,03, +1,2 odch. std.) mieści się w wariancji; dwa pudła kuponów (Olympiakos O1,5, Beşiktaş 12) to wyniki o p ok. 23-26%. Brak powtarzalnego błędu procesu poza jednym przypadkiem rotacji, zapisanym poniżej do obserwacji. Domknięcie nogi CS2 nie zmienia reguł.

## Do obserwacji
- **Rotacja opisana, p bez korekty w Over/gole faworyta:** 22.10 Olympiakos O1,5 (1-0), licznik 1 przypadek; dotychczas nie zebrano potwierdzenia z wcześniejszych weryfikacji. Warunek zmiany: ≥ 2 takie pudła z różnych meczów w kolejnych weryfikacjach -> w `football-analyst` (krok "Skalibruj", puchary z rotacją) dopisać liczbę dla Over/total przy opisanej rotacji.
- **Gole w pucharach:** LE/LK 22.10 średnio 2,7 gola na mecz (18 meczów); Over 1,5 w kuponach 1/2 (+ AGF ✅). Nie potwierdza wcześniejszej tendencji LM do wysokich wyników (LM 20-21.10: 12/16 O2,5 przy 10,27).
- **Remisy faworytów w LE/LK:** 3 z 18 meczów (Beşiktaş, Celje, AGF) przy oczekiwanych ok. 4,3; w granicach wariancji.
- **Piłka 12/1X2:** 11/12 (+1,4 odch. std.) w tej kolejce; razem z wcześniejszymi (LM 21.10: 5/6) 16/18. Nadmiar trafień, nie błąd; nie ścinać p ani nie podnosić na tej podstawie.
- **Nogi "przewaga niepotwierdzona":** hipotetycznie 4/6 przy 3,41; razem z poprzednimi (Ottawa +1,5 ✅) 6/10 -> 10/16 przy oczekiwanych ok. 10,3.
- **Jakość danych:** wszystko z ESPN (jedno źródło); CS2 z trzech zgodnych źródeł (Nuke rozbieżne, bez wpływu na wynik). Seattle - Utah (NHL) nie rozliczany, nie ma w typach.

Hipotetyczny zysk tylko informacyjny. To oszacowania, nie gwarancje; próba jest mała.
