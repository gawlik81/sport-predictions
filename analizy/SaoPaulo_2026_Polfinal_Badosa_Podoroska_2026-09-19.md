# Paula Badosa [2] vs Nadia Podoroska
**Turniej:** WTA SP Open São Paulo 2026 (WTA 250, kort twardy) | **Runda:** Półfinał | **Nawierzchnia:** twarda | **Format:** best-of-3, tiebreak standardowy do 7 (WTA 250, brak specjalnych zasad dla seta decydującego) | **Termin:** sobota, 19.09.2026, ok. 14:00, kort 1

## Uwaga wstępna: weryfikacja statusu meczu
Zgodnie z instrukcją zweryfikowano status meczu przed analizą. **Mecz NIE
został jeszcze rozegrany w momencie tej analizy** — wynik "7-6(5), 3-6, 6-3",
który krążył jako niepotwierdzona wzmianka, dotyczy w rzeczywistości
**ćwierćfinału Podoroska vs Suzan Lamens** (Podoroska wygrała tym właśnie
wynikiem), a nie półfinału z Badosą. Potwierdzone niezależnie przez
tennismajors.com (status "Coming soon", data 19.09.2026) oraz tennistonic.com
(zapowiedź meczu na sobotę, 14:00, kort 1, z kursami bukmacherskimi — a więc
mecz jeszcze się nie odbył). Poniżej pełna metodologia predykcji.

## Kontekst i forma
- **Forma Badosa** (2026): bilans sezonu ok. 23W-18P (różne źródła podają
  20-18/26-18 w zależności od metody liczenia), ranking WTA **#70** — mocno
  poniżej kariery (kariera: #2), efekt sezonu 2025 zdominowanego przez
  kontuzję pleców (grała zaledwie 2 mecze po Wimbledonie 2025). W 2026
  wróciła "zdrowa i niebezpieczna" (cytat WTA: "Badosa is back — and she's
  dangerous"), wygrała tytuł WTA 125 w Båstad. W tym turnieju: pokonała
  Mikulskyte 6-3 6-2, Ortenzi 4-6 6-2 6-2, Stoianę 6-4 6-2 (ćwierćfinał) —
  tylko 1 set stracony w 3 meczach, solidna forma turniejowa.
- **Forma Podoroska**: powraca po **ponad rocznej przerwie z powodu
  kontuzji** (wróciła do gry w marcu 2026), ranking spadł z kariery #36 do
  ok. #317-449 (źródła się różnią, ranking spada dynamicznie w trakcie
  dobrego turnieju). Bilans 2026: 29W-10P, **16W-3P na kortach twardych** —
  bardzo solidny wynik jak na powracającą zawodniczkę. To jej pierwszy
  półfinał WTA od września 2023 i najlepszy wynik całego comebacku. W tym
  turnieju: pokonała Stefanini, 5. rozstawioną Evę Lys (bardzo dobry wynik),
  a w ćwierćfinale Lamens 7-6(5), 3-6, 6-3 — **trzysetowy, wyczerpujący
  mecz z tie-breakiem w 1. secie**, realne ryzyko zmęczenia w półfinale.
- **H2H**: Badosa prowadzi **2-0, oba na kortach twardych**. Ostatni mecz:
  Igrzyska w Tokio, Badosa wygrała 6-2, 6-3. Wcześniej: Badosa 7-5, 6-4
  (kwalifikacje, Tampico). Wyraźna przewaga psychologiczna i stylistyczna
  Badosy w tym zestawieniu.
- **Kondycja/zmęczenie**: kluczowa asymetria tego meczu. Podoroska rozegrała
  trzysetowy, blisko 3-godzinny mecz w ćwierćfinale (na podstawie wyniku
  7-6, 3-6, 6-3) i wcześniej pokonała mocno rozstawioną Lys — kumulacja
  wysiłku w kilka dni turnieju. Badosa zakończyła swój ćwierćfinał w dwóch
  setach (6-4, 6-2), krótszy czas na korcie. To realny czynnik na korzyść
  Badosy, niezależnie od różnicy rankingowej.
- **Inne czynniki**: obie zawodniczki mają historycznie słaby bilans w
  półfinałach — Badosa 5-13 w karierze, Podoroska 0-4 (przegrała wszystkie
  dotychczasowe półfinały) — sygnał, że żadna z nich nie jest "specjalistką"
  od tej rundy, więc nie traktuję tego jako asymetrycznej korekty w żadną
  stronę, jedynie jako ogólny czynnik niepewności rundy. Kursy bukmacherskie
  (Tennis Tonic): Badosa 1.196, Podoroska 4.55 — rynek wycenia Badosę jako
  zdecydowaną faworytkę (~84% z odjętą marżą).

## Model bazowy (prawdopodobieństwo wygrania punktu na serwisie)
Średnia turowa WTA na twardym korcie: ~55-57% punktów wygranych na serwisie.
**Brak było dostępnych szczegółowych statystyk serwisu/returnu (1./2. serwis,
% returnu) dla żadnej z zawodniczek w publicznie dostępnych źródłach** (strony
WTA nie ujawniły tych danych w dostarczonej treści) — zaznaczam to wprost,
zgodnie z zasadą "szeroki, ale uczciwy przedział zamiast zmyślonej precyzji".

Oszacowanie oparte na dostępnych fragmentach danych i kontekście jakościowym:
- Badosa: 55.7% pierwszego serwisu w grze, 4.09 asów/mecz (solidny, ale nie
  ekstremalny serwis), 36.8% wykorzystanych break pointów jako returnerka
  (dobry return) — była top-3 WTA w karierze, ma znacznie bardziej
  kompletny, ofensywny styl niż przeciętna zawodniczka na tym poziomie
  rankingowym. Szacuję p_serve nieco powyżej średniej turowej: **60%**.
- Podoroska: brak precyzyjnych statystyk serwisu; styl typowo
  kontrujący/wytrzymałościowy (najlepsza nawierzchnia kariery: mączka,
  42.6% win rate), mniej kojarzona z dominującym serwisem, choć bilans
  16-3 na twardym w 2026 sugeruje solidną ogólną grę na tej nawierzchni.
  Dodatkowo zmęczenie po trzysetowym ćwierćfinale prawdopodobnie obniży jej
  skuteczność serwisową w tym meczu. Szacuję p_serve w okolicy/lekko poniżej
  średniej turowej, obniżone o zmęczenie: **54%**.

**p(Badosa na serwisie) = 60.0%, p(Podoroska na serwisie) = 54.0%**

## Prawdopodobieństwa (model: `tennis_model.py --p-a-serve 0.60 --p-b-serve 0.54 --best-of 3`)

### Zwycięzca meczu
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| **Badosa wygrywa** | **78.5%** | **1.27** |
| Podoroska wygrywa | 21.5% | 4.66 |

*Uzasadnienie: przewaga rankingowa, lepszy dotychczasowy przebieg turnieju
(mniej rozegranych setów, brak trzysetowych bojów), H2H 2-0 na twardym i
świeży powrót do zdrowia dają Badosie wyraźną przewagę. Model (78.5%) jest
lekko konserwatywniejszy niż rynek bukmacherski (~84% po odjęciu marży) —
uwzględnia to niepewność związaną z brakiem szczegółowych danych serwisu/
returnu oraz fakt, że Podoroska jest w najlepszej dyspozycji swojego
comebacku, więc nie zasługuje na automatyczne, ekstremalne odrzucenie mimo
niskiego rankingu.*

### Dokładny wynik meczu (sety)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 2-0 dla Badosy | 49.1% | 2.04 |
| 2-1 dla Badosy | 29.4% | 3.40 |
| 1-2 dla Podoroskiej | 12.5% | 7.98 |
| 0-2 dla Podoroskiej | 8.9% | 11.18 |

### Total gemów i handicap gemowy (sekcja priorytetowa)
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 18.5 gemów | 72.4% | 1.38 |
| Over 19.5 gemów | 65.0% | 1.54 |
| Over 20.5 gemów | 59.0% | 1.70 |
| Over 21.5 gemów | 53.6% | 1.87 |

- **Oczekiwana liczba gemów: 23.2**
- Uzasadnienie: różnica w p_serve (60% vs 54%) jest umiarkowana, nie
  ekstremalna — model przewiduje mecz z realną szansą na 3 sety (37.9% w
  sumie: 29.4% Badosa 2-1 + 12.5% Podoroska 1-2 czyli razem >6 gemów
  dodatkowych względem czystego 2-0), co podnosi oczekiwaną liczbę gemów.
  Obie zawodniczki mają wystarczająco solidny serwis, by unikać serii
  szybkich przełamań — total lekko powyżej "środka stawki" dla meczu
  best-of-3 kobiet.

### Pierwszy set
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Badosa wygrywa 1. set | 70.1% | 1.43 |
| Podoroska wygrywa 1. set | 29.9% | 3.34 |

Najbardziej prawdopodobne wyniki 1. seta: 6-3 (Badosa, 20.8%), 4-6
(Podoroska, 11.0%), 6-4 (Badosa, 11.0%), 6-2 (Badosa, 10.5%), 6-1 (Badosa,
10.5%), 7-6 (Badosa, 7.7%).

### Asy, podwójne błędy, break pointy
- Badosa: przy jej sezonowej średniej ~4.09 asów/mecz i oczekiwanych ~12
  gemach serwisowych w tym meczu, szacuję **4-8 asów** w tym spotkaniu.
  Podwójne błędy: przedział szeroki, ok. **3-6** (dokładny wskaźnik DF/mecz
  niepewny z dostępnych danych).
- Podoroska: brak wiarygodnych danych o asach/DF — szacuję szeroko, w
  oparciu o typowy profil returnerki/kontrującej: **2-5 asów**, **3-6
  podwójnych błędów** (może wzrosnąć z powodu zmęczenia).
- Break pointy: różnica w p_serve (60% vs 54%) przekłada się na oczekiwaną
  przewagę przełamań dla Badosy — spójne z rozkładem `match_score` powyżej
  (przewaga w wygranych setach 2-0/2-1).

### Ryzyko wycofania
Brak konkretnych sygnałów kontuzji u żadnej z zawodniczek w świeżych
źródłach na dziś, poza ogólnym kontekstem: Badosa wraca po sezonie 2025
zdominowanym przez kontuzję pleców (obecnie zdrowa), Podoroska wraca po
ponadrocznej przerwie (obecnie zdrowa, ale z akumulowanym zmęczeniem
turniejowym). Nie identyfikuję podwyższonego ryzyka wycofania w trakcie
meczu.

## Podsumowanie
Badosa jest wyraźną, ale nie przytłaczającą faworytką (78.5% wg modelu,
rynek bukmacherski wycenia ją jeszcze wyżej, ~84%) — przewaga rankingowa,
H2H 2-0 na twardym i świeższe nogi (2 sety w ćwierćfinale vs 3 sety i
tie-break u Podoroskiej) przemawiają zdecydowanie na jej korzyść. Total
gemów (oczekiwane 23.2, Over 20.5 na 59%) jest umiarkowanie wysoki — mecz
może pójść w 3 sety, zwłaszcza jeśli zmęczenie Podoroskiej nie da o sobie
znać od razu. Główne ryzyko dla typu na Badosę to brak szczegółowych
statystyk serwisu/returnu (oszacowanie jakościowe, nie w pełni oparte na
twardych danych sezonowych) oraz fakt, że Podoroska gra najlepszy tenis
swojego comebacku — nie jest to typowy "kryzysowy underdog", tylko
zawodniczka w rosnącej formie, co nieco podnosi ryzyko niespodzianki
względem czysto rankingowej oceny.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady
finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*
