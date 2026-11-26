#!/usr/bin/env python3
"""Exact finite audit of q-term support sums for a sparse binary expansion."""
import itertools
import json
import math
import sys
from collections import Counter


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    exponents = [int(x) for x in data["exponents"]]
    q = int(data["q"])
    if q < 1 or any(a < 0 for a in exponents) or exponents != sorted(set(exponents)):
        raise ValueError("exponents must be distinct increasing nonnegative integers and q positive")
    counts = Counter()
    for size in range(1, q + 1):
        for term in itertools.product(exponents, repeat=size):
            counts[sum(term)] += 1
    sums = sorted(counts)
    gaps = [right - left for left, right in zip(sums, sums[1:])]
    answer = {
        "finite_exponent_count": len(exponents),
        "max_ordered_representation_count": max(counts.values(), default=0),
        "observed_gap_maximum": max(gaps, default=None),
        "ordered_representation_bound_q_factorial_squared": math.factorial(q) ** 2,
        "q": q,
        "representable_sums": sums,
        "scope": "Exact finite enumeration only. It does not prove the source's global sparse-and-thin hypotheses or transcendence."
    }
    print(json.dumps(answer, indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: sparse_exponent_support_audit.py INPUT.json")
    main(sys.argv[1])
