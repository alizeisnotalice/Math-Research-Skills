#!/usr/bin/env python3
"""Compute or compare the exact count laws of independent Bernoulli trials."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import accumulate, combinations
import json
from pathlib import Path
from typing import Any

def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("probabilities must be integer or string-rational, never bool/float")
    if isinstance(value, int):
        answer = Fraction(value)
    elif isinstance(value, str):
        try:
            answer = Fraction(value)
        except (ValueError, ZeroDivisionError) as error:
            raise ValueError("invalid exact probability") from error
    else:
        raise ValueError("probabilities must be integer or string-rational")
    if not 0 <= answer <= 1:
        raise ValueError("each probability must lie in [0,1]")
    return answer


def as_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def exact_pmf(parameters: list[Fraction]) -> list[Fraction]:
    mass = [Fraction(1)]
    for probability in parameters:
        following = [Fraction(0)] * (len(mass) + 1)
        for index, coefficient in enumerate(mass):
            following[index] += coefficient * (1 - probability)
            following[index + 1] += coefficient * probability
        mass = following
    return mass


def survival(pmf: list[Fraction]) -> list[Fraction]:
    return [*reversed(list(accumulate(reversed(pmf)))), Fraction(0)]


def increasing_ratio(left: list[Fraction], right: list[Fraction]) -> bool:
    return all(left[i] * right[j] >= left[j] * right[i]
               for i, j in combinations(range(len(left)), 2))


def orders(left: list[Fraction], right: list[Fraction]) -> dict[str, bool]:
    n = max(len(left), len(right))
    x = left + [Fraction(0)] * (n - len(left))
    y = right + [Fraction(0)] * (n - len(right))
    sx, sy = survival(x), survival(y)
    stop_loss_x = list(accumulate(reversed(sx[1:])))
    stop_loss_y = list(accumulate(reversed(sy[1:])))
    return {
        "stochastic": all(a <= b for a, b in zip(sx, sy, strict=True)),
        "convex": stop_loss_x[-1] == stop_loss_y[-1] and all(
            a <= b for a, b in zip(stop_loss_x, stop_loss_y, strict=True)
        ),
        "likelihood_ratio": increasing_ratio(x, y),
        "reversed_hazard": increasing_ratio(list(accumulate(x)), list(accumulate(y))),
    }


def describe(pmf: list[Fraction], parameters: list[Fraction]) -> dict:
    return {
        "trial_count": len(parameters),
        "mean": as_text(sum(parameters, Fraction(0))),
        "variance": as_text(sum((p * (1 - p) for p in parameters), Fraction(0))),
        "pmf": [as_text(x) for x in pmf],
        "survival_ge": [as_text(x) for x in survival(pmf)],
    }


def certify(data: Any) -> dict:
    if not isinstance(data, dict) or not isinstance(data.get("probabilities"), list):
        raise ValueError("input must be an object with a probabilities array")
    p = [parse_fraction(value) for value in data["probabilities"]]
    left = exact_pmf(p)
    result = {"model": "each count sums independent Bernoulli trials", "left": describe(left, p)}
    if "comparison_probabilities" in data:
        raw = data["comparison_probabilities"]
        if not isinstance(raw, list):
            raise ValueError("comparison_probabilities must be an array")
        q = [parse_fraction(value) for value in raw]
        right = exact_pmf(q)
        result["right"] = describe(right, q)
        result["left_leq_right"] = orders(left, right)
        result["right_leq_left"] = orders(right, left)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
