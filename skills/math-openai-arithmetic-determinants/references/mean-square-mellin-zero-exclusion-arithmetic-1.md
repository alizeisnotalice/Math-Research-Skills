# Mean-square to Mellin zero exclusion

Source SHA-256: `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18` (49 physical pages; Wave 4 index checked). Physical pp.11--12 state Proposition 3.1 and its Mellin deduction; pp.21--22 state the scale-reducing transfer estimate.

For a finite-order Hecke character `nu`, excluded finite prime set `S`, and `W in C_c^infty((0,infty))`, the source assumes/proves the displayed mean-square bound (3.1) for `A_u(D)`. Its p.11 averaging gives (3.2), and p.12 obtains `A_1(D) << D^(11/12+epsilon)`. It then defines `M_W(s)=int A_1(D)D^(-s)dD/D`; the bound makes it holomorphic in `Re(s)>11/12`, while termwise integration for `Re(s)>1` gives `M_W(s)=hat W(s)/L_S,K(s,nu)`. A hypothetical zero `rho` is contradicted by choosing `W(y)=y^(-rho)phi(y)` with `phi>=0`, for which `hat W(rho)>0`.

Physical pp.21--22 provide a recursive scale interface: with `max(H,LF)<=Sigma`, the test functional `A(W)` is bounded by a supremum over `(H',X',F',Sigma')` satisfying the displayed inequalities (5.11)--(5.12), enabling finite induction after those inequalities are checked.

This is an analytic-transfer entry: preserve the smoothness, support, character, Euler-factor, and holomorphic-continuation prerequisites exactly.

## 固定来源

- 物理页 11, 12, 21, 22。Proposition 3.1, equations (3.1)–(3.3), and Proposition 5.4 (physical pp.11–12,21–22) SHA-256 `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`。[The Quasi-Riemann Hypothesis (alternate 11/12 proof)](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf)
