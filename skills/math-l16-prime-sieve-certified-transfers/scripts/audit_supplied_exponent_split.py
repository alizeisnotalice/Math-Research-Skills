#!/usr/bin/env python3
"""Audit a supplied p-minus-one exponent and its elementary gcd split tests."""

from __future__ import annotations

import argparse
import json
from math import gcd


def is_prime_trial(value: int) -> bool:
    """Use exact trial division because supplied exponent divisors are finite inputs."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def audit(n: int, base: int, exponent: int, prime_divisors: list[int]) -> dict[str, object]:
    if n <= 1:
        raise ValueError("n must exceed 1")
    if exponent < 1:
        raise ValueError("exponent must be positive")
    if not prime_divisors:
        raise ValueError("provide at least one supplied prime divisor of exponent")
    if len(set(prime_divisors)) != len(prime_divisors):
        raise ValueError("supplied prime divisors must be distinct")
    for q in prime_divisors:
        if not is_prime_trial(q):
            raise ValueError(f"{q} is not prime")
        if exponent % q:
            raise ValueError(f"{q} does not divide exponent")

    base %= n
    base_gcd = gcd(base, n)
    exponent_holds = base_gcd == 1 and pow(base, exponent, n) == 1
    tests = []
    for q in sorted(prime_divisors):
        residual = pow(base, exponent // q, n)
        divisor = gcd(residual - 1, n)
        tests.append(
            {
                "prime_divisor": q,
                "reduced_power": residual,
                "gcd": divisor,
                "nontrivial_divisor": divisor if 1 < divisor < n else None,
            }
        )
    return {
        "n": n,
        "base": base,
        "exponent": exponent,
        "base_gcd": base_gcd,
        "base_to_exponent_mod_n": pow(base, exponent, n),
        "exponent_holds_for_this_base": exponent_holds,
        "tests": tests,
        "scope": (
            "If the supplied exponent holds for this unit and a listed gcd lies strictly between 1 and n, "
            "that gcd is an exact factor. A failed gcd test neither disproves a common exponent nor proves primality."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("base", type=int)
    parser.add_argument("exponent", type=int)
    parser.add_argument("prime_divisors", type=int, nargs="+")
    args = parser.parse_args()
    try:
        result = audit(args.n, args.base, args.exponent, args.prime_divisors)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
