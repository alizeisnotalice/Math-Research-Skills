#!/usr/bin/env python3
"""Exact finite certificate for even-k paired-basis reflection in the count LP.

The input names an interior Bernoulli parameter and a paired basis
I = J union {n}.  It solves the binomial moment equations over Fraction,
checks the reflected weights at 1-p, and certifies the finite dual polynomial
Q_I on the integer count set {0,...,n}.  It is deliberately a finite checker:
it does not search for bases or settle endpoint, ordering, odd-k, or
objective-value symmetry claims.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path


class InputError(ValueError):
    """An input lies outside the stated paired-basis interface."""


def fraction(value: object) -> Fraction:
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as error:
        raise InputError(f"not a rational number: {value!r}") from error


def solve_square(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """Exact Gaussian elimination for a nonsingular square system."""
    size = len(rhs)
    augmented = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot is None:
            raise InputError("basis evaluation matrix is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            scale = augmented[row][column]
            if scale:
                augmented[row] = [entry - scale * pivot_entry for entry, pivot_entry in zip(augmented[row], augmented[column])]
    return [augmented[row][-1] for row in range(size)]


def moment_weights(n: int, k: int, p: Fraction, basis: list[int]) -> dict[int, Fraction]:
    matrix = [[Fraction(comb(node, r)) for node in basis] for r in range(k + 1)]
    target = [Fraction(comb(n, r)) * p**r for r in range(k + 1)]
    solution = solve_square(matrix, target)
    weights = dict(zip(basis, solution))
    for r in range(k + 1):
        actual = sum(weights[node] * comb(node, r) for node in basis)
        if actual != target[r]:
            raise AssertionError("exact moment replay failed")
    return weights


def validate(data: dict[str, object]) -> tuple[int, int, Fraction, list[tuple[int, int]]]:
    required = {"n", "k", "p", "pairs"}
    missing = sorted(required - set(data))
    if missing:
        raise InputError(f"missing fields: {', '.join(missing)}")
    n, k = data["n"], data["k"]
    if not isinstance(n, int) or not isinstance(k, int):
        raise InputError("n and k must be integers")
    if not (2 <= k <= n - 1):
        raise InputError("require 2 <= k <= n-1")
    if k % 2:
        raise InputError("this finite reflection interface requires even k")
    p = fraction(data["p"])
    if not 0 < p < 1:
        raise InputError("require interior rational p with 0 < p < 1")
    raw_pairs = data["pairs"]
    if not isinstance(raw_pairs, list) or len(raw_pairs) != k // 2:
        raise InputError("pairs must contain exactly k/2 adjacent pairs")
    pairs: list[tuple[int, int]] = []
    for pair in raw_pairs:
        if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(node, int) for node in pair):
            raise InputError("every pair must be a two-integer list")
        left, right = pair
        if right != left + 1:
            raise InputError("each supplied pair must be adjacent")
        if not (0 <= left < right <= n - 1):
            raise InputError("paired nodes must lie in {0,...,n-1}; endpoint n is fixed separately")
        pairs.append((left, right))
    pairs.sort()
    if any(pairs[index][1] >= pairs[index + 1][0] for index in range(len(pairs) - 1)):
        raise InputError("adjacent pairs must be disjoint and separated in the basis ordering")
    return n, k, p, pairs


def dual_values(n: int, pairs: list[tuple[int, int]]) -> dict[int, Fraction]:
    denominator = 1
    for left, right in pairs:
        denominator *= (n - left) * (n - right)
    values: dict[int, Fraction] = {}
    for x in range(n + 1):
        numerator = 1
        for left, right in pairs:
            numerator *= (x - left) * (x - right)
        values[x] = Fraction(numerator, denominator)
        if x == n:
            if values[x] != 1:
                raise AssertionError("dual endpoint normalization failed")
        elif values[x] < 0:
            raise AssertionError("paired dual polynomial is negative on a count node")
    return values


def render(weights: dict[int, Fraction]) -> dict[str, str]:
    return {str(node): str(weights[node]) for node in sorted(weights)}


def certificate(data: dict[str, object]) -> dict[str, object]:
    n, k, p, pairs = validate(data)
    original_j = [node for pair in pairs for node in pair]
    original_basis = original_j + [n]
    reflected_pairs = sorted((n - 1 - right, n - 1 - left) for left, right in pairs)
    reflected_j = [node for pair in reflected_pairs for node in pair]
    reflected_basis = reflected_j + [n]
    original = moment_weights(n, k, p, original_basis)
    reflected = moment_weights(n, k, 1 - p, reflected_basis)
    for node in original_j:
        star = n - 1 - node
        multiplier = p * (n - node) / ((1 - p) * (node + 1))
        if reflected[star] != multiplier * original[node]:
            raise AssertionError("exact reflected-weight identity failed")
    if any(weight < 0 for weight in original.values()) or any(weight < 0 for weight in reflected.values()):
        raise InputError("the supplied paired basis is not feasible at p and 1-p")
    original_dual = dual_values(n, pairs)
    reflected_dual = dual_values(n, reflected_pairs)
    return {
        "status": "certified-finite-interior-reflection",
        "scope": "exact count-LP certificate for the supplied even-k paired bases only",
        "n": n,
        "k": k,
        "p": str(p),
        "reflected_p": str(1 - p),
        "basis": original_basis,
        "reflected_basis": reflected_basis,
        "weights": render(original),
        "reflected_weights": render(reflected),
        "reflection_multiplier": "p*(n-s)/((1-p)*(s+1))",
        "moment_identities": "passed exactly for r=0,...,k on both bases",
        "dual_nonnegative_count_nodes": list(range(n + 1)),
        "finite_optimality_certificate": "Q_I and Q_I* are nonnegative off their endpoint and equal 1 at n; each feasible basic distribution therefore attains its dual upper bound.",
        "not_certified": ["endpoint reflection", "objective-value equality", "basis ordering or connectedness", "odd-k bases", "automatic basis search"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with n, k, p, and adjacent pairs")
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            raise InputError("top-level JSON value must be an object")
        print(json.dumps(certificate(data), indent=2, sort_keys=True))
    except (InputError, json.JSONDecodeError) as error:
        print(f"rejected: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
