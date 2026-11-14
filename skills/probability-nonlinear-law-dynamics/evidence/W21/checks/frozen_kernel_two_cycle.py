"""Exact synthetic counterexample: frozen kernels mix in one step, outer Phi cycles."""
import sympy as sp

p, q = sp.symbols('p q', real=True)
K = sp.Matrix([[p, 1-p], [p, 1-p]])  # states ordered 0,1; both rows equal
mu_p = sp.Matrix([[1-p, p]])          # Bernoulli(p), row-law convention
pi_p = sp.Matrix([[p, 1-p]])           # stationary row law of K_p

assert all(sp.simplify(x) == 0 for x in (K*K-K))
assert all(sp.simplify(x) == 0 for x in (pi_p*K-pi_p))
assert all(sp.simplify(x) == 0 for x in (mu_p*K-pi_p))

# The invariant law is Bernoulli(1-p); therefore the induced scalar outer map is 1-p.
phi = sp.simplify(1-p)
assert sp.simplify(phi.subs(p, phi)-p) == 0
assert sp.simplify(phi.subs(p, 0)) == 1
assert sp.simplify(phi.subs(p, 1)) == 0
assert sp.simplify(phi.subs(p, sp.Rational(1,2))-sp.Rational(1,2)) == 0

print('K_p =', K)
print('K_p^2 - K_p =', (K*K-K).applyfunc(sp.simplify))
print('mu_p (Bernoulli(p), states 0,1) =', mu_p)
print('unique stationary row law pi(K_p) =', pi_p)
print('outer scalar map Phi(p) =', phi)
print('Phi^2(p) - p =', sp.simplify(phi.subs(p, phi)-p))
print('orbit from p=0: 0,1,0,1,...; omega set {0,1}; neither point fixed')
print('scope: synthetic two-state law operator, not the A121 nearest-order-statistic kernel')
