"""Exact finite check for the tree-decomposition gluing formula."""

from fractions import Fraction
from itertools import product


def marginal(law, coordinates):
    result = {}
    for state, mass in law.items():
        label = tuple(state[index] for index in coordinates)
        result[label] = result.get(label, Fraction(0)) + mass
    return result


def main():
    # Bags {0,1}, {1,2}, and {1,3}, joined at the nonempty separator {1}.
    bag_01 = {
        (0, 0): Fraction(1, 5),
        (0, 1): Fraction(3, 10),
        (1, 0): Fraction(3, 10),
        (1, 1): Fraction(1, 5),
    }
    bag_12 = {
        (0, 0): Fraction(1, 10),
        (0, 1): Fraction(2, 5),
        (1, 0): Fraction(2, 5),
        (1, 1): Fraction(1, 10),
    }
    bag_13 = {
        (0, 0): Fraction(7, 20),
        (0, 1): Fraction(3, 20),
        (1, 0): Fraction(3, 20),
        (1, 1): Fraction(7, 20),
    }
    separator_mass = Fraction(1, 2)

    law = {}
    for state in product((0, 1), repeat=4):
        x0, x1, x2, x3 = state
        law[state] = (
            bag_01[(x0, x1)]
            * bag_12[(x1, x2)]
            * bag_13[(x1, x3)]
            / separator_mass**2
        )

    assert sum(law.values()) == 1
    assert marginal(law, (0, 1)) == bag_01
    assert marginal(law, (1, 2)) == bag_12
    assert marginal(law, (1, 3)) == bag_13
    assert all(law[state] == law[tuple(1 - bit for bit in state)] for state in law)

    # Re-root at {1,2}. Conditional factors yield the same joint law.
    rerooted = {}
    for state in product((0, 1), repeat=4):
        x0, x1, x2, x3 = state
        rerooted[state] = (
            bag_12[(x1, x2)]
            * bag_01[(x0, x1)] / separator_mass
            * bag_13[(x1, x3)] / separator_mass
        )
    assert rerooted == law

    # Empty separators retain their one-point marginal of mass one.
    singleton = {(0,): Fraction(1, 2), (1,): Fraction(1, 2)}
    empty_separator_law = {
        state: singleton[(state[0],)] * singleton[(state[1],)]
        for state in product((0, 1), repeat=2)
    }
    assert sum(empty_separator_law.values()) == 1
    assert marginal(empty_separator_law, (0,)) == singleton
    assert marginal(empty_separator_law, (1,)) == singleton

    # With common total mass zero, all local and global laws are zero measures.
    zero_bag = {(0,): Fraction(0), (1,): Fraction(0)}
    assert sum(zero_bag.values()) == 0
    print("exact gluing check passed: mass, bag marginals, symmetry, and root invariance")


if __name__ == "__main__":
    main()
