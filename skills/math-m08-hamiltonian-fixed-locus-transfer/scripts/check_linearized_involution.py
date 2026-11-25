#!/usr/bin/env python3
"""Exact local block check for the involution perturbation model."""

import sympy as sp


def rotation(angle):
    return sp.Matrix(
        [[sp.cos(angle), -sp.sin(angle)], [sp.sin(angle), sp.cos(angle)]]
    )


def main():
    epsilon = sp.symbols("epsilon", real=True)
    tangent_flow = rotation(epsilon)
    normal_flow = rotation(2 * epsilon)

    tangent_block = tangent_flow - sp.eye(2)
    normal_block = -normal_flow - sp.eye(2)

    tangent_det = sp.simplify(tangent_block.det())
    normal_det = sp.simplify(normal_block.det())
    assert sp.simplify(tangent_det - 4 * sp.sin(epsilon / 2) ** 2) == 0
    assert sp.simplify(normal_det - 4 * sp.cos(epsilon) ** 2) == 0
    assert tangent_det.subs(epsilon, sp.Rational(1, 5)) != 0
    assert normal_det.subs(epsilon, sp.Rational(1, 5)) != 0

    plus_generator = sp.Matrix([[0, -1], [1, 0]])
    minus_generator = sp.Matrix([[0, -2], [2, 0]])
    plus_limit = (sp.exp(epsilon * plus_generator) - sp.eye(2)) / epsilon
    minus_limit = -sp.exp(epsilon * minus_generator) - sp.eye(2)
    assert plus_limit.applyfunc(lambda entry: sp.limit(entry, epsilon, 0)) == plus_generator
    assert minus_limit.applyfunc(lambda entry: sp.limit(entry, epsilon, 0)) == -2 * sp.eye(2)
    print(
        "PASS: tangent det=4 sin(epsilon/2)^2; "
        "normal det=4 cos(epsilon)^2; both are nonzero at epsilon=1/5."
    )


if __name__ == "__main__":
    main()
