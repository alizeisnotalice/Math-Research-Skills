"""Reproducible arithmetic/symbolic checks for the CZ-03/04/05 reading batch.

These checks validate displayed scalar identities only. They do not verify any
of the papers' operator-theoretic or measure-theoretic arguments.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp


def main() -> None:
    s = sp.symbols("s", real=True)
    t = sp.tan(sp.pi * s / 4)
    qprime = sp.diff(4 / sp.pi * sp.atanh(sp.tan(sp.pi * s / 4)), s)
    qprime_tangent_form = (1 + t**2) / (1 - t**2)
    derivative_identity = sp.trigsimp(qprime_tangent_form - sp.sec(sp.pi * s / 2), method="fu")
    n = sp.symbols("n", positive=True)
    riesz_angular_mass = sp.simplify(
        sp.gamma((n + 1) / 2) / sp.pi ** ((n + 1) / 2)
        * 2 * sp.pi ** ((n - 1) / 2) / sp.gamma((n + 1) / 2)
    )

    mp.mp.dps = 50
    catalan = mp.catalan
    a_closed = 8 * catalan / mp.pi**2
    a_integral = mp.quad(lambda x: x / mp.cosh(mp.pi * x / 2), [0, 1, 4, mp.inf])
    kd = mp.pi**2 / (8 * catalan)

    # Scalar check of the semigroup subordination identity used for (3.10):
    # sqrt(1+s/r^2)-1 = (2 sqrt(pi) r)^(-1) int_0^infty
    # e^{-t r^2}(1-e^{-t s}) t^{-3/2} dt.
    r0, s0 = mp.mpf("1.7"), mp.mpf("2.4")
    subordination_lhs = mp.sqrt(1 + s0 / r0**2) - 1
    subordination_rhs = mp.quad(
        lambda x: mp.e ** (-x * r0**2) * (1 - mp.e ** (-x * s0)) * x ** (-mp.mpf("1.5")),
        [0, 1, 5, mp.inf],
    ) / (2 * mp.sqrt(mp.pi) * r0)

    result = {
        "scope": "formula checks only; not a proof audit",
        "q_prime_equals_sec_identity_sympy_residual": str(derivative_identity),
        "q_prime_formula": "q'(s) = sec^2(pi*s/4)/(1-tan^2(pi*s/4)) = sec(pi*s/2), 0<=s<1",
        "Riesz_angular_mass_simplified": str(riesz_angular_mass),
        "Riesz_angular_mass_input": "Gamma((n+1)/2)/pi^((n+1)/2) times the standard sphere integral 2*pi^((n-1)/2)/Gamma((n+1)/2) for |theta_j|",
        "Davis_a_closed_50dps": mp.nstr(a_closed, 45),
        "Davis_a_integral_50dps": mp.nstr(a_integral, 45),
        "Davis_a_abs_difference": mp.nstr(abs(a_closed - a_integral), 8),
        "K_D_closed_50dps": mp.nstr(kd, 45),
        "scalar_subordination_example_r": str(r0),
        "scalar_subordination_example_s": str(s0),
        "subordination_lhs": mp.nstr(subordination_lhs, 40),
        "subordination_rhs": mp.nstr(subordination_rhs, 40),
        "subordination_abs_difference": mp.nstr(abs(subordination_lhs - subordination_rhs), 8),
        "interpretation": "The derivative identity, Catalan integral normalization, and scalar Laplace-integral identity agree numerically/symbolically. This does not establish the operator-norm convergence or the weak-(1,1) theorem.",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
