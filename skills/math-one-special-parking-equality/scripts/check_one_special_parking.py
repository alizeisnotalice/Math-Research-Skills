#!/usr/bin/env python3
"""Exact finite checker for one-special-preference parking instances."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def subset_sums(values: list[int]) -> set[int]:
    sums = {0}
    for value in values:
        sums |= {value + old for old in sums}
    return sums


def parks(lengths: list[int], special_car: int, preference: int) -> bool:
    occupied = [False] * sum(lengths)
    for car, length in enumerate(lengths):
        start = preference - 1 if car == special_car else 0
        while start + length <= len(occupied):
            if all(not occupied[spot] for spot in range(start, start + length)):
                for spot in range(start, start + length):
                    occupied[spot] = True
                break
            start += 1
        else:
            return False
    return True


def is_superdecreasing(values: list[int]) -> bool:
    return all(value > sum(values[index + 1:]) for index, value in enumerate(values))


def symmetric_prefix(sums: set[int], value: int) -> bool:
    return value in sums and all(value - member in sums for member in sums if member <= value)


def check(lengths: list[int]) -> dict[str, object]:
    if not lengths or any(type(value) is not int or value <= 0 for value in lengths):
        raise ValueError("lengths must be a nonempty list of positive integers")
    total = sum(lengths)
    admissible = [preference for preference in range(1, total + 1)
                  if all(parks(lengths, car, preference) for car in range(len(lengths)))]
    bound = 2 ** (len(lengths) - 1)
    if len(lengths) == 1:
        criterion = True
        criterion_data: dict[str, object] = {}
    else:
        first, second, *suffix = lengths
        suffix_sum = sum(suffix)
        gap = first - second
        suffix_sums = subset_sums(suffix)
        criterion = (first >= second and is_superdecreasing([second, *suffix]) and
                     (gap >= suffix_sum or symmetric_prefix(suffix_sums, suffix_sum - gap)))
        criterion_data = {
            "first_minus_second": gap,
            "suffix_sum": suffix_sum,
            "tail_superdecreasing": is_superdecreasing([second, *suffix]),
            "symmetric_target": suffix_sum - gap,
            "suffix_subset_sums": sorted(suffix_sums),
        }
    return {
        "lengths": lengths,
        "W": admissible,
        "bound": bound,
        "direct_equality": len(admissible) == bound,
        "criterion_holds": criterion,
        "criterion_data": criterion_data,
        "criterion_matches_direct": criterion == (len(admissible) == bound),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_one_special_parking.py INPUT.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(check(payload["lengths"]), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
