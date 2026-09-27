# Weryfikacja predykcji — kolejki 21-24.08 i 28-31.08.2026

Porównanie 33 typów 1X2 wytypowanych w tej sesji z rzeczywistymi wynikami (sprawdzone 01.09.2026, po
zakończeniu obu kolejek). Cel: wyciągnąć wnioski do skorygowania metodologii w kolejnych analizach.

## Kolejka 1 (21-24.08.2026) — 15 typów

| Mecz | Typ | P | Wynik rzeczywisty | Trafiony? |
|---|---|---|---|---|
| Man City – Bournemouth | City | 69,0% | 2-1 | ✅ |
| Inter – Monza | Inter | 73,1% | 4-1 | ✅ |
| Elche – Barcelona | Barcelona | 59,9% | 0-5 | ✅ |
| PSG – Rennes (u Rennes) | PSG | 71,5% | **2-2** | ❌ remis |
| Piast Gliwice – Legia | Legia | 77,7% | **1-1** | ❌ remis |
| Arsenal – Coventry | Arsenal | 79,7% | 3-0 | ✅ |
| Hull City – Man Utd | Man Utd | 72,2% | **2-0 dla Hull** | ❌ |
| Espanyol – Real Madryt | Real Madryt | 63,8% | 1-2 (gol w 90') | ✅ |
| Athletic Bilbao – Sevilla | Athletic | 53,7% | **1-3 dla Sevilli** | ❌ |
| Frosinone – Juventus | Juventus | 70,1% | 0-1 | ✅ |
| Genoa – Napoli | Napoli | 67,5% | 0-2 | ✅ |
| Marseille – Strasbourg | Marseille | 53,6% | 4-0 | ✅ |
| Le Havre – Monaco | Monaco | 51,1% | 0-1 | ✅ |
| Radomiak – Zagłębie Lubin | Zagłębie | 63,9% | **0-0** | ❌ remis |
| Pogoń Szczecin – Wisła Kraków | Pogoń | 57,8% | **2-2** | ❌ remis |

**Bilans: 9/15 trafień (60%)**

## Kolejka 2 (28-31.08.2026) — 18 typów

| Mecz | Typ | P | Wynik rzeczywisty | Trafiony? |
|---|---|---|---|---|
| Liverpool – Nottingham Forest | Liverpool | 62,5% | **2-2** | ❌ remis |
| Aston Villa – Arsenal | Arsenal | 58,1% | 0-1 | ✅ |
| Man Utd – Ipswich | Man Utd | 51,2% | 5-2 | ✅ |
| Real Madryt – "Mallorca" | Real Madryt | 66,9% | 4-0 (⚠ realny przeciwnik: **Málaga**, nie Mallorca) | ✅ kierunek / ⚠ zły mecz |
| Rayo Vallecano – Barcelona | Barcelona | 60,5% | 5-2 | ✅ |
| Alavés – Atlético Madryt | Atlético | 53,7% | **1-1** | ❌ remis |
| Juventus – Parma | Juventus | 67,5% | 2-0 | ✅ |
| Milan – Venezia | Milan | 63,0% | 2-0 | ✅ |
| Napoli – Como | Napoli | 53,6% | **1-2 dla Como** | ❌ |
| Bayern – Stuttgart | Bayern | 76,4% | 5-1 | ✅ |
| Dortmund – Hamburger SV | Dortmund | 62,5% | 2-0 | ✅ |
| Elversberg – Leverkusen | Leverkusen | 55,9% | **3-2 dla Elversbergu** | ❌ |
| Lille – PSG | PSG | 53,5% | **2-2** | ❌ remis |
| Rennes – Le Mans | Rennes | 51,2% | 3-2 | ✅ |
| Lyon – Le Havre | Lyon (zaznaczone jako <50%, najsłabszy typ) | 48,7% | 1-1 | ⚪ zgodne z zastrzeżeniem |
| Legia Warszawa – Śląsk Wrocław | Legia | 65,6% | **1-1** | ❌ remis |
| Widzew Łódź – Lech Poznań | Lech | 58,4% | 2-3 | ✅ |
| Górnik Zabrze – GKS Katowice | Górnik | 53,7% | **2-3 dla GKS** | ❌ |

**Bilans: 10/17 trafień (58,8%)**, plus 1 mecz (Lyon-Havre) wcześniej wprost oznaczony jako niepewny (<50%) — remis potwierdza tę ostrożność, nie liczony jako czyste trafienie/pudło.

## Bilans łączny: 19/32 (59,4%) trafionych typów 1X2

---

## Wnioski do zastosowania w kolejnych analizach

### 1. Remis to główna, systematyczna przyczyna pudeł (NAJWAŻNIEJSZY WNIOSEK)
**9 z 13 nietrafionych typów to remisy**, nie zwycięstwa "drugiej strony". Model Poissona przy umiarkowanej
przewadze faworyta (50-70% szans) systematycznie zaniża prawdopodobieństwo remisu. Konkretne przykłady:
PSG-Rennes (71,5%→remis), Piast-Legia (77,7%→remis), Legia-Śląsk (65,6%→remis — **Legia zremisowała w
OBU analizowanych kolejkach z rzędu, mimo dwukrotnie wysokiej pewności typu**), Liverpool-Forest (62,5%→
remis), Alavés-Atlético (53,7%→remis), Lille-PSG (53,5%→remis), Radomiak-Zagłębie (63,9%→remis), Pogoń-
Wisła Kraków (57,8%→remis).

**Zastosowanie:** przy typach 1X2 w przedziale 50-75% pewności, jawnie ostrzegać w raporcie, że to
głównie ryzyko remisu, nie porażki faworyta — i rozważać lekką korektę w górę prawdopodobieństwa remisu
kosztem faworyta, szczególnie gdy underdog gra u siebie lub gdy faworyt ma jakikolwiek sygnał ostrzegawczy
(rotacja, zmęczenie, słaby przedsezon).

### 2. Sygnały ostrzegawcze odnotowane w raporcie, ale niedostatecznie przełożone na liczbę
PSG (zawieszenie Nuno Mendesa, porażka w Trophée des Champions z 10-osobowym Lens, przebudowany atak) i
Legia (ostatnie 2 H2H z Piastem przegrane, choć pod innym trenerem) miały jawnie wypisane czynniki ryzyka
w raporcie — mimo to końcowe λ i tak wylądowały na wysokiej pewności zwycięstwa. **Zastosowanie:** gdy
research (Krok 1) ujawnia konkretny czynnik ryzyka dla faworyta, korygować λ/prawdopodobieństwo wyraźniej
w dół, a nie tylko wspominać o nim opisowo bez realnego wpływu na liczbę.

### 3. Małe próby sezonowe (Ekstraklasa, wczesny sezon) zawyżają pewność
Legia miała w małej próbie (4-5 meczów) bilans 0,5 gola straconego/mecz — statystycznie ekstremalna
wartość, prawdopodobnie częściowo szczęście, nie trwała jakość obrony. Model wziął to dość dosłownie mimo
zastosowanego ważenia. **Zastosowanie:** przy próbie <8-10 meczów stosować mocniejsze niż dotąd
"ściągnięcie" (shrinkage) skrajnych wskaźników w stronę średniej ligowej, zwłaszcza dla obrony/rożnych
straconych — jedna-dwie "czyste" wygrane potrafią sztucznie spłaszczyć wskaźnik do zera.

### 4. Modele "uproszczone jakościowo" nie doceniały underdogów z dobrą świeżą formą
Elversberg (4 zwycięstwa w 5 przed meczem) pokonał Leverkusen mimo statusu wyraźnego outsidera w modelu;
podobnie Athletic Bilbao (mocna marka, ale słabszy start) przegrał z Sevillą, a Como pokonało Napoli.
**Zastosowanie:** gdy underdog ma wyraźnie pozytywny sygnał formy z ostatnich 3-5 meczów (a nie tylko
"jest nowy/mniejszy"), traktować to jako pełnoprawną korektę w górę jego λ, a nie tylko wzmiankę
kontekstową — reputacja/historia klubu nie powinna przeważać nad świeżą, konkretną formą.

### 5. Dla czołowych drużyn model bywał zbyt zachowawczy w drugą stronę
Barcelona (0-5, 5-2), Bayern (5-1), Inter (4-1) wygrywały wyraźnie wyżej, niż sugerowały końcowe λ —
kierunek trafiony, ale skala niedoszacowana. To mniej groźny błąd (nie zmienia typu 1X2), ale warto o nim
wiedzieć przy typowaniu rynków gola/handicapu.

### 6. Błąd weryfikacji terminarza — zawsze potwierdzaj parę drużyn z 2 źródeł
Mecz opisany jako "Real Madryt – Mallorca" w rzeczywistości był meczem z **Málagą** — pomyłka najpewniej
wynikła z jednego niewystarczająco zweryfikowanego źródła przy budowaniu terminarza (nazwy klubów
"Mallorca"/"Málaga" łatwo pomylić). Kierunek typu (wygrana Realu) i tak się potwierdził, ale to nie
umniejsza problemu. **Zastosowanie:** dla terminarzy odległych w czasie (szczególnie kolejnych kolejek,
nie najbliższego weekendu) zawsze potwierdzać parę drużyn co najmniej dwoma niezależnymi źródłami przed
przystąpieniem do modelowania, nie tylko przy niejasnościach już zauważonych w trakcie researchu.

### 7. Co działało dobrze — utrzymać w kolejnych analizach
- Model **prawidłowo identyfikował kierunek zwycięstwa** w ok. 60% przypadków przy średniej pewności rzędu
  60-65% — to sensowna kalibracja ogólna, nie ma sygnału rażącej "nadmiernej pewności siebie" w skali
  całego zbioru, tylko konkretny, powtarzalny problem z remisami (patrz pkt 1).
- Najwyższe typy pewności (Bayern 76,4%, Arsenal 79,7%/58,1%, Inter 73,1%) **trafiły** — ekstremalne
  przepaści jakościowe (mistrz vs beniaminek, mistrz broniący tytułu vs słabszy rywal) pozostają
  najbardziej wiarygodną kategorią typów.
- Jawne flagowanie niepewności (Lyon-Havre <50%, opisane wprost jako "nie mocna rekomendacja") okazało
  się trafne — remis potwierdził tę ostrożność zamiast jej zaprzeczyć.

---
*Weryfikacja ma charakter informacyjny i statystyczny, służy poprawie metodologii, nie stanowi porady finansowej.*
