# Negative pattern: do not promote inner mixing or partial exclusions

**Evidence used:** W21-001 and W21-002, both complete primary-source reads; cards and physical-page coverage linked from `references/sources.md`.

## Invalid inference: frozen-kernel mixing implies outer convergence

The bound in W21-001 Theorem 1 controls the Markov chain with one fixed `theta`. It does not bound the movement of `Phi(theta)=pi(K_theta)` when `theta` changes. Therefore it cannot, by itself, prove convergence of `theta[n+1]=Phi(theta[n])`, rule out cycles, or prove an almost-everywhere basin statement. W21-002 Conjecture 5 (PDF pp.13–14) explicitly states the finite-simplex almost-everywhere outer-convergence claim as a conjecture.

**Repair:** derive a cross-kernel/stationary-law perturbation bound for `theta != eta` and then prove a global outer contraction, Lyapunov/no-cycle theorem, or a separate basin-measure result.

## Invalid inference: density-only exclusion implies no full-support law

W21-002 §7.3 (PDF p.22) gives an additional exclusion criterion for invariant densities for selected `(j,k)` parameters. It does not exclude singular continuous or mixed full-support probability laws. The source's finite-grid invariant example is not a full-support law on the interval.

**Repair:** write the fixed-law equation for arbitrary Borel measures and control atoms, singular continuous parts, and absolutely continuous parts without inserting a density hypothesis.

## Invalid inference: continuity makes every omega-limit point fixed

A continuous map can have a periodic orbit. On the two-point state space `{0,1}`, parameterize laws by `mu_p = Bernoulli(p)` with row vector `(1-p,p)`, and let every row of the frozen transition matrix be `(p,1-p)`:

`K_p = [[p, 1-p], [p, 1-p]]`.

Every frozen chain reaches its unique stationary law `(p,1-p) = Bernoulli(1-p)` in one step, so the induced stationary-law map is `Phi(p)=1-p`. Its orbit from `p=0` is `0,1,0,1,...`; the omega-limit set `{0,1}` is invariant, but neither point is fixed. Exact symbolic verification is saved in `evidence/W21/checks/frozen_kernel_two_cycle.txt`.

This is a synthetic two-state law operator, **not** the nearest-order-statistic kernel in A121/A122. It disproves only the generic inference from frozen-kernel mixing (even one-step mixing), continuity, and compactness to outer-orbit convergence or fixedness of every omega-limit point.

**Repair:** prove asymptotic regularity `|Phi(p_n)-p_n| -> 0` if the goal is to show each cluster point is fixed, or independently exclude cycles/recurrent sets. To prove the whole sequence converges, add a global orbit argument.

## Invalid inference: a neighboring law operator has the same state space

- W21-003 concerns the continuous-time nonlinear flow `m˙=mQ(m)`. Its Kakutani, degree, and small-state ergodicity theorems do not give a discrete outer theorem for `theta -> pi(K_theta)`.
- W21-018 concerns a group-indexed quadratic stochastic operator. Theorem 3.9 compares each iterate to the uniform law on its current support; that support coset can cycle. The proof gives a quadratic error recurrence, but its printed Theorem 3.11 `log log ||error||` expression is undefined as the error tends to zero. Do not turn the moving-support statement into convergence to a fixed law on one eventual coset, or quote the malformed rate expression.
- W21-024 concerns weighted sums of iid copies, and W21-036 concerns a Poisson d-th-minimum RDE. Their weight moments, recursive-copy identities, tail domains, and (for W21-036) shift symmetry are substantive hypotheses.
- W21-025 studies the generalized smoothing transform `Law(Σ_i A_i Z_i)` and proves iteration convergence under a root and matched-tail condition. W21-027 contracts a centered Quicksort recursive cost law with coefficient `√(2/3)`. Neither transform has been derived from `θ↦π(K_θ)`; those source-specific constants/classifications do not transfer by analogy.
- W21-004's global Dobrushin theorem is for `μ↦μP_μ`. It has the right fixedpoint equation shape for A122 if `P_μ=K_μ`, but its cross-state/law overlap and same-state law sensitivity hypotheses remain unverified for the target. It does not prove convergence of the nested stationary-law map in A121.
- W21-007's stationary-regime theorem concerns invariant laws of varying-size stochastic systems `Y^N` under fixed-time conditional convergence to a deterministic process. It does not imply convergence of iterates of a fixed law map. W21-012's Kantorovich estimates concern specified diffusion semigroups and McKean–Vlasov SDE flows, not a finite-state stationary kernel without a proved representation.
- W21-023 has conflicting asymmetric p/q conventions: the printed kernel Eq. (2.1) assigns p to both outcomes; §3.1's two-atom recurrence corresponds to lower-p/upper-q, while §3.2's interval/density/CDF equations correspond to lower-q/upper-p. Theorem 4.6 also claims endpoint convergence for every continuous initial law, although a valid parent-selection kernel preserves an interior support interval. The paper declares `[0,1)` but later takes a limit to `delta_1`, and does not specify the topology of “strong limit”. Keep the finite and continuous subsection formulae separate and do not transfer the unsupported endpoint claim.

**Repair:** write the target operator in the same coordinates as the source and prove equality, including the domain, topology, transition/weight laws, invariance class, and all side conditions. If any identity is missing, keep the source as a method analogy and state the unresolved bridge.


## Invalid inference: recursive-law results transfer by topic label

W21-030 requires its independent-copy recursive sequence, Zolotarev moment class, coefficient contraction, and small-index/self-index bounds. W21-031’s degenerate normal limit needs logarithmic index drift plus quantitative L3 and mean/variance/toll assumptions; it is not a generic fixed-point theorem. W21-032 and W21-034 classify different deterministic weighted-sum and weighted-order-statistic operators with group, support, and drift conditions. W21-035’s RDE comes from an urn tree and includes phase-periodic behavior. None of these identities has been derived for `Phi(theta)=pi(K_theta)` or for the A122 kernel equation.

**Repair:** derive the target’s exact distributional identity, topology, independent-copy structure, coefficients, and moments first; then check the source theorem line by line. If the identity is absent, use the result only as a conditional method analogy.


## Invalid inference: a stationary perturbation bound is already an outer contraction

W21-038 and W21-040 compare stationary laws for two specified transition kernels. W21-038 needs the base finite chain to have one irreducible class and \(	au_1(P)<1\); W21-040 needs its Wasserstein-ergodicity and Lyapunov hypotheses. Neither source bounds \(K_	heta-K_\eta\) as a function of \(	heta-\eta\). Even after deriving that estimate, the composed constant may be at least one, and the finite-chain scrambling margin may vanish near a boundary stratum.

**Repair:** prove the parameter-to-kernel sensitivity bound on the exact stratum, make ergodicity/drift constants uniform there, and check that the resulting stationary-law Lipschitz factor is strictly below one before using Banach iteration.

## Invalid inference: simplex invariance, Volterra structure, or majorization settles orbit convergence

- W21-015 states that its explicit quadratic map has nonconvergent Cesàro averages for interior noncentral initial conditions, but Theorem 2's proof depends on a Theorem 1 passage from product decay to eventual avoidance of a center neighborhood that the two-page note does not separately justify. The source's Note 1 about the Cesàro cluster set also conflicts with connectedness. Preserve the exact source scope and these proof limits; it is not a counterexample for A121 unless the target is shown to contain or be conjugate to the map.
- W21-019’s equivalence is restricted to transversal Volterra QSOs by the paper’s explicit global standing assumption; the five-page manuscript states the theorem but contains no proof, so [3–4] remain unaudited. Its intro calls one displayed map non-Volterra, but the formula factors into Volterra form with a cyclic tournament; isolate this classification inconsistency, not the main equivalence theorem.
- W21-021 requires an actual doubly stochastic QSO, i.e. `Vx` is majorized by `x`, and its safe coefficient-slice criterion includes total-mass normalization. The printed Theorem 3.4 statement does not show that equality, while its proof uses `A in U_1`; this remains a possible scope omission for reviewer resolution. Do not use the standalone statement without normalization or infer majorization for a stationary-law map.

**Repair:** prove the target’s exact polynomial/Volterra/doubly-stochastic representation, including its coefficient constraints and boundary behavior, before importing any of these simplex results. Keep orbit convergence, Cesàro convergence, regularity, and supportwise ergodicity as separate conclusions.



## Source-level methods do not fill a missing target identity

W21-041/042/043/045 are eligible provisionally as operator-specific smoothing-transform/RDE sources, and W21-044 as a centered-QSO source. That tool-scope classification does not make them A121/A122 target evidence: verify the target has the exact weighted child-copy recursion or centered parental-average plus independent noise before using their theorem conclusions. The source cards preserve separate assumptions and proof boundaries; see [the W21 source map](../references/sources.md#supplementary-full-text-methods).

## Invalid inference: local characteristic-function decay guarantees a noise-factor weak limit

W21-044 Theorem 5 assumes both its local bound on `|φ_G|` and that the sequence of iterated noise factors `G^{ {n} }` already has a weak limit. For `G=N(m,σ²)` with `m≠0`, the local modulus condition holds with `ε=1`, but the factor is `N(nm,σ²Σ_{j<n}2^{-j})`: the variance stays below `2σ²` while the mean escapes. Chebyshev's inequality shows the sequence is not tight, so there is no weak limit to regularize. The exact geometric-sum calculation is saved in `evidence/W21/checks/W21-044-gaussian-noise-factor.txt` and the theorem's conditional scope is recorded in [the source card](../evidence/W21/cards/W21-044.md).

## Invalid inference: an elementary fixed-point criterion excludes all fixed points

In the read arXiv v1 of W21-043, Proposition 1's random-walk requirement is only `liminf S_n=-∞`, which permits oscillation; Theorem 2 uses the stronger full drift `S_n→−∞` for elementary fixedpoints. A neutral source-local adjudication confirms that an admissible arithmetic smoothing transform contradicts only Proposition 1(b)'s all-scale regular variation and Proposition 3(c)'s claim that there are no other fixed points. Keep those source-version statements isolated. Theorem 2, Proposition 3(a)–(b), and Propositions 4/6 are not refuted by that model; do not transfer any result without its exact hypotheses. No later journal-version equivalence was checked. See [the adjudication linked from the card](../evidence/W21/cards/W21-043.md).
