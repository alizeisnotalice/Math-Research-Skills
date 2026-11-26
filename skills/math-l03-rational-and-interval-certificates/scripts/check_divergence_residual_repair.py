#!/usr/bin/env python3
"""Exact one-dimensional verification of a supplied divergence-form residual repair."""

from __future__ import annotations

import argparse
import json
import sys
from math import comb

import sympy as sp


x, t = sp.symbols("x t", real=True)


def rational(value: object) -> sp.Rational:
    if type(value) in (int, str):
        return sp.Rational(value)
    raise ValueError("all scalar inputs and polynomial coefficients must be exact integers or rationals")


def polynomial(values: object, label: str) -> sp.Expr:
    if not isinstance(values, list) or not values:
        raise ValueError(f"{label} must be a nonempty coefficient list")
    return sum((rational(value) * x**power for power, value in enumerate(values)), sp.Integer(0))


def bernstein_coefficients(expression: sp.Expr, left: sp.Rational, right: sp.Rational) -> list[sp.Rational]:
    local = sp.Poly(sp.expand(expression.subs(x, left + (right - left) * t)), t)
    degree = local.degree()
    if degree < 0:
        return [sp.Rational(0)]
    monomial = [sp.Rational(local.nth(power)) for power in range(degree + 1)]
    return [
        sum((monomial[power] * sp.Rational(comb(index, power), comb(degree, power))
             for power in range(index + 1)), sp.Rational(0))
        for index in range(degree + 1)
    ]


def strict_bernstein_sign(expression: sp.Expr, left: sp.Rational, right: sp.Rational) -> tuple[str, list[sp.Rational]]:
    coefficients = bernstein_coefficients(expression, left, right)
    if all(value > 0 for value in coefficients):
        return "positive", coefficients
    if all(value < 0 for value in coefficients):
        return "negative", coefficients
    raise ValueError("Bernstein enclosure does not certify a strict sign on the requested interval")


def positive_rational(expression: sp.Expr, label: str, left: sp.Rational, right: sp.Rational) -> dict[str, object]:
    numerator, denominator = map(sp.expand, sp.fraction(sp.cancel(expression)))
    numerator_sign, numerator_coefficients = strict_bernstein_sign(numerator, left, right)
    denominator_sign, denominator_coefficients = strict_bernstein_sign(denominator, left, right)
    if numerator_sign != denominator_sign:
        raise ValueError(f"{label} is not certified positive on the requested interval")
    return {
        "label": label,
        "numerator_bernstein": [str(value) for value in numerator_coefficients],
        "denominator_bernstein": [str(value) for value in denominator_coefficients],
    }


def certify(data: object) -> dict[str, object]:
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    if data.get("operator") != "d(A u') + k^2 rho u = 0":
        raise ValueError("operator must be exactly d(A u') + k^2 rho u = 0")
    left, right = rational(data["left"]), rational(data["right"])
    if not left < right:
        raise ValueError("left must be strictly smaller than right")
    k = rational(data["k"])
    if k <= 0:
        raise ValueError("k must be positive")
    A = polynomial(data["A"], "A")
    rho = polynomial(data["rho"], "rho")
    inverse_metric = polynomial(data["inverse_metric"], "inverse_metric")
    u = polynomial(data["u"], "u")
    residual = sp.expand(sp.diff(A * sp.diff(u, x), x) + k**2 * rho * u)
    first_jet = sp.expand(u**2 + inverse_metric * sp.diff(u, x)**2)
    positivity = [
        positive_rational(A, "A", left, right),
        positive_rational(rho, "rho", left, right),
        positive_rational(inverse_metric, "inverse_metric", left, right),
        positive_rational(first_jet, "D = u^2 + I (u')^2", left, right),
    ]
    F = sp.cancel(-residual / first_jet)
    delta_A = sp.cancel(F * u * inverse_metric)
    delta_rho = sp.cancel((F * u - sp.diff(F * inverse_metric * sp.diff(u, x), x)) / k**2)
    corrected_A = sp.cancel(A + delta_A)
    corrected_rho = sp.cancel(rho + delta_rho)
    corrected_residual = sp.cancel(
        sp.diff(corrected_A * sp.diff(u, x), x) + k**2 * corrected_rho * u
    )
    if corrected_residual != 0:
        raise ValueError(f"corrected residual is not identically zero: {corrected_residual}")
    positivity.extend([
        positive_rational(corrected_A, "A + delta_A", left, right),
        positive_rational(corrected_rho, "rho + delta_rho", left, right),
    ])
    return {
        "status": "PASS",
        "interval": [str(left), str(right)],
        "initial_residual": str(residual),
        "F": str(F),
        "delta_A": str(delta_A),
        "delta_rho": str(delta_rho),
        "corrected_residual": "0",
        "strict_positivity_certificates": positivity,
        "scope": (
            "This is an exact one-dimensional coordinate-chart identity with dx volume. "
            "It does not supply derivative-size estimates, construct an input residual, or prove a global nodal result."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON certificate input")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as handle:
            result = certify(json.load(handle))
    except (OSError, KeyError, TypeError, ValueError, ZeroDivisionError, sp.PolynomialError) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
