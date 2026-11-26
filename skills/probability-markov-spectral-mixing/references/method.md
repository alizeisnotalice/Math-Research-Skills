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

### GKS and switching-method boundary

This candidate does not admit a GKS/GHS or random-current/switching-lemma proof route. W04S009–S010 are unread metadata records; no GKS theorem is high-scoped in this source aggregate. The accepted G04.01 rows cover the stated FKG/Holley/higher-spin association interfaces only. A static positive-correlation theorem, even when available from another source, does not establish a semigroup or gap inequality.

Neither GKS nor FKG is a theorem about a finite-time transition operator, its eigenvalues, or its spectral gap. An equilibrium derivative identity such as `d/dJ_e E_π[F] = Cov_π(F,σ_uσ_v)` is not a gap-derivative formula.

## 5. A040 evidence boundary

The arbitrary finite-graph, zero-field, inhomogeneous edge-monotonicity question remains unresolved by this candidate. The high-scoped sources establish narrower facts: Nacu's zero-field cycle derivative for positive edge couplings (W04S003); Kargin's homogeneous zero-field complete-graph branch (W04S004); and Shirai's fixed-time single-spin expectation counterexample on a graph containing a length-3 path (W04S005). Kargin's nonzero-field proof step is not admitted, and Shirai does not refute the spectral-gap claim. LPW Chapter 26 is present in the historic reading record, but is outside W04S001's accepted Chapter 12 source-use row.

Keep separate: (a) edge-addition monotonicity on arbitrary graphs, (b) common-temperature scaling, (c) homogeneous mean-field monotonicity, (d) stationary correlation monotonicity, and (e) fixed-time expectation monotonicity. The current accepted-use register does not turn one into another.

## 6. Numerical search protocol

For small n, enumerate all 2ⁿ configurations, build the actual random-site heat-bath kernel, verify row sums and detailed balance, symmetrize by `S=diag(sqrt(π)) P diag(1/sqrt(π))`, and compute the second-largest eigenvalue. Hold all other couplings fixed while varying one edge. Repeat near multiple eigenvalues at higher precision. Record the exact graph, rates, parameter values, solver precision, and any conditioning issue.

Numerics can reject a conjecture only when a candidate violation is certified; absence of a violation on a finite graph/sample/grid is not proof. The package contains row-bound finite scripts and outputs in `evidence/math_case_manifest.json` (earlier archive), plus R01 exact convention checks for clocks, pinning, the absolute-gap endpoint, and one simple moving-eigenvalue branch. These are finite examples only, not proof of an all-graphs statement.

## 7. General reversible-chain gap and comparison toolkit

Use the theorem matching the quantity being bounded; “spectral gap” has at least two relevant discrete-time meanings.

- For a finite irreducible reversible kernel, the Poincaré gap is `1−β₁`. Diaconis–Stroock's weighted canonical-path bound is `β₁≤1−1/κ`, with `κ=max_e Σ_{γ_xy∋e}|γ_xy|_Q π(x)π(y)` and `|γ|_Q=Σ_{e∈γ}Q(e)^{-1}`. On an unweighted simple random walk, their Corollary 1 is `β₁≤1−2|E|/(d_*² γ_* b)`. Record the actual path family and edge congestion; poor paths make the estimate weak. (W04S027, Proposition 1 / Corollary 1.)
- For worst-start discrete-time total variation, the Poincaré gap alone does not control an eigenvalue near `−1`. In a finite reversible chain, bound both endpoints, or establish laziness/nonnegative spectrum. Diaconis–Stroock's odd-return-path inequality bounds `β_min≥−1+2/ι`; the TV estimate depends on `β_* = max(β₁,|β_min|)`. Rate-one Poissonization has decay controlled by `1−β₁` and removes parity. (W04S027, Propositions 2–3.) For the L01 Wübker use, only the all-nontrivial-cut two-step criterion `k₂>0` is retained for a centered fixed-kernel two-sided gap; its Eq. (4) strict-half `k` and Eq. (6) all-cut `k_n` definitions are not silently identified on finite atomic spaces, and Eq. (13) is not used as a quantitative certificate. (W04S030, Corollary 1.)
- Cheeger bounds must use the exact reversible form and cut normalization. For W04S027, use only proof-supported `h²/2≤λ₁≤2h`; the stronger printed `h²` upper half is not used. W04S029 contributes only Theorem 1.2 inequality (1.11), with finite conservative reversible generator, verified maximum exit rate `M`, minimum-mass cut `k′`, and no killing; retain `gap≥M(1−√(1−(k′/M)²))≥(k′)²/(2M)`. The product-mass substitution and general unbounded-domain claims are outside the admitted interface.
- W04S031 contributes Theorems 1–2 only: the exact routed-demand ordinary flow compares `E`; an odd flow additionally compares `F` and controls the negative spectral endpoint. Preserve the common-law/ergodicity conditions stated in the source row. No nonreversible conductance upper-mixing theorem or other theorem route is approved by this row.
- Aldous’s finite-state continuous-time source contributes only Proposition 8 to this stage: `β` is the relaxation time, and `β≤τ₁≤β[1+½log(1/π_min)]` at its stated threshold (W04S028). Keep the original rate clock; this does not approve its broader Theorem 5–6 comparison or a discrete-time conversion.
- Aldous–Fill (W04S002) contributes only selected Chapter 3 §§3.6.1–3.6.4: the Rayleigh–Ritz identity (Theorem 3.25), CT contraction/comparison, and Lemmas 3.29/3.32 under the exact row scope. For Lemma 3.29 use only the proof-derived corrected two-sided weight bounds, not the source-printed lower factor; the exact two-state audit is in `evidence/W04/numerical/s002_lemma329_lower_audit.json`. Lemma 3.32's Dirichlet comparison uses common `π` and `δ>0`; its mixture interpretation additionally needs a full-entry nonnegative residual, and at `δ=1` the identity case is separate. The selected Chapter 4 §4.4 reading unit is historical reading coverage and is outside the current accepted source-use row. (W04S002, physical pp.87–94.)

- LPW (W04S001) contributes only Chapter 12 §§12.1–12.2 in the current high-scoped row: Lemma 12.2's symmetric conjugation/L²(π) representation and Theorems 12.4–12.5's discrete-time absolute-gap mixing bounds. The older reading record includes Chapter 15 and Chapter 26, but those uses are not high-scoped in this candidate; do not import its Ising path coupling, edge-deletion, block-comparison, fault-line, or open-question claims as active source methods.
- Sambale–Sinulis (W04S032) contributes the accepted full-support entropy/mLSI interface only. Keep the all-partial-conditionals lower bound, interdependence norm, total-rate-one random-site kernel, and size-uniform constants where an `O(n log n)` consequence is claimed. Ordinary LSI/higher-order concentration and hard-constraint support changes are outside this row.
- Paulin (W04S033) contributes only Theorem 3.5 equations (3.14)/(3.16) for stationary fixed-kernel variance. The chain starts at `π`, the observations are at discrete times, and the fixed/varying cases use `γ`/`γ_abs` respectively; Bernstein, Marton and other concentration results remain outside this row.

## Current source-method coverage boundary

The exact 37-row source-to-method associations are listed in `method_coverage.md`（本机附件：`references/method_coverage.md`）. They are limited to G03.01–G03.05 and G04.01. G04.01 means the admitted FKG/Holley/higher-spin association rows only; it does not certify GKS wholesale. G04.02 and G04.03 have no current high-scoped source association. The reviewed critical FK-Ising/RSW input in W04S020 is a dependency, not an admitted general G04.04 source row. The finite G03.06 Sturm/LDL certificate is separately DERIVED and has an explicit Jacobi restriction.
