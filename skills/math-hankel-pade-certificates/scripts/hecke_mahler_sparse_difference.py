#!/usr/bin/env python3
"""Exact finite support audit for a Hecke--Mahler difference sequence."""
import json
import math
import sys
from fractions import Fraction


def fraction(value):
    return Fraction(str(value))


def floor_radical(a, b, d):
    """Return floor(a + b*sqrt(d)) for b >= 0 using integer comparisons."""
    if b < 0 or d <= 0 or math.isqrt(d) ** 2 == d:
        raise ValueError("require nonsquare positive d and nonnegative radical coefficient")
    low = a.numerator // a.denominator - 1
    ceil_b = -((-b.numerator) // b.denominator)
    high = a.numerator // a.denominator + ceil_b * (math.isqrt(d) + 2) + 3
    while high - low > 1:
        candidate = (low + high) // 2
        remainder = Fraction(candidate) - a
        at_least = remainder <= 0 or b * b * d >= remainder * remainder
        if at_least:
            low = candidate
        else:
            high = candidate
    return low


def polynomial(coefficients, x):
    total = 0
    for coefficient in reversed(coefficients):
        total = total * x + int(coefficient)
    return total


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    theta = data["theta"]
    c = int(theta["c"])
    if c <= 0:
        raise ValueError("theta denominator c must be positive")
    theta_a = Fraction(int(theta["a"]), c)
    theta_b = Fraction(int(theta["b"]), c)
    d = int(theta["d"])
    alpha = fraction(data["alpha"])
    coeffs = data["polynomial"]
    if not coeffs or len(coeffs) == 1:
        raise ValueError("polynomial must be nonconstant")
    r, maximum = int(data["shift"]), int(data["max_m"])
    if r <= 0 or maximum < 0:
        raise ValueError("shift must be positive and max_m nonnegative")
    order = len(coeffs)
    values = [polynomial(coeffs, floor_radical(alpha + m * theta_a, m * theta_b, d))
              for m in range(maximum + order * r + 1)]
    weights = [(-1) ** j * math.comb(order, j) for j in range(order + 1)]
    difference = [sum(weights[j] * values[m + j * r] for j in range(order + 1))
                  for m in range(maximum + 1)]
    support = [m for m, value in enumerate(difference) if value]
    gaps = [b - a for a, b in zip(support, support[1:])]
    result = {
        "difference_order": order,
        "finite_prefix": [0, maximum],
        "least_observed_gap": min(gaps) if gaps else None,
        "nonzero_count": len(support),
        "nonzero_positions": support,
        "shift": r,
        "weights": weights,
        "scope": "Exact finite floor and finite-difference computation only; it does not prove Condition (*) or a transcendence statement."
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: hecke_mahler_sparse_difference.py INPUT.json")
    main(sys.argv[1])
