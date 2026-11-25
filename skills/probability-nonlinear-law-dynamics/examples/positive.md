# Positive pattern: separate the inner stationary law from the outer map

**Evidence used:** W21-001, complete 15-page Aldous–Feng paper; its card and section coverage are listed in [the source ledger](../references/sources.md).

For a fixed compact metric space and fixed parameter law `theta`, W21-001 Theorem 1 proves that the order-statistic kernel `K_{theta,j,k}` has a unique stationary law `pi_{j,k}(theta)`. The proof couples two chains using shared fresh samples; a partition convexity bound gives a per-two-step coalescence probability at least `k^{-(k-1)}`, and the displayed total-variation bound is

`D(2t) <= (1 - k^{-(k-1)})^t` for integers `t >= 1`.

A precise use is: for each fixed `theta`, denote the unique inner invariant law by `pi(theta)` and use the theorem's bound to control convergence of the frozen chain. Then separately define `Phi(theta)=pi(theta)` and prove the requested continuity or orbit property of `Phi` by an outer-map argument.

The same source proves that, on `[0,1]`, for `k=2` the only laws invariant for `pi_{2,2}` (and, by Theorem 3, `pi_{1,2}`) are point masses and equal two-point laws (Theorem 4, PDF pp.10–12). This exact parameter scope is useful when the user asks the `k=2` classification; it does not settle other `k`.

## Positive pattern: choose a theorem after matching the operator

- **Continuous-time nonlinear Markov flow (W21-003):** use the finite conservative-generator invariant-law correspondence under coordinate Lipschitzness/continuity. Claim uniqueness only when every `Q(m)` is irreducible and the corrected reduced Jacobian conditions hold. The row does not cover the two-/three-state branches or a nested stationary-law iteration.
- **Group-indexed QSO:** W21-018 proves that the distance to the uniform law on the current support coset tends to zero after the exact coefficients `p_ij,k=μ_(k−i−j)` are established. The coset can move periodically; only when the support is all of `G` does this directly give convergence to one fixed law, the center. Its proof's quadratic error recurrence implies a double-exponential bound, but Theorem 3.11's printed `log log ||error||` expression is undefined near zero and should not be repeated as a valid rate theorem. The support algebra is the proof mechanism, so verifying the coefficient identity comes first.
- **Poisson RDE (W21-036):** the exact transform, smoothing regularity, shift reflection, and gated even-envelope monotonicity are usable under the row's stated integrability and `D₁` bounds. The `d=1` logistic law and shift two-cycles are exact cases. Do not claim all-`d` global convergence, uniqueness, or envelope-width collapse.
- **Nonlinear Markov update:** W21-004 Theorem 2.2 applies to the exact update `N(μ)=μP_μ` when the source cross-state/law bound is `sup d_TV(P_μ(x,·),P_ν(y,·))≤2(1−α)`, which guarantees common transition mass at least `α` (not `2α`), and the same-state law sensitivity is at most `λ≤α`. It proves a unique invariant law and gives geometric convergence for `λ<α` or a `2/(λn)` bound at the threshold. This is an A122 method candidate only after the target's two Dobrushin bounds are proved; it is not an A121 outer-map result.
- **Finite-state MFG fixedpoint and stability:** W21-013 Theorem 4.1 gives a Kakutani existence proof for the stated discounted finite-state/action stationary-MFE correspondence under A1. W21-014 then supplies local-stability criteria for its myopic differential inclusion, and a two-policy global alternative only under the switching-surface and nonlinear-flow assumptions. Match the game and continuous-time inclusion before using either theorem.
- **Doubly stochastic QSO (W21-021):** use the normalized Theorem 3.6 bounds, compatible row-capped Theorem 3.8 bounds, or the specific constructive Theorem 4.1 completion. R14 rejected Corollary 4.3's general sufficient direction; normalized slices alone are not a certificate.
- **Stationary-regime passage:** W21-007 Theorem 1 applies when stochastic systems `Y^N` satisfy Feller and fixed-time conditional convergence to a deterministic measurable process. Each weak limit point of invariant laws is then invariant for that process. The corollary's Dirac limit additionally requires tightness and a continuous semiflow with a common global attractor. This transfers invariant probabilities across `N`, not iterations of one fixed operator.
- **Diffusion contraction:** W21-012 gives explicit reflection-coupling contractions for diffusion semigroups and for specified McKean–Vlasov law flows. Its Lyapunov, one-sided curvature, interaction Lipschitz, and small-interaction hypotheses are part of the theorem; retain whether the cost is additive or multiplicative.
- **Weighted-sum smoothing RDE (W21-025):** use only Lemma 7.3's local-to-global Laplace comparison with strict `p(a)<1` and local domination on `(0,t₀]`. It is not a fixed-point existence/classification or root-necessity result.
- **Centered recursive-cost contraction:** W21-027 proves `W₂(SF,SG)≤√(2/3)W₂(F,G)` for a centered Quicksort cost recursion. The exact coupling uses two independent copies and a common uniform pivot; the factor is specific to the `τ²+(1−τ)²` recursion.

- **Centered affine RDE (W21-029):** for the exact centered independent-copy affine transform with finite second moments, zero-mean square-integrable toll, and `Σ_i E T_i²<1`, Theorem 3 gives the centered `W₂` fixed point and geometric iteration. No finite-recursion or function-valued Find-process interface is admitted.
- **Finite-chain stationary sensitivity (W21-038):** if every base and perturbed matrix has one irreducible class and the base matrices have a uniform scrambling margin, the source bounds stationary-law changes by the row-matrix perturbation divided by \(1-	au_1(P)\). The parameter-to-kernel bound is an additional lemma.
- **Wasserstein stationary sensitivity (W21-040):** use Theorem 3.1's weighted Wasserstein finite-time perturbation and finite-moment stationary consequence under its exact ergodicity, drift and weighted-error hypotheses. The separate total-variation Theorem 3.2 is outside the row.

The detailed cards and physical-page coverage are linked from [the source map](../references/sources.md).


## Positive recursive-law examples with distinct hypotheses

- **W21-030:** use the ideal-`ζ_s` contraction and centered Corollary 3.4 classes for the exact finite recursive vector/scalar transform, with `0<s≤3` and `ξ<1`; apply only the mean/covariance gates required for that `s`. This is not a transfer theorem for arbitrary finite recursions.
- **W21-031:** use Lemma 3.1 only to close its exact nonnegative weighted error recursion under the negative log-index drift, `L_δ` recursion and remainder hypotheses. The row does not certify the one-branch CLT residual proof or the multi-branch sketch.
- **W21-032:** for deterministic signed weights with `sup|T_j|<1`, `ΣT_j²=1` and at least two nonzero weights, the accepted finite-variance fixed laws are Gaussian; a nonzero mean additionally requires `ΣT_j=s` and `m(s−1)=0`. **W21-034:** use only the positive-minimum support barrier and A1/A3 fixed-law cases with their positive deterministic weights and `inf_j T_j≥1` A1 gate. Neither row admits a full stable/group or Weibull classification.
- **W21-035:** use Theorem 5.3's finite-system prescribed-mean complex product-`W₂` contraction when its coefficient/toll moment and mean-balance conditions hold; cyclic Lemmas 6.8/.9 identify only the specified scalar law under `m≥7`, `ω=e^{2πi/m}`, `Re(ω)>1/2`, uniform `U`, and the stated `EX` gate. This does not imply joint covariance formulas or finite-urn transfer.

The complete source proofs and physical-page coverage are linked from [the source map](../references/sources.md).


## Positive method pattern: compose only after matching stationary-law hypotheses

W21-039 Theorem 3.1/Corollary 3.1 gives a quantitative perturbation template for `π(P)` when the base kernel is uniformly ergodic and the perturbed kernel has an invariant law. Its finite-state rank-kernel use first proves `||K_θ−K_η||op≤k||θ−η||` by maximal product coupling, then composes with the source bound only under the exact base-chain hypotheses. Uniform outer regularity requires uniform mixing constants; no outer orbit conclusion follows from this card. The theorem and coupling derivation are in the W21-039 card（本机附件：`evidence/usage_views/active/W21-039.md`）.

## Positive method pattern: exact RDE/QSO classes

W21-041/042/043/045 contribute four separate, narrowly scoped interfaces recorded in the [31-row source ledger](../references/sources.md): conditional regular-case disintegration with explicit tameness/nonarithmetic gates; a noninteger `1<α<2` Laplace-remainder comparison; Proposition 6's fixed-mean `1<p<2` characteristic-metric contraction; and finite-mean endogenous projection/pathwise identification. None admits its full source classification or an A121/A122 representation. R12's neutral review covers only the local formulas in W21-041/042/043. See [the corresponding source views](../references/sources.md).


## Positive pattern: certify only the frozen selector that was proved

Aldous–Feng W21-001 proves a unique stationary law and uniform mixing for its specific frozen nearest-order-statistic kernel. Use that result to answer the inner question at a fixed parameter. For any outer conclusion, separately derive a bound or orbit theorem for `Φ(θ)=π(K_θ)`. W21-001 Theorem 4 classifies interval fixed laws for `k=2` as point masses or equal two-point laws. W21-002's larger-family outer almost-everywhere statement is Conjecture 5, not a theorem; its general-`k` interval question remains open. The R13 calibration card and source-local proof caveats are in [the L13 reader packet](../references/method.md).

The newly added G21.01–.07 checklists in [the method reference](../references/method.md) describe what a future exact source bridge must establish; this example does not represent them as already sourced or reviewed.
