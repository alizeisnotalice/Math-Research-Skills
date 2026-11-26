#!/usr/bin/env python3
"""Exact finite coefficient/integrality replay for the Tschakaloff construction."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt


def beta_floor(n: int) -> int:
    """Return floor(n*(sqrt(5)-1)/2) using integer inequalities only."""
    target = 5 * n * n
    guess = max(0, (isqrt(target) - n) // 2)
    while (2 * (guess + 1) + n) ** 2 <= target:
        guess += 1
    while (2 * guess + n) ** 2 > target:
        guess -= 1
    return guess


def coefficient_list(n: int, q: Fraction) -> list[Fraction]:
    """Coefficients C_k in product_{j=1}^n (1-q^j T), in increasing T degree."""
    coefficients = [Fraction(1)]
    for j in range(1, n + 1):
        next_coefficients = [Fraction(0)] * (len(coefficients) + 1)
        for k, coefficient in enumerate(coefficients):
            next_coefficients[k] += coefficient
            next_coefficients[k + 1] -= coefficient * q**j
        coefficients = next_coefficients
    return coefficients


def audit(n: int, q1: int, q2: int, z1: int, z2: int) -> dict[str, object]:
    if n < 1:
        raise ValueError("n must be positive")
    if not all((q1, q2, z1, z2)):
        raise ValueError("q1, q2, z1, and z2 must be nonzero")
    q = Fraction(q1, q2)
    z = Fraction(z1, z2)
    if abs(q) <= 1:
        raise ValueError("the source construction's T_q regime requires |q| > 1")
    m = beta_floor(n)
    c = coefficient_list(n, q)
    degree_bound = n * (n + 1) // 2
    coefficient_scale = q2**degree_bound
    normalized_coefficients = [coefficient_scale * value for value in c]
    if not all(value.denominator == 1 for value in normalized_coefficients):
        raise AssertionError("equation (6) denominator inclusion failed")

    # Coefficients of T_q(z) and of the finite correction in source equation (8).
    b_raw = sum(
        z ** (-k) * c[k] * q ** (k * (k - 1) // 2 + k * m)
        for k in range(n + 1)
    )
    a_raw = sum(
        c[k]
        * sum(
            z ** (-(k - ell)) * q ** (k * (k - 1) // 2 + k * m - ell * (ell - 1) // 2)
            for ell in range(k + m + 1)
        )
        for k in range(n + 1)
    )
    scale = (
        z1**n
        * z2**m
        * q1 ** (m * (m - 1) // 2)
        * q2 ** (n * (n + 1) // 2 + n * (n - 1) // 2 + n * m)
    )
    a_scaled, b_scaled = scale * a_raw, scale * b_raw
    if a_scaled.denominator != 1 or b_scaled.denominator != 1:
        raise AssertionError("equations (9)--(10) finite integrality check failed")
    return {
        "n": n,
        "m": m,
        "q": [q.numerator, q.denominator],
        "z": [z.numerator, z.denominator],
        "degree_bound": degree_bound,
        "coefficient_denominators_cleared": True,
        "A_n": a_scaled.numerator,
        "B_n": b_scaled.numerator,
        "scaled_linear_form": "B_n*T_q(z)-A_n",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=4)
    parser.add_argument("--q1", type=int, default=2)
    parser.add_argument("--q2", type=int, default=1)
    parser.add_argument("--z1", type=int, default=3)
    parser.add_argument("--z2", type=int, default=1)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    result = audit(args.n, args.q1, args.q2, args.z1, args.z2)
    if args.self_test:
        try:
            audit(args.n, 1, 1, args.z1, args.z2)
        except ValueError:
            result["outside_convergence_boundary_rejected"] = True
        else:
            raise SystemExit("|q|=1 was incorrectly accepted")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
