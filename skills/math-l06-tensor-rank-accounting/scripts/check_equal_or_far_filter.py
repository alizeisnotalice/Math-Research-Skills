#!/usr/bin/env python3
"""Exhaustively check the stated equal-or-far filter in F_p."""
from __future__ import annotations

import itertools
from math import isqrt
import sys


def prime(n: int) -> bool:
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: check_equal_or_far_filter.py ODD_PRIME_P ALPHABET_Q", file=sys.stderr)
        return 2
    try:
        p, q = map(int, argv[1:])
    except ValueError:
        print("arguments must be integers", file=sys.stderr)
        return 2
    if p % 2 == 0 or not prime(p) or q < 2:
        print("requires an odd prime p and alphabet size q >= 2", file=sys.stderr)
        return 2
    words = list(itertools.product(range(q), repeat=2 * p - 1))
    checks = 0
    for x in words:
        for y in words:
            d = sum(a != b for a, b in zip(x, y))
            observed = (1 - pow(d, p - 1, p)) % p
            expected = 1 if d in (0, p) else 0
            if observed != expected:
                raise AssertionError((p, q, x, y, d, observed, expected))
            checks += 1
    print(f"pass: p={p}, q={q}, word_length={2*p-1}, pairs={checks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
