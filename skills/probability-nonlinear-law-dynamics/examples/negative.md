# Negative pattern: do not promote inner mixing or partial exclusions

**Evidence used:** W21-001 and W21-002, both complete primary-source reads; cards and physical-page coverage are listed in [the source ledger](../references/sources.md).

## Invalid inference: frozen-kernel mixing implies outer convergence

The bound in W21-001 Theorem 1 controls the Markov chain with one fixed `theta`. It does not bound the movement of `Phi(theta)=pi(K_theta)` when `theta` changes. Therefore it cannot, by itself, prove convergence of `theta[n+1]=Phi(theta[n])`, rule out cycles, or prove an almost-everywhere basin statement. W21-002 Conjecture 5 (PDF pp.13–14) explicitly states the finite-simplex almost-everywhere outer-convergence claim as a conjecture.

**Repair:** derive a cross-kernel/stationary-law perturbation bound for `theta != eta` and then prove a global outer contraction, Lyapunov/no-cycle theorem, or a separate basin-measure result.

## Invalid inference: density-only exclusion implies no full-support law

W21-002 §7.3 (PDF p.22) gives an additional exclusion criterion for invariant densities for selected `(j,k)` parameters. It does not exclude singular continuous or mixed full-support probability laws. The source's finite-grid invariant example is not a full-support law on the interval.

**Repair:** write the fixed-law equation for arbitrary Borel measures and control atoms, singular continuous parts, and absolutely continuous parts without inserting a density hypothesis.

## Invalid inference: continuity makes every omega-limit point fixed

A continuous map can have a periodic orbit. On the two-point state space `{0,1}`, parameterize laws by `mu_p = Bernoulli(p)` with row vector `(1-p,p)`, and let every row of the frozen transition matrix be `(p,1-p)`:

`K_p = [[p, 1-p], [p, 1-p]]`.

Every frozen chain reaches its unique stationary law `(p,1-p) = Bernoulli(1-p)` in one step, so the induced stationary-law map is `Phi(p)=1-p`. Its orbit from `p=0` is `0,1,0,1,...`; the omega-limit set `{0,1}` is invariant, but neither point is fixed. Exact symbolic verification is saved in `../evidence/checks/frozen_kernel_two_cycle.txt`.

This is a synthetic two-state law operator, **not** the nearest-order-statistic kernel in A121/A122. It disproves only the generic inference from frozen-kernel mixing (even one-step mixing), continuity, and compactness to outer-orbit convergence or fixedness of every omega-limit point.

**Repair:** prove asymptotic regularity `|Phi(p_n)-p_n| -> 0` if the goal is to show each cluster point is fixed, or independently exclude cycles/recurrent sets. To prove the whole sequence converges, add a global orbit argument.

## Invalid inference: a neighboring law operator has the same state space

- W21-003 concerns the continuous-time nonlinear flow `m˙=mQ(m)`. Its Kakutani, degree, and small-state ergodicity theorems do not give a discrete outer theorem for `theta -> pi(K_theta)`.
- W21-018 concerns a group-indexed quadratic stochastic operator. Theorem 3.9 compares each iterate to the uniform law on its current support; that support coset can cycle. The proof gives a quadratic error recurrence, but its printed Theorem 3.11 `log log ||error||` expression is undefined as the error tends to zero. Do not turn the moving-support statement into convergence to a fixed law on one eventual coset, or quote the malformed rate expression.
W21-024's accepted finite-mean branch requires finite fixed `N`, nonnegative weights, iid independent children, `m(1)=1`, `v′(1)<0`, and the stated higher moment; critical, infinite-mean and full tail/lattice classifications are excluded. W21-036 supplies its exact Poisson transform, regularity, reflected shifts, gated even-envelope monotonicity and `d=1` logistic examples, but not all-`d` global convergence or interval-width collapse.
- W21-025 is admitted only for Lemma 7.3's local-to-global Laplace comparison, under the strict moment `p(a)=EΣ_i A_i^a<1` and local domination `φ≤ψ` on `(0,t₀]`; it does not establish the root/matched-tail fixed-point classification or general iteration convergence. W21-027 separately contracts a centered Quicksort recursive cost law with coefficient `√(2/3)`. Neither transform has been derived from `θ↦π(K_θ)`, so its source-specific conclusions do not transfer by analogy.
- W21-004's global Dobrushin theorem is for `μ↦μP_μ`. It has the right fixedpoint equation shape for A122 if `P_μ=K_μ`, but its cross-state/law overlap and same-state law sensitivity hypotheses remain unverified for the target. It does not prove convergence of the nested stationary-law map in A121.
- W21-007's stationary-regime theorem concerns invariant laws of varying-size stochastic systems `Y^N` under fixed-time conditional convergence to a deterministic process. It does not imply convergence of iterates of a fixed law map. W21-012's Kantorovich estimates concern specified diffusion semigroups and McKean–Vlasov SDE flows, not a finite-state stationary kernel without a proved representation.
- W21-023 has conflicting asymmetric p/q conventions: the printed kernel Eq. (2.1) assigns p to both outcomes; §3.1's two-atom recurrence corresponds to lower-p/upper-q, while §3.2's interval/density/CDF equations correspond to lower-q/upper-p. Theorem 4.6 also claims endpoint convergence for every continuous initial law, although a valid parent-selection kernel preserves an interior support interval. The paper declares `[0,1)` but later takes a limit to `delta_1`, and does not specify the topology of “strong limit”. Keep the finite and continuous subsection formulae separate and do not transfer the unsupported endpoint claim.

**Repair:** write the target operator in the same coordinates as the source and prove equality, including the domain, topology, transition/weight laws, invariance class, and all side conditions. If any identity is missing, keep the source as a method analogy and state the unresolved bridge.


## Invalid inference: recursive-law results transfer by topic label

W21-030 admits only the ideal-`ζ_s` contraction and centered Corollary 3.4 classes under `0<s≤3`, independent tuple/children, and `ξ<1`; it does not admit the main finite-recursion transfer or nonzero-mean/L² extensions. W21-031 admits only Lemma 3.1's negative-log-index-drift closure of its exact weighted error recursion, not the full one-branch CLT residual proof or multi-branch sketch. W21-032 admits only the finite-variance Gaussian fixed-law class for its deterministic signed weights and mean gate, not full Lévy/Choquet/stable classification. W21-034 admits only the positive-min support barrier and A1/A3 cases with `inf_j T_j≥1` for A1, not A2/A4 or Weibull/Choquet–Deny classification. W21-035 admits Theorem 5.3's prescribed-mean complex product-`W₂` contraction and cyclic Lemmas 6.8/.9 only, not joint covariance or finite-urn transfer. None supplies an operator identity for `Φ(θ)=π(K_θ)`.

**Repair:** derive the target’s exact distributional identity, topology, independent-copy structure, coefficients, and moments first; then check the source theorem line by line. If the identity is absent, use the result only as a conditional method analogy.


## Invalid inference: a stationary perturbation bound is already an outer contraction

W21-038 and W21-040 compare stationary laws for two specified transition kernels. W21-038 needs the base finite chain to have one irreducible class and \(	au_1(P)<1\); W21-040 needs its Wasserstein-ergodicity and Lyapunov hypotheses. Neither source bounds \(K_	heta-K_\eta\) as a function of \(	heta-\eta\). Even after deriving that estimate, the composed constant may be at least one, and the finite-chain scrambling margin may vanish near a boundary stratum.

**Repair:** prove the parameter-to-kernel sensitivity bound on the exact stratum, make ergodicity/drift constants uniform there, and check that the resulting stationary-law Lipschitz factor is strictly below one before using Banach iteration.

## Invalid inference: simplex invariance, Volterra structure, or majorization settles orbit convergence

- W21-015 states that its explicit quadratic map has nonconvergent Cesàro averages for interior noncentral initial conditions, but Theorem 2's proof depends on a Theorem 1 passage from product decay to eventual avoidance of a center neighborhood that the two-page note does not separately justify. The source's Note 1 about the Cesàro cluster set also conflicts with connectedness. Preserve the exact source scope and these proof limits; it is not a counterexample for A121 unless the target is shown to contain or be conjugate to the map.
- **W21-019:** the R15-admitted use is only the derived sufficient convergence direction for a transitive tournament on the positive support of an exact transversal Volterra QSO. The proof-free four-way equivalence/converses and tie/zero-edge cases are not admitted. The source does not call its introductory map non-Volterra.
- **W21-021:** R14's neutral review rejects Corollary 4.3's general sufficient direction. Keep only Theorem 3.6's full normalization, Theorem 3.8's compatible row-capped witnesses, and the particular Theorem 4.1 completion. Do not cite Corollary 4.3 or infer a majorization certificate from normalized slices alone.

**Repair:** prove the target’s exact polynomial/Volterra/doubly-stochastic representation, including its coefficient constraints and boundary behavior, before importing any of these simplex results. Keep orbit convergence, Cesàro convergence, regularity, and supportwise ergodicity as separate conclusions.



## Source-level methods do not fill a missing target identity

W21-041/042/043/045 remain four distinct exact operator-specific interfaces. Their accepted uses and restrictions are in the [scoped source ledger](../references/sources.md); none is a general weighted smoothing-transform classification or an A121/A122 result without the exact target recursion.

## Invalid inference: local characteristic-function decay guarantees a noise-factor weak limit

W21-044 Theorem 5 assumes both its local bound on `|φ_G|` and that the sequence of iterated noise factors `G^{ {n} }` already has a weak limit. For `G=N(m,σ²)` with `m≠0`, the local modulus condition holds with `ε=1`, but the factor is `N(nm,σ²Σ_{j<n}2^{-j})`: the variance stays below `2σ²` while the mean escapes. Chebyshev's inequality shows the sequence is not tight, so there is no weak limit to regularize. The exact geometric-sum calculation is saved in `../evidence/checks/W21-044-gaussian-noise-factor.txt` and the theorem's conditional scope is recorded in the source card（本机附件：`evidence/usage_views/active/W21-044.md`）.

## Invalid inference: an elementary fixed-point criterion excludes all fixed points

In the read arXiv v1 of W21-043, Proposition 1's random-walk requirement is only `liminf S_n=-∞`, which permits oscillation; Theorem 2 uses the stronger full drift `S_n→−∞` for elementary fixedpoints. A neutral source-local adjudication confirms that an admissible arithmetic smoothing transform contradicts only Proposition 1(b)'s all-scale regular variation and Proposition 3(c)'s claim that there are no other fixed points. Keep those source-version statements isolated. Theorem 2, Proposition 3(a)–(b), and Propositions 4/6 are not refuted by that model; do not transfer any result without its exact hypotheses. No later journal-version equivalence was checked. See the adjudication linked from the card（本机附件：`evidence/usage_views/active/W21-043.md`）.


## New method boundary: do not treat the inherited baseline as seven new-source approvals

The inherited 31 works cover distinct nonlinear Markov, RDE, QSO, perturbation, and related modules. Their old exact use can be preserved without saying, for example, that a Dobrushin contraction proves a Markov-chain tree formula, a diffusion coupling proves Schur stability of a simplex map, or an RDE source certifies a bifurcation. The L13 crosswalk（本机附件：`evidence/G21_new_method_zero_mapping.md`） marks each new G21.01–.07 link unassigned pending an exact theorem and reviewed bridge.
