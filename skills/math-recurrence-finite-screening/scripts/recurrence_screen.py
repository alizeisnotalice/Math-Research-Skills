#!/usr/bin/env python3
"""Exact, bounded residual screens for three recurrence problems.

This program deliberately has no asymptotic branch: it reports only identities
in the requested finite box.  JSON is read from stdin and JSON is written to
stdout.  It is a source-derived residual checker, not a proof of any paper's
global theorem.
"""
from functools import cache
from math import isqrt
import json
import sys


def kpell(k, nmax):
    if k < 2 or nmax < 2:
        raise ValueError("require k >= 2 and n_max >= 2")
    p = [0] * (nmax + 1)
    p[1] = 1
    for n in range(2, nmax + 1):
        p[n] = 2 * p[n - 1] + sum(p[n - j] for j in range(2, min(k, n) + 1))
    return p


@cache
def possible_prime_exponents(bit_length):
    # Any exponent e for a base >= 2 satisfies e < bit_length.
    primes = []
    for candidate in range(2, bit_length):
        limit = isqrt(candidate)
        if all(candidate % prime for prime in primes if prime <= limit):
            primes.append(candidate)
    return tuple(primes)


def floor_root(a, exponent):
    lo, hi = 1, 1 << ((a.bit_length() + exponent - 1) // exponent)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** exponent <= a:
            lo = mid
        else:
            hi = mid
    return lo


def primitive_base(a):
    """Extract all prime factors of the maximal perfect-power exponent."""
    if a < 1:
        raise ValueError("primitive base is defined here only for positive terms")
    for exponent in possible_prime_exponents(a.bit_length()):
        while exponent < a.bit_length():
            root = floor_root(a, exponent)
            if root ** exponent != a:
                break
            a = root
    return a


def pell_dependence(data):
    kmin, kmax = data["k_min"], data["k_max"]
    nmax, mmin = data["n_max"], data.get("m_min", 2)
    if kmin < 2 or kmax < kmin or nmax <= mmin or mmin < 2:
        raise ValueError("invalid k-Pell bounds")
    hits, pairs = [], 0
    for k in range(kmin, kmax + 1):
        terms = kpell(k, nmax)
        bases = [None, None] + [primitive_base(terms[n]) for n in range(2, nmax + 1)]
        for n in range(mmin + 1, nmax + 1):
            for m in range(mmin, n):
                pairs += 1
                if bases[n] == bases[m]:
                    hits.append({"k": k, "m": m, "n": n, "base": str(bases[n])})
    return {"mode": "kpell_dependence", "box": {"k_min": kmin, "k_max": kmax,
            "m_min": mmin, "n_max": nmax}, "pairs_checked": pairs,
            "dependent_pairs": hits}


def klucas(k, nmax):
    if k < 3 or nmax < 1:
        raise ValueError("require k >= 3 and n_max >= 1")
    out = [2, 1]
    for n in range(2, nmax + 1):
        out.append(sum(out[n - j] for j in range(1, min(k, n) + 1)))
    return out


def lucas_concat(data):
    kmin, kmax, nmax = data["k_min"], data["k_max"], data["n_max"]
    if kmin < 3 or kmax < kmin or nmax < 2:
        raise ValueError("invalid k-Lucas bounds")
    hits, candidates = [], 0
    for k in range(kmin, kmax + 1):
        terms = klucas(k, nmax)
        for n in range(2, nmax + 1):
            for m in range(n):
                for p in range(n):
                    candidates += 1
                    d = len(str(terms[p]))
                    if terms[n] == terms[m] * 10 ** d + terms[p]:
                        hits.append({"k": k, "m": m, "n": n, "p": p, "digits": d,
                                     "value": str(terms[n])})
    return {"mode": "klucas_concat", "box": {"k_min": kmin, "k_max": kmax,
            "n_max": nmax}, "candidates_checked": candidates, "identities": hits}


def abc_common_values(data):
    coeff, initial, radius = data["coefficients"], data["initial"], data["radius"]
    q = len(coeff) - 1
    if type(radius) is not int or any(type(x) is not int for x in coeff + initial):
        raise ValueError("recurrence data must be integer values")
    if q < 2 or coeff[0] != 1 or len(initial) != q or radius < q:
        raise ValueError("need monic degree >= 2 coefficients, q initial values, and radius >= q")
    if abs(coeff[-1]) != 1:
        raise ValueError("two-sided exact propagation requires unit constant coefficient")
    values = dict(enumerate(initial))
    for r in range(q, radius + 1):
        values[r] = -sum(coeff[j] * values[r - j] for j in range(1, q + 1))
    for r in range(-1, -radius - 1, -1):
        numerator = -(values[r + q] + sum(coeff[j] * values[r + q - j]
                                            for j in range(1, q)))
        if numerator % coeff[-1]:
            raise ValueError("backward recurrence left the integers")
        values[r] = numerator // coeff[-1]
    by_abs = {}
    for i in range(-radius, radius + 1):
        by_abs.setdefault(abs(values[i]), []).append(i)
    collisions = [{"absolute_value": str(v), "indices": is_} for v, is_ in by_abs.items()
                  if len(is_) > 1]
    return {"mode": "abc_common_values", "box": {"radius": radius},
            "coefficients": coeff, "initial_values": initial,
            "values": {str(i): str(values[i]) for i in range(-radius, radius + 1)},
            "absolute_value_collisions": collisions}


def main():
    data = json.load(sys.stdin)
    functions = {"kpell_dependence": pell_dependence, "klucas_concat": lucas_concat,
                 "abc_common_values": abc_common_values}
    if data.get("mode") not in functions:
        raise ValueError("mode must be kpell_dependence, klucas_concat, or abc_common_values")
    print(json.dumps(functions[data["mode"]](data), sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError) as error:
        print(json.dumps({"error": str(error)}))
        sys.exit(2)
