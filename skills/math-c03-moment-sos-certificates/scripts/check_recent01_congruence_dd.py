#!/usr/bin/env python3
"""Exact congruence/strict-diagonal-dominance verifier for a rational Gram matrix."""
from __future__ import annotations
import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

def integer(value: object, label: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be an integer")
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be an integer") from exc
    if str(result) != str(value):
        raise ValueError(f"{label} must be an integer")
    return result

def matrix(value: object, label: str, size: int | None = None) -> list[list[int]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a nonempty square matrix")
    n = len(value) if size is None else size
    if len(value) != n:
        raise ValueError(f"{label} has wrong row count")
    rows: list[list[int]] = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"{label}[{i}] has wrong column count")
        rows.append([integer(entry, f"{label}[{i}][{j}]") for j, entry in enumerate(row)])
    return rows

def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]

def verify(payload: dict[str, object]) -> dict[str, object]:
    c = Fraction(str(payload.get("positive_scale")))
    if c <= 0:
        raise ValueError("positive_scale must be strictly positive")
    a = matrix(payload.get("integer_matrix_A"), "integer_matrix_A")
    n = len(a)
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("integer_matrix_A must be symmetric")
    r = matrix(payload.get("integer_matrix_R"), "integer_matrix_R", n)
    rt = [list(column) for column in zip(*r)]
    j = multiply(multiply(r, a), rt)
    margins = [j[i][i] - sum(abs(j[i][k]) for k in range(n) if k != i) for i in range(n)]
    if any(margin <= 0 for margin in margins):
        raise ValueError(f"strict diagonal dominance fails; row margins={margins}")
    return {"status":"verified-congruence-strict-dd","dimension":n,"positive_scale":str(c),"row_margins":margins,"certifies":"Q=A/positive_scale is positive definite"}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text())
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(verify(payload), sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError, ZeroDivisionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
