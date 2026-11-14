"""Exact symbolic algebra checks for two R02-requested formula corrections.

These checks verify displayed algebra/limits only; they are not proofs of the
source's probabilistic limit theorems or of RT002's uniform O(1) remainder.
"""
import sympy as sp
import sys

mu, sigma2, beta2, rho = sp.symbols("mu sigma2 beta2 rho", positive=True)

# RT020 equations (7.8)--(7.10): Cov(Y,S)=-mu and Var(S)=sigma2.
cov_y_s = -mu
coef = mu / sigma2
cov_corrected = sp.simplify(cov_y_s + coef * sigma2)
var_corrected = sp.simplify(beta2 + 2 * coef * cov_y_s + coef**2 * sigma2)
cov_wrong_sign = sp.simplify(cov_y_s - coef * sigma2)
var_wrong_sign = sp.simplify(beta2 - 2 * coef * cov_y_s + coef**2 * sigma2)

# RT004 equation (12.10): substitute z=psi(1+rho)-psi(1) and take rho->0.
z = sp.digamma(1 + rho) - sp.digamma(1)
prefactor = -z * sp.gamma(-rho) / sp.polygamma(1, 1 + rho)
prefactor_limit = sp.simplify(sp.limit(prefactor, rho, 0))

assert cov_corrected == 0
assert sp.simplify(var_corrected - (beta2 - mu**2 / sigma2)) == 0
assert sp.simplify(cov_wrong_sign + 2 * mu) == 0
assert sp.simplify(var_wrong_sign - (beta2 + 3 * mu**2 / sigma2)) == 0
assert prefactor_limit == 1

print(f"Runtime: Python {sys.version.split()[0]}, SymPy {sp.__version__}")
print("RT020 corrected projection covariance:", cov_corrected)
print("RT020 corrected projection variance:", var_corrected)
print("RT020 wrong-sign covariance:", cov_wrong_sign)
print("RT020 wrong-sign variance:", var_wrong_sign)
print("RT004 full gamma prefactor limit at z=0:", prefactor_limit)
print("Scope: algebra/limit checks only; no theorem proof or RT002 O(1) bound.")
