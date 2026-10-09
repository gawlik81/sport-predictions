# TOP 10 predykcji 07-08.10.2026 (analiza sportowa + kursy GGBET)

Wersja oparta na analizie sportowej (statystyki, H2H, informacje medialne, modele `tennis_model.py` / `series.py` / `poisson.py`), kursy GGBET tylko do wyliczenia EV. Poprzednia wersja (same de-vigowane kursy) została zastąpiona; zawierała błędne H2H Hurkacza (jest 2-0, nie 1-0).

Uwaga o danych: p_serve w tenisie oszacowane z rankingu/formy sezonu (brak pełnych statystyk serwisu), więc p meczu to mieszanka modelu, niezależnych modeli (Tennis Tonic, Stats Insider, Dimers) i rynku. Warunki w Szanghaju 2026 (upał, tempo kortu) niepotwierdzone - w 2025 było bardzo wolno i duszno (CPI 32,8), co sprzyja returnującym i obniża pewność dużych serwerów.

## Ranking

| # | Typ | Wydarzenie / czas | p | Fair | Kurs | EV | Pewność |
|---|-----|-------------------|----|------|------|-----|---------|
| 1 | Team Spirit wygra | CS2 EPL S24, decydujący mecz Swiss vs M80 (bo3), dziś 19:45 | 78% | 1.28 | 1.11 | -13% | średnia |
| 2 | Hubert Hurkacz wygra | ATP Szanghaj R1 vs Duckworth, jutro ok. 07:30-08:30 | 71% | 1.41 | 1.43 | +1,5% | średnia |
| 3 | Nuno Borges wygra | ATP Szanghaj R1 vs Diaz Acosta, jutro 06:00 | 69% | 1.45 | 1.28 | -12% | niska |
| 4 | Zizou Bergs wygra | ATP Szanghaj R1 vs Kopriva, jutro 10:30 | 68% | 1.47 | 1.34 | -9% | średnia |
| 5 | Cameron Norrie wygra | ATP Szanghaj R1 vs Svrcina, jutro | 68% | 1.47 | 1.52 | +3% | średnia |
| 6 | Matteo Arnaldi wygra | ATP Szanghaj R1 vs Tomic, jutro 07:30 | 66% | 1.52 | 1.38 | -9% | niska |
| 7 | Tallon Griekspoor wygra | ATP Szanghaj R1 vs Kotov, jutro 06:00 | 66% | 1.52 | 1.40 | -8% | średnia |
| 8 | Ilia Simakin wygra | ATP Szanghaj R1 vs Ugo Carabelli, jutro 06:00 | 62% | 1.61 | 1.43 | -11% | niska |
| 9 | Jaume Munar wygra | ATP Szanghaj R1 vs Brooksby, jutro 06:00 | 60% | 1.67 | 1.48 | -11% | niska |
| 10 | Vitória BA wygra | Brasileirão 29. kolejka vs Chapecoense, 07.10 20:00 BRT (jutro 01:00 PL) | 55% | 1.82 | 1.57 | -14% | niska |

Tylko #2 i #5 są w okolicy fair (EV ≈ 0 lub lekko dodatnie, w granicach błędu szacunku). Pozostałe typy są najbardziej prawdopodobnymi, ale przepłaconymi; to nie value bety.

## Analizy

### Team Spirit - M80 (CS2, ESL Pro League S24, ostatnia runda Swiss, bo3, 07.10 19:45)
- **Kontekst:** Spirit (nr 1 HLTV/VRS, zwycięzca EWC 2026 i BLAST Open Porto) przegrał w Swiss z MOUZ (pierwsza porażka w fazie Swiss od 668 dni) i z 1win - to mecz o awans. M80 (27. w rankingu, kwalifikacja z ECL S51, 0-2 z MOUZ na starcie, Mirage 9-13) też gra o życie. Źródła: HLTV (matchups, newsy), dust2.us.
- **Liczby:** p mapy Spirit ok. 0,64 (korekta za dwie porażki z rzędu i bo3 z pickiem M80 w dół z ok. 0,70) → seria 70-78%; przyjęto 78%. Rynek 85% - różnica >10 pp, brak informacji o stand-inie/problemie, ale dwie świeże porażki to realny sygnał.
- **Ryzyka:** forma Spirit (dwie wpadki), mapa wybrana przez M80, bo3 losowe.
- **Rynek:** kurs 1.11 vs fair 1.28 → niedoszacowanie ryzyka przez rynek lub moja ostrożność; EV ujemne.

### Hurkacz - Duckworth (ATP Szanghaj R1, hard)
- Hurkacz (34. ATP, 32-21 w 2026, 20-11 na hardzie, 7 z 9 ostatnich, mistrz Szanghaju 2023) vs Duckworth (64., 3 porażki z rzędu, 34 lata). H2H 2-0 dla Hurkacza (nie grali na hardzie). Model (p_serve 0,69/0,635): 74,8%; niezależne modele ok. 74%; rynek po marży 65%. Przyjęto 71% (wolny kort, historia kontuzji Hurkacza, brak informacji o zdrowiu). Źródła: Tennis Tonic, Dimers, Stats Insider.

### Borges - Diaz Acosta
- Borges 51. ATP, ale 27-27 w sezonie (13-12 na hardzie), trzy porażki z rzędu (ostatnia 3-6 6-7 z Djokovicem w Pekinie, bez zgłoszonego urazu). Diaz Acosta 69., 49-19 głównie na Challengerach i glinie, tylko 4 mecze na hardzie w sezonie. Pierwszy mecz H2H. Model (0,635/0,62): 57,5%; niezależne modele 76%; rynek 73% → przyjęto 69%, pewność niska (zła forma Borgesa vs nieprzetestowany na hardzie rywal).

### Bergs - Kopriva
- Bergs ćwierćfinalista Szanghaju 2025, serwis przydatny w wolnych warunkach, ale 2 porażki z rzędu; Kopriva 9 porażek z rzędu z graczami top 100. H2H 1-1 (Challenger, nie na hardzie; ostatnio wygrał Kopriva po 3 setach). Model 62%; niezależny 71%; rynek 70% → 68%.

### Norrie - Svrcina
- Norrie (40. ATP, 20-17 w sezonie, 17-9 na hardzie, pokonał de Minaura w Montrealu) vs Svrcina (126., 20-11, ćwierćfinał Los Cabos). Pierwszy mecz H2H. Rynek ok. 62-64%; przyjęto 68% (forma na hardzie i doświadczenie w wolnych warunkach). Pewność średnia.

### Arnaldi - Tomic
- Arnaldi (38. ATP): półfinał RG 2026 (zakończony chorobą), tytuł Sardegna Open na mączce, ale **0-3 na hardzie w 2026** i przewlekła kontuzja stopy w tym sezonie. Tomic (ok. 171-185 ATP, 33 lata): wygrał Challenger w Lincoln (hard, lipiec), dobra forma w Los Cabos, pierwszy mecz M1000 od 2019. Sygnały ryzyka obniżyły p z ok. 77% do 66%; pewność niska.

### Griekspoor - Kotov
- Griekspoor 58. ATP, Kotov 187. (kwalifikant, po wygranych kwalifikacjach - ma rytm). H2H 3-2 dla Kotova, ale 1-0 Griekspoora na hardzie. Model 64,7%, niezależny 66,6% → 66%.

### Simakin - Ugo Carabelli
- Simakin 154. ATP, 45-17 w sezonie (głównie Challengery); Ugo Carabelli 21-24, 3-11 na hardzie, 4 porażki z rzędu. Brak H2H. Typ Tennis Tonic: Simakin w 3 setach (kursy 1.74/2.08). Przyjęto 62%.

### Munar - Brooksby
- Munar 49. ATP (17-15 w sezonie) grał półfinał w Tokio 5.10 (przegrał z Alcarazem) - krótka przerwa i podróż do Szanghaju (korekta w dół); Brooksby 102., 16-23. Model 55%, Stats Insider 62% → 60%.

### Vitória - Chapecoense (Brasileirão, 29. kolejka, Barradão)
- Vitória (6 kontuzjowanych: Baralhas, Camutanga, Dudu, Edu, Nathan Mendes, Ramon) vs Chapecoense (8 kontuzji, m.in. Bruno Tubarão, Franco Rossi, Heitor, Victor Caetano). λ 1,55 / 0,85 → 1: 53,8%, X: 25,6%, 2: 20,6%; przyjęto 55%. Ryzyko = remis ORAZ wygrana Chapecoense w równym stopniu. Rynek po marży 60,6%; wyższe od mojego, ale brak danych xG. Źródła: Gazeta Esportiva, VAVEL, A Tarde.

## Zestawy (slip.py)

Najlepszy układ to pojedyncze #2 i #5 (EV około 0). Akumulatory pogłębiają ujemne EV: np. #2 + #5 + #7 (p ≈ 0,71×0,68×0,66 = 32%) przy kursie ≈ 3,04 daje EV ≈ -3%.

## Odrzucone po analizie (brak wystarczających danych lub p zbyt niskie)

- K27 - Metizport (kwalifikacje Private Club 2): tier-3, brak wiarygodnych danych.
- Coquimbo - Cobreloa (Puchar Chile, rewanż, Coquimbo prowadzi 2-1 z pierwszego meczu): kurs 1.37 dotyczy 90 minut, a motywacja przy zaliczce nie została zbadana.
- Cerundolo - Mejia: Mejía wygrał turniej w Meksyku na hardzie (finał z Duckworthem), Cerundolo głównie glina → p ok. 58% przy kursie 1.47, EV ≈ -15%.
- Tsitsipas - Coppejans (1.06), Shelton - Altmaier (1.10): fair ≤ 1.15.
- Mecze Brasileirão bez kursów lub bez analizy (Palmeiras-Bahia, Santos-Flamengo, Internacional-Corinthians, Bragantino-Mirassol).
- Challenger Braga McDonald - Nijboer: brak danych.

To oszacowania probabilistyczne, nie gwarancje.

## Kupony (max 3 typy, p każdego typu >60%, kurs kuponu >1.5)

- **Kupon 1:** Hurkacz (1.43, p 71%) + Norrie (1.52, p 68%) - p 48,3%, kurs 2.17, fair 2.07, EV +4,9%.
- **Kupon 2:** Griekspoor (1.40, p 66%) + Bergs (1.34, p 68%) - p 44,9%, kurs 1.88, fair 2.23, EV -15,8%.

Typy się nie powtarzają ani nie wykluczają. Trzeci typ w kuponie 2 (Arnaldi) obniżał p do 29,6% i EV do -23%, więc go pominięto.
