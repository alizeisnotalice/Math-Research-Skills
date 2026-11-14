# AUX-BOWDITCH-TOKUSHIGE-2020 — Differentiability of the speed of biased random walks on Galton–Watson trees

**Authors:** Adam Bowditch, Yuki Tokushige; arXiv:1906.07913v2, title page 4 May 2020. **Read source:** complete author manuscript, physical PDF pp. 1–33, SHA-256 `c3b303079a2f4acfca3b3460f04bce181f338febbd5b411282fabb89e27deb51`. Review pending.

## Theorem and hypotheses

A supercritical GW tree has offspring pgf `f`, mean `μ>1`, extinction probability `q`, and `λ_c=f′(q)`. The walk is parent-weight `λ`, under the conditioned-tree annealed law; the surviving tree decomposes into a no-leaf backbone plus finite subcritical traps. Under an exponential offspring moment `sum_{k≥1} p_k β^k < ∞` for some `β>1`, **Theorem 1.1 (physical p. 3)** says the speed `υ_λ` is differentiable for `λ∈(√λ_c,μ)` and `υ′_λ=E_λ[XY]`, where `(X,Y)` is a centered two-dimensional Gaussian limit: `X` is scaled centered displacement and `Y` the scaled score of the likelihood ratio. The derivative is for **speed**, not harmonic-measure dimension. The authors expect extension to `(λ_c,μ)`, but their proof requires second moments of regeneration times.

## Proof dependencies

1. **Regeneration and root conditioning (§2, pp. 4–6).** Level-regeneration blocks are iid. The first block can have poor moments because the walk may make many root excursions, so work under `Pᴺᴮ_λ`, conditioning on no return to the added parent; after the first block, the law matches the ordinary inter-regeneration law. Proposition 2.5 supplies uniform block-time moments on compact bias intervals.
2. **Finite-difference approximation (Proposition 3.1, pp. 6–9).** Approximate speed differences using `n`-step displacements under `Pᴺᴮ_{λ+h}` and `Pᴺᴮ_λ`, with `h→0`, `n→∞`, `h²n→1`. Renewal-reward formulas and a bound `E max_{i≤n}(τ_{i+1}−τ_i)=O(n^κ)`, `κ<1/2`, make the end-block error `o(√n)`.
3. **Discrete Girsanov expansion (§3.1, physical pp. 10–15).** For one step, expand `log(A_{λ+h}/A_λ)=hB_λ+(h²/2)C_λ+(h³/6)D_{λ+sh}`. Summing gives likelihood ratio `exp(hP_n−h²Q_n+R_{n,h})`. The local score `B_λ` has conditional mean zero by differentiating row-sum one; its quadratic term is normalized by the corresponding second derivative. Regeneration-block CLT plus Proposition 3.4 gives joint Gaussian convergence of displacement and score, with covariance matrix in (3.20). The second-order term converges to half the variance of `Y`, and the remainder vanishes for `h≈n^−1/2`.
4. **Removing nonbacktracking conditioning (§3.1–3.2).** Lemma 3.3 controls the escape-indicator discrepancy using Hölder, the centered-displacement second moment, bounded likelihood ratios in L4, and continuity of escape probability (Proposition 2.9). Uniform integrability permits passage to the exponential tilt; Gaussian integration by parts yields `E[X exp(Y−Var(Y)/2)]=E[XY]`.
5. **Moment engine (§§4–6, pp. 16–31).** For the no-leaf backbone, use Rayleigh monotonicity and a Girsanov comparison to obtain uniform regeneration moments. Subcritical trap generation sizes obey `E W_n^r≤C_r λ_c^n` and joint-product bounds under the exponential offspring moment (Lemmas 5.1–5.2). A geometric-return estimate inside each trap and excursion-count bounds along the backbone give Proposition 2.5 for the full tree.

The interval restriction matters: `λ` must be above `√λ_c` for the required `2+ε` block moments. This is not a general differentiability theorem for every transient `λ`.

## Use for B076

This is a methodological comparator for parameter perturbation: it shows a pathwise likelihood score, joint CLT, uniform regeneration moments and a Gaussian response formula can differentiate `υ_λ`. It has no formula for `d(λ)=dim HARM_λ`, no invariant boundary-dimension derivative, and no monotonicity consequence for B076. A new argument would have to control how the harmonic-flow stationary law itself changes with `λ`.

**Rendered checks:** original pp. 3 (Theorem 1.1), 10 (Girsanov Taylor expansion and score), 13–15 (joint covariance and derivative limit), and 28 (trap-generation moment sum). Full read coverage: `evidence/W20/reading_coverage.json`.
