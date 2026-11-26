#!/usr/bin/env python3
"""Exact rational specialization of Johansson's Theorem 1 tail factor."""

import argparse
from fractions import Fraction


def rationals(text):
    if not text:
        return []
    return [Fraction(part.strip()) for part in text.split(",")]


def factor(a, b, n, z):
    if len(b) < len(a):
        raise ValueError("requires p <= q+1, i.e. at least as many b values as a values")
    shifted = [item + n for item in b]
    if any(item <= 0 for item in shifted):
        raise ValueError("requires b_i + N > 0 in this real-rational specialization")
    result = abs(z)
    for ai, bi, shifted_bi in zip(a, b, shifted):
        result *= 1 + abs(ai - bi) / shifted_bi
    for shifted_bi in shifted[len(a) :]:
        result /= shifted_bi
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", required=True, help="comma-separated rational a_i values")
    parser.add_argument("--b", required=True, help="comma-separated rational b_i values")
    parser.add_argument("--n", required=True, type=int, help="integer tail index N")
    parser.add_argument("--z", required=True, help="rational real z")
    args = parser.parse_args()
    d = factor(rationals(args.a), rationals(args.b), Fraction(args.n), Fraction(args.z))
    print(f"D = {d}")
    if d >= 1:
        raise SystemExit("REJECT: D >= 1; the theorem supplies no finite geometric tail factor")
    print(f"C = {1 / (1 - d)}")


if __name__ == "__main__":
    main()
