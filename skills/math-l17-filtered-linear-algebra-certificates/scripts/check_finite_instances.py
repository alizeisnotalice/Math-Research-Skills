#!/usr/bin/env python3
"""Exact, deliberately small checks for the two finite-algebra interfaces in L17.

This is an executable fixture, not a decision procedure for arbitrary power
series or filtrations.  All arithmetic is Fraction arithmetic.
"""

from fractions import Fraction as Q


def matrix(rows):
    return [[Q(x) for x in row] for row in rows]


def zeros(n, m):
    return [[Q(0) for _ in range(m)] for _ in range(n)]


def ident(n):
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = Q(1)
    return a


def add(a, b, sign=1):
    return [[a[i][j] + sign * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[Q(c) * x for x in row] for row in a]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def power(a, n):
    out = ident(len(a))
    for _ in range(n):
        out = mul(a, out)
    return out


def rref(a):
    a = [row[:] for row in a]
    m, n = len(a), (len(a[0]) if a else 0)
    pivots, row = [], 0
    for col in range(n):
        pivot = next((i for i in range(row, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        c = a[row][col]
        a[row] = [x / c for x in a[row]]
        for i in range(m):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [a[i][j] - c * a[row][j] for j in range(n)]
        pivots.append(col)
        row += 1
        if row == m:
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def col(m, j):
    return [m[i][j] for i in range(len(m))]


def columns(vectors):
    if not vectors:
        return []
    return [[v[i] for v in vectors] for i in range(len(vectors[0]))]


def in_span(v, basis):
    if not basis:
        return not any(v)
    b = columns(basis)
    return rank(b) == rank([row + [v[i]] for i, row in enumerate(b)])


def apply(a, v):
    return [sum((a[i][j] * v[j] for j in range(len(v))), Q(0))
            for i in range(len(a))]


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


def add_poly(a, b):
    out = dict(a)
    for exp, coeff in b.items():
        out[exp] = out.get(exp, Q(0)) + coeff
        if not out[exp]:
            del out[exp]
    return out


def mul_poly(a, b):
    out = {}
    for aa, ca in a.items():
        for bb, cb in b.items():
            exp = tuple(x + y for x, y in zip(aa, bb))
            out[exp] = out.get(exp, Q(0)) + ca * cb
    return {exp: coeff for exp, coeff in out.items() if coeff}


def lead(poly):
    return min(poly)  # The fixture's declared order is lexicographic.


def check_least_terms():
    # Monomial table is ordered increasingly for the declared lex order.
    monomials = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
    generators = [
        {(0, 0): Q(2), (1, 0): Q(1), (1, 1): Q(4)},
        {(0, 1): Q(3), (1, 0): Q(1), (2, 0): Q(5)},
        {(0, 0): Q(2), (0, 1): Q(6), (1, 1): Q(1)},
    ]
    coeff = [[p.get(exp, Q(0)) for exp in monomials] for p in generators]
    _, pivots = rref(coeff)
    assert_true(len(pivots) == 3, "expected a 3-dimensional test space")
    assert_true([monomials[j] for j in pivots] == [(0, 0), (0, 1), (1, 0)],
                "RREF pivots do not give the declared least-term set")

    f = {(0, 0): Q(2), (1, 0): Q(3), (1, 1): Q(1)}
    g = {(0, 1): Q(5), (1, 0): Q(7), (2, 0): Q(11)}
    product = mul_poly(f, g)
    assert_true(lead(product) == tuple(x + y for x, y in zip(lead(f), lead(g))),
                "least exponent of product is not additive")
    assert_true(product[lead(product)] == f[lead(f)] * g[lead(g)],
                "least coefficient of product is not the product of least coefficients")
    print("PASS least-term: exact RREF rank=3, pivots=(0,0),(0,1),(1,0); product lead is additive")


def filtration_basis(grades, cutoff):
    return [[Q(int(g <= cutoff)) if i == j else Q(0)
             for i, g in enumerate(grades)] for j in range(len(grades)) if grades[j] <= cutoff]


def check_lowering():
    # One length-two primitive string v0, e v0=v1, e v1=v2;
    # f v1=2v0, f v2=2v1; grades are -2,0,2 and center r=0.
    e = matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    f = matrix([[0, 2, 0], [0, 0, 2], [0, 0, 0]])
    grades, r = [-2, 0, 2], 0
    commutator = add(mul(f, e), mul(e, f), sign=-1)  # [f,e]
    relation = add(mul(commutator, e), mul(e, commutator), sign=-1)
    assert_true(relation == scale(-2, e), "[[f,e],e] != -2e")

    # Here F and G are independently supplied but equal standard filtrations.
    for name in ("F", "G"):
        for k in range(-3, 4):
            ak = filtration_basis(grades, k)
            assert_true(all(in_span(apply(e, v), filtration_basis(grades, k + 2)) for v in ak),
                        f"{name}: e does not raise filtration by at most 2")
            assert_true(all(in_span(apply(f, v), filtration_basis(grades, k - 2)) for v in ak),
                        f"{name}: f does not lower filtration by at most 2")

    for i in range(3):
        source = [j for j, g in enumerate(grades) if g == r - i]
        target = [j for j, g in enumerate(grades) if g == r + i]
        if not source and not target:
            continue
        block = [[power(e, i)[u][v] for v in source] for u in target]
        assert_true(len(source) == len(target) == rank(block),
                    f"E^{i} is not Lefschetz at center {r}")

    h = add(mul(e, f), mul(f, e), sign=-1)  # [e,f]
    assert_true(h == matrix([[-2, 0, 0], [0, 0, 0], [0, 0, 2]]),
                "computed h has the wrong graded eigenvalues")

    bad_relation = add(mul(zeros(3, 3), e), mul(e, zeros(3, 3)), sign=-1)
    assert_true(bad_relation != scale(-2, e), "negative fixture unexpectedly passes commutator gate")
    print("PASS lowering: exact sl2 relation, both filtration bounds, and all Lefschetz blocks")
    print("PASS lowering negative gate: f=0 is rejected by [[f,e],e]=-2e")


if __name__ == "__main__":
    check_least_terms()
    check_lowering()
    print("PASS all finite L17 fixtures")
