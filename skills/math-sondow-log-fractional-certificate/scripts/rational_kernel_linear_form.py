#!/usr/bin/env python3
"""Extract an exact Sondow--Zlobin linear form from explicit partial fractions.

The input records a rational kernel

    R(t) = sum_k (b2[k]/(t+k)^2 + b1[k]/(t+k)).

This program checks the two vanishing asymptotic coefficients required by
Proposition 1 of arXiv:math/0211075v4.  It does not claim an integrality
result, a tail bound, or an irrationality result.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(value: Any) -> Fraction:
    """Read a JSON integer or a string accepted by Fraction."""
    if isinstance(value, bool):
        raise ValueError("Boolean values are not coefficients")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"coefficient must be an integer or p/q string, got {value!r}")


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def harmonic(number: int) -> Fraction:
    return sum((Fraction(1, divisor) for divisor in range(1, number + 1)), Fraction())


def load_kernel(path: Path) -> tuple[int, list[tuple[int, Fraction, Fraction]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    degree = payload.get("n")
    if not isinstance(degree, int) or isinstance(degree, bool) or degree < 1:
        raise ValueError("n must be a positive integer")
    entries = payload.get("coefficients")
    if not isinstance(entries, list):
        raise ValueError("coefficients must be a list")

    by_index: dict[int, tuple[Fraction, Fraction]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("each coefficient entry must be an object")
        index = entry.get("k")
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("every k must be an integer")
        if index in by_index:
            raise ValueError(f"duplicate coefficient index k={index}")
        if "double" not in entry or "simple" not in entry:
            raise ValueError(f"coefficient k={index} needs double and simple fields")
        by_index[index] = (parse_fraction(entry["double"]), parse_fraction(entry["simple"]))

    if len(by_index) != degree + 1 or any(k < 0 or k > degree for k in by_index):
        raise ValueError("indices must be exactly 0,...,n")
    return degree, [(index, *by_index[index]) for index in range(degree + 1)]


def extract(degree: int, coefficients: list[tuple[int, Fraction, Fraction]]) -> dict[str, Any]:
    # (t+k)^-1 = t^-1 - k t^-2 + O(t^-3),
    # (t+k)^-2 = t^-2 + O(t^-3).
    coefficient_t_minus_1 = sum((simple for _, _, simple in coefficients), Fraction())
    coefficient_t_minus_2 = sum(
        (double - index * simple for index, double, simple in coefficients), Fraction()
    )
    has_required_decay = coefficient_t_minus_1 == 0 and coefficient_t_minus_2 == 0

    gamma_coefficient = sum((double for _, double, _ in coefficients), Fraction())
    rational_term = sum(
        (double * harmonic(degree + index) for index, double, _ in coefficients), Fraction()
    )
    log_weights: list[dict[str, Any]] = []
    for offset in range(1, degree + 1):
        coefficient = sum((simple for index, _, simple in coefficients if index >= offset), Fraction())
        if coefficient:
            log_weights.append(
                {"argument": degree + offset, "coefficient": fraction_text(coefficient)}
            )
    return {
        "n": degree,
        "required_decay_certified": has_required_decay,
        "asymptotic_coefficients": {
            "t^-1": fraction_text(coefficient_t_minus_1),
            "t^-2": fraction_text(coefficient_t_minus_2),
        },
        "gamma_coefficient_B": fraction_text(gamma_coefficient),
        "rational_term_A": fraction_text(rational_term),
        "log_weights_L": log_weights,
        "proposition_if_decay_holds": "sum_{v=n+1}^infinity integral_v^infinity R(t) dt = B*gamma + L - A",
        "scope": "No integrality, tail estimate, positivity, or irrationality conclusion is certified here.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kernel_json", type=Path, help="JSON with n and explicit coefficients")
    parser.add_argument("--indent", type=int, default=2, help="JSON indentation")
    arguments = parser.parse_args()
    try:
        degree, coefficients = load_kernel(arguments.kernel_json)
        result = extract(degree, coefficients)
    except (OSError, ValueError, ZeroDivisionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=arguments.indent, sort_keys=True))
    return 0 if result["required_decay_certified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
