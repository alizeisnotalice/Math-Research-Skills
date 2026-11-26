#!/usr/bin/env python3
"""Enumerate Lemma 9.2 weighted linear-forest patterns exactly."""

from __future__ import annotations
import argparse
import json
import sys
from typing import Iterator, Tuple

Component = Tuple[int, ...]
Pattern = Tuple[Component, ...]


def compositions(total: int, length: int) -> Iterator[Component]:
    if length == 0:
        if total == 0:
            yield ()
        return
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def normalized_components(vertices: int, budget: int, lower: Component) -> Iterator[Component]:
    if () >= lower:
        yield ()
    for length in range(1, vertices):
        for total in range(length, budget + 1):
            for component in compositions(total, length):
                canonical = min(component, tuple(reversed(component)))
                if component == canonical and canonical >= lower:
                    yield canonical


def patterns(vertices: int, budget: int, max_patterns: int) -> list[Pattern]:
    output: list[Pattern] = []

    def visit(remaining_vertices: int, remaining_budget: int, lower: Component, prefix: Pattern) -> None:
        if len(output) > max_patterns:
            return
        if remaining_vertices == 0:
            output.append(prefix)
            return
        for component in normalized_components(remaining_vertices, remaining_budget, lower):
            amount = sum(component)
            consumed = len(component) + 1
            if amount <= remaining_budget and consumed <= remaining_vertices:
                visit(remaining_vertices - consumed, remaining_budget - amount, component, prefix + (component,))

    visit(vertices, budget, (), ())
    if len(output) > max_patterns:
        raise ValueError(f"more than max_patterns={max_patterns}; lower the budgets or raise the explicit limit")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Exact canonical weighted path-forest enumeration.")
    parser.add_argument("input", help="JSON file with nonnegative integer fields vertices and budget")
    parser.add_argument("--max-patterns", type=int, default=100000, help="explicit output safety limit")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as handle:
            data = json.load(handle)
        vertices, budget = data["vertices"], data["budget"]
        if isinstance(vertices, bool) or isinstance(budget, bool) or not isinstance(vertices, int) or not isinstance(budget, int):
            raise ValueError("vertices and budget must be integers")
        if vertices < 0 or budget < 0 or args.max_patterns < 1:
            raise ValueError("vertices and budget must be nonnegative and max-patterns must be positive")
        result = patterns(vertices, budget, args.max_patterns)
        json.dump({"vertices": vertices, "budget": budget, "count": len(result),
                   "patterns": [[list(component) for component in pattern] for pattern in result]},
                  sys.stdout, separators=(",", ":"))
        sys.stdout.write("\n")
        return 0
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
