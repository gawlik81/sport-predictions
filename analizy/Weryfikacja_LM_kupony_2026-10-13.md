# Weryfikacja: Liga Mistrzów, 2. kolejka - analiza i 4 kupony z 13.10.2026

Zweryfikowany plik: `ZWERYFIKOWANE_Analiza_LM_kupony_2026-10-13.md` (po weryfikacji oznaczony prefiksem `ZWERYFIKOWANE_`).

Źródło wyników: ESPN (scoreboard `uefa.champions`, status "Full Time"). Rożnych i kartek nie sprawdzałem, bo analiza nie miała typów na te rynki. Lens - Sporting (0-2) i Sabah - Slavia (2-0) były poza analizą (już trwały w chwili jej pisania), więc nie ma tu typów do oceny.

## Wyniki 7 analizowanych meczów

| Mecz | Wynik | Gole |
|---|---|---|
| Galatasaray - Barcelona | 1-4 | 5 |
| Inter - Club Brugge | 3-4 | 7 |
| Villarreal - Napoli | 3-1 | 4 |
| Atlético - Man United | 2-0 | 2 |
| Arsenal - Lille | 3-0 | 3 |
| RB Leipzig - PSV | 1-0 | 1 |
| Viking - Bayern | 3-3 | 6 |

## Wyceny nóg (p = Pinnacle no-vig po składach)

| Typ | p | Kurs | Wynik |
|---|---|---|---|
| Atlético wygra | 53,0% | 1.87 | ✅ |
| Arsenal wygra | 78,8% | 1.24 | ✅ |
| Villarreal - Napoli Under 3.5 | 66,2% | 1.47 | ❌ (4 gole) |
| Leipzig wygra | 62,7% | 1.55 | ✅ |
| Atlético - United Under 3.5 | 63,7% | 1.50 | ✅ |
| Leipzig - PSV Over 3.5 | 58,7% | 1.63 | ❌ (1 gol) |
| Barcelona wygra | 74,4% | 1.28 | ✅ |
| Arsenal - Lille Under 3.5 | 61,2% | 1.55 | ✅ |
| Inter wygra | 76,3% | 1.24 | ❌ (3-4) |
| Galatasaray - Barcelona Over 3.5 | 63,1% | 1.50 | ✅ (5 goli) |
| Viking - Bayern Under 4.5 | 52,6% | 1.87 | ❌ (6 goli) |

Pominięte w analizie (poza kuponami, hipotetycznie): Villarreal wygra (p 44,6%) ✅, Bayern wygra (@1.13) ❌ (remis 3-3), Bayern - Viking Over 2.5 (@1.15) ✅.

## Kupony (wszystkie z wnioskiem "EV < 0, stawka 0%")

| Kupon | Nogi | Kurs | p | Wynik |
|---|---|---|---|---|
| 1 | Atlético wygra + Arsenal wygra | 2.32 | 41,8% | ✅ |
| 2 | Viking - Bayern Under 4.5 + Barcelona wygra | 2.39 | 39,1% | ❌ (Under 4.5) |
| 3 | Leipzig wygra + Inter wygra | 1.92 | 47,8% | ❌ (Inter) |
| 4 | Villarreal - Napoli Under 3.5 + Leipzig - PSV Over 3.5 | 2.40 | 38,9% | ❌ (obie) |

Bilans kuponów: 1 z 4 (oczekiwane p: 41,8 + 39,1 + 47,8 + 38,9 = 1,68 kuponu). Hipotetycznie przy stałej stawce 1: +1,32 - 3 = -1,68, ale analiza zalecała stawkę 0%, więc w praktyce nic nie postawiono.

## Bilans vs oczekiwane

- Wygrane faworytów (Pinnacle): Atlético, Arsenal, Barcelona, Leipzig, Inter, Bayern; oczekiwane suma p = 4,68, faktycznie 4 z 6 (Inter przegrał, Bayern zremisował). Różnica -0,7 trafienia mieści się w wariancji.
- Rynki goli: 6 nóg z 5 trafionymi i 4 nietrafionymi z oczekiwanym p 52-66%: Under 3.5 Atlético ✅, Arsenal ✅, Villarreal ❌; Over 3.5 Gala-Barca ✅, Leipzig-PSV ❌; Under 4.5 Viking-Bayern ❌. Razem 3 z 6 przy oczekiwanych ok. 3,8. Trafność poniżej oczekiwań, ale to 6 nóg, więc wariancja.
- Mecze o dużej liczbie goli (Inter - Brugge 7, Viking - Bayern 6, Galatasaray - Barcelona 5) pokrywają się z tym, że kupony 2 i 3 przegrały na "bezpiecznych" nogach. Żaden z tych typów nie wyróżniał się jako przeszacowany względem rynku: p pochodziło wprost z Pinnacle, więc błąd dotyczy rynku, nie modelu.

## Co zadziałało

- **Brak rekomendacji gry (stawka 0%)** przy braku EV względem Pinnacle: analiza uczciwie napisała, że nie ma nogi z EV > 0, i nie wymuszała value. Gdyby postawiono kupony, 3 z 4 przegrałyby, więc wniosek był słuszny, choć sam wynik niczego nie dowodzi (jedna kolejka).
- Przyjęcie Pinnacle po składach jako p, bez własnych korekt: zgodne z regułą "przewaga nad rynkiem >5 pp bez twardych danych to podejrzenie błędu". Żadnej korekty modelowej nie trzeba było tu bronić.

## Błędy procesu

Nie znalazłem błędu procesu, który uzasadniałby zmianę skilli:
- Inter - Brugge (3-4) i Viking - Bayern (3-3) to wyniki przeciwne rynkowi (Inter 76%, Bayern 82,6% z Pinnacle), ale bez konkretnej informacji, której analiza by nie uwzględniła. Absencje (Urbig zamiast Neuera, Bayern bez wyróżniających się braków) były znane i wycenione w cenie Pinnacle.
- Wymóg użytkownika "kupon w przedziale kursów 1.6-2.5" wymusił kupony 3 i 4 z nogami o ujemnym EV; analiza to jawnie opisała i dała stawkę 0%. Zgodne z `bet-slip-builder` (nie fabrykuj typu).

## Kalibracja skilli

Bez zmian w skillach: jedna kolejka (7 meczów, 11 nóg) to za mało na wniosek, a odchylenia mieszczą się w wariancji. Do obserwacji (zgodnie z handoffem): grupa "wygrana/1X, p 58-85%" jest dziś poniżej oczekiwań (4 z 6 przy 4,68), co nie wspiera zmiany reguły o korygowaniu p faworytów w dół; licznik dwóch weekendów z handoffu dotyczył ligi krajowej, więc tej kolejki LM nie doliczam.

To oszacowania, nie gwarancje; próba jednej kolejki jest mała.
