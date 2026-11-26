#!/usr/bin/env python3
"""Enumerate irredundant intersections of irreducible oversemigroups."""

import argparse
from itertools import combinations
import json


def defines_semigroup(gaps):
    if not gaps:
        return True
    largest_gap = max(gaps)
    elements = [n for n in range(largest_gap + 1) if n not in gaps]
    return all(a + b not in gaps for a in elements for b in elements)


def check_lengths(gaps):
    if any(gap <= 0 for gap in gaps) or not defines_semigroup(gaps):
        raise ValueError("gaps must define a numerical semigroup")
    ordered = sorted(gaps)
    supersets = [
        frozenset(subset)
        for size in range(len(gaps) + 1)
        for subset in combinations(ordered, size)
        if defines_semigroup(subset)
    ]
    irreducibles = []
    for candidate in supersets:
        if not candidate:
            continue
        proper = [smaller for smaller in supersets if smaller < candidate]
        if not any(left | right == candidate for left, right in combinations(proper, 2)):
            irreducibles.append(candidate)

    lengths = set()
    for size in range(len(irreducibles) + 1):
        for family in combinations(irreducibles, size):
            if frozenset().union(*family) != gaps:
                continue
            if all(frozenset().union(*(family[:i] + family[i + 1:])) != gaps for i in range(size)):
                lengths.add(size)
    ordered_lengths = sorted(lengths)
    return {
        "gaps": ordered,
        "oversemigroups": len(supersets),
        "irreducible_oversemigroups": [sorted(candidate) for candidate in irreducibles],
        "lengths": ordered_lengths,
        "interval": bool(lengths) and ordered_lengths == list(range(min(lengths), max(lengths) + 1)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gaps", required=True, help="comma-separated gaps; empty string means no gaps")
    args = parser.parse_args()
    try:
        gaps = frozenset(int(text) for text in args.gaps.split(",") if text)
        report = check_lengths(gaps)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(report, sort_keys=True))
    if not report["interval"]:
        raise SystemExit("non-interval length set for supplied input")


if __name__ == "__main__":
    main()
