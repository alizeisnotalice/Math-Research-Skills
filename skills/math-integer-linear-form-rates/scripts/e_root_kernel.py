#!/usr/bin/env python3
"""Exact formal Hermite--Pade kernel for the e^(1/n) construction.

The program checks only the polynomial/integral identities through degree L;
it does not certify integrality after scaling, a determinant, a common factor,
or a transcendence-measure estimate.
"""
from fractions import Fraction
from math import factorial, gcd
import json
import sys


def add(a, b):
    out = a[:]
    if len(out) < len(b):
        out += [Fraction(0)] * (len(b) - len(out))
    for i, x in enumerate(b):
        out[i] += x
    return out


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power_linear(alpha, exponent):
    out = [Fraction(1)]
    for _ in range(exponent):
        out = mul(out, [alpha, Fraction(-1)])
    return out


def shifted(poly, alpha):
    out = [Fraction(0)]
    for i, c in enumerate(poly):
        term = [Fraction(1)]
        for _ in range(i):
            term = mul(term, [alpha, Fraction(1)])
        out = add(out, [c * z for z in term])
    return out


def denom_lcm(values):
    d = 1
    for x in values:
        d = d * x.denominator // gcd(d, x.denominator)
    return d


def as_string(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def exp_times_poly(a0, alpha, limit):
    out = [Fraction(0)] * (limit + 1)
    for degree, coefficient in enumerate(a0):
        for r in range(limit - degree + 1):
            out[degree + r] += coefficient * alpha ** r / factorial(r)
    return out


def main():
    data = json.load(sys.stdin)
    n, k, ell = data["n"], data["k"], data["ell"]
    if not isinstance(n, int) or not isinstance(k, int) or n < 2 or k < n:
        raise ValueError("require integers k >= n >= 2")
    if not isinstance(ell, list) or len(ell) != k + 1 or any(not isinstance(x, int) or x < 1 for x in ell):
        raise ValueError("ell must contain k+1 positive integers")
    alphas = [Fraction(j, n) for j in range(k + 1)]
    omega = [Fraction(1)]
    for alpha, exponent in zip(alphas, ell):
        omega = mul(omega, power_linear(alpha, exponent))
    L = sum(ell)
    # A_0(t) = sum_i i! sigma_i t^(L-i).
    a0 = [Fraction(0)] * (L + 1)
    for i, sigma in enumerate(omega):
        a0[L - i] = factorial(i) * sigma
    aj_all, checks = [], []
    for j, alpha in enumerate(alphas):
        translated = shifted(omega, alpha)
        aj = [Fraction(0)] * (L + 1)
        for i, coefficient in enumerate(translated):
            aj[L - i] = factorial(i) * coefficient
        difference = exp_times_poly(a0, alpha, L)
        for degree in range(L + 1):
            difference[degree] -= aj[degree]
        aj_all.append(aj)
        checks.append(all(x == 0 for x in difference))
    all_coeffs = omega + a0 + [x for aj in aj_all for x in aj]
    output = {
        "n": n, "k": k, "ell": ell, "L": L,
        "alpha": [as_string(x) for x in alphas],
        "omega_coefficients_low_to_high": [as_string(x) for x in omega],
        "a0_coefficients_low_to_high": [as_string(x) for x in a0],
        "aj_denominator_lcm": [denom_lcm(aj) for aj in aj_all],
        "low_degree_identity_zero_for_each_j": checks,
        "formal_identity_verified_through_degree_L": all(checks),
        "all_kernel_coefficient_denominator_lcm": denom_lcm(all_coeffs),
        "scope": "formal kernel only; no scaled-integrality, determinant, common-factor, or measure claim"
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError) as error:
        print(json.dumps({"error": str(error)}))
        sys.exit(2)
