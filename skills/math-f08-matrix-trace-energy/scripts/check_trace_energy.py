#!/usr/bin/env python3
"""High-precision finite checks for the F08 matrix trace-energy formulas."""

from decimal import Decimal, getcontext

getcontext().prec = 70


def phi_diagonal(values):
    return sum(value.sqrt() * value for value in values)


def b_diagonal(values, entries):
    total = Decimal(0)
    for i, row in enumerate(entries):
        for j, entry in enumerate(row):
            total += entry * entry / (values[i].sqrt() + values[j].sqrt())
    return Decimal(3) * total / Decimal(2)


def main():
    # P=diag(4,9), K=[[1,2],[2,-1]].  A centred difference along K
    # is computed through the explicit two-by-two eigenvalue formula.
    p = (Decimal(4), Decimal(9))
    k = ((Decimal(1), Decimal(2)), (Decimal(2), Decimal(-1)))
    h = Decimal("1e-12")
    trace = p[0] + p[1]
    determinant = p[0] * p[1]
    def phi_at(sign):
        diagonal_sum = trace + sign * h * (k[0][0] + k[1][1])
        det = (p[0] + sign * h * k[0][0]) * (p[1] + sign * h * k[1][1]) - (sign * h * k[0][1]) ** 2
        discriminant = (diagonal_sum * diagonal_sum - Decimal(4) * det).sqrt()
        eigenvalues = ((diagonal_sum + discriminant) / 2, (diagonal_sum - discriminant) / 2)
        return phi_diagonal(eigenvalues)

    finite_second = (phi_at(1) - 2 * phi_diagonal(p) + phi_at(-1)) / (h * h)
    hessian = b_diagonal(p, k)
    assert abs(finite_second - hessian) < Decimal("2e-12"), (finite_second, hessian)

    # A commuting T +/- U instance checks the midpoint gap and its dyadic telescope.
    t = (Decimal(9), Decimal(16))
    u = (Decimal(3), Decimal(-4))
    midpoint_gain = (phi_diagonal((t[0] + u[0], t[1] + u[1])) + phi_diagonal((t[0] - u[0], t[1] - u[1]))) / 2 - phi_diagonal(t)
    midpoint_bound = b_diagonal(t, ((u[0], Decimal(0)), (Decimal(0), u[1]))) / (2 * Decimal(2).sqrt())
    assert midpoint_gain >= midpoint_bound
    parent = phi_diagonal(t)
    children_average = parent + midpoint_gain
    assert children_average - parent == midpoint_gain

    # sigma=1/2 gives p=3/2, q=3, D=sqrt(27/16).  Equality W=3 Z^2.
    sigma = Decimal("0.5")
    coefficient = sigma ** sigma / (1 + sigma) ** (1 + sigma)
    z = (Decimal(1), Decimal(2))
    w = tuple(Decimal(3) * item * item for item in z)
    young_gap = coefficient * sum(item * item.sqrt() for item in w) - sum(left * right for left, right in zip(w, z)) + sum(item ** 3 for item in z)
    assert abs(young_gap) < Decimal("1e-65"), young_gap
    nonoptimal_w = (Decimal(2), Decimal(5))
    nonnegative_gap = coefficient * sum(item * item.sqrt() for item in nonoptimal_w) - sum(left * right for left, right in zip(nonoptimal_w, z)) + sum(item ** 3 for item in z)
    assert nonnegative_gap > 0
    print("PASS: Hessian finite difference, midpoint gap, dyadic telescope, and trace Young equality")
    print(f"second={finite_second}; hessian={hessian}; midpoint={midpoint_gain}; lower={midpoint_bound}")


if __name__ == "__main__":
    main()
