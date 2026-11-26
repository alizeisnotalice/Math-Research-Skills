#!/usr/bin/env python3
"""Check a finite weak-(1,1) weighted-aggregation threshold certificate.

For supplied positive a_i, C_i, thresholds u_i, and alpha, it verifies
sum(a_i*u_i) <= alpha and returns sum(C_i/u_i).  Given weak bounds
mu{T_i f > u} <= C_i ||f||_1/u, the union argument then bounds the level
set of sum(a_i*T_i f) above alpha by that returned constant times ||f||_1.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


def rational(value: object, field: str) -> Fraction:
    if type(value) is int:
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as error:
            raise ValueError(f"{field} must contain rational integers or p/q strings") from error
    raise ValueError(f"{field} must contain rational integers or p/q strings")


def positive_list(payload: dict, field: str) -> list[Fraction]:
    values = payload.get(field)
    if not isinstance(values, list) or not values:
        raise ValueError(f"{field} must be a nonempty list")
    result = [rational(value, field) for value in values]
    if any(value <= 0 for value in result):
        raise ValueError(f"{field} must be strictly positive")
    return result


def rational_sqrt(value: Fraction) -> Fraction | None:
    numerator_root = math.isqrt(value.numerator)
    denominator_root = math.isqrt(value.denominator)
    if numerator_root * numerator_root != value.numerator or denominator_root * denominator_root != value.denominator:
        return None
    return Fraction(numerator_root, denominator_root)


def validate(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    weights = positive_list(payload, "weights")
    constants = positive_list(payload, "weak_constants")
    thresholds = positive_list(payload, "component_thresholds")
    if len({len(weights), len(constants), len(thresholds)}) != 1:
        raise ValueError("weights, weak_constants, and component_thresholds need equal lengths")
    target = rational(payload.get("target_threshold"), "target_threshold")
    if target <= 0:
        raise ValueError("target_threshold must be strictly positive")
    weighted_threshold_sum = sum((weight * threshold for weight, threshold in zip(weights, thresholds)), Fraction())
    if weighted_threshold_sum > target:
        raise ValueError("sum(weights[i] * component_thresholds[i]) exceeds target_threshold")
    union_constant = sum((constant / threshold for constant, threshold in zip(constants, thresholds)), Fraction())
    claimed = payload.get("claimed_weak_constant")
    if claimed is not None and rational(claimed, "claimed_weak_constant") != union_constant:
        raise ValueError("claimed_weak_constant differs from the exact union-bound constant")
    roots = [rational_sqrt(weight * constant) for weight, constant in zip(weights, constants)]
    optimizer_thresholds = [rational_sqrt(constant / weight) for weight, constant in zip(weights, constants)]
    source_formula = None
    if all(root is not None for root in roots) and all(threshold is not None for threshold in optimizer_thresholds):
        square_root_sum = sum(roots, Fraction())
        source_formula = {
            "sqrt_weight_constant_sum": str(square_root_sum),
            "optimal_weak_constant": str(square_root_sum * square_root_sum / target),
            "optimal_component_thresholds": [str(target * threshold / square_root_sum) for threshold in optimizer_thresholds],
            "input_attains_source_bound": union_constant == square_root_sum * square_root_sum / target,
        }
    else:
        source_formula = {
            "symbolic_bound": "(sum_i sqrt(weights[i] * weak_constants[i]))^2 / target_threshold",
            "input_attains_source_bound": None,
        }
    return {
        "terms": len(weights),
        "weighted_threshold_sum": str(weighted_threshold_sum),
        "target_threshold": str(target),
        "threshold_budget_verified": True,
        "union_bound_weak_constant": str(union_constant),
        "claimed_constant_verified": claimed is not None,
        "source_formula": source_formula,
        "implication": "Under the supplied component weak-(1,1) hypotheses, mu{sum_i a_i T_i f > alpha} <= union_bound_weak_constant * ||f||_1.",
        "scope": "Finite nonnegative operator families only. Countable aggregation additionally needs monotone partial sums and the stated square-root summability.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
