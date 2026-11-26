#!/usr/bin/env python3
"""Exact finite-support Euclidean replay for the centred inductive-mean identity."""
import argparse
import itertools
import json
import sys
from fractions import Fraction


def q(value):
    return Fraction(str(value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", required=True, help="JSON list of coordinate lists")
    parser.add_argument("--weights", required=True, help="JSON list of rational strings")
    parser.add_argument("--steps", type=int, required=True)
    args = parser.parse_args()
    try:
        points = [[q(x) for x in row] for row in json.loads(args.points)]
        weights = [q(x) for x in json.loads(args.weights)]
    except (ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"rejected: invalid rational JSON ({exc})")
        return 2
    if not points or len(points) != len(weights) or args.steps < 1:
        print("rejected: nonempty matching support and positive steps required")
        return 2
    dim = len(points[0])
    if not dim or any(len(p) != dim for p in points) or any(w < 0 for w in weights):
        print("rejected: equal nonzero dimension and nonnegative weights required")
        return 2
    if sum(weights) != 1:
        print("rejected: weights must sum exactly to 1")
        return 2
    mean = [sum(w * p[k] for w, p in zip(weights, points)) for k in range(dim)]
    if any(mean):
        print("rejected: Euclidean barycenter is not zero")
        return 2
    outcomes = len(points) ** args.steps
    if outcomes > 1_000_000:
        print("rejected: support^steps exceeds exact replay cap 1000000")
        return 2
    moment = sum(w * sum(x*x for x in p) for w, p in zip(weights, points))
    observed = Fraction()
    for choices in itertools.product(range(len(points)), repeat=args.steps):
        prob = Fraction(1)
        total = [Fraction() for _ in range(dim)]
        for i in choices:
            prob *= weights[i]
            total = [a + b for a, b in zip(total, points[i])]
        observed += prob * sum(x*x for x in total) / (args.steps * args.steps)
    expected = moment / args.steps
    if observed != expected:
        print(f"rejected: identity mismatch observed={observed} expected={expected}")
        return 1
    print(f"accepted: sigma2={moment} steps={args.steps} mean_energy={observed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
