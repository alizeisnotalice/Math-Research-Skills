#!/usr/bin/env python3
"""Exact checks for Prévost's finite exp(-t) Padé/Hurwitz interface."""

import argparse
from fractions import Fraction
import json
from math import factorial, comb


def rising(a, count):
    answer = 1
    for offset in range(count):
        answer *= a + offset
    return answer


def require_domain(m, n, s):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0 or m + n == 0:
        raise ValueError("require integers m,n >= 0 with m+n > 0")
    if not isinstance(s, (int, Fraction)) or s <= -1:
        raise ValueError("s must be rational and greater than -1")


def pade_polynomials(m, n):
    denominator = lambda k: rising(-m - n, k)
    p = [Fraction(rising(-n, k) * (-1) ** k, denominator(k) * factorial(k)) for k in range(n + 1)]
    q = [Fraction(rising(-m, k), denominator(k) * factorial(k)) for k in range(m + 1)]
    return p, q


def verify_contact(m, n):
    p, q = pade_polynomials(m, n)
    for degree in range(m + n + 1):
        qe = sum(q[k] * Fraction((-1) ** (degree - k), factorial(degree - k))
                 for k in range(min(degree, m) + 1))
        p_at_degree = p[degree] if degree <= n else 0
        assert qe == p_at_degree
    return p, q


def formula_coefficients(m, n, s):
    require_domain(m, n, s)
    linear = []
    for j in range(1, m + 1):
        linear.append((j, Fraction(rising(-m, j), rising(-m - n, j) * j * (s + 1) ** j)))
    hurwitz = []
    for j in range(2, max(m, n) + 1):
        numerator = rising(-m, j) - (-1) ** j * rising(-n, j)
        coefficient = -Fraction(numerator, rising(-m - n, j) * j)
        if coefficient:
            hurwitz.append((j, coefficient))
    return linear, hurwitz


def rational_remainder_bound(m, n, s):
    """Bound the Hurwitz series by its first term and a rational integral."""
    require_domain(m, n, s)
    r = m + n + 1
    a = Fraction(s + 1)
    zeta_bound = a**(-r) + a**(1-r) / (r - 1)
    return zeta_bound / (r * comb(m + n, n))


def run_examples():
    p, q = verify_contact(1, 1)
    linear, hurwitz = formula_coefficients(1, 1, 0)
    assert p == [Fraction(1), Fraction(-1, 2)]
    assert q == [Fraction(1), Fraction(1, 2)]
    assert linear == [(1, Fraction(1, 2))] and hurwitz == []
    assert rational_remainder_bound(1, 1, 0) == Fraction(1, 4)
    # Thus source (H)--(R) gives 1/2 < gamma < 3/4 in this special case.

    verify_contact(1, 2)
    multi_linear, multi_hurwitz = formula_coefficients(1, 2, 1)
    assert multi_linear and multi_hurwitz and rational_remainder_bound(1, 2, 1) == Fraction(5, 576)

    for bad in ((0, 0, 0), (1, 1, -1)):
        try:
            formula_coefficients(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid input accepted: {bad}")

    print("m=n=1,s=0", "P", p, "Q", q, "remainder<", Fraction(1, 4))
    print("m=1,n=2,s=1", "log", multi_linear, "hurwitz", multi_hurwitz, "remainder<", Fraction(5, 576))
    print("invalid-domain-rejection ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", type=int)
    parser.add_argument("--n", type=int)
    parser.add_argument("--s", type=Fraction)
    args = parser.parse_args()
    if all(value is None for value in (args.m, args.n, args.s)):
        run_examples()
        return
    if any(value is None for value in (args.m, args.n, args.s)):
        parser.error("--m, --n and --s are required together")
    try:
        linear, hurwitz = formula_coefficients(args.m, args.n, args.s)
        p, q = verify_contact(args.m, args.n)
        bound = rational_remainder_bound(args.m, args.n, args.s)
    except ValueError as error:
        parser.error(str(error))
    sign = (-1)**(args.n + 1)
    result = {"p": [str(x) for x in p], "q": [str(x) for x in q],
              "finite_terms": [[j, str(x)] for j, x in linear],
              "hurwitz_coefficients": [[j, str(x)] for j, x in hurwitz],
              "s": str(args.s), "absolute_remainder_upper": str(bound),
              "remainder_sign": sign}
    if args.s == 0 and not hurwitz:
        base = sum((x for _, x in linear), Fraction())
        endpoint = base + sign * bound
        result["strict_gamma_interval"] = [str(min(base, endpoint)), str(max(base, endpoint))]
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
