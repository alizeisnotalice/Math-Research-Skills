#!/usr/bin/env python3
"""Check the finite arithmetic premise and conclusion of the cited valuation split."""

from __future__ import annotations

import argparse
import json
import sys


def fibonacci(index: int) -> int:
    """Return F_index exactly by fast doubling."""
    if index < 0:
        raise ValueError("index must be nonnegative")

    def pair(n: int) -> tuple[int, int]:
        if n == 0:
            return 0, 1
        a, b = pair(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if n & 1 else (c, d)

    return pair(index)[0]


def exact_power_divides(value: int, base: int, exponent: int) -> bool:
    """Return whether base**exponent exactly divides positive value."""
    power = base**exponent
    return value % power == 0 and value % (power * base) != 0


def check(n: int, ell: int, k: int) -> dict[str, object]:
    if n <= 0 or ell < 3 or k < 2:
        raise ValueError("require n > 0, ell >= 3, and k >= 2")
    f_ell = fibonacci(ell)
    f_n = fibonacci(n)
    premise = exact_power_divides(f_n, f_ell, k)
    nl = n * ell
    if ell % 6 != 3:
        branch = "ell_not_3_mod_6"
        expected_exponent = k - 1
    elif nl % (2 ** (k - 1)) == 0:
        branch = "ell_3_mod_6_and_two_power_divides"
        expected_exponent = k - 1
    else:
        branch = "ell_3_mod_6_and_two_power_does_not_divide"
        expected_exponent = k - 2
    conclusion = exact_power_divides(nl, f_ell, expected_exponent)
    return {
        "n": n,
        "ell": ell,
        "k": k,
        "F_ell": f_ell,
        "F_n": f_n,
        "premise_F_ell_pow_k_exactly_divides_F_n": premise,
        "branch": branch,
        "source_conclusion_exact_power": expected_exponent,
        "conclusion_F_ell_pow_e_exactly_divides_n_ell": conclusion,
        "verified": premise and conclusion,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("ell", type=int)
    parser.add_argument("k", type=int)
    args = parser.parse_args()
    try:
        result = check(args.n, args.ell, args.k)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, sort_keys=True))
    return 0 if result["verified"] else 1


if __name__ == "__main__":
    sys.exit(main())
