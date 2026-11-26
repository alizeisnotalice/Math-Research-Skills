#!/usr/bin/env python3
"""Certify a full-rank, consistent system E y = a over Z/modulus Z exactly.

This is an offline generic modular-linear-relation checker. It performs only
integer operations and does not search for discrete logarithms.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    """Return positive gcd and Bezout coefficients for nonnegative integers."""
    old_r, remainder = left, right
    old_s, coefficient_s = 1, 0
    old_t, coefficient_t = 0, 1
    while remainder:
        quotient = old_r // remainder
        old_r, remainder = remainder, old_r - quotient * remainder
        old_s, coefficient_s = coefficient_s, old_s - quotient * coefficient_s
        old_t, coefficient_t = coefficient_t, old_t - quotient * coefficient_t
    return old_r, old_s, old_t


def integer(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer")
    return value


def parse_payload(payload: object) -> tuple[int, list[list[int]], list[int]]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    modulus = integer(payload.get("modulus"), "modulus")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    relations = payload.get("relations")
    if not isinstance(relations, list) or not relations:
        raise ValueError("relations must be a nonempty list")
    rows: list[list[int]] = []
    rhs_values: list[int] = []
    width: int | None = None
    for position, relation in enumerate(relations):
        if not isinstance(relation, dict):
            raise ValueError(f"relations[{position}] must be an object")
        coefficients = relation.get("coefficients")
        if not isinstance(coefficients, list) or not coefficients:
            raise ValueError(f"relations[{position}].coefficients must be a nonempty list")
        row = [integer(value, f"relations[{position}].coefficients[{index}") % modulus
               for index, value in enumerate(coefficients)]
        if width is None:
            width = len(row)
        elif len(row) != width:
            raise ValueError("all coefficient rows must have one common length")
        rows.append(row)
        rhs_values.append(integer(relation.get("rhs"), f"relations[{position}].rhs") % modulus)
    return modulus, rows, rhs_values


def check_system(modulus: int, rows: list[list[int]], rhs_values: list[int]) -> dict[str, object]:
    """Return a solution only after rank, residual, and original-row checks."""
    relation_count = len(rows)
    variable_count = len(rows[0])
    if relation_count < variable_count:
        return {"status": "underdetermined", "certified": False,
                "reason": "fewer relations than variables cannot certify full row span"}
    augmented = [row[:] + [rhs] for row, rhs in zip(rows, rhs_values, strict=True)]
    for column in range(variable_count):
        for lower_row in range(column + 1, relation_count):
            pivot, entry = augmented[column][column], augmented[lower_row][column]
            if entry == 0:
                continue
            divisor, pivot_factor, entry_factor = extended_gcd(pivot, entry)
            pivot_row, lower = augmented[column][:], augmented[lower_row][:]
            augmented[column] = [(pivot_factor * left + entry_factor * right) % modulus
                                 for left, right in zip(pivot_row, lower, strict=True)]
            augmented[lower_row] = [((-entry // divisor) * left + (pivot // divisor) * right) % modulus
                                   for left, right in zip(pivot_row, lower, strict=True)]
        divisor, inverse, _ = extended_gcd(augmented[column][column], modulus)
        if divisor != 1:
            return {"status": "pivot_not_unit", "certified": False, "column": column,
                    "pivot": augmented[column][column], "gcd_with_modulus": divisor,
                    "reason": "relations do not establish required full span over Z/modulus Z"}
        augmented[column] = [(inverse * value) % modulus for value in augmented[column]]
    for column in range(variable_count - 1, -1, -1):
        for upper_row in range(column):
            multiplier = augmented[upper_row][column]
            augmented[upper_row] = [(left - multiplier * right) % modulus
                                    for left, right in zip(augmented[upper_row], augmented[column], strict=True)]
    residual_rows = augmented[variable_count:]
    if any(any(value != 0 for value in row) for row in residual_rows):
        return {"status": "inconsistent_relations", "certified": False,
                "reason": "a redundant transformed relation has nonzero residue",
                "residual_rows": residual_rows}
    solution = [augmented[column][-1] for column in range(variable_count)]
    original_residuals = [(sum(coefficient * value for coefficient, value in zip(row, solution, strict=True)) - rhs) % modulus
                          for row, rhs in zip(rows, rhs_values, strict=True)]
    if any(original_residuals):
        raise AssertionError("internal invariant failed")
    return {"status": "certified_solution", "certified": True, "solution": solution,
            "original_residuals": original_residuals,
            "scope": "The supplied finite modular linear relation system only."}


def run_file(path: Path) -> dict[str, object]:
    modulus, rows, rhs_values = parse_payload(json.loads(path.read_text(encoding="utf-8")))
    return {"modulus": modulus, "relation_count": len(rows), "variable_count": len(rows[0]),
            **check_system(modulus, rows, rhs_values)}


def self_test() -> None:
    positive = check_system(12, [[2, 3], [3, 2], [5, 7]], [7, 9, 10])
    assert positive["status"] == "certified_solution" and positive["solution"] == [5, 3]
    assert check_system(12, [[1, 0]], [5])["status"] == "underdetermined"
    assert check_system(2, [[0], [1]], [1, 1])["status"] == "inconsistent_relations"
    try:
        parse_payload({"modulus": 2, "relations": [{"coefficients": [1], "rhs": True}]})
    except ValueError as error:
        assert "rhs must be an integer" in str(error)
    else:
        raise AssertionError("boolean rhs was accepted")
    print("self_test=passed; positive=certified_solution; underdetermined=rejected; malformed=rejected")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="JSON system to validate")
    parser.add_argument("--self-test", action="store_true")
    arguments = parser.parse_args()
    if arguments.self_test:
        self_test()
    if arguments.input is not None:
        try:
            result = run_file(arguments.input)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result["certified"] else 1
        except (OSError, ValueError, json.JSONDecodeError) as error:
            parser.error(str(error))
    elif not arguments.self_test:
        parser.error("provide an input JSON file or --self-test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
