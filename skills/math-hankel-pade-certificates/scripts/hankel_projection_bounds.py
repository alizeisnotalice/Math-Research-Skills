#!/usr/bin/env python3
"""Replay Ferguson's Hankel projection ratios with exact rational arithmetic."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path

from hankel_pade_certificate import as_fraction, hankel, show, solve_unique


def gamma_moment(n: int) -> Fraction:
    scale = factorial(n - 1)
    return sum(
        Fraction(scale * (-1)**i * comb(n, i) * (n - 2*i - 1), (i + 1)**(n + 1))
        for i in range(n + 1)
    )


def gompertz_moments(last: int) -> list[Fraction]:
    values = [Fraction(1)]
    for n in range(1, last):
        values.append(n * values[-1] + 1)
    return values


def zeta_moment(n: int, power: int) -> Fraction:
    return sum(Fraction((-1)**i * comb(n - 1, i), (i + 1)**power) for i in range(n))


def projection_ratios(moments: list[Fraction], last_order: int) -> list[dict]:
    """Read the nonconstant moments a1,...; check leading Gram minors."""
    if last_order < 0 or len(moments) < 2 * last_order + 2:
        raise ValueError("require order N >= 0 and moments indexed 1 through 2*N+2")
    coefficients = [Fraction(0), *moments]
    rows = []
    previous = Fraction(0)
    for n in range(last_order + 1):
        size = n + 1
        q = hankel(coefficients[2:], size)
        if q <= 0:
            raise ValueError(f"shifted Gram leading minor Q_{n} must be positive")
        p = -hankel(coefficients, size + 1)
        ratio = p / q
        gram = [[coefficients[i + j + 2] for j in range(size)] for i in range(size)]
        b = coefficients[1:size + 1]
        c = solve_unique(gram, b)
        projected_energy = sum(value * weight for value, weight in zip(b, c, strict=True))
        if projected_energy != ratio or ratio < previous:
            raise ArithmeticError(f"projection identity or nesting failed at order {n}")
        rows.append({
            "order": n,
            "P": show(p),
            "Q": show(q),
            "ratio": show(ratio),
            "increase": show(ratio - previous),
            "projection_coefficients": [show(x) for x in c],
        })
        previous = ratio
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--constant", choices=("gamma", "gompertz", "zeta"))
    source.add_argument("--moments", type=Path, help="JSON array of exact moments a1,a2,...")
    parser.add_argument("--zeta-power", type=int)
    parser.add_argument("--order", type=int, required=True, help="last order N, starting at 0")
    args = parser.parse_args()
    last = 2 * args.order + 2
    try:
        if args.order < 0:
            raise ValueError("order must be nonnegative")
        if args.constant == "zeta":
            if args.zeta_power is None or args.zeta_power < 2:
                raise ValueError("zeta requires an integer --zeta-power >= 2")
        elif args.zeta_power is not None:
            raise ValueError("--zeta-power is only valid with --constant zeta")

        if args.constant == "gamma":
            moments = [gamma_moment(n) for n in range(1, last + 1)]
        elif args.constant == "gompertz":
            moments = gompertz_moments(last)
        elif args.constant == "zeta":
            moments = [zeta_moment(n, args.zeta_power) for n in range(1, last + 1)]
        else:
            data = json.loads(args.moments.read_text())
            if not isinstance(data, list):
                raise ValueError("moment file must contain a JSON array")
            moments = [as_fraction(x) for x in data]

        rows = projection_ratios(moments, args.order)
    except (OSError, ValueError, ZeroDivisionError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "constant": args.constant,
        "zeta_power": args.zeta_power,
        "scope": ("analytic lower bounds with source hypotheses" if args.constant else
                  "finite projection identities; target mass and positive moment extension require evidence"),
        "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
