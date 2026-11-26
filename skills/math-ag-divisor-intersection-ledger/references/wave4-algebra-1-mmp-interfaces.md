# Wave 4 algebra-1: MMP discrepancy and nef-adjoint interfaces

These OpenAI-draft interfaces are pinned to `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`. They support only a supplied finite divisor/discrepancy ledger.

## Generalized lc Q-pairs

*Minimal models and Mori fibre spaces for generalized log canonical Q-pairs*, SHA-256 `37e6d650c989c3fb3316987648aff5865f1615323274b50e5bea4794155bd22f`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/paper.pdf), physical pp. 8--16, Theorem 3.1 and equations (3.2)--(3.9).

For a scaling program the source writes `A_i(u)=A_{X_i}(u)`, `E_i(u)=A_i(u)-A_X(u)`, and `Delta_i(u)=A_{i+1}(u)-A_i(u)>=0`. For `0<t<=lambda_i`, its equation (3.3) is
`F_i(t;u)=sum_{j<i}(1-t/lambda_j) Delta_j(u)`.
At a scaling value, semiampleness yields `sigma_u(lambda_i)<=E_i(u)<=sigma_u`; after multiplier-ideal stabilization the source obtains its uniform bound (3.7). The local phase assertion and all termination, multiplier-ideal, finite-extension, and toroidal arguments remain required source hypotheses/proof stages.

## Numerical dimension one

*Minimal models in numerical dimension one*, SHA-256 `6fe4b337ba8c912889b0495f65c298d03abbee61c1f1641bd5a99113adf8b624`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/paper.pdf), physical pp. 5--7, Lemmas 2.2--2.3 and the perturbation construction.

On a common resolution of a canonical step, the draft takes `D=p^*K_U-q^*K_{U+}` and uses negativity to conclude `D>=0`; coefficientwise `a(F,U+)-a(F,U)=coeff_F(D)`. Its codimension-two stabilization uses the finite-dimensional cycle-class space `A_{n-2}(V)` and the monotone dimension inequality (2.3). The subsequent dyadic perturbations are `t_j=2^{-j}` and have boundaries `Delta_j=t_{j+1}B_{V_j}`.

## Nef adjoints

*Numerical Semiampleness of Nef Adjoint Divisors*, SHA-256 `b3f337e5dc5b1eda3afe298c6b97ff5eade266947e89021accfb331a3c9048c3`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/paper.pdf), physical pp. 1--4 and 6, Theorem 1.1, Lemma 2.1, and Lemma 3.2.

Its stated input is a projective klt rational pair in characteristic zero, `K_X+B` pseudoeffective, `M` nef rational Cartier, and `D=K_X+B+M` nef. The result is a semiample rational Cartier `L` with `D equiv L`. For pseudo-effective `D`, the finite support decomposition is `N_sigma(D)=sum_Gamma sigma_Gamma(D) Gamma`, `P_sigma(D)=D-N_sigma(D)`. Lemma 2.1 supplies nonnegative degree on every curve through a sufficiently very general point.

The ledger may verify supplied rational equalities, inequalities, supports, and intersection entries. It cannot check klt, nefness, pseudoeffectivity, MMP termination, multiplier ideals, a very-general condition, or numerical semiampleness. All three items are source-stated, not independently proof-audited.
