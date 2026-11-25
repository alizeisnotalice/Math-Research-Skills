#!/usr/bin/env python3
"""Exact symbolic checks for the local N11 prescribed-velocity identities."""

import sympy as sp


def residual(field, variables, viscosity):
    t, x, y, z = variables
    velocity = sp.Matrix(field)
    convection = velocity[0] * velocity.diff(x) + velocity[1] * velocity.diff(y) + velocity[2] * velocity.diff(z)
    laplacian = velocity.diff(x, 2) + velocity.diff(y, 2) + velocity.diff(z, 2)
    return sp.simplify(velocity.diff(t) + convection - viscosity * laplacian)


def main():
    t, x, y, z, nu = sp.symbols("t x y z nu", positive=True)
    variables = (t, x, y, z)

    stream = t * x**2 * y
    planar = (sp.diff(stream, y), -sp.diff(stream, x))
    scalar = t**2 * (x + y)
    velocity = (*planar, scalar)
    divergence = sp.simplify(sp.diff(velocity[0], x) + sp.diff(velocity[1], y) + sp.diff(velocity[2], z))
    force = residual(velocity, variables, nu)
    scalar_force = sp.simplify(sp.diff(scalar, t) + planar[0] * sp.diff(scalar, x) + planar[1] * sp.diff(scalar, y) - nu * (sp.diff(scalar, x, 2) + sp.diff(scalar, y, 2)))
    assert divergence == 0
    assert sp.simplify(force[2] - scalar_force) == 0

    base = sp.Matrix((y, -x, 0))
    amplitude = t / (1 + t) ** 2
    slow = sp.log(1 + t) + 1 / (1 + t) - 1
    rescaled = amplitude * base
    expected = sp.diff(amplitude, t) * base + amplitude**2 * (base[0] * base.diff(x) + base[1] * base.diff(y)) - nu * amplitude * (base.diff(x, 2) + base.diff(y, 2) + base.diff(z, 2))
    assert sp.simplify(residual(rescaled, variables, nu) - expected) == sp.zeros(3, 1)
    assert sp.simplify(sp.diff(slow, t) - amplitude) == 0
    assert sp.limit(slow, t, sp.oo) == sp.oo

    phi = -sp.cos(x)
    raw_force = sp.Matrix((sp.sin(x), sp.cos(x), 0))
    projected = sp.simplify(raw_force - sp.Matrix((sp.diff(phi, x), sp.diff(phi, y), sp.diff(phi, z))))
    assert sp.simplify(sum(sp.diff(projected[i], (x, y, z)[i]) for i in range(3))) == 0
    assert projected == sp.Matrix((0, sp.cos(x), 0))

    scales = (sp.Rational(2), sp.Rational(3), sp.Rational(1, 6))
    assert sp.prod(scales) == 1
    print("PASS: residual/scalar reduction, onto clock, torus projection, determinant-one box scales")


if __name__ == "__main__":
    main()
