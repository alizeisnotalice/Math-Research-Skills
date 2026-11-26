#!/usr/bin/env python3
"""Exact finite checks for Osburn--Sahu generalized Apéry supercongruences."""

from __future__ import annotations

import argparse
import json
from math import comb


def c(n: int, a: int, b: int) -> int:
    return sum(comb(n, k) ** a * comb(2 * k, k) ** b for k in range(n + 1))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is not used in this audit")
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def is_prime(value: int) -> bool:
    return value > 1 and all(value % candidate for candidate in range(2, int(value**0.5) + 1))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--b", type=int, required=True)
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--m", type=int, default=1)
    parser.add_argument("--r", type=int, default=1)
    args = parser.parse_args()
    if args.a < 2 or args.b < 1 or args.m < 1 or args.r < 1 or args.p <= 3 or not is_prime(args.p):
        parser.error("require a>=2, b,m,r>=1, and prime p>3")
    current_index = args.m * args.p**args.r
    previous_index = args.m * args.p ** (args.r - 1)
    current = c(current_index, args.a, args.b)
    previous = c(previous_index, args.a, args.b)
    difference = current - previous
    observed = valuation(difference, args.p)
    required = (3 if args.a >= 3 else 2) * args.r
    print(json.dumps({
        "source": "arXiv:0906.3413v3, Theorem 1.1",
        "C": "sum_{k=0}^n binom(n,k)^a binom(2k,k)^b",
        "parameters": vars(args),
        "indices": [current_index, previous_index],
        "difference": difference,
        "p_adic_valuation": observed,
        "theorem_required_lower_bound": required,
        "finite_check": observed >= required,
        "scope": "one finite instance only; the theorem's all-m,r proof is external to this script",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
