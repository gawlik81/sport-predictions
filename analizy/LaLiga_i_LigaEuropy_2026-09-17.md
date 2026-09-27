# LaLiga (dokończenie kolejki 6) i Liga Europy (kolejka 1, dzień 2) — 17 września 2026

**Zakres:** dokończenie jornady 6 LaLiga (2 mecze — Levante-Athletic zostało odwołane
16.09 z powodu ulewy, termin TBA, nie wchodzi w zakres) + drugi dzień 1. kolejki fazy
ligowej Ligi Europy (9 meczów). Łącznie 11 meczów.

**Metodologia:** model bazowy Poissona dla goli (Krok 2-3 skilla), rożnych (Krok 4) i
fauli (Krok 5, tam gdzie obie strony mają wiarygodne dwustronne dane), z korektą
jakościową na bazie formy/kadry/kontekstu i profilu dyscyplinarnego indywidualnego
(Krok 6). Dla par międzyligowych (wszystkie mecze LE) zastosowano metodologię z Kroku 2
"mecze międzyligowe" — siła ataku/obrony liczona względem własnej ligi, szerszy margines
niepewności. Sezony krajowe są bardzo młode (3-8 kolejek), więc część współczynników to
małe próbki — zaznaczone przy każdym meczu.

---

# Część 1: LaLiga — dokończenie kolejki 6

## 1. Real Betis vs Getafe (19:00, La Cartuja)

**Forma:** Betis 4W-1L w ostatnich 5 (7:6), niepokonany i bez straty gola w 2 domowych
meczach. Getafe 1W-2D-2L (3:6) — **najgorszy atak ligi na wyjeździe (0 goli w 2 meczach)**.

**Kadra:** Betis bez Ruibala (uraz), Llorente wątpliwy; gra co 3 dni (LM w środku
tygodnia) — realne ryzyko rotacji Pellegriniego. Getafe bez Uche, Juanmi, Femeníi, Abqara.

**Model goli:** λ(Betis)=1,6, λ(Getafe)=0,55 — mocna przewaga gospodarza, ale skorygowana
w dół względem "czystych" 2 domowych meczów (2,0 GF/0,0 GA) z uwagi na ryzyko rotacji.

| Wynik | P | Kurs uczciwy |
|---|---|---|
| Betis | **63,0%** | 1,59 |
| Remis | 24,4% | 4,10 |
| Getafe | 12,5% | 8,02 |

**Model rożnych** (λ_dom=4,5, λ_wyj=4,6): praktycznie remisowy — przewaga Betis 42,0% /
remis 13,4% / Getafe 44,6%. Getafe koncedes lots at home for Betis but takes it back away.
Żaden sygnał ≥55%.

**Model fauli** (λ_dom=13,0, λ_wyj=13,0 — Getafe fizyczny styl Bordalása równoważy
przewagę Betisu): przewaga 46,1%/46,1% (remis rożny... tj. remis fauli 7,9%), Over 22,5 =
74,8%, **Over 24,5 = 60,4%**, Over 26,5 = 44,8%.

**Faule i kartki (indywidualnie):** Betis — Roca/Antony liderzy fauli (~1,0/90), Natan 2
żółte. Getafe — Terrats lider (1,6 faula/90), M.Martín 2 żółte. Nikt na progu zawieszenia
(5 żółtych w LaLiga). **Brak podstaw do dodatkowej korekty λ goli.**

*Podsumowanie: najsilniejszy, najczystszy sygnał to wygrana Betisu — forma, kadra i
statystyki sezonowe wskazują zgodnie w jedną stronę.*

---

## 2. Málaga vs Villarreal (21:30, La Rosaleda)

**Kontekst:** obie drużyny bez wygranej po 5 kolejkach — Málaga (beniamin) 3 pkt/18.
miejsce, Villarreal 2 pkt/19. miejsce, w kryzysie (3 porażki z rzędu).

**Forma:** Málaga 0W-3D-2L (2:8). Villarreal 0W-2D-3L (7:10).

**Kadra:** Villarreal bez Murillo, Diarry, Ochoi, Lobete; Calero wątpliwy (żebra). Málaga
— Pastor/Aznou/Dotor wrócili po infekcji, dostępni.

**Model goli:** λ(Málaga)=1,0, λ(Villarreal)=1,3 — lekka przewaga gościa za jakość kadry,
tłumiona przez własny kryzys formy.

| Wynik | P |
|---|---|
| Málaga | 28,6% |
| Remis | 28,0% |
| Villarreal | 43,4% |

**Model rożnych** (λ_dom=5,6, λ_wyj=5,0 — dane obu klubów obejmują częściowo ogon sezonu
2025/26, szerszy margines niepewności):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| Więcej rożnych: Málaga | 51,1% | 1,96 |
| Over 8,5 | **73,1%** | 1,37 |
| Over 9,5 | 61,5% | 1,63 |

**Model fauli** (λ_dom=12,75, λ_wyj=12,1 — dane Villarreal o faulach mają szeroki
przedział 11,3-14,2, niepewne rozbicie): przewaga 51,2%/48,5% remis 8,0%, Over 22,5=67,2%,
Over 24,5=51,5%.

**Faule i kartki (indywidualnie):** Villarreal — **Santi Comesaña lider fauli całej
czwórki analizowanych klubów (2,2/90)**. Málaga — Puga (1,8/90). Nikt na progu
zawieszenia.

*Podsumowanie: mecz dwóch kryzysowych zespołów bez jasnego faworyta w 1X2 — najsilniejszy
sygnał to łączna liczba rożnych (Over 8,5).*

---

# Część 2: Liga Europy — kolejka 1, dzień 2 (17.09)

## 3. OFI Crete vs Hoffenheim (18:45, Pankritio)

**Forma:** OFI (Grecja) świetna forma — pokonał Olympiacos 1-0 na wyjeździe, triumf w
Pucharze Grecji. Hoffenheim (Niemcy) niestabilny, **2,33 gola straconego/mecz** (leaky
defense mimo wyższej klasy ligowej).

**Model goli:** λ(OFI)=1,3, λ(Hoffenheim)=1,5 — umiarkowana przewaga gościa za jakość
Bundesligi, silnie tłumiona formą OFI i słabą defensywą Hoffenheim.

| Wynik | P |
|---|---|
| OFI | 32,9% |
| Remis | 25,1% |
| Hoffenheim | 41,9% |

**Model fauli** (λ_dom=11,29, λ_wyj=14,71 — oba kluby dość kontaktowe):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| **Więcej fauli: Hoffenheim** | **71,7%** | 1,40 |
| Over 22,5 | 74,8% |
| Over 24,5 | 60,4% |

**Rożne:** brak wiarygodnego rozbicia dla obu klubów — model pominięty.

**Faule i kartki:** sędzia Javier Alberola Rojas (Hiszpania) — surowy, ~3,5-4,2
żółtych/mecz. Brak aktualnych liderów indywidualnych fauli.

*Podsumowanie: 1X2 niepewny, ale przewaga Hoffenheim w faulach bardzo wyraźna.*

---

## 4. Levski Sofia vs Salzburg (18:45, Sofia)

**Forma:** Levski (Bułgaria) 8W-1D w 9 meczach, 3 czyste konta w 3 europejskich meczach
domowych. Salzburg (Austria) niepokonany w 12 meczach, ale **przegrał każdy z ostatnich 9
wyjazdowych meczów fazy głównej Ligi Europy** — istotny, tłumiący kontrapunkt.

**Model goli:** λ(Levski)=1,3, λ(Salzburg)=1,6 — przewaga jakościowa Salzburga tłumiona
fenomenalną formą domową Levski i serią porażek wyjazdowych Salzburga w LE.

| Wynik | P |
|---|---|
| Levski | 31,1% |
| Remis | 24,5% |
| Salzburg | 44,3% |

**Model rożnych** (λ_dom=5,84, λ_wyj=3,47 — Levski dominuje rożnie w lidze bułgarskiej,
ale to ekstrapolacja z meczów z słabszymi rywalami krajowymi, szerszy margines
niepewności):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| **Więcej rożnych: Levski** | **73,0%** | 1,37 |
| Over 8,5 | 58,4% | 1,71 |

**Faule i kartki:** brak aktualnych liderów indywidualnych. Sędzia: Mohammad Al-Emara
(Finlandia), ~3,3 żółtych/mecz.

*Podsumowanie: 1X2 niepewny (Salzburg lekki faworyt), ale przewaga rożna Levski —
oparta na realnej dominacji w lidze krajowej — jest czytelniejszym sygnałem, choć z
zastrzeżeniem, że to inny poziom rywalizacji.*

---

## 5. Lillestrøm vs Torreense (21:00, Åråsen)

**Kontekst:** Lillestrøm (Norwegia, ekstraklasa) awansował przez baraż. Torreense (Portugal
2. liga) — pierwszy klub spoza najwyższej klasy w fazie ligowej LE od Zurichu 2016/17.

**Forma:** Lillestrøm słaba passa domowa (2W-3L w ostatnich 5). Torreense 1W-2D-2L.

**Model goli:** λ(Lillestrøm)=1,5, λ(Torreense)=0,8 — różnica poziomów rozgrywkowych
(norweska ekstraklasa vs portugalska D2) przeważa nad słabą formą gospodarza.

| Wynik | P |
|---|---|
| Lillestrøm | 53,7% |
| Remis | 26,2% |
| Torreense | 20,0% |

**Model fauli** (λ_dom=13,0, λ_wyj=11,75):

| Rynek | P |
|---|---|
| **Więcej fauli: Lillestrøm** | **56,0%** |
| Over 22,5 | 66,5% |

**Rożne:** dane Torreense niereprezentatywne (tylko zespół U23) — model pominięty.

*Podsumowanie: różnica klas rozgrywkowych faworyzuje Lillestrøm, ale to jedyny sygnał
ponad próg pewności w tym meczu.*

---

## 6. Beşiktaş vs Marseille (21:00)

**Forma:** Beşiktaş (Turcja) 4W-1L, nowy trener Vincenzo Italiano, dobra forma domowa.
Marseille (Francja) w kryzysie — **3 porażki z rzędu w Ligue 1**, liczne kontuzje
(Gomes, Kondogbia, Nnadi, Paixão).

**Model goli:** λ(Beşiktaş)=1,8, λ(Marseille)=1,1 — wyraźna przewaga gospodarza z formy.

| Wynik | P |
|---|---|
| Beşiktaş | 53,5% |
| Remis | 23,1% |
| Marseille | 23,1% |

**Model fauli** (λ_dom=13,5, λ_wyj=11,375):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| Więcej fauli: Beşiktaş | 62,8% |
| **Over 22,5** | **67,4%** | 1,48 |
| Over 24,5 | 51,7% |

**Model rożnych** (λ_dom=4,35, λ_wyj=5,45 — dane Beşiktaşu bez rozbicia "against",
niższa wiarygodność): przewaga Marseille 57,5%.

*Podsumowanie: forma jednoznacznie po stronie Beşiktaşu, ale najsilniejszy, w pełni
ugruntowany sygnał to łączna liczba fauli.*

---

## 7. Celtic vs Ferencváros (21:00, Glasgow)

**Forma:** Celtic (Szkocja) **6W-0D-0L, gole 14:3**, dominująca forma domowa. Ferencváros
(Węgry) solidny (8W-1D-1L w ostatnich 10 meczach wszystkich rozgrywek), ale liga węgierska
generalnie słabsza od szkockiej.

**Kadra:** Celtic bez Osmanda, Johnstona, Joty; **Oxlade-Chamberlain zawieszony**
(okoliczności czerwonej kartki niejasne w źródłach). Ferencváros — Pappoe/Ötvös wątpliwi.

**Model goli:** λ(Celtic)=2,2, λ(Ferencváros)=0,8 — duża przewaga gospodarza z formy i
różnicy klas ligowych.

| Wynik | P | Kurs uczciwy |
|---|---|---|
| **Celtic** | **68,6%** | 1,46 |
| Remis | 18,4% | 5,42 |
| Ferencváros | 12,2% | 8,18 |

**Rożne/faule:** dane Ferencváros zbyt skąpe dla wiarygodnego modelu dwustronnego
(pominięto — nie zgaduję liczb). Celtic samodzielnie ma bardzo silny profil rożny
(12,6 łącznie/mecz, lider ligi), co dodatkowo wspiera obraz dominacji, ale bez
rywala-referencji nie da się policzyć solidnego % przewagi.

*Podsumowanie: najbardziej jednoznaczny wynikowo mecz dnia — dominująca forma domowa
Celticu kontra słabsza liga węgierska.*

---

## 8. Viktoria Plzeň vs Union SG (21:00)

**Kontekst:** Union SG dotarł do LE po eliminacji w playoffie Ligi Mistrzów, ale **traci 7
zawodników** — 3 zawieszonych (Van de Perre, Zorgane, Florucz, kumulacja kartek z burzliwego
zakończenia playoffu LM) + 4 niedostępnych z innych powodów.

**Forma:** Plzeň (Czechy) 2W-4D-2L, mecze wysoko punktowane w obie strony. Union SG
(Belgia) jakościowo silniejszy, ale osłabiony kadrowo.

**Model goli:** λ(Plzeň)=1,5, λ(Union SG)=1,3 — normalna przewaga jakościowa Union SG
prawie zniwelowana przez masowe absencje.

| Wynik | P |
|---|---|
| Plzeň | 41,9% |
| Remis | 25,1% |
| Union SG | 32,9% |

**Rożne/faule:** brak wiarygodnych dwustronnych danych dla obu klubów — model pominięty.

*Podsumowanie: żaden rynek nie przekracza progu pewności — najbardziej wyrównany i
najmniej przewidywalny mecz dnia, głównie z powodu skali osłabień Union SG.*

---

## 9. Crystal Palace vs Lech Poznań (21:00, Selhurst Park)

**Kontekst:** bukmacherzy dają Crystal Palace zdecydowanym faworytem (~1,40), ale
**leżące pod tym liczby są dużo bliższe niż sugeruje sama różnica lig**.

**Forma:** Crystal Palace (Anglia) w kryzysie: **1W-3L, 2,75 gola straconego/mecz**,
16. miejsce PL. Lech Poznań (Polska) 3. miejsce Ekstraklasy, 1,71 GF/0,86 GA, **rekord
Polski: 31 kolejnych meczów europejskich ze strzeloną bramką**.

**Kadra:** Crystal Palace bez Chadiego Riada, **Mateta (główny napastnik) na pewno nie
zagra**, kilku zawodników nie zgłoszonych do kadry LE (Doucouré, Lerma, Gozo, Guéssand,
Matthews). Lech bez Gholizadeha, Douglasa, Kozubala; niejasny status Sayyadmanesha
(najlepszy strzelec, problem wizowy).

**Model goli:** λ(CP)=1,3, λ(Lech)=1,15 — **model wyraźnie bliższy niż kurs bukmacherski**
(~65-70% implikowane dla CP) — leżąca u podstaw forma i kadra CP (leaky defense, brak
napastnika) nie uzasadniają tak dużego dystansu. To jawna rozbieżność model-vs-rynek,
warto ją odnotować zamiast ukrywać (zasada transparentności skilla).

| Wynik | P |
|---|---|
| Crystal Palace | 40,0% |
| Remis | 27,2% |
| Lech | 32,8% |

**Model fauli** (λ_dom=9,0, λ_wyj=10,8 — dane CP z rozbiciem dom/wyjazd, Lech tylko
łączna wartość, jeden element modelu oparty na przybliżeniu):

| Rynek | P |
|---|---|
| **Więcej fauli: Lech** | **61,5%** |
| Over 16,5 | 76,6% |
| Over 18,5 | 60,2% |

**Rożne:** dane obu klubów tylko jednostronne ("zdobyte", bez "oddane") — model zbyt
niepewny, pominięty jako pozycja rankingowa (orientacyjnie: Lech generuje dużo więcej
rożnych w lidze krajowej, ale ekstrapolacja na rywala z wyższej ligi jest ryzykowna).

**Faule i kartki:** Lech — 7 zawodników z 1 żółtą, nikt bliski zawieszenia; licznik LE
zerowy dla obu (Lech debiutuje w fazie ligowej po 6 latach). Sędzia: Michal Ocenáš
(Słowacja).

*Podsumowanie: to mecz, gdzie warto zaufać modelowi bardziej niż kursom — CP nie jest
tak wyraźnym faworytem, jak sugeruje rynek, biorąc pod uwagę realny stan formy i kadry.*

---

## 10. Juventus vs N.E.C. Nijmegen (21:00, Turyn)

**Forma:** Juventus (Włochy) 2W-1D-1L, silna obrona domowa (0,50 GA/mecz w 2 meczach).
NEC (Holandia) w kryzysie defensywnym — **15 goli straconych w 6 ostatnich meczach, 9 bez
czystego konta**, ale zaskakująco niezła skuteczność na wyjeździe (2,33 GF).

**Kadra:** Juventus bez Locatellego (kapitan, po operacji), Yıldıza, Thurama, Bogi,
Ekhatora, Milika, Cabala; **Lloyd Kelly zawieszony w Lidze Europy** (kartka
kontynentalna). NEC — **Crettaz (bramkarz) zawieszony** po czerwonej z barażu LM.

**Model goli:** λ(Juventus)=1,6, λ(NEC)=1,1 — przewaga Serie A i solidnej obrony domowej
Juve, tłumiona własnymi problemami kadrowymi w ataku.

| Wynik | P |
|---|---|
| Juventus | 48,8% |
| Remis | 24,9% |
| NEC | 26,1% |

**Model fauli** (λ_dom=15,25, λ_wyj=11,585 — **Juventus ma bardzo wysoki wskaźnik fauli
popełnionych, 16,0/mecz**, jeden z najwyższych w całej analizie):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| **Więcej fauli: Juventus** | **73,0%** | 1,37 |
| Over 24,5 | 66,5% |
| Over 26,5 | 51,3% |

**Rożne:** brak danych dla obu klubów (paywall) — model pominięty.

*Podsumowanie: 1X2 niepewny, ale bardzo wysoki wskaźnik fauli Juventusu daje najsilniejszy
sygnał w tym meczu.*

---

## 11. Real Sociedad vs Bournemouth (21:00, San Sebastián)

**Kontekst:** oba kluby w kryzysie formy w swoich ligach. Bournemouth debiutuje w
europejskich pucharach w historii klubu.

**Forma:** Sociedad 2W-1D-3L, nie strzelili gola w połowie meczów. Bournemouth 0W-3D-1L
("Poor", 0,75 pkt/mecz).

**Kadra:** Sociedad bez Odriozoli (długoterminowo), **Zubeldia (kontuzja) i Aramburu
(zawieszenie za czerwoną z europejskich rozgrywek vs Man Utd)** — dwóch środkowych
obrońców naraz. Bournemouth bez Araujo, Adli, Milosavljevicia, Kroupiego.

**Model goli:** λ(Sociedad)=1,1, λ(Bournemouth)=1,3 — dwa słabe w formie zespoły, lekka
przewaga gościa, tłumiona osłabieniami obrony Sociedad.

| Wynik | P |
|---|---|
| Sociedad | 31,4% |
| Remis | 27,5% |
| Bournemouth | 41,1% |

**Model fauli** (λ_dom=14,79, λ_wyj=11,25 — **Sociedad w domu bardzo faulująca,
15,33/mecz**, zapewne efekt gry pod presją przy słabej formie):

| Rynek | P | Kurs uczciwy |
|---|---|---|
| **Więcej fauli: Sociedad** | **72,5%** | 1,38 |
| Over 24,5 | 60,7% |
| Over 26,5 | 45,1% |

**Model rożnych** (λ_dom=5,06, λ_wyj=5,25 — dane Sociedad częściowo z sezonu 2025/26,
szerszy margines): przewaga Bournemouth 46,0% — brak sygnału ≥55%.

*Podsumowanie: 1X2 niepewny, ale bardzo wysoka faulowość Sociedad w tym sezonie u siebie
to najsilniejszy, dobrze ugruntowany sygnał.*

---

# Najpewniejsze predykcje na dziś (17.09.2026)

**Zasady:** 1 mecz = 1 pozycja (najsilniejszy pojedynczy rynek spośród 1X2/rożne/faule),
próg wejścia ≥55%, "Over 1,5 gola" i BTTS nie liczą się jako headline (zbyt trywialne —
wysokie praktycznie zawsze). Rynki oparte na sfabrykowanych/zgrubnych placeholderach (np.
korekta korców Celtic-Ferencváros czy CP-Lech, gdzie jedna ze stron nie miała żadnych
danych) zostały odrzucone na rzecz lepiej ugruntowanych alternatyw z tego samego meczu.

**Wykluczony 1 mecz z 11:** Viktoria Plzeň – Union SG (żaden rynek nie osiągnął 55% —
mecz zbyt niejasny, głównie z powodu masowych absencji Union SG neutralizujących
normalną przewagę klasową).

| # | Mecz | Rozgrywki | Predykcja | P |
|---|---|---|---|---|
| 1 | Málaga – Villarreal | LaLiga | Over 8,5 rożnych łącznie | **73,1%** |
| 2 | Levski Sofia – Salzburg | Liga Europy | Levski więcej rożnych | **73,0%** |
| 3 | Juventus – N.E.C. Nijmegen | Liga Europy | Juventus więcej fauli | **73,0%** |
| 4 | Real Sociedad – Bournemouth | Liga Europy | Sociedad więcej fauli | 72,5% |
| 5 | OFI Crete – Hoffenheim | Liga Europy | Hoffenheim więcej fauli | 71,7% |
| 6 | Celtic – Ferencváros | Liga Europy | Celtic wygrywa | 68,6% |
| 7 | Beşiktaş – Marseille | Liga Europy | Over 22,5 fauli łącznie | 67,4% |
| 8 | Real Betis – Getafe | LaLiga | Betis wygrywa | 63,0% |
| 9 | Crystal Palace – Lech Poznań | Liga Europy | Lech więcej fauli | 61,5% |
| 10 | Lillestrøm – Torreense | Liga Europy | Lillestrøm więcej fauli | 56,0% |

**Krótkie uzasadnienie:**
- **Faule dominują dzisiejszy ranking** (6 z 10 pozycji) — dzień z wieloma meczami
  międzyligowymi, gdzie różnice stylu gry (drużyny fizyczne vs techniczne) dają
  czytelniejszy sygnał niż niepewne różnice klasowe w 1X2.
- **#1-#2** (rożne) to jedyne dwie pozycje rożne dziś — obie oparte na realnych,
  dwustronnych danych, choć #2 (Levski) ekstrapoluje dominację z ligi bułgarskiej na
  europejskiego rywala, więc traktuj z lekką rezerwą.
- **#6 i #8** to jedyne pozycje 1X2 w rankingu — Celtic (dominująca forma domowa) i Betis
  (Getafe ma najgorszy atak wyjazdowy ligi) to najbardziej jednoznaczne wyniki dnia.
- **#9 (Crystal Palace-Lech)** wart uwagi: model bazowy 1X2 (CP 40,0%/Lech 32,8%) jest
  wyraźnie bliższy niż implikuje kurs bukmacherski (~1,40 dla CP, czyli ~65-70%) — realny
  stan formy i kadry CP (2,75 gola straconego/mecz, brak Katety) nie uzasadnia takiej
  różnicy. To rozbieżność model-vs-rynek warta zaznaczenia, a nie ukrycia.
- **Odrzucone jako niewiarygodne** (nie weszły do rankingu mimo wysokich liczb): rożne w
  meczach Celtic-Ferencváros i Crystal Palace-Lech — obie strony brakowały dwustronnych
  danych, a użyte przybliżenia były zbyt zgrubne, by prezentować je jako pewny sygnał.

---

# Dodatek: 5 "superpewniaków"

To inne zadanie niż TOP 10 wyżej — tam celowo wykluczyłem "Over 1,5 gola" i BTTS jako
headline, bo są wysokie praktycznie w każdym meczu i nie różnicują (mało "insightowe").
Dla "superpewniaka" priorytet jest odwrotny: **maksymalna surowa pewność**, nawet jeśli
rynek jest generyczny. Dlatego to zestawienie bierze najwyższe prawdopodobieństwa z całej
analizy 11 meczów, bez tego wykluczenia (wciąż z wyjątkiem rynków bez sensu bukmacherskiego,
np. "obie drużyny miały ≥1 rożny" — to ~100% z definicji i nic nie mówi o meczu).

| # | Mecz | Predykcja | P | Kurs uczciwy |
|---|---|---|---|---|
| 1 | Celtic – Ferencváros | Over 1,5 gola | **80,1%** | 1,25 |
| 2 | Levski Sofia – Salzburg | Over 1,5 gola | **78,5%** | 1,27 |
| 3 | Beşiktaş – Marseille | Over 1,5 gola | **78,5%** | 1,27 |
| 4 | OFI Crete – Hoffenheim | Over 1,5 gola | **76,9%** | 1,30 |
| 5 | Juventus – N.E.C. Nijmegen | Over 1,5 gola | **75,1%** | 1,33 |

**Uzasadnienie #1-4:** wszystkie 4 mecze mają sumę oczekiwanych goli (λ_dom+λ_wyj) między
2,7 a 3,0 — wystarczająco dużo, żeby "co najmniej 2 gole w meczu" było bezpieczne
niezależnie od tego, kto wygra. To nie przypadek, że wszystkie 4 to ten sam rynek: to
jest właśnie mechanizm, przez który matematyka Poissona generuje "pewniaki" — łączna
liczba goli jest dużo stabilniejsza statystycznie niż to, KTO je strzeli. Każdy z tych 4
meczów ma inny rozkład sił (Celtic i Beşiktaş to zdecydowani faworyci, Levski i OFI to
raczej wyrównane starcia), ale w każdym z nich to właśnie total goals jest
najbezpieczniejszym zakładem.

**Uzasadnienie #5:** kolejna pozycja z rynku "Over 1,5 gola" (λ_dom=1,6 Juventus, λ_wyj=1,1
NEC, suma 2,7) — pełniej ugruntowana niż poprzednia wersja tej pozycji (Crystal
Palace-Lech, oparta częściowo na przybliżeniu dla strony Lecha): tu obie strony mają
realne, rozbite na dom/wyjazd dane sezonowe. Juventus ma silną obronę domową (0,50
gola straconego/mecz w 2 meczach), a NEC mimo kryzysu defensywnego (15 goli straconych w
6 meczach) ma zaskakująco niezłą skuteczność na wyjeździe (2,33 gola/mecz) — to właśnie
ta kombinacja (solidny gospodarz + skuteczny, choć dziurawy defensywnie gość) daje wysoką
szansę na 2+ gole niezależnie od tego, kto wygra.

**Jeśli szukasz większej różnorodności rynków** (nie tylko "Over 1,5"/faule) przy
niewiele niższej pewności, alternatywa to pozycje #1-#4 z głównego rankingu TOP 10 wyżej
(73,1% / 73,0% / 73,0% / 72,5% — rożne i faule w różnych meczach).

**Uwaga o korelacji:** tych 5 zakładów jest w pełni niezależnych (5 różnych meczów, różne
rozgrywki/dni), więc w przeciwieństwie do wcześniejszych zestawień można je bezpiecznie
łączyć w jeden kupon AKO bez utraty rzetelności szacunku łącznej szansy (iloczyn ~28,5%
na wszystkie 5 na raz, jeśli o to chodzi — dla samych pierwszych 4 wychodzi ~38%).

---

# Dodatek 2: superpewniaki na BTTS

BTTS (obie drużyny strzelają gola) to z natury rynek bliższy "50/50" niż total goals —
najwyższe prawdopodobieństwo w całej dzisiejszej analizie to 66,3%, dużo niżej niż 80,1%
dla "Over 1,5 gola" wyżej. To nie błąd modelu, tylko właściwość rynku: rozstrzyga o nim
zarówno atak, jak i obrona OBU stron naraz, więc jest z natury trudniejszy do
jednoznacznego przewidzenia niż samo "ile razem". Poniżej wszystkie mecze z dzisiejszej
analizy, gdzie BTTS (Tak lub Nie — bierz stronę z wyższym %) przekracza 55%:

| # | Mecz | Predykcja | P | Kurs uczciwy |
|---|---|---|---|---|
| 1 | Real Betis – Getafe | BTTS – Nie | **66,3%** | 1,51 |
| 2 | Levski Sofia – Salzburg | BTTS – Tak | **57,9%** | 1,73 |
| 3 | Lillestrøm – Torreense | BTTS – Nie | **57,3%** | 1,75 |
| 4 | OFI Crete – Hoffenheim | BTTS – Tak | **56,4%** | 1,77 |

*(Viktoria Plzeň – Union SG ma identyczne 56,4% na BTTS Tak, ale ten mecz odrzuciłem z
głównej analizy z powodu braku pewnego sygnału gdzie indziej — traktuj jako słabszy
"5. wybór" niż powyższe 4. Beşiktaş – Marseille ma 55,5% na BTTS Tak, tuż nad progiem —
kolejna rezerwowa opcja, jeśli chcesz więcej niż 4 pozycje.)*

**Uzasadnienie:**
- **#1 (Betis-Getafe, BTTS Nie)** — najsilniejsza pozycja, bo oparta na dwóch zgodnych
  faktach: Getafe ma najgorszy atak wyjazdowy ligi (0 goli w 2 meczach), a Betis nie
  stracił gola w 2 domowych meczach. To rzadki przypadek, gdzie atak i obrona jednej
  strony wzmacniają się nawzajem w tym samym kierunku.
- **#2 (Levski-Salzburg, BTTS Tak)** — obie strony regularnie strzelają (Levski 2,3
  gola/mecz w lidze, Salzburg 2,5), więc mimo niepewnego 1X2 obaj przynajmniej trafiają do
  siatki jest prawdopodobne.
- **#3 (Lillestrøm-Torreense, BTTS Nie)** — różnica klas rozgrywkowych (norweska
  ekstraklasa vs portugalska D2) sprawia, że Torreense może po prostu nie trafić do
  siatki, niezależnie od tego jak skończy się mecz.
- **#4 (OFI-Hoffenheim, BTTS Tak)** — obie strony mają realny atak, a Hoffenheim dodatkowo
  bardzo dziurawą obronę (2,33 gola straconego/mecz) — OFI ma spore szanse trafić.
- **Uwaga o korelacji z poprzednim zestawem:** OFI Crete-Hoffenheim występuje też w
  zestawie "Over 1,5 gola" wyżej — to nie przypadek (oba rynki napędza ta sama leżąca u
  podstaw wysoka oczekiwana liczba goli w tym meczu), więc nie traktuj ich jako w pełni
  niezależnych, jeśli łączysz obie listy w jeden kupon.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani
zachęty do zakładów. Graj odpowiedzialnie.*
