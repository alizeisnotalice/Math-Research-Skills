#!/usr/bin/env python3
"""Exact finite check for the Weyl-block algebra in two OpenAI 2026 sources.

It checks only the pointwise, oriented Einstein-4 curvature-block interface
with Ric = 3g.  It does not test whether any supplied blocks come from a
metric, nor any global rigidity conclusion.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def q(value: str) -> Fraction:
    return Fraction(value)


def block(values: list[str], name: str) -> tuple[Fraction, Fraction]:
    if len(values) != 3:
        raise ValueError(f"{name} must have exactly three eigenvalues")
    eig = tuple(q(v) for v in values)
    if sum(eig) != 0:
        raise ValueError(f"{name} must be trace-free")
    minimum = min(eig)
    x = -minimum
    if x < 0:
        raise ValueError(f"{name} has positive minimum; this violates the source parametrization")
    norm_sq = sum(v * v for v in eig)
    # Source notation: v^2 = |T|^2/6 and v <= x <= 2v.
    v_sq = norm_sq / 6
    if not (v_sq <= x * x <= 4 * v_sq):
        raise AssertionError("trace-free eigenvalue norm bounds failed")
    return x, v_sq


def check(t: list[str], u: list[str]) -> dict[str, object]:
    x, v_sq = block(t, "T")
    y, b_sq = block(u, "U")
    sectional_minimum = Fraction(1) - (x + y) / 2
    return {
        "normalization": "oriented Einstein four-dimensional pointwise interface Ric=3g",
        "x": str(x), "y": str(y),
        "v_squared": str(v_sq), "b_squared": str(b_sq),
        "sectional_minimum": str(sectional_minimum),
        "strictly_positive_sectional_curvature": sectional_minimum > 0,
        "nonnegative_sectional_curvature": sectional_minimum >= 0,
    }


def self_test() -> None:
    positive = check(["-1", "0", "1"], ["-1/2", "0", "1/2"])
    assert positive["strictly_positive_sectional_curvature"]
    boundary = check(["-1", "0", "1"], ["-1", "0", "1"])
    assert not boundary["strictly_positive_sectional_curvature"]
    assert boundary["nonnegative_sectional_curvature"]
    negative = check(["-1", "0", "1"], ["-3/2", "0", "3/2"])
    assert not negative["nonnegative_sectional_curvature"]
    try:
        check(["0", "0", "1"], ["-1", "0", "1"])
    except ValueError:
        return
    raise AssertionError("non-trace-free input was accepted")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", nargs=3, metavar="EIG", help="three rational T eigenvalues")
    parser.add_argument("--u", nargs=3, metavar="EIG", help="three rational U eigenvalues")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("PASS: positive, zero-plane boundary, negative, and rejected trace cases")
        return
    if not (args.t and args.u):
        parser.error("supply both --t and --u, or --self-test")
    try:
        result = check(args.t, args.u)
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
