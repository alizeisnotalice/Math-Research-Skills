#!/usr/bin/env python3
"""Exact finite sieve of an arithmetic-progression coordinate interval.

This is deliberately a finite, integer-only checker.  It counts coordinates
``j`` for which every selected prime avoids ``a + q*j``.  It does not test
whether ``a + q*j`` is prime and supplies no prime-distribution estimate.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def count_congruence(low: int, high: int, residue: int, modulus: int) -> int:
    """Count integers j with low < j <= high and j == residue (mod modulus)."""
    return (high - residue) // modulus - (low - residue) // modulus


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def mobius_for_squarefree_subset_size(size: int) -> int:
    return -1 if size % 2 else 1


def validate(data: dict) -> tuple[int, int, int, list[int]]:
    required = {"a", "q", "start_exclusive", "end_inclusive", "primes"}
    missing = sorted(required.difference(data))
    if missing:
        raise ValueError(f"missing keys: {', '.join(missing)}")
    a, q = int(data["a"]), int(data["q"])
    low, high = int(data["start_exclusive"]), int(data["end_inclusive"])
    primes = [int(p) for p in data["primes"]]
    if q <= 0 or low > high:
        raise ValueError("require q > 0 and start_exclusive <= end_inclusive")
    if math.gcd(a, q) != 1:
        raise ValueError("require gcd(a, q) = 1")
    if len(primes) != len(set(primes)) or not all(is_prime(p) for p in primes):
        raise ValueError("primes must be distinct primes")
    if any(q % p == 0 for p in primes):
        raise ValueError("every sieve prime must be coprime to q")
    return a, q, low, high, primes


def compute(data: dict) -> dict:
    a, q, low, high, primes = validate(data)
    period = product(primes)
    length = high - low
    roots = {p: (-a * pow(q, -1, p)) % p for p in primes}

    # Inclusion--exclusion: for d = product(T), r_d is the unique bad
    # coordinate modulo d because q is invertible modulo every d | period.
    inclusion_exclusion = 0
    terms = []
    for size in range(len(primes) + 1):
        for subset in combinations(primes, size):
            d = product(list(subset))
            residue = (-a * pow(q, -1, d)) % d
            count = count_congruence(low, high, residue, d)
            sign = mobius_for_squarefree_subset_size(size)
            inclusion_exclusion += sign * count
            terms.append({"d": d, "residue": residue, "sign": sign, "count": count})

    allowed_per_period = product([p - 1 for p in primes])
    expected = Fraction(length * allowed_per_period, period)
    result = {
        "input": {"a": a, "q": q, "start_exclusive": low, "end_inclusive": high, "primes": primes},
        "interval_length": length,
        "period": period,
        "bad_coordinate_residue_by_prime": roots,
        "allowed_residues_per_period": allowed_per_period,
        "inclusion_exclusion_survivors": inclusion_exclusion,
        "period_average": {"numerator": expected.numerator, "denominator": expected.denominator},
        "discrepancy_from_period_average": {
            "numerator": (Fraction(inclusion_exclusion) - expected).numerator,
            "denominator": (Fraction(inclusion_exclusion) - expected).denominator,
        },
        "inclusion_exclusion_error_bound": 2 ** len(primes),
        "inclusion_exclusion_terms": terms,
        "scope": "Counts only finite coordinate survivors; it neither detects nor estimates primes.",
    }

    # Independently materialize the finite set only when requested bounds make
    # it practical.  This validates both the formula and its implementation.
    materialization_limit = int(data.get("materialization_limit", 1_000_000))
    if length <= materialization_limit and period <= materialization_limit:
        direct = sum(all((a + q * j) % p != 0 for p in primes) for j in range(low + 1, high + 1))
        allowed_residues = [
            r for r in range(period)
            if all((a + q * r) % p != 0 for p in primes)
        ]
        residue_sum = sum(count_congruence(low, high, r, period) for r in allowed_residues)
        if direct != inclusion_exclusion or residue_sum != inclusion_exclusion:
            raise AssertionError("direct, residue-class, and inclusion--exclusion counts disagree")
        result["direct_coordinate_survivors"] = direct
        result["residue_class_sum_survivors"] = residue_sum
        result["materialized_allowed_residue_count"] = len(allowed_residues)
    else:
        result["materialization_skipped"] = "interval or period exceeds materialization_limit"
    expected_survivors = data.get("expected_survivors")
    if expected_survivors is not None and inclusion_exclusion != int(expected_survivors):
        raise AssertionError(f"expected {expected_survivors} survivors, got {inclusion_exclusion}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON input describing a finite coordinate interval")
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            result = compute(json.load(handle))
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
