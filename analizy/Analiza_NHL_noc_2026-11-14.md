# Analiza NHL, noc 13/14.11.2026 (odświeżona wersja ok. 22:45 CET)

Skill: nhl-analyst. Punkt wyjścia: `Analiza_NHL_2026-11-13.md` (09:18). Odświeżono ok. 22:45 CET: ESPN scoreboard (status bramkarzy, kursy DraftKings), Superbet (kursy, `superbet_event_odds`), WebSearch (Inside the Rink 13.11, Vancouver Hockey Daily, Yahoo, DK Network). BettingPros: brak klucza, nie użyty. xG/CF% niedostępne, więc λ oparte na golach, strzałach i SV%. Skład może się jeszcze zmienić do pierwszego buliona.

Rozmiar próby mały (19-20 meczów): λ zregresowane do średniej ligi (~3,17 gola na drużynę).

## Lista zmian względem poprzedniej wersji

| Co | Było | Jest |
|---|---|---|
| Garand (NYR) | Expected | **Confirmed** (ESPN) |
| Meriläinen (VAN) | Expected | nadal **Expected** (ESPN, Vancouver Hockey Daily: Demko na IR); Lankinen jako ryzyko |
| Hill (VGK) | Expected | **Confirmed** (ESPN) |
| Saros (NSH) | Expected | **Confirmed** (ESPN) |
| Canucks skład | brak danych | Chytil wraca do składu (+0,05 gola VAN), Willander DTD, MacEachern IR |
| Rangers skład | brak danych | poza grą: Smits, Durzi, Veleno, Sykora (głębia, wpływ pomijalny); Shesterkin do końca sezonu; Korpisalo wrócił po infekcji stopy (rezerwa) |
| VGK skład | brak danych | Hanifin (obrońca) out do ok. 24.11: λ NSH +0,05 |
| NSH skład | brak danych | Marchessault DTD (oczekiwany do gry), Trudeau out |
| NYR-VAN λ | 2,65 - 3,65 (6,3) | **2,70 - 3,60** (6,3): Chytil wraca, Garand potwierdzony (neutralny) |
| NYR-VAN p Rangers ML | 65,6% | **64,1%** (fair 1,56) |
| NYR-VAN kursy | Superbet 1,42/2,77, DK -225/+185 | bez zmian; DK total 6,5 otwarcie O +110 / U -130, teraz **O -105 / U -115** (ruch w stronę Over) |
| NSH-VGK λ | 3,15 - 2,55 (5,7) | **3,15 - 2,70** (5,85): Hanifin out, Saros potwierdzony (rynek po nim przesunął się w stronę NSH) |
| NSH-VGK p VGK ML | 60,0% | **57,4%** (fair 1,74) |
| NSH-VGK kursy | Superbet VGK 1,51 / NSH 2,52 | Superbet **VGK 1,58 / NSH 2,35**; DK -192 (otwarcie) do **-162 / +136** |
| NSH-VGK total (DK) | w poprzedniej wersji opisany jako 5,5 | poprawka: DK linia to **6,5 (O +114 / U -135)**, otwarcie O +105 / U -125; Superbet 5,5: O 1,70 / U 2,12; 6,5: O 2,10 / U 1,71 |
| NSH-VGK Under 6,5 | p 62,5%, EV +6% | **p 60% z modelu, po korekcie do rynku 57%**: brak przewagi (EV od -2,5% do +2,6%) |
| Puck line NSH +1,5 | EV +6% (DK -162) | DK -180: **EV ok. +5%** (p 67,4%); nadal tylko kurs DK |

---

## 1. Rangers @ Canucks (14.11, 03:00 PL; 13.11, 18:00 PT, Rogers Arena; Superbet 15587063)

**Typ:** Rangers wygrywają (moneyline z dogrywką) | **p:** 64,1% | **Fair odds:** 1,56 | **Pewność:** średnia (Garand potwierdzony, Meriläinen oczekiwany); brak przewagi nad rynkiem

### Rynki (λ: Canucks 2,70, Rangers 3,60, łącznie 6,3)
| Rynek | p | fair | Kurs rynkowy | EV | Pewność |
|---|---|---|---|---|---|
| Rangers ML (z OT/karnymi) | 64,1% | 1,56 | Superbet 1,42; DK -225 | -9,0% | średnia |
| Canucks ML (z OT/karnymi) | 35,9% | 2,79 | Superbet 2,77; DK +185 | -0,5% | średnia |
| 60' 1 / X / 2 | 28,6 / 15,3 / 56,1% | 3,50 / 6,53 / 1,78 | Superbet 3,80 / 4,25 / 1,70 | 2: -4,6% | średnia (remis realnie ~21-23%, fair ~4,5) |
| Puck line Rangers -1,5 | 39,9% | 2,51 | DK +114 (2,14) | -14,6% | średnia |
| Puck line Canucks +1,5 | 60,1% | 1,66 | DK -135 (1,74) | +4,6% (kurs DK) | średnia/niska (fair >1,15) |
| Total 5,5 Over / Under | 60,1 / 39,9% | 1,66 / 2,51 | Superbet O 1,59 / U 2,30 | O -4,4%, U -8% | średnia |
| Total 6,5 Over / Under | 47,2 / 52,8% | 2,12 / 1,89 | Superbet O 1,95 / U 1,85; DK O -105 / U -115 | O -8%, U -2,3% | średnia |
| Total 7,5 Over / Under | 29,8 / 70,2% | 3,35 / 1,42 | Superbet O 3,15 / U 1,33 | U -6,6% | średnia |

Najlepszy rynek meczu (z dogrywką): Canucks +1,5 po kursie DK (EV +4,6%), ale to rynek z kursu spoza Superbet i na drużynę z 6 porażkami z rzędu; Superbet nie pokazał puck line w pobranej liście. Dla Rangers ML brak value (marża Superbet ~6%). Nie ma mocnego typu samodzielnego; Rangers ML tylko jako noga kuponu.

**Statystyki drużyn (NHL.com/ESPN):**
- Canucks 3-16-1 (32. miejsce), GF 56 / GA 90, u siebie 1-8-0, seria 6 porażek, SV% drużyny .858 (32. w lidze).
- Rangers 11-8-1, GF 59 / GA 56, wyjazd 3-6-1; SV% .906 (ESPN, 5. w lidze), mało strzałów przeciwko (~25/mecz).

**H2H:** brak danych z sezonu, waga niska.

**Bramkarze (sprawdzono ok. 22:45 CET):**
- Rangers: Dylan Garand **potwierdzony** (ESPN), 14 GP, GAA 2,48, SV% .905. Korpisalo wrócił po infekcji stopy, ale start Garanda jest już ogłoszony. Shesterkin out do końca sezonu.
- Canucks: Leevi Meriläinen oczekiwany (ESPN Expected; Demko na IR hip), SV% .889, GAA 3,41. Alternatywa Lankinen (SV% .808): wtedy λ Rangers +0,4, p Rangers ok. 72%.

**Informacje medialne:** Chytil wraca do składu Canucks (Jeff Paterson, Vancouver Hockey Daily), Willander DTD, MacEachern IR. Rangers bez Smitsa, Durziego, Veleno, Sykory (głębia). Brak back-to-back po obu stronach; Rangers trzeci mecz wyjazdowej serii (EDM, CGY, VAN).

**Oczekiwane gole:** Canucks 2,70 - Rangers 3,60 (łącznie 6,3). Rynek: total 6,5.

**Porównanie z rynkiem:** model Rangers 64,1% vs rynek bez marży 66,1% (Superbet) / 66,4% (DK): różnica 2 pp, zgodne. Brak sygnału, którego rynek nie widzi.

**Ryzyka:** (1) Lankinen zamiast Meriläinena (korzyść Rangers); (2) wysoka losowość, faworyt max ~65-68%; (3) dogrywka/karne ~15%; (4) zmęczenie Rangers trzecim wyjazdem; (5) pusta bramka podbija różnice i totale.

### Rynki zawodnika (niska pewność; skład Canucks niepotwierdzony, kombinacje z wynikiem w Superbet)
Średnie z NHL.com (20 GP): strzały Dorofeyev 3,0/mecz, Lafrenière 2,15, Zibanejad 1,85. Superbet wycenia je tylko w kombinacji z wygraną drużyny.
| Rynek | p | fair | Superbet | Uwagi |
|---|---|---|---|---|
| Dorofeyev Over 3,5 SOG (singiel) | 35,2% | 2,84 | tylko kombinacja z Rangers win 3,75 | kombinacja szac. 25-28%, fair ok. 3,7-4,0 vs 3,75: brak przewagi |
| Lafrenière strzelec gola (Over 0,5) | 28,1% | 3,56 | brak singla | brak typu |
| Zibanejad Over 0,5 asyst + Rangers win | ok. 33% | ok. 3,0 | 2,62 | EV ujemne (ok. -14%) |
| Obrony bramkarza | nie wyceniam | | brak linii | Meriläinen niepotwierdzony; po potwierdzeniu: oczekiwane strzały VAN ~ 28-29 na Garanda, Rangers strzelają średnio ~29, ale linii brak |

Typu zawodnika na kupon: brak (brak singli do porównania, kombinacje z ujemnym EV).

---

## 2. Predators @ Golden Knights (14.11, 04:00 PL; 13.11, 19:00 PT, T-Mobile Arena; Superbet 15587103)

**Typ:** Golden Knights wygrywają (moneyline z dogrywką) | **p:** 57,4% | **Fair odds:** 1,74 | **Pewność:** średnia (obaj bramkarze potwierdzeni, ale wyrównane siły); brak przewagi nad rynkiem, to "lekki faworyt"

### Rynki (λ: Golden Knights 3,15, Predators 2,70, łącznie 5,85)
| Rynek | p | fair | Kurs rynkowy | EV | Pewność |
|---|---|---|---|---|---|
| VGK ML (z OT/karnymi) | 57,4% | 1,74 | Superbet 1,58; DK -162 | -9,3% | średnia |
| NSH ML (z OT/karnymi) | 42,6% | 2,35 | Superbet 2,35; DK +136 | 0% (DK +136: +0,5%) | średnia, brak przewagi |
| 60' 1 / X / 2 | 48,9 / 16,6 / 34,5% | 2,04 / 6,01 / 2,90 | Superbet 1,97 / 4,10 / 3,05 | 1: -3,7%, 2: +5,2% (ale remis w modelu zaniżony, realnie p 2 ok. 31-32%) | niska/średnia |
| Puck line VGK -1,5 | 32,6% | 3,07 | DK +150 (2,50) | -18,5% | średnia |
| Puck line NSH +1,5 | 67,4% | 1,48 | DK -180 (1,56) | +4,9% (kurs DK) | średnia (fair >1,15) |
| Total 5,5 Over / Under | 53,0 / 47,0% | 1,89 / 2,13 | Superbet O 1,70 / U 2,12 | O -9,9%, U -0,4% | średnia/niska |
| Total 6,5 Over / Under | 40,0 / 60,0% | 2,50 / 1,67 | Superbet O 2,10 / U 1,71; DK O +114 / U -135 | U +2,6% (p 60%), po korekcie do rynku (57%) -2,5% | niska |
| Total 4,5 | Over ok. 83% | fair ok. 1,2 | Superbet O 1,22 | pomijam (fair <= 1,2) | |

Najlepszy rynek meczu: Under 6,5 goli (z dogrywką), ale przewaga wynika z mojego λ poniżej rynku (5,85 vs ok. 6,0-6,1; rynek bez marży Under 6,5 Superbet 55%, DK 57%). Różnica 5 pp bez konkretnego sygnału, więc zgodnie z zasadą "nie schodź pod rynek >3 pp w Under" liczę p ok. 57%: EV -2,5%, brak typu. Puck line NSH +1,5 ma EV około +5% tylko po kursie DK (-180), Superbet w pobranej liście go nie miał.

**Statystyki drużyn (NHL.com/ESPN):**
- Golden Knights 13-5-2, GF 68-69 (3,4) / GA 54, u siebie 7-3-0, seria 4 zwycięstw (5-3 UTA 11.11), SV% .899.
- Predators 10-4-5, GF 58-59 / GA 53, wyjazd 4-1-3, seria 6 zwycięstw (4-2 ANA 11.11), 5 porażek po OT/karnych, SV% .909 (4. w lidze).
- xG i CF% niedostępne; wnioski z goli.

**H2H:** brak wiarygodnych danych z sezonu; waga niska (ostatnie spotkanie 13.10.2026, wg NHL.com: VGK 5-2-0 vs NSH 2-1-2 w momencie zapowiedzi, wynik niezweryfikowany).

**Bramkarze (sprawdzono ok. 22:45 CET):**
- Golden Knights: Adin Hill **potwierdzony** (ESPN), SV% .903; rezerwowy Carter Hart.
- Predators: Juuse Saros **potwierdzony** (ESPN), SV% .918 (NHL.com), rezerwowy Justus Annunen.
- Wpływ w λ: Saros +0,1 gola obrony dla NSH (już wliczone), Hill neutralny.

**Informacje medialne:** Hanifin (VGK, obrońca) out do ok. 24.11 (Yahoo/Inside the Rink): λ NSH +0,05. Predators: Marchessault DTD (oczekiwany do gry), Trudeau out. Olofsson (VGK) według Inside the Rink w składzie, status niepotwierdzony. Linie: VGK Connelly - Eichel - Stone; NSH Stamkos - O'Reilly - Bourque, Forsberg w drugiej linii. Oba zespoły po 1 dniu przerwy (mecze 11.11), brak back-to-back.

**Oczekiwane gole:** Golden Knights 3,15 - Predators 2,70 (łącznie 5,85). Rynek: total ok. 6,0-6,1.

**Porównanie z rynkiem:** p VGK 57,4% vs rynek bez marży 59,8% (Superbet) / 59,3% (DK): różnica 2 pp, zgodne. Rynek przesunął się w stronę NSH (DK -192 do -162), czyli potwierdzenie Saros jest w cenie.

**Ryzyka:** (1) wyrównane siły, p 57% to lekki faworyt; (2) dogrywka/karne ~17% meczów (NSH 5 porażek po OT); (3) przy Marchessault poza składem NSH λ -0,05; (4) Over 6,5 przesuwa się w DK (otwarcie U -125 do U -135 czyli rynek ruszył w stronę Under, uwaga na sprzeczne sygnały: Under w DK mocniej wyceniony niż w Superbet).

### Rynki zawodnika (niska pewność; Hill i Saros potwierdzeni, linii strzałów brak w singlach)
| Rynek | p | fair | Superbet | Uwagi |
|---|---|---|---|---|
| Eichel Over 3,5 SOG (singiel) | ok. 39% (śr. 3,2, bez drugiego źródła) | ok. 2,5 | tylko kombinacja z VGK win 4,60 | kombinacja szac. 25-27%, fair ok. 3,8-4,0 vs 4,60: formalnie EV dodatnie (ok. +15-20%), ale średnia strzałów z jednego źródła, więc brak typu |
| Forsberg Over 3,5 SOG + NSH win | ok. 40% singiel (śr. 3,4) | | 5,85 | kombinacja szac. 17-19%, fair ok. 5,4-5,9: brak przewagi |
| Marner Over 0,5 asyst + VGK win | ok. 55% asysta * korelacja = ok. 34% | ok. 2,9 | 2,77 | EV ok. -4%, brak typu |
| Obrony Saros (VGK strzela ~29-30) | wyc. średnia 26-27 | Over 24,5: 58% (1,71), Under 26,5: 55% (1,81) | brak linii | po potwierdzeniu Saros typ możliwy, ale bez linii bukmachera nie wyceniam kursu |
| Obrony Hill (NSH strzela ~27-28) | wyc. średnia 24 | Over 22,5: 59% (1,70), Under 24,5: 55% (1,80) | brak linii | jw. |

Typ zawodnika na kupon: brak (wymóg dwóch niezależnych źródeł niespełniony dla strzałów, brak linii obron).

---

## Ranking i kandydaci na kupon (fair > 1,15; wszystko po potwierdzonych Garand/Hill/Saros, Meriläinen oczekiwany)

| Mecz | Rynek | p | fair | Kurs | EV | Pewność | Zależy od |
|---|---|---|---|---|---|---|---|
| NSH-VGK | Puck line NSH +1,5 | 67,4% | 1,48 | DK 1,56 (Superbet brak) | +4,9% | średnia | kurs spoza Superbet |
| NYR-VAN | Puck line VAN +1,5 | 60,1% | 1,66 | DK 1,74 (Superbet brak) | +4,6% | średnia/niska | Meriläinen, kurs spoza Superbet |
| NYR-VAN | Rangers ML (z OT) | 64,1% | 1,56 | Superbet 1,42 | -9,0% | średnia | Meriläinen/Lankinen |
| NSH-VGK | VGK ML (z OT) | 57,4% | 1,74 | Superbet 1,58 | -9,3% | średnia | rotacja/Marchessault |
| NSH-VGK | Under 6,5 (z OT) | 57-60% | 1,67-1,75 | Superbet 1,71 | -2,5% do +2,6% | niska | λ poniżej rynku |
| NYR-VAN | Under 6,5 (z OT) | 52,8% | 1,89 | Superbet 1,85 | -2,3% | średnia | Meriläinen |

Według domyślnych progów kuponu (p > 50%, EV > 0, kurs łączny 1,5-2,5) nie ma kandydata z Superbet z dodatnim EV; dodatnie EV mają tylko puck line +1,5 po kursach DK (nie Superbet). Kupon z dwóch nóg DK (VAN +1,5 i NSH +1,5): p ok. 40% (korelacja niska), kurs 1,74 x 1,56 = 2,71, powyżej progu 2,5 - nie spełnia. Zastrzeżenie: marże Superbet są wyższe niż DK, więc przewagi nie da się zrealizować po Superbet.

Wszystko to oszacowania probabilistyczne, nie gwarancje; skład i bramkarze (zwłaszcza Meriläinen) mogą się zmienić do rozpoczęcia meczu (sprawdzono ok. 22:45 CET, 13.11.2026).
