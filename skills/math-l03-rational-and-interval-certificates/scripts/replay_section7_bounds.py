#!/usr/bin/env python3
"""Directed-interval replay of the public source's Section-7 n_0 kernel.

It certifies the signs and integer roundings used by the source computation,
not the modular, Thue, or linear-form theorem that makes that bound applicable.
Requires python-flint >= 0.9.0.
"""
from argparse import ArgumentParser
from math import comb
from flint import arb, ctx

ctx.prec = 384

LAURENT = {10: (252, 10), 12: (234, 10), 14: (221, 10), 16: (211, 10),
           18: (203, 10), 20: (197, 10), 22: (192, 10), 24: (188, 10),
           26: (184, 10), 28: (181, 10), 30: (179, 10)}
PUBLISHED_TABLE = {6: 80968, 10: 173419, 14: 278265, 18: 543366,
                   22: 927845, 26: 1438387, 30: 2084701, 34: 2875394,
                   38: 3818215, 42: 4920232, 46: 6187948, 50: 7627398,
                   54: 9244217, 58: 11043693, 62: 13030815,
                   66: 15210304, 70: 16550269, 74: 18440172,
                   78: 20987069, 82: 23725616, 86: 26659268,
                   90: 29791351, 94: 33125067, 98: 36663510}


def integer_floor(x):
    y = x.floor()
    if not y.is_exact() or not y.is_integer():
        raise ArithmeticError("interval did not isolate an integer floor")
    return int(y.unique_fmpz())


def sign(x):
    if x.lower() > 0:
        return 1
    if x.upper() < 0:
        return -1
    raise ArithmeticError("interval sign is not isolated")


def source_h_coefficient(k):
    """Exact coefficient path in the public Sage source, retained for fidelity."""
    g = [0] * (k + 1)
    for j in range(0, k + 1, 2):
        g[j] = comb(k, j)
    f = []
    for i in range(k - 1):
        f.append(g[i] - (f[i - 2] if i >= 2 else 0))
    h = [0]
    for i, coefficient in enumerate(f):
        term = [comb(i, j) * (-1) ** (i - j) * coefficient for j in range(i + 1)]
        if len(h) < len(term):
            h += [0] * (len(term) - len(h))
        for j, value in enumerate(term):
            h[j] += value
    return h[k // 2 - 2], h


def source_bound(k):
    if k not in PUBLISHED_TABLE:
        raise ValueError("k must be one of 6,10,...,98")
    q = arb(k)
    half = k // 2
    hkm2, h = source_h_coefficient(k)
    # This is the source-code expression (not a new analytic estimate).
    if hkm2 == 0:
        raise ArithmeticError("source coefficient used as a denominator vanishes")
    x0 = max(sum(abs(v) for v in h[:-2]) // hkm2, 200 * hkm2, k) + 1
    c1 = arb(50255) * q * q * arb(half - 1) / arb(100000)
    a_upper = q ** half / 2
    n1 = integer_floor((q * x0 / 4).log() / arb(3).log())
    n2 = max(integer_floor((c1 / a_upper.log()).log() / arb(3).log()),
             integer_floor(c1.log() / arb(3).log()),
             integer_floor((a_upper.log() + 1) / (arb(3) / 2).log()))
    n3 = integer_floor(100 * q * q.log() / (arb(3) / 2 * arb(3) ** (half - 1)).log())
    w1 = (arb(half - 1) + (arb(3) / 2).log() / arb(3).log()) * q * q.log() / 2
    w2 = c1.log() / arb(3).log()
    a = arb(201) / (100 * q * q.log())
    candidates, certificates = [], []
    for m, (numerator, denominator) in LAURENT.items():
        c2 = arb(numerator) / denominator
        n4 = integer_floor((arb(m) - arb(38) / 100).exp() * q * q.log() / 2)
        f = lambda n: c2 * (a * n).log() ** 2 * w1 + w2 - n
        derivative = lambda n: 2 * c2 * w1 * (a * n).log() / n - 1
        # Above n4 the derivative decreases because log(a*n4) > 1.
        if sign((a * n4).log() - 1) < 0:
            raise ArithmeticError("initial threshold is outside the decreasing-derivative range")
        if sign(f(n4)) < 0:
            if sign(derivative(n4)) >= 0:
                raise ArithmeticError("negative threshold does not yet bound all larger exponents")
            last_positive = n4 - 1
            derivative_certified = True
        else:
            # The source starts its coarse scan at 7.  For the faster replay,
            # enter the decreasing branch first; f is positive up to its sole
            # large crossing, so this preserves the source's final crossing.
            lo = n4
            while sign(derivative(lo)) >= 0:
                lo *= 2
            if sign(f(lo)) <= 0:
                raise ArithmeticError("crossing occurred before decreasing branch")
            hi = 2 * lo
            while sign(f(hi)) > 0:
                hi *= 2
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if sign(f(mid)) > 0:
                    lo = mid
                else:
                    hi = mid
            last_positive = lo
            derivative_certified = True
            if sign(f(last_positive)) <= 0 or sign(f(last_positive + 1)) >= 0:
                raise ArithmeticError("crossing certificate failed")
        candidate = max(n1, n2, n3, n4, last_positive)
        candidates.append(candidate)
        certificates.append((m, n4, last_positive, derivative_certified, candidate))
    result = min(candidates)
    return result, certificates, (n1, n2, n3, x0, hkm2)


def main():
    parser = ArgumentParser()
    parser.add_argument("--k", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    if bool(args.k) == bool(args.all):
        parser.error("choose exactly one of --k and --all")
    ks = sorted(PUBLISHED_TABLE) if args.all else [args.k]
    for k in ks:
        bound, rows, auxiliaries = source_bound(k)
        expected = PUBLISHED_TABLE[k]
        text = (f"k={k} n0={bound} expected={expected} match={bound == expected} "
                f"n1,n2,n3,x0,h={auxiliaries}")
        if args.verbose:
            text += f" rows={rows}"
        print(text)
        if bound != expected:
            raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except (ArithmeticError, ValueError) as error:
        print(f"error: {error}")
        raise SystemExit(2)
