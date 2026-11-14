"""Finite/symbolic checks tied to the cited formulas; these are not proofs."""
from fractions import Fraction
from math import gamma, pi
import json

# RT015: fixed-point second-moment identity for alpha=1/2.
a = 0.5
moment_coefficient = (a*a + 1.0)/(2.0*a + 1.0)
cross = 2.0*a*gamma(a+1)**2/gamma(2*a+2)  # 2 alpha B(alpha+1,alpha+1)
m2_from_fixed_point = cross/(1.0-moment_coefficient)
m2_gamma_formula = gamma(a+1)**2/((1.0-a/2.0)*gamma(2*a+1))

# RT024: exact expectation recurrence for leaves in a uniform binary increasing tree.
# With n existing vertices, there are n+1 free positions; 2L belong to leaves.
leaf_mean = Fraction(1, 1)
leaf_means = {1: leaf_mean}
for n in range(1, 100001):
    leaf_mean = leaf_mean + 1 - Fraction(2, n+1)*leaf_mean
    if n+1 in (2, 3, 10, 100, 1000, 100000):
        leaf_means[n+1] = leaf_mean

# RT035: deterministic symmetric two-type urn alpha=2, beta=1.
# A=[[2,1],[1,2]], lambda1=3, v1=(1/2,1/2), a=(1,1), D=I/2.
# Evaluate the source integral (5.2) numerically via the exact eigenspace reduction
# M exp(sA)=exp(s)M, M=I-v1*a^T.
import sympy as sp
A = sp.Matrix([[2,1],[1,2]])
lam1 = sp.Integer(3)
v1 = sp.Matrix([[sp.Rational(1,2)],[sp.Rational(1,2)]])
activity = sp.Matrix([[1,1]])
D = sp.Rational(1,2)*sp.eye(2)
M = A - lam1*v1*activity
s = sp.symbols("s", nonnegative=True)
P = sp.Matrix([[sp.Rational(1,2),-sp.Rational(1,2)],[-sp.Rational(1,2),sp.Rational(1,2)]])
expA = sp.exp(3*s)*v1*activity + sp.exp(s)*P
assert sp.simplify(M*expA - sp.exp(s)*M) == sp.zeros(2)
integrand = sp.simplify(lam1*M*expA*D*expA.T*M.T*sp.exp(-lam1*s))
Sigma_exact = integrand.applyfunc(lambda entry: sp.integrate(entry, (s,0,sp.oo)))
Sigma_expected = sp.Rational(3,4)*sp.Matrix([[1,-1],[-1,1]])

out = {
    "checks_are_numeric_or_finite_recurrence_not_proofs": True,
    "RT015_alpha": a,
    "RT015_E_X2_from_fixed_point": m2_from_fixed_point,
    "RT015_E_X2_from_Corollary1_gamma_expression": m2_gamma_formula,
    "RT015_abs_difference": abs(m2_from_fixed_point-m2_gamma_formula),
    "RT015_first_moment_rhs": a/(a+1)+(1/(a+1)),
    "RT024_binary_leaf_mean_exact_recurrence_samples": {str(k): {"exact_fraction": f"{v.numerator}/{v.denominator}", "ratio_to_n": float(v/k)} for k,v in leaf_means.items()},
    "RT024_leaf_limit_formula_d2_k1": 2*1/((1*1+2)*(1*1+1)),
    "RT035_two_type_A": [[int(v) for v in row] for row in A.tolist()],
    "RT035_lambda1": int(lam1),
    "RT035_lambda2": 1.0,
    "RT035_integrand_from_source_formula": [[str(v) for v in row] for row in integrand.tolist()],
    "RT035_sigma_from_source_integral": [[str(v) for v in row] for row in Sigma_exact.tolist()],
    "RT035_sigma_from_Example7.2_formula": [[str(v) for v in row] for row in Sigma_expected.tolist()],
    "RT035_sigma_exact_difference": [[str(v) for v in row] for row in (Sigma_exact-Sigma_expected).tolist()],
}
print(json.dumps(out, indent=2, sort_keys=True))
