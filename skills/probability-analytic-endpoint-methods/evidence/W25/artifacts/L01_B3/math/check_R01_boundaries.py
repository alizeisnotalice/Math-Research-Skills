from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

# AEP-009 p. 5 finite counterexample to the proof's arbitrary-set affine step.
eps = sp.Rational(1, 10)
mu_F = eps**2 / 2
mu_affine_F = sp.Rational(1, 2) - (1 - 2 * eps) ** 2 / 2
ratio = sp.simplify(mu_affine_F / mu_F)

# AEP-016 vector log estimate: source prints K>2/pi but has |E|/(K-1).
K = sp.Rational(4, 5)
vector_log_rhs = sp.simplify(1 / (K - 1))  # f=0, |E|=1; left side is zero.
K_above_printed_threshold = float(K) > float(2 / sp.pi)

# AEP-016 Lemma 2.7 p<2: exact p=3/2 boundary and stationary comparisons.
p = sp.Rational(3, 2)
gamma0 = sp.simplify(p ** (-1 / (p - 1)) * sp.gamma(p / (p - 1)))
gamma_boundary_power = sp.simplify(gamma0 ** (p - 1))
gamma0_over_p = sp.simplify(gamma0 / p)
gamma0_over_2 = sp.simplify(gamma0 / 2)
t, g, gp = sp.symbols("t g gp", positive=True)
G_stationary = (t + g) * (t ** (p - 1) + 1 / p) - t**p - p * t ** (p - 1) * g
ode_rule = sp.Eq(1 + gp, p * (p - 1) * t ** (p - 2) * g)
# Substitute p(p-1)t^(p-1)g = t(1+g') at a stationary point.
G_stationary_collected = (t + g) / p - (p - 1) * t ** (p - 1) * g
G_stationary_reduced = sp.simplify(G_stationary_collected.subs(t ** (p - 1) * g, t * (1 + gp) / (p * (p - 1))))
G_target = sp.simplify((g - t * gp) / p)
stationary_identity_difference = sp.simplify(G_stationary_reduced - G_target)

# AEP-017 Theorem 4.11 generic-C scaling counterexample on the circle.
a = sp.Rational(1, 12)
C = a**2
th411_lhs_ratio = a
th411_printed_rhs_ratio = sp.simplify(6 * C)

# AEP-017 Prop. 4.6(14)/4.8 diagonal example, p=2, m=sigma=1, eigenvalue 1.
diagonal_norm_ratio = sp.simplify(1 / (sp.sqrt(2) - 1) / sp.sqrt(2))
diagonal_rhs = sp.Integer(1)  # p*=2, so p*-1=1.

result = {
    "tool": "Python + SymPy from project .runtime",
    "scope": "Exact finite counterexamples and algebraic identities for R01 B3 findings; not universal operator proofs.",
    "AEP009_affine_set_step": {
        "weight": "mu(dx)=|x| dx on R; doubling factor for centered intervals at dilation 2 is at most 4 (analytic case split)",
        "F": "[0,1/10]",
        "affine_map": "x -> 2(x-1)+1",
        "mu_F": str(mu_F),
        "mu_affine_F": str(mu_affine_F),
        "ratio": str(ratio),
        "conclusion": "ratio 36 exceeds the cube-doubling factor 4; arbitrary-set affine control used on p. 5 is not implied by doubling. This does not disprove the finite-union lemma or its Lebesgue specialization."
    },
    "AEP016_vector_log_range": {
        "source_printed_range": "K>2/pi",
        "K": str(K),
        "K_above_2_over_pi": K_above_printed_threshold,
        "f": "0",
        "event_measure": "1",
        "lhs": "0",
        "rhs": str(vector_log_rhs),
        "conclusion": "The printed range includes K<1, where the vector-log RHS is negative; operational restriction K>1 is necessary."
    },
    "AEP016_Lemma2_7_supplement": {
        "range": "1<p<2",
        "p_example": str(p),
        "gamma0_exact": str(gamma0),
        "gamma0_power_p_minus_1": str(gamma_boundary_power),
        "gamma0_over_p": str(gamma0_over_p),
        "gamma0_over_2": str(gamma0_over_2),
        "stationary_G_identity_difference": str(stationary_identity_difference),
        "analytic_argument_to_record": "gamma(t)~t^(2-p)/(p(p-1)) as t->infinity by l'Hopital on its defining tail integral, hence gamma(t)->infinity and the Taylor lower bound G(t)>=p(p-1)/2*(t+gamma(t))^(p-2)*gamma(t)^2 tends to infinity. Boundary G(0)=gamma(0)^p>=gamma(0)/2 follows from gamma(0)^(p-1)=Gamma(p/(p-1))^(p-1)/p>=1/p>1/2. At an interior minimum G'=0 gives (t+gamma)^(p-1)-t^(p-1)=1/p; the ODE gives G=(gamma-t*gamma')/p>=gamma(0)/p>gamma(0)/2 because gamma is concave. This independently supplies the missing global-minimum argument; other source steps remain as printed.",
        "conclusion": "Exact algebra checked; asymptotic/minimum argument is recorded as a W25 analytic supplement pending independent review."
    },
    "AEP017_Th4_11_generic_C": {
        "epsilon": str(a),
        "C": str(C),
        "lhs_norm_ratio": str(th411_lhs_ratio),
        "printed_rhs_ratio": str(th411_printed_rhs_ratio),
        "inequality_fails": bool(th411_lhs_ratio > th411_printed_rhs_ratio),
        "setting": "normalized circle, trivial real line bundle, L=partial_x^2, d_a=epsilon partial_x, eta=sin(x), p=2, Phi(x)=x^(-1/2), alpha=delta_0"
    },
    "AEP017_second_order_diagonal": {
        "setting": "normalized circle, L=partial_x^2, i=j=1, m=sigma=1, f=sin(x), p=2",
        "operator_norm_ratio": str(diagonal_norm_ratio),
        "printed_rhs": str(diagonal_rhs),
        "inequality_fails": bool(diagonal_norm_ratio > diagonal_rhs),
        "matrix_reason": "For i=j the source A_ij matrix has diagonal entry 2; its norm is 2, not the norm-one off-diagonal matrix used in the proof."
    }
}
assert ratio == 36
assert K_above_printed_threshold and vector_log_rhs == -5
assert gamma0 == sp.Rational(8, 9)
assert gamma_boundary_power == 2 * sp.sqrt(2) / 3
assert gamma0_over_p > gamma0_over_2
assert stationary_identity_difference == 0
assert th411_lhs_ratio == sp.Rational(1, 12) and th411_printed_rhs_ratio == sp.Rational(1, 24)
assert diagonal_norm_ratio == 1 + sp.sqrt(2) / 2 and diagonal_norm_ratio > diagonal_rhs
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
