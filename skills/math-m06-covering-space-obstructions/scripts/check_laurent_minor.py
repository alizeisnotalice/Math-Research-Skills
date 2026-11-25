#!/usr/bin/env python3
"""Exact finite check for the Laurent-minor step used in the cyclic-cover lemma."""

from sympy import Matrix, symbols


def main():
    z = symbols("z")
    boundary = Matrix([[z, 1], [0, z + 1]])
    determinant = boundary.det().expand()
    assert determinant.subs(z, 1) == 2
    assert determinant != 0
    assert boundary.subs(z, 1).rank() == 2

    # A nonzero determinant supplies a left inverse over C(z), hence no kernel there.
    adjugate_identity = (boundary.adjugate() * boundary).applyfunc(lambda entry: entry.expand())
    assert adjugate_identity == determinant * Matrix.eye(2)
    print(
        "PASS: D(z) has nonzero Laurent minor "
        f"{determinant}; D(1) determinant is 2; adjugate certificate verified."
    )


if __name__ == "__main__":
    main()
