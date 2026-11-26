#!/usr/bin/env python3
"""Exact Rabin-style Frobenius irreducibility certificate over F_p."""
from __future__ import annotations

import argparse
import json
import math
import sys


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def sub(a, b, p):
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def divmod_poly(a, b, p):
    a = a[:]
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        c = a[-1] * inv % p
        d = len(a) - len(b)
        q[d] = c
        for i, x in enumerate(b):
            a[d + i] = (a[d + i] - c * x) % p
        trim(a)
    return trim(q), a


def mod(a, f, p):
    return divmod_poly(a, f, p)[1]


def gcd(a, b, p):
    while b != [0]:
        a, b = b, mod(a, b, p)
    inv = pow(a[-1], -1, p)
    return [(x * inv) % p for x in a]


def powmod(a, exponent, f, p):
    out = [1]
    while exponent:
        if exponent & 1:
            out = mod(mul(out, a, p), f, p)
        a = mod(mul(a, a, p), f, p)
        exponent //= 2
    return out


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="JSON: p and low-to-high monic coefficients")
    ns = ap.parse_args()
    try:
        data = json.load(open(ns.input))
        p = int(data["p"])
        f = trim([int(x) % p for x in data["coefficients"]])
        if not is_prime(p):
            raise ValueError("p must be prime")
        if len(f) < 2 or f[-1] != 1:
            raise ValueError("coefficients must encode a monic polynomial of positive degree")
        degree = len(f) - 1
        x = mod([0, 1], f, p)
        frob = [x]
        for _ in range(degree):
            frob.append(powmod(frob[-1], p, f, p))
        if frob[degree] != x:
            raise ValueError("X^(p^D) is not congruent to X modulo A")
        divisors = [d for d in range(1, degree) if degree % d == 0]
        gcd_degrees = {}
        for d in divisors:
            g = gcd(f, sub(frob[d], x, p), p)
            gcd_degrees[str(d)] = len(g) - 1
            if len(g) != 1:
                raise ValueError(f"proper-divisor gcd is nontrivial at d={d}")
        print(json.dumps({"accepted": True, "p": p, "degree": degree,
                          "proper_divisor_gcd_degrees": gcd_degrees}, sort_keys=True))
        return 0
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
