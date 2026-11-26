#!/usr/bin/env python3
"""Exact checker for supplied Graver-style integer augmentations.

This is a finite verifier, not a Graver-basis generator.  Its conditional
optimality claim requires every Graver direction of A to be supplied.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Callable


class InputError(ValueError):
    """A precise failure in a purported exact-integer instance."""


def int_value(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InputError(f"{name} must be an integer")
    return value


def vector(value: Any, name: str, n: int | None = None) -> list[int]:
    if not isinstance(value, list):
        raise InputError(f"{name} must be a JSON list")
    out = [int_value(v, f"{name}[{i}]") for i, v in enumerate(value)]
    if n is not None and len(out) != n:
        raise InputError(f"{name} has length {len(out)}, expected {n}")
    return out


def dot(row: list[int], point: list[int]) -> int:
    return sum(a * x for a, x in zip(row, point))


def objective_from(raw: Any, lo: list[int], hi: list[int]) -> tuple[Callable[[list[int]], int], str, bool]:
    if not isinstance(raw, dict):
        raise InputError("objective must be an object")
    n = len(lo)
    kind = raw.get("type")
    if kind == "separable_quadratic":
        q = vector(raw.get("quadratic"), "objective.quadratic", n)
        c = vector(raw.get("linear"), "objective.linear", n)
        if any(v < 0 for v in q):
            raise InputError("quadratic coefficients must be nonnegative for convexity")
        return (lambda x: sum(q[i] * x[i] * x[i] + c[i] * x[i] for i in range(n)),
                "separable convex integer quadratic", True)
    if kind == "separable_values":
        raw_tables = raw.get("tables")
        if not isinstance(raw_tables, list) or len(raw_tables) != n:
            raise InputError("objective.tables must contain one table per coordinate")
        tables: list[dict[int, int]] = []
        for i, raw_table in enumerate(raw_tables):
            if not isinstance(raw_table, dict):
                raise InputError(f"objective.tables[{i}] must be an object")
            table: dict[int, int] = {}
            for key, value in raw_table.items():
                try:
                    k = int(key)
                except ValueError as error:
                    raise InputError(f"objective.tables[{i}] has noninteger key {key!r}") from error
                if str(k) != key:
                    raise InputError(f"objective.tables[{i}] key {key!r} is not canonical")
                table[k] = int_value(value, f"objective.tables[{i}][{key!r}]")
            if len(table) != hi[i] - lo[i] + 1 or any(not lo[i] <= k <= hi[i] for k in table):
                raise InputError(f"objective.tables[{i}] must define exactly its bounded integer domain")
            tables.append(table)
        convex = all(
            table[k-1] + table[k+1] >= 2 * table[k]
            for i, table in enumerate(tables)
            for k in range(lo[i] + 1, hi[i])
        )
        return (lambda x: sum(tables[i][x[i]] for i in range(n)),
                "finite separable value tables", convex)
    raise InputError("objective.type must be separable_quadratic or separable_values")


def parse(data: Any) -> tuple[list[list[int]], list[int], list[int], list[int], list[int], list[list[int]], Callable[[list[int]], int], str, bool]:
    if not isinstance(data, dict):
        raise InputError("top-level JSON must be an object")
    raw_A = data.get("A")
    if not isinstance(raw_A, list) or not raw_A or not isinstance(raw_A[0], list) or not raw_A[0]:
        raise InputError("A must be a nonempty matrix with a positive column count")
    n = len(raw_A[0])
    A = [vector(row, f"A[{i}]", n) for i, row in enumerate(raw_A)]
    b, lo, hi, x = (vector(data.get(name), name, size) for name, size in
                    (("b", len(A)), ("lower", n), ("upper", n), ("x", n)))
    for i, (lower, upper, value) in enumerate(zip(lo, hi, x)):
        if lower > upper:
            raise InputError(f"lower[{i}] exceeds upper[{i}]")
        if not lower <= value <= upper:
            raise InputError(f"x[{i}] violates its inclusive bounds")
    if [dot(row, x) for row in A] != b:
        raise InputError("x is not feasible: A*x differs from b")
    raw_dirs = data.get("directions")
    if not isinstance(raw_dirs, list):
        raise InputError("directions must be a JSON list")
    directions: list[list[int]] = []
    seen: set[tuple[int, ...]] = set()
    for i, raw_direction in enumerate(raw_dirs):
        direction = vector(raw_direction, f"directions[{i}]", n)
        if not any(direction):
            raise InputError(f"directions[{i}] is zero")
        if tuple(direction) in seen:
            raise InputError(f"directions[{i}] duplicates an earlier direction")
        if any(dot(row, direction) for row in A):
            raise InputError(f"directions[{i}] is not in ker_Z(A)")
        seen.add(tuple(direction))
        directions.append(direction)
    objective, scope, convex = objective_from(data.get("objective"), lo, hi)
    return A, b, lo, hi, x, directions, objective, scope, convex


def max_step(x: list[int], g: list[int], lo: list[int], hi: list[int]) -> int:
    caps = []
    for value, delta, lower, upper in zip(x, g, lo, hi):
        if delta > 0:
            caps.append((upper - value) // delta)
        elif delta < 0:
            caps.append((value - lower) // -delta)
    return min(caps)


def line_minimum(
    x: list[int],
    g: list[int],
    lo: list[int],
    hi: list[int],
    f: Callable[[list[int]], int],
    *,
    convex: bool,
) -> tuple[int, list[int], int] | None:
    cap = max_step(x, g, lo, hi)
    if cap < 1:
        return None

    def point(step: int) -> list[int]:
        return [value + step * delta for value, delta in zip(x, g, strict=True)]

    if convex:
        left, right = 0, cap
        while left < right:
            mid = (left + right) // 2
            if f(point(mid)) <= f(point(mid + 1)):
                right = mid
            else:
                left = mid + 1
        step = left
        value = f(point(step))
    else:
        value, step = min((f(point(t)), t) for t in range(1, cap + 1))
    if value >= f(x):
        return None
    return step, point(step), value


def augment(lo: list[int], hi: list[int], start: list[int], directions: list[list[int]], f: Callable[[list[int]], int], cap: int, *, convex: bool) -> tuple[list[int], list[dict[str, Any]], bool]:
    x, trace = start[:], []
    for _ in range(cap):
        candidates = []
        for g in directions:
            result = line_minimum(x, g, lo, hi, f, convex=convex)
            if result is not None:
                step, target, value = result
                candidates.append((value, step, tuple(g), target))
        if not candidates:
            return x, trace, True
        value, step, direction, target = min(candidates)
        trace.append({"direction": list(direction), "step": step, "objective_after": value, "point_after": target})
        x = target
    return x, trace, False


def exhaustive(A: list[list[int]], b: list[int], lo: list[int], hi: list[int], f: Callable[[list[int]], int], cap: int) -> dict[str, Any]:
    total = math.prod(upper - lower + 1 for lower, upper in zip(lo, hi))
    if total > cap:
        raise InputError(f"box has {total} points, above --exhaustive-cap={cap}")
    best: tuple[int, list[int]] | None = None
    feasible = 0
    for values in itertools.product(*(range(lower, upper + 1) for lower, upper in zip(lo, hi))):
        point = list(values)
        if [dot(row, point) for row in A] != b:
            continue
        feasible += 1
        candidate = (f(point), point)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        raise InputError("bounded box contains no feasible point")
    return {"box_points_checked": total, "feasible_points": feasible, "objective": best[0], "point": best[1]}


def run(data: Any, iterations: int, use_exhaustive: bool, exhaustive_cap: int) -> dict[str, Any]:
    A, b, lo, hi, start, directions, f, scope, convex = parse(data)
    final, trace, stopped = augment(lo, hi, start, directions, f, iterations, convex=convex)
    result: dict[str, Any] = {
        "input_feasible": True, "direction_count": len(directions), "objective_scope": scope,
        "objective_is_discrete_convex_on_box": convex,
        "start": {"point": start, "objective": f(start)},
        "final": {"point": final, "objective": f(final)},
        "augmentation_trace": trace, "no_improving_supplied_direction": stopped,
        "status": "no-improvement-over-supplied-directions" if stopped else "iteration-cap-reached",
    }
    if stopped and convex:
        result["conditional_statement"] = ("If the supplied direction list contains every Graver direction of A, "
                                           "the final point is globally optimal for this separable convex objective.")
    elif stopped:
        result["conditional_statement"] = ("No supplied direction improves the point. A value table failed discrete convexity, "
                                           "so Graver optimality does not apply.")
    else:
        result["conditional_statement"] = "No certificate: the iteration cap was reached."
    if use_exhaustive:
        result["exhaustive_certificate"] = exhaustive(A, b, lo, hi, f, exhaustive_cap)
        result["exhaustive_certificate"]["matches_augmentation_final"] = (
            result["exhaustive_certificate"]["objective"] == result["final"]["objective"])
    return result


def self_test() -> None:
    root = Path(__file__).resolve().parents[1]
    good = run(json.loads((root / "examples/graver-augmentation-positive.json").read_text()), 100, True, 1000)
    assert good["final"]["point"] == [1, 2, 1] and good["final"]["objective"] == -6
    assert good["exhaustive_certificate"]["matches_augmentation_final"]
    partial = run(json.loads((root / "examples/graver-augmentation-incomplete-directions.json").read_text()), 100, True, 1000)
    assert partial["no_improving_supplied_direction"] and not partial["exhaustive_certificate"]["matches_augmentation_final"]
    bad = json.loads((root / "examples/graver-augmentation-positive.json").read_text())
    bad["directions"] = [[1, 1, 0]]
    try:
        run(bad, 100, False, 1000)
    except InputError as error:
        assert "ker_Z" in str(error)
    else:
        raise AssertionError("nonkernel direction was accepted")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instance", nargs="?", type=Path)
    parser.add_argument("--iterations", type=int, default=10000)
    parser.add_argument("--exhaustive", action="store_true")
    parser.add_argument("--exhaustive-cap", type=int, default=200000)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            print(json.dumps({"status": "self-test-passed"}))
            return 0
        if args.instance is None:
            raise InputError("provide an instance or --self-test")
        if args.iterations < 1 or args.exhaustive_cap < 1:
            raise InputError("caps must be positive")
        print(json.dumps(run(json.loads(args.instance.read_text()), args.iterations, args.exhaustive, args.exhaustive_cap), indent=2))
        return 0
    except (InputError, OSError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
