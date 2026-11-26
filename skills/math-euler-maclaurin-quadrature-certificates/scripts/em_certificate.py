#!/usr/bin/env python3
"""Exact finite Euler--Maclaurin certificate for rational polynomials.

Implements Eq. (2) and the endpoint-vanishing estimator of Theorem 3 in
Bailey--Borwein (2005).  The enclosure is conditional on the supplied rational
pi enclosure; this program deliberately does not validate that external fact.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


class CertificationError(ValueError):
    """Raised for an input outside the theorem's certified scope."""


def fraction(value: Any, name: str) -> Fraction:
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificationError(f"{name} is not a valid rational: {value!r}") from exc


def strict_integer(value: Any, name: str) -> int:
    """Accept a JSON integer or a base-10 integral string, never bool/float."""
    if isinstance(value, bool):
        raise CertificationError(f"{name} must be an integer, not a boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"[+-]?[0-9]+", value):
        return int(value)
    raise CertificationError(f"{name} must be an integer (nonintegral forms are rejected)")


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def derivative(poly: list[Fraction], times: int = 1) -> list[Fraction]:
    answer = poly[:]
    for _ in range(times):
        answer = [Fraction(i) * answer[i] for i in range(1, len(answer))]
        if not answer:
            return [Fraction(0)]
    return trim(answer)


def evaluate(poly: Iterable[Fraction], x: Fraction) -> Fraction:
    total = Fraction(0)
    for coefficient in reversed(list(poly)):
        total = total * x + coefficient
    return total


def integral(poly: list[Fraction], a: Fraction, b: Fraction) -> Fraction:
    return sum(
        coefficient * (b ** (power + 1) - a ** (power + 1)) / (power + 1)
        for power, coefficient in enumerate(poly)
    )


def bernoulli_even(order: int) -> Fraction:
    """Return B_order (order must be nonnegative and even) exactly."""
    if order < 0 or order % 2:
        raise ValueError("only nonnegative even Bernoulli numbers are needed")
    values: list[Fraction] = []
    for m in range(order + 1):
        values.append(Fraction(1, m + 1))
        for j in range(m, 0, -1):
            values[j - 1] = j * (values[j - 1] - values[j])
    return values[0]


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def closed_interval(center_coefficient: Fraction, power: int, radius_plain: Fraction,
                    radius_pi_coefficient: Fraction, pi_lower: Fraction,
                    pi_upper: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose c/pi**power +/- (r0+r1/pi**power), using a pi enclosure."""
    inv_low = Fraction(1, 1) / (pi_upper ** power)
    inv_high = Fraction(1, 1) / (pi_lower ** power)
    candidates = [center_coefficient * inv_low, center_coefficient * inv_high]
    central_low, central_high = min(candidates), max(candidates)
    radius_upper = radius_plain + radius_pi_coefficient * inv_high
    return central_low - radius_upper, central_high + radius_upper


def crude_l1_bound(poly: list[Fraction], a: Fraction, b: Fraction) -> Fraction:
    """A rational triangle-inequality bound for integral |poly| on [a,b]."""
    endpoint_radius = max(abs(a), abs(b))
    return (b - a) * sum(abs(c) * endpoint_radius ** degree for degree, c in enumerate(poly))


def certify(data: dict[str, Any]) -> dict[str, Any]:
    required = {"coefficients", "a", "b", "subintervals", "m", "n", "pi_lower", "pi_upper"}
    missing = sorted(required - data.keys())
    if missing:
        raise CertificationError("missing required field(s): " + ", ".join(missing))
    if not isinstance(data["coefficients"], list) or not data["coefficients"]:
        raise CertificationError("coefficients must be a nonempty low-to-high list")
    poly = trim([fraction(item, "coefficient") for item in data["coefficients"]])
    a, b = fraction(data["a"], "a"), fraction(data["b"], "b")
    if not a < b:
        raise CertificationError("require a < b")
    subintervals = strict_integer(data["subintervals"], "subintervals")
    m = strict_integer(data["m"], "m")
    n = strict_integer(data["n"], "n")
    if subintervals < 1 or m < 1 or n < 1:
        raise CertificationError("require subintervals >= 1 and m,n >= 1")
    pi_lower = fraction(data["pi_lower"], "pi_lower")
    pi_upper = fraction(data["pi_upper"], "pi_upper")
    if not (0 < pi_lower < pi_upper):
        raise CertificationError("require 0 < pi_lower < pi_upper")

    derivative_order = 2 * (m + n)
    current = poly
    endpoint_checks = []
    for order in range(derivative_order + 1):
        left, right = evaluate(current, a), evaluate(current, b)
        endpoint_checks.append({"order": order, "at_a": fstr(left), "at_b": fstr(right)})
        if left != 0 or right != 0:
            raise CertificationError(
                "Theorem 3 rejected: endpoint derivative order "
                f"{order} is not zero (a: {fstr(left)}, b: {fstr(right)})."
            )
        current = derivative(current)

    h = (b - a) / subintervals
    exact_integral = integral(poly, a, b)
    node_sum = sum(evaluate(poly, a + h * j) for j in range(subintervals + 1))
    trapezoid = h * node_sum - h * (evaluate(poly, a) + evaluate(poly, b)) / 2
    correction = Fraction(0)
    for i in range(1, m + 1):
        dpoly = derivative(poly, 2 * i - 1)
        correction += h ** (2 * i) * bernoulli_even(2 * i) * (
            evaluate(dpoly, b) - evaluate(dpoly, a)
        ) / math.factorial(2 * i)
    quadrature = trapezoid - correction
    exact_error = exact_integral - quadrature

    d2m = derivative(poly, 2 * m)
    sum_d2m = sum(evaluate(d2m, a + h * j) for j in range(subintervals + 1))
    central_coefficient = ((-1) ** (m - 1)) * h ** (2 * m + 1) * sum_d2m / (2 ** (2 * m))
    highest_derivative = derivative(poly, derivative_order)
    l1_upper = crude_l1_bound(highest_derivative, a, b)
    # From Theorem 3 after |I_k| <= L and |u+v| <= |u|+|v|:
    # 2(h/(2pi))^P [zeta(2n)+zeta(P)]L
    # = r0 + r1/pi^(2m), using zeta(2r)=|B_2r|(2pi)^(2r)/(2(2r)!).
    radius_plain = h ** derivative_order * abs(bernoulli_even(derivative_order)) * l1_upper / math.factorial(derivative_order)
    radius_pi_coefficient = (
        h ** derivative_order * abs(bernoulli_even(2 * n)) * l1_upper
        / (math.factorial(2 * n) * 2 ** (2 * m))
    )
    lower, upper = closed_interval(
        central_coefficient, 2 * m, radius_plain, radius_pi_coefficient, pi_lower, pi_upper
    )
    contains_exact = lower <= exact_error <= upper
    if not contains_exact:
        raise AssertionError("internal failure: exact polynomial error escaped the derived enclosure")

    return {
        "certificate_kind": "exact rational polynomial identity; interval conditional on supplied certified pi enclosure",
        "source": "Bailey--Borwein (2005), Eq. (2), Theorem 3; see references/certificate-format.md",
        "input": {
            "a": fstr(a), "b": fstr(b), "subintervals": subintervals, "m": m, "n": n,
            "coefficients_low_to_high": [fstr(c) for c in poly],
            "pi_enclosure_assumed": [fstr(pi_lower), fstr(pi_upper)],
        },
        "endpoint_checks": endpoint_checks,
        "exact_integral": fstr(exact_integral),
        "em_quadrature_Q_m": fstr(quadrature),
        "exact_error_E_h_m": fstr(exact_error),
        "theorem_3_E2": {"coefficient_over_pi_to_2m": fstr(central_coefficient), "power": 2 * m},
        "derivative_l1_upper": fstr(l1_upper),
        "remainder_radius_upper": {
            "constant_term": fstr(radius_plain),
            "coefficient_over_pi_to_2m": fstr(radius_pi_coefficient),
            "power": 2 * m,
        },
        "certified_error_interval": [fstr(lower), fstr(upper)],
        "exact_error_in_interval": contains_exact,
        "scope_note": "The interval requires the caller's independently certified pi enclosure; it is not a certificate for arbitrary non-polynomial integrands.",
    }


def positive_input() -> dict[str, Any]:
    return {
        "coefficients": ["0", "0", "0", "0", "0", "1", "-5", "10", "-10", "5", "-1"],
        "a": "0", "b": "1", "subintervals": 2, "m": 1, "n": 1,
        "pi_lower": "333/106", "pi_upper": "355/113",
    }


def self_test() -> dict[str, Any]:
    positive = certify(positive_input())
    rejected = False
    try:
        certify({
            "coefficients": ["0", "0", "1"], "a": "0", "b": "1", "subintervals": 1,
            "m": 1, "n": 1, "pi_lower": "333/106", "pi_upper": "355/113",
        })
    except CertificationError as exc:
        rejected = "endpoint derivative" in str(exc)
    integer_rejected = True
    for field, bad_value in (("subintervals", True), ("m", 1.5), ("n", "1.0")):
        malformed = positive_input()
        malformed[field] = bad_value
        try:
            certify(malformed)
        except CertificationError:
            continue
        integer_rejected = False
    if (not positive["exact_error_in_interval"] or not rejected or not integer_rejected
            or positive["theorem_3_E2"]["coefficient_over_pi_to_2m"] == "0"):
        raise AssertionError("self-test failed")
    return {
        "positive_case": "x^5(1-x)^5 on two cells accepted; nonzero E2 and exact error lie in conditional interval",
        "positive_exact_error": positive["exact_error_E_h_m"],
        "rejection_case": "x^2 rejected because its first endpoint derivative is nonzero",
        "integer_rejection": "bool, float, and decimal-string integer forms rejected",
        "passed": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="JSON certificate input")
    parser.add_argument("--self-test", action="store_true", help="run exact positive and rejection checks")
    args = parser.parse_args()
    if args.self_test == (args.input is not None):
        parser.error("supply exactly one of an input JSON file or --self-test")
    try:
        result = self_test() if args.self_test else certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (CertificationError, json.JSONDecodeError, OSError) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
