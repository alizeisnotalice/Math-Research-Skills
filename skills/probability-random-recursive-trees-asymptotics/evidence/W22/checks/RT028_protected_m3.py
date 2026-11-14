"""Exact arithmetic check of the mean coefficient printed in RT028, Eq. (10)."""
from sympy import Rational, factorial, harmonic, simplify

m = 3
mu = simplify(
    Rational(1, m * (harmonic(m) - 1))
    * sum(
        factorial(m) / factorial(m - ell)
        * factorial(m * (m - ell))
        / factorial(m * (m - ell) + ell + 1)
        for ell in range(m)
    )
)
node_per_key = simplify(1 / (2 * (harmonic(m) - 1)))
protected_node_fraction = simplify(mu / node_per_key)
print(f"m={m}, protected-node linear mean coefficient mu={mu}={float(mu):.12f}")
print(f"RT022 Thm. 7.11 node/key coefficient={node_per_key}")
print(f"cross-source node-normalized fraction mu/node_per_key={protected_node_fraction}")
print(f"RT022 Thm. 10.3 value 19/140 matches={protected_node_fraction == Rational(19, 140)}")
print("Exact arithmetic consistency check only; it does not replace either source's proof.")
