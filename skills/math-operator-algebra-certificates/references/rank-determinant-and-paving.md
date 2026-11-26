# Rank expansion, determinant normalization, and finite paving certificates

Use these routines with explicitly finite matrices, projections, or vector-bundle data.  Their source theorems require further structural hypotheses for global consequences.

## Collective rank expansion and normalized determinant potentials

**Source.** *An explicit obstruction to nuclear norm-ultrapower embeddings*, OpenAI (23 September 2026), physical pp. 5–8, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/paper.pdf), SHA-256 `4d38fbd185d56ad449e377de26b9ff2155485bda94fa89fc127304fe57117ad5`.

The finite input is a bundle-map family with the stated collective-rank-expansion property.  The source turns this into a determinant-potential normalization and then an obstruction construction.  A reusable certificate should therefore contain the ranks on every specified incidence, the nonvanishing determinant/potential domain, and the normalized maps, while separately naming any nuclearity or quotient-transport theorem used later.

**Source.** *A counterexample to Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness*, OpenAI (23 September 2026), physical pp. 5–8, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf), SHA-256 `c46465adfaef9b9fe3213d524a2c2cbee5015b686031c94192d1156a55dbde05`.

Its Lemmas 3.1–3.2 make the same computational interface explicit: verify the incidence-dimension inequality, construct smooth bundle maps with collective rank expansion, and apply a log-determinant potential to get continuous normalized maps.  The next proposition packages those maps; preserve the source's rank thresholds and domains in any reuse.

## Finite paving and even-moment spectral cuts

**Source.** *Approximation Paving over Arbitrary Maximal Abelian Subalgebras*, OpenAI (25 September 2026), physical pp. 14–17, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf), SHA-256 `2207c8250f6c641648a4b0727652808477d85678d518a9c641e4ca3e81c7d809`.

The source's finite interface is a mixed determinant identity followed by a rooted spectral-measure construction.  For a finite approximation, retain the chosen rooted measure, determinant identity, approximation tolerance, and the resulting diagonal/paving data rather than retaining only a norm claim.

**Scoped reference.** *Quadratic Strong-Operator Paving over Arbitrary Maximal Abelian Subalgebras*, OpenAI (25 September 2026), physical pp. 8–9, 12–13, and 52–53, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf), SHA-256 `d0cda0544b3c1b1b0091af621b26c2e66e1ac55e9ecb36c9c824d0c149dc3f1f`.

For a self-adjoint finite compression \(z=\sum_i p_i(x-a)p_i\), its final deterministic step uses
\[
 \varphi(z^{2k})<\rho\varepsilon^{2k},\qquad q=\mathbf1_{[-\varepsilon,\varepsilon]}(z),
\]
to conclude \(\varphi(1-q)<\rho\) and \(\|qzq\|\le\varepsilon\).  The accompanying checker computes exactly this finite-dimensional moment/Markov bound for a coordinate projection partition.  The general paving theorem still needs the source's masa, state, approximation and strong-operator hypotheses.
