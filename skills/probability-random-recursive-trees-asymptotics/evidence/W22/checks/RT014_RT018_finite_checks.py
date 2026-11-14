"""Exact finite arithmetic checks tied to W22 L14_B4 source equations.

These checks validate selected formulas/recurrences on small inputs. They are
not proofs of any asymptotic theorem and do not verify the A127 interface.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, log, sqrt


def integrated_bm_covariance(k: int, ell: int, s: Fraction, u: Fraction) -> Fraction:
    """Integrate (s-y)^(k-1)(u-y)^(ell-1) exactly by polynomial expansion."""
    a = min(s, u)
    total = Fraction(0)
    for i in range(k):
        for j in range(ell):
            total += (
                (-1) ** (i + j)
                * comb(k - 1, i)
                * comb(ell - 1, j)
                * s ** (k - 1 - i)
                * u ** (ell - 1 - j)
                * a ** (i + j + 1)
                / (i + j + 1)
            )
    return total


@lru_cache(None)
def rrt_fringe_count_distribution(n: int, k: int) -> dict[int, Fraction]:
    """Exact law from RT018 (1), with uniform split I_n in {1,...,n-1}."""
    if n < k:
        return {0: Fraction(1)}
    if n == k:
        return {1: Fraction(1)}
    out: dict[int, Fraction] = defaultdict(Fraction)
    split_mass = Fraction(1, n - 1)
    for j in range(1, n):
        left = rrt_fringe_count_distribution(j, k)
        right = rrt_fringe_count_distribution(n - j, k)
        root_overlap = int(n - j == k)
        for x, px in left.items():
            for y, py in right.items():
                out[x + y - root_overlap] += split_mass * px * py
    return dict(out)


def moments(dist: dict[int, Fraction]) -> tuple[Fraction, Fraction]:
    mean = sum(Fraction(x) * p for x, p in dist.items())
    second = sum(Fraction(x * x) * p for x, p in dist.items())
    return mean, second - mean * mean


def main() -> None:
    print("RT017 integrated-Brownian covariance: exact polynomial integration")
    for k in range(1, 7):
        for ell in range(1, 7):
            got = integrated_bm_covariance(k, ell, Fraction(1), Fraction(1))
            expected = Fraction(1, k + ell - 1)
            assert got == expected, (k, ell, got, expected)
    print("  verified 36 pairs: Cov(R_k(1),R_l(1)) = 1/(k+l-1)")
    print("  example k=2,l=4:", integrated_bm_covariance(2, 4, Fraction(1), Fraction(1)))

    print("RT018 RRT fringe-count recurrence: exact rational distributions")
    cases = [(10, 1), (10, 2), (8, 3), (18, 4)]
    for n, k in cases:
        dist = rrt_fringe_count_distribution(n, k)
        mean, variance = moments(dist)
        target_mean = Fraction(n, k * (k + 1))
        target_variance = Fraction((2 * k * k - 1) * n, k * (k + 1) ** 2 * (2 * k + 1))
        assert mean == target_mean, (n, k, mean, target_mean)
        assert n > 2 * k
        assert variance == target_variance, (n, k, variance, target_variance)
        print(f"  n={n}, k={k}: support={len(dist)}, mean={mean}, variance={variance}")

    print("RT014 RRT low-level asymptotic correlation expression")
    for k, ell in [(1, 1), (2, 3), (5, 8), (10, 4)]:
        rho = sqrt((2 * k - 1) * (2 * ell - 1)) / (k + ell - 1)
        assert rho <= 1 + 1e-14
        if k == ell:
            assert abs(rho - 1.0) < 1e-14
        print(f"  k={k}, h={ell}: rho_0-formula={rho:.12f}")

    print("RT016 BST (m=2,t=0) Dirichlet split contraction factor at z=1,s=2")
    # V~Uniform[0,1]; lambda_1(z)=2z, so A_r=z V_r^(lambda_1(z)-1)=V_r at z=1.
    # E[V^2+(1-V)^2] = 2 int_0^1 v^2 dv = 2/3.
    contraction = 2 * Fraction(1, 3)
    assert contraction == Fraction(2, 3) and contraction < 1
    print("  exact E sum_r |A_r|^2 =", contraction)

    print("RT017 population-time scale: n^s versus n*s (finite numeric illustration, s=1/2)")
    for root_n in (10**2, 10**6):
        n = root_n * root_n
        power_index = root_n  # floor(n^(1/2)) is exact for these square n values.
        power_ratio = log(power_index) / log(n)
        linear_index = n // 2
        linear_ratio = log(linear_index) / log(n)
        assert abs(power_ratio - 0.5) < 1e-14
        assert linear_ratio > 0.9
        print(f"  n={n}: log(floor(n^s))/log(n)={power_ratio:.6f}; log(floor(ns))/log(n)={linear_ratio:.6f}")
    print("Evidence boundary: finite arithmetic only; no asymptotic proof or target-model transfer.")


if __name__ == "__main__":
    main()
