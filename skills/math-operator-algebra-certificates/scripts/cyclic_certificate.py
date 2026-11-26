#!/usr/bin/env python3
"""Exact finite scalar certificate for the translation-commutant lemma."""
import argparse
import itertools
import json
from fractions import Fraction


def q(x):
    return Fraction(str(x))


def matrix(raw):
    return [[q(x) for x in row] for row in raw]


def det(a):
    a = [row[:] for row in a]
    ans = Fraction(1)
    for i in range(len(a)):
        pivot = next((r for r in range(i, len(a)) if a[r][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            ans = -ans
        p = a[i][i]
        ans *= p
        for r in range(i + 1, len(a)):
            f = a[r][i] / p
            for c in range(i + 1, len(a)):
                a[r][c] -= f * a[i][c]
    return ans


def psd(a):
    n = len(a)
    return all(det([[a[i][j] for j in ix] for i in ix]) >= 0
               for r in range(1, n + 1) for ix in itertools.combinations(range(n), r))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ns = ap.parse_args()
    d = json.load(open(ns.input))
    n = int(d['n'])
    if not 1 <= n <= 8:
        raise SystemExit('REJECT n must be between 1 and 8 for exact principal-minor checking')
    W, T, C = [q(x) for x in d['kernel']], matrix(d['T']), matrix(d['C'])
    if len(W) != n or any(len(X) != n for X in (T, C)) or len(T) != n or len(C) != n:
        raise SystemExit('REJECT incompatible cyclic dimensions')
    A = [[W[(y - x) % n] for y in range(n)] for x in range(n)]
    if C != [[C[0][(y - x) % n] for y in range(n)] for x in range(n)]:
        raise SystemExit('REJECT C is not a cyclic translation-commutant matrix')
    K, dnorm = q(d['K']), q(d['d'])
    if K < 0 or dnorm < 0:
        raise SystemExit('REJECT K and d must be nonnegative')
    row2 = sum(x*x for x in T[0])
    col2 = sum((A[x][0]-T[x][0])**2 for x in range(n))
    if row2 > K*K or col2 > K*K:
        raise SystemExit('REJECT declared K does not bound row_0(T) and col_0(A-T)')
    B = [[T[i][j]-C[i][j] for j in range(n)] for i in range(n)]
    gram = [[sum(B[r][i]*B[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
    slack = [[(dnorm*dnorm if i == j else 0)-gram[i][j] for j in range(n)] for i in range(n)]
    if not psd(slack):
        raise SystemExit('REJECT d^2 I-(T-C)^T(T-C) is not PSD')
    E = sum(x*x for x in W)
    if E > 4*(K+dnorm)**2:
        raise SystemExit('REJECT certificate contradicts the lemma (check data)')
    lower = '0' if E == 0 else 'sqrt(%s)/2-%s' % (E, K)
    print('ACCEPT E=%s row2=%s col2=%s lower-distance>=%s' % (E, row2, col2, lower))


if __name__ == '__main__':
    main()
