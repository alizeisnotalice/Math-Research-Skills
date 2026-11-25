#!/usr/bin/env python3
"""Finite exact replay for L11's elementary algebraic interfaces.

This checks one fixed rational Gram--Schmidt configuration, the PSD determinant
comparison used after Gaussian smoothing, the corresponding Gaussian-difference
covariance, and one exact projected-ellipsoid volume.  It deliberately does not
attempt to prove the measure-theoretic theorems.
"""

from fractions import Fraction
from math import pi, sqrt


def det2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    # t1=(0,0,0), t2=(3,0,0), t3=(1,4,0).  Thus D^T D is exact.
    gram = ((9, 3), (3, 17))
    gram_det = det2(gram)
    heights_product_sq = 3**2 * 4**2
    assert gram_det == 144 == heights_product_sq

    # With delta^2=1, I+11^T=[[2,1],[1,2]] for the two differences.
    noise = ((2, 1), (1, 2))
    covariance = tuple(
        tuple(gram[i][j] + noise[i][j] for j in range(2)) for i in range(2)
    )
    covariance_det = det2(covariance)
    assert covariance == ((11, 4), (4, 19))
    assert covariance_det == 193 > gram_det

    # Lemma 3.3 with m=1,k=3 evaluates the centered bivariate Gaussian density.
    gaussian_difference_density = 1.0 / (2.0 * pi * sqrt(covariance_det))

    # For A=diag(3,4) embedded in R^(2x3), R=5: v_2 R^2 sqrt(det AA^T).
    projected_ellipsoid_area = pi * 5**2 * 12
    assert Fraction(5**2 * 12, 1) == 300

    print("gram_det=", gram_det)
    print("height_product_sq=", heights_product_sq)
    print("smoothed_covariance=", covariance)
    print("smoothed_covariance_det=", covariance_det)
    print("gaussian_difference_density=%.15g" % gaussian_difference_density)
    print("projected_ellipsoid_area=300*pi=%.15g" % projected_ellipsoid_area)
    print("status=PASS (finite algebraic replay only)")


if __name__ == "__main__":
    main()
