"""Exact finite-state check illustrating why ordinary weak convergence is too weak.

For n>=2, let mu_n put mass 1/2 at (0,0) and 1/2 at (1/n,2), while
mu puts mass 1/2 at each of (0,0),(0,2).  The state space is R with bounded
compatible metric d(x,y)=min(1,|x-y|); the path metric for p=1 is d(x1,y1)+d(x2,y2).
"""
from fractions import Fraction as Q
import json
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')

# Every ordinary weak test is continuous on R^2, and the moving atom (1/n,2)
# converges to (0,2), so mu_n => mu.  Compute the relevant adapted-W1 coupling.
# Write a coupling matrix between rows X=(0,0),(1/n,2) and columns Y=(0,0),(0,2).
# Marginals 1/2 force the matrix to [[a,1/2-a],[1/2-a,a]].  Bicausality in
# the reverse direction requires X_1 independent of Y_2, since Y_1 is constant;
# with both Bernoulli marginals 1/2 this forces a=1/4 and every cell is 1/4.
# Thus there is a unique bicausal coupling and its cost is exact.
cols = [(Q(0), Q(0)), (Q(0), Q(2))]
q = [[Q(1, 4), Q(1, 4)], [Q(1, 4), Q(1, 4)]]

def d(a, b):
    return min(Q(1), abs(a-b))

def adapted_cost(n):
    rows = [(Q(0), Q(0)), (Q(1, n), Q(2))]
    return sum(
        q[i][j] * (d(rows[i][0], cols[j][0]) + d(rows[i][1], cols[j][1]))
        for i in range(2) for j in range(2)
    )

checked_costs = {str(n): str(adapted_cost(n)) for n in range(2, 21)}
for n in range(2, 21):
    assert adapted_cost(n) == Q(1, 2) + Q(1, 2*n)
assert adapted_cost(10) == Q(11, 20)
assert all(adapted_cost(n) > Q(1, 2) for n in range(2, 21))

# Continuous bounded adapted rewards on Omega=R^2:
# L_1=1; L_2(x1,x2)=min(2,max(0,x2)).  For finite-support laws, the
# source-convention value is v_L(mu)=inf_{tau<=2} E[L_tau] = E[min(L_1,E[L_2|X_1])].
# Under mu_10 the two histories reveal terminal rewards 0 and 2, giving 1/2;
# under mu the common history has conditional mean 1, giving 1.
value_mu_n_inf = (min(Q(1), Q(0)) + min(Q(1), Q(2))) / 2
value_mu_inf = min(Q(1), (Q(0)+Q(2))/2)
value_mu_n_sup = (max(Q(1), Q(0)) + max(Q(1), Q(2))) / 2
value_mu_sup = max(Q(1), (Q(0)+Q(2))/2)
assert value_mu_n_inf == Q(1, 2)
assert value_mu_inf == Q(1)
assert value_mu_n_sup == Q(3, 2)
assert value_mu_sup == Q(1)

result = {
    'calculation': 'exact Fraction arithmetic; finite two-stage example, p=1',
    'state_metric': 'd(x,y)=min(1,abs(x-y)) on R; path metric is sum of the two stage costs',
    'laws': {
        'mu_n': '1/2 delta_(0,0) + 1/2 delta_(1/n,2)',
        'mu': '1/2 delta_(0,0) + 1/2 delta_(0,2)',
        'ordinary_weak_convergence': 'mu_n => mu by continuity of bounded continuous test functions at (1/n,2)->(0,2)',
    },
    'bicausal_constraint': 'reverse causality forces X1 independent of Y2 because Y1 is constant; all four coupling cells are 1/4',
    'adapted_W1_at_n_10': str(adapted_cost(10)),
    'adapted_W1_exact_checks_n_2_to_20': checked_costs,
    'general_adapted_W1_formula': '1/2 + 1/(2n), hence not -> 0',
    'stopping_rewards': 'L1=1; L2(x1,x2)=min(2,max(0,x2)); bounded continuous and adapted',
    'source_stopping_convention': 'v_L(mu)=inf_{tau<=2} E_mu[L_tau] (cost/minimization), as defined in the source p. 6',
    'source_inf_stopping_value_at_mu_n': str(value_mu_n_inf),
    'source_inf_stopping_value_at_mu': str(value_mu_inf),
    'alternative_sup_reward_convention': 'sup_{tau<=2} E_mu[L_tau]; distinct from the source v_L convention',
    'sup_reward_value_at_mu_n': str(value_mu_n_sup),
    'sup_reward_value_at_mu': str(value_mu_sup),
    'interpretation': 'weak process-law convergence alone does not imply continuity of the source inf stopping value; the example is within finite horizon, not a model-specific queue theorem',
}
OUT.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
