#!/usr/bin/env python3
"""Exact quotient-polynomial and root-bracket checks from the cograph family."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def p(m: int, x: Fraction) -> Fraction:
    return x**3 + 3*x**2 - x - 3 - m*(4*x**2 + 10*x + 4)


def check(m: int) -> dict[str, object]:
    if m < 1:
        raise ValueError("m must be positive")
    # Evaluate det(xI-Q) at four exact points to certify the claimed cubic identity.
    samples = [Fraction(-3), Fraction(-2), Fraction(0), Fraction(1)]
    def qdet(x):
        return det3([[x, -2*m, -1], [-1, x-(4*m-3), -2], [-1, -4*m, x]])
    polynomial_match = all(qdet(x) == p(m, x) for x in samples)
    left, right = -2-Fraction(1, 2*m), Fraction(-2)
    return {"m":m, "polynomial_match":polynomial_match, "left":str(left), "p_left":str(p(m,left)), "right":"-2", "p_right":str(p(m,right)), "strict_bracket":p(m,left)<0<p(m,right)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--m", type=int, nargs="+", required=True)
    for m in ap.parse_args().m: print(json.dumps(check(m), sort_keys=True))


if __name__ == "__main__": main()
