#!/usr/bin/env python3
"""Exact Hamming-weight certificate for a Boolean ANF polynomial."""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import sys


def normalize(variables: int, monomials: list[list[int]]) -> list[frozenset[int]]:
    if type(variables) is not int or variables < 0:
        raise ValueError("variables must be a nonnegative integer")
    parity: set[frozenset[int]] = set()
    for monomial in monomials:
        if not isinstance(monomial, list) or any(type(item) is not int or not 1 <= item <= variables for item in monomial):
            raise ValueError("each monomial must be a list of variable indices")
        subset = frozenset(monomial)
        if len(subset) != len(monomial):
            raise ValueError("a monomial must be square-free")
        if subset in parity:
            parity.remove(subset)
        else:
            parity.add(subset)
    return sorted(parity, key=lambda value: (len(value), tuple(sorted(value))))


def formula_weight(variables: int, monomials: list[frozenset[int]]) -> int:
    total = 0
    for size in range(1, len(monomials) + 1):
        for chosen in combinations(monomials, size):
            union = frozenset().union(*chosen)
            total += (-2) ** (size - 1) * 2 ** (variables - len(union))
    return total


def table_weight(variables: int, monomials: list[frozenset[int]]) -> int:
    total = 0
    for point in range(1 << variables):
        value = 0
        for monomial in monomials:
            value ^= all((point >> (index - 1)) & 1 for index in monomial)
        total += value
    return total


def check(payload: dict[str, object]) -> dict[str, object]:
    variables = payload.get("variables")
    monomials = payload.get("monomials")
    if not isinstance(monomials, list):
        raise ValueError("monomials must be a list")
    normalized = normalize(variables, monomials)
    formula = formula_weight(variables, normalized)
    result: dict[str, object] = {
        "variables": variables,
        "monomials_after_cancellation": [sorted(item) for item in normalized],
        "maximum_degree": max(map(len, normalized), default=0),
        "formula_weight": formula,
    }
    if variables <= 20:
        enumerated = table_weight(variables, normalized)
        result["truth_table_weight"] = enumerated
        result["formula_matches_truth_table"] = formula == enumerated
    return result


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_anf_weight.py INPUT.json")
    print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
