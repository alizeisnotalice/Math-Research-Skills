import sympy as sp

q = sp.sqrt(sp.Rational(2, 3))
full_tail_factor = sp.simplify(1 / (1 - q))
assert sp.simplify(full_tail_factor - (3 + sp.sqrt(6))) == 0
# The source's finite sum for m=1, n=5 already exceeds its printed 3*q^m bound.
finite_sum = sp.simplify(sum(q**j for j in range(1, 5)))
ratio = sp.simplify(finite_sum / q)
assert sp.simplify(ratio - sp.Rational(5, 3) * (1 + q)) == 0
assert sp.simplify(5 * q - 4).is_positive
print('q =', q)
print('1/(1-q) =', full_tail_factor, '=', sp.N(full_tail_factor, 12))
print('sum(j=1..4) =', finite_sum, '=', sp.N(finite_sum, 12))
print('sum(j=1..4)/q =', ratio, '=', sp.N(ratio, 12), '> 3')
print('printed RHS factor 3*q =', sp.N(3*q, 12))
