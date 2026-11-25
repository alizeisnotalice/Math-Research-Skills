#!/usr/bin/env python3
"""Exact symbolic checks for the narrow cusp-elimination certificate."""

import sympy as sp


def main() -> None:
    h, u, v, w = sp.symbols("h u v w")
    x = u**3 + h * v
    y = -u**2 + h * w
    s_value = 2 * u**3 * v + 3 * u**4 * w + h * (v**2 - 3 * u**2 * w**2) + h**2 * w**3
    assert sp.expand(x**2 + y**3 - h * s_value) == 0

    U, V, W, G, y_symbol = sp.symbols("U V W G y")
    universal_s = 2 * U**3 * V + 3 * U**4 * W + h * (V**2 - 3 * U**2 * W**2) + h**2 * W**3
    transformed = sp.expand(universal_s.subs(V, G - U * W) - (h * G**2 - 2 * U * y_symbol * G + y_symbol**2 * W))
    assert sp.expand(transformed.subs(y_symbol, h * W - U**2)) == 0

    p = -2 * s_value**2 * x + 3 * s_value * y**2 - 3 * s_value**3 * y
    F = h - p - 1
    critical = {h: 2, u: 0, v: sp.Rational(-1, 2), w: sp.Rational(1, 2)}
    assert F.subs(critical) == -1
    assert all(sp.diff(F, variable).subs(critical) == 0 for variable in (h, u, v, w))

    # A zero-divisor example of alpha*h + beta*y = 1 in Z/6Z.
    modulus, alpha, beta, h0, y0 = 6, 2, 1, 2, 3
    assert (alpha * h0 + beta * y0) % modulus == 1
    r = alpha * (1 + beta * y0)
    q = beta**2
    assert (r * h0 + q * y0**2) % modulus == 1

    print("PASS: cusp identity, G substitution, critical point, and Z/6 unit-ideal certificate")


if __name__ == "__main__":
    main()
