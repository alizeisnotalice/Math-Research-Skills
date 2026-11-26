#!/usr/bin/env python3
"""Check the finite-magma instance of the one-occurrence constancy rewrite."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path
import sys


def variables(term):
    if isinstance(term, str):
        return {term}
    if set(term) != {"op"} or not isinstance(term["op"], list) or len(term["op"]) != 2:
        raise ValueError("a compound term must be {'op': [left, right]}")
    return variables(term["op"][0]) | variables(term["op"][1])


def evaluate(term, assignment, table):
    if isinstance(term, str):
        return assignment[term]
    left, right = term["op"]
    return table[evaluate(left, assignment, table)][evaluate(right, assignment, table)]


def check(data):
    table = data["table"]
    size = len(table)
    if size == 0 or any(len(row) != size for row in table):
        raise ValueError("table must be a nonempty square array")
    if any(type(value) is not int or not 0 <= value < size for row in table for value in row):
        raise ValueError("table entries must be element indices")
    left, right, varied = data["s"], data["t"], data["variable"]
    left_variables, right_variables = variables(left), variables(right)
    if varied in left_variables or varied not in right_variables:
        raise ValueError("variable must occur in t and not in s")
    all_variables = sorted(left_variables | right_variables)
    for values in product(range(size), repeat=len(all_variables)):
        assignment = dict(zip(all_variables, values))
        if evaluate(left, assignment, table) != evaluate(right, assignment, table):
            raise ValueError("the supplied equation does not hold in this magma")
    other_variables = [name for name in all_variables if name != varied]
    checks = 0
    for values in product(range(size), repeat=len(other_variables)):
        assignment = dict(zip(other_variables, values))
        image = {evaluate(right, assignment | {varied: value}, table) for value in range(size)}
        checks += 1
        if len(image) != 1:
            raise AssertionError("valid equation failed its constancy consequence")
    return {"magma_size": size, "variable": varied, "fixed_other_assignments": checks,
            "constant_under_varied_variable": True}


if __name__ == "__main__":
    try:
        source = Path(sys.argv[1])
        print(json.dumps(check(json.loads(source.read_text())), ensure_ascii=False))
    except (IndexError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
