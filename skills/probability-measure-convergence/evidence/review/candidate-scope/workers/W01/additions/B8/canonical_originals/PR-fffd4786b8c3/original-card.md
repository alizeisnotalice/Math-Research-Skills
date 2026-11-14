# W02-S002 — Doob convergence theorems formalized in mathlib

## Source and reading scope

Kexing Ying and Rémy Degenne, “A Formalization of Doob’s Martingale Convergence Theorems in mathlib,” CPP 2023, DOI 10.1145/3573105.3575675; local arXiv v1 PDF, 14 pages. I read the complete original PDF, physical pp. 1–14 (including references). The paper describes the development as merged into mathlib at conference time; this card records the paper’s statements and does not independently check a current Lean source revision.

## Results and precise conditions

The paper defines conditional expectation for a Banach-valued integrable function on a measure space. If \(\mathcal B\subset\mathcal A\), the restriction of \(\mu\) to \(\mathcal B\) is sigma-finite, and \(f\in L^1(\mu;E)\), the conditional expectation exists and is unique up to a.e. equality (Definition 2.1, PDF p. 4). Its library function is total: outside these hypotheses it defaults to zero. Thus identities for that function are conditional on the stated domain hypotheses. The construction projects in \(L^2\) onto the closed subspace of \(\mathcal B\)-measurable functions, then extends to \(L^1\) through bounded linear extension from integrable simple functions (pp. 4–5).

The discrete-time Doob a.e. convergence theorem is stated for an adapted real submartingale \((f_n,\mathcal F_n)\) with a uniform \(L^1\) bound \(\sup_n\int |f_n|\le R\); it converges a.e. to an integrable \(\mathcal F_\infty=\sigma(\bigcup_n\mathcal F_n)\)-measurable version (Theorem 3.1, p. 8; proof pp. 10–11). The actual Lean lemma displayed for this result assumes a finite measure space. This is more general than a probability space, but it is still a finiteness hypothesis in the formalized statement.

Doob’s upcrossing estimate for an adapted submartingale on a finite measure space is (Theorem 3.2, pp. 9–10)
\[
(b-a)\,\mathbb E U_N(a,b)\le \mathbb E[(f_N-a)^+],\qquad
(b-a)\,\mathbb E U(a,b)\le \sup_N\mathbb E[(f_N-a)^+].
\]
The finite-horizon displayed lemma itself does not need \(a<b\): for \(a\ge b\) its left side is nonpositive and its right side nonnegative. The second inequality uses monotone convergence for the increasing upcrossing counts; their measurability comes from the stopping-time construction and each finite-horizon count is bounded by \(N\).

The \(L^1\) convergence theorem (Theorem 3.6, pp. 11–12) gives the equivalence for a discrete-time martingale: (i) probabilistic uniform integrability; (ii) convergence in \(L^1\) to an integrable \(\mathcal F_\infty\)-measurable \(f\); (iii) \(f_n=\mathbb E[f\mid\mathcal F_n]\) a.e. for every \(n\). The proof is decomposed into Theorem 3.7: UI implies an \(L^1\) bound, then Theorem 3.1 gives a.e. convergence, a.e. convergence gives convergence in measure, and Vitali gives \(L^1\) convergence; for a martingale, conditional-expectation contraction gives
\[
\|f_n-\mathbb E[f\mid\mathcal F_n]\|_1
=\|\mathbb E[f_m-f\mid\mathcal F_n]\|_1\le\|f_m-f\|_1\quad(m\ge n),
\]
so the difference vanishes as \(m\to\infty\). Conversely, the conditional expectations of one integrable \(g\) form a UI martingale; the limit is identified with \(g\) by equality of integrals over every \(\mathcal F_n\), followed by the \(\pi\)-system/Dynkin argument on the generated \(\mathcal F_\infty\) (pp. 11–12). The paper distinguishes analyst’s UI (uniform absolute continuity of integrals over small measurable sets) from probabilist’s tail UI; for finite \(\mu\), the latter is equivalent to the former plus uniform \(L^1\)-boundedness (Proposition 2.5, pp. 5–6). For formal reuse, carry through the displayed finite-measure assumptions: the a.e. convergence lemma requires a finite measure and the Vitali lemma is stated with `[is_finite_measure μ]` (pp. 11–12 and p. 6).

## Proof dependency and boundaries

For a.e. convergence the proof reduces convergence of each sample path to boundedness plus finitely many rational-band upcrossings. For fixed \(a<b\), recursively defined lower/upper hitting times select intervals \([\sigma_k,\tau_{k+1})\). Their indicator defines a bounded nonnegative predictable stake \(c_{n+1}=\sum_{k<N}1_{[\sigma_k,\tau_{k+1})}(n)\). The discrete stochastic integral \((c\cdot f)_N=\sum_{n<N}c_{n+1}(f_{n+1}-f_n)\) is a submartingale; telescoping each completed interval shows \((b-a)U_N\le(c\cdot f)_N\) up to the final nonnegative incomplete interval, while applying the same fact to \(1-c\) yields \(\mathbb E(c\cdot f)_N\le\mathbb E f_N-\mathbb E f_0\). After the positive-part/translation reduction this gives the displayed estimate (pp. 8–10). Uniform \(L^1\) boundedness bounds expected upcrossings; finite expectation makes the infinite upcrossing count finite a.s. Fatou’s lemma rules out paths with \(|f_n|\to\infty\), and the a.e. limit is measurable for \(\mathcal F_\infty\) and integrable by the same lemma (pp. 10–11).

Boundary: this is discrete time. In the formalization, stopping times take values in the time index and therefore cannot equal infinity; the paper explicitly notes the mismatch with the usual \(\tau\wedge n\) setup and duplicated stopped-process arguments (PDF p. 13). Do not silently apply the API to infinite-valued stopping times or continuous-time processes. The measure-space results are not all probability-only, but theorem 3.1’s displayed formal statement assumes finite measure. The general Banach-valued conditional expectation requires sigma-finiteness of the restricted measure and integrability; the article notes the construction does not cover all sigma-integrable functions.

## Use in this library

Use as a precise discrete-time source for the proof architecture behind Doob convergence, UI/Vitali, upcrossing, finite-range stopping-time formalization, and measure assumptions. It is a formalization paper, not a replacement for checking hypotheses of a new stochastic model; continuous time, extended-valued stopping times, and model-specific filtrations need separate justification.
