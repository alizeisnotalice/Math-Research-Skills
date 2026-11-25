#!/usr/bin/env python3
"""Compare carry-free packed partition rows against integer dynamic programming."""

from itertools import zip_longest


def packed_rows(n, width):
    packed = 1
    mask = (1 << (width * (n + 1))) - 1
    digit_mask = (1 << width) - 1
    for part in range(1, n + 1):
        packed = sum(packed << (width * part * copies) for copies in range(n // part + 1)) & mask
        yield [(packed >> (width * total)) & digit_mask for total in range(n + 1)]


def ordinary_rows(n):
    row = [1] + [0] * n
    for part in range(1, n + 1):
        for total in range(part, n + 1):
            row[total] += row[total - part]
        yield row.copy()


def main():
    checks = 0
    for n, expected in ((5, 7), (36, 17977), (100, 190569292)):
        for packed, ordinary in zip_longest(packed_rows(n, n), ordinary_rows(n)):
            assert packed == ordinary
            checks += len(ordinary)
        assert ordinary[-1] == expected
        print(f"n={n}: partitions={ordinary[-1]}; all packed fields agree")
    assert list(packed_rows(5, 2))[-1] != list(ordinary_rows(5))[-1]
    print(f"PASS: {checks} exact field comparisons; insufficient width causes corruption.")


if __name__ == "__main__":
    main()
