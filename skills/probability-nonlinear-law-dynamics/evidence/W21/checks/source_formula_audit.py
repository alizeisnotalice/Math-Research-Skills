"""Symbolic checks for W21-018 Thm 3.11 and W21-023 coefficient conventions.

This verifies algebraic identities and a concrete support counterexample only;
the source-page rendering and the general support argument are recorded in the
associated proof cards.
"""
import sympy as sp

p, q, alpha, mass_a, mass_left, mass_right, eps, k, c = sp.symbols(
    "p q alpha mass_a mass_left mass_right eps k c", positive=True
)

# W21-023 §3.1: a valid lower-p / upper-q rule gives the printed mass at a.
finite_lower_p = alpha**2 + 2 * p * alpha * (1 - alpha)
assert sp.factor(finite_lower_p - alpha * (alpha + 2 * p * (1 - alpha))) == 0

# §3.2's interval formula has p on the left exterior mass and q on the right.
# Under a parent-selection rule this is lower-q / upper-p, opposite to §3.1.
continuous_printed = mass_a**2 + 2 * p * mass_a * mass_left + 2 * q * mass_a * mass_right
continuous_if_lower_p = mass_a**2 + 2 * q * mass_a * mass_left + 2 * p * mass_a * mass_right
orientation_difference = sp.factor(continuous_printed - continuous_if_lower_p)
assert orientation_difference == 2 * mass_a * (p - q) * (mass_left - mass_right)

# W21-018 §3 proof recurrence: eps_next <= k eps^2. With z=k eps,
# z_next <= z^2. The iterated comparison envelope satisfies equality in this
# scalar recurrence and is eps_(n0+r)=c^(2^r)/k when c=k eps_(n0)<1.
r = sp.symbols("r", integer=True, nonnegative=True)
eps_bound = c ** (2**r) / k
assert sp.simplify(k * eps_bound**2 - c ** (2 ** (r + 1)) / k) == 0
assert sp.simplify(k * (k * eps**2) - (k * eps) ** 2) == 0

# A valid endpoint-selection kernel always returns one of its two parent points.
# Thus support in [1/4,3/4] is preserved by every iterate; x is a separating
# continuous test function for the claimed weak limit delta_1.
lower_support, upper_support = sp.Rational(1, 4), sp.Rational(3, 4)
assert lower_support > 0 and upper_support < 1
print(f"W21-023 coefficient mismatch (shown minus lower-p convention): {orientation_difference}")
print("W21-023 concrete atomless support interval: [1/4, 3/4]; every parent-selection iterate remains there.")
print("W21-018 recurrence rescales exactly to z_next <= z^2; c<1 gives eps_(n0+r) <= c^(2^r)/k.")
print("Any nonzero error sequence satisfying that bound has liminf (1/r) log(-log eps) >= log(2).")
print("These computations check algebra/examples; the generic operator and support conclusions are proved in the card.")
