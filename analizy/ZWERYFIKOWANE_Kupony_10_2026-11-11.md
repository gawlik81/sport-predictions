# Kupony noc NBA+NHL 11→12.11.2026 (czas polski)

**Okres:** noc NBA i NHL, 11.11 (wieczór ET) → 12.11.2026 (01:00-04:00 PL). Tylko NBA i NHL (10 + 6 meczów), reszta sportów pominięta na życzenie.
**Kursy:** Betclic.pl, pobrane 11.11 ok. 22:00-23:15 PL. gg397.bet nie sprawdzony (brak potwierdzenia drugim źródłem). Kursy mogą się zmienić do startu.
**Poziomy luzowania:** dopuszczone tylko 0-2 (wybór użytkownika).
**Analizy:** `analizy/Analiza_dnia_NBA_NHL_2026-11-11.md`.

## Wynik: 1 kupon (zamiast 10) + wariant alternatywny
Przy kursach Betclic prawie każda noga ma EV ujemne (p modeli = p rynku). Kupon z łącznym p > 50% i kursem 1,5-2,5 wymaga nóg o p ≥ 70%; z dostępnych kursów spełniają to tylko 3 nogi. Nie dobijam do 10 (zasada "nie fabrykuj typu").

## Pula nóg o p ≥ 70% (z kursem Betclic)
| Mecz | Rynek | p | Kurs Betclic | Fair | EV | Uwagi |
|---|---|---|---|---|---|---|
| Raptors - Celtics (01:00) | BOS +5,5 handicap (linia alternatywna) | 80% | 1,22 | 1,25 | -2,4% | p wyliczone z parametrów modelu analityka (średnia różnicy +5,0, SD 12,5), nie z raportu; BOS na B2B, George OUT |
| Flyers - Oilers (03:00) | EDM lub remis po 60' | 72% | 1,30 | 1,39 | -6,4% | p = 50% + 22% remisu z raportu; Vladar (PHI) niepotwierdzony |
| Spurs - Bulls (02:00) | SAS -7,5 handicap (alternatywna) | 70,5% | 1,28 | 1,42 | -9,8% | p z modelu (średnia +14,5, SD 13); ryzyko blowoutu i statusów Vassell/Wilson/Powell |
| Rockets - Warriors (03:30) | HOU ML | 65,5% | 1,36 | 1,53 | -10,9% | oba zespoły B2B |

## Kupony
### Kupon 1 (poziom 2: EV ujemne; p > 50%, kurs 1,5-2,5, 2 nogi > 1,2 spełnione)
| Godz. PL | Mecz | Typ | p | Kurs | EV | Źródło kursu |
|---|---|---|---|---|---|---|
| 01:00 (11.11 19:00 ET) | Raptors - Celtics | BOS +5,5 | 80% | 1,22 | -2,4% | Betclic |
| 03:00 (11.11 21:00 MT) | Oilers - Flyers | EDM lub remis (60') | 72% | 1,30 | -6,4% | Betclic |
Łączne p: 57,6% | Fair: 1,74 | Kurs: 1,59 | EV: -8,6% | Stawka: 0%.
Ryzyko: BOS na B2B i w składzie bez George'a (Brown niewyjaśniony), Vladar (PHI) niepotwierdzony. Pewność niska.

### Wariant alternatywny do kuponu 1 (te same nogi nie mogą grać razem, więc to albo kupon 1, albo kupony 1A+1B)
- **1A** (poziom 2): BOS +5,5 (80%, 1,22) + HOU ML (65,5%, 1,36). p 52,4%, kurs 1,66, EV -13,1%, stawka 0%.
- **1B** (poziom 2): SAS -7,5 (70,5%, 1,28) + EDM lub remis 60' (72%, 1,30). p 50,8%, kurs 1,66, EV -15,5%, stawka 0%.

## Czego nie wycenione
- Pozostałe spready i totale NBA: strony Betclic pokazują tylko linie alternatywne (main line niewidoczna w tekście), więc dla 8 z 10 meczów NBA nie mam kursów handicap/total; dla Raptors-Celtics i Spurs-Bulls wzięto linie alternatywne.
- Puck line NHL: Betclic nie wystawia go jako osobnego rynku na stronie meczu. Rynki zawodnika: brak wyceny w analizach.
- Poniżej progu p > 50% (poziom -2/-1, wymaga zgody): nogi z EV > 0 przy kursach Betclic: SJS-PIT Under 5,5 (p 42,2%, kurs 2,65, EV +11,8%), SAS Under 124,5 pkt (p 50%, kurs 2,18, EV +9%), CGY wygra w 60' (p 38,4%, kurs 2,75, EV +5,6%), NSH wygra w 60' (p 38,9%, 2,70, +5,0%), SJS wygra w 60' (p 37,9%, 2,70, +2,3%), UTA Under 2,5 gola (p 45%, 2,27, +2,2%). Wszystkie "przewaga niepotwierdzona" (p modeli zakotwiczone w rynku, Poisson zaniża remisy po 60'), bez potwierdzonych bramkarzy.

## Ostrzeżenia
- Założenie niezależności meczów; kursy mogą się zmienić do startu; składy NBA i bramkarze NHL do potwierdzenia przed meczem (injury report ok. 90 min przed).
- Wszystkie p to oszacowania, nie gwarancje; przy EV ujemnym stawka 0% (brak przewagi nad rynkiem).

## Dodatek na życzenie: kupon tylko NBA, kurs min 3,0 (zapytanie użytkownika nadpisuje progi domyślne: p > 50% i kurs < 2,5 nie obowiązują)
Kursy Betclic z 11.11 ok. 22:30 PL.
- **Kupon N1 (poziom spoza 0-2, wg zapytania):** SAS pkt Under 124,5 (Bulls - Spurs, 02:00 PL; p 50%, kurs 2,18) + DEN ML (Grizzlies - Nuggets, 02:00 PL; p 62%, kurs 1,55). Łączne p 31,0%, kurs 3,38, fair 3,23, EV +4,7% (przy p nogi SAS ściągniętym do rynku + 5 pp: p 29,4%, EV -0,5%, stawka 0%). Noga SAS Under 124,5 oznaczona "przewaga niepotwierdzona" (model niżej od linii o ok. 2 pkt na bazie ryzyka blowoutu); Jokić/Stewart do potwierdzenia.
- **Kupon N2 (bez przewagi, wyższe p):** OKC ML (1,79) + TOR pkt Over 104,5 (1,79). Łączne p 29,6%, kurs 3,20, EV -5,2%, stawka 0%.
