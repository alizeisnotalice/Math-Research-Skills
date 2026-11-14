> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-020 — Topological States in the Kuramoto Model

## Source and reading evidence

- Timothy Ferguson, arXiv:1704.02294v1 (7 Apr 2017), published DOI 10.1137/17M112484X.
- Exact local source: ../pdfs/PGEL-020.pdf, 10 physical pages, SHA-256 a544832a2e3b8575fe0acbd798751b3e94fdc5051dc2681186e2f6625ed61425.
- Complete physical PDF pp. 1–10 read in order, including Appendix proofs, examples, and references. Full section coverage and rendered page hashes are in reading_coverage.json#sources.PGEL-020.
- Canonical full-read index was checked before reading; no accepted exact-title, arXiv work-key, or source-hash match was found. The full read is accepted as reading evidence; theorem-scope findings below remain pending re-review.

## Model and cycle coordinates

The paper begins with a weighted graph Kuramoto equation, then specializes counting and stability statements to zero-frequency gradient dynamics. Let B be the oriented incidence matrix, V=[v1 ... vc] an integer cycle-lattice basis, c=|E|-|V|+1, and Dγ=diag(γe) with nonzero edge weights. Standing assumptions include a simple graph in which each edge is omitted by some spanning tree (equivalently, no bridges) and edge branches Ie on which sin restricted to Ie is injective. The phases are considered modulo a common rotation.

For a frequency vector compatible with the incidence equation, ω∈im B (for a connected graph this is 1-perp), the Appendix parameterizes edge flows by cycle coordinates:
\[
L(\alpha)=D_\gamma^{-1}(B^+\omega+V\alpha),\qquad
W(\alpha)=\frac1{2\pi}V^\top\sin_I^{-1}L(\alpha),
\]
on the admissible polytope A where each inverse branch is defined. Keep the p. 3 normalization 1/(2π) distinct from the separate single-cycle convention on p. 6.

## What the cycle-space proof establishes

The Appendix proof of Theorem 1 (physical p. 9) gives an existence parameterization: for a compatible ω and fixed admissible branches, a fixed point orbit is recovered from an α satisfying W(α)∈Z^c, by solving
\[
B^\top\theta=\sin_I^{-1}L(\alpha)-2\pi K
\]
for the compatible integer edge vector K. The cycle-lattice condition is exactly the condition that such K exists; for a connected graph the recovered phase vector is unique modulo common rotation once α and K are fixed.

This does **not** make W injective. The printed Theorem 1 says fixed-point orbits and lattice points in W(A) are in one-to-one correspondence for arbitrary sine-injective branches; that uniqueness/counting claim is false under the printed hypotheses. A lattice point may have a nontrivial α-fiber, with distinct equilibrium orbits in that fiber. Retain the implicit existence parameterization and α-fiber; do not count equilibria from image lattice points without an injectivity gate or fiber multiplicity control.

### Exact mixed-branch counterexample to the unrestricted injectivity claim

Take C4 with unit positive weights, zero frequency, oriented cycle basis V=(1,1,1,1), and alternating branches I+ = (-π/2,π/2), I- = (π/2,3π/2). For α∈(-1,1), write a=arcsin α. The branchwise edge differences may be represented as (a,π-a,a,π-a), so
\[
W(\alpha)=\frac{2a+2(\pi-a)}{2\pi}=1
\]
for every α∈(-1,1). Both θ=(0,0,π,π) (a=0) and θ=(0,π/6,π,7π/6) (a=π/6) solve the exact equilibrium equation B sin(Bᵀθ)=0, have winding 1, and are not related by common rotation. The branches are sine-injective and all edge values are interior. Thus branchwise sine injectivity alone does not yield W injectivity, even after quotienting by phase rotation.

## A separately proved restricted certificate

The following restriction is a reader-derived safe method, not a repaired statement of the source's general Theorem 1. Assume a connected graph, compatible ω, all γe>0, and all branches are the principal open interval Ie=(-π/2,π/2). Let α,β∈A and put u=L(α), v=L(β). Since u-v=Dγ^{-1}V(α-β), the source normalization gives
\[
(\alpha-\beta)^\top(W(\alpha)-W(\beta))
=\frac1{2\pi}\sum_e\gamma_e(u_e-v_e)
(\arcsin u_e-\arcsin v_e)>0\quad(\alpha\ne\beta).
\]
The strict inequality follows from strict monotonicity of arcsin, γe>0, and full column rank of V. Hence W is injective on this restricted admissible set.

At an exact equilibrium with edge differences φe in these strict branches,
\[
DW(\alpha)=\frac1{2\pi}V^\top
\operatorname{diag}\!\left(\frac1{\gamma_e\cos\phi_e}\right)V
\]
is positive definite on cycle coordinates. Independently, the phase-energy Hessian is B diag(γe cosφe) Bᵀ. If the graph is connected and every γe cosφe>0, this Hessian is positive definite on 1-perp, so the negative Jacobian is strictly stable modulo common rotation (indeed locally exponentially stable for the smooth ODE). This certificate is for an exactly verified equilibrium; it does not find equilibria or establish global synchronization.

## Theorem-by-theorem scope and findings

1. **Theorem 1 (physical p. 3; proof p. 9).** The source's literal one-to-one claim for arbitrary branch choices is contradicted by the C4 example above. The Appendix existence condition W(α)∈Z^c with phase recovery modulo rotation remains useful when ω∈im B and the branch/cycle compatibility is retained. Any equilibrium count additionally needs injectivity or fiber analysis.

2. **Theorem 2 (physical p. 4; induction proof p. 9).** The source prints that, when sin(Ie)=[-1,1], the number of facets of A equals twice the edge count after smoothing all degree-two vertices. This unrestricted weighted statement is contradicted by the following legal example. Let K2,3 be represented as three length-two paths from vertex 0 to vertex 4, with weights 1,1,3 on the three paths. In the fundamental cycle basis,
   \[
   L(x,y)=(x,x,y,y,-(x+y)/3,-(x+y)/3).
   \]
   With all principal closed branches, A=[-1,1]^2: the third-path constraint |x+y|/3≤1 is strictly redundant because its maximum on the square is 2/3. Thus A has four facets. Smoothing the three degree-two vertices leaves three edges, so the literal formula predicts six facets. The graph is simple, connected, and bridgeless; no equal-weight condition is printed. Quarantine the unrestricted weighted facet statement and its proof; this example does not supply a corrected general formula.

3. **Theorem 3 (physical pp. 5–6; proof pp. 9–10).** For the stated edge-subdivision sequence, the printed limit for M^{-c} times the number of lattice points in W_M(A_M) is a geometric image-set asymptotic obtained by rescaling and Riemann sums. Keep it as an image-lattice count. The paper's interpretation as an asymptotic fixed-point count requires the Theorem 1 injectivity/fiber issue to be resolved; that interpretation is not certified for arbitrary branches. The deterministic statement is not a random-graph law.

4. **Theorem 4 (physical p. 6; proof p. 10).** The source reports that |W(A)| is maximized either by \(I_e=[-\pi/2,\pi/2]\) for γe>0 and \(I_e=[\pi/2,3\pi/2]\) for γe<0, or by the simultaneous complementary choice. Its proof uses |W(A)|=∫A|det DW|. This audit does not refute the volume-maximization inequality, but the printed proof invokes injectivity already refuted under the general standing assumptions. Therefore the unrestricted proof and conclusion are not certified here; no guessed correction is claimed. Separately, the adjacent prose extends automatic stability to closed sign-matched endpoints. Zero-cosine boundary points do not meet the strict weighted-Laplacian certificate: on C4 with unit weights, θ=(0,π/2,π,3π/2) is stationary with energy 4, while an integrable edge perturbation (3ε,-ε,-ε,-ε) changes the energy by -4 sin^3 ε<0 for small ε>0. This refutes treating that endpoint as a local energy minimum; it is not a counterexample to the volume-maximization statement. For ordinary local stability use connectedness and strict γe cosφe>0, or give a separate boundary proof.

5. **Theorem 5 (physical p. 6).** The single-cycle section locally defines \(\widehat W(\alpha)=\sum_{e\in E}\sin^{-1}_{I_e}(\alpha/\gamma_e)\), without the p. 3 factor 1/(2π). Its sufficient instability inequalities use this local unnormalized \(\widehat W\); when comparing with the p. 3 map, state \(\widehat W=2\pi W\) and rescale both sides. With I+=(0,π/2)∪(π,3π/2), I-=(π/2,π)∪(3π/2,2π), and α determined by the source's single-cycle L(α)=sin(Bᵀθ), the alternatives are
   \[
   \widehat W(\alpha)>\max_{e\in E}\left[
   \sin^{-1}_{I_-}(\alpha/\gamma_e)+
   \sum_{e'\ne e}\sin^{-1}_{I_+}(\alpha/\gamma_{e'})\right],\quad \alpha\ge0,
   \]
   or
   \[
   \widehat W(\alpha)<\min_{e\in E}\left[
   \sin^{-1}_{I_+}(\alpha/\gamma_e)+
   \sum_{e'\ne e}\sin^{-1}_{I_-}(\alpha/\gamma_{e'})\right],\quad \alpha\le0.
   \]
   The source proof uses a sufficient Hessian instability test when at least two edges have γe cosθe<0. These remain sufficient single-cycle tests under their branch assumptions.

6. **Theorem 6 (physical p. 7; proof derivative p. 10).** Retain the already-recorded source quarantine only: for two nontrivially intersecting cycles, common weight γ, and common principal or shifted branch, the printed bracket \(\pi^2/2+2J\) is equated to approximately 0.64368 although \(J=\int_0^1\arcsin(1-\beta)/\sqrt{1-\beta^2}\,d\beta\) itself is approximately 0.6436805 and the bracket is approximately 6.22216. Also p. 3's W has a factor 1/(2π) per coordinate while the p. 10 derivative display omits it, a (2π)^(-2) determinant-scale mismatch when c=2. Do not infer a corrected constant or theorem.

## Actual local mathematical checks

The original exact C6 and high-precision integral checks are retained in ../math/pgel_l03_b7_checks.py/json. The revision checks in ../math/pgel_l03_b7_revision_checks.py/json independently compute the mixed-branch C4 equilibrium residuals and constant W, the weighted K2,3 admissible square and redundant facet constraint, the C4 endpoint energy drop, and the connected positive C4 Hessian spectrum. These finite exact examples verify only their stated examples; the general strict-principal injectivity and stability statements above are supported by the displayed analytic argument.

Rendered pages p. 3, 5, 6, 7, 9, and 10 were visually checked for definitions, theorem conditions, branches, Appendix equations, and determinant scaling; all ten physical pages were rendered, and the complete-page reading log covers the whole document.

## Reuse limits

Keep the implicit compatible-frequency cycle-flow/winding existence parameterization with phase recovery and α-fibers. Use the independently proved positive-weight strict-principal injectivity and local-stability certificate only under its explicit gates. Quarantine arbitrary-branch W injectivity, unrestricted weighted Theorem 2 facet counts, unqualified fixed-point counting through image lattice points, and the unrestricted Theorem 4 proof; do not call Theorem 4 volume maximization false. The closed-endpoint stability extrapolation is invalid, while strict positive-cosine stability remains valid. Theorem 6 stays as already isolated. Nothing here proves a uniform ER statement, a signed-graph statement, or resolves C106/C107/C118.

## Review state

Full-text evidence is accepted, but source-level revisions remain pending R02 re-review. No mother ledger or skill has been changed.
