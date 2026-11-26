#!/usr/bin/env python3
"""Exact finite certificate for overflow order and hinge-convex objectives."""
import argparse
import json
from fractions import Fraction


def fraction(value):
    return Fraction(str(value))


def overflow(weights, density, threshold):
    return sum(weight * max(value - threshold, Fraction(0))
               for weight, value in zip(weights, density))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", help="JSON certificate")
    args = parser.parse_args()
    with open(args.certificate, encoding="utf-8") as handle:
        data = json.load(handle)
    weights = [fraction(x) for x in data["base_weights"]]
    selected = [fraction(x) for x in data["selected_density"]]
    competitor = [fraction(x) for x in data["competitor_density"]]
    if not weights or not (len(weights) == len(selected) == len(competitor)):
        raise SystemExit("weights and both density lists must be equally nonempty")
    if any(x <= 0 for x in weights) or any(x < 0 for x in selected + competitor):
        raise SystemExit("weights must be positive and densities nonnegative")
    selected_mass = sum(w * x for w, x in zip(weights, selected))
    competitor_mass = sum(w * x for w, x in zip(weights, competitor))
    if selected_mass != competitor_mass:
        raise SystemExit("the two densities must have equal weighted mass")
    thresholds = sorted({Fraction(0), *selected, *competitor})
    rows = [(t, overflow(weights, selected, t), overflow(weights, competitor, t))
            for t in thresholds]
    if any(left > right for _, left, right in rows):
        raise SystemExit("selected density does not satisfy overflow domination")
    hinges = [(fraction(item["threshold"]), fraction(item["coefficient"]))
              for item in data.get("hinges", [])]
    if any(coefficient < 0 for _, coefficient in hinges):
        raise SystemExit("hinge coefficients must be nonnegative")
    def objective(density):
        return sum(coefficient * overflow(weights, density, threshold)
                   for threshold, coefficient in hinges)
    left_objective, right_objective = objective(selected), objective(competitor)
    if left_objective > right_objective:
        raise SystemExit("hinge objective contradicts the overflow certificate")
    print(json.dumps({
        "equal_mass": str(selected_mass),
        "overflow_checks": [[str(t), str(left), str(right)] for t, left, right in rows],
        "selected_hinge_objective": str(left_objective),
        "competitor_hinge_objective": str(right_objective),
        "result": "verified",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
