#!/usr/bin/env python3
"""Check the finite 3x-1 inverse-word decoder using exact Python integers."""

import argparse
import json


def valuation2(value):
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=int, required=True)
    parser.add_argument("--word", required=True, help="comma-separated positive valuations")
    args = parser.parse_args()
    word = [int(item) for item in args.word.split(",") if item]
    if args.root <= 0 or args.root % 2 == 0:
        parser.error("root must be a positive odd integer")
    if not word or any(a <= 0 for a in word):
        parser.error("word must be a nonempty comma-separated list of positive integers")
    values = [0] * (len(word) + 1)
    values[-1] = args.root
    for i in range(len(word), 0, -1):
        numerator = (1 << word[i - 1]) * values[i] + 1
        if numerator % 3:
            parser.error(f"inverse step {i} is not integral")
        values[i - 1] = numerator // 3
        if values[i - 1] <= 0 or values[i - 1] % 2 == 0:
            raise AssertionError("integral inverse step was not positive odd")
    A = sum(word)
    B = sum(3 ** (len(word) - i - 1) * 2 ** sum(word[:i])
            for i in range(len(word)))
    if 3 ** len(word) * values[0] != 2 ** A * args.root + B:
        raise AssertionError("affine identity failed")
    for i, a in enumerate(word):
        if valuation2(3 * values[i] - 1) != a:
            raise AssertionError("valuation check failed")
    print(json.dumps({"root": args.root, "word": word, "source": values[0],
                      "orbit": values, "offset": B}))


if __name__ == "__main__":
    main()
