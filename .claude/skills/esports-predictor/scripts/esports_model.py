#!/usr/bin/env python3
"""Probability models for esports (CS2, League of Legends, Dota 2).

The esports analogue of the football skill's Poisson model and the tennis
skill's point->game->set->match model. Everything is exact enumeration
(dynamic programming / closed-form distributions), not simulation.

Subcommands:

  elo      Convert two ratings (Elo/Glicko-style) into a single-map/game
           win probability for team A.

  series   Map/game probabilities -> series outcome (BO1/BO2/BO3/BO5/BO7):
           series winner, exact series score, map handicaps (+/-1.5, -2.5),
           total maps over/under and the chance each map gets played.
           Accepts one probability per map (CS2 veto: A pick, B pick,
           decider) or a single probability reused for every map.

  cs-map   CS2 round model for a single map (MR12, first to 13, MR3
           overtime at 12-12, first to 4 in each OT, repeated at 3-3):
           map winner, overtime probability, total rounds over/under,
           round handicap, most likely final scores. Side-aware: team A's
           round-win probability can differ on CT and T side. Can also
           solve for the per-round probability that matches a target
           map-win probability (--p-map-target), so a rating-based map
           probability can be turned into a total-rounds distribution.

  totals   Over/under for count or continuous per-game stats: total kills
           (LoL/Dota, negative binomial when overdispersed, Poisson
           otherwise) or game duration in minutes (normal approximation).

Known simplifications (documented, not hidden -- correct them
qualitatively in the report, same as lambda corrections in football):
- Map/game probabilities are independent between maps (no momentum,
  no tilt, no in-series adaptation, no LoL fearless-draft pool depletion).
- CS2 round-win probability is constant within a side (no economy
  modelling: pistol rounds, eco/force-buy streaks and timeouts are ignored,
  which slightly underestimates the variance of round totals).
- OT side rule: teams start each overtime on the side they finished the
  previous segment on and swap after 3 rounds (standard CS2 rule; verify
  the tournament rulebook if it differs).

Usage:
    python esports_model.py elo --rating-a 1720 --rating-b 1610
    python esports_model.py series --map-probs 0.62,0.48,0.55 --best-of 3
    python esports_model.py series --p-map 0.58 --best-of 5
    python esports_model.py cs-map --p-a-round 0.53 --ct-bias 0.04 \
        --round-lines 19.5,20.5,21.5,22.5 --handicap-lines 3.5,4.5
    python esports_model.py cs-map --p-map-target 0.66 --ct-bias 0.03
    python esports_model.py totals --mean 27.5 --sd 7.5 --lines 24.5,26.5,28.5
    python esports_model.py totals --mean 32.5 --sd 5.5 --continuous \
        --lines 30.5,32.5,34.5
"""

import argparse
import itertools
import json
import math
from collections import defaultdict


def fair_odds(p):
    return round(1 / p, 2) if p and p > 0 else None


def pct(p):
    return {"p": round(p, 4), "odds": fair_odds(p)}


def clamp(p, lo=0.01, hi=0.99):
    return max(lo, min(hi, p))


# --------------------------------------------------------------------- elo

def elo_prob(rating_a, rating_b, scale=400.0):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / scale))


# ------------------------------------------------------------------ series

def series_distribution(map_probs, best_of):
    """Exact distribution over series outcomes.

    Returns {(maps_a, maps_b): prob} and a list of P(map i is played)."""
    probs = list(map_probs)
    while len(probs) < best_of:
        probs.append(probs[-1])

    if best_of == 2:
        need = None  # both maps are always played, 1-1 draw possible
    else:
        need = best_of // 2 + 1

    final = defaultdict(float)
    played = [0.0] * best_of
    for outcome in itertools.product((1, 0), repeat=best_of):
        p = 1.0
        a = b = 0
        for i, won in enumerate(outcome):
            p *= probs[i] if won else 1 - probs[i]
        # walk the series, stop when decided
        for i, won in enumerate(outcome):
            if need is not None and (a == need or b == need):
                break
            played[i] += p
            a += won
            b += 1 - won
        final[(a, b)] += p
    # `played` was accumulated once per full outcome, which is exact because
    # outcomes of maps not played are marginalised over (they sum to 1).
    return final, played


def analyze_series(map_probs, best_of, map_lines, handicap_lines):
    final, played = series_distribution(map_probs, best_of)

    win_a = sum(p for (a, b), p in final.items() if a > b)
    win_b = sum(p for (a, b), p in final.items() if b > a)
    draw = sum(p for (a, b), p in final.items() if a == b)

    maps_dist = defaultdict(float)
    diff_dist = defaultdict(float)
    for (a, b), p in final.items():
        maps_dist[a + b] += p
        diff_dist[a - b] += p

    if not map_lines:
        map_lines = [x + 0.5 for x in range(best_of // 2 + 1, best_of)]
    if not handicap_lines:
        handicap_lines = [x + 0.5 for x in range(1, best_of // 2 + 1)] if best_of >= 3 else []

    over_under = {}
    for line in map_lines:
        under = sum(p for n, p in maps_dist.items() if n < line)
        over_under[str(line)] = {"over": round(1 - under, 4), "over_odds": fair_odds(1 - under),
                                 "under": round(under, 4), "under_odds": fair_odds(under)}

    handicap = {}
    for line in handicap_lines:
        a_minus = sum(p for d, p in diff_dist.items() if d > line)     # A -line
        b_plus = 1 - a_minus                                           # B +line
        b_minus = sum(p for d, p in diff_dist.items() if -d > line)   # B -line
        a_plus = 1 - b_minus                                           # A +line
        handicap[str(line)] = {
            f"a_-{line}": pct(a_minus), f"b_+{line}": pct(b_plus),
            f"b_-{line}": pct(b_minus), f"a_+{line}": pct(a_plus),
        }

    result = {
        "inputs": {"map_probs": map_probs, "best_of": best_of},
        "series_win": {"a": pct(win_a), "b": pct(win_b)},
        "exact_score": {f"{a}-{b}": pct(p)
                        for (a, b), p in sorted(final.items(), key=lambda kv: -kv[1])},
        "total_maps": {"expected": round(sum(n * p for n, p in maps_dist.items()), 3),
                       "over_under": over_under},
        "map_handicap": handicap,
        "p_map_played": [round(x, 4) for x in played],
    }
    if best_of == 2:
        result["series_win"]["draw"] = pct(draw)
    return result


# ------------------------------------------------------------------ cs-map

def _segment(state, rounds, p_a, stop):
    """Advance a score distribution `rounds` rounds with constant p_a,
    moving states that hit `stop(a, b)` into a finished bucket."""
    finished = defaultdict(float)
    for _ in range(rounds):
        nxt = defaultdict(float)
        for (a, b), p in state.items():
            for na, nb, q in ((a + 1, b, p_a), (a, b + 1, 1 - p_a)):
                if stop(na, nb):
                    finished[(na, nb)] += p * q
                else:
                    nxt[(na, nb)] += p * q
        state = nxt
    return state, finished


def cs_map_distribution(p_a_ct, p_a_t, a_starts_ct, max_ot=30):
    """Final-score distribution {(rounds_a, rounds_b): prob} for one CS2 map."""
    first = p_a_ct if a_starts_ct else p_a_t
    second = p_a_t if a_starts_ct else p_a_ct
    reg_stop = lambda a, b: a == 13 or b == 13

    state = {(0, 0): 1.0}
    state, fin1 = _segment(state, 12, first, reg_stop)
    state, fin2 = _segment(state, 12, second, reg_stop)
    final = defaultdict(float)
    for d in (fin1, fin2):
        for k, v in d.items():
            final[k] += v

    # remaining mass sits at 12-12 -> overtime
    tie_mass = state.get((12, 12), 0.0)
    side_now = second  # A keeps the side it finished regulation on
    other = first
    base = 12
    for _ in range(max_ot):
        if tie_mass < 1e-12:
            break
        ot_stop = lambda a, b: a == 4 or b == 4
        s = {(0, 0): tie_mass}
        s, f1 = _segment(s, 3, side_now, ot_stop)
        s, f2 = _segment(s, 3, other, ot_stop)
        for d in (f1, f2):
            for (a, b), v in d.items():
                final[(base + a, base + b)] += v
        tie_mass = s.get((3, 3), 0.0)
        base += 3
        side_now, other = other, side_now  # next OT starts on the side just finished
    return final


def analyze_cs_map(p_a_ct, p_a_t, start_side, round_lines, handicap_lines, top_scores):
    if start_side == "ct":
        final = cs_map_distribution(p_a_ct, p_a_t, True)
    elif start_side == "t":
        final = cs_map_distribution(p_a_ct, p_a_t, False)
    else:
        f1 = cs_map_distribution(p_a_ct, p_a_t, True)
        f2 = cs_map_distribution(p_a_ct, p_a_t, False)
        final = defaultdict(float)
        for d in (f1, f2):
            for k, v in d.items():
                final[k] += v / 2

    win_a = sum(p for (a, b), p in final.items() if a > b)
    p_ot = sum(p for (a, b), p in final.items() if a + b > 24)
    totals = defaultdict(float)
    diffs = defaultdict(float)
    for (a, b), p in final.items():
        totals[a + b] += p
        diffs[a - b] += p

    ou = {}
    for line in round_lines:
        under = sum(p for n, p in totals.items() if n < line)
        ou[str(line)] = {"over": round(1 - under, 4), "over_odds": fair_odds(1 - under),
                         "under": round(under, 4), "under_odds": fair_odds(under)}

    hc = {}
    for line in handicap_lines:
        a_minus = sum(p for d, p in diffs.items() if d > line)
        b_minus = sum(p for d, p in diffs.items() if -d > line)
        hc[str(line)] = {f"a_-{line}": pct(a_minus), f"b_+{line}": pct(1 - a_minus),
                         f"b_-{line}": pct(b_minus), f"a_+{line}": pct(1 - b_minus)}

    top = sorted(final.items(), key=lambda kv: -kv[1])[:top_scores]
    return {
        "inputs": {"p_a_ct": round(p_a_ct, 4), "p_a_t": round(p_a_t, 4), "start_side": start_side},
        "map_win": {"a": pct(win_a), "b": pct(1 - win_a)},
        "overtime": pct(p_ot),
        "total_rounds": {"expected": round(sum(n * p for n, p in totals.items()), 2),
                         "over_under": ou},
        "round_handicap": hc,
        "top_scores": [{"score": f"{a}-{b}", "p": round(p, 4)} for (a, b), p in top],
    }


def sides_from_round(p_round, ct_bias):
    return clamp(p_round + ct_bias), clamp(p_round - ct_bias)


def solve_p_round(p_map_target, ct_bias, start_side):
    lo, hi = 0.2, 0.8
    for _ in range(60):
        mid = (lo + hi) / 2
        ct, t = sides_from_round(mid, ct_bias)
        win = analyze_cs_map(ct, t, start_side, [], [], 1)["map_win"]["a"]["p"]
        # use unrounded value for stability
        if win < p_map_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ------------------------------------------------------------------ totals

def negbin_pmf(k, mean, var):
    r = mean ** 2 / (var - mean)
    p = r / (r + mean)
    return math.exp(math.lgamma(k + r) - math.lgamma(r) - math.lgamma(k + 1)
                    + r * math.log(p) + k * math.log(1 - p))


def poisson_pmf(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


def normal_cdf(x, mu, sd):
    return 0.5 * (1 + math.erf((x - mu) / (sd * math.sqrt(2))))


def analyze_totals(mean, sd, lines, continuous):
    out = {"inputs": {"mean": mean, "sd": sd, "continuous": continuous}}
    ou = {}
    if continuous:
        out["distribution"] = "normal"
        for line in lines:
            under = normal_cdf(line, mean, sd)
            ou[str(line)] = {"over": round(1 - under, 4), "over_odds": fair_odds(1 - under),
                             "under": round(under, 4), "under_odds": fair_odds(under)}
    else:
        var = sd ** 2 if sd else mean
        use_nb = var > mean * 1.001
        out["distribution"] = "negative_binomial" if use_nb else "poisson"
        pmf = (lambda k: negbin_pmf(k, mean, var)) if use_nb else (lambda k: poisson_pmf(k, mean))
        for line in lines:
            under = sum(pmf(k) for k in range(0, int(math.floor(line)) + 1))
            ou[str(line)] = {"over": round(1 - under, 4), "over_odds": fair_odds(1 - under),
                             "under": round(under, 4), "under_odds": fair_odds(under)}
    out["over_under"] = ou
    return out


# -------------------------------------------------------------------- main

def floats(s):
    return [float(x) for x in s.split(",") if x.strip()] if s else []


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("elo", help="rating difference -> single map/game win probability")
    e.add_argument("--rating-a", type=float, required=True)
    e.add_argument("--rating-b", type=float, required=True)
    e.add_argument("--scale", type=float, default=400.0)

    s = sub.add_parser("series", help="map probabilities -> series outcome")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--map-probs", type=str,
                   help="Comma-separated P(A wins map i), in map order; last value is reused")
    g.add_argument("--p-map", type=float, help="Same P(A wins a map) for every map")
    s.add_argument("--best-of", type=int, choices=[1, 2, 3, 5, 7], default=3)
    s.add_argument("--map-lines", type=str, default="", help="Total-maps O/U lines, e.g. 2.5")
    s.add_argument("--handicap-lines", type=str, default="", help="Map handicap lines, e.g. 1.5,2.5")

    c = sub.add_parser("cs-map", help="CS2 round model for one map")
    c.add_argument("--p-a-ct", type=float, help="P(A wins a round while A is CT)")
    c.add_argument("--p-a-t", type=float, help="P(A wins a round while A is T)")
    c.add_argument("--p-a-round", type=float, help="Side-neutral P(A wins a round)")
    c.add_argument("--p-map-target", type=float,
                   help="Solve for the side-neutral round probability giving this map-win probability")
    c.add_argument("--ct-bias", type=float, default=0.0,
                   help="Map CT-sidedness: CT round win rate minus 0.5 (e.g. 0.04 for a CT-sided map)")
    c.add_argument("--start-side", choices=["ct", "t", "random"], default="random")
    c.add_argument("--round-lines", type=str, default="19.5,20.5,21.5,22.5")
    c.add_argument("--handicap-lines", type=str, default="2.5,3.5,4.5")
    c.add_argument("--top-scores", type=int, default=8)

    t = sub.add_parser("totals", help="O/U for kills (count) or game duration (continuous)")
    t.add_argument("--mean", type=float, required=True)
    t.add_argument("--sd", type=float, default=0.0,
                   help="Standard deviation; for counts, sd^2 > mean switches to negative binomial")
    t.add_argument("--lines", type=str, required=True)
    t.add_argument("--continuous", action="store_true", help="Normal approximation (e.g. minutes)")

    args = ap.parse_args()

    if args.cmd == "elo":
        p = elo_prob(args.rating_a, args.rating_b, args.scale)
        res = {"inputs": vars(args), "map_win": {"a": pct(p), "b": pct(1 - p)}}
    elif args.cmd == "series":
        probs = floats(args.map_probs) if args.map_probs else [args.p_map]
        res = analyze_series(probs, args.best_of, floats(args.map_lines), floats(args.handicap_lines))
    elif args.cmd == "cs-map":
        solved = None
        if args.p_a_ct is not None and args.p_a_t is not None:
            ct, tt = args.p_a_ct, args.p_a_t
        elif args.p_a_round is not None:
            ct, tt = sides_from_round(args.p_a_round, args.ct_bias)
        elif args.p_map_target is not None:
            solved = solve_p_round(args.p_map_target, args.ct_bias, args.start_side)
            ct, tt = sides_from_round(solved, args.ct_bias)
        else:
            ap.error("cs-map needs --p-a-ct/--p-a-t, --p-a-round or --p-map-target")
        res = analyze_cs_map(ct, tt, args.start_side, floats(args.round_lines),
                             floats(args.handicap_lines), args.top_scores)
        if solved is not None:
            res["inputs"]["solved_p_a_round"] = round(solved, 4)
    else:
        res = analyze_totals(args.mean, args.sd, floats(args.lines), args.continuous)

    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
