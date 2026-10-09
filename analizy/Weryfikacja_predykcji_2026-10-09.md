# Weryfikacja predykcji z 07-08.10.2026 (CS2 ESL Pro League S24, ATP Szanghaj R1, Brasileirão)

Zweryfikowany plik: `Top10_predykcje_2026-10-07.md`

Źródła wyników: ATP Tour (Szanghaj 2026 results, wyniki z 9.10 wynikające z drabinki), Tennis.com, Perfect Tennis, NOS, esports.ru / skin.club, VAVEL Brasil, Gazeta Esportiva. Wynik Munar - Brooksby wnioskowany z drabinki (Brooksby zagrał w R2 9.10, więc wygrał R1); wyniku setowego nie potwierdzono.

## Wyniki

| # | Typ | p | Kurs | Wynik | Status |
|---|-----|---|------|-------|--------|
| 1 | Team Spirit wygra (vs M80, bo3) | 78% | 1.11 | Spirit 2-0 | ✅ |
| 2 | Hurkacz wygra (vs Duckworth) | 71% | 1.43 | 6-3 7-6(4), 19 asów | ✅ |
| 3 | Borges wygra (vs Diaz Acosta) | 69% | 1.28 | 7-6(5) 6-2 | ✅ |
| 4 | Bergs wygra (vs Kopriva) | 68% | 1.34 | 6-3 6-1 | ✅ |
| 5 | Norrie wygra (vs Svrcina, Q) | 68% | 1.52 | 3-6 6-3 4-6 | ❌ |
| 6 | Arnaldi wygra (vs Tomic, Q) | 66% | 1.38 | 6-3 6-1 | ✅ |
| 7 | Griekspoor wygra (vs Kotov, Q) | 66% | 1.40 | 4-6 6-7(4) | ❌ |
| 8 | Simakin wygra (vs Ugo Carabelli) | 62% | 1.43 | 6-2 2-6 5-7 | ❌ |
| 9 | Munar wygra (vs Brooksby) | 60% | 1.48 | porażka (Brooksby w R2) | ❌ |
| 10 | Vitória wygra (vs Chapecoense) | 55% | 1.57 | 4-0 | ✅ |

**Bilans: 6/10.** Oczekiwane trafienia z podanych p: 6,6, więc łącznie bez dużego odchylenia. Rozkład błędów jest jednak nierówny: CS2 i piłka 2/2, tenis 4/8.

**Kupony:** Kupon 1 (Hurkacz + Norrie) ❌ - Norrie. Kupon 2 (Griekspoor + Bergs) ❌ - Griekspoor. Obie przegrały przez jedną nogę, a obie przegrane nogi to faworyci z p = 66-68%.

**Flat stake na 10 typów po kursach z tabeli:** wygrane 1.11 + 1.43 + 1.28 + 1.34 + 1.38 + 1.57 = 8,11 przy stawce 10 → ok. -1,9 j. (ROI -19%). Zgodnie z ostrzeżeniem w pliku: przepłacone kursy nie dawały przewagi.

## Analiza pomyłek

### 1. Norrie - Svrcina (68%, ❌)
Svrcina to kwalifikant, więc grał już dwa mecze w Szanghaju (aklimatyzacja, rytm). Norrie wszedł z ranking 40 vs 126 i bilansem 20-17 w sezonie. Moje 68% było ponad rynkiem (62-64%) bez żadnej twardej informacji: "doświadczenie w wolnych warunkach" to opis, nie dane. Dodatni EV (+3%) Norriego i Kuponu 1 (+4,9%) wynikał wyłącznie z tego, że przyjąłem więcej niż rynek. To była pozorna wartość, nie przewaga.

### 2. Griekspoor - Kotov (66%, ❌)
Kotov: kwalifikant (187. ATP), po wygranych kwalifikacjach i H2H 3-2 dla niego. Wszystkie trzy sygnały (rytm meczowy, H2H, kwalifikacje) wskazywały w stronę rywala, a opisałem je, nie obniżając liczby (66% to praktycznie wynik niezależnego modelu 66,6%). To ten sam wzorzec co "opisowa wzmianka bez wpływu na liczbę".

### 3. Simakin - Ugo Carabelli (62%, ❌)
Wybrałem niżej notowanego (154. ATP) na podstawie bilansu 45-17, zdobytego głównie na Challengerach, przeciw rywalowi z ATP z 3-11 na hardzie i serią porażek. Bilans z Challengerów nie przekłada się na poziom ATP/M1000, a "zła forma rywala" nie czyni z kogoś faworyta, gdy ranking i poziom turniejów go nie wspierają. Do tego Simakin był kwalifikantem (też grał już w Szanghaju), więc to nie kwestia rytmu. Typ oparto głównie na jednym źródle (Tennis Tonic) i nie powinien trafić do TOP 10 z p 62%.

### 4. Munar - Brooksby (60%, ❌)
Munar grał półfinał w Tokio 5.10, a w Szanghaju wyszedł w pierwszej rundzie 7-8.10 (dwa, trzy dni po półfinale i po podróży). Zanotowałem to jako "korektę w dół", ale model 55% i Stats Insider 62% dały 60%, czyli średnią zewnętrznych źródeł. Przeciwnik 102. ATP z bilansem 16-23, ale z pełnym odpoczynkiem. Ten sam błąd co wyżej: korekta zmęczenia była wzmianką, nie liczbą. Dodatkowo wybór wyższej wartości z rozstępu (55-62%) tylko dlatego, że potrzebowałem dziesiątego typu.

### 5. Co zadziałało
- **Hurkacz, Bergs, Borges, Arnaldi** trafione, ale z p 66-71% to były typy około "2 na 3"; trafienie 4/4 to częściowo szczęście. Szczególnie Borges: model dawał 57,5%, ja 69% (nad modelem o 11 pp) i wygrał 7-6 6-2, ale dla jakości procesu to nie dowód.
- **Arnaldi** (0-3 na hardzie w 2026, kontuzja stopy) - obniżenie z 77% do 66% okazało się zbędne, wygrał 6-3 6-1. Pojedynczy przypadek, nie wymaga zmiany reguł, ale pokazuje, że korekty "za dużo sygnałów ryzyka" bez wspólnej logiki są losowe.
- **Vitória** (55%) - 4-0, trafione; moje p było niższe od rynku (60,6%), czyli byłem zbyt ostrożny.
- **Spirit** (78% vs rynek 85%) - wygrali 2-0 (Dust2 i Cache), bez problemów. Obniżenie o 7 pp względem rynku za "dwie świeże porażki" nie miało twardych podstaw (brak stand-ina, kontuzji). Wniosek: przy braku konkretnej informacji nie schodzić daleko pod rynek.

### 6. Wzorzec wspólny
- Wszystkie 4 pudła to tenis R1 z p 60-68%, gdzie nie było twardych statystyk serwisu/returnu (p_serve z rankingu) i wartość brałem ze średniej: model / niezależne modele / rynek. Przy rozstępie 10-20 pp to uśrednianie dawało liczby, których nie broni żadne źródło.
- 3 z 4 pudeł (Norrie, Griekspoor, Simakin) to mecze z kwalifikantem po drugiej stronie albo samym kwalifikantem.
- Wymuszone 10 typów: pozycje 6-10 miały p 55-66% i 3 z 5 przegrały. Lista TOP 10 powinna być krótsza, jeśli nie ma 10 typów z p ≥ 70% i twardymi danymi.

## Kalibracja skilli (wprowadzone zmiany)

- **tennis-analyst, Krok 3:** nowe reguły: kwalifikant po drugiej stronie, bilans z Challengerów, krótki odpoczynek po półfinale/finale, uśrednianie źródeł, "wartość = różnica wobec rynku".
- **bet-slip-builder:** EV dodatnie wynikające tylko z p wyższego od rynku o >5 pp bez twardej informacji traktuj jako podejrzane, nie jako value; nie dobijaj listy TOP-N na siłę do 10; limit p dla nóg kuponu w tenisie R1.
- **esports-analyst / football-analyst:** reguła symetryczna: nie schodź pod rynek o >5 pp bez konkretnej informacji (stand-in, kontuzja). Spirit i Vitória były niedoszacowane przez ostrożność, nie przez dane.

To oszacowania, nie gwarancje; próba 10 typów jest mała.
