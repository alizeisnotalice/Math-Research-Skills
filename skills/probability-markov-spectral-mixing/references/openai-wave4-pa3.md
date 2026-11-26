# Wave 4 PA3: transfer-gap and finite-box references

## Exact mass asymptotics for the two-dimensional O(4) lattice model

Source SHA-256 `4eb3ab28f756532217d79b66690587de12f732cf71286ede8011f5397994a14c`, physical pp. 10--12, Proposition 2.3 and Lemmas 2.4--2.5.  For the reflection-positive O(4) Wilson plane law, let `r_*` be the top of the spectral support of a one-spin OS vector.  The reference records
\[
m(\beta)=-\log r_*=-\log\lim_{n\to\infty}\mathbb E[q^1_{(0,0)}q^1_{(n,0)}]^{1/n},
\]
and places the centered even sector below `r_*^2`.  On a finite cylinder, an odd bounded detector `F` has
\[
\omega(F(F\circ\vartheta^n))\ge \frac{\tau}{1+\tau}\tau^n,
\]
while its correlation is controlled by a sum of component correlations.  The method is the parity decomposition of the positive transfer kernel, followed by an Edwards--Sokal sign-cluster visibility comparison.

**Scope.** Scoped reference. It requires the named reflection-positive O(4) Gibbs/OS construction, positive transfer kernel, and finite-volume-to-cylinder limit.  It does not identify a gap for another spin model or supply the renormalization input used later in the source.

## Sharp mass bounds for the two-dimensional O(4) model

Source SHA-256 `e87f407df77777cadabcce10347533a68e7744be365ecd40c9602acc1129baac`, physical pp. 10--12, Lemma 2.1 and Proposition 2.2.  For normalized transfer eigenvalues, define the trace tail `s_n=\sum_{i\ge2}(\lambda_i/\lambda_1)^n` and the rectangular defect `p`.  When `p(n,w)\le1/4`, the source uses
\[
(\lambda_2/\lambda_1)^n\le2p(n,w),\qquad p(2n,w)\le4p(n,w)^2.
\]
With the exact rectangle identity and square defect
\[
\Delta_\beta(n)=4\log Z_\beta(n,n)-\log Z_\beta(2n,2n)
=2p(n,n)+q(2n,n),
\]
the hypothesis `\Delta_\beta(n)\le2^{-10}` gives `\Delta_\beta(2r)\le64\Delta_\beta(r)^2`, transfer-ratio control on circumferences `2^k n`, and the full local-observable gap lower bound `(\log2)/n`.

**Scope.** Scoped reference. It needs the stated compact positive trace-class row transfer operators, exact torus rectangle identities, reflection positivity, and the small initial square-box defect.  It is not a generic static-correlation-to-gap theorem.

## 固定来源

- 物理页 10, 11, 12。Proposition 2.3; Lemmas 2.4--2.5 SHA-256 `4eb3ab28f756532217d79b66690587de12f732cf71286ede8011f5397994a14c`。[Exact mass asymptotics for the two-dimensional O(4) lattice model](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/exact-mass-o4.pdf)
- 物理页 10, 11, 12。Lemma 2.1; Proposition 2.2 SHA-256 `e87f407df77777cadabcce10347533a68e7744be365ecd40c9602acc1129baac`。[Sharp mass bounds for the two-dimensional O(4) model](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf)
