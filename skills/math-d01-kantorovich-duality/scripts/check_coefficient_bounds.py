#!/usr/bin/env python3
"""Exactly check the finite-metric sign-test coefficient bounds."""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def rational(value: Any, label: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError(f"{label} must be an exact integer or rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"{label} is not an exact rational") from error


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def certify(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    raw_matrix = payload.get("distance_matrix")
    if not isinstance(raw_matrix, list) or len(raw_matrix) < 2:
        raise ValueError("distance_matrix must be a square matrix of order at least two")
    size = len(raw_matrix)
    if any(not isinstance(row, list) or len(row) != size for row in raw_matrix):
        raise ValueError("distance_matrix must be square")
    matrix = [[rational(value, f"distance_matrix[{i}][{j}]") for j, value in enumerate(row)]
              for i, row in enumerate(raw_matrix)]
    basepoint = payload.get("basepoint")
    if isinstance(basepoint, bool) or not isinstance(basepoint, int) or not 0 <= basepoint < size:
        raise ValueError("basepoint must be a valid integer index")
    raw_coefficients = payload.get("coefficients")
    if not isinstance(raw_coefficients, list) or len(raw_coefficients) != size:
        raise ValueError("coefficients must have one exact rational entry per point")
    coefficients = [rational(value, f"coefficients[{i}]") for i, value in enumerate(raw_coefficients)]
    if coefficients[basepoint] != 0:
        raise ValueError("coefficient at basepoint must be zero")
    for i in range(size):
        if matrix[i][i] != 0:
            raise ValueError(f"distance_matrix[{i}][{i}] must be zero")
        for j in range(size):
            if matrix[i][j] < 0 or matrix[i][j] != matrix[j][i]:
                raise ValueError("distance matrix must be nonnegative and symmetric")
            if i != j and matrix[i][j] == 0:
                raise ValueError("distinct metric points must have positive distance")
            for k in range(size):
                if matrix[i][k] > matrix[i][j] + matrix[j][k]:
                    raise ValueError(f"triangle inequality fails at ({i}, {j}, {k})")
    separation = min(matrix[i][j] for i in range(size) for j in range(size) if i != j)
    if separation < 1:
        raise ValueError(f"separation is {text(separation)}, below the required 1")
    diameter = max(max(row) for row in matrix)
    bound = rational(payload.get("diameter_bound", diameter), "diameter_bound")
    if bound < diameter:
        raise ValueError(f"diameter_bound {text(bound)} is smaller than exact diameter {text(diameter)}")
    signs = [Fraction(0) if i == basepoint or coefficients[i] == 0 else Fraction(1 if coefficients[i] > 0 else -1, 2)
             for i in range(size)]
    maximum_difference = max(abs(signs[i] - signs[j]) for i in range(size) for j in range(size) if i != j)
    sign_lipschitz_constant = max(abs(signs[i] - signs[j]) / matrix[i][j]
                                  for i in range(size) for j in range(size) if i != j)
    if sign_lipschitz_constant > 1:
        raise AssertionError("the sign test should be 1-Lipschitz under separation >= 1")
    ell_one = sum(abs(value) for value in coefficients)
    lower = sum(coefficients[i] * signs[i] for i in range(size))
    if lower != ell_one / 2:
        raise AssertionError("sign-test identity failed")
    return {
        "status": "PASS", "point_count": size, "basepoint": basepoint,
        "minimum_separation": text(separation), "exact_diameter": text(diameter),
        "diameter_bound": text(bound), "coefficient_l1_norm": text(ell_one),
        "sign_test_values": [text(value) for value in signs],
        "maximum_sign_difference": text(maximum_difference),
        "sign_test_lipschitz_constant": text(sign_lipschitz_constant),
        "certified_lower_bound_for_free_space_norm": text(lower),
        "certified_upper_bound_for_free_space_norm": text(bound * ell_one),
        "claim": "For Jc=sum c_x delta_x in the Lipschitz-free space over this finite pointed metric, (1/2)||c||_1 <= ||Jc|| <= B||c||_1.",
        "limit": "This checks only the supplied finite metric and coefficient vector. It does not compute the free-space norm, prove a countable completion statement, or establish BAP/AP/failure of BAP.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="finite pointed metric certificate JSON")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(certify(payload), ensure_ascii=False, indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
