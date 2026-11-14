# AUX-MEHRDAD-SEN-ZHU-2015 — High-bias speed comparison across progeny laws

**Authors/citation:** Behzad Mehrdad, Sanchayan Sen, Lingjiong Zhu; *Annales de l’Institut Henri Poincaré, Probabilités et Statistiques* 51(1), 304–318 (2015). **Read version:** complete author manuscript arXiv:1212.3004v4, 2 March 2015, physical PDF pp. 1–17. SHA-256 f47954c8ff8b555eeeda35ae9542eb5ee856d7d5b6ea82c8258993411e08f388. D05 verified identity and extent; W20 read all pages. Independent review pending.

## Model and exact claim

The offspring laws P1 and P2 are supported on positive integers (so there are no leaves); P1 stochastically dominates P2 and P1 ≠ P2. In the paper’s convention, at a vertex with k children the parent is chosen with probability 1/(1+βk), and each child with probability β/(1+βk); root children are equiprobable. Thus β is childward bias, the inverse direction of the parent-weight λ convention used in the W20 harmonic-dimension dossier. The walk starts at the root, and speed is the deterministic a.s. limit v(β,P).

**Theorem 1 (physical p. 2; parameters continued on p. 3).** For each δ>0 there is a threshold β0=max{β1, 23/4+δ}, with β1 depending on P1,P2,δ as in (1.3), such that β>β0 implies the strict comparison v(β,P1)>v(β,P2). Formula (1.3) uses independent Z1∼P1,Z2∼P2 and an ordered coupling (Z′1,Z′2) with marginals P1,P2 and Z′1≥Z′2 a.s. The first term in β1 is proportional to E[(1/Z1−1/Z2)1{Z1<Z2}]/E[1/Z′2−1/Z′1]; the second is E[Z′2(1/Z′2−1/Z′1)]/E[1/Z′2−1/Z′1]+1. The proportionality constant cδ is universal for fixed δ. The rendered p. 2 confirms both the strict dominance condition and the 23/4+δ cutoff. This is a sufficiently-high-bias comparison of speeds across offspring laws, not monotonicity of harmonic-measure dimension and not a claim for every β.

**Theorem 4 (physical p. 3; rendered):** if for some integer ℓ>1 there is a coupling of two ℓ-tuples, each tuple internally iid with law P1 or P2 respectively, such that the minimum of the P1 tuple is at least the maximum of the P2 tuple almost surely, then for every δ>0, `v(β,P1) ≥ v(β,P2)` whenever `β > max{K·β1^(1/ℓ), 23/4+δ}`, where `K=(27/4)·3^(5/3)` and β1 is the Theorem 1 quantity. This conclusion is non-strict. Corollary 5 gives eventual strict comparison for generation-k offspring laws under its exponential-moment and growth assumptions. Neither result changes the target quantity from speed to boundary dimension.

## Proof chain checked

Section 2 constructs the two tree walks and a one-dimensional simple biased walk using common uniforms. At newly exposed sites the offspring counts use an ordered coupling; mismatched revisits use independent marginals so each marginal tree still has the correct GW law. A regeneration time of the auxiliary walk that is simultaneously a maximum to the past and a minimum to the future is a super-regeneration time for both tree walks. Under the law conditioned that zero is a negative regeneration time, regeneration increments are iid, and the expected regeneration-time denominators for the two speeds agree. Therefore speed ordering reduces to ordering expected regeneration heights.

For Theorem 1, split according to the number k of backward steps before the first positive regeneration. When k=1, an explicit five-step event gives a positive expected height difference. For k≥2, the path-height loss is at most 2(k−1); the proof bounds the chance of a negative difference by forcing one of the offspring mismatches in the coupling, then sums with the geometric tail bound for k and the regeneration-time bound τ1≤3k+2. The two alternative estimates (3.8) and (3.19) yield the two candidate controls in (1.3); choosing β above β0 makes the positive one-backstep contribution dominate the entire multiple-backstep loss. Theorem 4 reuses the coupling after ℓ ordered exposures, reducing the adverse contribution from early mismatches.

## W20 boundary

This is useful only as a neighboring speed/progeny comparison. It uses β childward bias on leafless GW trees; translate β=1/λ only when the W20 parent-weight convention and all hypotheses match. Speed ordering does not imply ordering or differentiability of harmonic-measure dimension d(λ). It does not settle B076.

**Coverage:** entire 17-page PDF read, including Sections 1–3, acknowledgments and references. Page-by-page section coverage is in evidence/W20/reading_coverage.json.
