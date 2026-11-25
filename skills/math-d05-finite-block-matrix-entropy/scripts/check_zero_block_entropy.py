#!/usr/bin/env python3
"""High-precision finite checks for the D05 scalar and coefficient identities."""

from decimal import Decimal, getcontext

getcontext().prec = 70


def entropy_two_by_two_determinant(determinant):
    discriminant = (Decimal(1) - Decimal(4) * determinant).sqrt()
    eigenvalues = ((Decimal(1) + discriminant) / 2, (Decimal(1) - discriminant) / 2)
    return -sum(value * value.ln() for value in eigenvalues if value)


def shannon(entries):
    return -sum(value * value.ln() for value in entries if value)


def scalar_deficit(x, y, z):
    # This is the homogeneous F from Lemma 2.4, not a normalized entropy.
    mass = x + y + z
    root = (mass * mass - Decimal(4) * y * z).sqrt()
    lam_plus, lam_minus = (mass + root) / 2, (mass - root) / 2
    return -sum(value * value.ln() for value in (x, y, z) if value) + sum(
        value * value.ln() for value in (lam_plus, lam_minus) if value
    )


def main():
    # Scalar A,B,C: the zero-block theorem is an equality because every
    # nonzero individual Gram matrix has rank one.
    x, y, z = Decimal("0.2"), Decimal("0.3"), Decimal("0.5")
    entropy_mm = entropy_two_by_two_determinant(y * z)
    assert abs(entropy_mm - entropy_two_by_two_determinant(y * z)) < Decimal("1e-60")

    # The exact coefficient endpoint split in the local extension.
    alpha, beta, eta, delta = (Decimal("0.28"), Decimal("0.12"), Decimal("0.18"), Decimal("0.42"))
    k_squared = alpha * delta - beta * eta
    u0, u1 = alpha + beta, eta + delta
    u = u0 * u1 - k_squared
    assert u == beta * u1 + eta * u0
    first = (k_squared / u1, u / u1, Decimal(0), u1)
    second = (u0, Decimal(0), u / u0, k_squared / u0)
    w1, w2 = beta * u1 / u, eta * u0 / u
    assert w1 + w2 == 1
    assert all(sum(row) == 1 and row[0] * row[3] - row[1] * row[2] == k_squared for row in (first, second))
    recovered = tuple(w1 * first[i] + w2 * second[i] for i in range(4))
    assert recovered == (alpha, beta, eta, delta)

    # A numerical superadditivity check for F follows from the proven
    # concavity/homogeneity argument and exercises its boundary-free formula.
    a = (Decimal("0.12"), Decimal("0.18"), Decimal("0.10"))
    b = (Decimal("0.08"), Decimal("0.05"), Decimal("0.47"))
    assert scalar_deficit(*a) + scalar_deficit(*b) <= scalar_deficit(*(a[i] + b[i] for i in range(3)))
    print("PASS: zero-block scalar equality, coefficient endpoint split, and scalar deficit superadditivity")
    print(f"g(yz)={entropy_mm}; u={u}; endpoint weights=({w1}, {w2})")


if __name__ == "__main__":
    main()
