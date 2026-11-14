# LPP1996BIASED — Biased random walks on Galton–Watson trees

**Authors/year:** Russell Lyons, Robin Pemantle, Yuval Peres (1996), *Probability Theory and Related Fields* 106(2), 249–264. **Read source:** complete author manuscript, version 22 May 1996, physical PDF pp. 1–19; SHA-256 `c233e9139b1baff7e46ccbf4ffd8090aedbf4ce868fb769507088bc9b31325d5`. D05 verified acquisition/identity; W20 read the full text. Review pending.

## Model and conventions

The offspring law has mean `m=f′(1)>1`; the tree is conditioned on nonextinction, and the standing assumption is that no `p_k=1`. At a nonroot vertex with `k` children, the parent is chosen with probability `λ/(k+λ)`, each child with probability `1/(k+λ)`; at the root, children are equiprobable. Thus `λ` is parent weight (“toward-root” bias). The boundary metric assigns distance `e^(−n)` to rays with `n` common edges. Harmonic measure is the ray law of the transient walk after loop erasure.

## Exact results and proof dependencies

- **Theorem 3.1 (physical pp. 5–9):** for `1<λ<m`, almost every surviving GW tree has an a.s. constant positive speed. A quantitative lower bound is `(1−λ⁻¹)^3/[12(1−q_λ)^2]`, where `q_λ` is the least nonnegative solution of `f(1−λ⁻¹(1−q_λ))=q_λ`. The proof first bounds `G(x,x) ≤ (d(x)+λ)G(ρ,ρ)/(λ−1)` (Proposition 2.1), combines return probabilities and degree drift to obtain linear expected range (Proposition 2.2), then uses fresh epochs and regeneration slabs. Slabs are iid after conditioning on survival; their gaps have finite mean, so the renewal-reward ratio gives speed.
- **Theorem 4.1 (pp. 9–11):** if `p₀>0`, for `0≤λ<1` speed exists and is positive iff `f′(q)<λ<1`, and is zero for `0≤λ≤f′(q)`. The proof decomposes the surviving tree into a no-leaf backbone and finite bushes. A bush return-time expectation is `2/(1−f′(q)/λ)` when `λ>f′(q)`, infinite otherwise; finite/infinite mean excursion time determines positive/zero speed.
- **Theorem 5.1 (pp. 12–13):** for `0≤λ<m`, conditional on nonextinction, `dim HARM^λ_T<log m` a.s.; for `0≤λ₁<λ₂<m`, the two harmonic measures are a.s. mutually singular. Allow `λ=0` only when `p₀=0`. The proof reduces the leaf case to the backbone. For `p₀=0`, regeneration slabs generate a stationary chain of forward trees; a tower over exit epochs gives a finite stationary measure for the HARM chain. Its occupation measure is dominated by the sum of forward-subtree indicators, hence is absolutely continuous w.r.t. GW. The dimension-drop theorem of LPP (1995, Thm. 7.1) then applies once HARM is shown not to equal the limit-uniform measure. For distinct biases, equal harmonic measures would force the child-conductance ratios `γ_{λ₁}(T(x))/γ_{λ₂}(T(x))` to be constant across iid child subtrees, which implies a degenerate offspring law, contradicting the standing assumption.
- **Corollary 5.3 (pp. 14–16):** with `p₀=0`, most walk mass can be confined to a subtree whose exponential growth rate is the harmonic-measure dimension. The proof combines the speed limit, the harmonic-measure Hölder exponent, GW neighborhood-growth bounds, and Egorov uniformization.
- **Section 6 (pp. 16–18):** the authors explicitly say their methods do not analyze dependence of speed or dimension on `λ`. Question 2 asks for smoothness of both functions. This paper therefore does **not** prove monotonicity of harmonic-measure dimension.

## Use for W20 dossiers

For **B076**, this is an exact-model baseline: it gives fixed-`λ` dimension drop and singularity, not an ordering of `d(λ)`. The updated LPP chapter (AUX-LPP-TREE-OPEN-1997, Question 3.4) states the monotonicity problem directly. For **C139**, use the root-parent convention and speed regimes only after matching the dossier's bias direction. Neither speed positivity nor mutual singularity implies dimension monotonicity.

**Rendered check:** original physical PDF p. 12, including Theorem 5.1 and Lemma 5.2; section coverage is in `evidence/W20/reading_coverage.json`.
