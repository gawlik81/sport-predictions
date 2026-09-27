# Arsenal vs Manchester City

**Rozgrywki:** UWAGA — w tej chwili **nie ma** zaplanowanego meczu Arsenal – Manchester City w ramach Premier League (zob. sekcja "Ważna uwaga" poniżej). Najbliższe spotkanie tych drużyn to **FA Community Shield 2026** (oficjalny superpuchar Anglii, mecz towarzyski między mistrzem Premier League a zdobywcą Pucharu Anglii).
**Termin:** niedziela, 16 sierpnia 2026, godz. 15:00 (Principality Stadium, Cardiff — boisko neutralne)
**Ranga meczu:** Oficjalny "curtain raiser" przed sezonem 2026/27 — prestiżowy, ale niskostawkowy pojedynek otwierający sezon, często z rotacjami składu i nowymi twarzami w sztabach.

## Ważna uwaga (przeczytaj przed resztą raportu)

Sezon Premier League 2025/26 **zakończył się 24 maja 2026** — Arsenal zdobył mistrzostwo (85 pkt, +44 bilans bramek), a Manchester City był wicemistrzem (78 pkt). Obie drużyny rozegrały już w tym sezonie **dwa** mecze ligowe między sobą:
- Arsenal vs Manchester City (21.09.2025, Emirates) — wynik nie został potwierdzony w dostępnych źródłach
- Manchester City 2–1 Arsenal (19.04.2026, Etihad) — gole: Cherki, Haaland (City); Havertz (Arsenal)

**Kolejny mecz Premier League** między tymi drużynami odbędzie się dopiero w sezonie 2026/27 (terminarz tej rundy jeszcze nie został opublikowany na dzień dzisiejszy — sezon 2025/26 zakończył się dopiero 24 maja, terminarze nowego sezonu publikuje się zwykle w czerwcu).

Najbliższym faktycznym starciem obu klubów jest więc **FA Community Shield (16 sierpnia 2026, Cardiff)** — mecz towarzyski, a nie ligowy. Poniższa analiza dotyczy **tego** meczu, traktowanego jako najbliższe spotkanie Arsenal – Manchester City, z wyraźnym zaznaczeniem, że ranga i kontekst różnią się od standardowego meczu PL.

Dodatkowy istotny czynnik: latem 2026 **Pep Guardiola odszedł z Manchester City** po 10 latach (ogłoszone w maju 2026), a jego następcą ma zostać (wg doniesień medialnych) **Enzo Maresca**. To oznacza, że City wejdzie w ten mecz pod wodzą nowego trenera, prawdopodobnie z eksperymentalnym składem/taktyką typową dla pierwszego meczu nowego szkoleniowca i okresu przedsezonowego — element dużej niepewności, którego żaden model statystyczny oparty na danych z sezonu 2025/26 nie uchwyci.

## Kontekst i forma

- **Arsenal (sezon 2025/26, Premier League, 38 meczów)**: Mistrz Anglii — 26W-7D-5L, 85 pkt, 71 bramek strzelonych, 27 straconych (+44). Najlepsza defensywa w Europie (0,71 gola straconego/mecz, 19 czystych kont, najmniej strzałów oddanych przeciwnikom — 310 i najmniej "big chances" — 50 w lidze). Arsenal ustanowił rekord PL pod względem goli z rzutów rożnych w sezonie (19) i ogółem ze stałych fragmentów gry (25).
- **Manchester City (sezon 2025/26, Premier League)**: Wicemistrz — 78 pkt, 69 bramek strzelonych, 32 stracone (+37/+42 w zależności od źródła — drobna rozbieżność danych między serwisami). Erling Haaland: 25 goli w PL (król strzelców), drugi najlepszy bramkarz ligi pod względem czystych kont (Donnarumma, 11/12).
- **H2H (sezon 2025/26)**: dwa mecze ligowe — w kwietniu 2026 City wygrało 2-1 na Etihadzie (Haaland decydujący gol w 65. minucie), co zmniejszyło przewagę Arsenalu w tabeli do 3 punktów na finiszu sezonu. Wynik pierwszego meczu (wrzesień 2025, Emirates) nie został potwierdzony w dostępnych źródłach.
- **Kadra / zmiany trenerskie**: Kluczowa zmiana — Guardiola opuścił City, prawdopodobnie zastąpi go Maresca. Brak aktualnych informacji o kontuzjach/zawieszeniach na sierpień 2026 (zbyt odległy termin, okres przerwy letniej i okienka transferowego — składy mogą się jeszcze mocno zmienić).
- **Inne czynniki**: Mecz na neutralnym stadionie (Cardiff), tradycyjnie towarzyski charakter Community Shield — drużyny często rotują skład, dają szanse rezerwowym i nowym transferom, intensywność niższa niż w meczu ligowym o punkty.

## Model bazowy (oczekiwane gole)

Obliczenia oparte na pełnych statystykach sezonu 2025/26 (38 meczów):
- Średnia ligowa: gospodarze 1,53 gola/mecz, goście 1,22 gola/mecz (średnia ogólna ~1,385)
- Arsenal: siła ataku = (71/38) / 1,385 ≈ 1,36; siła obrony = (27/38) / 1,385 ≈ 0,52
- Man City: siła ataku = (69/38) / 1,385 ≈ 1,32; siła obrony = (32/38) / 1,385 ≈ 0,61
- Surowe λ (Arsenal jako "gospodarz"): λ_Arsenal = 1,36 × 0,61 × 1,53 ≈ 1,27; λ_City = 1,32 × 0,52 × 1,22 ≈ 0,83

**Korekty jakościowe:**
1. Boisko neutralne (Cardiff) — Arsenal traci część "bonusu gospodarza" wynikającego z atmosfery Emirates, City odzyskuje trochę (efekt: λ_Arsenal w dół, λ_City w górę).
2. Charakter Community Shield (towarzyski, rotacje, nowy trener City) — obniża pewność predykcji w obie strony i lekko spłaszcza różnicę między drużynami w porównaniu do "czystego" modelu sezonowego.
3. Brak aktualnych danych o kadrze na sierpień 2026 — nie uwzględniono ewentualnych transferów letnich, które mogą znacząco zmienić siłę obu zespołów.

Po korektach przyjęto:
- **λ(Arsenal) = 1,40**
- **λ(Manchester City) = 1,20**

To wciąż lekka przewaga Arsenalu (mistrz, najlepsza defensywa w Europie), ale różnica jest mniejsza niż sugerowałyby surowe liczby sezonowe — głównie ze względu na neutralny charakter meczu i niepewność związaną ze zmianą trenera City.

## Prawdopodobieństwa

### Wynik meczu (1X2)
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Arsenal wygrywa | 41,5% | 2,41 |
| Remis | 26,2% | 3,81 |
| Manchester City wygrywa | 32,2% | 3,11 |

*Uzasadnienie: Arsenal jest faworytem dzięki znacznie lepszej defensywie i tytułowi mistrza Anglii, ale przewaga jest umiarkowana — neutralne boisko i nieznana forma City pod nowym trenerem zawężają różnicę względem typowego meczu na Emirates.*

### Najbardziej prawdopodobne wyniki
| Wynik | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| 1-1 | 12,5% | 8,01 |
| 1-0 | 10,4% | 9,62 |
| 0-1 | 8,9% | 11,22 |
| 2-1 | 8,7% | 11,45 |
| 1-2 | 7,5% | 13,36 |
| 0-0 | 7,4% | 13,46 |

### Bramki
| Rynek | Prawdopodobieństwo | Kurs uczciwy |
|---|---|---|
| Over 1.5 | 73,3% | 1,36 |
| Over 2.5 | 48,2% | 2,08 |
| Over 3.5 | 26,4% | 3,79 |
| BTTS – Tak | 52,6% | 1,90 |
| BTTS – Nie | 47,4% | 2,11 |

*Uzasadnienie: Obie drużyny mają w składzie napastników zdolnych strzelać w każdym meczu (Haaland po stronie City, ofensywa Arsenalu wzmocniona skutecznością ze stałych fragmentów gry), więc BTTS jest bliski 50/50. Mecz lekko poniżej granicy 2,5 gola w ujęciu modelowym, ale w meczach towarzyskich/Community Shield liczba bramek bywa wyższa niż w lidze ze względu na luźniejszą grę defensywną — warto o tym pamiętać przy interpretacji.*

### Rożne
- Arsenal: ~4,7 (na podstawie 5,68 rożnych zdobytych/mecz w sezonie PL i ~3,66 rożnych oddawanych przez City/mecz — średnia tych dwóch wartości)
- Manchester City: ~3,9 (na podstawie 6,42 rożnych zdobytych/mecz przez City i 3,32 rożnych oddawanych przez Arsenal/mecz)
- Łącznie: zakres ok. 6-12, średnio ~8,5-8,6
- Over/Under:
  - Over 8.5: ~49,1% (kurs uczciwy 2,04) / Under 8.5: ~50,9% (1,96)
  - Over 9.5: ~36,0% (2,78) / Under 9.5: ~64,0% (1,56)
  - Over 10.5: ~24,8% (4,04) / Under 10.5: ~75,2% (1,33)

*Arsenal jest wyraźnie bardziej "rożnogenną" drużyną (prawie 6 rożnych/mecz w lidze, najwięcej dzięki dominacji w grze pozycyjnej i licznym wrzutkom), podczas gdy City rzadziej zdobywa rożne (3,7/mecz). To jednak dane z meczów ligowych pod Guardiolą — przy nowym trenerze i towarzyskim charakterze meczu styl gry City może się różnić, co dodaje niepewności do tego oszacowania.*

### Strzały i strzały celne
- Arsenal: ~14,5 strzałów/mecz (sezon PL), w tym ~4,9 celnych/mecz
- Manchester City: ~15,7 strzałów/mecz, w tym ~5,5 celnych/mecz
- Łącznie szacunkowo: ~26-32 strzałów, ~9-11 celnych
- Komentarz: City miało w sezonie 2025/26 nieco wyższą objętość strzałów (15,7 vs 14,5) i wyższą skuteczność celności (~35% trafień na bramkę vs ~34% u Arsenalu), napędzaną głównie formą Haalanda (25 goli ligowych). Arsenal kompensuje to świetną defensywą, więc mimo że City może oddawać więcej strzałów, Arsenal skutecznie ogranicza sytuacje bramkowe rywali w typowym meczu sezonowym — w towarzyskim meczu ta dyscyplina defensywna może być jednak luźniejsza.

### Faule i kartki
Brak wiarygodnych, aktualnych danych na temat fauli i kartek dla obu drużyn pod kątem konkretnie tego meczu (sierpień 2026) — nie udało się znaleźć sezonowych statystyk fauli/żółtych kartek per drużyna w przeszukanych źródłach, a dodatkowo Community Shield to mecz towarzyski, gdzie liczba fauli/kartek bywa zwykle niższa niż w meczu ligowym o stawkę. Z tego, co wiadomo: Arsenal w sezonie 2025/26 jako jedyna drużyna w historii PL zakończyła sezon bez czerwonej kartki i bez rzutu karnego dla rywali — sugeruje to zdyscyplinowaną, niskoryzykowną defensywę. Nie podaję konkretnych liczb fauli/kartek, by uniknąć fałszywej precyzji.

### Inne istotne statystyki (opcjonalnie)
- Statystyki posiadania piłki i spalonych nie zostały zebrane dla tego raportu — dla meczu towarzyskiego o niskiej stawce nie wnoszą istotnej wartości predykcyjnej w porównaniu do niepewności związanej ze zmianą trenera City i nieznanymi składami wyjściowymi.

## Podsumowanie

Arsenal wchodzi w to starcie jako świeżo upieczony mistrz Anglii z najlepszą defensywą w Europie, co daje mu lekką przewagę w modelu (41,5% vs 32,2% dla City, 26,2% remis) — ale przewaga jest wyraźnie mniejsza niż mogłaby sugerować różnica w tabeli ligowej (85 vs 78 pkt), głównie ze względu na neutralne boisko i fakt, że to mecz towarzyski poprzedzający sezon. Największą niewiadomą jest debiut nowego trenera City (prawdopodobnie Enzo Maresca po odejściu Guardioli) — żadna statystyka z minionego sezonu nie odda stylu gry, jaki City zaprezentuje pod nowym sztabem, więc warto traktować te liczby jako punkt wyjścia, a nie pewnik. Pod względem rożnych Arsenal ma wyraźną przewagę liczbową (5,68 vs 3,7 zdobywanych/mecz w sezonie), co przekłada się na oczekiwaną przewagę ~4,7 do ~3,9 w tym meczu, choć łączna liczba (~8,5) oscyluje blisko typowych linii bukmacherskich.

---
*Analiza ma charakter informacyjny i statystyczny, nie stanowi porady finansowej ani zachęty do zakładów. Graj odpowiedzialnie.*

## Meta note (for evaluation)

Największą trudnością było to, że na dzień 11.06.2026 sezon Premier League 2025/26 jest już zakończony (Arsenal mistrzem), a kolejny mecz ligowy Arsenal–Man City odbędzie się dopiero w sezonie 2026/27, którego terminarz jeszcze nie jest opublikowany — więc "najbliższy mecz" w sensie ścisłym (Premier League) obecnie nie istnieje. Zdecydowałem się potraktować jako "najbliższy mecz" zaplanowany FA Community Shield (16.08.2026, Cardiff) jako najbardziej zbliżone i jasno zakomunikowane rozwiązanie, wyraźnie zaznaczając tę różnicę w raporcie. Dodatkowym utrudnieniem był brak danych o fauli/kartkach dla obu drużyn oraz odejście Guardioli z City (zastąpienie przez prawdopodobnie Enzo Marescę) tuż przed tym meczem, co wprowadza dużą niepewność niezawartą w statystykach sezonowych. Część znalezionych danych liczbowych (np. punkty/bilans bramek City) była wzajemnie sprzeczna w różnych źródłach — przyjąłem dane z pełnego sezonu (38 meczów) jako bazę do obliczeń.
