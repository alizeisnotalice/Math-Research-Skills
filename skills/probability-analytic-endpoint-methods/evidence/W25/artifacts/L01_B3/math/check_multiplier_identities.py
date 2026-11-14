from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

lam, m, sigma, y = sp.symbols("lambda m sigma y", positive=True, finite=True)
root = sp.sqrt(lam + m**2 / sigma**2)
rho = (root - m / sigma) / sigma
q = 2 * m / sigma**2
Ginf = (1 - sp.exp(-q * y)) / (2 * m)
K = sp.exp(-rho * y)
# AEP-017, §3.3.1: Phi(lambda)=int G(+infty,y) (d_y K)^2 a(y)^2 dy,
# with a=sigma and K(y,lambda)=exp(-rho*y).
phi_integrand = sp.expand(Ginf * sp.diff(K, y)**2 * sigma**2)
# Integrate the two exponential terms separately on (0,infinity); this
# explicit antiderivative avoids SymPy's conditional unevaluated Integral.
phi_integral = sp.simplify(
    sigma**2 * rho**2 / (2 * m) * (1 / (2 * rho) - 1 / (2 * rho + q))
)
phi_expected = sp.Rational(1, 4) * (1 - m / (sigma * root))
phi_difference = sp.simplify(phi_integral - phi_expected)

x = sp.symbols("x", positive=True, finite=True)
# AEP-017, Remark 4.7: scalar spectral multiplier in (14) tends to 2/x as sigma downarrow 0.
limand = 1 / ((sp.sqrt(x + m**2 / sigma**2) - m / sigma) * sp.sqrt(x + m**2 / sigma**2))
lim_exact = sp.simplify(sp.limit(limand, sigma, 0, dir="+"))

numeric = []
for xv, mv in [(sp.Rational(1, 2), sp.Rational(3, 2)), (sp.Integer(2), sp.Integer(1))]:
    vals = []
    for sv in [sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)]:
        actual = sp.N(limand.subs({x: xv, m: mv, sigma: sv}), 16)
        target = sp.N(2 / xv, 16)
        vals.append({"sigma": str(sv), "value": str(actual), "target_2_over_x": str(target), "absolute_error": str(abs(actual-target))})
    numeric.append({"x": str(xv), "m": str(mv), "checks": vals})

result = {
    "tool": "Python 3 + SymPy from project .runtime",
    "source": "AEP-017 arXiv:2003.02077v2, physical pp. 15–16 and 20–22",
    "checks": {
        "brownian_drift_vertical_diffusion_phi_integrand": str(phi_integrand),
        "brownian_drift_vertical_diffusion_phi_integral_minus_printed_formula": str(phi_difference),
        "remark_4_7_sigma_to_zero_operator_multiplier_limit": str(lim_exact),
    },
    "numeric_convergence_checks": numeric,
    "limitation": "These calculations verify scalar algebra and one-parameter numerical convergence only; they do not prove the martingale representation, Lp bounds, operator-domain claims, or endpoint estimates."
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
