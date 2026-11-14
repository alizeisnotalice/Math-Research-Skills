<!-- Card revision: W15; source originally fully read in the earlier W16 batch. -->
# David Ruelle (1967), “A Variational Formulation of Equilibrium Statistical Mechanics and the Gibbs Phase Rule”

- Source: *Communications in Mathematical Physics* 5, 324–329 (1967). Author PDF: https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B18%5D.pdf. Local PDF: `evidence/fulltexts/C04.pdf` (6 pages; SHA-256 `a9bbd41a367a4e9432675fde723d0320ee18f78e34b970e4f82cf495c782dcba`).
- Reading: all 6 PDF pages. This revision corrects the source ID from the prior misnamed `E01` card.
- Scope: lattice equilibrium statistical mechanics with at most one particle per site; comparison only, not a deletion-channel capacity characterization.

## Results and assumptions

The interaction is a translation-invariant family φ with absolute-summability norm (1.2),
\[
\|\phi\|=\sum_{k\ge1}\frac1{k!}\sum_{\substack{x_1,\ldots,x_{k-1}\in\mathbb Z^\nu\\\text{pairwise distinct and nonzero}}}
|\phi^{(k)}(0,x_1,\ldots,x_{k-1})|<\infty.
\]
The `1/k!` normalization and the restriction to pairwise-distinct nonzero tuples are part of the source definition. Theorem 1 (PDF pp. 1–2) gives the thermodynamic pressure limit and convex continuity; differentiability/unique tangent is restricted to the generic set (D). Theorem 2 (PDF p. 3) gives existence, affinity, and upper semicontinuity of mean entropy on translation-invariant states. Theorem 3 (PDF p. 3) states the variational identity
\[
P(\phi)=\sup_{\theta\in E\cap I}\{s(\theta)-\theta(A_\phi)\}.
\]
The proof of the variational property is on PDF pp. 3–5. Theorem 4 starts on PDF p. 5 and continues on p. 6; it asserts uniqueness of the maximizing equilibrium state and its extremality only when φ∈D. These qualifications are part of the result.

## Transfer limit

This is an entropy-minus-energy variational principle for a Gibbs model. It does not identify the deletion-channel information-rate functional with mean energy, establish a polymer representation, or justify exchanging a capacity supremum with a small-(d) expansion.
