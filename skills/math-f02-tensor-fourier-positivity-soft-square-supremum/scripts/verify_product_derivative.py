#!/usr/bin/env python3
"""Exact combinatorial check for the affine tensor-product derivative bound."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import factorial
from typing import Iterable


def parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid rational {text!r}") from exc


def elementary_symmetric(weights: Iterable[Fraction], order: int) -> Fraction:
    coeffs = [Fraction(0) for _ in range(order + 1)]
    coeffs[0] = Fraction(1)
    for weight in weights:
        for degree in range(order, 0, -1):
            coeffs[degree] += weight * coeffs[degree - 1]
    return coeffs[order]


def certificate(weights: list[Fraction], order: int, c: Fraction, amplitude: Fraction) -> dict[str, object]:
    if order < 0:
        raise ValueError("order must be nonnegative")
    if c <= 0:
        raise ValueError("c must be strictly positive")
    if amplitude < 0:
        raise ValueError("amplitude must be nonnegative")
    if any(weight < 0 for weight in weights):
        raise ValueError("all weights must be nonnegative")
    total = sum(weights, Fraction(0))
    symmetric = elementary_symmetric(weights, order)
    lhs = factorial(order) * symmetric
    rhs = total ** order
    assert lhs <= rhs
    ceiling = max(weights, default=Fraction(0))
    return {
        "status": "PASS",
        "arithmetic": "exact rational",
        "dimension": len(weights),
        "order": order,
        "U": str(total),
        "w": str(ceiling),
        "elementary_symmetric_e_k": str(symmetric),
        "k_factorial_times_e_k": str(lhs),
        "U_to_k": str(rhs),
        "combinatorial_inequality": "k! e_k(u) <= U^k",
        "analytic_factor_contract": "|z_j| <= exp(-c u_j), |z_j'| <= A u_j",
        "dimension_free_bound": f"({amplitude})^{order} * exp(({c})*({order})*({ceiling})) * ({c})^(-{order}) * {factorial(order)}",
        "note": "The exponential factor is symbolic; this program does not certify analytic factor bounds from floats.",
    }


def self_test() -> None:
    first = certificate([Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(0)], 2, Fraction(2, 5), Fraction(7))
    assert first["k_factorial_times_e_k"] == "3/4"
    assert first["U_to_k"] == "169/144"
    zero = certificate([Fraction(1, 2), Fraction(1, 3)], 3, Fraction(1, 7), Fraction(7))
    assert zero["elementary_symmetric_e_k"] == "0"
    assert zero["k_factorial_times_e_k"] == "0"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weights", required=False, default="", help="comma-separated nonnegative rationals")
    parser.add_argument("--order", type=int, required=False, default=0)
    parser.add_argument("--c", type=parse_fraction, required=False, default=Fraction(1))
    parser.add_argument("--amplitude", type=parse_fraction, required=False, default=Fraction(7))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print(json.dumps({"status": "PASS", "self_test": "exact rational cases"}))
        return 0
    weights = [] if not args.weights else [parse_fraction(part.strip()) for part in args.weights.split(",")]
    try:
        result = certificate(weights, args.order, args.c, args.amplitude)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
