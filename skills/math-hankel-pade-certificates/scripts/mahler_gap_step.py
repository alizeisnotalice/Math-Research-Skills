#!/usr/bin/env python3
"""Exact finite propagation for one homogeneous Mahler continued-fraction gap.

It implements only the algebra in Badziahin's gap recurrence.  The caller must
separately establish that p/q is a convergent of a Laurent-series solution and
that [u, v] is its actual gap.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


Polynomial = list[Fraction]  # ascending coefficients


def fraction(value: object) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean is not a rational coefficient")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational coefficient {value!r}")


def display(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def trim(poly: Polynomial) -> Polynomial:
    output = poly[:]
    while output and output[-1] == 0:
        output.pop()
    return output


def degree(poly: Polynomial) -> int:
    reduced = trim(poly)
    if not reduced:
        raise ValueError("zero polynomial has no degree")
    return len(reduced) - 1


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return trim(result)


def substitute_power(poly: Polynomial, d: int) -> Polynomial:
    result = [Fraction(0) for _ in range(degree(poly) * d + 1)]
    for index, value in enumerate(poly):
        result[index * d] = value
    return trim(result)


def divide_with_remainder(numerator: Polynomial, denominator: Polynomial) -> tuple[Polynomial, Polynomial]:
    work = trim(numerator)
    denominator = trim(denominator)
    if not denominator:
        raise ValueError("division by the zero polynomial")
    quotient = [Fraction(0) for _ in range(max(0, degree(work) - degree(denominator)) + 1)]
    while work and degree(work) >= degree(denominator):
        shift = degree(work) - degree(denominator)
        coefficient = work[-1] / denominator[-1]
        quotient[shift] += coefficient
        for j, value in enumerate(denominator):
            work[j + shift] -= coefficient * value
        work = trim(work)
    return trim(quotient), work


def monic_gcd(left: Polynomial, right: Polynomial) -> Polynomial:
    left, right = trim(left), trim(right)
    while right:
        _, remainder = divide_with_remainder(left, right)
        left, right = right, remainder
    if not left:
        raise ValueError("gcd(0, 0) is undefined")
    return [value / left[-1] for value in left]


def exact_divide(numerator: Polynomial, denominator: Polynomial) -> Polynomial:
    quotient, remainder = divide_with_remainder(numerator, denominator)
    if remainder:
        raise AssertionError("expected an exact polynomial division")
    return quotient


def as_poly(raw: object, name: str) -> Polynomial:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"{name} must be a nonempty ascending-coefficient list")
    parsed = trim([fraction(value) for value in raw])
    if not parsed:
        raise ValueError(f"{name} must be nonzero")
    return parsed


def encode(poly: Polynomial) -> list[str]:
    return [display(value) for value in trim(poly)]


def certificate(raw: dict[str, object]) -> dict[str, object]:
    d = raw.get("d")
    if type(d) is not int or d < 2:
        raise ValueError("d must be an integer at least 2")
    a = as_poly(raw.get("A"), "A")
    b = as_poly(raw.get("B"), "B")
    p = as_poly(raw.get("p"), "p")
    q = as_poly(raw.get("q"), "q")
    if degree(monic_gcd(p, q)) != 0:
        raise ValueError("p and q must be coprime over Q")
    gap = raw.get("gap")
    if not isinstance(gap, dict):
        raise ValueError("gap must be an object with integer u and v")
    u, v = gap.get("u"), gap.get("v")
    if type(u) is not int or type(v) is not int or u < 0 or v <= u:
        raise ValueError("gap requires integers 0 <= u < v")
    if degree(q) != u:
        raise ValueError("gap.u must equal deg(q)")

    numerator_before = multiply(a, substitute_power(p, d))
    denominator_before = multiply(b, substitute_power(q, d))
    common = monic_gcd(numerator_before, denominator_before)
    next_p = exact_divide(numerator_before, common)
    next_q = exact_divide(denominator_before, common)
    r_a, r_b, r_c = degree(a), degree(b), degree(common)
    next_u = d * u + r_b - r_c
    next_v = d * v + r_c - r_a
    if degree(next_q) != next_u:
        raise AssertionError("denominator-degree recurrence failed")
    if degree(monic_gcd(next_p, next_q)) != 0:
        raise AssertionError("reduced propagated numerator and denominator are not coprime")
    big_threshold_numerator = r_a + r_b
    is_big = (d - 1) * (v - u) > big_threshold_numerator
    growth = next_v - next_u
    output: dict[str, object] = {
        "arithmetic": "exact fractions.Fraction arithmetic over Q[z]",
        "input_gap": {"u": u, "v": v, "size": v - u},
        "degrees": {"deg_A": r_a, "deg_B": r_b, "deg_common_factor": r_c},
        "common_factor_monic_low_to_high": encode(common),
        "next_numerator_low_to_high": encode(next_p),
        "next_denominator_low_to_high": encode(next_q),
        "next_gap": {"u": next_u, "v": next_v, "size": growth},
        "recurrence_checked": {
            "u_next": "d*u + deg(B) - deg(C)",
            "v_next": "d*v + deg(C) - deg(A)",
            "finite_big_gap_condition": "(d-1)*(v-u) > deg(A)+deg(B)",
            "condition_holds": is_big,
            "strict_size_growth": growth > v - u,
        },
        "scope": (
            "This verifies the finite rational-polynomial update. It does not prove that the input "
            "fraction is a convergent, that the supplied endpoints are a genuine gap, eventual "
            "periodicity of cancellations, nonvanishing at b^(d^m), irrationality, or an "
            "irrationality exponent."
        ),
    }
    expected = raw.get("expected_next_gap")
    if expected is not None:
        if not isinstance(expected, dict) or expected.get("u") != next_u or expected.get("v") != next_v:
            raise AssertionError("expected_next_gap does not match the exact recurrence")
        output["expected_next_gap_checked"] = True
    return output


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} INPUT.json", file=sys.stderr)
        return 2
    try:
        raw = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("top-level JSON must be an object")
        print(json.dumps(certificate(raw), ensure_ascii=False, indent=2))
        return 0
    except (OSError, TypeError, ValueError, AssertionError) as error:
        print(f"input error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
