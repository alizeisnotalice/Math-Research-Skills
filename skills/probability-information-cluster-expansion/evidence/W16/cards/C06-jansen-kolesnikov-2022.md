<!-- Reader: W15; full paper read in this batch. The D01 handoff hash matches this local W16 copy. -->
# Sabine Jansen and Leonid Kolesnikov (2022), “Cluster Expansions: Necessary and Sufficient Convergence Conditions”

- Source: *Journal of Statistical Physics* 189, article 33 (2022), DOI [10.1007/s10955-022-02992-6](https://doi.org/10.1007/s10955-022-02992-6); arXiv:2112.13134v3. Local PDF: `evidence/fulltexts/C06.pdf` (49 pages; SHA-256 `ec19cbc3218cce7adb44075b13a709741d034929f15a4e99c99f84f1a1587df8`). The D01 handoff lists the same source/hash at `downloads/D01/papers/W16-C06_Cluster-Expansions-Necessary-and-Sufficient-Convergence-Cond.pdf`.
- Reader: W15; full PDF pp. 1–49.
- Scope: activity expansions of correlation functions for Gibbs point processes and specified abstract-polymer/hard-core models; not deletion-channel capacity.

## Main criteria

In Section 2.1, the reference is a σ-finite measure λ on a measurable space X; the pair potential is a measurable symmetric map `v:X×X→R∪{∞}`. Define the Mayer function `f=e^(−v)−1`, the multi-rooted activity expansions ρ_n, and the sign-flipped Kirkwood–Salsburg operator K̃_s^z determined by a root-selection rule s (Eq. (2.4)). Theorem 2.1 (PDF pp. 6–7) states: for nonnegative activity z, a measurable symmetric family of nonnegative functions ξ_n satisfying the exact pointwise inequality (2.5),

`z(x₁)·1_{n=1} + (K̃_s^z ξ)_n(x₁,…,xₙ) ≤ ξ_n(x₁,…,xₙ)`

for every n≥1 and every tuple, is sufficient for absolute convergence of all ρ_n at those arguments, with the corresponding absolute-sum bound by ξ_n. If the pair potential is nonnegative (repulsive), absolute convergence also implies existence of such a family, so the condition is necessary as well. For stable potentials with negative parts, the theorem does not state necessity.

Corollaries 2.2–2.3 (PDF pp. 7–8) recover Kotecký–Preiss-type and Fernández–Procacci-type sufficient tests with stability/local-stability and pointwise activity inequalities. Proposition 2.4 (PDF pp. 9–11) gives a stronger sufficient criterion for hard-core abstract polymers. Theorem 2.7 (PDF pp. 13–15) gives a necessary-and-sufficient characterization for this paper’s subset-polymer activity expansions; that result is model-specific. Proofs use root removal in multi-rooted graphs, forest/graph identities, and recursive Kirkwood–Salsburg inequalities (PDF pp. 17–25); concrete hard-core applications occupy Section 4 (PDF pp. 26–42).

## Transfer limit

The necessary-and-sufficient statement is restricted to the nonnegative pair-potential model and its defined correlation/activity series. No relation between those series and the optimized deletion-channel information rate has been proved. A channel application would need an explicit representation, all pointwise inequalities, and uniform control allowing the block-length, entropy-rate, and input-supremum limits.
