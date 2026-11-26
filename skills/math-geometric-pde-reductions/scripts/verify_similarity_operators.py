"""Symbolically verify O43's exact similarity-variable derivative identities.

Scope: supplied O43 preprint, physical p. 5, equation (3).  The program
derives q_t and q_z from the implicit coordinate relation, applies the chain
rule to independent polynomial profiles f(x,e), then compares the result with
the stated T_b and Z_b expressions.  It does not solve or discretize the PDE.
"""
import sympy as sp

Q = sp.symbols("Q", positive=True)
h, e, x, z, t = sp.symbols("h e x z t", real=True)
D = sp.Rational(1, 2) - h
d = 1 - e**2
L = 1 - 2 * h * e**2

# The relation tau = Q(1-e^2), e=z Q^(-D), expressed without e.
relation = Q - z**2 * Q**(1 - 2 * D) - (1 - t)
Rq = sp.diff(relation, Q).subs(z, e * Q**D)
Rz = sp.diff(relation, z).subs(z, e * Q**D)
assert sp.simplify(Rq - L) == 0

# Implicit differentiation at fixed z and fixed t, respectively.
qt = sp.simplify(-sp.diff(relation, t) / Rq)
qz = sp.simplify(-Rz / Rq)
assert sp.simplify(qt + 1 / L) == 0
assert sp.simplify(qz - 2 * e * Q**(1 - D) / L) == 0

# Chain derivatives of x=r^2/(2Q), e=z Q^(-D).
xt = sp.simplify(-x * qt / Q)
et = sp.simplify(-D * e * qt / Q)
xz = sp.simplify(-x * qz / Q)
ez = sp.simplify(Q**(-D) - D * e * qz / Q)
assert sp.simplify(xt - x / (Q * L)) == 0
assert sp.simplify(et - D * e / (Q * L)) == 0
assert sp.simplify(xz + 2 * e * x * Q**(-D) / L) == 0
assert sp.simplify(ez - Q**(-D) * d / L) == 0

tests = [
    (sp.Rational(7, 3), x**3 * e**4 + 2 * x * e - 5),
    (-sp.Rational(5, 4), x**2 * e**5 - 3 * x**4 + e**2),
    (sp.Rational(1, 2), 1 + x**5 * e**3 - 7 * x**2 * e**6),
]
for i, (bval, f) in enumerate(tests, start=1):
    # Chain rule applied to Q^b f(x,e).
    actual_t = sp.expand(bval * Q**(bval - 1) * qt * f + Q**bval * (sp.diff(f, x) * xt + sp.diff(f, e) * et))
    actual_z = sp.expand(bval * Q**(bval - 1) * qz * f + Q**bval * (sp.diff(f, x) * xz + sp.diff(f, e) * ez))
    expected_t = Q**(bval - 1) / L * (-bval * f + D * e * sp.diff(f, e) + x * sp.diff(f, x))
    expected_z = Q**(bval - D) / L * (2 * bval * e * f + d * sp.diff(f, e) - 2 * e * x * sp.diff(f, x))
    rt = sp.simplify(actual_t - expected_t)
    rz = sp.simplify(actual_z - expected_z)
    print(f"case={i} b={bval} T_residual={rt} Z_residual={rz}")
    assert rt == 0 and rz == 0

print("PASS: all exact chain-rule residuals vanish")
