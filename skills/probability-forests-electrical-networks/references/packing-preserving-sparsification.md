# Preserving spanning-tree packing during cut sparsification

OpenAI, *The strong thin tree conjecture*, local archived manuscript SHA-256 a2b847ce72f66109dee2db00ea456bad74c13889b93bc7666e5ad9abefc23da4. Proposition 6.2, PDF p. 12, provides the source interface. The following iteration uses that interface as a hypothesis. [Pinned manuscript](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf)

## Check the two invariants

Take a finite loopless undirected multigraph H with at least two vertices and r explicitly packed edge-disjoint spanning trees. Count parallel edges by their individual indices. For a certificate by partition inequalities, check the number of crossing edges against r(k−1) for every partition into k nonempty blocks.

The shortcut matrix X must dominate L_H and satisfy 1_S^T X 1_S ≤ 3|δ_H(S)| on all proper nonempty cuts. Retain a packing in the low-leverage edges b_e^T X^−1 b_e ≤ 4r^−1/2, using the reduced coordinates for the Laplacian and cut tests as in the manuscript. The stacked vectors use a normalized incidence block and a packing block. Their cross covariance need not be zero. Cauchy–Schwarz gives the bound by twice the block diagonal if both diagonal blocks are bounded by I. A single selected subgraph must meet both the cut upper bound and the packing lower bound.

## Iterate only a certified step

Write u=r^−1/16, epsilon=6r^−1/2 and tau=2 sqrt(epsilon)+epsilon. Above the source cutoff, Proposition 6.2 supplies a subgraph with
\[
r'=\lfloor (1-4u)r/2\rfloor,\qquad
|\delta_{H'}(S)|\le (1/2+3\tau)|\delta_H(S)|.
\]
For the normalized cut size |δ_H(S)|/r the multiplier is at most 1+15u, using the source bounds 5/16 ≤ r'/r ≤ 1/2. If r_j is the final packing count, the earlier counts satisfy r_i≥2^(j−i)r_j. Hence the logarithm of the accumulated multiplier is at most 15 r_j^−1/16 times the geometric sum of 2^−k/16 for k≥1. The terminal packing count stays positive and bounded when the iteration first drops below a fixed sufficiently large threshold. Choose a tree from the terminal packing.

The source step includes a shortcut construction, a packing representation, and a partition argument. To claim these for a different model, supply each of those pieces separately. An exact finite test of the iteration or of a tree packing does not establish the source cutoff, an efficient construction, or transport to directed cuts or an unrelated Laplacian model.
