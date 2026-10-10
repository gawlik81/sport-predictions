# Weryfikacja predykcji z 08-09.10.2026 (CS2 EPL S24, ATP Szanghaj R2, WTA Pekin, Bundesliga, Süper Lig, Brasileirão)

Zweryfikowany plik: `Top10_predykcje_2026-10-08.md` (faktycznie 9 typów + kupon 3-nogowy)

Źródła wyników: ESPN scoreboard (ATP Szanghaj, Süper Lig, Brasileirão), OpenLigaDB (Bundesliga), sport1.pl (statystyki Świątek - Mertens), esports.gg / fragster / lufkindailynews (ćwierćfinały EPL S24).

## Wyniki

| # | Typ | p | Kurs | Wynik | Status |
|---|-----|---|------|-------|--------|
| 1 | Vitality wygra serię z PARIVISION | 83% | 1.16 | 2-0 (Inferno 13-2) | ✅ |
| 2 | Świątek wygra z Mertens | 80% | 1.21 | 6-7(0) 3-6 | ❌ |
| 3 | Dortmund wygra z Werderem | 70% | 1.35 | 2-2 (2-0 w 85'), gole Werderu 88' i 90'+2 | ❌ |
| 4 | Tiafoe wygra z Hanfmannem | 70% | 1.33 | 6-4 6-4 | ✅ |
| 5 | Galatasaray wygra z Kasımpaşą | 68% | 1.27 | 3-1 (gole 45', 90', 90'+6; czerwona Torreira 65') | ✅ |
| 6 | MOUZ wygra serię z FURIA | 63% | 1.58 | 2-0 | ✅ |
| 7 | Cobolli wygra z Mannarino | 62% | 1.42 | 1-6 6-4 3-6 | ❌ |
| 8 | Nakashima wygra z Berrettinim | 57% | 1.62 | 7-6 7-5 | ✅ |
| 9 | Palmeiras wygra z Bahią | 55% | 1.59 | 1-0 (26:10 strzałów, Bahia 1 celny) | ✅ |

**Bilans: 6/9.** Oczekiwane trafienia z podanych p: 6,1, średnie p 67,6% vs trafność 66,7%, więc kalibracja w normie.

**Kupon (Vitality + Świątek + MOUZ, kurs 2.22, p 41,8%) ❌** - przegrał przez Świątek. Alternatywa z Dortmundem zamiast MOUZ też ❌ (Świątek i Dortmund).

**Flat stake 1 j. na 9 typów po kursach z tabeli:** wygrane 1.16 + 1.33 + 1.27 + 1.58 + 1.62 + 1.59 = 8,55 przy stawce 9 → -0,45 j. (ROI -5%). Zgodne z ostrzeżeniem w pliku: żaden typ nie miał dodatniego EV.

Mecze z pliku, których nie typowano: Falcons - Spirit (Spirit 2-0, nie typowane), Zverev - Wu (Zverev wygrał 6-4 7-6, odrzucone przez fair ≤ 1.15), Djokovic - Hurkacz (Hurkacz 6-4 6-3, odrzucone: "brak mocnego typu" - sygnał zmęczenia Djokovicia i problemu Hurkacza z przywodzicielem wskazywał kierunek, ale nie podjęto typu).

## Analiza pomyłek

### 1. Świątek - Mertens (80%, ❌)
Statystyki: 34 niewymuszone błędy Świątek vs 11 Mertens, zero break pointów dla Świątek (drugi raz w karierze), punkty po 1. serwisie 63% vs 87% Mertens, tie-break przegrany 0-7. Mertens przyszła po wygranej 6-3 6-3 z Gauff, z bilansem H2H 0-2.
Co było w analizie: ryzyko "słabsza R3 Świątek, Mertens wyrównuje serwisem i returnem" było nazwane, a liczba została zbita z 90% (model) do 80% (Dimers, rynek 82,6%). Czyli moje p było równe rynkowi, a nie ponad nim. Źródłem pudła nie był błąd w procesie, tylko zdarzenie z 20% - przy tak wielu niewymuszonych błędach nie widać też sygnału, który wcześniej dało się wycenić (brak kontuzji, brak przerwy). **Wniosek: wariancja, bez zmiany reguł.**

### 2. Dortmund - Werder (70%, ❌)
Prowadzenie 2-0 w 85' i dwa gole w 88' i 90'+2. Remis (20%) był wymieniony jako ryzyko numer jeden, wygrana Werderu jako drugie. Pierwsza połowa 0-0. Model i rynek (74%) zgodne, korekta w dół o 4 pp była już zrobiona. **Wniosek: wariancja końcówki, bez zmiany reguł.** Dla spójności z regułą "remis ORAZ wygrana underdoga": zrealizował się remis.

### 3. Cobolli - Mannarino (62%, ❌)
Cobolli wygrał drugiego seta po 1-6 w pierwszym i przegrał 3-6 w trzecim. Analiza wprost opisywała jego niestabilność (przegrany pierwszy mecz w 9 z 20 turniejów) i dała p 62% przy rynku 70% (kurs 1.42), czyli ostrożnie. Typ nie miał EV (-12%) i niskiej pewności; w rankingu był na 7. miejscu. **Wniosek: sygnał ryzyka zmienił liczbę (62% vs 70% rynku), zadziałało zgodnie z regułami; porażka mieści się w 38% niepewności.** Sam fakt wpisania typu z EV -12% i niską pewnością do rankingu jest tu jedynym punktem do poprawy (patrz niżej, ale bez nowej reguły).

### Co zadziałało
- **Vitality, MOUZ** (CS2): 2-0 oba, p 83% i 63%. Model mapowy dobrze skalibrowany; przy Vitality p 83% vs rynek 86% - obniżenie o 3 pp, mieści się w regule "nie schodź pod rynek o >5 pp".
- **Galatasaray** (68%, rynek 74%): korekta o rotację przed Ligą Mistrzów nie była potrzebna - Torreira i Leão zagrali (kartki w protokole); wygrali 3-1 mimo czerwonej kartki w 65'. Korekta w dół o 6 pp względem rynku bez twardych danych (media "przewidują rotację") okazała się zbędna, tak samo jak przy Spirit i Vitórii poprzednio. Reguła "nie schodź pod rynek o >5 pp bez konkretnej informacji" obowiązuje już w skillu; tu zadziałała jako przestroga, nie jako nowa lekcja.
- **Tiafoe, Nakashima**: trafione bez niespodzianek. Nakashima 57% (niska pewność) wygrał 7-6 7-5, więc nie świadczy o niczym.
- **Palmeiras** (55%): wygrali 1-0 przy 26:10 strzałów, Bahia miała 1 celny. Moje p było niższe od rynku (59%).

### Wzorzec wspólny
Pudła są mniejsze niż w poprzednim cyklu (3 z 9, a poprzednio 4 z 10) i żadne nie miało powtarzalnej przyczyny z reguł już znanych: brak kwalifikanta, brak Challengera, brak rzekomo "uśrednionego" p. Dwa z trzech (Świątek, Dortmund) to najwyższe p zestawienia obok Vitality, a trafność typów p ≥ 70% wyniosła 2/4 (50%) przy p ~76%. To próba czterech zdarzeń, więc nie wyciągam wniosku o systematycznym przeszacowaniu faworytów; do obserwacji w następnych weryfikacjach.

## Kalibracja skilli

**Brak zmian w `SKILL.md`.** Uzasadnienie: żaden z trzech błędów nie wynika z naruszenia ani z luki w istniejących regułach, a zmiana reguły po jednym zdarzeniu 20-38% byłaby dopasowaniem do szumu (ten sam wniosek jak przy Arnaldim w weryfikacji z 09.10). Konkretnie:
- Świątek: p = rynek, ryzyko nazwane, liczba skorygowana (90% → 80%).
- Dortmund: remis i wygrana underdoga rozważone, p poniżej rynku.
- Cobolli: sygnał niestabilności obniżył p poniżej rynku.

Do obserwacji (bez zmiany reguł do czasu kolejnych weryfikacji): trafność typów p ≥ 70% (teraz 2/4; poprzednio 6/10 w całym zestawie p 55-78%) oraz fakt, że ranking po p konsekwentnie daje ujemne EV (tu -0,5% do -13,6%), co `bet-slip-builder` już każe pokazywać wprost.

To oszacowania, nie gwarancje; próba 9 typów jest mała.
