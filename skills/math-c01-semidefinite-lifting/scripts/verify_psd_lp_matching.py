#!/usr/bin/env python3
"""Verify a finite rational certificate that a rank-one-cut LP matches an SDP.

For the primal minimization SDP
    min <C,X>  subject to <A_i,X>=b_i, X >= 0,
the associated LP retains the affine equations and the cuts v_j^T X v_j >= 0.
The JSON certificate supplies y, nonnegative alpha_j, cut vectors v_j, and a
PSD primal witness X.  The checker verifies, exactly,
    C - sum_i y_i A_i = sum_j alpha_j v_j v_j^T,
    <C,X> = b^T y,
along with primal feasibility.  These identities prove that both the SDP and this
particular LP have value b^T y.  It is a verifier, not an SDP or LP solver.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


MAX_PSD_DIMENSION = 12  # Exact principal-minor verification is exponential in n.


def q(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all scalars must be integers or rational strings; floats are forbidden")
    if isinstance(value, (int, str)):
        return Fraction(value)
    raise ValueError(f"not an exact rational: {value!r}")


def vector(raw: Any, n: int | None = None, name: str = "vector") -> list[Fraction]:
    if not isinstance(raw, list):
        raise ValueError(f"{name} must be a list")
    result = [q(x) for x in raw]
    if n is not None and len(result) != n:
        raise ValueError(f"{name} has length {len(result)}, expected {n}")
    return result


def matrix(raw: Any, n: int | None = None, name: str = "matrix") -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"{name} must be a nonempty square list of lists")
    size = len(raw)
    if n is not None and size != n:
        raise ValueError(f"{name} has dimension {size}, expected {n}")
    result = [vector(row, size, f"{name}[{i}]") for i, row in enumerate(raw)]
    for i in range(size):
        for j in range(size):
            if result[i][j] != result[j][i]:
                raise ValueError(f"{name} is not symmetric at ({i},{j})")
    return result


def zero(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def dot_matrix(a: list[list[Fraction]], b: list[list[Fraction]]) -> Fraction:
    return sum((a[i][j] * b[i][j] for i in range(len(a)) for j in range(len(a))), Fraction(0))


def outer(v: list[Fraction]) -> list[list[Fraction]]:
    return [[left * right for right in v] for left in v]


def add_scaled(target: list[list[Fraction]], source: list[list[Fraction]], scale: Fraction) -> None:
    for i in range(len(target)):
        for j in range(len(target)):
            target[i][j] += scale * source[i][j]


def determinant(a: list[list[Fraction]]) -> Fraction:
    """Exact determinant by elimination, including row swaps for zero pivots."""
    work = [row[:] for row in a]
    sign = Fraction(1)
    answer = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign = -sign
        pivot_value = work[col][col]
        answer *= pivot_value
        for row in range(col + 1, len(work)):
            factor = work[row][col] / pivot_value
            for right in range(col + 1, len(work)):
                work[row][right] -= factor * work[col][right]
            work[row][col] = Fraction(0)
    return sign * answer


def assert_psd(a: list[list[Fraction]], name: str) -> int:
    """PSD iff every principal minor is nonnegative (exact but exponential)."""
    n = len(a)
    if n > MAX_PSD_DIMENSION:
        raise ValueError(f"{name} has dimension {n}; exact principal-minor mode is capped at {MAX_PSD_DIMENSION}")
    checked = 0
    for k in range(1, n + 1):
        for indices in itertools.combinations(range(n), k):
            minor = [[a[i][j] for j in indices] for i in indices]
            value = determinant(minor)
            checked += 1
            if value < 0:
                raise ValueError(f"{name} is not PSD: principal minor {indices} equals {value}")
    return checked


def text_matrix(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    problem = payload.get("problem")
    certificate = payload.get("certificate")
    if not isinstance(problem, dict) or not isinstance(certificate, dict):
        raise ValueError("top-level problem and certificate objects are required")
    c = matrix(problem.get("C"), name="C")
    n = len(c)
    raw_a = problem.get("A")
    raw_b = problem.get("b")
    if not isinstance(raw_a, list) or not isinstance(raw_b, list) or len(raw_a) != len(raw_b):
        raise ValueError("A and b must be equally long lists")
    a = [matrix(item, n, f"A[{i}]") for i, item in enumerate(raw_a)]
    b = vector(raw_b, len(a), "b")
    y = vector(certificate.get("dual_y"), len(a), "certificate.dual_y")
    raw_cuts = certificate.get("cuts")
    if not isinstance(raw_cuts, list) or not raw_cuts:
        raise ValueError("certificate.cuts must be a nonempty list")

    slack = [[c[i][j] for j in range(n)] for i in range(n)]
    for i, ai in enumerate(a):
        add_scaled(slack, ai, -y[i])
    conic_slack = zero(n)
    cuts: list[tuple[list[Fraction], Fraction]] = []
    for index, raw_cut in enumerate(raw_cuts):
        if not isinstance(raw_cut, dict):
            raise ValueError(f"cuts[{index}] must be an object")
        v = vector(raw_cut.get("vector"), n, f"cuts[{index}].vector")
        alpha = q(raw_cut.get("weight"))
        if alpha < 0:
            raise ValueError(f"cuts[{index}].weight must be nonnegative")
        add_scaled(conic_slack, outer(v), alpha)
        cuts.append((v, alpha))
    if slack != conic_slack:
        raise ValueError(
            "dual slack does not equal the nonnegative combination of rank-one cut matrices; "
            f"slack={text_matrix(slack)}, combination={text_matrix(conic_slack)}"
        )

    x = matrix(certificate.get("primal_X"), n, "certificate.primal_X")
    principal_minors = assert_psd(x, "certificate.primal_X")
    for i, ai in enumerate(a):
        value = dot_matrix(ai, x)
        if value != b[i]:
            raise ValueError(f"primal equality {i} fails: <A[{i}],X>={value}, expected {b[i]}")
    for i, (v, _) in enumerate(cuts):
        value = sum((v[row] * x[row][col] * v[col] for row in range(n) for col in range(n)), Fraction(0))
        if value < 0:
            raise ValueError(f"PSD primal witness violates cut {i}: v^T X v={value}")
    bound = sum((b[i] * y[i] for i in range(len(a))), Fraction(0))
    primal_objective = dot_matrix(c, x)
    if primal_objective != bound:
        raise ValueError(f"objective mismatch: <C,X>={primal_objective}, b^T y={bound}")
    return {
        "status": "verified-sdp-lp-value-match",
        "value": str(bound),
        "dimension": n,
        "affine_equalities": len(a),
        "rank_one_cuts": len(cuts),
        "psd_principal_minors_checked": principal_minors,
        "method": "exact rational primal-dual equality plus nonnegative rank-one slack decomposition",
        "scope": "the stated minimization SDP and the LP retaining exactly the stated rank-one cuts",
        "not_certified": "how to find the dual optimum/cuts, a general LP replacement, numerical SDP output, or rank-one primal recovery",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON certificate")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        result = verify(payload)
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
