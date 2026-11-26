#!/usr/bin/env python3
"""Verify an exact finite active-gradient projection certificate."""
import argparse
import json
from fractions import Fraction


def q(value):
    return Fraction(str(value))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", help="JSON with gradients and weights")
    args = ap.parse_args()
    with open(args.certificate, encoding="utf-8") as handle:
        data = json.load(handle)
    gradients = [[q(x) for x in row] for row in data["gradients"]]
    weights = [q(x) for x in data["weights"]]
    if not gradients or len(gradients) != len(weights):
        raise SystemExit("need one nonempty gradient list and one weight per gradient")
    dim = len(gradients[0])
    if not all(len(row) == dim for row in gradients):
        raise SystemExit("gradient dimensions disagree")
    if any(weight < 0 for weight in weights) or sum(weights) != 1:
        raise SystemExit("weights must be nonnegative and sum exactly to one")
    point = [sum(weights[i] * gradients[i][j] for i in range(len(weights))) for j in range(dim)]
    norm2 = sum(x * x for x in point)
    dots = [sum(row[j] * point[j] for j in range(dim)) for row in gradients]
    if any(dot < norm2 for dot in dots):
        raise SystemExit("certificate fails the projection inequality")
    print(json.dumps({"projection": [str(x) for x in point], "norm_squared": str(norm2),
                      "projection_inequality": "verified", "separating_direction":
                      "-p/||p|| when norm_squared is positive"}, sort_keys=True))


if __name__ == "__main__":
    main()
