# AUX-LPP-TREE-OPEN-1997 — Unsolved Problems Concerning Random Walks on Trees

**Authors:** Russell Lyons, Robin Pemantle, Yuval Peres. Independently authored contribution in the edited volume *Classical and Modern Branching Processes* (1997), printed pp. 223–238. **Read source:** complete 16-page updated author-hosted contribution manuscript, version 25 Oct. 2025, physical PDF pp. 1–16, SHA-256 `c0f8a5ad83d1cac171acd4dff892da72ab15bf270789cf5e63fd1b2f2cd647c0`. The complete containing volume was not acquired (`full_book_acquired=false`); this is a complete independently authored contribution, counted as one paper/full-text read rather than as a book-selected chapter. Review pending.

## Model and exact open question

The chapter uses the same rooted-tree convention as LPP1996: a nonroot vertex with `k` children steps to its parent with probability `λ/(k+λ)`, and to each child with probability `1/(k+λ)`. The relevant GW setting is nondegenerate, supercritical with finite offspring mean `m>1`, and for much of the discussion `p₀=0`. The boundary metric is `e^(−n)` for rays sharing `n` initial edges; the walk's limit-ray law is harmonic measure.

After defining `d(λ,T)=dim_H HARM_λ(T)`, **Question 3.4 (printed p. 231; physical PDF p. 9)** asks: for `0≤λ<m`, is `d(λ,T)` nondecreasing for GW `T`, and is it strictly increasing? The chapter does not answer this. Repeated filtering shows nonmonotonicity on some general trees, which is not a counterexample for GW trees.

## Examples and conductance recursion

On the Fibonacci tree (a type-1 vertex has one type-2 child; a type-2 vertex has one type-1 and one type-2 child), the escape probabilities satisfy the displayed two-type conductance recursion. The harmonic measure is a two-state Markov measure, so its dimension is its entropy rate. The chapter computes a formula that is monotone for `0≤λ<(1+√5)/2` on this one deterministic tree; this special case does not imply the GW assertion.

Section 4 switches to simple random walk on a no-leaf GW tree. If `C(T)` is unit-edge effective conductance to infinity and `γ(T)=C(T)/(1+C(T))`, then

`γ(T)=sum_{|x|=1} γ(T(x)) / (1+sum_{|x|=1} γ(T(x)))`.

For offspring pgf `f(s)=sum_k p_k s^k`, the cdf satisfies `F_γ(s)=sum_k p_k F_γ^{*k}(s/(1−s))`, `0<s<1`. **Theorem 4.1** says this distributional equation has exactly the physical solution and the Heaviside solution; iteration from any other cdf with endpoint values `F(0)=0,F(1)=1` converges weakly to the physical law. The absolute continuity of this conductance distribution is left as Question 4.1. This is a simple-walk recursion, not the missing λ-derivative comparison for B076.

## Scope for W20

This is the direct source-record for the B076 question and a useful conductance recursion baseline. It supplies neither a proof nor a counterexample for nondegenerate GW offspring laws. The containing volume was not acquired; the complete contribution counts as one paper/full-text reading unit, not as a whole-book or selected-chapter unit. Full coverage is in `evidence/W20/reading_coverage.json`.

**Rendered check:** original physical p. 9, Question 3.4 and surrounding boundary/dimension statements.
