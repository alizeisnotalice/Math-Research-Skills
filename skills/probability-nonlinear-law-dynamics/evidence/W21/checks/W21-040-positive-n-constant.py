from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 40

# State space {0,1}, metric d(0,1)=1.
# Ideal P has both rows delta_0. Two perturbations below are row-constant.
P = ((F(1), F(0)), (F(1), F(0)))
P_tilde_W = ((F(0), F(1)), (F(0), F(1)))
P_tilde_TV = ((F(19, 20), F(1, 20)), (F(19, 20), F(1, 20)))
assert P[0] == P[1] and P_tilde_W[0] == P_tilde_W[1] and P_tilde_TV[0] == P_tilde_TV[1]
assert P[0] != P_tilde_W[0] and P[0] != P_tilde_TV[0]

# Every positive power of P has both rows delta_0, so both Wasserstein
# tau(P^n) and the V=1 TV ergodicity distance are 0 for n>=1.
# For V~=1, delta=L=1/2 gives both drift inequalities required by Theorem 3.2.
# Initial laws are both delta_0.
C_W, rho_W, gamma_W, kappa_W = F(1, 10), F(1, 2), F(1), F(1)
true_W = F(1)  # delta_0 P = delta_0; delta_0 P_tilde_W = delta_1
n = 1
rhs_W = C_W * (rho_W**n * F(0) + (1-rho_W**n) * gamma_W*kappa_W/(1-rho_W))
rhs_W_repaired = max(C_W, F(1)) * (rho_W**n * F(0) + (1-rho_W**n) * gamma_W*kappa_W/(1-rho_W))
assert rhs_W == F(1, 10) and true_W > rhs_W and rhs_W_repaired == true_W

# For the TV theorem, ||delta_0 - (19/20 delta_0 + 1/20 delta_1)||_tv = 1/10
# under the source convention ||q||_tv = 2 sup_A |q(A)|.
C_TV, rho_TV, gamma_TV = F(1, 10000), F(1, 2), F(1, 10)
true_TV = gamma_TV
assert F(2) * F(1, 20) == true_TV
# Decimal evaluation of the printed noninitial term in (3.18), with kappa=1,L=delta=1/2.
D = Decimal
c, rho, gamma, L, kappa = D(1)/D(10000), D(1)/D(2), D(1)/D(10), D(1)/D(2), D(1)
log_inverse_gamma = (D(1)/gamma).ln()
printed_rhs_TV = (kappa * D(1).exp() / (D(1)-rho)
                  * (D(2)*c*(L+D(1))) ** (D(1)/log_inverse_gamma)
                  * gamma * log_inverse_gamma)
cprime = D(1)
repaired_rhs_TV = (kappa * D(1).exp() / (D(1)-rho)
                   * (D(2)*cprime*(L+D(1))) ** (D(1)/log_inverse_gamma)
                   * gamma * log_inverse_gamma)
assert printed_rhs_TV < D(1)/D(10)
assert repaired_rhs_TV > D(1)/D(10)

print('Exact two-state witness for the positive-integer convention:')
print('Ideal P has both rows delta_0; p_0 = p_tilde_0 = delta_0; V~=1; delta=L=1/2.')
print('For every n>=1: tau(P^n)=0 <= C*rho^n for any C>0, rho=1/2.')
print('Theorem 3.1 witness: P_tilde rows delta_1, gamma=kappa=1, C=1/10.')
print(f'  n=1 true W distance = {true_W}; printed RHS = {rhs_W}; repaired C\'=max(C,1) RHS = {rhs_W_repaired}.')
print('Theorem 3.2 witness: P_tilde rows (19/20 delta_0 + 1/20 delta_1), gamma=1/10, C=1/10000.')
print('  Source TV convention gives true n=1 distance = 1/10; Decimal-evaluated printed RHS =', printed_rhs_TV)
print('  Decimal-evaluated RHS after C\'=max(C,1) =', repaired_rhs_TV)
print('The examples isolate the zero-power constant issue under n in N = positive integers; the arithmetic is not a substitute for the theorem proofs.')
