# Working method and theorem boundaries

## 1. Freeze the dynamics before discussing a gap

Record: finite graph G=(V,E), state space {−1,+1}^V, boundary condition, external field, couplings and sign convention, heat-bath versus Metropolis update, site selection probabilities, and whether time is discrete or continuous. Reversibility is with respect to the stated Gibbs law; irreducibility is needed for a unique stationary law and positive gap.

For the zero-field ferromagnetic pair model used in A040,

`π_J(σ) ∝ exp(Σ_{uv∈E} J_uv σ_u σ_v)`, with `J_uv ≥ 0`.

Do not silently add a field, change the graph, or replace single-site heat-bath by a different kernel. Nacu, Kargin, Shirai, LPW, and the finite scan use random-site discrete-time heat-bath, but their normalizations must still be compared explicitly.

## 2. Normalize the clock

Let K_v be the heat-bath conditional-resampling Markov operator at site v. Random-site discrete time is

`P = (1/n) Σ_v K_v`, `n=|V|`.

The per-site-rate-one continuous-time generator is

`L_site = Σ_v (K_v − I) = n(P−I)`.

The total-update-rate-one continuous-time generator is

`L_total = (1/n) Σ_v (K_v − I) = P−I`.

Thus the Poincaré gaps satisfy `gap(L_site)=n(1−λ₂(P))` and `gap(L_total)=1−λ₂(P)`. Multiplying all transition rates by c multiplies the continuous-time gap by c and divides relaxation time by c. State the convention every time a rate or gap is compared.

For heat-bath updates each K_v is conditional expectation onto functions of σ_{−v}, hence a self-adjoint projection on L²(π). Their average P is positive semidefinite. Here the Poincaré gap is `1−λ₂(P)`; do not replace it by an absolute gap unless the question asks for worst-case convergence in a non-lazy chain with negative spectrum.

## 3. Use the variational identity, not a heuristic

For a finite reversible continuous-time generator Q with stationary π,

`gap(Q) = inf_{Var_π(f)>0} D_Q(f,f)/Var_π(f)`,

where `D_Q(f,f) = (1/2) Σ_{x,y} π(x)Q(x,y)(f(x)−f(y))²`. For a reversible discrete kernel P use `D_P(f,f)=⟨f,(I−P)f⟩_π`. A parameter change changes both π and transition conductances. A sign for `Cov_π(F,σ_uσ_v)` alone does not determine a sign for the infimum or for the moving second eigenvalue.

When differentiating λ₂(J), first check whether the eigenvalue is simple and differentiable. At crossings or multiplicity, formulate the claim as an order inequality on gaps or eigenvalues, not an unqualified derivative.

## 4. Keep static correlation theorems in scope

### FKG

On a finite distributive lattice Γ, if μ is positive and log-supermodular,

`μ(x∧y) μ(x∨y) ≥ μ(x) μ(y)` for every x,y,

then increasing f,g satisfy `Cov_μ(f,g)≥0`. For the pairwise Ising model with coordinatewise order on {−1,+1}^V, J_uv≥0 gives this lattice condition. Arbitrary one-site fields cancel from the meet/join difference, so the FKG increasing-observable statement allows arbitrary fields. Holley's comparison theorem is a separate cross-condition for two measures; do not invoke “Holley” without writing the exact condition and order direction.

### GKS

For the classical pair-interaction Ising ferromagnet, GKS inequalities concern equilibrium spin products: under the original hypotheses (nonnegative pair couplings and, for the field version, nonnegative fields / plus boundary), spin-product expectations and their relevant covariances are nonnegative. State which GKS version is being used. The 1972 higher-order-spin source gives additional coefficient restrictions for FKG and emphasizes that GKS and FKG have different scopes.

Neither GKS nor FKG is a theorem about a finite-time transition operator, its eigenvalues, or its spectral gap. An equilibrium derivative identity such as `d/dJ_e E_π[F] = Cov_π(F,σ_uσ_v)` is not a gap-derivative formula.

## 5. A040 evidence map

The source record LPW, Chapter 26 Question 2 (printed pp.359–360), asks whether the zero-field Ising Glauber gap on any graph is non-increasing in each inhomogeneous ferromagnetic edge interaction. Nacu proves the cycle case with arbitrary positive edge couplings and no field. Kargin's Theorem 1 is printed for a homogeneous complete-graph family with uniform field, but the audited proof uses `f_k=−f_{n−k}` at PDF p.5; reflection of the magnetization chain is available at `H=0`, not automatically at `H≠0`. This evidence pack therefore uses only the audited zero-field homogeneous subcase and records the nonzero-field proof as unresolved, not as a refuted theorem. Neither result changes one arbitrary edge on every graph.

Shirai disproves a stronger fixed-time claim: for a finite graph containing a length-3 path there are positive ferromagnetic couplings, a time, and a site for which the all-plus-start single-site expectation decreases in one edge coupling. This shows a direct static-correlation-to-dynamics argument is unsafe; it does not settle the gap conjecture.

In any proof, search, or literature summary, keep separate: (a) edge-addition monotonicity, (b) common-temperature scaling, (c) homogeneous mean-field monotonicity, (d) stationary correlation monotonicity, and (e) fixed-time expectation monotonicity.

## 6. Numerical search protocol

For small n, enumerate all 2ⁿ configurations, build the actual random-site heat-bath kernel, verify row sums and detailed balance, symmetrize by `S=diag(sqrt(π)) P diag(1/sqrt(π))`, and compute the second-largest eigenvalue. Hold all other couplings fixed while varying one edge. Repeat near multiple eigenvalues at higher precision. Record the exact graph, rates, parameter values, solver precision, and any conditioning issue.

Numerics can reject a conjecture only when a candidate violation is certified; absence of a violation on a finite graph/sample/grid is not proof. The saved MATLAB scan is double-precision gap evidence for its finite scope. Its Shirai check uses MATLAB Symbolic Math Toolbox at 50-digit precision and cross-checks the full 16-state chain against the four-dimensional spin subspace.

## 7. General reversible-chain gap and comparison toolkit

Use the theorem matching the quantity being bounded; “spectral gap” has at least two relevant discrete-time meanings.

- For a finite irreducible reversible kernel, the Poincaré gap is `1−β₁`. Diaconis–Stroock's weighted canonical-path bound is `β₁≤1−1/κ`, with `κ=max_e Σ_{γ_xy∋e}|γ_xy|_Q π(x)π(y)` and `|γ|_Q=Σ_{e∈γ}Q(e)^{-1}`. On an unweighted simple random walk, their Corollary 1 is `β₁≤1−2|E|/(d_*² γ_* b)`. Record the actual path family and edge congestion; poor paths make the estimate weak. (W04S027, Proposition 1 / Corollary 1.)
- For worst-start discrete-time total variation, the Poincaré gap alone does not control an eigenvalue near `−1`. In a finite reversible chain, bound both endpoints, or establish laziness/nonnegative spectrum. Diaconis–Stroock's odd-return-path inequality bounds `β_min≥−1+2/ι`; the TV estimate depends on `β_* = max(β₁,|β_min|)`. Rate-one Poissonization has decay controlled by `1−β₁` and removes parity. (W04S027, Propositions 2–3.) Wübker's `0<k≤K<2` criterion gives the same warning at the level of discrete-time reversible chains: `k>0` alone misses near-periodicity; `K<2` or an independent lower-endpoint bound is needed. (W04S030, Theorem 2.)
- Cheeger bounds apply to the exact reversible form and exact isoperimetric normalization. Here `h=min_{S:π(S)≤1/2} Q(S,Sᶜ)/π(S)`, including sets with mass exactly `1/2`. Diaconis–Stroock print Proposition 6 on printed p.52 / physical p.18 as `1−2h≤β₁≤1−h²`, but the proof-supported weak estimate `h²/2≤λ₁≤2h` is equation (3.4) on printed p.56 / physical p.22; its derivation continues through equations (3.5)–(3.7), physical pp.22–24. An exact four-state reversible, irreducible, aperiodic chain in `evidence/W04/numerical/s027_cheeger_printed_bound_audit.json` contradicts the printed `h²` upper half. Treat this as a source-side inconsistency pending independent review; the skill relies only on `β₁≤1−h²/2`. Proposition 6 states finite ergodic reversibility and gives no laziness or nonnegative-spectrum hypothesis. Chen–Wang's bounds for general symmetric forms require their scaled jump/killing operator-norm condition and, in the centered inequality, `K=0`; do not substitute an unbounded form or a different denominator without checking hypotheses. (W04S027, Proposition 6 / §3C equation (3.4); W04S029, Theorems 1.1–1.2.)
- To compare two finite reversible chains, an ordinary flow compares difference Dirichlet forms, but an odd flow is needed to compare the `F(f,f)=½ΣπP(f(x)+f(y))²` form and retain control near `−1`. The mixing-time comparison also assumes ergodicity and a common stationary law in the stated theorem; different stationary laws add a variance-comparison factor. For nonreversible chains, additive reversiblization yields a Poincaré/conductance lower bound, but it does not by itself give a discrete-time upper mixing bound for the original chain. Check an auxiliary chain and the source's time convention. (W04S031, Theorems 1–2, 8, 19, 22–23.)
- Aldous's source is a finite-state ergodic continuous-time chain with transition-rate matrix `Q` and semigroup `P_t`; its `τ₁` TV threshold, exact-stationarity stopping time `τ₂`, and hitting-time parameters `τ₃,τ₄` all use this continuous-time clock. Theorem 5 compares the four quantities up to universal constants under reversibility; Theorem 6 gives the general-chain bounds with `log(1/π_min)` losses. In Proposition 8, `β` is a relaxation time with spectral decay `exp(−t/β)`, and `β≤τ₁≤β[1+½log(1/π_min)]` (printed p.566 / PDF p.3). Do not invert `β` or apply these as discrete-time step bounds; any discrete-time conversion needs an explicit rate/Poissonization and periodicity argument. Use the results as comparisons of scales, not exact constants or reversibility-free bounds. (W04S028, Theorems 5–6 and Proposition 8.)
- Aldous–Fill's selected Chapter 3 units use the Rayleigh–Ritz identity `τ₂=sup_{π(g)=0}||g||²₂/E(g,g)` (Theorem 3.25). Lemma 3.29 is a direct weighted comparison, but its printed lower expression `min_e(w_e/w_e*)/max_i(w_i/w_i*)` is not supported by its proof and is false in an exact two-state lazy-chain check. The displayed proof instead implies `min_i(w_i/w_i*)/max_e(w_e/w_e*)≤τ₂/τ₂*`; reversing starred and unstarred weights gives the printed upper bound `τ₂/τ₂*≤max_i(w_i/w_i*)/min_e(w_e/w_e*)`. See `evidence/W04/cards/W04S002.md` and `evidence/W04/numerical/s002_lemma329_lower_audit.json`. Lemma 3.32's common-π off-diagonal domination `p_ij≥δp*_ij` for `δ>0` directly implies `τ₂≤δ⁻¹τ₂*` by Dirichlet-form comparison. The source's following mixture remark additionally needs `Q` entrywise nonnegative: for `0<δ<1` this is equivalent to full-entry domination; at `δ=1` the decomposition is undefined and the endpoint identity separately requires `P=P*`. Off-diagonal domination alone does not guarantee the mixture interpretation (exact audit: `evidence/W04/numerical/s002_lemma332_mixture_audit.json`). Neither direct comparison uses path congestion. Examples 3.30–3.31 on p.94 show large relaxation-time changes are possible despite comparable total edge weight. The path-routing bound is Theorem 4.32, which requires a specified path for each ordered state pair and an edge-load calculation. Chapter 4 §4.4 starts on physical p.131 and separates continuous-time `τ₂≤τ₁≤τ₂[1+½log(1/π_min)]` from its discrete-time variant; maintain each source clock. (W04S002, §§3.6.1–3.6.4 and §4.4, physical pp.87–94 and 131–141.)
- LPW Chapter 15's high-temperature Ising path-coupling result is for the zero-field random-site heat-bath chain: `Δ tanh β<1` gives `t_rel≤n/[1−Δ tanh β]`; its even-degree improvement uses `(Δ/2)tanh(2β)<1`. Proposition 15.8 has only the exponential edge-deletion comparison `γ̃≤e^{2β(Δ+2r)}γ`. For Theorem 15.10, retain the source's printed statement `γ_B≤M²M_*(4e^{2βΔ(M+1)})γ` separately from its displayed proof: p.240 counts `4^M` block-state pairs and obtains `R≤2(n/b)M M_*4^M e^{2βΔ(M+1)}`, which with `n/b≤M` gives `R≤2M²M_*4^M e^{2βΔ(M+1)}`. The source proof's last simplification remains unsupported by those displayed estimates; this is not a theorem disproof. A separate conditional-variance/Walsh-tensorization proof establishes the stronger `γ_B≤M M_*e^{2βΔM}γ` under a finite zero-field homogeneous Ising law with `0≤β<∞`, uniform site selection, uniform selection among covering blocks, the same stationary law, and the stated discrete-time per-update clocks. R02 accepted this as a **library-derived alternate proof**, not the author's proof; see the card and bound supporting files. Do not extrapolate it to nonzero/unbounded fields, hard constraints, different stationary laws, or changed clocks. Theorem 15.13 is a low-temperature square-lattice fault-line bound. These are distinct, geometry-specific tools and do not establish arbitrary-graph edgewise gap monotonicity. (W04S001, Chapter 15, physical pp.231–247.)
- For Dyer–Goldberg–Jerrum, Lemmas 1 and 2 assume `‖R‖≤μ<1` for random-update and systematic-scan mixing, respectively; Lemma 22 separately assumes `‖R⃗‖≤μ<1` for the full-scan product. Systematic-scan time is in full scans, and multiplying by the number of sites converts to single-site updates. Do not attribute the scan-product hypothesis to Lemma 2. (W04S014, Lemmas 1–2, 22.)

### Weak-dependence and fixed-chain concentration routes

- For a finite-spin measure, Sambale–Sinulis requires both a lower bound `β̃(μ)≥α₁` over every supported one-site conditional after every partial conditioning (for full support, the minimum one-site conditional mass) and an interdependence matrix satisfying `‖J‖₂→₂≤1−α₂`. Under both conditions, Theorem 4.1 gives `ρ₀=2|I|/(α₁α₂²)` for mLSI and `σ²=log(α₁⁻¹)/(log(2)α₁α₂²)` for LSI; Theorem 2.2 gives entropy decay `exp(−α₁α₂²t/(2|I|))` for the random-site kernel. The paper's continuous-time generator is `P−I` (total update rate one); per-site-rate-one time scales rates by `|I|`. These are sufficient fixed-family estimates, not a general Ising theorem. (W04S032, Theorems 2.2 and 4.1.)
- Paulin's inequalities are for a fixed stationary discrete-time chain: keep reversible gap `γ`, absolute gap `γ*`, and nonreversible pseudo-gap `γps` distinct. Proposition 3.3/3.4 relate those quantities to mixing; Theorem 3.9's reversible Bernstein statement requires bounded centered summands and either finite state space or even sample length, while Theorem 3.11 uses `γps>0`. Theorem 2.9/Corollary 2.11 use Marton coupling and a mixing-time parameter for functions of a trajectory. These bounds can turn already established fixed-chain mixing/gap control into concentration; they do not compare gaps between Ising parameter vectors. Use the corrected arXiv v5 proof and its own physical-page numbering for the general-state Bernstein result. (W04S033.)

These results are general chain tools. They provide lower bounds or comparisons for a fixed kernel; none orders the gaps of two Ising systems solely because one edge coupling is larger.
