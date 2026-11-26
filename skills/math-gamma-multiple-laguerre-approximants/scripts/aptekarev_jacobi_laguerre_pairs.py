#!/usr/bin/env python3
"""Exact finite Aptekarev gamma pairs from arXiv:1004.0578v1, formula (5)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def harmonic(n: int) -> sp.Rational:
    return sum((sp.Rational(1, j) for j in range(1, n + 1)), sp.S.Zero)


def pair(n: int) -> tuple[sp.Integer, sp.Integer]:
    """Return (p_n, q_n) from the a=0, b=1 specialization of formula (5)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    q_value = sum((sp.binomial(n, k) ** 2 * sp.factorial(n + k) for k in range(n + 1)), sp.S.Zero)
    leading = sum((sp.binomial(n, k) ** 2 * sp.factorial(n + k) * harmonic(n + k) for k in range(n + 1)), sp.S.Zero)
    correction = sum(
        (
            sp.Rational((-1) ** (m + k), k)
            * sp.binomial(n, k + ell)
            * sp.binomial(k, m)
            * sp.binomial(n - k, ell)
            * sp.factorial(m + n + ell)
            for k in range(1, n + 1)
            for m in range(k + 1)
            for ell in range(n - k + 1)
        ),
        sp.S.Zero,
    )
    p_value = sp.cancel(leading - 2 * correction)
    if not (p_value.is_Integer and q_value.is_Integer):
        raise AssertionError("the special a=0,b=1 finite formula should be integral")
    return sp.Integer(p_value), sp.Integer(q_value)


def load_indices(path: Path) -> list[int]:
    data = json.loads(path.read_text())
    indices = data.get("indices")
    if not isinstance(indices, list) or not indices or not all(isinstance(n, int) and n >= 0 for n in indices):
        raise ValueError("input must contain a nonempty 'indices' list of nonnegative integers")
    return indices


def self_test() -> None:
    expected = [(0, 1), (2, 3), (31, 50)]
    observed = [tuple(map(int, pair(n))) for n in range(3)]
    if observed != expected:
        raise AssertionError(f"initial-value mismatch: {observed}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="JSON object with an 'indices' list")
    parser.add_argument("--self-test", action="store_true", help="check the source's n=0,1,2 values")
    args = parser.parse_args()
    if not args.input and not args.self_test:
        parser.error("supply --input and/or --self-test")
    try:
        if args.self_test:
            self_test()
        result = {"self_test": "passed"} if args.self_test else {}
        if args.input:
            rows = []
            for n in load_indices(Path(args.input)):
                p_value, q_value = pair(n)
                reduced = sp.Rational(p_value, q_value)
                rows.append({"n": n, "p_n": int(p_value), "q_n": int(q_value), "reduced_p_over_q": [int(reduced.p), int(reduced.q)]})
            result["pairs"] = rows
            result["scope"] = "exact finite formula (5) only; no gamma evaluation, error bound, nonvanishing, or irrationality claim"
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
