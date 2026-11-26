#!/usr/bin/env python3
"""Decode and independently check the packed A7 witness in Data.lean."""
import re
import sys
from collections import Counter
from pathlib import Path


def compose(left, right):
    return tuple(left[index] for index in right)


def inverse(permutation):
    answer = [0] * 7
    for index, image in enumerate(permutation):
        answer[image] = index
    return tuple(answer)


def is_even(permutation):
    return sum(
        permutation[i] > permutation[j]
        for i in range(7)
        for j in range(i + 1, 7)
    ) % 2 == 0


def main(path):
    source = Path(path).read_text()
    try:
        image_section = source.split("def images (i : Nat) : Nat :=", 1)[1].split(
            "def shifts", 1
        )[0]
    except IndexError as error:
        raise ValueError("not the documented A7 Data.lean format") from error
    blocks = {
        int(index): int(value, 16)
        for index, value in re.findall(r"\| (\d+) => 0x([0-9a-f]+)", image_section)
    }
    if set(blocks) != set(range(40)):
        raise ValueError("expected exactly 40 packed image blocks")
    rows = []
    for index in range(2520):
        packed = (blocks[index // 64] >> (21 * (index % 64))) % (2 ** 21)
        rows.append(tuple((packed >> (3 * coordinate)) & 7 for coordinate in range(7)))
    identity = tuple(range(7))
    if any(sorted(row) != list(range(7)) or not is_even(row) for row in rows):
        raise ValueError("decoded data are not all even permutations")
    if len(set(rows)) != 2520 or rows[0] != identity:
        raise ValueError("decoded rows are not a normalized enumeration of A7")
    counts = Counter(compose(inverse(left), right) for left, right in zip(rows, rows[1:]))
    for element in rows[1:]:
        total = counts[element]
        if element != inverse(element):
            total += counts[inverse(element)]
        if total != (1 if element == inverse(element) else 2):
            raise ValueError("A7 terrace count failed")
    print("verified packed A7: 2520 even distinct rows; 2519 quotient conditions")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: replay_packed_a7.py PATH/TO/Data.lean")
    main(sys.argv[1])
