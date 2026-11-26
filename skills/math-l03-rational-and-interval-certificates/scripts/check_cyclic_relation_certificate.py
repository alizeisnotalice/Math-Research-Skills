#!/usr/bin/env python3
"""Verify a finite cyclic-group relation certificate with exact integer arithmetic."""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from typing import Any

from check_modular_linear_relations import check_system, integer, parse_payload


def unit(value: Any, modulus: int, label: str) -> int:
    value = integer(value, label) % modulus
    if gcd(value, modulus) != 1:
        raise ValueError(f"{label} must be a unit modulo group_modulus")
    return value


def product_of_powers(values: list[int], exponents: list[int], modulus: int) -> int:
    result = 1
    for value, exponent in zip(values, exponents, strict=True):
        result = result * pow(value, exponent, modulus) % modulus
    return result


def certify(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    exponent_modulus, rows, rhs_values = parse_payload(
        {"modulus": payload.get("exponent_modulus"), "relations": payload.get("relations")}
    )
    group_modulus = integer(payload.get("group_modulus"), "group_modulus")
    if group_modulus < 2:
        raise ValueError("group_modulus must be at least 2")
    generator = unit(payload.get("generator"), group_modulus, "generator")
    raw_elements = payload.get("elements")
    if not isinstance(raw_elements, list) or len(raw_elements) != len(rows[0]):
        raise ValueError("elements must be a list with one unit for every relation column")
    elements = [unit(value, group_modulus, f"elements[{position}]")
                for position, value in enumerate(raw_elements)]
    torsion_values = [generator, *elements]
    torsion_residuals = [pow(value, exponent_modulus, group_modulus)
                         for value in torsion_values]
    if any(value != 1 for value in torsion_residuals):
        raise ValueError("generator and every element must satisfy x^exponent_modulus = 1")
    relation_residuals = [
        product_of_powers(elements, row, group_modulus)
        * pow(generator, -rhs, group_modulus) % group_modulus
        for row, rhs in zip(rows, rhs_values, strict=True)
    ]
    if any(value != 1 for value in relation_residuals):
        return {
            "status": "relation_mismatch",
            "certified": False,
            "relation_residuals": relation_residuals,
            "scope": "A supplied relation fails in the specified finite unit group.",
        }
    system = check_system(exponent_modulus, rows, rhs_values)
    if not system["certified"]:
        return {"group_modulus": group_modulus, "exponent_modulus": exponent_modulus, **system}
    exponents = system["solution"]
    conclusion_residuals = [
        element * pow(generator, -exponent, group_modulus) % group_modulus
        for element, exponent in zip(elements, exponents, strict=True)
    ]
    if any(value != 1 for value in conclusion_residuals):
        raise AssertionError("full-span relation algebra did not replay in the supplied group")
    return {
        "status": "certified_cyclic_relations",
        "certified": True,
        "group_modulus": group_modulus,
        "exponent_modulus": exponent_modulus,
        "relation_count": len(rows),
        "element_exponents": exponents,
        "relation_residuals": relation_residuals,
        "conclusion_residuals": conclusion_residuals,
        "scope": "Only the supplied finite unit group and relation matrix. This does not find a discrete logarithm or certify any descent or complexity bound.",
    }


def run_file(path: Path) -> dict[str, object]:
    return certify(json.loads(path.read_text(encoding="utf-8")))


def self_test() -> None:
    positive = certify({
        "group_modulus": 17,
        "exponent_modulus": 16,
        "generator": 3,
        "elements": [5, 10],
        "relations": [
            {"coefficients": [2, 3], "rhs": 3},
            {"coefficients": [1, 1], "rhs": 8},
        ],
    })
    assert positive["certified"] and positive["element_exponents"] == [5, 3]
    bad_relation = certify({
        "group_modulus": 17,
        "exponent_modulus": 16,
        "generator": 3,
        "elements": [5, 10],
        "relations": [{"coefficients": [2, 3], "rhs": 4}, {"coefficients": [1, 1], "rhs": 8}],
    })
    assert bad_relation["status"] == "relation_mismatch"
    underdetermined = certify({
        "group_modulus": 17,
        "exponent_modulus": 16,
        "generator": 3,
        "elements": [5, 10],
        "relations": [{"coefficients": [1, 1], "rhs": 8}],
    })
    assert underdetermined["status"] == "underdetermined"
    print("self_test=passed; full_span=certified; bad_relation=rejected; underdetermined=rejected")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    arguments = parser.parse_args()
    if arguments.self_test:
        self_test()
    if arguments.input is None:
        if arguments.self_test:
            return 0
        parser.error("provide an input JSON file or --self-test")
    try:
        result = run_file(arguments.input)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["certified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
