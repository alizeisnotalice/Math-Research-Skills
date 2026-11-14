# AIDEKON2014SPEED — speed of biased walk on a Galton–Watson tree

**Source:** Elie Aïdékon, “Speed of the Biased Random Walk on a Galton–Watson Tree,” *Probability Theory and Related Fields* 159 (2014), 597–617, DOI 10.1007/s00440-013-0515-y; local file is arXiv:1111.4313v4. Complete 22-page preprint read (SHA-256 `541ff7432d7a9726a3c04350829b57db00192aea496a3aa04c8b6ff9d030f6f0`). The transition convention and Theorem 1.1 formula were checked on rendered physical PDF p. 2.

## Model and speed theorem

The offspring law ν takes values in \(\mathbb N\) (leaves are allowed), with \(m=\mathbb E\nu\in(1,\infty)\); the Galton–Watson tree is conditioned to survive. At a non-artificial vertex \(x\), the λ-biased walk moves to its parent with probability λ/(\lambda+\nu(x)) and to each child with probability (1/(\lambda+\nu(x))); the walk is reflected at an artificial parent \(e_*\). Thus larger λ means stronger bias toward the root. Put \(q=\mathbb P(\text{extinction})\) and \(\lambda_c=\mathbb E[\nu q^{\nu-1}]\). The paper's positive-speed regime is \(\lambda\in(\lambda_c,m)\), where the a.s. speed \(\ell_\lambda=\lim_n|X_n|/n\) is deterministic and positive.

For a fixed tree, \(\beta(x)=P_x(\tau_{x^*}=\infty)\) is the quenched probability of never hitting the parent. In Theorem 1.1 (PDF p. 2), let \(\beta_0,\beta_1,\ldots\) be iid copies of \(\beta(e)\), independent of \(\nu\). Then
\[
\ell_\lambda=
\frac{\mathbb E\!\left[\dfrac{(\nu-\lambda)\beta_0}{\lambda-1+\sum_{i=0}^{\nu}\beta_i}\right]}
{\mathbb E\!\left[\dfrac{(\nu+\lambda)\beta_0}{\lambda-1+\sum_{i=0}^{\nu}\beta_i}\right]}.
\]
The identical denominator and the index range \(i=0,\ldots,\nu\) are part of the statement. The speed formula is not a theorem about harmonic-measure dimension.

## Proof dependencies

The proof first defines fresh epochs and a backward tree. Proposition 3.2 (PDF pp. 8–10) uses time reversal/branching to identify the tree seen from a first-visited vertex; regeneration epochs and Lemma 3.3 give the asymptotic frequency of fresh epochs, with finite mean regeneration time exactly in the positive-speed interval. Theorem 4.1 (PDF pp. 11–12, proved pp. 18–21) identifies the limiting environment seen from the particle on trees with a marked backbone, with density proportional to
\[
\frac{(\lambda+\nu_+(e))\beta(e)}{\lambda-1+\beta(e)+\sum_{i=1}^{\nu_+(e)}\beta_+(i)}.
\]
Here the normalizing constant is finite by Lemma 4.2 (pp. 13–14), using the conductance recursion \(\beta(e)=\sum_i\beta(i)/(\lambda+\sum_i\beta(i))\) and \(\lambda>\lambda_c\). Finally, §5 (p. 21) writes the one-step generation increment as \((\nu(X_k)-\lambda)/(\nu(X_k)+\lambda)\), uses Theorem 4.1: the speed numerator is the stationary expected generation increment, and the denominator in (1.4) is the normalizing expectation for the invariant environment density.

## Scope for W20 problems

This source supplies a speed formula only under \(m<\infty\), survival conditioning, and \(\lambda\in(\lambda_c,m)\). Speed, transience, and harmonic-measure dimension are distinct observables. Do not infer monotonicity of harmonic-measure dimension from speed comparisons, and keep the toward-root bias convention explicit when comparing to other papers.

## Complete-paper coverage

Physical PDF pp. 1–3: model, regimes, Theorem 1.1; pp. 3–6: tree and backward-tree preliminaries; pp. 7–10: fresh epochs, time reversal, and regeneration; pp. 11–20: invariant environment, conductance recursion, integrability and proof of Theorem 4.1; p. 21: speed proof; p. 22: references. All 22 pages were read; the exact formula (including the denominator λ−1+Σβ_i), invariant density, and conductance recursion were checked against rendered pages.
