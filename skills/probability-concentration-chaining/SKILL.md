---
name: probability-concentration-chaining
description: Apply and audit concentration inequalities, large-deviation bounds, empirical-process/chaining estimates, and anti-concentration results while preserving model assumptions and the distinction between upper tails and small-ball bounds.
---

# Concentration, large deviations, and chaining

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

**W03 independently reviewed release.** R02 accepted 29 complete paper reads (P001–P012, P015–P016, P018–P030, P034–P035) and one complete selected chapter from the fully acquired P031 book, totaling 30 distinct eligible sources. The final independent verdict and exact version binding are in [R02 review](evidence/review/review.json). Reader-ledger `pending` labels remain historical declarations; independent approval is recorded separately. P033 is a partially read course-notes paper and is excluded from the quota; P032 is an incomplete scan, and P013/P014 have no local PDF. These gaps are retained.

## Use this skill when

- choosing or auditing a tail bound for sums, functions of independent inputs, martingales, or random matrices;
- bounding a supremum over a finite or separable stochastic process using metric entropy or generic chaining;
- approximating an empirical-process supremum by a Gaussian supremum;
- controlling short-interval probabilities for a Gaussian supremum or translating approximation error into coverage error;
- deciding whether a large-deviation principle or moderate-deviation approximation is actually available from the read sources.

## Workflow

1. **Write the event and target scale.** Specify upper/lower/two-sided tail, supremum versus one variable, fixed-time versus time-uniform control, and whether the task needs an interval probability or a small-ball estimate.
2. **State the law and dependence.** Identify independent coordinates, iid empirical sampling, exchangeability, Markov dependence, or a filtration. Never replace one with another implicitly.
3. **Choose the theorem by its hypotheses.**
   - Independent self-adjoint matrix sums: P001 has matrix Chernoff/Hoeffding/Bernstein theorems with dimension factors.
   - Independent bounded scalar sums: P005 sharpens the one-sided Hoeffding proxy only for left-skewed intervals; use its valid Eq. (23) sum bound. Its later Eq. (28)–(33), (36) displays mis-scale `S_n` by `n` after defining `\bar M_n=M_n/√n`; preserve the source issue and do not cite those as sum-tail bounds.
   - Geometrically ergodic Markov/HMM paths: P006 requires the underlying chain's inverse-mixing bound and retains the expected-bias term in its empirical-law inequalities.
   - Weighted finite exchangeable samples: P007 assumes bounded coordinates and fixed weights; nonnegative weights have a sharper Hoeffding form, and the general Bernstein form retains the finite-population correction and a random finite-vector empirical variance (not `Var(X_1)`).
   - Sampling without replacement and permutation statistics: P008 uses a uniform random permutation, bounded coordinate family, and modified log-Sobolev argument. Its Theorem 2.2 statement is recorded, but a denominator mismatch in its printed p. 4 proof must be checked before claiming that exact proof chain is verified.
   - Product-measure/Talagrand bounds: P009 gives entropy-method proofs for convex distance, biased-cube L1–L2 variance, Gaussian T2, and independent empirical suprema; use each only with its own model and gradient/variance interface.
   - Functions of independent inputs: P003 requires a product input law and its centered coordinate replacement differences in the stated Orlicz norms.
   - Dependent product-space functions: P010 requires bounded coordinate metrics and valid Wasserstein matrices for the actual conditional-expectation kernels; alternatively its transport-information route requires conditional one-coordinate inequalities. Dependence alone does not supply these matrices.
   - Convex Gaussian lower deviations: P011 proves lower bounds on deviation probabilities when a convex Lipschitz function has variance at least a specified fraction of its squared Lipschitz constant. It is not an upper-tail inequality; preserve the median and variance-scale hypotheses.
   - Process suprema: P002 requires the stated `psi_alpha` or mixed-tail increment condition and the right semimetric(s); keep both gamma complexity and diameter terms.
   - Gaussian generic chaining: P015 Theorem 2.5 gives the `γ₂(T,d)` upper bound under its sub-Gaussian increment condition (1.1). For the two-sided Gaussian Theorem 5.1, use the canonical metric `d(s,t)=sqrt(E(X_s−X_t)²)` defined in Eq. (1.2), p. 3; §5 p. 29 refers to (1.1), so do not transfer the lower bound to an arbitrary larger tail-control metric. Its proof uses Sudakov minoration and Gaussian concentration with proof citations to other sources.
   - Time-uniform crossings: P004 requires a valid nonnegative supermartingale domination for the pair `(S,V)`, its filtration, `psi`, and initial normalizer `l_0`.
   - Empirical-process Gaussian approximation: P018 requires pointwise measurability, envelope moments, pre-Gaussianity, and control of the local entropy/envelope terms in its coupling bound.
   - Finite-candidate scoring for C168: for `G,H` independent standard Gaussian vectors, rewrite the formal integral as `(2π)^n E[f(G)g(H)sin⟨G,H⟩]`. If at most `M` measurable sign-pairs are fixed before an independent validation sample, the finite list has simultaneous two-sided error `(2π)^n sqrt(2 log(2M/δ)/N)` with probability at least `1−δ`. The proof and numerical check are in `evidence/W03/validation/C168_finite_candidate_holdout.md` and its JSON certificate. This scores only that finite list: it does not control all measurable partitions, global optimality, or discretization/approximation error.
   - Gaussian anti-concentration: P012 Theorem 2.1 requires a separable centered Gaussian process with unit marginal variance and finite supremum; it bounds a Levy concentration function, not an upper tail.
   - Gaussian maxima with unequal marginal variances: P021 Theorem 3 has a separate `log(σ̄/ε)` term; the equal-variance formula cannot be reused without common variances.
   - Maxima with common non-Gaussian marginals: P019 Theorem 1 is sharp over arbitrary copulas, while its improved Theorem 2 requires a convex copula diagonal.
   - One-dimensional log-concave laws: P024 gives density/variance, stochastic-order, and moment bounds; Theorem 3.8 compares `X−EX` with the centered uniform `U∼Unif[-1/(2M),1/(2M)]`, where `M=||f_X||∞`. Check whether the target is continuous or integer-valued and preserve the log-concavity and finite-moment assumptions.
   - Gaussian-polynomial small balls: P023 Theorem 1.2 is for a nonnegative degree-two polynomial of a standard Gaussian vector; require positive expectation (or exact degree two) to exclude the zero polynomial exception.
   - Gaussian order statistics/suprema: P020 states variance-sensitive interval-concentration bounds, but its upper-bound proof chain uses a false unrestricted negative-`s` sum-closure lemma (card P020, PDF p. 18). Do not use those upper bounds as established by this proof until the gap is independently repaired or bypassed; the arbitrary-variable lower bound in Remark 1 is separate.
   - Gaussian Hilbert-ball statistics: P022 compares norms and gives short bands for squared norms using covariance eigenvalue scales; it is not a coordinatewise-max theorem.
   - Large deviations: P016 is a survey reference for LDP set bounds and Laplace/entropy duality. Check the model-specific theorem and topology before using any Cramér, Sanov, Markov, small-noise, or hydrodynamic rate.
   - Model-specific moderate deviations: P026 treats a supercritical branching process in an iid random environment under its annealed law, no-zero-offspring and integrability assumptions; its uniformity over the starting generation is not a generic martingale MDP.
   - Stationary Gaussian high excursions: P029's Pickands theorem needs a continuous centered stationary Gaussian process, local covariance `1−|t|^α+o(|t|^α)`, and `r(t)<1` for every positive lag. It is an asymptotic as `u→∞`, not a finite-threshold tail inequality.
   - Gaussian fields with a maximum-variance manifold: P030's local Pickands and manifold asymptotics need the entropy, local correlation scaling, variance-loss regime and manifold assumptions in its card. Use Theorem 1 only for the unit-variance locally homogeneous full-dimensional setting; the nonconstant-variance strata use separate propositions, and several proof details are referred to earlier sources.
   - Martingale Cramér deviations: distinguish P025's conditional signed-moment Bernstein condition with a deterministic terminal bracket tolerance, P027's same type of moment condition with sub-Gaussian *probabilistic* terminal-bracket concentration, and P028's self-normalized statistic `S_n/sqrt([S]_n)` with conditional `(2+ρ)` moments plus concentration of `<S>_n`. P027 and P028 print Corollary 2.2 scales using `a_n min{ε_n,δ_n}` or `a_n min{γ_n,δ_n}`; the audited Rademacher counterexample shows those conditions do not imply the claimed MDP. Preserve the printed statements as source findings, and distinguish the cards' derived max-condition sufficient scale. For P028 Remark 2.1, A1 and A1′ have no global strength ordering: with common constants A1 is tighter at `0<x≤1`, while A1′ is tighter at `x≥1`. P028's main proof is in a separate supplement; P027 also sends the smoothing details for its tilted Berry–Esseen lemma to a supplement.
   - Martingale exponential crossing bounds: P034 Theorem 2.1 needs the per-step conditional exponential inequality and predictable `V` budget; Theorem 2.6 specifically assumes positive predictable `V_{i−1}`, while Corollary 2.7 assumes nonnegative predictable `U_{i−1}`. Preserve the theorem-specific controls and crossing event. Its applications are model-specific.
   - Two-sample DKW: P035 proves the sharp DKWM constant `C=2` for equal sample sizes `m=n≥458`; the unequal-size results are computations on stated finite ranges and are not a general theorem.
4. **Keep all error and complexity terms visible.** Record variance proxy, envelope moments, gamma functional or entropy, diameter, dimension/prefactor, confidence parameter, and constants. Do not hide terms behind an unexplained `O(1)` when they control transfer.
5. **Check the transfer interface.** Show how the target model produces independent summands, coordinate replacements, process increments, a Gaussian coupling, or a nonnegative supermartingale. The cited theorem does not supply that model-specific reduction.
6. **Separate coupling and anti-concentration.** A coupling controls distance between statistics on a joint space. A continuity/Kolmogorov conclusion also needs anti-concentration or another modulus-of-continuity bound for the Gaussian target. An upper-tail inequality does not control `P(|X-t|<=epsilon)`.
7. **Separate finite-sample inequalities from asymptotics.** P016 provides LDP definitions and a survey of rate functions, but it does not supply one general theorem for all models; the specific hypotheses, speed, topology, and proof source remain necessary. Do not infer an LDP from concentration inequalities or unread entries.
8. **Record source state.** Cite the exact theorem, PDF page, version, and assumptions from a full-text card. The current inventory marks all sources pending independent review.

## Current evidence and limitations

- P001: matrix tail inequalities and their Laplace/Lieb proof chain; full text read.
- P002: generic chaining moment/tail bounds, mixed-tail chaining, empirical-process and chaos applications; full text read.
- P003: entropy-method Hoeffding/Bernstein inequalities for functions of independent inputs; full text read; see its card for the Theorem 4.6 formula audit limitation.
- P004: sub-`psi` supermartingale condition and equivalent time-uniform line-crossing bounds; full text read.
- P005: improved Hoeffding MGF and valid sum-tail Eq. (23), with geometric proxy only on left-skewed intervals; full text read, publication metadata incomplete because the PDF journal fields are placeholders. Later displayed tails Eq. (28)–(33), (36) have a factor-`n²` sum/mean normalization inconsistency and are isolated in the card.
- P006: geometric-ergodic Markov/HMM concentration, DKW-type empirical law and uniform occupation Chernoff bounds; the Theorem 3 rare-cell mass term is `Σ_{ρ_y<1/n}ρ_y` with coefficient 1 (no `1/4`); full text read.
- P007: fixed-weight Hoeffding/Bernstein bounds for bounded exchangeable samples; Theorem 6 uses the random finite-vector empirical variance `N⁻¹Σ_i(X_i−\bar X)²`, not the marginal variance; full text read.
- P008: Bennett concentration for sampling without replacement and permutation Hoeffding statistics; full text read; a printed p. 4 proof-line denominator mismatch is flagged in its card, without declaring the theorem false.
- P009: entropy-method proofs of four Talagrand inequalities (convex distance, L1–L2 variance, Gaussian T2 and independent empirical supremum); full text read.
- P010: martingale concentration for dependent product-space functions via Wasserstein matrices or conditional transport-information bounds; full text read.
- P011: convex Gaussian lower-deviation bounds and norm applications; these are lower probabilities and require the variance/Lipschitz conditions; full text read.
- P012: anti-concentration for separable unit-variance Gaussian suprema and honest confidence-band results; full text read.
- P016: Varadhan's survey of LDP bounds, Laplace/entropy duality, and model-specific rate mechanisms; full text read.
- P026: uniform Cramér deviations and Berry–Esseen bounds for a supercritical branching process in an iid random environment under the annealed law; full text read.
- P029: Pickands' asymptotic high-excursion formula for continuous stationary Gaussian processes, proved by local blocks and a double-sum estimate; full text read.
- P030: Gaussian-field high-excursion asymptotics near a smooth maximum-variance manifold, separated into local-homogeneous, homogeneous-like, Talagrand, transition and general cases; full text read, with proof-outline/external-reference limitations recorded.
- P015: full 69-page author-hosted DVI conversion of Talagrand's generic-chaining paper read; Theorem 2.5 upper bound and Gaussian Theorem 5.1 two-sided characterization recorded. For Theorem 5.1 use the canonical metric from Eq. (1.2), not an arbitrary metric satisfying the general increment-tail display (1.1); the section-5 cross-reference is flagged. The conversion may differ from the final journal version, and lower-bound proof dependencies cited to external sources are flagged.
- P031: complete Chapter 2 of Vershynin's second-edition high-dimensional probability textbook read (physical PDF pp. 33–66), from a full 341-page book acquisition. Theorem 2.2.6 is stated on p. 38; its proof is assigned to an exercise. The PDF's personal-use-only notice is retained.
- P033: complete §2 (subsections 2.1–2.3, physical pp. 5–11) of Konarovskyi's complete available course notes read. This is not a published book; the non-everywhere-finite cumulant case in the Cramér lower-bound proof is cited externally.
- P034: full 22-page martingale exponential-inequality paper read; complete Theorem 2.6 and Corollary 2.7 hypotheses on physical PDF p. 7 and the Theorem 2.1 proof page 14 checked visually. In particular, `V_{i−1}` is positive in Theorem 2.6, while `U_{i−1}` is nonnegative in Corollary 2.7.
- P035: full 32-page two-sample DKW paper read; equal-sample theorem and proof/computation split checked. Unequal-size conclusions are limited to computed ranges.
- P018: non-asymptotic Gaussian approximation of empirical-process suprema, including local and series applications; full text read.
- P019: sharp maximum concentration bounds under arbitrary and diagonally convex copulas; full text read.
- P020: the stated variance-sensitive bounds for Gaussian order statistics and separable suprema were fully read. Its upper-bound proof chain is flagged: Lemma 7 (PDF p. 18) incorrectly asserts unrestricted closure of negative-`s`-concave functions under summation; Proposition 4 and the Theorem 1/2 upper-bound arguments are not certified as written. The theorem statements are not declared false; the lower bound in Remark 1 remains separate.
- P021: Gaussian maximum comparison, anti-concentration, and multiplier-bootstrap conditions; full text read.
- P022: Gaussian Hilbert-ball comparison and anti-concentration of squared norms; full text read.
- P023: small-ball anti-concentration for nonnegative degree-two Gaussian polynomials; full text read. Keep the positive-mean qualification and the exact-degree convention visible.
- P024: continuous and lattice anti-concentration/moment bounds for log-concave variables; full text read. Theorem 3.8's uniform comparator is centered, with support `[-1/(2M),1/(2M)]`.
- P025: two-sided Cramér tail expansions for martingales under conditional Bernstein moments and a deterministic bracket bound; full text read.
- P027: moderate deviations for martingales under conditional Bernstein moments and sub-Gaussian terminal-bracket concentration; full text read, with the tilted smoothing proof partly referred to a supplement. Its printed Corollary 2.2 `min` scale is contradicted by the checked counterexample in its card.
- P028: self-normalized martingale deviations under conditional `(2+ρ)` moments and bracket concentration; full article read, but its detailed main-theorem proof is in a separate supplement not included here. Its printed Corollary 2.2 `min` scale is contradicted by the checked counterexample; A1 versus A1′ has no global strength ordering.
- P032 remains an incomplete scanned local copy (printed pages end at 61 although the contents indicate material through p. 143), so it is not eligible for a selected-book reading unit. P013/P014 remain download gaps. The current candidate quota is 29 full-text papers plus P031's complete selected textbook chapter, all pending review; P033's notes section is additional evidence but does not count as a published-book unit.
- See [the method map](references/method.md) and [source inventory](references/sources.md). The proof obligations in the problem mappings remain open.
