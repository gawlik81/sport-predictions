# Weryfikacja analiz i kuponów z 11-12.10.2026

Zweryfikowane pliki: `ZWERYFIKOWANE_Freiburg_Schalke_2026-10-11.md`, `ZWERYFIKOWANE_Liverpool_ManCity_2026-10-11.md`, `ZWERYFIKOWANE_Pogon_Korona_2026-10-11.md`, `ZWERYFIKOWANE_Kupon_wieczor_2026-10-11.md`, `ZWERYFIKOWANE_Kupon_wieczor_2026-10-12.md` (po weryfikacji oznaczone prefiksem `ZWERYFIKOWANE_`).

Źródła wyników: ESPN (scoreboard i podsumowania meczów: gole, rożne, kartki), ekstraklasa.org, gol24.pl i Dziennik Zachodni (GKS - Wieczysta), Sports Mole i Empire of the Kop (nieobecność Szoboszlaia). Nie znalazłem liczby rożnych w Pogoń - Korona, więc dwa kupony z rożnymi z tego meczu pozostają niezweryfikowane. Wartości EV i stawki z plików to wartości hipotetyczne (plików nie traktuję jako postawionych zakładów).

## Wyniki meczów

| Mecz | Wynik | Rożne | Inne |
|---|---|---|---|
| Freiburg - Schalke | 2-1 | 7:2 (9) | |
| Liverpool - Man City | 0-3 | 5:6 (11) | żółte kartki 2+2; Szoboszlai poza kadrą meczową (uraz ścięgna) |
| Pogoń - Korona | 2-0 | brak danych | |
| Cagliari - Juventus | 1-1 | | |
| Legia - Wisła Kraków | 2-0 | | |
| Racing Santander - Valencia | 2-2 | 8:3 (11) | |
| Torino - Udinese | 2-1 | 4:3 (7) | |
| GKS Katowice - Wieczysta (zaległy mecz) | 2-1 | | |
| Atalanta - Venezia | 3-1 | | |
| Radomiak - Motor | 2-3 | | |
| Coventry - Newcastle | 4-1 | | |
| Levante - Sevilla | 3-3 | | |

## Freiburg - Schalke (11.10)

Analiza: model Freiburg 57,3% (rynek ok. 58%), wniosek "żaden kupon nie ma dodatniego EV, nie rekomenduję gry". Mecz zakończył się zgodnie z modelem (2-1, 3 gole, 9 rożnych).
- Wszystkie 9 wycenionych kuponów trafiłoby: 1X + rożne O8.5 (kurs 1.79) ✅, 1X + O2.5 ✅, 1X + O1.5 ✅, 1X + O1.5 + rożne O7.5 ✅, Under 3.5 + rożne O8.5 (2.25) ✅, Under 3.5 + O7.5 ✅, 12 + Under 3.5 ✅, Freiburg wygra + O7.5 ✅, Freiburg wygra + Under 3.5 ✅.
- Fakt, że wszystkie by weszły, nie zmienia oceny ex ante: z EV od -2% do -28% i p 37-51% były to zakłady bez przewagi nad rynkiem; zgodnie z wnioskiem nie rekomendowano gry. Rożne w modelu: średnia 10,0 (bez danych sezonowych), faktycznie 9 - trafiło O8.5 i O7.5.
- Bez korekt.

## Liverpool - Man City (11.10)

Wynik: 0-3; model City 43% (✅), Liverpool 31,6%, remis 25,3% - bez typu, EV ujemne.
- Rynki dodatkowe, hipotetycznie: X2 ✅, Over 2.5 ✅ (3 gole), Under 3.5 ✅, BTTS tak ❌, rożne O9.5 ✅ (11), City O4.5 rożnych ✅ (6), kartki O3.5 ✅ (4 żółte, mierzone żółtymi).
- **Kupon (wariant główny): Szoboszlai Over 1.5 strzałów (kurs 1.63) - nie do rozstrzygnięcia: Szoboszlai nie był w kadrze meczowej** (napięte ścięgno podkolanowe po zgrupowaniu kadry; według relacji Sports Mole trener powiedział, że zawodnik nie jest w pełni gotowy). Analiza oznaczała typ jako "do potwierdzenia po składach" i niską pewność, ale (a) wymieniła jako absencje Isaka, Gakpo, Ekitike, Bradleya i Leoniego, nie Szoboszlaia, (b) średnia strzałów (2,4) nie miała źródła, (c) typ z "EV +10,4%" był wariantem głównym kuponu. Alternatywa (rożne O9.5, 1.71, EV -9% do +1,6%) ✅.
- **Przyczyna:** dla zawodnika, od którego zależał główny typ kuponu, nie zrobiono osobnego sprawdzenia kontuzji/kadry (jak w `tennis-analyst`: osobne zapytanie "[nazwisko] injury" dla każdego zawodnika); ogólna lista absencji nie wystarczyła. Typ z niepotwierdzonym p, wyższym od rynku (+10% EV), był jednocześnie wariantem głównym, wbrew regule `bet-slip-builder` ("EV z p wyższego od rynku o >5 pp bez twardych danych to podejrzenie błędu").

## Pogoń - Korona (11.10)

Wynik 2-0 (Pogoń 46,3% w modelu, rynek 41,6%; bez typu na wynik).
- Kupony: 1X + Under 3.5 (1.65) ✅, 12 + Under 3.5 (1.56) ✅, X2 + Under 3.5 ❌, Korona +0.25 / +0.5 / +0.75 ❌ (Pogoń wygrała), 1X + rożne O7.5 i Under 3.5 + rożne O7.5 niezweryfikowane (brak rożnych).
- Wniosek analizy ("nie rekomenduję gry, 1X + Under 3.5 po 1.65 spełnia warunki, EV -10%") zgodny z wynikiem; to był zakład z ujemnym EV, który wszedł. Bez korekt.

## Wieczór 11.10 (Cagliari - Juve, Legia - Wisła, Racing - Valencia)

| Typ | p | Wynik |
|---|---|---|
| Cagliari - Juve Under 3.5 (1.29) | 80% | ✅ (1-1) |
| Racing - Valencia Under 3.5 (1.44) | ok. 66% | ❌ (2-2, 4 gole) |
| Legia - Wisła Under 3.5 (1.40) | ok. 67% | ✅ (2-0) |
| Legia 1X (1.28) | ok. 72% | ✅ |
| Juve wygra (1.52) | 52-57% | ❌ (remis) |

- **Kupon główny (Cagliari U3.5 + Racing U3.5, 1.86, p 53%) ❌** przez Racing. Alternatywa (Cagliari U3.5 + Legia 1X, 1.65) ✅.
- Racing - Valencia: plik zawierał dane, że Racing był w 4 z 6 ostatnich meczów w grze 4+ goli (19 straconych w 6), a typ Under 3.5 miał p 66% przy rynku zbliżonym (EV -3%). Dane o 4+ golach były opisane, ale noga trafiła w kupon jako "najmniej szkodliwe dopełnienie", mimo że sygnał przemawiał za Over. To ten sam błąd co wcześniej: opis ryzyka bez efektu na decyzję. Nie zmienia to faktu, że 4+ goli w meczu z p 34% to zdarzenie niewyjątkowe.

## Wieczór 12.10 (kupon domyślny: kurs nogi > 1.2, kupon > 1.6, EV > 0, p > 50%)

| Typ | p | Kurs | Wynik |
|---|---|---|---|
| **Udinese - Torino Under 2.5 (typ końcowy, stawka 2,1% bankrolla)** | 62,3% | 1.65 | ❌ (2-1, 3 gole) |
| Torino wygra | 43,4% | 2.40 | ✅ |
| GKS - Wieczysta Under 2.5 | 42,3% | 2.44 | ❌ (2-1) |
| GKS - Wieczysta BTTS tak | 62,8% | 1.43 | ✅ |
| Coventry - Newcastle Under 3.5 | 64,5% (rynek) | 1.46 | ❌ (4-1) |
| Levante - Sevilla Under 2.5 | 54,1% (rynek) | 1.74 | ❌ (3-3) |
| Atalanta - Venezia Under 3.5 (odrzucony) | 76-85% (model) vs 58% (rynek) | | ❌ (3-1, 4 gole): odrzucenie słuszne |
| Radomiak - Motor Under 2.5 (odrzucony) | 58% (model) vs 42% (rynek) | | ❌ (2-3, 5 goli): odrzucenie słuszne |

Kupony: wariant główny (Torino 2.40 + GKS U2.5 2.44 = 5.86) ❌, wariant bezpieczniejszy (Udinese - Torino U2.5 + GKS U2.5, 4.07) ❌, wariant bezpieczny (Udinese - Torino U2.5 + GKS BTTS, 2.38) ❌. **Jedyny typ rekomendowany jako samodzielny (Udinese - Torino Under 2.5, 1.65, EV +2,8%) przegrał** (hipotetycznie -2,1% bankrolla).

### Przyczyna: Udinese - Torino Under 2.5
Przewaga +2,8% EV wzięła się z podwyższenia Under 2.5 o 5,4 pp nad rynek (62,3% vs 56,9%) przez obniżenie λ Udinese z 1,0 do 0,9 za trzech nieobecnych (Zaniolo, Gueye, Piotrowski). W tym samym pliku były dane przemawiające w drugą stronę: Udinese traciło średnio 2 gole na mecz (10 straconych w 5) i Torino 7 straconych w 5 meczach. Nieobecni dotyczą ataku Udinese; słabą obronę (która napędza Over) analiza zignorowała. Efekt kadrowy został więc uwzględniony po jednej stronie, a jego wielkość (-10% λ = +5,4 pp na totalu) była hojna jak na brak pojedynczego pomocnika/skrzydłowego i dwóch rezerwowych. Wynik 2-1 nie dowodzi błędu (zdarzenie z 38%), ale struktura typu (EV z jednej korekty kadrowej przy sprzecznych danych) jest tym, co `bet-slip-builder` nazywa "pozorną wartością".

### Co zadziałało
- **Odrzucenie Atalanta - Venezia Under 3.5 i Radomiak - Motor Under 2.5**, gdy model rozjechał się z rynkiem o >10 pp: w obu meczach rynek miał rację (4 i 5 goli). Zgodne z regułą "przewaga >5 pp bez twardej informacji to własny błąd, nie value".
- Rynek wyniku: Torino 43% (✅), Freiburg 57% (✅), City 43% (✅).

## Kalibracja skilli

1. **`football-analyst` - rynki zawodnika:** dopisane: dla zawodnika, od którego zależy typ (zwłaszcza wariant główny kuponu), wykonaj osobne sprawdzenie "[zawodnik] injury/in squad" (konferencja trenera dzień przed meczem); typ warunkowy ("jeśli zagra") i oparty na niepotwierdzonej średniej nie może być wariantem głównym. Uzasadnienie: Szoboszlai (poza kadrą, główny typ kuponu Liverpool - City).
2. **`football-analyst` - korekta kadrowa na totalach:** dopisane: absencja dotyczy tylko jednej strony boiska (atak lub obrona), więc nie wyciągaj z niej przewagi nad rynkiem na totalu, gdy forma obu drużyn (stracone gole) przemawia w przeciwną stronę, i nie podwyższaj p o >~3 pp z samej nieobecności jednego-trzech graczy bez rotacji kluczowych. Uzasadnienie: Udinese - Torino Under 2.5 (+5,4 pp przy sprzecznych danych). **Próg 3 pp to moje oszacowanie, nie wynik pomiaru;** jedno zdarzenie nie dowodzi błędu, więc to doprecyzowanie, nie nowa reguła ilościowa.
3. **`bet-slip-builder` - bez zmian** (ma niezacommitowane zmiany użytkownika; reguła o EV z p ponad rynek >5 pp obejmuje oba przypadki).

Pozostałe wnioski (Freiburg - Schalke, Pogoń - Korona, wieczór 11.10): bez zmian w skillach.

To oszacowania, nie gwarancje; próba jednego weekendu jest mała.
