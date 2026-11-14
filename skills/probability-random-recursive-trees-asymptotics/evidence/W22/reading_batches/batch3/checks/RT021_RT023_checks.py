"""Small exact checks for identities transcribed from the RT021/RT023 PDFs.

These calculations check algebra/normalization only; they do not prove any
probabilistic limit theorem.
"""
import sympy as sp

# RT021, Example 4.1 / Theorem 5.1: uniform ordered trees have
# Phi_tau(x)=1/(2-x), pi_0=1/2, and p_l=Phi_tau(p_{l-1})-pi_0.
l = sp.symbols("ell", integer=True, positive=True)
p = sp.symbols("p")
rec = sp.factor(1 / (2 - p) - sp.Rational(1, 2))
candidate = 3 / (4**l + 2)
assert sp.simplify(rec.subs(p, 3 / (4 ** (l - 1) + 2)) - candidate) == 0

# RT021, BST protected-root formula (6.3)-(6.4): integrate the printed
# non-protection polynomial against the independent Exp(1) time.
t = sp.symbols("t", positive=True)
q_not_protected = 2 * sp.exp(-t) - 2 * sp.exp(-2*t) + 2 * sp.exp(-3*t) - sp.exp(-4*t)
bst_protected = sp.simplify(1 - sp.integrate(q_not_protected * sp.exp(-t), (t, 0, sp.oo)))
assert bst_protected == sp.Rational(11, 30)

# RT023 Theorem 4.4: the constant fringe-size limit applies in the
# aperiodic case d_p=0. Choose letter probabilities (1/2,1/3,1/6);
# log 2/log 3 is irrational, so their logarithms are not on a common
# lattice. Check the printed limiting masses by telescoping.
H = -sum(q * sp.log(q) for q in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)))
tail_mass_factor = sp.summation(1 / (sp.Symbol("k", integer=True, positive=True) * (sp.Symbol("k", integer=True, positive=True) - 1)), (sp.Symbol("k", integer=True, positive=True), 2, sp.oo))
assert tail_mass_factor == 1
total_mass = sp.simplify(H / (1 + H) + tail_mass_factor / (1 + H))
assert total_mass == 1
aperiodic_leaf_mass = sp.N(H / (1 + H), 12)
aperiodic_k2_mass = sp.N(1 / (1 + H) / (2 * 1), 12)

print("RT021 uniform ordered-tree recursion: p_l=3/(4^l+2) substituted exactly; residual=0")
print(f"RT021 BST protected probability from (6.3)-(6.4): {bst_protected} = {sp.N(bst_protected, 12)}")
print("RT023 aperiodic fringe-size limiting masses: sum_{k>=2} 1/[k(k-1)] = 1; total including singleton mass = 1")
print(f"RT023 example probabilities (1/2,1/3,1/6): H={sp.N(H, 12)}; singleton mass={aperiodic_leaf_mass}; k=2 mass={aperiodic_k2_mass}")
print("RT023 symmetric binary law has d_p=log(2)>0, so its asymptotics use periodic (4.30), not convergence claim (4.31).")
print("Scope: exact recursion/integral/telescoping checks only; no asymptotic theorem or A127 interface proved.")
