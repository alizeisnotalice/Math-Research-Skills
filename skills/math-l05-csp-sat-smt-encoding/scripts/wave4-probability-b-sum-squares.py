#!/usr/bin/env python3
"""Exact finite check for compiling a conjunction of integer equations by squares."""
import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    data = json.load(open(args.input))
    values = data["equation_values"]
    if not isinstance(values, list) or not all(isinstance(x, int) for x in values):
        parser.error("equation_values must be an integer list")
    total = sum(x * x for x in values)
    print(json.dumps({"sum_of_squares": total, "all_zero": total == 0}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
