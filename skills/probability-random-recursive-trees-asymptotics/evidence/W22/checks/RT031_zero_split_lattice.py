"""Exact finite-law check for the RT031 zero-splitter lattice-scope example.

This diagnoses the literal log(V*) interface only; it is not an asymptotic
proof or a counterexample to the paper's theorem.
"""

from fractions import Fraction as F


split_law = {
    (F(1, 2), F(1, 2)): F(1, 2),
    (F(1), F(0)): F(1, 4),
    (F(0), F(1)): F(1, 4),
}
b = 2

assert sum(split_law.values()) == 1
assert all(sum(v) == 1 for v in split_law)
p_max_one = sum(p for v, p in split_law.items() if max(v) == 1)
p_min_positive = sum(p for v, p in split_law.items() if min(v) > 0)
assert p_max_one == F(1, 2)
assert p_min_positive == F(1, 2)

# V* selects a uniform coordinate independently of the split vector.
vstar = {}
for v, p in split_law.items():
    for coordinate in v:
        vstar[coordinate] = vstar.get(coordinate, F(0)) + p / b
assert vstar == {F(1, 2): F(1, 2), F(1): F(1, 4), F(0): F(1, 4)}

# Standard split vectors have beta=1.  The Radon–Nikodym factor is b*v.
vhat = {v: p * b * v for v, p in vstar.items() if p * b * v > 0}
assert vhat == {F(1, 2): F(1, 2), F(1): F(1, 2)}
assert sum(vhat.values()) == 1

print("b = 2; standard split vector; beta = 1")
print(f"P(V_(1)=1) = {p_max_one}; P(V_(2)>0) = {p_min_positive}")
print("V* exact masses:", {str(k): str(v) for k, v in sorted(vstar.items())})
print(f"P(V*=0) = {vstar[F(0)]}; literal log(V*) undefined with this probability")
print("Vhat exact masses:", {str(k): str(v) for k, v in sorted(vhat.items())})
print("-log(Vhat) support = {0, log(2)}; arithmetic span = log(2)")
print("Scope: exact probability-law check only; no renewal theorem or asymptotic conclusion inferred.")
