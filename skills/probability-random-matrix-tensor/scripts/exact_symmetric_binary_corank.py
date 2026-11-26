#!/usr/bin/env python3
"""Exact finite evaluator for the symmetric two-atom corank-tail certificate.

It enumerates the product distribution of a rational symmetric matrix A with
independent identically distributed upper-triangular entries in two distinct
rational values, then adds a fixed symmetric rational offset H.  It reports
the exact probability that corank_Q(A+H) is at least k and the source bound
  sum_{j=k}^n binom(n,j) b^(j(j+1)/2),
where b is the larger atom probability.  Enumeration is deliberately capped
at n<=5.  This checks one finite product model; it is not a sharp-rate tool.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


MAX_ENUMERATION_DIMENSION = 5


def q(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numeric inputs must be exact integers or rational strings; floats are forbidden")
    if isinstance(value, (str, int)):
        return Fraction(value)
    raise ValueError(f"not an exact rational: {value!r}")


def matrix(raw: Any, n: int, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or len(raw) != n:
        raise ValueError(f"{name} must be a {n}-by-{n} list")
    answer = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"{name}[{i}] must have length {n}")
        answer.append([q(value) for value in row])
    for i in range(n):
        for j in range(n):
            if answer[i][j] != answer[j][i]:
                raise ValueError(f"{name} is not symmetric at ({i},{j})")
    return answer


def rank(a: list[list[Fraction]]) -> int:
    work = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        for row in range(pivot_row + 1, len(work)):
            factor = work[row][col] / pivot_value
            for right in range(col, len(work[0])):
                work[row][right] -= factor * work[pivot_row][right]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def make_matrix(offset: list[list[Fraction]], choices: tuple[int, ...], values: list[Fraction]) -> list[list[Fraction]]:
    n = len(offset)
    answer = [row[:] for row in offset]
    position = 0
    for i in range(n):
        for j in range(i, n):
            value = values[choices[position]]
            position += 1
            answer[i][j] += value
            if i != j:
                answer[j][i] += value
    return answer


def probability_of_choice(choices: tuple[int, ...], probabilities: list[Fraction]) -> Fraction:
    answer = Fraction(1)
    for choice in choices:
        answer *= probabilities[choice]
    return answer


def tail_bound(n: int, k: int, b: Fraction) -> Fraction:
    return sum((Fraction(math.comb(n, j)) * b ** (j * (j + 1) // 2) for j in range(k, n + 1)), Fraction(0))


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    n = payload.get("n")
    k = payload.get("corank_at_least")
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    if n > MAX_ENUMERATION_DIMENSION:
        raise ValueError(f"exact enumeration is capped at n<={MAX_ENUMERATION_DIMENSION}")
    if not isinstance(k, int) or isinstance(k, bool) or not 1 <= k <= n:
        raise ValueError("corank_at_least must be an integer in [1,n]")
    distribution = payload.get("upper_triangle_product_distribution")
    if not isinstance(distribution, dict):
        raise ValueError("upper_triangle_product_distribution is required")
    raw_values = distribution.get("values")
    raw_probabilities = distribution.get("probabilities")
    if not isinstance(raw_values, list) or not isinstance(raw_probabilities, list) or len(raw_values) != 2 or len(raw_probabilities) != 2:
        raise ValueError("the finite component requires exactly two values and two probabilities")
    values = [q(value) for value in raw_values]
    probabilities = [q(value) for value in raw_probabilities]
    if values[0] == values[1]:
        raise ValueError("the two upper-triangular values must remain distinct over Q")
    if any(probability <= 0 for probability in probabilities) or sum(probabilities) != 1:
        raise ValueError("probabilities must be strictly positive exact rationals summing to 1")
    offset = matrix(payload.get("symmetric_offset"), n, "symmetric_offset")
    b = max(probabilities)
    coordinates = n * (n + 1) // 2
    actual_tail = Fraction(0)
    corank_law = [Fraction(0) for _ in range(n + 1)]
    for choices in itertools.product((0, 1), repeat=coordinates):
        probability = probability_of_choice(choices, probabilities)
        current_corank = n - rank(make_matrix(offset, choices, values))
        corank_law[current_corank] += probability
        if current_corank >= k:
            actual_tail += probability
    bound = tail_bound(n, k, b)
    if actual_tail > bound:
        raise AssertionError("enumerated model violates the stated principal-block corank bound")
    coarse_bound = Fraction(2**n) * b ** (k * (k + 1) // 2)
    return {
        "status": "verified-exact-finite-symmetric-corank-tail",
        "field": "Q",
        "n": n,
        "corank_at_least": k,
        "upper_triangle_coordinates": coordinates,
        "max_atom_probability_b": str(b),
        "exact_enumerated_tail_probability": str(actual_tail),
        "principal_block_union_bound": str(bound),
        "coarse_source_bound_2^n_b_power": str(coarse_bound),
        "corank_distribution": [str(value) for value in corank_law],
        "method": "exact enumeration of the stated independent product model plus rational Gaussian rank",
        "scope": "one finite symmetric two-atom product model over Q with the supplied fixed symmetric offset",
        "not_certified": "dependent entries, value collapse in another field, asymptotic sharp singularity rates, or arbitrary atom laws",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="exact product-model JSON")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        result = verify(payload)
    except (OSError, json.JSONDecodeError, ValueError, AssertionError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
