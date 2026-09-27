#!/usr/bin/env python3
"""Poisson-based football match outcome model.

Given expected goals (xG) for the home and away team, computes:
- 1X2 probabilities (home win / draw / away win)
- Probability matrix and ranked list of most likely correct scores
- Over/Under probabilities for the requested goal lines
- Both Teams To Score (BTTS) probability

Each probability is also converted to a "fair" decimal odd (1 / p),
useful for comparing against bookmaker odds.

The model is generic in lambda, so it also powers the skill's corner-kick
model (the priority stat, see SKILL.md Krok 4): pass expected corners
instead of expected goals and read "1x2" as "which team gets more corners".
Raise --max-goals accordingly since corner counts run higher than goals.

Usage:
    python poisson_model.py --lambda-home 1.8 --lambda-away 1.2
    python poisson_model.py --lambda-home 1.4 --lambda-away 1.4 \
        --max-goals 8 --ou-lines 1.5,2.5,3.5,4.5 --top-scores 8
    # Corners instead of goals:
    python poisson_model.py --lambda-home 6.2 --lambda-away 4.6 \
        --max-goals 15 --ou-lines 8.5,9.5,10.5,11.5 --top-scores 5
"""

import argparse
import json
import math


def poisson_pmf(k: int, lam: float) -> float:
    return math.exp(-lam) * lam ** k / math.factorial(k)


def fair_odds(p: float) -> float:
    return round(1 / p, 2) if p > 0 else None


def build_score_matrix(lambda_home: float, lambda_away: float, max_goals: int):
    home_probs = [poisson_pmf(i, lambda_home) for i in range(max_goals + 1)]
    away_probs = [poisson_pmf(i, lambda_away) for i in range(max_goals + 1)]
    return [[h * a for a in away_probs] for h in home_probs]


def analyze(lambda_home: float, lambda_away: float, max_goals: int,
            ou_lines: list, top_scores: int):
    matrix = build_score_matrix(lambda_home, lambda_away, max_goals)

    home_win = sum(matrix[h][a] for h in range(max_goals + 1)
                    for a in range(max_goals + 1) if h > a)
    draw = sum(matrix[h][a] for h in range(max_goals + 1)
               for a in range(max_goals + 1) if h == a)
    away_win = sum(matrix[h][a] for h in range(max_goals + 1)
                    for a in range(max_goals + 1) if h < a)

    btts_yes = sum(matrix[h][a] for h in range(1, max_goals + 1)
                    for a in range(1, max_goals + 1))
    btts_no = 1 - btts_yes

    scores = []
    for h in range(max_goals + 1):
        for a in range(max_goals + 1):
            scores.append({"score": f"{h}-{a}", "p": matrix[h][a]})
    scores.sort(key=lambda x: x["p"], reverse=True)
    top = scores[:top_scores]

    over_under = {}
    for line in ou_lines:
        under = sum(matrix[h][a] for h in range(max_goals + 1)
                     for a in range(max_goals + 1) if (h + a) < line)
        over = 1 - under
        over_under[str(line)] = {
            "over": round(over, 4), "over_odds": fair_odds(over),
            "under": round(under, 4), "under_odds": fair_odds(under),
        }

    return {
        "inputs": {"lambda_home": lambda_home, "lambda_away": lambda_away,
                    "max_goals": max_goals},
        "1x2": {
            "home": {"p": round(home_win, 4), "odds": fair_odds(home_win)},
            "draw": {"p": round(draw, 4), "odds": fair_odds(draw)},
            "away": {"p": round(away_win, 4), "odds": fair_odds(away_win)},
        },
        "btts": {
            "yes": {"p": round(btts_yes, 4), "odds": fair_odds(btts_yes)},
            "no": {"p": round(btts_no, 4), "odds": fair_odds(btts_no)},
        },
        "over_under": over_under,
        "top_scores": [
            {"score": s["score"], "p": round(s["p"], 4), "odds": fair_odds(s["p"])}
            for s in top
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                       formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lambda-home", type=float, required=True,
                         help="Expected goals for the home team")
    parser.add_argument("--lambda-away", type=float, required=True,
                         help="Expected goals for the away team")
    parser.add_argument("--max-goals", type=int, default=6,
                         help="Max goals per team considered (default: 6)")
    parser.add_argument("--ou-lines", type=str, default="0.5,1.5,2.5,3.5,4.5",
                         help="Comma-separated over/under lines (default: 0.5,1.5,2.5,3.5,4.5)")
    parser.add_argument("--top-scores", type=int, default=6,
                         help="How many most likely correct scores to return (default: 6)")
    args = parser.parse_args()

    ou_lines = [float(x) for x in args.ou_lines.split(",")]
    result = analyze(args.lambda_home, args.lambda_away, args.max_goals,
                      ou_lines, args.top_scores)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
