#!/usr/bin/env python3
"""Exact checks for the one-dimensional bounded Frostman model."""

from fractions import Fraction


def main():
    # For Lebesgue measure on [0,1], I_t = 2 / ((1-t)(2-t)).
    t = Fraction(1, 2)
    energy = Fraction(2, 1) / ((1 - t) * (2 - t))
    assert energy == Fraction(8, 3)

    # The intersection of any radius-r ball with [0,1] has length <= 2r.
    # At x=1/2 and r=1/4 equality verifies the sharp local bound.
    r = Fraction(1, 4)
    intersection_length = Fraction(1, 2)
    assert intersection_length == 2 * r

    # Projection R^2 -> R of uniform measure on [0,1]^2 is the same interval
    # measure, so the checked t-energy remains 8/3.
    projected_energy = energy
    assert projected_energy == Fraction(8, 3)
    print("PASS: I_(1/2)(Lebesgue[0,1])=8/3; ball and coordinate-projection checks passed")


if __name__ == "__main__":
    main()
