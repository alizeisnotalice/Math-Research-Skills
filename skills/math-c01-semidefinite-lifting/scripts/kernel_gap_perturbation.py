#!/usr/bin/env python3
"""Check a diagonal rational instance of the kernel-gap perturbation contract.

This intentionally accepts a certificate-friendly finite subclass: A is diagonal,
P is the coordinate projection on its zero diagonal entries, and a max-row-sum
bound certifies ||B||_2 <= epsilon*g for symmetric B.  It reports the exact
second-order compressed matrix -P B A^{-1} B P.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from fractions import Fraction


def q(value):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("entries must be integers or rational strings")
    return Fraction(value)


def fail(message):
    print(json.dumps({"ok": False, "error": message}))
    raise SystemExit(2)


def render(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON file with diagonal A, symmetric B, g, epsilon")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("A_diagonal"), list):
            raise ValueError("A_diagonal must be an array")
        raw_b = data.get("B")
        if not isinstance(raw_b, list) or not all(isinstance(row, list) for row in raw_b):
            raise ValueError("B must be an array of rows")
        diag = [q(value) for value in data["A_diagonal"]]
        B = [[q(value) for value in row] for row in raw_b]
        g, eps = q(data["g"]), q(data["epsilon"])
    except (OSError, ValueError, KeyError, ZeroDivisionError) as error:
        fail(str(error))
    n = len(diag)
    if n == 0 or len(B) != n or any(len(row) != n for row in B):
        fail("dimension mismatch or empty matrix")
    if g <= 0 or eps < 0 or eps >= Fraction(1, 2):
        fail("require g>0 and 0<=epsilon<1/2")
    if any(B[i][j] != B[j][i] for i in range(n) for j in range(n)):
        fail("B must be symmetric")
    zero = [i for i, a in enumerate(diag) if a == 0]
    nonzero = [i for i, a in enumerate(diag) if a != 0]
    if not zero:
        fail("P=ker(A) must be nonzero")
    if any(a < g for a in (diag[i] for i in nonzero)):
        fail("diagonal A does not satisfy A>=gQ")
    if any(B[i][j] != 0 for i in zero for j in zero):
        fail("PBP must vanish")
    row_bound = max(sum(abs(x) for x in row) for row in B)
    if row_bound > eps * g:
        fail("row-sum norm certificate does not prove ||B||_2<=epsilon*g")
    minus_k = [
        [render(-sum((B[i][k] * B[k][j] / diag[k] for k in nonzero), Fraction(0)))
         for j in zero]
        for i in zero
    ]
    print(json.dumps({
        "ok": True,
        "kernel_indices": zero,
        "row_sum_norm_bound": render(row_bound),
        "epsilon_g": render(eps * g),
        "second_order_effective_operator_minus_K": minus_k,
        "energy_error_bound": render(2 * g * eps ** 3),
        "scope": "The displayed error bound follows under the cited finite-dimensional lemma; this script verifies only its exact finite input contract.",
    }))


if __name__ == "__main__":
    main()
