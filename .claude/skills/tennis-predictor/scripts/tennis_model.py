#!/usr/bin/env python3
"""Hierarchical point -> game -> set -> match probability model for tennis.

Given the probability that each player wins a point on their own serve,
computes exact match-win probability, match score (sets) distribution,
total-games distribution and over/under, games handicap, and first-set
outcome -- via forward dynamic programming (exact enumeration), not
simulation.

This is the tennis analogue of the football skill's Poisson model: instead
of expected goals (lambda), the core input here is expected points won on
serve (p). The same "attack strength x defense strength x baseline" idea
from the football model carries over almost unchanged -- see SKILL.md
Krok 2 for how to turn serve/return stats into p_a_serve and p_b_serve
before calling this script.

Known simplifications (documented, not hidden -- correct these qualitatively
in the report, same as football's lambda corrections):
- Point-win probability is treated as constant through the whole match (no
  fatigue/momentum/pressure modeling).
- Tiebreak points use a single averaged point-win probability rather than
  alternating exact server-by-server probabilities point by point.
- Player A is assumed to serve first in every set. Real matches sometimes
  alternate who serves first between sets depending on the previous set's
  total games; the effect on match-level probabilities is a minor,
  second-order one.
- Only "tiebreak at 6-6" deciding sets are modeled via --final-set-tiebreak-to
  (e.g. 7 for a standard breaker, 10 for an Australian-Open-style match
  tiebreak). Wimbledon's "breaker at 12-12" rule is NOT modeled exactly --
  treat that case qualitatively with a wider uncertainty band instead of
  trusting this script's deciding-set output at face value.

Usage:
    python tennis_model.py --p-a-serve 0.64 --p-b-serve 0.61 --best-of 3
    python tennis_model.py --p-a-serve 0.68 --p-b-serve 0.60 --best-of 5 \
        --final-set-tiebreak-to 10 --game-lines 37.5,38.5,39.5
"""

import argparse
import json
import math
from collections import defaultdict


def race_win_prob(p: float, target: int) -> float:
    """Probability of winning a race to `target` points, win-by-2, i.i.d.
    point-win probability p. Generalizes the classic tennis game-win formula
    (target=4) to tiebreaks (target=7 or 10)."""
    if p <= 0:
        return 0.0
    if p >= 1:
        return 1.0
    total = 0.0
    for m in range(0, target - 1):
        total += math.comb(target - 1 + m, m) * p ** target * (1 - p) ** m
    p_tie = math.comb(2 * (target - 1), target - 1) * p ** (target - 1) * (1 - p) ** (target - 1)
    d = p ** 2 / (p ** 2 + (1 - p) ** 2)
    total += p_tie * d
    return total


def fair_odds(p: float):
    return round(1 / p, 2) if p and p > 0 else None


def set_score_distribution(p_a_serve, p_b_serve, tiebreak_to=7, server_first="A"):
    """Exact distribution over set outcomes as {(winner, games_a, games_b): prob}.

    games_a / games_b always mean "A's games" / "B's games" regardless of
    who won the set (e.g. a 4-6 loss for A is stored as ("B", 4, 6))."""
    p_game_a = race_win_prob(p_a_serve, 4)   # P(A wins a game A is serving)
    p_game_b = race_win_prob(p_b_serve, 4)   # P(B wins a game B is serving)
    p_tb_a = (p_a_serve + (1 - p_b_serve)) / 2  # avg point-win prob for A in a breaker

    state = {(0, 0): 1.0}
    results = defaultdict(float)

    for _ in range(12):  # 6-6 can only first appear after exactly 12 games
        next_state = defaultdict(float)
        for (i, j), prob in state.items():
            if prob == 0:
                continue
            game_idx = i + j
            a_serves = (game_idx % 2 == 0) if server_first == "A" else (game_idx % 2 == 1)
            p_a_wins_game = p_game_a if a_serves else (1 - p_game_b)

            for winner, ni, nj, p_step in (
                ("A", i + 1, j, p_a_wins_game),
                ("B", i, j + 1, 1 - p_a_wins_game),
            ):
                if p_step == 0:
                    continue
                mass = prob * p_step
                if ni == 6 and ni - nj >= 2:
                    results[("A", ni, nj)] += mass
                elif nj == 6 and nj - ni >= 2:
                    results[("B", ni, nj)] += mass
                elif ni == 7 and nj == 5:
                    results[("A", ni, nj)] += mass
                elif nj == 7 and ni == 5:
                    results[("B", ni, nj)] += mass
                else:
                    next_state[(ni, nj)] += mass
        state = next_state

    leftover = state.get((6, 6), 0.0)
    if leftover > 0:
        p_win_tb = race_win_prob(p_tb_a, tiebreak_to)
        results[("A", 7, 6)] += leftover * p_win_tb
        results[("B", 6, 7)] += leftover * (1 - p_win_tb)

    return results


def match_distribution(p_a_serve, p_b_serve, best_of=3, tiebreak_to=7,
                        final_set_tiebreak_to=None):
    if final_set_tiebreak_to is None:
        final_set_tiebreak_to = tiebreak_to
    sets_needed = best_of // 2 + 1

    regular_set = set_score_distribution(p_a_serve, p_b_serve, tiebreak_to, "A")
    decider_set = set_score_distribution(p_a_serve, p_b_serve, final_set_tiebreak_to, "A")

    active = {(0, 0, 0, 0): 1.0}  # (sets_a, sets_b, games_a, games_b)
    final = defaultdict(float)

    for _ in range(best_of):
        if not active:
            break
        next_active = defaultdict(float)
        for (sa, sb, ga, gb), prob in active.items():
            is_decider = (sa == sets_needed - 1 and sb == sets_needed - 1)
            outcomes = decider_set if is_decider else regular_set
            for (winner, sga, sgb), sp in outcomes.items():
                nsa = sa + (1 if winner == "A" else 0)
                nsb = sb + (1 if winner == "B" else 0)
                nga, ngb = ga + sga, gb + sgb
                mass = prob * sp
                if nsa == sets_needed or nsb == sets_needed:
                    final[(nsa, nsb, nga, ngb)] += mass
                else:
                    next_active[(nsa, nsb, nga, ngb)] += mass
        active = next_active

    return final, regular_set


def analyze(p_a_serve, p_b_serve, best_of, tiebreak_to, final_set_tiebreak_to,
            game_lines, handicap_lines, top_set_scores):
    final, first_set = match_distribution(p_a_serve, p_b_serve, best_of,
                                           tiebreak_to, final_set_tiebreak_to)

    match_win_a = sum(p for (sa, sb, ga, gb), p in final.items() if sa > sb)
    match_win_b = 1 - match_win_a

    match_score = defaultdict(float)
    total_games_dist = defaultdict(float)
    diff_dist = defaultdict(float)
    for (sa, sb, ga, gb), p in final.items():
        match_score[f"{sa}-{sb}"] += p
        total_games_dist[ga + gb] += p
        diff_dist[ga - gb] += p

    over_under = {}
    for line in game_lines:
        under = sum(p for g, p in total_games_dist.items() if g < line)
        over = 1 - under
        over_under[str(line)] = {
            "over": round(over, 4), "over_odds": fair_odds(over),
            "under": round(under, 4), "under_odds": fair_odds(under),
        }

    handicap = {}
    for line in handicap_lines:
        a_covers = sum(p for d, p in diff_dist.items() if d > line)
        handicap[str(line)] = {
            "a_covers": round(a_covers, 4), "a_odds": fair_odds(a_covers),
            "b_covers": round(1 - a_covers, 4), "b_odds": fair_odds(1 - a_covers),
        }

    first_set_a = sum(p for (w, ga, gb), p in first_set.items() if w == "A")
    top_first_set = sorted(
        [{"score": f"{ga}-{gb}", "winner": w, "p": round(p, 4)}
         for (w, ga, gb), p in first_set.items()],
        key=lambda x: x["p"], reverse=True)[:top_set_scores]

    expected_games = sum(g * p for g, p in total_games_dist.items())

    return {
        "inputs": {"p_a_serve": p_a_serve, "p_b_serve": p_b_serve, "best_of": best_of,
                   "tiebreak_to": tiebreak_to, "final_set_tiebreak_to": final_set_tiebreak_to},
        "match_win": {
            "a": {"p": round(match_win_a, 4), "odds": fair_odds(match_win_a)},
            "b": {"p": round(match_win_b, 4), "odds": fair_odds(match_win_b)},
        },
        "match_score": {
            k: {"p": round(v, 4), "odds": fair_odds(v)}
            for k, v in sorted(match_score.items(), key=lambda kv: -kv[1])
        },
        "first_set": {
            "a": {"p": round(first_set_a, 4), "odds": fair_odds(first_set_a)},
            "b": {"p": round(1 - first_set_a, 4), "odds": fair_odds(1 - first_set_a)},
            "top_scores": top_first_set,
        },
        "total_games": {
            "expected": round(expected_games, 2),
            "over_under": over_under,
        },
        "games_handicap": handicap,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--p-a-serve", type=float, required=True,
                         help="Probability player A wins a point on A's own serve")
    parser.add_argument("--p-b-serve", type=float, required=True,
                         help="Probability player B wins a point on B's own serve")
    parser.add_argument("--best-of", type=int, choices=[3, 5], default=3)
    parser.add_argument("--tiebreak-to", type=int, default=7,
                         help="Points to win a standard-set tiebreak (default: 7)")
    parser.add_argument("--final-set-tiebreak-to", type=int, default=None,
                         help="Points to win the deciding-set tiebreak if different "
                              "(e.g. 10 for an Australian-Open-style match tiebreak). "
                              "Defaults to --tiebreak-to.")
    parser.add_argument("--game-lines", type=str, default="20.5,21.5,22.5,23.5",
                         help="Comma-separated total-games over/under lines")
    parser.add_argument("--handicap-lines", type=str, default="",
                         help="Comma-separated games-handicap lines for player A, "
                              "e.g. 3.5,4.5 (A -3.5 games, A -4.5 games)")
    parser.add_argument("--top-set-scores", type=int, default=6)
    args = parser.parse_args()

    game_lines = [float(x) for x in args.game_lines.split(",") if x]
    handicap_lines = [float(x) for x in args.handicap_lines.split(",") if x]

    result = analyze(args.p_a_serve, args.p_b_serve, args.best_of, args.tiebreak_to,
                      args.final_set_tiebreak_to, game_lines, handicap_lines,
                      args.top_set_scores)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
