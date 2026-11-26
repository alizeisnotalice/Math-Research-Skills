#!/usr/bin/env python3
"""Exact finite-field checker for the degree < q-1 affine-line sum lemma."""
import argparse
import itertools
import json
import sys


def degree(poly):
    return poly.bit_length() - 1


def pmul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def pmod(a, modulus):
    d = degree(modulus)
    while a and degree(a) >= d:
        a ^= modulus << (degree(a) - d)
    return a


def irreducible(modulus, r):
    if degree(modulus) != r or not (modulus & 1):
        return False
    for d in range(1, r // 2 + 1):
        for lower in range(1 << d):
            f = (1 << d) | lower
            if f & 1 and pmod(modulus, f) == 0:
                return False
    return True


class GF:
    def __init__(self, r, modulus):
        self.r, self.modulus, self.q = r, modulus, 1 << r

    def mul(self, a, b):
        return pmod(pmul(a, b), self.modulus)

    def power(self, a, k):
        ans = 1
        while k:
            if k & 1:
                ans = self.mul(ans, a)
            a = self.mul(a, a)
            k >>= 1
        return ans

    def inv(self, a):
        if not a:
            raise ValueError("zero has no inverse")
        return self.power(a, self.q - 2)


def fail(message):
    print(f"REJECT: {message}")
    return 2


def parse(data):
    r = data.get("r")
    modulus = data.get("modulus")
    n = data.get("n")
    if not isinstance(r, int) or r < 2 or not isinstance(modulus, int):
        raise ValueError("r must be at least 2 and modulus must be an integer")
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if not irreducible(modulus, r):
        raise ValueError("modulus is not an irreducible binary polynomial of degree r")
    q = 1 << r
    terms = data.get("terms")
    if not isinstance(terms, list):
        raise ValueError("terms must be a list")
    clean = []
    for term in terms:
        e, c = term.get("exp"), term.get("coef")
        if (not isinstance(e, list) or len(e) != n or
                any(not isinstance(x, int) or x < 0 for x in e) or
                not isinstance(c, int) or not 0 <= c < q):
            raise ValueError("each term needs nonnegative n-vector exp and field coefficient")
        if c:
            clean.append((tuple(e), c))
    return GF(r, modulus), n, clean


def value(gf, terms, point):
    total = 0
    for exps, coeff in terms:
        piece = coeff
        for x, e in zip(point, exps):
            piece = gf.mul(piece, gf.power(x, e))
        total ^= piece
    return total


def canonical_line(gf, base, direction):
    points = tuple(sorted(tuple(b ^ gf.mul(t, v) for b, v in zip(base, direction))
                          for t in range(gf.q)))
    return points


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="JSON polynomial over GF(2^r)")
    args = ap.parse_args()
    try:
        with open(args.input, encoding="utf-8") as f:
            gf, n, terms = parse(json.load(f))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return fail(str(exc))
    maxdeg = max((sum(e) for e, _ in terms), default=0)
    if maxdeg > gf.q - 2:
        return fail(f"total degree {maxdeg} exceeds q-2={gf.q - 2}")
    points = list(itertools.product(range(gf.q), repeat=n))
    directions = set()
    for raw in points:
        if not any(raw):
            continue
        i = next(j for j, x in enumerate(raw) if x)
        scale = gf.inv(raw[i])
        directions.add(tuple(gf.mul(scale, x) for x in raw))
    lines = set()
    for direction in directions:
        for base in points:
            lines.add(canonical_line(gf, base, direction))
    bad = [(line, sum((value(gf, terms, x) for x in line), 0)) for line in []]
    # Field addition is XOR, not integer addition.
    for line in lines:
        line_sum = 0
        for point in line:
            line_sum ^= value(gf, terms, point)
        if line_sum:
            return fail(f"enumerated affine line has nonzero sum {line_sum}: {line}")
    space_sum = 0
    for point in points:
        space_sum ^= value(gf, terms, point)
    if space_sum:
        return fail(f"full affine space has nonzero sum {space_sum}")
    print(f"OK: GF(2^{gf.r}), n={n}, degree={maxdeg}, lines={len(lines)}, space_sum=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
