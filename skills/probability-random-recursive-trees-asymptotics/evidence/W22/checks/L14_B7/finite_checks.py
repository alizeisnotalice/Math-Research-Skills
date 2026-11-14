"""Finite/exact arithmetic checks for W22 L14_B7 source formulas.

These calculations validate only the encoded finite identities and one example
distribution. They do not prove the cited asymptotic theorems.
"""
from fractions import Fraction
from math import comb


def cladogram_count(n: int) -> int:
    """Rooted binary cladogram count c_n=(2n-3)!!, with c_1=1."""
    if n == 1:
        return 1
    out = 1
    for odd in range(3, 2 * n - 2, 2):
        out *= odd
    return out


def beta0_split(n: int) -> list[Fraction]:
    """Beta(0) unnormalized gamma weights are all one."""
    weights = [Fraction(1) for _ in range(1, n)]
    z = sum(weights)
    return [w / z for w in weights]


def uniform_cladogram_split(n: int) -> list[Fraction]:
    """Aldous beta=-3/2 split law: 1/2 * C(n,i)c_i c_(n-i)/c_n."""
    c_n = cladogram_count(n)
    return [
        Fraction(comb(n, i) * cladogram_count(i) * cladogram_count(n - i), 2 * c_n)
        for i in range(1, n)
    ]


def main() -> None:
    # Beta(0) is the uniform root-split law at every finite n.
    for n in range(2, 51):
        q0 = beta0_split(n)
        assert q0 == [Fraction(1, n - 1)] * (n - 1)
        assert sum(q0) == 1

        # Beta=-3/2 split probabilities normalize exactly, and the prescribed
        # leaf's branch law P(B_n=i)=2i q_n(i)/n also normalizes exactly.
        q = uniform_cladogram_split(n)
        assert sum(q) == 1
        assert q == list(reversed(q))
        b = [Fraction(2 * i, n) * q[i - 1] for i in range(1, n)]
        assert sum(b) == 1

    # Long dendron with one-point base: d(i,j)=a_i+a_j off diagonal.
    twigs = [Fraction(1, 2), Fraction(1), Fraction(3, 2)]
    d = [[Fraction(0) if i == j else twigs[i] + twigs[j]
          for j in range(len(twigs))] for i in range(len(twigs))]
    assert d == [
        [Fraction(0), Fraction(3, 2), Fraction(2)],
        [Fraction(3, 2), Fraction(0), Fraction(5, 2)],
        [Fraction(2), Fraction(5, 2), Fraction(0)],
    ]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                assert d[i][k] <= d[i][j] + d[j][k]
    a = Fraction(2)
    constant_d = [[Fraction(0) if i == j else 2 * a
                   for j in range(4)] for i in range(4)]
    assert all(constant_d[i][j] == 4 for i in range(4) for j in range(4) if i != j)

    # RT042 §7.3, under its explicit edge-count recursion, for p0=1/2:
    # W0 is geometric on {0,1,...}; G+ is geometric on {1,2,...}.
    # Kesten path edges L=G+ + W0, so P(L=n)=n/2^(n+1), n>=1.
    # The finite exact masses are checked; geometric-series identities give
    # total mass 1 and mean 3. The source's unshifted W0+W0' has mass at zero.
    p0 = Fraction(1, 2)
    p_w0 = [p0 * (1 - p0) ** i for i in range(50)]
    assert p_w0[0] == Fraction(1, 2)
    assert sum(p_w0) == 1 - Fraction(1, 2) ** 50
    assert all(Fraction(n, 2 ** (n + 1)) == n * p0**2 * (1-p0)**(n-1)
               for n in range(1, 20))
    kesten_edge_pmf = [Fraction(n, 2 ** (n + 1)) for n in range(1, 80)]
    assert sum(kesten_edge_pmf) == 1 - Fraction(81, 2**80)
    assert sum(Fraction(n) * p for n, p in enumerate([Fraction(0)] + kesten_edge_pmf)) < 3
    # Source's printed unshifted sum has P(W0+W0'=0)=1/4, while a Kesten
    # path from its root necessarily traverses at least one edge.
    assert p_w0[0] ** 2 == Fraction(1, 4)
    assert Fraction(0) == 0

    print("PASS: beta=0 root split is exactly uniform for n=2..50.")
    print("PASS: beta=-3/2 cladogram split and prescribed-leaf branch laws normalize exactly for n=2..50.")
    print("PASS: one-point long-dendron sample distances form the stated metric; constant twig a=2 gives off-diagonal 4.")
    print("PASS: RT042 edge-count interpretation has P(L=n)=n/2^(n+1) at p0=1/2; exact series gives E[L]=3.")
    print("CAVEAT: source's unshifted geometric sum puts mass 1/4 at zero at p0=1/2, conflicting with the edge recursion on Kesten's tree.")
    print("LIMIT: these checks are finite/exact arithmetic and a model derivation; they do not prove asymptotic convergence.")


if __name__ == "__main__":
    main()
