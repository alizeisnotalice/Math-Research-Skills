#!/usr/bin/env python3
"""Exact certificate for the fixed m=9 radial affine-maximal ODE box."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import sys


EXPECTED = (Q(9, 2), Q(7, 2), Q(33, 7))


def v(a: Q, b: Q, d: Q) -> tuple[Q, Q, Q]:
    return (
        a * (1 + b - a),
        b * (9 + a + Q(12, 11) * b * d - 9 * b),
        (11 - d) * a - 8 * d + b * d * (1 - d / 11),
    )


def parse_q(text: str) -> Q:
    try:
        return Q(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"not a rational number: {text}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upper", nargs=3, type=parse_q, metavar=("A", "B", "D"),
                        default=EXPECTED, help="candidate upper corner (default: 9/2 7/2 33/7)")
    ns = parser.parse_args()
    a, b, d = ns.upper
    errors: list[str] = []
    if min(a, b, d) < 0:
        errors.append("upper bounds must be nonnegative")
    if d > 11:
        errors.append("D upper bound exceeds 11, so d_A V3 can be negative")

    corner = v(a, b, d)
    # Coordinatewise upper-face maxima follow from these cross derivatives.
    cross = (a, b, Q(12, 11) * b * b, 11 - d, d * (1 - d / 11))
    names = ("d_B V1", "d_A V2", "d_D V2", "d_A V3", "d_B V3")
    for name, value in zip(names, cross):
        if value < 0:
            errors.append(f"{name}={value} is negative")
    for name, value in zip(("V1", "V2", "V3"), corner):
        if value > 0:
            errors.append(f"upper-face maximum {name}(upper corner)={value} is positive")

    lower = (Q(0), Q(0), 11 * a)
    if any(value < 0 for value in lower):
        errors.append("a lower face points outward")

    if errors:
        print("FAIL")
        print("; ".join(errors))
        return 1
    print("PASS exact invariant-box certificate")
    print(f"upper=({a},{b},{d}); V(upper)=({corner[0]},{corner[1]},{corner[2]})")
    print("cross derivatives are nonnegative; lower-face values=(0,0,11*A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
