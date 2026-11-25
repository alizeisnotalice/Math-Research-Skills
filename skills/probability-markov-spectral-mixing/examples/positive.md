# Positive example: state the A040 boundary exactly

> For a finite cycle with zero external field and random-site discrete heat-bath updates, Nacu proves that the per-site-rate-one relaxation time is non-decreasing in each positive edge coupling. Kargin's paper states a homogeneous complete-graph theorem with uniform field, but its audited proof uses the reflection `f_k=−f_{n−k}`; this evidence pack applies the proof only at `H=0` and leaves the stated nonzero-field case unresolved. The arbitrary-graph edgewise gap monotonicity question remains unresolved by the current accepted source set; LPW Chapter 26 is historical reading coverage, outside W04S001's accepted Chapter 12 row. Shirai's fixed-time single-spin counterexample refutes a stronger expectation claim only; it does not decide the gap question.

This report keeps geometry, fields, parameter path and clock visible. It leaves arbitrary-graph A040 open in this evidence pack.

For a finite reversible kernel, a path comparison is applied to that fixed kernel: verify `π`, `Q`, the chosen path family and edge congestion, and use `β₁≤1−1/κ` for the Poincaré gap. If the claim is discrete-time worst-case TV, also control `β_min` (for example by odd-return paths) or prove the actual kernel is lazy/positive semidefinite. A comparison of two kernels' mixing times uses an odd flow unless the target chain has no negative-endpoint obstruction. These are fixed-model inequalities, not an ordering in an Ising edge parameter.

## Additional accepted baseline interfaces

These are the exact high-scoped uses matched to all 30 W04 baseline works; their remaining conditions are indexed in the 37-work accepted-use register（本机附件：`references/accepted_scope_register.md`）.

- **Conditional return mixture (W04S013):** for a finite continuous-time reversible chain, let `Psi` be the event that one fixed site has a specified state, with exit rate at most one, and start from `pi(·|Psi)`. The return probability to `Psi` has nonnegative spectral coefficients. If `mu=pi(Psi)∈(0,1)` and that site's clock has rate one, the accepted persistence bound is `f(t)≥mu+(1−mu)exp(−t/(1−mu))`. A rate `r` changes the exponent to `−rt/(1−mu)`.
- **Dobrushin update contractions (W04S014):** with the source's dependency matrix `R` (rows are input sites, columns updated sites), `||R||_1≤mu<1` gives random-update TV contraction `n(1−(1−mu)/n)^t`; a complete systematic scan has bound `n mu^k` after `k` scans. These clocks differ.
- **Monotone censoring (W04S015):** for the fixed strictly positive stationary law and exogenous schedule covered by the source, deleting a subsequence of conditional updates raises the law in stochastic order and does not reduce total-variation distance from stationarity. The initial law must be the top state or satisfy that `mu0/pi` is increasing.
- **Mean-field spectral reduction (W04S017):** for the zero-field homogeneous Curie–Weiss heat-bath chain on the complete graph, the magnetization chain has the same nontrivial spectral gap as the full chain. The accepted row does not include the entire phase diagram.
- **Odd-size censored mean field (W04S018):** for odd `n`, the source's global-spin-flip quotient and equal-magnetization pairing yield `min(gap_scalar,c/n)≤gap_full≤gap_scalar`, with `c=2/(1+exp(2 beta))` in the reviewed comparison. This is a quotient comparison, not a monotone coupling of full configurations.
- **Tree block criterion (W04S019):** under the stated fixed bottom boundary family, finite block-gap input, and `gamma*kappa*b<1`, the source's VM-to-block comparison gives a uniform per-site heat-bath gap on finite `b`-ary trees.
- **Critical two-dimensional rectangles (W04S020):** at the critical square-lattice Ising temperature, the reviewed block-recursion proof gives inverse gap at most `n^C` uniformly over the stated rectangles and fixed boundary conditions. RSW/FK and Martinelli block comparison are named external inputs, not reread or newly credited here.

The four preceding S013–S016 uses are also source-specific: conditional-equilibrium persistence, operator-norm update/scan contraction, exogenous fixed-law censoring, and the all-plus mixing lower bound with its LPW/Nacu dependencies. They are detailed in the linked scope map. None of these examples establishes arbitrary-graph edgewise gap monotonicity.

- **Graphical barrier approximation (W04S021):** for fixed dimension `d`, nearest-neighbor heat-bath updates at per-site rate one, `log^3 n≤m≤n`, and the source's torus/core/collar scales, shared graphical updates approximate the periodic-barrier core dynamics up to `log^(4/3)n` simultaneously over starts and times, with failure at most `n^(−10d)` for sufficiently large `n`. This local approximation is not the full cutoff theorem.
- **PSD Ising localization (W04S022):** for a finite-cube law proportional to `exp(xᵀJx/2+hᵀx)`, real symmetric `0≤J<I`, and the per-site-rate-one conditional-variance heat-bath form, `(1−||J||op) Var(f)≤Σ_i E Var(f|others)`. The accepted proof scope uses the source's finite rank-one stopping argument and only the loose stop bound `T≤Tr J`.
- **Pinned spectral independence (W04S023):** under spectral independence for every feasible pinning of a weighted `n`-subset distribution, use the source's exact `κ_(r,s)` expression for the down-up gap and its `ell/(n κ_(n−ell,n))` block factor. No final degree-dependent main-theorem constant is imported.
- **Field-to-Glauber comparison (W04S024):** the accepted Lemma 2.4 comparison is `gap_GD(mu)≥gap_FD(mu,theta)·min_pinning gap_GD(mu^theta)`, with every feasible pinning in the minimum and the original `n`-coordinate clock, including frozen holds.
- **Fixed-law order-statistic inner chain (W04S025):** for fixed compact-space law `theta`, `k≥2`, and `1≤j≤k`, the source's common-second-batch construction gives a unique stationary `pi` and the reviewed two-step contraction and set-mass inequalities. This says nothing about nonlinear iteration of `theta↦pi`.

## Five final W04 baseline interfaces

- **Aldous Proposition 8 (W04S028):** on the finite irreducible reversible continuous-time chain with the source clock and TV threshold, use `β≤τ₁≤β[1+½log(1/π_min)]`, where `β` is relaxation time. This is not a discrete-time bound.
- **Chen–Wang Theorem 1.2 (W04S029):** with finite reversible conservative `Q`, `max_i(-Q_ii)≤M`, no killing and the source minimum-mass cut value `k′`, use `gap≥M(1−√(1−(k′/M)²))≥(k′)²/(2M)`.
- **Dyer–Goldberg–Jerrum Theorems 1–2 (W04S031):** compute the exact directed-edge loads for the source-positive routed demands. The ordinary flow controls `E`; the odd-flow condition additionally controls `F` and the lower spectral endpoint.
- **Sambale–Sinulis (W04S032):** with full support, every partial one-site conditional at least `α₁`, the stated updated-row/input-column norm bound `||J||₂≤1−α₂`, and the total-rate-one random-site kernel, use the accepted entropy/mLSI bounds with their stated constants.
- **Paulin Theorem 3.5 (W04S033):** for a finite reversible kernel started at `X₁~π`, centered observables, and the source discrete observation times, use equations (3.14)/(3.16), with `γ>0` for fixed and `γ_abs>0` for varying observables.

These are source-specific accepted interfaces, not a blanket approval of nearby source theorems.

## Exact convention checks

R01's separate exact finite audit (not new source credit) constructs the two-spin zero-field heat-bath chain and verifies the distinctions needed by the methods above: at `exp(2J)=4`, random-site/total-rate-one gap `1/5` versus per-site-rate-one generator gap `2/5`; a one-spin pinning keeps the original two-coordinate clock gap `1/2`, whereas renormalizing to one active coordinate gives `1`; a near-periodic two-state kernel has Poincaré gap `99/50` and absolute gap `1/50`; on the simple `y=exp(2J)>1` branch the moving-stationary-law terms cancel and `dλ₂/dJ=2y/(1+y)^2`. The exact script and output are `exact_checks.py`（本机附件：`evidence/math_cases/old_markov_entry_integration_v1/exact_checks.py`） and `exact_checks.out.json`（本机附件：`evidence/math_cases/old_markov_entry_integration_v1/exact_checks.out.json`）; their proof note states the finite scope.
