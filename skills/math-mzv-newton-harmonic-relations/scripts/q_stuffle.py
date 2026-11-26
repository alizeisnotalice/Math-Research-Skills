#!/usr/bin/env python3
"""Exact formal q-stuffle expansions for Bradley-normalized q-zeta indices."""

from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache


Poly = tuple[int, ...]  # coefficient list in r=1-q
Word = tuple[int, ...]
Expansion = dict[Word, Poly]


def add_poly(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    out = [0] * n
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def shift(poly: Poly) -> Poly:
    return (0,) + poly


def mul_poly(left: Poly, right: Poly) -> Poly:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return tuple(out)


def add_prefixed(target: dict[Word, Poly], head: int, source: Expansion, r_power: int = 0) -> None:
    for tail, coefficient in source.items():
        for _ in range(r_power):
            coefficient = shift(coefficient)
        word = (head,) + tail
        target[word] = add_poly(target.get(word, (0,)), coefficient)


@lru_cache(maxsize=None)
def q_stuffle(left: Word, right: Word) -> tuple[tuple[Word, Poly], ...]:
    if not left:
        return ((right, (1,)),)
    if not right:
        return ((left, (1,)),)
    a, *u = left
    b, *v = right
    first = dict(q_stuffle(tuple(u), right))
    second = dict(q_stuffle(left, tuple(v)))
    merged = dict(q_stuffle(tuple(u), tuple(v)))
    output: dict[Word, Poly] = {}
    add_prefixed(output, a, first)
    add_prefixed(output, b, second)
    add_prefixed(output, a + b, merged)
    add_prefixed(output, a + b - 1, merged, r_power=1)
    return tuple(sorted(output.items()))


def format_poly(poly: Poly) -> str:
    pieces = []
    for degree, coefficient in reversed(list(enumerate(poly))):
        if coefficient == 0:
            continue
        atom = "1" if degree == 0 else "r" if degree == 1 else f"r^{degree}"
        pieces.append(atom if coefficient == 1 else f"{coefficient}*{atom}")
    return " + ".join(pieces) or "0"


def format_word(word: Word) -> str:
    return "zeta_q[" + ",".join(map(str, word)) + "]"


def parse_word(text: str) -> Word:
    word = tuple(int(x) for x in text.split(",") if x)
    if not word or word[0] <= 1 or any(x < 1 for x in word):
        raise ValueError("each index must be positive and the first must exceed 1")
    return word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", nargs="?", help="comma-separated admissible index")
    parser.add_argument("right", nargs="?", help="comma-separated admissible index")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        expected = { (2, 3): (1,), (3, 2): (1,), (5,): (1,), (4,): (0, 1) }
        got = dict(q_stuffle((2,), (3,)))
        assert got == expected, got
        # Associativity is a formal consequence expected of this recursion.
        def distribute(terms: Expansion, word: Word) -> Expansion:
            out: dict[Word, Poly] = {}
            for prior, coeff in terms.items():
                for nxt, ncoeff in q_stuffle(prior, word):
                    product = mul_poly(coeff, ncoeff)
                    out[nxt] = add_poly(out.get(nxt, (0,)), product)
            return out
        left_associated = distribute(dict(q_stuffle((2,), (3,))), (4,))
        right_associated = distribute(dict(q_stuffle((3,), (4,))), (2,))
        assert left_associated == right_associated
        print("self-test passed: depth-one identity and a formal associativity check")
        return
    if args.left is None or args.right is None:
        parser.error("supply two indices or use --self-test")
    for word, coefficient in q_stuffle(parse_word(args.left), parse_word(args.right)):
        print(f"{format_poly(coefficient)} * {format_word(word)}")


if __name__ == "__main__":
    main()
