"""Exact algebraic consistency checks for Heyda (2026), not recurrence proofs."""
from fractions import Fraction as F
import json
from pathlib import Path

out = Path(__file__).with_name('w14_044_exact_checks_output.txt')
delta1 = delta2 = delta3 = F('0.05')
delta4 = F('0.6')
beta = F('2.00046')
alpha = F('1.28020')

# In 4D, the middle 2x2 covariance block has eigenvalues 2 and 2 beta.
eigs4 = [F(1), F(1), F(2), 2 * beta]
assert all(x > 0 for x in eigs4)

# The first reflection column equals (1,1,1,1+delta1); theta + R e1 = v.
theta4 = [-F(1)] * 4
first_col4 = [F(1), F(1), F(1), F(1) + delta1]
v4 = [theta4[i] + first_col4[i] for i in range(4)]
assert v4 == [F(0), F(0), F(0), delta1]
assert all(x >= 0 for x in v4) and v4[0] == 0

# In 5D, likewise theta + R e1 = delta1 e5; H Sigma H^T = I.
theta5 = [-F(1)] * 5
first_col5 = [F(1), F(1), F(1), F(1), F(1) + delta1]
v5 = [theta5[i] + first_col5[i] for i in range(5)]
assert v5 == [F(0), F(0), F(0), F(0), delta1]
assert all(x >= 0 for x in v5) and v5[0] == 0
h = [F(1), 1/alpha, 1/alpha, 1/alpha, F(1)]
sigma5_diag = [F(1), alpha**2, alpha**2, alpha**2, F(1)]
transformed_diag = [h[i]**2 * sigma5_diag[i] for i in range(5)]
assert transformed_diag == [F(1)] * 5
transformed_drift = [h[i] * theta5[i] for i in range(5)]
assert transformed_drift == [-F(1), -1/alpha, -1/alpha, -1/alpha, -F(1)]

result = {
    'source': 'W14-044 Heyda (2026), Theorems 2.2, 2.4, 2.5; Eqs. (2.3.1)-(2.4.3)',
    'tool': 'Python fractions.Fraction exact rational arithmetic',
    'input': {'delta1': str(delta1), 'delta2': str(delta2), 'delta3': str(delta3), 'delta4': str(delta4), 'beta_threshold': str(beta), 'alpha_threshold': str(alpha)},
    'checks': {
        '4D_covariance_eigenvalues_at_beta_threshold': [str(x) for x in eigs4],
        '4D_theta_plus_first_reflection_column': [str(x) for x in v4],
        '5D_theta_plus_first_reflection_column': [str(x) for x in v5],
        '5D_HSigmaHt_diagonal': [str(x) for x in transformed_diag],
        '5D_transformed_drift': [str(x) for x in transformed_drift]
    },
    'result': 'All exact algebraic identities and positivity checks passed.',
    'limit': 'Consistency checks only; they do not prove positive recurrence, capture-time tail bounds, or the numerical eigenvalue thresholds.'
}
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
