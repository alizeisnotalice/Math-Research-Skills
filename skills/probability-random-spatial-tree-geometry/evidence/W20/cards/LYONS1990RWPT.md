# LYONS1990RWPT — random walks and percolation on trees

**Source:** Russell Lyons, “Random Walks and Percolation on Trees,” *The Annals of Probability* 18(3) (1990), 931–958, DOI 10.1214/aop/1176990730. Complete article read from the 29-page scanned PDF (SHA-256 `df29dc8ef0fcb7f2fc15a28a4cd74a56e4f29d9381419e8f0882f3a09ab4b234`). Physical PDF pp. 2–29 are the article (printed pp. 931–958); all article pages were visually inspected, with theorem/formula pages checked against the page images.

## Models and results

The paper develops the **branching number** \(\operatorname{br}(T)\) as a cutset growth parameter for rooted trees and connects it to unit flows, reversible random walk, adjacency-operator growth, and percolation. Proposition 2.1 gives a flow characterization of \(\operatorname{br}(T)\); Proposition 3.1 supplies the subperiodic/quasispherical comparison used to turn level growth into cutset estimates. Theorem 4.1 is the electrical criterion: a reversible walk on a tree is transient exactly when there is a unit flow from the root to infinity with finite energy. Corollary 4.2 is the associated Nash–Williams cutset bound.

For the canonical λ-biased walk (parent-edge weight λ, child-edge weight 1), Theorem 4.3 gives transience when \(\lambda<\operatorname{br}(T)\) and recurrence when \(\lambda>\operatorname{br}(T)\); the critical equality case is not decided by that dichotomy and can be either recurrent or transient. The paper also relates the tree's branching number to pointwise spectral growth and to percolation: Theorem 6.2 identifies the critical percolation parameter as \(p_c=1/\operatorname{br}(T)\), and Theorems 6.4–6.6 treat Galton–Watson, multitype, and random-conductance settings under their own hypotheses. These comparisons do not identify branching number with a generic exponential level-growth rate without the paper's tree assumptions.

## Proof dependencies and limits

The electrical criterion comes from the reversible-network correspondence and the finite-energy-flow criterion; Nash–Williams then gives a lower bound on effective resistance from disjoint cutsets. The biased-walk threshold applies this flow criterion to the level-dependent conductances associated with the specified parent/child bias. The percolation threshold is proved by comparing open cutset growth with \(\operatorname{br}(T)\), while the random-conductance extension additionally assumes the stated moment domination and almost-sure upper bound on edge conductances. Do not infer the critical equality case from the strict inequalities.

This is a foundational comparator for tree transience, electrical networks, and branching/percolation thresholds. It does not prove monotonicity of harmonic-measure dimension for a bias family, equivalence of two boundary measures, or the SIRSN fixed-origin route-maximum estimate.

## Complete-paper coverage

| Physical PDF pages | Content read and mechanism |
|---|---|
| 1 | JSTOR cover; not part of the article pagination. |
| 2–6 | Printed pp. 931–935: branching-number definitions, cutset/flow criteria, and subperiodicity/quasispherical estimates. |
| 7–17 | Printed pp. 936–946: reversible networks, finite-energy-flow transience criterion, Nash–Williams bound, and biased-walk threshold. |
| 18–21 | Printed pp. 947–950: spectral-radius/pointwise-growth results for periodic trees and related comparisons. |
| 22–29 | Printed pp. 951–958: percolation threshold, Galton–Watson and multitype cases, random conductances, boundary-dimension discussion, and references. |

**Visual checks:** title/author and theorem pages were rendered in the prior reading pass; the full scanned article was inspected page by page. Page mapping is physical PDF n to printed page n+929, for 2≤n≤29.
