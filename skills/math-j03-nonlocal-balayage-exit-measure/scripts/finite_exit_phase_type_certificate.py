#!/usr/bin/env python3
"""Exact all-time exit law, occupation and moments for a finite absorbing CTMC.

All rates and initial masses are parsed as fractions.  The program accepts only a
finite chain for which every transient state graph-reaches a declared absorbing
physical-exit state.  That finite graph certificate rules out a closed transient
class, hence makes the exit time phase-type and all output moments finite.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def f(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("numbers must be exact integer or rational strings, never floats")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational: {value!r}") from exc


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def total(values: Iterable[Fraction]) -> Fraction:
    return sum(values, Fraction(0))


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return [[total(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rowmat(v: list[Fraction], a: list[list[Fraction]]) -> list[Fraction]:
    return [total(v[i] * a[i][j] for i in range(len(v))) for j in range(len(a[0]))]


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("expected nonempty square matrix")
    work = [row[:] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            raise ValueError("transient generator is singular; no finite all-time certificate")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [x / scale for x in work[col]]
        for row in range(n):
            if row == col:
                continue
            scale = work[row][col]
            if scale:
                work[row] = [work[row][j] - scale * work[col][j] for j in range(2 * n)]
    return [row[n:] for row in work]


def parse(data: dict[str, Any]) -> tuple[list[str], list[list[Fraction]], list[int], dict[str, list[int]], list[Fraction], int, list[Fraction]]:
    labels = data.get("state_labels")
    if not isinstance(labels, list) or not labels or not all(isinstance(x, str) and x for x in labels) or len(set(labels)) != len(labels):
        raise ValueError("state_labels must be distinct nonempty strings")
    index = {x: i for i, x in enumerate(labels)}
    n = len(labels)
    raw_q = data.get("generator")
    if not isinstance(raw_q, list) or len(raw_q) != n or any(not isinstance(row, list) or len(row) != n for row in raw_q):
        raise ValueError("generator must be square and match state_labels")
    q = [[f(x) for x in row] for row in raw_q]
    for i, row in enumerate(q):
        if any(row[j] < 0 for j in range(n) if j != i) or row[i] > 0 or row[i] != -total(row[j] for j in range(n) if j != i):
            raise ValueError(f"generator row {i} is not conservative with nonnegative off-diagonals")
    try:
        transient = [index[x] for x in data["transient"]]
        raw_classes = data["exit_classes"]
    except (KeyError, TypeError) as exc:
        raise ValueError("transient and exit_classes are required") from exc
    if not transient or len(set(transient)) != len(transient):
        raise ValueError("transient must be a nonempty nonrepeating list")
    if not isinstance(raw_classes, dict) or not raw_classes or not all(isinstance(key, str) and key for key in raw_classes):
        raise ValueError("exit_classes must be a nonempty object mapping names to state-label lists")
    classes: dict[str, list[int]] = {}
    for name, values in raw_classes.items():
        if not isinstance(values, list) or not values:
            raise ValueError("each exit class needs at least one state")
        try:
            classes[name] = [index[x] for x in values]
        except KeyError as exc:
            raise ValueError(f"unknown state in exit class {name}") from exc
    exits = [i for values in classes.values() for i in values]
    if len(set(exits)) != len(exits) or set(transient) & set(exits) or set(transient) | set(exits) != set(range(n)):
        raise ValueError("transient and all exit classes must form a disjoint partition of the state set")
    for i in exits:
        if any(q[i][j] != 0 for j in range(n)):
            raise ValueError("declared exit states must be absorbing; use a killed/stopped chain")
    raw_initial = data.get("initial")
    if not isinstance(raw_initial, list) or len(raw_initial) != n:
        raise ValueError("initial must have one exact mass per state")
    initial = [f(x) for x in raw_initial]
    if any(x < 0 for x in initial) or total(initial) != 1:
        raise ValueError("initial must be a nonnegative probability vector")
    if any(initial[i] != 0 for i in exits):
        raise ValueError("initial exit mass is excluded: this finite-phase tool assumes the process starts in transient states")
    max_moment = data.get("max_moment", 2)
    if not isinstance(max_moment, int) or isinstance(max_moment, bool) or not 1 <= max_moment <= 8:
        raise ValueError("max_moment must be an integer from 1 to 8")
    laplace_points = [f(x) for x in data.get("laplace_points", [])]
    if any(x < 0 for x in laplace_points):
        raise ValueError("laplace_points must be nonnegative")
    return labels, q, transient, classes, initial, max_moment, laplace_points


def reaches_exit(q: list[list[Fraction]], transient: list[int], exits: set[int]) -> tuple[bool, list[int]]:
    """Graph certificate: reverse-search exit nodes through positive-rate arcs."""
    n = len(q)
    reached = set(exits)
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i not in reached and any(q[i][j] > 0 for j in reached):
                reached.add(i)
                changed = True
    missing = [i for i in transient if i not in reached]
    return not missing, missing


def serial_matrix(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[fs(x) for x in row] for row in matrix]


def certify(data: dict[str, Any]) -> dict[str, Any]:
    labels, q, transient, classes, initial, max_moment, laplace_points = parse(data)
    exits = {i for states in classes.values() for i in states}
    ok, missing = reaches_exit(q, transient, exits)
    if not ok:
        names = ", ".join(labels[i] for i in missing)
        raise ValueError(f"not every transient state graph-reaches physical exit ({names}); all-time mean may be infinite")
    nt = len(transient)
    qtt = [[q[i][j] for j in transient] for i in transient]
    h = [[-qtt[i][j] for j in range(nt)] for i in range(nt)]
    green = inverse(h)  # Integral_0^infty exp(Q_TT t) dt.
    class_names = list(classes)
    b = [[total(q[i][j] for j in classes[name]) for name in class_names] for i in transient]
    exit_by_start = matmul(green, b)
    alpha = [initial[i] for i in transient]
    exit_initial = rowmat(alpha, exit_by_start)
    ones = [[Fraction(1)] for _ in range(nt)]
    moment_columns: list[list[Fraction]] = [[row[0] for row in matmul(green, ones)]]
    for order in range(2, max_moment + 1):
        prior = [[x] for x in moment_columns[-1]]
        moment_columns.append([order * row[0] for row in matmul(green, prior)])
    moments_initial = [total(alpha[i] * column[i] for i in range(nt)) for column in moment_columns]
    variance = moments_initial[1] - moments_initial[0] ** 2 if len(moments_initial) >= 2 else None
    transform: dict[str, Any] = {}
    identity = [[Fraction(int(i == j)) for j in range(nt)] for i in range(nt)]
    for s in laplace_points:
        resolvent = inverse([[s * identity[i][j] - qtt[i][j] for j in range(nt)] for i in range(nt)])
        by_class = rowmat(alpha, matmul(resolvent, b))
        transform[fs(s)] = {"by_exit_class": {name: fs(by_class[j]) for j, name in enumerate(class_names)}, "total": fs(total(by_class))}
    return {
        "certificate_kind": "finite absorbing CTMC all-time phase-type certificate (exact rationals)",
        "assumption_certificate": {
            "finite_conservative_generator": True,
            "exit_states_absorbing": True,
            "graph_reachability": "every transient state has a positive-rate directed path to a physical-exit state",
            "consequence": "no closed transient communicating class; absorption occurs almost surely and every exit-time moment is finite",
        },
        "formulas": {
            "green": "G=(-Q_TT)^(-1)=integral_0^infinity exp(Q_TT t) dt",
            "exit_classes": "H=G Q_TE",
            "moments": "m_1=G 1; m_k=k G m_(k-1)",
            "laplace": "E_alpha[exp(-s tau); exit class]=alpha (sI-Q_TT)^(-1) Q_TE",
        },
        "state_order": [labels[i] for i in transient],
        "exit_class_order": class_names,
        "green_occupation_time_by_start_and_transient_state": serial_matrix(green),
        "exit_probability_by_start_and_class": serial_matrix(exit_by_start),
        "initial_distribution_on_transient_order": [fs(x) for x in alpha],
        "exit_probability_by_initial_class": {name: fs(exit_initial[j]) for j, name in enumerate(class_names)},
        "mean_exit_time_by_start": {labels[transient[i]]: fs(moment_columns[0][i]) for i in range(nt)},
        "raw_moment_by_initial_order_1_to_k": [fs(x) for x in moments_initial],
        "variance_by_initial": fs(variance) if variance is not None else None,
        "laplace_transform_by_initial": transform,
        "limits": [
            "The certificate is for the supplied finite killed chain, not an infinite-state truncation or a continuum nonlocal PDE discretization.",
            "If graph reachability fails, this tool refuses an all-time mean/moment claim; finite-horizon exit probability may still be meaningful.",
            "The exit classes must represent physical absorption. A truncation loss state must not be included unless the modelling question defines it as physical exit.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            result = certify(json.load(handle))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
