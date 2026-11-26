#!/usr/bin/env python3
"""Exact finite audit for Zudilin's Apéry zeta(3) linear forms.

It checks only finite identities/integrality in arXiv:math/0202159v1.
It does not numerically approximate zeta(3) or prove its irrationality.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, gcd


def lcm(left: int, right: int) -> int:
    return left // gcd(left, right) * right


def d(n: int) -> int:
    value = 1
    for integer in range(1, n + 1):
        value = lcm(value, integer)
    return value


def u_binomial(n: int) -> int:
    # Equation (2), then u_n=2 sum_k A_{2k}^{(n)} in equation (3).
    return 2 * sum(comb(n + k, n) ** 2 * comb(n, k) ** 2 for k in range(n + 1))


def forms(through: int) -> list[tuple[int, Fraction]]:
    if through < 0:
        raise ValueError("through must be nonnegative")
    values: list[tuple[int, Fraction]] = [(2, Fraction(0))]
    if through == 0:
        return values
    values.append((10, Fraction(12)))
    for n in range(1, through):
        coefficient = (2 * n + 1) * (17 * n * n + 17 * n + 5)
        u_next = Fraction(coefficient * values[n][0] - n**3 * values[n - 1][0], (n + 1) ** 3)
        v_next = Fraction(coefficient * values[n][1] - n**3 * values[n - 1][1], (n + 1) ** 3)
        if u_next.denominator != 1:
            raise AssertionError(f"u recurrence is nonintegral at n={n}")
        values.append((u_next.numerator, v_next))
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=8)
    args = parser.parse_args()
    values = forms(args.through)
    rows = []
    for n, (u, v) in enumerate(values):
        dn = d(n)
        scaled_v = dn**3 * v
        if scaled_v.denominator != 1 or u != u_binomial(n):
            raise AssertionError(f"source finite arithmetic identity failed at n={n}")
        rows.append({"n": n, "D_n": dn, "u_n": u, "v_n": str(v), "D_n^3_v_n": scaled_v.numerator})
    # 27(sqrt(2)-1)^4<1 iff 458<324 sqrt(2); this square certificate is positive.
    square_margin = 2 * 324**2 - 458**2
    if square_margin <= 0:
        raise AssertionError("unexpected contraction certificate failure")
    print(json.dumps({
        "source": "arXiv:math/0202159v1, equations (1)-(4),(7),(10),(15)",
        "through": args.through,
        "finite_checks": ["u_n equals the binomial coefficient sum", "u_n integer", "D_n^3 v_n integer"],
        "contraction_certificate": {"claim": "27*(sqrt(2)-1)^4 < 1", "integer_square_margin": square_margin},
        "rows": rows,
        "scope": "finite arithmetic only; the source's infinite positive remainder bound is cited, not recomputed",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
