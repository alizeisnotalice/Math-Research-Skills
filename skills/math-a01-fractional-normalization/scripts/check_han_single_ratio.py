#!/usr/bin/env python3
"""Exact finite checker for the Han--Gomez--Prokopyev single-ratio theorem.

The input is a JSON object with b0, a, b, and optionally feasible_masks.
All numeric values must be JSON integers or strings accepted by Fraction;
JSON floating-point values are deliberately rejected.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any


EXIT_NOT_SUBMODULAR = 1
EXIT_OUT_OF_SCOPE = 2
EXIT_INPUT_ERROR = 3


class InputProblem(ValueError):
    """An input that cannot be interpreted as the claimed finite model."""


def frac(value: Any, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise InputProblem(f"{name} must be an integer or an exact rational string, not a float")
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise InputProblem(f"{name} is not an exact rational: {value!r}") from exc


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def elements(mask: int, n: int) -> list[int]:
    return [i + 1 for i in range(n) if mask & (1 << i)]


def immediate_subsets(mask: int):
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        yield mask ^ bit
        remaining ^= bit


def emit(value: dict[str, Any]) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2))


def load_model(path: Path, max_n: int) -> tuple[Fraction, list[Fraction], list[Fraction], list[int]]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InputProblem(f"cannot read JSON input: {exc}") from exc
    if not isinstance(raw, dict):
        raise InputProblem("the JSON top level must be an object")
    for key in ("b0", "a", "b"):
        if key not in raw:
            raise InputProblem(f"missing required key {key!r}")
    if not isinstance(raw["a"], list) or not isinstance(raw["b"], list):
        raise InputProblem("a and b must be arrays")
    if len(raw["a"]) != len(raw["b"]):
        raise InputProblem("a and b must have the same length")
    n = len(raw["a"])
    if n > max_n:
        raise InputProblem(f"n={n} exceeds --max-n={max_n}; increase it knowingly because enumeration is exponential")
    b0 = frac(raw["b0"], "b0")
    a = [frac(value, f"a[{i}]") for i, value in enumerate(raw["a"])]
    b = [frac(value, f"b[{i}]") for i, value in enumerate(raw["b"])]
    limit = 1 << n
    raw_masks = raw.get("feasible_masks")
    if raw_masks is None:
        masks = list(range(limit))
    else:
        if not isinstance(raw_masks, list):
            raise InputProblem("feasible_masks must be an array of integer bitmasks")
        masks = []
        for pos, mask in enumerate(raw_masks):
            if isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit:
                raise InputProblem(f"feasible_masks[{pos}] is not a bitmask in [0, {limit})")
            masks.append(mask)
        if len(set(masks)) != len(masks):
            raise InputProblem("feasible_masks contains duplicates")
        masks.sort()
    return b0, a, b, masks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Han--Gomez--Prokopyev Theorem 1 exactly for one binary ratio."
    )
    parser.add_argument("input", type=Path, help="JSON model with b0, a, b, and optional feasible_masks")
    parser.add_argument(
        "--max-n", type=int, default=20,
        help="maximum number of binary variables to enumerate (default: 20)"
    )
    args = parser.parse_args()
    if args.max_n < 0:
        parser.error("--max-n must be nonnegative")

    try:
        b0, a, b, masks = load_model(args.input, args.max_n)
    except InputProblem as exc:
        emit({"status": "input_error", "error": str(exc)})
        return EXIT_INPUT_ERROR

    n = len(a)
    scope_problems: list[str] = []
    if b0 <= 0:
        scope_problems.append("b0 must be strictly positive for Theorem 1")
    for i, value in enumerate(a, start=1):
        if value < 0:
            scope_problems.append(f"a[{i}] must be nonnegative (A2)")
    for i, value in enumerate(b, start=1):
        if value <= 0:
            scope_problems.append(f"b[{i}] must be strictly positive (A2)")
    feasible = set(masks)
    for mask in masks:
        if any(submask not in feasible for submask in immediate_subsets(mask)):
            scope_problems.append("feasible_masks is not downward closed (A3)")
            break
    if scope_problems:
        emit({
            "status": "out_of_scope",
            "theorem": "Han--Gomez--Prokopyev (arXiv:2012.07235v1), Theorem 1",
            "scope_problems": scope_problems,
            "note": "No conclusion about submodularity is made when these hypotheses fail. In particular, b0=0 is not repaired by this checker.",
        })
        return EXIT_OUT_OF_SCOPE

    # A1 follows here: b0>0 and every b_i>0 make every listed denominator positive.
    numerator = {0: Fraction(0)}
    denominator = {0: b0}
    values = {0: Fraction(0)}
    for mask in masks:
        if mask == 0:
            continue
        bit = mask & -mask
        i = bit.bit_length() - 1
        previous = mask ^ bit
        numerator[mask] = numerator[previous] + a[i]
        denominator[mask] = denominator[previous] + b[i]
        values[mask] = numerator[mask] / denominator[mask]
    ratios = [ai / bi for ai, bi in zip(a, b, strict=True)]


    checked = 0
    predicate_violation: dict[str, Any] | None = None
    max_direct_delta: Fraction | None = None
    for s in masks:
        absent = [i for i in range(n) if not (s & (1 << i))]
        for i, j in combinations(absent, 2):
            si = s | (1 << i)
            sj = s | (1 << j)
            sij = si | (1 << j)
            if sij not in feasible:
                continue
            checked += 1
            lhs = values[si] + values[sj]
            rhs = ratios[i] + ratios[j]
            theorem_gap = lhs - rhs
            direct_delta = values[sij] - values[sj] - values[si] + values[s]
            if max_direct_delta is None or direct_delta > max_direct_delta:
                max_direct_delta = direct_delta
            if (theorem_gap <= 0) != (direct_delta <= 0):
                raise RuntimeError("exact theorem predicate and direct second difference disagree")
            if theorem_gap > 0 and predicate_violation is None:
                predicate_violation = {
                    "S": elements(s, n), "i": i + 1, "j": j + 1,
                    "h_S_union_i": frac_text(values[si]), "h_S_union_j": frac_text(values[sj]),
                    "pair_lhs": frac_text(lhs), "ratio_rhs": frac_text(rhs),
                    "theorem_gap_lhs_minus_rhs": frac_text(theorem_gap),
                    "direct_second_difference": frac_text(direct_delta),
                }


    base = {
        "theorem": "Han--Gomez--Prokopyev (arXiv:2012.07235v1), Theorem 1",
        "exact_arithmetic": "fractions.Fraction; no floating-point input or comparison",
        "assumptions_verified": {
            "A1_positive_denominators": True,
            "A2_nonnegative_a_positive_b": True,
            "A3_downward_closed_family": True,
            "b0_strictly_positive": True,
        },
        "n": n,
        "feasible_set_count": len(masks),
        "pair_tests_checked": checked,
        "largest_direct_second_difference": (
            frac_text(max_direct_delta) if max_direct_delta is not None else None
        ),
    }
    if predicate_violation is None:
        emit({
            **base,
            "status": "submodular",
            "conclusion": "Theorem 1's finite pair predicate holds on the supplied downward-closed family.",
        })
        return 0
    emit({
        **base,
        "status": "not_submodular",
        "conclusion": "Theorem 1's finite pair predicate fails; the included witness also violates the direct diminishing-returns inequality.",
        "witness": predicate_violation,
    })
    return EXIT_NOT_SUBMODULAR


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        emit({"status": "internal_error", "error": str(exc)})
        raise SystemExit(EXIT_INPUT_ERROR)
