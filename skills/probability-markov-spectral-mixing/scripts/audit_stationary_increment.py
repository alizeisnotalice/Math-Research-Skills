#!/usr/bin/env python3
"""Exact finite audit for a stationary reversible-chain increment inequality.

Input is JSON with rational entries represented either as JSON integers or strings
accepted by fractions.Fraction (for example "3/10").  The required fields are
``P`` (a square stochastic matrix), ``pi`` (a stationary distribution), ``f``
(a real-valued observable), and nonnegative integer ``steps``.

The program rejects a non-reversible input rather than treating a numerical
approximation as a certificate.  On acceptance it verifies exactly

  E_pi[(f(Y_k)-f(Y_0))^2] <= 2 k <f,(I-P)f>_pi.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


from rational_reversible_chain import rational, reversible_chain


def matrix_product(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [[sum(a[i][r] * b[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def matrix_power(a: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    n = len(a)
    out = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    base = a
    while exponent:
        if exponent & 1:
            out = matrix_product(out, base)
        exponent //= 2
        if exponent:
            base = matrix_product(base, base)
    return out


def parse_and_check(payload: dict[str, Any]) -> tuple[list[list[Fraction]], list[Fraction], list[Fraction], int]:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    steps = payload.get("steps")
    if type(steps) is not int or steps < 0:
        raise ValueError("steps must be a nonnegative JSON integer")
    p, pi, _ = reversible_chain(payload.get("P"), payload.get("pi"))
    raw_f = payload.get("f")
    if not isinstance(raw_f, list) or len(raw_f) != len(pi):
        raise ValueError("f must have one rational value per state")
    return p, pi, [rational(x) for x in raw_f], steps


def audit(p: list[list[Fraction]], pi: list[Fraction], f: list[Fraction], steps: int) -> dict[str, Any]:
    pk = matrix_power(p, steps)
    increment = sum(pi[i] * pk[i][j] * (f[j] - f[i]) ** 2 for i in range(len(pi)) for j in range(len(pi)))
    form = sum(pi[i] * p[i][j] * (f[j] - f[i]) ** 2 for i in range(len(pi)) for j in range(len(pi))) / 2
    upper = 2 * steps * form
    if increment > upper:  # Defensive: exact theorem check, never a floating comparison.
        raise AssertionError("increment inequality failed after exact reversible validation")
    return {
        "certificate": "stationary_reversible_increment",
        "steps": steps,
        "increment_second_moment": str(increment),
        "discrete_dirichlet_form": str(form),
        "upper_bound_2kE": str(upper),
        "inequality_verified_exactly": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="JSON input with P, pi, f, steps")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        p, pi, f, steps = parse_and_check(payload)
        print(json.dumps(audit(p, pi, f, steps), indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, ZeroDivisionError) as exc:
        print(f"input rejected: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
