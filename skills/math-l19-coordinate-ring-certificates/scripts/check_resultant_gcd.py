#!/usr/bin/env python3
"""Exact finite verifier for the linear-resultant gcd lemma."""
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


def value(coeffs, x):
    return sum(int(c) * x**i for i, c in enumerate(coeffs))


def vp(n, p):
    n = abs(n)
    out = 0
    while n and n % p == 0:
        out += 1
        n //= p
    return out


def main(path):
    data = json.loads(Path(path).read_text())
    linear = data["linear_coefficients"]
    poly = data["polynomial_coefficients"]
    x0 = int(data["x"])
    if len(linear) != 2 or int(linear[1]) == 0 or len(poly) < 2:
        raise ValueError("need nonconstant alpha*x+beta and nonconstant polynomial")
    beta, alpha = map(int, linear)
    x = sp.symbols("x")
    f = alpha * x + beta
    g = sum(int(c) * x**i for i, c in enumerate(poly))
    delta = abs(int(sp.resultant(f, g, x)))
    if delta == 0:
        raise ValueError("resultant is zero")
    fx, gx = value(linear, x0), value(poly, x0)
    common = math.gcd(fx, gx)
    if delta % common:
        raise AssertionError("computed gcd does not divide resultant")
    out = {"status": "pass", "resultant_abs": str(delta), "f_at_x": str(fx),
           "g_at_x": str(gx), "gcd": str(common)}
    if "prime" in data:
        p = int(data["prime"])
        deriv = sum(i * int(c) * Fraction(-beta, alpha) ** (i - 1)
                    for i, c in enumerate(poly) if i)
        if not sp.isprime(p) or vp(delta, p) != 1 or alpha % p == 0 or deriv.denominator != 1 or int(deriv) % p or common % p:
            raise ValueError("prime-side hypotheses fail")
        if vp(gx, p) != 1:
            raise AssertionError("source simple-divisibility conclusion fails")
        out["prime_simple_divisibility"] = str(p)
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except (IndexError, ValueError, AssertionError, json.JSONDecodeError) as err:
        print(json.dumps({"status": "reject", "reason": str(err)}, sort_keys=True))
        raise SystemExit(2)
