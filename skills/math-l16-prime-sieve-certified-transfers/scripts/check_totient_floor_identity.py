#!/usr/bin/env python3
"""Exact replay of the coprime floor-sum formula for phi(n), n >= 3."""

from __future__ import annotations

import argparse
import json
from math import gcd


def coprime_floor_sum(n: int) -> int:
    """S(n)=sum_{gcd(k,n)=1, 1<=k<=n} sum_{j=1}^{n-1} floor(j*k/n)."""
    if n < 3:
        raise ValueError("the cited denominator formula is used only for n >= 3")
    return sum(
        (j * k) // n
        for k in range(1, n + 1)
        if gcd(k, n) == 1
        for j in range(1, n)
    )


def phi_by_count(n: int) -> int:
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def certificate(n: int) -> dict[str, int | str]:
    s = coprime_floor_sum(n)
    denominator = (n - 1) * (n - 2)
    numerator = 4 * s
    quotient, remainder = divmod(numerator, denominator)
    direct = phi_by_count(n)
    if remainder or quotient != direct:
        raise ArithmeticError("source floor identity did not replay")
    return {
        "status": "EXACT_TOTIENT_FLOOR_IDENTITY",
        "n": n,
        "S": s,
        "numerator_4S": numerator,
        "denominator_(n-1)(n-2)": denominator,
        "phi_floor": quotient,
        "phi_direct": direct,
        "scope": "finite exact identity; no complexity or asymptotic claim",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    try:
        print(json.dumps(certificate(args.n), sort_keys=True))
    except (ValueError, ArithmeticError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
