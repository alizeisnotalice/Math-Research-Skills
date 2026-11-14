# C168 finite-candidate holdout guarantee

**Status:** self-contained derivation for an auxiliary finite-candidate score; independent review pending. It does not solve C168 or certify the global optimum.

## Formal objective and Gaussian normalization

The formal input defines, for fixed `n≥2`,

`I_n(f,g)=∫∫ f(x)g(y) sin⟨x,y⟩ exp(−(||x||²+||y||²)/2) dx dy`,

where `f,g:Rⁿ→{−1,1}` are measurable. If `G,H` are independent `N(0,I_n)` vectors, then their product density is `(2π)^(−n)exp(−(||x||²+||y||²)/2)`, hence

`I_n(f,g)=(2π)^n E[f(G)g(H)sin⟨G,H⟩]`.

This identity is exact and follows directly from the Gaussian density; it does not assert anything about which sign functions maximize the integral.

## Theorem (finite, pre-fixed candidate list)

Let `M≥1`. A training data sigma-field `𝒯` determines a measurable list `𝒞(𝒯)={(f_j,g_j):1≤j≤m}` with `m≤M`. Let the validation pairs `(G_i,H_i)`, `i=1,…,N`, be iid with law `γ_n⊗γ_n` and independent of `𝒯`. Define

`Z_{ij}=f_j(G_i)g_j(H_i)sin⟨G_i,H_i⟩`, `θ_j=E[Z_{ij}|𝒯]`, and `θ̂_j=N⁻¹Σ_i Z_{ij}`.

Then, for every `δ∈(0,1)`,

`P{ max_{j≤m}|θ̂_j−θ_j| > sqrt(2 log(2M/δ)/N) | 𝒯 } ≤ δ`.

Consequently, simultaneously for the finite candidate list,

`max_{j≤m}|Ĩ_j−I_j| ≤ (2π)^n sqrt(2 log(2M/δ)/N)`

with conditional and unconditional probability at least `1−δ`, where `I_j=(2π)^n θ_j` and `Ĩ_j=(2π)^n θ̂_j`.

## Proof

Condition on `𝒯`; the candidate list is now fixed and the validation sample remains iid. For each fixed `j`, `Z_{ij}∈[−1,1]`. Here is the needed width-2 Hoeffding-lemma bound explicitly. For the conditional law of a fixed score `Z=Z_{ij}`, let `φ(λ)=log E[e^{λZ}|𝒯]`. Then `φ(0)=0`, `φ'(0)=θ_j`, and `φ''(λ)=Var_λ(Z|𝒯)≤1`, since every exponentially tilted law is still supported on `[−1,1]`, whose variance is at most one. Taylor's integral formula, valid also for negative `λ`, yields

`φ(λ)−λθ_j = λ²∫₀¹(1−s)φ''(sλ)ds ≤ λ²/2`,

and therefore

`E[exp{λ(Z_{ij}−θ_j)}|𝒯] ≤ exp(λ²/2)`.

Independence across validation indices yields

`E[exp{λΣ_i(Z_{ij}−θ_j)}|𝒯] ≤ exp(Nλ²/2)`.

For `ε>0`, Markov's inequality and optimization at `λ=ε` give

`P(θ̂_j−θ_j≥ε|𝒯) ≤ inf_{λ>0} exp(−λNε+Nλ²/2)=exp(−Nε²/2)`.

Apply the same argument to `−Z_{ij}` and take a union bound over at most `M` candidates:

`P(max_j|θ̂_j−θ_j|≥ε|𝒯) ≤ 2M exp(−Nε²/2)`.

Setting `ε=sqrt(2 log(2M/δ)/N)` gives the displayed result. Multiplication by `(2π)^n` gives the integral-scale bound. Taking expectations over `𝒯` preserves the same probability bound.

The bounded-variable Hoeffding statement is Theorem 2.2.6 in P031 (printed p. 30; physical PDF p. 38); that book assigns the general bounded-variable proof to an exercise. The derivation above supplies the needed width-2 case from the log-mgf curvature bound, followed by Chernoff optimization; the theorem statement alone is not treated as a reproduced proof.

## Scope and non-claims

The candidate list may be chosen using an independent training sample, but it must not adapt to the validation pairs. The guarantee controls only the listed finite scores. It gives no uniform bound over all measurable sign partitions, no global optimality proof, and no candidate-approximation, discretization, truncation, or quadrature error bound. In particular it does not certify the optimal partition for `n=2`.

## Numerical sanity check

`C168_finite_candidate_holdout_check.json` records a Python calculation for `n=2`, `N=10000`, `M=100`, and `δ=0.05`. It checks that the chosen threshold makes the union-bound right side equal to `δ` up to floating-point roundoff and reports the rescaled integral error threshold. This is a numerical consistency check, not a proof of the theorem or of any optimization claim.
