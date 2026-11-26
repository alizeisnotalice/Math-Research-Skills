#!/usr/bin/env python3
"""Check finite binomial-transform divisibility for integer sequence data."""

from __future__ import annotations

from math import comb
import json
from pathlib import Path
import sys


def primes_to(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


def check(data: dict[str, object]) -> dict[str, object]:
    values = data.get("values")
    if not isinstance(values, list) or not values or any(type(value) is not int for value in values):
        raise ValueError("values must be a nonempty list of integers")
    transforms = [sum(((-1) ** (index - k)) * comb(index, k) * values[k]
                      for k in range(index + 1)) for index in range(len(values))]
    product = 1
    rows = []
    prime_set = set(primes_to(len(values) - 1))
    for index, value in enumerate(transforms):
        if index in prime_set:
            product *= index
        rows.append({"n": index, "P_n": product, "binomial_transform": value,
                     "divisible": value % product == 0})
    return {"checked_prefix_length": len(values), "rows": rows,
            "prefix_divisibility_holds": all(row["divisible"] for row in rows),
            "scope": "finite prefix only; an all-index proof is required for a primary pseudo-polynomial conclusion"}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_primary_pseudopolynomial.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
