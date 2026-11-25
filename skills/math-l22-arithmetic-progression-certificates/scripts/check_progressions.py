#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def progressions(size, length):
    for start in range(size):
        for step in range(1, (size - 1 - start) // (length - 1) + 1):
            yield tuple(start + i * step for i in range(length))


def digit_colors(number, base_color, positions):
    digits = []
    for _ in range(positions):
        number, digit = divmod(number, len(base_color))
        digits.append(base_color[digit])
    return tuple(digits)


def no_overlong_colored_progression():
    color = (0, 0, 1, 1, 1)
    modulus = len(color)
    for start in range(modulus):
        for step in range(1, modulus):
            assert len({color[(start + j * step) % modulus] for j in range(4)}) > 1
    interval = modulus**3
    colors = [digit_colors(n, color, 3) for n in range(interval)]
    tested = 0
    for indices in progressions(interval, 4):
        assert len({colors[i] for i in indices}) > 1
        tested += 1
    print(f"Digit product: {len(set(colors))} colors, interval={interval}, APs={tested}")


def extremal_small_triples(size):
    triples = [set(p) for p in progressions(size, 3)]
    for count in range(size, 0, -1):
        for points in combinations(range(size), count):
            if not any(triple.issubset(points) for triple in triples):
                return count
    raise ValueError("size must be positive")


def weighted_count():
    blocks = [1, 2, 4, 8]
    sizes = [extremal_small_triples(length) for length in blocks]
    assert sizes == [1, 2, 3, 4]
    covering = sum(Fraction(count, length) for length, count in zip(blocks, sizes))
    assert not any(len({1, 2, 4, 8}.intersection(p)) == 3 for p in progressions(16, 3))
    weight = sum(Fraction(1, point) for point in blocks)
    assert weight == Fraction(15, 8) <= covering == Fraction(13, 4)
    print(f"Dyadic count: extremal sizes={sizes}, witness={weight}, upper bound={covering}")


if __name__ == "__main__":
    no_overlong_colored_progression()
    weighted_count()
