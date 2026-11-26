#!/usr/bin/env python3
"""Exact finite ICG spectrum candidate and adjacency-moment certificate.

For explicit n,D, use residue classes to form the integer Ramanujan values
lambda_t=sum_{d in D} c_{n/d}(t).  Direct adjacency multiplication checks
the second and fourth moments against these values.  The reported energy is
the l1 norm of this finite Fourier spectrum; no extremal assertion is made.
"""
import argparse
import json
from math import gcd


def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


def phi(n):
    ans = n
    for p, _ in factor(n):
        ans = ans // p * (p - 1)
    return ans


def mu(n):
    sign = 1
    for _, e in factor(n):
        if e > 1:
            return 0
        sign = -sign
    return sign


def ramanujan(m, t):
    """c_m(t)=mu(m/gcd(m,t))*phi(m)/phi(m/gcd(m,t)), including t=0."""
    r = m // gcd(m, t)
    return mu(r) * phi(m) // phi(r)


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, required=True)
    ap.add_argument('--divisors', required=True, help='comma-separated proper positive divisors')
    args = ap.parse_args()
    n = args.n
    if n < 2:
        raise SystemExit('n must be at least 2')
    try:
        ds = tuple(sorted({int(x) for x in args.divisors.split(',') if x}))
    except ValueError as e:
        raise SystemExit('divisors must be integers') from e
    if not ds or any(d <= 0 or d >= n or n % d for d in ds):
        raise SystemExit('supply a nonempty set of proper positive divisors of n')
    adjacency = [[int(i != j and gcd((j - i) % n, n) in ds) for j in range(n)] for i in range(n)]
    lambdas = [sum(ramanujan(n // d, t) for d in ds) for t in range(n)]
    a2 = matmul(adjacency, adjacency)
    tr2 = sum(a2[i][i] for i in range(n))
    tr4 = sum(a2[i][j] * a2[j][i] for i in range(n) for j in range(n))
    out = {
        'n': n, 'divisors': list(ds), 'degree': sum(adjacency[0]),
        'ramanujan_eigenvalues': lambdas, 'ramanujan_energy': sum(abs(x) for x in lambdas),
        'trace_A2_direct': tr2, 'trace_A2_ramanujan': sum(x*x for x in lambdas),
        'trace_A4_direct': tr4, 'trace_A4_ramanujan': sum(x**4 for x in lambdas),
    }
    out['moments_match'] = out['trace_A2_direct'] == out['trace_A2_ramanujan'] and out['trace_A4_direct'] == out['trace_A4_ramanujan']
    print(json.dumps(out, sort_keys=True))
    if not out['moments_match']:
        raise SystemExit('direct adjacency moments do not match Ramanujan values')


if __name__ == '__main__':
    main()
