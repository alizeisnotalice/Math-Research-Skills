# Positive examples (W03 interim)

## Independent matrix sum

**Task:** Bound the upper tail of the largest eigenvalue of a finite sum of independent centered self-adjoint random matrices.

**Safe workflow:** Verify independence, `E X_k=0`, and an almost-sure upper bound `lambda_max(X_k)<=R`. Compute/check `sigma^2=||sum E X_k^2||`. Then cite Tropp P001, Theorem 1.4 (PDF p. 4), preserving the dimension factor `d` and exponent `-t^2/[2(sigma^2+Rt/3)]`. For an operator-norm tail, repeat the argument for `-X_k` with its own upper bound.

## Empirical-process supremum with Gaussian calibration

**Task:** Approximate the distribution of a studentized supremum over a growing class and use a short-interval bound to control coverage error.

**Safe workflow:** First verify the iid, pointwise-measurability, envelope-moment, and pre-Gaussian hypotheses and select `epsilon_n,gamma_n` so P018 Theorem 2.1/Corollary 2.2 makes the coupling error small. If the Gaussian process has separable paths, zero mean, unit marginal variances, and finite supremum, P012 Theorem 2.1 bounds the Levy concentration function by `4 epsilon(E sup G+1)`. Then use the anti-concentration bound to convert the coupling/estimation perturbation into a coverage or Kolmogorov error, preserving every error term.

**Evidence state:** P001, P012, and P018 have full-text cards; their review status is pending. The target empirical-process class and all quantitative coupling conditions remain model-specific proof obligations.

## Maximum with shared marginals and dependence information

**Task:** Bound `P{x < max_i X_i ≤ x+ε}` for identically distributed coordinates with an unknown copula.

**Safe workflow:** Use P019 Theorem 1 for the sharp arbitrary-copula extrema. If the actual copula diagonal is convex, P019 Theorem 2 improves the upper bound; then use a verified marginal density/hazard bound if a uniform-in-`x` result is needed. A common marginal CDF is essential, and the arbitrary-copula result may grow linearly with dimension.

## Gaussian Hilbert norm comparison

**Task:** Compare `P(||ξ−a||≤x)` with another centered Gaussian Hilbert-ball probability, or bound a short interval for `||ξ−a||²`.

**Safe workflow:** Check that the elements lie in a separable Hilbert space with trace-class covariance. Apply P022 Theorem 2.1 with the eigenvalue-sequence difference and `||a||²`, or Theorems 2.6–2.7 with the full spectral scale `κ(Σ)`. Do not substitute this for a coordinatewise Gaussian maximum bound.

## Large-deviation formulation

**Task:** Identify a candidate exponential rate for a sequence of probability laws.

**Safe workflow:** Use P016 to organize the speed, Polish-space topology, rate-function goodness, closed-set upper bound and open-set lower bound; use the Laplace principle only after its LDP and functional hypotheses hold. Verify the applicable Cramér/Sanov/Markov/small-noise theorem at its primary source before claiming a rate.

## Choose the martingale normalization before the theorem

**Task:** Obtain a Gaussian tail approximation for a martingale sum when its quadratic variation is random.

**Safe workflow:** If conditional signed moments satisfy P027 (A1) and the terminal predictable bracket has the sub-Gaussian deviation bound P027 (A2), use the theorem for `X_n/sqrt(<X>_n)` and retain its stated range and logarithmic error. If the target is instead `S_n/sqrt([S]_n)`, P028 has that self-normalized statistic but needs conditional `(2+ρ)` moment control relative to conditional variances and concentration of `<S>_n`; its main proof is in an external supplement. P025 is another distinct option only when the terminal predictable bracket is deterministically within the stated tolerance. Do not swap predictable and realized brackets or import assumptions from one theorem into another.

**Evidence state:** P025, P027, and P028 have full-text cards; review remains pending. P027's Theorem 2.1 proof is present in the paper, but the smoothing details for Lemma 4.5 are cited to its supplement. P028's Theorem 2.1 detailed proof is not in the 24-page article.

## High excursions of a stationary Gaussian process

**Task:** Obtain the leading asymptotic of `P(sup_[0,p] X(t)>u)` as `u→∞`.

**Safe workflow:** Verify that `X` is centered, continuous, stationary, and Gaussian; check the local covariance expansion `r(t)=1−|t|^α+o(|t|^α)` for a fixed `0<α≤2` and the strict condition `r(t)<1` for every `t>0`. Then P029 Theorem 4 gives `H_α p u^(2/α) Ψ(u)(1+o(1))`. Its proof needs the local block limit and the separated-block overlap bounds, so retain the entire assumption set and label the conclusion asymptotic.

## Smooth-manifold Gaussian field

**Task:** Classify the leading high-excursion contribution near a non-isolated maximum-variance set.

**Safe workflow:** For P030, derive the standardized-field entropy condition, local correlation scale `q_t(u)`, variance-loss limit `h_{1t}`, and the smooth manifold/stratum geometry. Choose among the homogeneous-like, transition, Talagrand or general case only after checking which `K`-sets cover the neighborhood. Theorem 1 applies to the unit-variance locally homogeneous full-dimensional case; the propositions for nonconstant variance or lower-dimensional maximum loci have different normalizations. Read the cited source for proof details the article only outlines.

**Evidence state:** P029 and P030 were read in full and their theorem/condition pages visually checked. Both remain pending independent review.

## Finite-candidate holdout score for C168

**Task:** Compare a finite list of proposed sign partitions for the two-dimensional OU sine-kernel objective using independent Gaussian validation samples.

**Safe workflow:** For `G,H` iid standard Gaussian vectors in `R²`, compute the score `Z=f(G)g(H)sin⟨G,H⟩∈[-1,1]`; the unnormalized objective is `(2π)² E Z`. Select and freeze at most `M` candidate pairs using prior knowledge or independent training data, then draw `N` independent validation pairs. Hoeffding plus a union bound gives simultaneous error `(2π)² sqrt(2 log(2M/δ)/N)` with probability at least `1−δ`. The derivation and a numerical formula check are in `evidence/W03/validation/C168_finite_candidate_holdout.md`.

**Evidence state:** The score bound is a proved finite-list result. It does not compare the list with all measurable partitions, prove global optimality, or bound candidate discretization/approximation error. P031 Theorem 2.2.6 is cited for the bounded-variable Hoeffding statement, whose proof is assigned in that textbook; the validation card includes a self-contained Hoeffding-lemma proof for this width-2 case.


## Match the dependence model and statistic

- For independent centered scalars in intervals `[a_i,b_i]`, compute `A_i=(|a_i|+b_i)/2` and `G_i=√(|a_i|b_i)` and apply P005's geometric proxy only when `b_i<|a_i|`; use the complementary proxy for the other tail. For sums use Eq. (23), or derive from it with `M_n²=n\bar M_n²`; do not use the paper's later mis-scaled sum displays.
- For a countable-state HMM, first establish the underlying chain's geometric-ergodicity constants `(G,θ)`. P006 then gives a Hamming-Lipschitz path bound, and under stationarity gives the histogram and uniform-occupation bounds with their bias terms.
- For a bounded finite exchangeable vector, write the exact finite-population mean and fixed weights before using P007. If the weights are nonnegative, Theorem 5 removes the `ε_N` inflation; otherwise keep it. In Theorem 6 retain the random length-`N` empirical variance in both the mgf and stated random threshold.
- For a uniform permutation statistic or sampling without replacement, identify the permutation model and its quadratic proxy before using P008. The theorem statement is recorded, with the p. 4 proof-line inconsistency disclosed in the card.
- For Talagrand-type bounds, select P009's inequality by the actual structure: product convex distance, biased cube, standard Gaussian transport, or independent empirical supremum.
