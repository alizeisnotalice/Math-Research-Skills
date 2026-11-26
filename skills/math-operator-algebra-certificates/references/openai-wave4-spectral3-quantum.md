# Scoped OpenAI quantum and QAC0 interfaces (wave4 spectral-3)

These records preserve the source conditions and are not certificates of a
spectral gap, a threshold state, magnetization, or a circuit lower bound.

## Boundary-field spin-one chain

*A boundary-field gap for the spin-one Heisenberg chain* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/paper.pdf), SHA-256 `7fb53ff5eb7f82060d746192174c1165fa4d5b994ffbcb5e489b4f2534ccc1a7`, physical pp. 1--3, 6--10) uses the paper's finite-volume spin-one Hamiltonian, boundary field, and parameter regime.  Lemma 3.1 and (3.3) give the named local concentration/propagation input.  Its usable rule is conditional: propagate a local concentration estimate only after retaining the exact finite-volume boundary term, the stated spectral projection, and its parameter inequalities.  It is not a gap statement for a changed spin, boundary condition, or infinite-volume limit.

## BFSS massive comparison and profile exclusion

*The unique threshold bound state of the SU(N) BFSS model* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/paper.pdf), SHA-256 `7a4b12bd2a7e8902c19fbda1fd0a9e73c063d8a7a0353667bceaf4194bffadef`, physical pp. 1--6, 12--13, 20--21, 27--33, 40--42) is an induction in rank with a massive deformation.  The source first fixes the common graph domain and massive index, then compares massive kernels.  The cluster-profile construction explicitly assumes lower-rank conclusions for proper blocks.  Lemma 6.2 gives a quantitative exclusion of intermediate scales only for vectors with the stated bounded norm and charge bounds.  Proposition 7.1 obtains massive tightness via annular localization and its two parameter regimes.  Do not omit the rank-induction hypothesis, gauge/rotation restrictions where present, or the massive-to-undeformed comparison.

## SU(2)-invariant Gibbs-state disintegration

*Spontaneous magnetization in the quantum Heisenberg ferromagnet* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf), SHA-256 `8c9083e5eb7a9d6f877ef0695ec48ccbebb02c53d06b6e4af2719e24a3fdf70b`, physical pp. 44--46) applies its loop/pinning estimates to a finite-volume, SU(2)-invariant Gibbs state.  The p.45 proof of Theorem 1.1 decomposes that state into irreducible total-spin sectors and conditions a chosen spin component on the total-spin label `J`.  Use this only with an actual finite-dimensional SU(2) representation, invariant state, and the supplied sector weights; a generic Gibbs state has no such disintegration.

## Product-projection localization

*Product-projection localization and the QAC0 parity lower bound* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/paper.pdf), SHA-256 `12393c9f997aa808d71792f8afbd0cd2e65cf2892725f621ef845cc87b61efcf`, physical pp. 5--7) uses counts made from commuting one-qubit complements and circuits in the stated product-state-reflection normal form.  Theorem 2 gives the uniform conjugated-product-projection estimate only for fixed depth and fixed `0<=s<t`, sufficiently large `N`.  Its Lemma 3 polynomial has exact integer roots and a Chebyshev factor: if `0<a<b` and `u>(a+b)/2`, then eventually `deg p<=Nu`, `W_N(p)<=exp(Nu)`, `p(0)=1`, and `|p(x)|<=exp(-Na)` on integer `1<=x<=ceil(Nb)`.  The global weighted-coefficient bound is essential when expanding a count polynomial.

## Regular trajectories and quantum parity filters

*Regular trajectories, pruning and quantum parity* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/paper.pdf), SHA-256 `de3f7a04ba13787664d79ef15d5fc8d0a97f068d36af9c06ecd9a6004c3f34d8`, physical pp. 6, 9--12) starts with sequences whose qubit count tends to infinity and a bounded number of analytic layers.  Lemma 2.2 converts an eventual assertion for *every sequence* of permitted auxiliary choices into a uniform eventual threshold for all choices at an index; the parameter tuple must stay fixed.

For an integer-spectrum count, Lemma 3.1 builds a zero filter under `0<q<L<1` and `r>(q+L)/2`; it has exact value one at zero, exponential error on integer counts through `mL`, and source-stated degree/norm budgets.  Lemma 3.2 instead uses `0<v<h<u<=1`, `s>0`, and `k>s+(u-h)/2` to form a globally nonnegative tail detector, avoiding cancellation outside the detected range.  Proposition 4.1 propagates a low-degree perturbation only along the paper's regular trajectory and only with its strict `k<K<1` degree/norm budgets.  The companion exact helper checks the finite polynomial algebra, not these asymptotic circuit conclusions.
