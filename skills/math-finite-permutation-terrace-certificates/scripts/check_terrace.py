#!/usr/bin/env python3
"""Verify an explicit directed terrace for the alternating group A_n."""
import json
import math
import sys
from collections import Counter
from pathlib import Path


def compose(left, right):
    """Return left o right for image-list permutations."""
    return tuple(left[index] for index in right)


def inverse(permutation):
    answer = [0] * len(permutation)
    for index, image in enumerate(permutation):
        answer[image] = index
    return tuple(answer)


def is_even(permutation):
    return sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    ) % 2 == 0


def main(path):
    payload = json.loads(Path(path).read_text())
    degree = payload["degree"]
    rows = [tuple(row) for row in payload["rows"]]
    if not isinstance(degree, int) or degree < 3:
        raise ValueError("degree must be an integer at least 3")
    expected_size = math.factorial(degree) // 2
    if len(rows) != expected_size:
        raise ValueError(f"expected {expected_size} rows, got {len(rows)}")
    if any(sorted(row) != list(range(degree)) for row in rows):
        raise ValueError("every row must be a permutation of 0,...,degree-1")
    if any(not is_even(row) for row in rows):
        raise ValueError("every row must be even")
    if len(set(rows)) != expected_size:
        raise ValueError("rows must be distinct")
    identity = tuple(range(degree))
    if rows[0] != identity:
        raise ValueError("the first row must be the identity")

    quotient_counts = Counter(
        compose(inverse(left), right) for left, right in zip(rows, rows[1:])
    )
    for group_element in rows[1:]:
        inverse_element = inverse(group_element)
        total = quotient_counts[group_element]
        if group_element != inverse_element:
            total += quotient_counts[inverse_element]
        expected = 1 if group_element == inverse_element else 2
        if total != expected:
            raise ValueError(
                "terrace quotient count failed for "
                f"{list(group_element)}: got {total}, expected {expected}"
            )
    print(json.dumps({
        "degree": degree,
        "group": f"A_{degree}",
        "rows": len(rows),
        "consecutive_quotients": len(rows) - 1,
        "status": "verified",
    }, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_terrace.py INPUT.json")
    main(sys.argv[1])
