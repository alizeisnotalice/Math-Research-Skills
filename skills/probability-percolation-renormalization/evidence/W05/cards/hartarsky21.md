# hartarsky21 — Update-family infection time: two thresholds

**Reading status:** `partial_read`; PDF pp. 1–16 and 32–34 were read, not the whole 43-page paper. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Ivailo Hartarsky, “\(\mathcal U\)-Bootstrap Percolation: Critical Probability, Exponential Decay and Applications,” *Ann. Inst. H. Poincaré Probab. Stat.* 57(3) (2021), 1255–1280, DOI [10.1214/20-AIHP1112](https://doi.org/10.1214/20-AIHP1112), arXiv:1806.11405v4.

## Model and exact distinction

The paper studies finite update families on \(\mathbb Z^2\) with iid initial **infection** density \(q\), and local monotone updates \(A_{t+1}=A_t\cup\{x:\exists U\in\mathcal U,\ x+U\subseteq A_t\}\) (PDF pp. 3–5). It defines

\[
q_c=\inf\{q:\mathbb P_q([A]=\mathbb Z^2)=1\},\qquad
\widetilde q_c=\inf\{q:\sum_n n\theta_n(q)<\infty\},
\]

with \(q_c\le\widetilde q_c\) (PDF p. 8). Here \(\theta_n\) is the finite-volume one-arm/late-infection event; a second, reflexive event \(E_n\) records a chain of sites with large finite-box infection times (Definition 2.3, PDF pp. 10–11).

Theorem 3.5 (PDF pp. 14–15) proves for every update family in this 2D setting:

- if \(q>\widetilde q_c\), then for some \(c(q)>0\), both one-arm quantities \(\theta_n(q)\) and \(\widetilde\theta_n(q)\) decay at most \(e^{-c(q)n}\);
- if \(q<\widetilde q_c\), then \(\mathbb P_q(\tau_0>n)\ge c(q)/n\), hence \(\mathbb E_q\tau_0=\infty\).

The proof of the first assertion uses a randomized revealment algorithm for \(E_n\) (Lemma 7.3, PDF pp. 32–33), Russo’s formula and the revealment method of Duminil-Copin–Raoufi–Tassion. The paper explicitly notes that equality \(q_c=\widetilde q_c\) is expected but not known in general.

## Consequence for B179

The source proves an exponential tail in the regime \(q>\widetilde q_c\), not automatically for every \(q>q_c\). The possible interval \(q_c<q\le\widetilde q_c\), the requested all-subcritical-family claim, and extensions outside this 2D setting remain unproved interfaces. Also distinguish an exponential bound on a finite-volume one-arm event from the exact time tail in the question; the paper relates them using finite-range propagation and its event definitions. Do not replace the gap by the assertion “above criticality” without proving threshold equality.
