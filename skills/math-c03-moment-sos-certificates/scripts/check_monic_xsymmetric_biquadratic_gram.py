#!/usr/bin/env python3
"""Exact Gram constructor/checker for a monic x-symmetric biquadratic form.

For m >= 2 and rational symmetric n-by-n A,B with diag(B)=0, this checks
 Q = I+B-A >= 0,     R = I+B+(m-1)A >= 0,
and the explicit coefficient tensor T_{ij,kl} against the Gram matrix
 M = I_m kron Q + (1/m) 11^T kron (R-Q).
The ordering is (i,j) -> i*n+j, zero based.  Equality with T proves exactly
 P(x,y)=sum T[i][j][k][l] x_i y_j x_k y_l=(x kron y)^T M(x kron y).
The block identity makes M PSD and gives rank(M)=rank(R)+(m-1)rank(Q).
It verifies a structured certificate; it does not test arbitrary biquadratic PSD.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


MAX_SMALL_BLOCK_DIMENSION = 12


def q(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all scalars must be exact integers or rational strings; floats are forbidden")
    if isinstance(value, (int, str)):
        return Fraction(value)
    raise ValueError(f"not an exact rational: {value!r}")


def matrix(raw: Any, n: int | None = None, name: str = "matrix") -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"{name} must be a nonempty square list of lists")
    size = len(raw)
    if n is not None and size != n:
        raise ValueError(f"{name} has dimension {size}, expected {n}")
    answer: list[list[Fraction]] = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != size:
            raise ValueError(f"{name}[{i}] must have length {size}")
        answer.append([q(value) for value in row])
    for i in range(size):
        for j in range(size):
            if answer[i][j] != answer[j][i]:
                raise ValueError(f"{name} is not symmetric at ({i},{j})")
    return answer


def determinant(a: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in a]
    answer, sign = Fraction(1), Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign = -sign
        p = work[col][col]
        answer *= p
        for row in range(col + 1, len(work)):
            factor = work[row][col] / p
            for right in range(col + 1, len(work)):
                work[row][right] -= factor * work[col][right]
            work[row][col] = Fraction(0)
    return sign * answer


def assert_psd(a: list[list[Fraction]], name: str) -> int:
    n = len(a)
    if n > MAX_SMALL_BLOCK_DIMENSION:
        raise ValueError(f"{name} has dimension {n}; exact principal-minor mode is capped at {MAX_SMALL_BLOCK_DIMENSION}")
    checked = 0
    for size in range(1, n + 1):
        for indices in itertools.combinations(range(n), size):
            value = determinant([[a[i][j] for j in indices] for i in indices])
            checked += 1
            if value < 0:
                raise ValueError(f"{name} is not PSD: principal minor {indices} equals {value}")
    return checked


def rank(a: list[list[Fraction]]) -> int:
    work = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        p = work[pivot_row][col]
        for row in range(pivot_row + 1, len(work)):
            factor = work[row][col] / p
            for right in range(col, len(work[0])):
                work[row][right] -= factor * work[pivot_row][right]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def construct_gram(m: int, q_block: list[list[Fraction]], r_block: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(q_block)
    answer = [[Fraction(0) for _ in range(m * n)] for _ in range(m * n)]
    for i in range(m):
        for k in range(m):
            for j in range(n):
                for ell in range(n):
                    value = (r_block[j][ell] - q_block[j][ell]) / m
                    if i == k:
                        value += q_block[j][ell]
                    answer[i * n + j][k * n + ell] = value
    return answer


def parse_tensor(raw: Any, m: int, n: int) -> list[list[list[list[Fraction]]]]:
    if not isinstance(raw, list) or len(raw) != m:
        raise ValueError(f"coefficient_tensor must have {m} outer x-index entries")
    answer = []
    for i, by_j in enumerate(raw):
        if not isinstance(by_j, list) or len(by_j) != n:
            raise ValueError(f"coefficient_tensor[{i}] must have {n} y-index entries")
        parsed_j = []
        for j, by_k in enumerate(by_j):
            if not isinstance(by_k, list) or len(by_k) != m:
                raise ValueError(f"coefficient_tensor[{i}][{j}] must have {m} second x-index entries")
            parsed_k = []
            for k, by_l in enumerate(by_k):
                if not isinstance(by_l, list) or len(by_l) != n:
                    raise ValueError(f"coefficient_tensor[{i}][{j}][{k}] must have {n} second y-index entries")
                parsed_k.append([q(value) for value in by_l])
            parsed_j.append(parsed_k)
        answer.append(parsed_j)
    return answer


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in a]


def verify(payload: dict[str, Any], emit_gram: bool) -> dict[str, Any]:
    m = payload.get("m")
    if not isinstance(m, int) or isinstance(m, bool) or m < 2:
        raise ValueError("m must be an integer at least 2")
    a = matrix(payload.get("A"), name="A")
    n = len(a)
    b = matrix(payload.get("B"), n, "B")
    if any(b[i][i] != 0 for i in range(n)):
        raise ValueError("monic x-symmetric input requires zero diagonal in B")
    q_block = matrix(payload.get("Q"), n, "Q")
    r_block = matrix(payload.get("R"), n, "R")
    expected_q = [[(Fraction(1) if i == j else Fraction(0)) + b[i][j] - a[i][j] for j in range(n)] for i in range(n)]
    expected_r = [[(Fraction(1) if i == j else Fraction(0)) + b[i][j] + (m - 1) * a[i][j] for j in range(n)] for i in range(n)]
    if q_block != expected_q:
        raise ValueError(f"Q must equal I+B-A exactly; expected {strings(expected_q)}")
    if r_block != expected_r:
        raise ValueError(f"R must equal I+B+(m-1)A exactly; expected {strings(expected_r)}")
    q_minors = assert_psd(q_block, "Q")
    r_minors = assert_psd(r_block, "R")
    gram = construct_gram(m, q_block, r_block)
    tensor = parse_tensor(payload.get("coefficient_tensor"), m, n)
    for i in range(m):
        for j in range(n):
            for k in range(m):
                for ell in range(n):
                    expected = gram[i * n + j][k * n + ell]
                    if tensor[i][j][k][ell] != expected:
                        raise ValueError(
                            "coefficient tensor/Gram mismatch at "
                            f"({i},{j},{k},{ell}): got {tensor[i][j][k][ell]}, expected {expected}"
                        )
    q_rank, r_rank = rank(q_block), rank(r_block)
    result: dict[str, Any] = {
        "status": "verified-monic-xsymmetric-biquadratic-sos-gram",
        "m": m,
        "n": n,
        "small_psd_principal_minors_checked": {"Q": q_minors, "R": r_minors},
        "tensor_to_form_identity": "verified exactly in ordering (i,j)->i*n+j",
        "gram_construction": "M=I_m kron Q+(1/m)11^T kron(R-Q)",
        "sos_rank_construction_bound": r_rank + (m - 1) * q_rank,
        "rank_Q": q_rank,
        "rank_R": r_rank,
        "scope": "the supplied monic x-symmetric coefficient tensor only",
        "not_certified": "arbitrary biquadratic PSD, a rational square-factor list, numerical eigenvalue tests, or a general SOS hierarchy",
    }
    if emit_gram:
        result["gram_matrix"] = strings(gram)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="structured rational coefficient JSON")
    parser.add_argument("--emit-gram", action="store_true", help="include the constructed exact Gram matrix in JSON output")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        result = verify(payload, args.emit_gram)
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
