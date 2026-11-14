# Negative examples (W03 interim)

## Dependence mismatch and anti-concentration mismatch

**Unsafe claim:** “The summands are exchangeable, so Tropp's independent matrix Bernstein inequality applies; its upper-tail estimate also proves the maximum is not concentrated in a short interval.”

**Why this fails:** P001 Theorem 1.4 assumes independent summands and gives an upper tail for a maximum eigenvalue. Exchangeability does not supply independence, and an upper-tail inequality does not bound `P(|Y-t|<=epsilon)`.

**Repair:** Find a theorem matching the dependence and matrix hypotheses, and prove any reduction explicitly. For short intervals, use a separately verified anti-concentration result. P012 Theorem 2.1 applies only to a separable centered Gaussian process with unit marginal variances and finite supremum; it cannot be applied directly to an arbitrary dependent or non-Gaussian maximum.

## Coupling without anti-concentration

**Unsafe claim:** “The empirical supremum is close to a Gaussian supremum, therefore their CDFs are uniformly close.”

**Why this fails:** P018 gives a coupling error for the statistics, but a small perturbation can still change a CDF substantially where the Gaussian statistic places significant mass in a short interval.

**Repair:** Verify a modulus/anti-concentration bound for the Gaussian target (for example P012 under its unit-variance separable Gaussian assumptions), then combine that bound with the coupling error. Keep the coupling and concentration-function terms separate.

## Dropping the copula or spectral assumptions

**Unsafe claim:** “The sharp copula maximum bound automatically improves for any dependence,” or “the Gaussian Hilbert-ball anti-concentration bound depends only on the largest covariance eigenvalue.”

**Why this fails:** P019's improved theorem requires a convex copula diagonal; its arbitrary-copula extrema can scale linearly in dimension. P022's scale also depends on a second eigenvalue/eigenvalue tail; a rank-one example has short squared-norm bands of order `√ε`.

**Repair:** Verify the diagonal-convex condition before using P019 Theorem 2. For P022, compute the stated `κ(Σ)` and keep any infinite/degenerate scale visible; distinguish squared-norm bands from radius bands.

## Turning concentration tails into an LDP

**Unsafe claim:** “A Chernoff or Gaussian upper-tail inequality proves the proposed large-deviation principle and rate function.”

**Why this fails:** An LDP needs both closed-set upper and open-set lower bounds at a specified speed and topology. P016 is a survey and its different model classes use different rate functions and proof mechanisms.

**Repair:** Verify both LDP bounds, the rate function's lower semicontinuity/goodness when needed, the correct model assumptions and speed. Use a matching primary LDP theorem; a one-event tail bound alone is insufficient.

## Summing negative-s-concave functions

**Unsafe claim:** “Each conditional term in an order-statistic density is `s`-concave, so the sum is `s`-concave for `s<0`; apply P020 Theorem 1's upper bound.”

**Why this fails:** P020 Lemma 7 (PDF p. 18) asserts this unrestricted sum closure, but for `s=−1` the functions `f_1(x)=exp(−(x−3)^2)` and `f_2(x)=exp(−(x+3)^2)` are individually `−1`-concave while their sum fails the midpoint inequality: `2exp(−9)<1+exp(−36)`. Proposition 4 uses Lemma 7 to obtain `s`-concavity for the order-statistic law and its uniform smoothing (PDF pp. 18–19); Proposition 5 and the Theorem 1 upper-bound proof then rely on this. Theorem 2's upper-bound proof passes through Theorem 1.

**Repair:** Do not use P020's upper-bound chain as established until an independent proof repairs or bypasses this closure step. This counterexample refutes Lemma 7's stated generality, not the main theorem statements. The lower-bound assertion in Remark 1 is separate.

## Treating a printed metric-space constant as settled

**Unsafe claim:** “P003 Theorem 4.6 follows from Theorem 3.2 with exactly the displayed Lipschitz and `ψ₁`-diameter factors, so its constants can be plugged in directly.”

**Why this fails:** The PDF p. 8 display uses `Δ₁=||d(X,X′)||_(ψ₁)` and denominator `4eL²ΣΔ₁²+2et maxΔ₁`; direct substitution of the p. 3 Theorem 3.2 expression appears to give `4e²L²ΣΔ₁²+2eLt maxΔ₁`. The paper's stated implication and its printed formula do not match that direct derivation.

**Repair:** Use only P003 Theorems 3.1–3.3 as transcribed in the card unless you independently resolve the P004.6 discrepancy against its proof or a corrected source. Keep the source's statement distinct from a derived estimate.

## Confusing predictable and realized brackets

**Unsafe claim:** “A theorem for `S_n/sqrt([S]_n)` applies as soon as the predictable bracket `<S>_n` is close to its target,” or “a theorem normalized by `sqrt(<S>_n)` is automatically self-normalized.”

**Why this fails:** P025 and P027 use the predictable quadratic characteristic in the normalization/interface; P025 assumes a deterministic terminal-bracket tolerance, while P027 assumes a probabilistic sub-Gaussian bracket-deviation bound. P028 uses the realized square bracket `[S]_n` in its statistic and separately controls `<S>_n` while requiring conditional `(2+ρ)` moments. These are different denominators and different assumptions.

**Repair:** Write both brackets explicitly, identify which one is observed in the target statistic, verify the exact theorem's conditional moment and bracket hypotheses, and preserve its range. P028's main proof is in a separate supplement and should not be described as reproduced in the article.

## Promoting Gaussian extreme-value asymptotics to finite-threshold bounds

**Unsafe claim:** “The Pickands equivalent gives a rigorous upper-tail bound for every fixed threshold,” or “a one-dimensional stationary theorem applies unchanged to a nonstationary field on a manifold.”

**Why this fails:** P029 Theorem 4 is an `u→∞` equivalent for a continuous centered stationary Gaussian process with the exact local covariance expansion and `r(t)<1` at every positive lag. P030 treats nonstationary fields only after separate entropy, anisotropic-correlation, variance-loss and manifold assumptions; its homogeneous-like, transition and Talagrand regimes have different leading terms.

**Repair:** Keep the conclusion asymptotic and verify every local/global condition. For P030 determine the maximum-variance manifold dimension and the `h_{1t}` regime before choosing a proposition; for a finite threshold use an independently established nonasymptotic inequality.

## Using a convex Gaussian lower-deviation result as concentration

**Unsafe claim:** “P011 proves a stronger Gaussian upper-tail bound for every convex Lipschitz function.”

**Why this fails:** Theorems 1.1 and 2.8 lower-bound `P(|f−med(f)|≥tL)` and need a positive variance-to-Lipschitz ratio. They address when the classical Gaussian concentration bound is tight, not a universally improved upper tail.

**Repair:** Preserve the direction of the inequality, median center, convexity, and variance hypotheses. Use a separate upper-tail theorem if the target is `P(f−med(f)≥t)`.

## Promoting finite candidate validation to a global optimizer certificate

**Unsafe claim:** “Hoeffding control for the sampled C168 candidate partitions proves the best candidate is the supremum over all measurable sign partitions.”

**Why this fails:** The finite-list union bound only controls the scores for candidates fixed before the independent validation sample. It supplies neither a covering bound for all measurable partitions nor an approximation error for the candidate discretization. Reusing validation data to choose candidates also invalidates the stated conditional independence argument.

**Repair:** Freeze the finite list before validation (or select it from independent training data), report the simultaneous finite-list error with the `(2π)^n` scale, and keep global optimality and candidate-approximation error as separate proof obligations. See `evidence/W03/validation/C168_finite_candidate_holdout.md`.


## Using a printed MDP scale without checking the theorem range

**Unsafe claim:** “P027/P028 Corollary 2.2 proves an MDP whenever `a_n min{ε_n,δ_n}→0` or `a_n min{γ_n,δ_n}→0`.”

**Why this fails:** The source assumptions do not force the two error sequences to be comparable. For independent Rademacher differences normalized by `√n`, choose the moment parameter `ε_n` (or `γ_n`) as `n^(−1/2)` and the bracket concentration parameter `δ_n=e^(−n)`. The bracket is deterministic and the conditional moment hypotheses hold, yet with `a_n=n` the printed minimum condition holds while the normalized statistic divided by `a_n` is bounded by `n^(−1/2)`. The MDP lower bound for `(1,2)` fails. The counterexample refutes the printed corollary condition/conclusion, not the main tail theorem.

**Repair:** Preserve the source's literal minimum condition in the audit. A separate sufficient scale derived from the main tail theorem is `a_n max{ε_n,δ_n}→0` (P027) or `a_n max{γ_n,δ_n}→0` (P028), conditional on that theorem and the standard tail-to-LDP argument; do not silently substitute it for the source statement.

## Treating exchangeability and without-replacement proof statements as interchangeable

**Unsafe claim:** “Every weighted exchangeable sample has the iid Hoeffding bound,” or “P008's Bennett statement is proved with the exact printed constants on p. 4.”

**Why this fails:** P007 demonstrates that arbitrary weights do not inherit the iid bound; its no-inflation result requires nonnegative weights, while the general finite-exchangeable theorem retains `ε_N`. In P008, the proof of Theorem 2.2 assumes `32t≥C_1C_2 E\widetildeΣ²` but the next intermediate bound prints denominator `C_1²`; a later line returns to `C_1C_2`.

**Repair:** Check the weight sign and finite-population centering in P007. For P008, preserve the stated theorem separately from the inconsistent proof line; verify the large-deviation argument independently before claiming that exact proof chain is established.

### Using P005's later `n`-scaled display as a sum-tail bound

P005 defines `\bar M_n²=M_n²/n` and first proves the sum inequality `P(S_n≥t)≤exp(−t²/(2M_n²))` in (23). Its later (28) prints `exp(−n(t/\bar M_n)²/2)` for the event `S_n≥t`. For two independent Rademacher signs and `t=2`, the event probability is `1/4` but that displayed RHS is `e^(−4)`, so the printed scaling cannot be used for that sum event.

**Repair:** retain (23), or rewrite it as `exp(−t²/(2n\bar M_n²))`. An exponent `−nt²/(2\bar M_n²)` corresponds to a sample-mean event when the sum inequality is applied at threshold `nt`.
