"""Exact/algebraic checks accompanying the two B18 reading cards.
These checks illustrate formulas and a counterexample; they do not prove the papers' theorems.
"""
from fractions import Fraction
import json
import sympy as sp

x, y, r, lam = sp.symbols('x y r lam', real=True)
J = sp.Rational(1, 2) * (x**2 - 2*r*x*y + y**2)
J_completed = sp.Rational(1, 2) * (x-r*y)**2 + sp.Rational(1, 2) * (1-r**2)*y**2
conditional_rate = sp.simplify(J - sp.Rational(1, 2)*(1-r**2)*y**2)
mgf_limit = lam*r*y + sp.Rational(1, 2)*lam**2
legendre_objective = lam*x - mgf_limit
critical_lam = sp.solve(sp.diff(legendre_objective, lam), lam)[0]
legendre = sp.simplify(legendre_objective.subs(lam, critical_lam))
source_example9_1_rate = (x-r*y)**2
quadratic_matrix = sp.Matrix([[1, -r], [-r, 1]])
normalizer_determinant = sp.factor(quadratic_matrix.det())
normalizer_eigenvalues = [sp.factor(v) for v in quadratic_matrix.eigenvals()]

# Finite exact example: P_n((X,Y)=(0,1/n))=P_n((1,-1/n))=1/2.
# Then P_n weakly converges to 1/2 delta_(0,0)+1/2 delta_(1,0).
# At y_n=1/n the regular conditional law is delta_0; at the limit Y=0
# the conditional law is the mixture (1/2,1/2), since Y is constant.
finite = {
    "joint_masses_for_each_n": ["1/2", "1/2"],
    "E_n_X_given_Y_eq_1_over_n": "0",
    "limit_E_X_given_Y_eq_0": "1/2",
    "conditional_weak_test_gap_for_phi(x)=x": "1/2",
    "joint_weak_convergence": "yes: Y-coordinates converge uniformly to 0 on the two atoms; X-marginal is unchanged",
}

result = {
    "gaussian_completion_square_residual": str(sp.simplify(J-J_completed)),
    "conditional_rate_from_Thm1_2_or_Thm1_3": str(conditional_rate),
    "scaled_log_mgf": str(mgf_limit),
    "legendre_optimizing_lambda": str(critical_lam),
    "legendre_transform_of_scaled_log_mgf": str(legendre),
    "printed_Example_9_1_rate_as_extracted": str(source_example9_1_rate),
    "Example_9_1_normalizer_quadratic_matrix_determinant": str(normalizer_determinant),
    "Example_9_1_normalizer_quadratic_matrix_eigenvalues": [str(v) for v in normalizer_eigenvalues],
    "Example_9_1_finite_normalizer_condition": "positive definite iff 1-r**2>0, i.e. |r|<1; combined with the source's r!=0 gives 0<|r|<1",
    "printed_rate_minus_legendre_rate": str(sp.simplify(source_example9_1_rate-legendre)),
    "finite_joint_weak_but_conditional_gap": finite,
    "scope": "Symbolic algebra verifies the Gaussian exponent/rate normalization, positive-definiteness determinant condition for a finite 2D normalizer, and an exact finite conditional-kernel discontinuity example. It does not establish the large-deviation theorem or repair the source's Example 9.1 sentence."
}
print(json.dumps(result, indent=2))
