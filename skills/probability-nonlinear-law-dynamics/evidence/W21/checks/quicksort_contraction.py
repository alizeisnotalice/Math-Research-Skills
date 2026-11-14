"""Symbolic checks for formulas printed in Rösler's Quicksort limit paper."""

import sympy as sp

u, a, b = sp.symbols("u a b", positive=True)
tau = sp.symbols("tau", real=True)
C = 2 * u * sp.log(u) + 2 * (1 - u) * sp.log(1 - u) + 1

# Use beta-function derivatives to evaluate the only mixed-log integral,
# avoiding a numerical quadrature and retaining exact constants.
cross = sp.diff(sp.beta(a, b), a, b).subs({a: 2, b: 2})
integral_x2_log2 = 2 * sp.integrate(u**2 * sp.log(u) ** 2, (u, 0, 1))
integral_A2 = sp.simplify(integral_x2_log2 + 2 * cross)
integral_C = sp.simplify(sp.integrate(C, (u, 0, 1)))
beta22 = sp.Rational(1, 6)
integral_A2 = sp.simplify(integral_A2.subs(sp.beta(2, 2), beta22))
integral_C2 = sp.simplify((4 * integral_A2 - 1).expand())
contraction_squared = sp.simplify(
    sp.integrate(tau**2 + (1 - tau) ** 2, (tau, 0, 1))
)

print("integral_0^1 C(u) du =", integral_C)
print("integral_0^1 [u log u + (1-u) log(1-u)]^2 du =", integral_A2)
print("integral_0^1 C(u)^2 du =", integral_C2)
print("3 * integral_0^1 C(u)^2 du =", sp.simplify(3 * integral_C2))
print("integral_0^1 [tau^2 + (1-tau)^2] dtau =", contraction_squared)
print("W2 contraction factor =", sp.sqrt(contraction_squared))
