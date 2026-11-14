<!-- Card created by W15 after reading the complete repository PDF, including its cover; review pending. -->

# Suren Poghosyan and Daniel Ueltschi, “Abstract cluster expansion with applications to statistical mechanical systems”

- **Identity/version:** Journal of Mathematical Physics 50, 053509 (2009), DOI `10.1063/1.3124770`. Warwick WRAP repository metadata, DOI, and the article title page were checked. Reader PDF: `evidence/fulltexts/C15.pdf`, SHA-256 `49886a5c29117d7d6e0498f279d17b4424da3a0a3940c3f1eb121d202ad4797f`, 18 physical pages: repository cover p. 1 and the full 17-page article on pp. 2–18. W15 read all pages.
- **Identity boundary:** C15 is verified as “Abstract cluster expansion with applications to statistical mechanical systems,” DOI `10.1063/1.3124770`. The separate claimed C14 title “Abstract Polymer Models with Inhomogeneous Activities” and DOI `10.1063/1.3130968` remain unverified: the DOI did not resolve and the exact title-author search did not validate that citation. Do not merge C14 with C15, but do not describe C14 as a confirmed distinct work either. C15 does not fill the C01 full-text gap.

## Model and results

The paper develops a continuous/measurable abstract cluster expansion for a complex measure `μ`, symmetric complex-measurable pair potential `u`, and Mayer function `ζ(x,y)=e^{−u(x,y)}−1`. Assumption 1 is the stability condition: for every `n` and `|μ|^{⊗n}`-almost every tuple, `∏_{i<j}|1+ζ(x_i,x_j)|≤∏_i e^{b(x_i)}`, equivalently `∑_{i<j} Re u(x_i,x_j)≥−∑_i b(x_i)`. The real-part qualification matters for complex-valued potentials.

Assumption 2 (article §II, PDF physical p. 3 / printed p. 2) requires a nonnegative `a` such that, for `|μ|`-almost every `x`,
`∫ |ζ(x,y)| exp(a(y)+2b(y)) |μ|(dy) ≤ a(x)`.
The distinct alternative Assumption 2′ (physical p. 4 / printed p. 3) defines `\bar u(x,y)=u(x,y)` when `Re u(x,y)≠+∞`, and `\bar u(x,y)=1` when `Re u(x,y)=+∞`; it requires
`∫ |\bar u(x,y)| exp(a(y)+b(y)) |μ|(dy) ≤ a(x)`
for `|μ|`-almost every `x`. In both routes Assumption 1 is also required. These are not interchangeable without proving the corresponding hypothesis for the chosen model.

- **Theorem 2.1, cluster expansion (PDF physical p. 4 / printed article p. 3).** Under Assumptions 1 and 2, or Assumptions 1 and 2′, and the separate global condition `∫ exp(a(y)+2b(y)) |μ|(dy)<∞`, the partition function is the exponential of the connected-cluster series, which converges absolutely. The rooted estimate (2.9) is, for `|μ|`-almost every `x₁`, `Σ_{n≥2} n∫|μ|(dx₂)…∫|μ|(dxₙ)|φ(x₁,…,xₙ)| ≤ (e^{a(x₁)}−1)e^{2b(x₁)}`; under Assumptions 1 and 2′ the same bound has `e^{b(x₁)}` instead of `e^{2b(x₁)}`.
- **Theorems 2.2–2.3 (PDF physical p. 5 / printed article p. 4).** Theorem 2.2 gives normalized one- and two-point correlation identities under the same hypotheses as Theorem 2.1. Theorem 2.3 gives the displayed truncated-correlation estimate under Assumptions 1 and 2; the text then states the analogous bound under Assumptions 1 and 2′ with `|\bar u|` in place of `|ζ|` and `e^{b(·)}` in place of `e^{2b(·)}`. The extra assumptions for the classical-gas decay application occur later in §III and must not be folded into this theorem statement.
- **Proposition 6.1 and Section 7 (article §§VI–VII; PDF physical pp. 12–17).** The tree-graph estimates bound connected graph sums by tree sums under the paper's finite-stability conditions. The proof uses a Ruelle-type algebraic partition and a separate Penrose/BBF tree identity route, then induction and absolute-convergence estimates to prove the main theorems.

## Transfer boundary

This is an auxiliary cluster-expansion source for B051 methodology. Its hypotheses concern a complex measure on a measurable space, stable complex pair potentials, the exact weighted inequalities above, and global integrability. It provides no channel representation, deletion-run activity bounds, entropy-rate interchange, or optimizer-uniformity argument. It is not C01 and does not validate the unresolved C14 citation candidate or solve B051's higher-order/convergence question.

## Full-text coverage

See `evidence/W16/reading_coverage.json#C15`: physical pp. 1–18, covering the repository wrapper, all article sections, tree estimates, theorem proofs, applications, and references.
