#!/usr/bin/env python3
"""Exact finite audit for Kleiner's Poisson--binomial atom-reversal threshold.

Inputs are JSON objects with a ``probabilities`` array of integer or string-rational
parameters.  Floats are rejected: all displayed atom masses and comparisons are exact.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def nonnegative_int(value: str) -> int:
    answer = int(value)
    if answer < 0:
        raise argparse.ArgumentTypeError("must be a non-negative integer")
    return answer


def positive_int(value: str) -> int:
    answer = int(value)
    if answer < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return answer


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("probabilities must be integer or string-rational, never bool/float")
    if isinstance(value, int):
        answer = Fraction(value)
    elif isinstance(value, str):
        answer = Fraction(value)
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


def staircase_d(k: int) -> int:
    """The integer d_k, evaluated without a floating-point square root."""
    d = 2
    while k >= 8 * d * d - 2 * d - 4:
        d += 1
    return d


def distance_two_relation(mean: Fraction, k: int, d: int) -> str:
    """Compare mean-k with Delta_k by squaring only non-negative quantities.

    Delta_k = (d*A-k*H)/(A+H), A^2=(k+1)(k+2), H^2=d(d-1).
    This returns the exact relation; it never evaluates either square root.
    """
    excess = mean - k
    left = excess - d
    right = excess + k  # This equals the nonnegative mean.
    if left >= 0:
        return "greater"
    # Need right*H ? (d-excess)*A.  Both sides are nonnegative.
    lhs = right * right * d * (d - 1)
    rhs = (d - excess) * (d - excess) * (k + 1) * (k + 2)
    return "greater" if lhs > rhs else "equal" if lhs == rhs else "less"


def threshold_description(k: int, r: int) -> tuple[str, dict[str, Any]]:
    if r == 1:
        excess = Fraction(1, k + 2)
        return (
            f"{k}+{as_text(excess)}",
            {"kind": "rational", "excess": as_text(excess)},
        )
    if r >= 3:
        return (f"{k}+1", {"kind": "integer", "excess": "1"})
    d = staircase_d(k)
    return (
        f"{k} + (d*sqrt((k+1)(k+2)) - k*sqrt(d(d-1))) / "
        f"(sqrt((k+1)(k+2)) + sqrt(d(d-1))), d={d}",
        {
            "kind": "quadratic-radical",
            "d": d,
            "A_squared": (k + 1) * (k + 2),
            "H_squared": d * (d - 1),
        },
    )


def boundary(k: int) -> dict[str, Any]:
    d = staircase_d(k)
    lower = None if d == 2 else 8 * (d - 1) ** 2 - 2 * (d - 1) - 4
    upper = 8 * d * d - 2 * d - 4
    ratio_square = Fraction((k + 1) * (k + 2), d * (d - 1))
    n = k + d
    coefficient_ratio = Fraction(math.comb(n, k + 2), math.comb(n, k))
    return {
        "k": k,
        "d": d,
        "staircase_interval": {"lower_inclusive": lower, "upper_exclusive": upper},
        "odds_ratio_square_at_boundary": as_text(ratio_square),
        "binomial_coefficient_ratio": as_text(coefficient_ratio),
        "exact_tie_check": as_text(coefficient_ratio * ratio_square),
        "threshold": threshold_description(k, 2)[0],
        "note": "exact_tie_check=1 proves P(Bin(k+d,q)=k+2)=P(Bin(k+d,q)=k) whenever q/(1-q) has the displayed squared value; no radical is evaluated.",
    }


def audit(path: Path, k: int, r: int) -> dict[str, Any]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("probabilities"), list):
        raise ValueError("input must be an object with a probabilities array")
    probabilities = [parse_fraction(value) for value in document["probabilities"]]
    pmf = exact_pmf(probabilities)
    lower = pmf[k] if k < len(pmf) else Fraction(0)
    upper_index = k + r
    upper = pmf[upper_index] if upper_index < len(pmf) else Fraction(0)
    mean = sum(probabilities, Fraction(0))
    threshold, data = threshold_description(k, r)
    if r == 2:
        mean_relation = distance_two_relation(mean, k, int(data["d"]))
    else:
        mean_relation = "greater" if mean > k + Fraction(data["excess"]) else "equal" if mean == k + Fraction(data["excess"]) else "less"
    reversed_atoms = upper > lower
    return {
        "model": "finite independent Bernoulli sum with rational parameters",
        "trial_count": len(probabilities),
        "mean": as_text(mean),
        "k": k,
        "r": r,
        "P(S=k)": as_text(lower),
        "P(S=k+r)": as_text(upper),
        "strict_reversal": reversed_atoms,
        "threshold_infimum": threshold,
        "mean_vs_threshold": mean_relation,
        "theorem_check": (
            "passes necessary condition" if not reversed_atoms or mean_relation == "greater"
            else "CONTRADICTION: investigate input or implementation"
        ),
        "scope": "Kleiner Theorem 1.1: the converse is not asserted; a non-reversal says nothing about the mean threshold.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    boundary_parser = commands.add_parser("boundary", help="exact distance-two staircase and binomial tie identity")
    boundary_parser.add_argument("--k", type=nonnegative_int, required=True)
    audit_parser = commands.add_parser("audit", help="exact rational PBD audit against the sharp necessary threshold")
    audit_parser.add_argument("--input", type=Path, required=True)
    audit_parser.add_argument("--k", type=nonnegative_int, required=True)
    audit_parser.add_argument("--r", type=positive_int, required=True)
    arguments = parser.parse_args()
    try:
        result = boundary(arguments.k) if arguments.command == "boundary" else audit(arguments.input, arguments.k, arguments.r)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if arguments.command == "boundary" or not result["strict_reversal"] or result["mean_vs_threshold"] == "greater" else 1


if __name__ == "__main__":
    raise SystemExit(main())
