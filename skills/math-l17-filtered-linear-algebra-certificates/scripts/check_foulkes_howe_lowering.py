#!/usr/bin/env python3
"""Exact sparse finite-bidegree replay for D_{Y,U}=sum_i Y_i d/dU_i."""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


def compositions(total: int, n: int) -> list[tuple[int, ...]]:
    if n == 1:
        return [(total,)]
    return [(a,) + tail for a in range(total + 1) for tail in compositions(total - a, n - 1)]


def parse_fraction(value: object) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean is not a rational coefficient")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("coefficient must be an integer or a rational string")


def rank(rows: list[dict[int, Fraction]]) -> int:
    """Fraction-exact Gaussian elimination on a sparse row dictionary."""
    pivot_row = 0
    columns = sorted({j for row in rows for j in row})
    for col in columns:
        source = next((r for r in range(pivot_row, len(rows)) if rows[r].get(col, 0)), None)
        if source is None:
            continue
        rows[pivot_row], rows[source] = rows[source], rows[pivot_row]
        pivot = rows[pivot_row][col]
        rows[pivot_row] = {j: x / pivot for j, x in rows[pivot_row].items() if x / pivot}
        for r, row in enumerate(rows):
            if r == pivot_row or not (scale := row.get(col, 0)):
                continue
            changed = dict(row)
            for j, x in rows[pivot_row].items():
                changed[j] = changed.get(j, Fraction(0)) - scale * x
                if not changed[j]:
                    del changed[j]
            rows[r] = changed
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def error(message: str) -> None:
    print(json.dumps({"ok": False, "error": message}, sort_keys=True))
    raise SystemExit(2)


def format_term(exponents: tuple[int, ...], coefficient: Fraction) -> dict[str, object]:
    n = len(exponents) // 2
    return {"u": list(exponents[:n]), "y": list(exponents[n:]), "coefficient": str(coefficient)}


def main(path: str) -> None:
    try:
        data = json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error(f"invalid JSON: {exc}")
    permitted = {"n", "u_degree", "y_degree", "coefficients"}
    if not isinstance(data, dict) or set(data) - permitted or not {"n", "u_degree", "y_degree"} <= set(data):
        error("need n, u_degree, y_degree and optional coefficients only")
    n, p, q = (data["n"], data["u_degree"], data["y_degree"])
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (n, p, q)) or n < 1 or p < 1 or q < 0:
        error("require integer n>=1, u_degree>=1, y_degree>=0")
    source = [u + y for u in compositions(p, n) for y in compositions(q, n)]
    target = [u + y for u in compositions(p - 1, n) for y in compositions(q + 1, n)]
    target_index = {m: i for i, m in enumerate(target)}
    rows = [dict() for _ in target]
    columns: list[list[tuple[int, Fraction]]] = []
    for col, monomial in enumerate(source):
        u, y = monomial[:n], monomial[n:]
        sparse: list[tuple[int, Fraction]] = []
        for i, exponent in enumerate(u):
            if exponent:
                next_u, next_y = list(u), list(y)
                next_u[i] -= 1
                next_y[i] += 1
                row = target_index[tuple(next_u + next_y)]
                value = Fraction(exponent)
                rows[row][col] = value
                sparse.append((row, value))
        columns.append(sparse)
    matrix_rank = rank([dict(row) for row in rows])
    supplied: dict[tuple[int, ...], Fraction] = {}
    raw_terms = data.get("coefficients")
    if raw_terms is not None:
        if not isinstance(raw_terms, list):
            error("coefficients must be a list")
        source_index = {m: i for i, m in enumerate(source)}
        for k, term in enumerate(raw_terms, 1):
            if not isinstance(term, dict) or set(term) != {"u", "y", "coefficient"}:
                error(f"coefficient term {k} needs exactly u, y, coefficient")
            u, y = term["u"], term["y"]
            if not isinstance(u, list) or not isinstance(y, list):
                error(f"coefficient term {k} needs list exponent vectors")
            if not all(isinstance(v, int) and not isinstance(v, bool) and v >= 0 for v in u + y) or len(u) != n or len(y) != n:
                error(f"coefficient term {k} has invalid exponent vectors")
            if sum(u) != p or sum(y) != q:
                error(f"coefficient term {k} is not of bidegree ({p},{q})")
            try:
                coefficient = parse_fraction(term["coefficient"])
            except (ValueError, ZeroDivisionError) as exc:
                error(f"coefficient term {k}: {exc}")
            monomial = tuple(u + y)
            assert monomial in source_index
            supplied[monomial] = supplied.get(monomial, Fraction(0)) + coefficient
            if not supplied[monomial]:
                del supplied[monomial]
    image: dict[tuple[int, ...], Fraction] = {}
    if supplied:
        source_index = {m: i for i, m in enumerate(source)}
        for monomial, coefficient in supplied.items():
            for row, factor in columns[source_index[monomial]]:
                target_monomial = target[row]
                image[target_monomial] = image.get(target_monomial, Fraction(0)) + coefficient * factor
                if not image[target_monomial]:
                    del image[target_monomial]
    out: dict[str, object] = {
        "ok": True,
        "operator": "sum_i Y_i*d/dU_i",
        "n": n,
        "bidegree": [p, q],
        "target_bidegree": [p - 1, q + 1],
        "domain_dimension": len(source),
        "codomain_dimension": len(target),
        "sparse_nonzeros": sum(len(col) for col in columns),
        "rank": matrix_rank,
        "full_column_rank": matrix_rank == len(source),
        "source_claim_regime_p_gt_q": p > q,
    }
    if raw_terms is not None:
        out["input_terms"] = [format_term(m, c) for m, c in sorted(supplied.items())]
        out["lowered_terms"] = [format_term(m, c) for m, c in sorted(image.items())]
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_foulkes_howe_lowering.py INSTANCE.json", file=sys.stderr)
        raise SystemExit(2)
    main(sys.argv[1])
