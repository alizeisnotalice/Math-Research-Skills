#!/usr/bin/env python3
"""Exact identity checker for the Bennett--Ghadermazi F_{3,t} candidates."""

from __future__ import annotations

import argparse


def form(t: int, x: int, y: int) -> int:
    return x**3 - (t**4 - t) * x**2 * y + (t**5 - 2 * t**2) * x * y**2 + y**3


def source_candidates(t: int) -> list[tuple[int, int]]:
    return [
        (1, 0),
        (0, 1),
        (t, 1),
        (t**4 - 2 * t, 1),
        (1 - t**3, t**8 - 3 * t**5 + 3 * t**2),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("t", type=int, help="integer parameter t")
    args = parser.parse_args()
    candidates = source_candidates(args.t)
    if args.t == -1:
        candidates.append((6, -5))
    for x, y in candidates:
        value = form(args.t, x, y)
        if value != 1:
            raise SystemExit(f"FAILED t={args.t}, (x,y)=({x},{y}), F={value}")
        print(f"t={args.t} (x,y)=({x},{y}) F=1")
    print("verified displayed candidates only; this program does not prove completeness")


if __name__ == "__main__":
    main()
