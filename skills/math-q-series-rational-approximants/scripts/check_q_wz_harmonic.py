#!/usr/bin/env python3
"""Check the finite q-WZ identity used for the q-harmonic series exactly."""

import argparse
import json
from fractions import Fraction


def q_pochhammer(q: int, n: int) -> Fraction:
    """Return (q)_n = product_{j=1}^n (1-q^j), exactly."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = Fraction(1)
    for j in range(1, n + 1):
        result *= 1 - q**j
    return result


def q_binomial(q: int, n: int, k: int) -> Fraction:
    """Return the Gaussian binomial coefficient [n choose k]_q exactly."""
    if n < 0 or k < 0 or k > n:
        raise ValueError("require 0 <= k <= n")
    return q_pochhammer(q, n) / (q_pochhammer(q, k) * q_pochhammer(q, n - k))


def pair(q: int, n: int, k: int) -> tuple[Fraction, Fraction]:
    """The Amdeberhan--Zeilberger q-harmonic WZ pair (physical p. 2)."""
    f = -Fraction(1, q_binomial(q, n + k + 1, k) * q_pochhammer(q, n + 1))
    g = f * q ** (n + 1) / (q ** (n + 1) - 1)
    return f, g


def check(q: int, max_n: int, max_k: int) -> dict[str, int | str]:
    """Check Delta_n F(n,k) = Delta_k G(n,k) on a finite integer grid."""
    if abs(q) <= 1:
        raise ValueError("require an integer q with |q| > 1")
    if max_n < 0 or max_k < 0:
        raise ValueError("grid bounds must be non-negative")
    for n in range(max_n + 1):
        for k in range(max_k + 1):
            f, g = pair(q, n, k)
            f_next, _ = pair(q, n + 1, k)
            _, g_next = pair(q, n, k + 1)
            if f_next - f != g_next - g:
                raise AssertionError(f"identity fails at n={n}, k={k}")
    return {"q": q, "max_n": max_n, "max_k": max_k, "checks": (max_n + 1) * (max_k + 1), "status": "passed"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q", type=int, help="integer q with |q| > 1")
    parser.add_argument("--max-n", type=int, default=4)
    parser.add_argument("--max-k", type=int, default=4)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.q, args.max_n, args.max_k), sort_keys=True))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
