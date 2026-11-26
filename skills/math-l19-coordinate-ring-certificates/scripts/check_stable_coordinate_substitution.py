#!/usr/bin/env python3
"""Check only the determinant-one substitution on pp.4--5 of source 52d49d."""
import argparse
import sys

import sympy as sp


def matrices(edge=False):
    s, u = sp.symbols("s u")
    x0 = s**2-u**2
    forward = sp.Matrix([[x0**2, -(1+2*s*x0)], [1-2*s*x0, 4*s**2]])
    lower_right = 4*s**2 + (1 if edge else 0)
    inverse = sp.Matrix([[4*s**2, 1+2*s*x0], [-(1-2*s*x0), x0**2]])
    if edge:
        inverse[0, 0] = lower_right
    return forward, inverse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=("positive", "perturb"), default="positive")
    args = parser.parse_args()
    forward, inverse = matrices(edge=args.case == "perturb")
    product = (forward*inverse).applyfunc(sp.expand)
    ok = sp.expand(forward.det()-1) == 0 and product == sp.eye(2)
    if not ok:
        print("rejected: substitution is not the displayed determinant-one inverse", file=sys.stderr)
        return 2
    print("verified: determinant-one substitution and inverse")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
