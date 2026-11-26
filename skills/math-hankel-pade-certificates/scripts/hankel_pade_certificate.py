#!/usr/bin/env python3
"""Exact finite Hankel--Pade certificates; no global theorem admission."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def as_fraction(value: object) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean is not a rational coefficient")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational value: {value!r}")


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Exact determinant using fraction-preserving row elimination."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant matrix must be square")
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result = -result
        pivot_value = work[col][col]
        result *= pivot_value
        for row in range(col + 1, n):
            if not work[row][col]:
                continue
            factor = work[row][col] / pivot_value
            for j in range(col + 1, n):
                work[row][j] -= factor * work[col][j]
            work[row][col] = Fraction(0)
    return result


def solve_unique(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """Solve a nonsingular square system exactly, rejecting singular input."""
    n = len(matrix)
    if len(rhs) != n or any(len(row) != n for row in matrix):
        raise ValueError("invalid square linear system")
    work = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            raise ValueError("singular Padé denominator system")
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
        pivot_value = work[col][col]
        work[col] = [entry / pivot_value for entry in work[col]]
        for row in range(n):
            if row == col or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [work[row][j] - factor * work[col][j] for j in range(n + 1)]
    return [work[row][-1] for row in range(n)]


def hankel(coefficients: list[Fraction], n: int) -> Fraction:
    if n < 0 or 2 * n - 2 >= len(coefficients) and n:
        raise ValueError(f"need coefficients through c_{2 * n - 2} for H_{n}")
    return determinant([[coefficients[i + j] for j in range(n)] for i in range(n)])


def bordered_hankel(coefficients: list[Fraction], k: int, r: int) -> Fraction:
    if not (k <= r):
        raise ValueError("bordered determinant needs r >= k")
    if k + r >= len(coefficients):
        raise ValueError(f"need coefficients through c_{k + r} for H_({k},{r})")
    matrix = [[coefficients[i + j] for j in range(k + 1)] for i in range(k)]
    matrix.append([coefficients[r + j] for j in range(k + 1)])
    return determinant(matrix)


def multiply_truncated(left: list[Fraction], right: list[Fraction], maximum: int) -> list[Fraction]:
    return [sum((left[j] * right[index - j] for j in range(max(0, index - len(right) + 1), min(index, len(left) - 1) + 1)), Fraction(0)) for index in range(maximum + 1)]


def pade_certificate(coefficients: list[Fraction], k: int, ell: int) -> dict[str, object]:
    if not (1 <= k < ell):
        raise ValueError("require 1 <= order < later_order")
    h_k = hankel(coefficients, k)
    h_ell = hankel(coefficients, ell)
    result: dict[str, object] = {
        "order": k,
        "later_order": ell,
        "H_k": show(h_k),
        "H_ell": show(h_ell),
    }
    if not h_k or not h_ell:
        result.update({
            "finite_certificate": "ineligible",
            "reason": "Theorem 3.1 finite witness requires both H_k and H_ell nonzero.",
        })
        return result

    border_values = [(r, bordered_hankel(coefficients, k, r)) for r in range(k, ell)]
    nonzero = next(((r, value) for r, value in border_values if value), None)
    if nonzero is None:  # Inconsistent with H_ell != 0, retained as a defensive check.
        raise AssertionError("H_ell nonzero but no required bordered minor was found")
    r, h_kr = nonzero

    # Q(z)=1+q_1 z+...+q_k z^k.  Its coefficients z^k,...,z^(2k-1)
    # in Qf vanish.  The coefficient matrix is a reversed H_k matrix.
    system = [[coefficients[k + row - (column + 1)] for column in range(k)] for row in range(k)]
    q_tail = solve_unique(system, [-coefficients[k + row] for row in range(k)])
    denominator = [Fraction(1)] + q_tail
    numerator = multiply_truncated(denominator, coefficients, k - 1)
    product = multiply_truncated(denominator, coefficients, k + r)
    residual = product[:]
    for index in range(k):
        residual[index] -= numerator[index]
    first_nonzero = next((index for index, value in enumerate(residual) if value), None)
    expected = h_kr / h_k
    if first_nonzero != k + r or residual[k + r] != expected:
        raise AssertionError("independent Padé replay disagrees with the bordered determinant identity")

    result.update({
        "finite_certificate": "certified",
        "least_border_index": r,
        "bordered_H_k_r": show(h_kr),
        "P_coefficients_low_to_high": [show(value) for value in numerator],
        "Q_coefficients_low_to_high": [show(value) for value in denominator],
        "first_residual_power": first_nonzero,
        "first_residual_coefficient": show(residual[first_nonzero]),
        "bordered_ratio_H_k_r_over_H_k": show(expected),
        "identity_checked": "Q(z) f(z)-P(z) has zero coefficients below z^(k+r), with the displayed exact leading coefficient.",
        "bordered_candidates": [{"r": index, "H_k_r": show(value)} for index, value in border_values],
    })
    return result


def evaluate_polynomial(coefficients: Iterable[Fraction], point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(list(coefficients)):
        value = value * point + coefficient
    return value


def theorem_2_1_prefix(raw: object) -> dict[str, object] | None:
    if raw is None:
        return None
    if not isinstance(raw, dict):
        raise ValueError("theorem_2_1 must be an object")
    d = raw.get("d")
    b = raw.get("b")
    prefix = raw.get("nonvanishing_prefix", 0)
    if not isinstance(d, int) or d < 2 or not isinstance(b, int) or b < 2:
        raise ValueError("theorem_2_1 requires integer d>=2 and b>=2")
    if not isinstance(prefix, int) or prefix < 0:
        raise ValueError("nonvanishing_prefix must be a nonnegative integer")
    b_poly = [as_fraction(value) for value in raw.get("B", [])]
    c_poly = [as_fraction(value) for value in raw.get("C", [])]
    if not b_poly or not c_poly:
        raise ValueError("theorem_2_1 requires nonempty ascending-coefficient B and C")
    rows = []
    for m in range(prefix):
        point = Fraction(1, b ** (d ** m))
        b_value = evaluate_polynomial(b_poly, point)
        c_value = evaluate_polynomial(c_poly, point)
        rows.append({"m": m, "point": show(point), "B_value": show(b_value), "C_value": show(c_value), "nonzero": bool(b_value and c_value)})
    return {
        "theorem": "Bugeaud--Han--Wen--Yao Theorem 2.1 (arXiv:1503.02797v2)",
        "finite_b_nonvanishing": {
            "checked_m": f"0..{prefix - 1}" if prefix else "empty prefix",
            "all_checked_nonzero": all(row["nonzero"] for row in rows),
            "rows": rows,
            "scope": "finite_prefix_only; this does not prove nonvanishing for every m>=0",
        },
        "separate_global_gates": {
            "formal_functional_equation_and_unit_disk_convergence": "external proof required; not certified from coefficient prefix",
            "infinite_nonzero_Hankel_subsequence_with_successive_ratio_tending_to_1": "external proof required; not certified from finite determinants",
            "b_admissibility_for_every_m": "external proof required; finite prefix is reported above",
        },
        "user_audit_notes": {
            "functional_equation_proof": raw.get("functional_equation_proof", "not supplied"),
            "infinite_hankel_proof": raw.get("infinite_hankel_proof", "not supplied"),
        },
        "theorem_conclusion": "not asserted by this finite computation",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} INPUT.json", file=sys.stderr)
        return 2
    try:
        raw = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("top-level JSON must be an object")
        coefficients = [as_fraction(value) for value in raw["coefficients"]]
        output: dict[str, object] = {
            "series_indexing": "coefficients[0] is c_0 in f(z)=sum_{j>=0} c_j z^j",
            "arithmetic": "exact fractions.Fraction arithmetic",
            "finite_hankel_pade": pade_certificate(coefficients, raw["order"], raw["later_order"]),
        }
        gates = theorem_2_1_prefix(raw.get("theorem_2_1"))
        if gates is not None:
            output["theorem_2_1_audit"] = gates
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (KeyError, TypeError, ValueError) as error:
        print(f"input error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
