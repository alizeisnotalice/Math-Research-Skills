# W02-S003 — Criens, Pfaffelhuber & Schmidt, *The Martingale Problem Method Revisited*

## Source and reading evidence

David Criens, Peter Pfaffelhuber, and Thorsten Schmidt, arXiv:2108.11930v1 (2021). The complete local 38-page PDF was read, physical pp. 1–38, including appendices and references. Identity was checked against arXiv front matter; the local SHA-256 is recorded in `sources.json`. The theorem statements and proof formulas cited below were visually checked in rendered original pages 13–14, 25–26, 28–30, and 33.

## Abstract martingale-problem limit theorem

Theorem 2.28 (PDF pp. 13–14) is a transfer theorem, not a tightness or uniqueness theorem. In its controlled formulation, Assumptions 2.21 and 2.27 and a dense time set (D\subset\mathbb R_+) are supplemented by:

1. (A1) the joint laws (Q_n=P_n\circ(L_n,X_n)^{-1}) converge weak-strong to (Q=P\circ(L,X)^{-1});
2. (A2) a determining family (Z^\circ\) for the test-process class \(\mathcal X\);
3. (A3) each (Y\in\mathcal X) has a canonical version (Y_t^\circ(L,X)); for dense (s<t) and determining (Z_s^\circ), both (Y_t^\circ) and (Y_t^\circ Z_s^\circ) are \((Q_n,Q)\)-continuous, the approximating test values are uniformly integrable on bounded time intervals, and
\[
\mathbb E^{P_n}\!\left[(Y_t^\circ(L_n,X_n)-Y_s^\circ(L_n,X_n))Z_s^\circ(L_n,X_n)\right]\longrightarrow0.
\]

Then (P\in\mathcal M(\mathcal X)): every test process is a martingale in the limit filtration. Proof: canonical versions express the limit expectation as a function of ((L,X)); weak-strong convergence plus continuity passes it to the limit of the approximating expectations, which vanish by the displayed identity. The determining family yields the conditional expectation identity at dense times. Uniform integrability, right-continuity, and Vitali's theorem extend it to arbitrary (s<t). Corollary 2.31 (pp. 14–15) is the no-control version; it still requires weak convergence, a determining set, canonical tests, uniform integrability, and the approximate identities.

## Application to path limits with jumps

Theorem 4.3 (PDF pp. 25–26) permits fixed discontinuity times: (X^n\Rightarrow X) in (D(E)) with Skorokhod (J_1), together with Assumptions 4.1–4.2, implies the limit law solves the stated martingale problem. Assumption 4.1 supplies high-probability jump control and compactness of the control-variable laws; Assumption 4.2 supplies bounded expectations and convergence of the generator, drift-integral, and compensator test identities at dense times. The proof extracts a weak-strong subsequence for ((L_n,X^n)), uses jump control to obtain the needed continuity on the relevant path sets, and applies Theorem 2.28. It is not enough to have path weak convergence alone.

Theorem 4.6 (PDF pp. 28–30) is a semimartingale-characteristics counterpart. Under weak (J_1) convergence, convergence in probability of drift (B^n), the modified second characteristic (\widetilde C^n), and tested jump compensators (g*\nu^n) to their canonical limit functionals on a dense time set, the theorem also requires stopped bounds involving \(\|\widetilde C^n_{T\wedge S_n}\|^2+g^2*\nu^n_{T\wedge S_n}\) and the same type of control-variable compactness and jump-control set. Here \(\widetilde C^{ij}=C^{ij}+\int h^i(x)h^j(x)\nu(dt,dx)-\sum_{s\le t}\Delta B_s^i\Delta B_s^j\), the modified second characteristic used in the martingale-problem formulation (Definition 2.4, PDF pp. 5–6); it is not simply the continuous characteristic \(C\). The conclusion is that the canonical limit is a semimartingale with characteristics ((B(X),C(X),\nu(X))) for the fixed continuous truncation function. The stopped bounds give true martingales and uniform integrability in the proof; they cannot be replaced by convergence of characteristics alone.

## Proof/use boundaries

For a diffusion problem, the test process is typically
\[
f(X_t)-f(X_0)-\int_0^t Lf(X_s)\,ds,
\]
with the chosen domain of (L) stated explicitly. A martingale-problem identification step does not prove tightness, convergence of coefficients, or uniqueness. For discontinuous limits, test continuity is delicate at fixed jumps and must be established with the theorem's path-control hypotheses. For C112, this source can organize a limit passage only after the conditioned laws, tightness, effective generator, and UI conditions are separately proved; it supplies neither a CLT nor positivity of a limiting covariance.
