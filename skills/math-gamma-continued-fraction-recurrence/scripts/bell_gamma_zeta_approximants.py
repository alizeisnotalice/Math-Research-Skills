#!/usr/bin/env python3
"""Exact finite checks for Theorem 1 of arXiv:1011.3833v1.

The script evaluates the Bell-polynomial rational approximants p_(n,mu)/q_n
using only integers and fractions.  It checks finite integrality assertions
and source-printed special cases; it does not numerically prove the paper's
asymptotics or any irrationality statement.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb, factorial, lcm


def require_index(index: int, name: str = "index") -> None:
    if index < 0:
        raise ValueError(f"{name} must be nonnegative")


def require_parameters(a: int, mu: int) -> None:
    if a < 2:
        raise ValueError("a must be at least 2")
    if not 1 <= mu <= a - 1:
        raise ValueError("mu must satisfy 1 <= mu <= a - 1")


def harmonic(index: int, order: int = 1) -> Fraction:
    """Return H_index^(order), exactly, with H_0^(order)=0."""
    require_index(index)
    if order < 1:
        raise ValueError("order must be positive")
    return sum((Fraction(1, divisor**order) for divisor in range(1, index + 1)), Fraction())


def lcm_to(index: int) -> int:
    """Return lcm(1,...,index), with the source convention D_0=1."""
    require_index(index)
    answer = 1
    for divisor in range(1, index + 1):
        answer = lcm(answer, divisor)
    return answer


def complete_bell(values: list[Fraction]) -> Fraction:
    """Evaluate Y_m(x_1,...,x_m) via the recurrence on PDF p. 4."""
    bell = [Fraction(1)]
    for degree in range(len(values)):
        bell.append(
            sum(
                (Fraction(comb(degree, term)) * values[term] * bell[degree - term]
                 for term in range(degree + 1)),
                Fraction(),
            )
        )
    return bell[-1]


def r_value(a: int, n: int, k: int, order: int) -> Fraction:
    """Return r_order(k) of equation (8), exactly."""
    if a < 2:
        raise ValueError("a must be at least 2")
    require_index(n, "n")
    if not 0 <= k <= n:
        raise ValueError("k must satisfy 0 <= k <= n")
    if order < 1:
        raise ValueError("order must be positive")
    sign = -1 if order % 2 else 1
    return Fraction(factorial(order - 1)) * (
        a * harmonic(n - k, order) + sign * (a - 1) * harmonic(k, order)
    )


def approximant(a: int, n: int, mu: int) -> tuple[Fraction, int]:
    """Return (p_(n,mu), q_n) from Theorem 1's finite sums."""
    require_parameters(a, mu)
    require_index(n, "n")
    numerator = Fraction()
    denominator = 0
    for k in range(n + 1):
        weight = comb(n, k) ** a * factorial(k)
        denominator += weight
        numerator += weight * complete_bell([r_value(a, n, k, order) for order in range(1, mu + 1)])
    return numerator, denominator


def alpha_text(a: int, mu: int) -> str:
    """Return the formal target alpha_mu; transcendental values are not evaluated."""
    require_parameters(a, mu)
    arguments = ["gamma"]
    for order in range(2, mu + 1):
        coefficient = factorial(order - 1) * (a + ((-1) ** order) * (a - 1))
        arguments.append(f"{coefficient}*zeta({order})")
    return f"Y_{mu}(" + ", ".join(arguments) + ")"


def fraction_text(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check_integrality(a: int, mu: int, through: int) -> None:
    """Check q_n and D_n^mu p_(n,mu) integrality through a finite range."""
    require_parameters(a, mu)
    require_index(through, "through")
    for n in range(through + 1):
        p_value, q_value = approximant(a, n, mu)
        scaled = lcm_to(n) ** mu * p_value
        if q_value != int(q_value) or scaled.denominator != 1:
            raise AssertionError(f"integrality check fails at n={n}")


def check_a2_crosscheck(through: int) -> None:
    """Independently cross-check a=2, mu=1 against arXiv:1010.1420's sum."""
    require_index(through, "through")
    for n in range(through + 1):
        old_p = sum(
            (Fraction(comb(n, k) ** 2 * factorial(k)) * (2 * harmonic(n - k) - harmonic(k))
             for k in range(n + 1)),
            Fraction(),
        )
        old_q = sum(comb(n, k) ** 2 * factorial(k) for k in range(n + 1))
        p_value, q_value = approximant(2, n, 1)
        if (p_value, q_value) != (old_p, old_q):
            raise AssertionError(f"a=2 cross-check fails at n={n}")


def check_a3_example() -> None:
    """Check the a=3 initial values printed in Example 1 (PDF p. 6)."""
    expected_q = [1, 2, 11]
    expected_p1 = [Fraction(0), Fraction(1), Fraction(13, 2)]
    expected_p2 = [Fraction(0), Fraction(18), Fraction(95)]
    for n in range(3):
        p1, q1 = approximant(3, n, 1)
        p2, q2 = approximant(3, n, 2)
        if (q1, q2, p1, p2) != (expected_q[n], expected_q[n], expected_p1[n], expected_p2[n]):
            raise AssertionError(f"a=3 Example 1 check fails at n={n}")


def check_rejections() -> None:
    """Exercise invalid parameter branches rather than silently extending the theorem."""
    invalid_calls = (
        lambda: approximant(1, 0, 1),
        lambda: approximant(2, -1, 1),
        lambda: approximant(2, 0, 0),
        lambda: approximant(2, 0, 2),
        lambda: harmonic(-1),
        lambda: r_value(2, 1, 2, 1),
    )
    for call in invalid_calls:
        try:
            call()
        except ValueError:
            continue
        raise AssertionError("an out-of-domain input was accepted")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, default=3, help="integer a in the theorem (default: 3)")
    parser.add_argument("--mu", type=int, default=2, help="Bell-polynomial order mu (default: 2)")
    parser.add_argument("--through", type=int, default=6, help="largest n for finite checks (default: 6)")
    parser.add_argument("--crosscheck-a2", action="store_true", help="cross-check the a=2 gamma sum")
    parser.add_argument("--check-a3", action="store_true", help="check a=3 Example 1 initial values")
    parser.add_argument("--negative-tests", action="store_true", help="check rejection of out-of-domain inputs")
    arguments = parser.parse_args()

    require_parameters(arguments.a, arguments.mu)
    require_index(arguments.through, "through")
    check_integrality(arguments.a, arguments.mu, arguments.through)
    print(f"exact finite integrality check passed through n={arguments.through}")
    print(f"formal target: {alpha_text(arguments.a, arguments.mu)}")
    for n in range(arguments.through + 1):
        p_value, q_value = approximant(arguments.a, n, arguments.mu)
        print(
            f"n={n}: p={fraction_text(p_value)}, q={q_value}, "
            f"D_n^mu*p={fraction_text(lcm_to(n) ** arguments.mu * p_value)}"
        )
    if arguments.crosscheck_a2:
        check_a2_crosscheck(arguments.through)
        print(f"a=2, mu=1 direct-sum cross-check passed through n={arguments.through}")
    if arguments.check_a3:
        check_a3_example()
        print("a=3 Example 1 initial-value check passed (alpha_2 = gamma^2 + 5*zeta(2))")
    if arguments.negative_tests:
        check_rejections()
        print("out-of-domain rejection checks passed")
    print("scope: exact finite identities only; no asymptotic or irrationality conclusion")


if __name__ == "__main__":
    main()
