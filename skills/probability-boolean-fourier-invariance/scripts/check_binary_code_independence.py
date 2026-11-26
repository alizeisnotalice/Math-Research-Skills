#!/usr/bin/env python3
"""Certify low-order uniform marginals of an explicitly generated binary linear code."""

from __future__ import annotations

import argparse
from functools import reduce
from itertools import combinations
import json
from operator import xor
from pathlib import Path


def certify(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    generator = payload.get("generator_rows")
    if not isinstance(generator, list) or not generator or not all(isinstance(row, list) for row in generator):
        raise ValueError("generator_rows must be a nonempty binary matrix")
    n = len(generator[0])
    if n < 1 or any(len(row) != n or any(type(bit) is not int or bit not in (0, 1) for bit in row)
                    for row in generator):
        raise ValueError("generator_rows must be a rectangular matrix of 0 and 1")
    order = payload.get("max_order")
    if type(order) is not int or not 1 <= order <= n:
        raise ValueError("max_order must be an integer between 1 and the number of columns")
    columns = [sum(bit << i for i, bit in enumerate(column)) for column in zip(*generator, strict=True)]
    checked = 0
    for weight in range(1, order + 1):
        for support in combinations(range(n), weight):
            checked += 1
            if reduce(xor, (columns[i] for i in support), 0) == 0:
                return {
                    "status": "nonuniform_marginal",
                    "requested_order": order,
                    "subsets_checked": checked,
                    "dual_distance": weight,
                    "witness_support": list(support),
                    "marginal_constraint": "the XOR of the witness coordinates is always zero",
                }
    return {
        "status": "certified_uniform_marginals",
        "requested_order": order,
        "subsets_checked": checked,
        "dual_distance_lower_bound": order + 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "certified_uniform_marginals" else 1


if __name__ == "__main__":
    raise SystemExit(main())
