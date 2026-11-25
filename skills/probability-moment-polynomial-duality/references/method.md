## Entry point: select the finite model before choosing a theorem

| Data and target | Admitted route | Check before use |
| --- | --- | --- |
| Labeled Boolean event under k-wise Bernoulli constraints | G13.01 finite cube mass LP; degree-at-most-k pointwise majorant/minorant | Include every subset moment through k; keep the product reference, output coding, and objective direction explicit. |
| Symmetric all-ones event on one exchangeable block | G13.01 count LP, with G13.03 Krawtchouk or adjacent-pair tools under their named hypotheses | Symmetrize the feasible class and objective; positivity is on the integer grid. PYY, BEKK, and Hermann conditions are not interchangeable. |
| Function of partitioned event counts | G13.02 product-grid moment LP and G13.04 binomial-basis dual | Retain every supplied mixed moment; verify the dual on the full grid; prove a labeled lift before claiming exactness. |
| Only aggregate or selected event intersections are known | Source-specific G13.01 count LP or G13.04 finite inclusion-exclusion/thinning certificate | Use only the exact summary rows and parity/order conditions; do not infer unobserved intersections. |
| Arbitrary dependence with fixed finite discrete marginals | G13.01 full product-support atom LP and marginal-indicator dual | Keep normalization, every marginal row, and dual inequalities on event and complement atoms. |
| Bounded product factors under k-wise independence | G13.04 approximate expectation or symmetric-polynomial tail component | State support, variance, independence order, and threshold conditions; this does not provide a pointwise sandwich or tree recursion. |
| Tensor moments on a tree or stable multilevel recursion | Not covered here; G13.05/G13.06 remain open | A direct source/proof must define node messages, cross-child moment closure, conditional independence order, and a quantitative error recurrence. |

For finite support Omega, moment rows h_j, and objective g, include normalization explicitly as h_0≡1, b_0=1, and write q_x >= 0 with sum q_x = 1 and A q = b. A maximization dual certificate is phi(x)=lambda_0+sum_j lambda_j h_j(x) with phi(x) >= g(x) at every x in Omega; then E_Q g <= lambda_0+sum_j lambda_j b_j. A minimization lower certificate reverses the pointwise inequality. A dual-feasible certificate gives a bound. Sharpness requires a matching feasible primal law attaining that same value, or a proof that this certificate attains the dual optimum together with strong duality for the specified primal/dual pair.

### Family-level coverage state

| Method | Entry status | Supported scope |
| --- | --- | --- |
| G13.01 | Scoped coverage | Finite event/count moment LPs, finite-cube k-wise LPs, selected finite-marginal atom LPs, and named finite-grid moment projections. |
| G13.02 | Scoped coverage | Exchangeable or partitioned count LPs with all supplied mixed moments; no generic reverse label lift. |
| G13.03 | Narrow scoped coverage | One-block Krawtchouk/count-basis and even-k adjacent-pair reflection results only under each source's exact assumptions. |
| G13.04 | Scoped coverage | Pointwise finite-grid polynomial certificates, named union/Bonferroni/thinning formulas, and bounded-factor low-degree expectation-error auxiliaries. |
| G13.05 | Uncovered | No admitted source proves tensor-moment closure with tree-shaped message recursion. |
| G13.06 | Uncovered | No admitted source proves the targeted multilevel stability/error propagation. |

The R07 source-use index supplies exact source IDs, versions, accepted theorem interfaces, conditions, transfer limits, and review hashes. Root-wide work-family deduplication remains pending.

# Method and scope notes

## Finite k-wise-independence LP

For `X∈{0,1}^n` with product reference `P_p`, let `A(n,k,p)` be the laws whose every marginal on at most `k` coordinates is iid Bernoulli(p). Use variables `q_x=Q(X=x)`. Include normalization, nonnegativity, and the all-one constraints `E_Q∏_{i∈S}X_i=p^{|S|}` for every `S⊆[n]`, `|S|≤k`. For binary variables these all-one moments determine every zero/one pattern on the same subset by inclusion-exclusion.

For an event `f:{0,1}^n→{0,1}`, maximize/minimize `E_Q f`. The BGP finite-cube dual is respectively the product expectation of a pointwise degree-≤k majorant and minorant. Keep each direction visible. A source theorem's strong LP equality is not a theorem about a truncated univariate moment problem unless its moment map and support are the same.

## Block-count reduction

Suppose a group permuting coordinates within each block preserves both the constraint class and objective. Average a feasible law over that group. For blocks `b=1,…,r` of sizes `m_b`, define `S_b=Σ_j X_{b,j}`. Expanding a product of falling factorials counts ordered tuples of distinct coordinates in each block, so k-wise independence implies

`E∏_b (S_b)_{a_b}=∏_b(m_b)_{a_b}p^{a_1+⋯+a_r}`, for `0≤a_b≤m_b` and `Σ_b a_b≤k`; terms with `a_b>m_b` are vacuous zero constraints.

These mixed constraints—not just powers of `S_1+⋯+S_r`—retain interactions across blocks. Under within-block exchangeability, each fixed subset's all-one probability equals the corresponding mixed factorial moment divided by `∏_b(m_b)_{a_b}`; inclusion-exclusion recovers all patterns. Without the symmetry, the averaged count constraints are necessary but may not be sufficient for labeled k-wise independence.

The saved exact witness uses two size-2 blocks. It constructs a law with the same complete total-count distribution as iid Bernoulli(1/2), but a different `E[S_1S_2]` and hence a different fixed cross-block pair probability. This is finite numerical evidence for why the constraint set must be explicit; the general identity above is a separate derived proof.

## K2 and threshold limits

In BGP, `ε_f(k,p)` is the spread of the event probability over all laws in `A(n,k,p)`. For a sequence of monotone sharp-threshold Boolean functions with critical point `p_c`, `K_2` is formally a class of functions `k(n)` such that the spread at `p_c` tends to zero. A two-level estimate or a finite LP does not by itself prove an iterated-majority recursion, a uniform depth bound, or convergence of a family of LP optima.

## G14 handoff to the Boolean skill

Route Walsh normalization, output coding, singleton coefficients, dependence, influence, and Fourier support to the existing probability-boolean-fourier-invariance skill. Under its normalized Walsh convention, total influence for a {0,1}-valued function is four times the degree-weighted Fourier mass. A nonzero singleton coefficient proves dependence on that coordinate; dependence on every coordinate can come from higher-level terms. Its W10 source ledger and reviewed addressing context remain in that skill. This G13 skill uses these distinctions only to prevent an invalid step from bounded marginal moments to a Fourier or sign conclusion.

DKN is a boundary example: its degree-2 Boolean-cube theorem needs the exact independence order and, in the regular branch, the source regularity, smoothing and anti-concentration route. A Gaussian-coordinate result is a different model.

## Scope split and unresolved interfaces

G13 is the proposed core. G14 is a precise handoff to the existing Boolean Fourier skill, not an additional method family covered here. G15 is uncovered/routed: no support-isolation, Freiman, additive-energy or inverse Littlewood–Offord method is claimed without a direct Boolean finite-support bridge. A141 (random disjoint witnesses in UST), A175 (arbitrary nonnegative-real PGF factors), and A199 remain conditional/outside routes. A164 (monotone and depends on every coordinate) is not A165 (every singleton coefficient nonzero). A166 uses nonzero input support, not Fourier support, and signed weights allow cancellation.



## One-block exchangeability and its limits

For the symmetric all-ones objective on a single Bernoulli cube, coordinate averaging is valid because both the k-wise class and objective are permutation invariant. The exchangeable law is represented by `S=Σ_i X_i`; its support is the integer grid `{0,…,n}` and its first k moments match `Bin(n,p)`. The primal is a finite mass LP; its exact dual is degree at most k, nonnegative on the integer sites `0,…,n−1`, and at least 1 at `n`. Complementary slackness supplies the support/zero relation. This reduction and converse lift are specific to one full symmetric block; do not replace a multi-block vector by the total count. See PYY（本机附件：`evidence/localized_markdown/2c8b0f6f4b43fb92_EXSRC-b7060e8a46c8c70d.md`）, physical pp.8–10 and p.29.

For even k, PYY's continuous-support relaxation changes `{0,…,n}` to `[0,n]`, so it is an upper bound on the discrete maximum. Its dual positivity domain is an interval. The source proves equality of the relaxation optimum and a restricted square optimization; the feasible polynomial sets are not equal, and a general nonnegative interval polynomial need not be a single square. Its square/Krawtchouk expression belongs to that relaxed problem. PYY's lower comparison theorem requires even k, `0<p<1`, `N=np(1−p)−1`, and `k≤c₁N`, with loss `(c₃/k)exp(−c₂k/V(N/k))`; it does not give an exact answer throughout the middle parameter range. BEKK gives exact formulas on named intervals. Isolate Corollary 2.4's high-p parity branch, Theorem 2.7(2)'s k=2 lower endpoint, and Proposition 3.2's equality parity; use the explicitly labeled R04 reviewer-derived corrections from the local card rather than attributing corrected formulas to the article. The adjacent-pair basis structure is a dual-feasibility condition; equality still requires nonnegative primal basic weights. Numerical basis patterns in BEKK's final section remain conjectures. See BEKK（本机附件：`evidence/localized_markdown/29935bd4997d0457_EXSRC-a425d22da6d4eb7c.md`）, physical pp.6–14, 21–35, and 35–43.

## Multivariate discrete-moment polynomial certificates

If counts have known finite product support and a linear objective, write the full product-support mass LP and keep the supplied mixed-moment map explicit. In binomial coordinates the constraints are `E[∏_b C(S_b,a_b)]` for the actual multi-indices provided by the model. For a candidate basis, construct its Lagrange interpolant and verify pointwise domination at every support point. A dual-feasible basis gives a one-sided expectation bound; claim sharpness only after checking primal feasibility. Mádi-Nagy–Prékopa's multivariate residual is a sum of two terms. For Theorems 4.1–4.3 require both nonnegative total-order `(m+1)` divided differences and, in every coordinate `z_j`, nonnegative divided differences of order `m+|K_j|`; reverse the resulting inequalities when these specified differences are nonpositive. Eq. (4.1) defines `K_j` from adjacent pairs `{u^(j),u^(j)+1,…,v^(j),v^(j)+1}`: min/even is pairs only; min/odd adds `{m}`; max/even adds `{m,n_j}`; max/odd adds `{n_j}`. The pair indices make the displayed set a subset of `{m,…,n_j}` with the stated parity. Theorem 4.1 is ascending/min and gives a lower bound. Theorem 4.2 uses descending order and direct `K_j`: for `m+1` even, max/even or min/odd gives a lower bound; for `m+1` odd the same structures give an upper bound. Theorem 4.3 is general-`s`, ascending, and uses Eq. (4.1) for `n_j−K_j` (even: max; odd: min), with the same `m+1` parity directions. Only the §5 Min/Max algorithms are bivariate. To claim sharpness for a candidate interpolant, exhibit a feasible primal law attaining the same objective value, or prove that the interpolant is dual-optimal and invoke strong duality for this exact finite LP. The source's coordinate-axis convexity does not imply convexity along arbitrary oblique directions. See Mádi-Nagy–Prékopa（本机附件：`evidence/localized_markdown/e6a8ee27a8b5d0c3_EXSRC-d869e24ff9bec2ff.md`）, physical pp.1–17 and 18–21.

This source interface bounds objectives over a finite discrete moment class; it does not by itself show that a proposed block-count law lifts to the labeled Boolean cube. Prove within-block symmetrization and the mixed falling-factorial identities, or keep the count problem only as a relaxation. Do not import generalized continuous moment/SOS theorems into the Boolean cube without matching support, objective, and moment assumptions.

## Current source status

R07 has accepted 30 source-scoped uses in the current L07 admission exports; 30 source IDs and 30 lane-local work-family IDs are distinct within those exports. Root-wide identity/version reconciliation and quota export remain pending. Source-use acceptance does not certify ancillary formulas or approve whole-skill publication; see the source ledger and R07 use index.


## Partial-moment event LPs and general finite-grid duals

When the available information is only `P(A_i)` and `Σ_{j≠i}P(A_i∩A_j)`, Yang–Alajaji–Takahara's `a_i(k)` model gives an exact achievable lower union bound in that information class: minimize `Σ_{i,k}a_i(k)/k` with the per-event zeroth/first count moments and the all-`j,k` coupling inequalities. This does not encode all individual intersections or arbitrary higher Boolean marginal constraints. For pairwise-independent Bernoulli vectors, Ramachandra–Natarajan instead keep all labeled one- and two-coordinate equalities on the cube; their degree-two dual is valid pointwise on `{0,1}^n`. Only the identical-marginal symmetric objective permits the paper's exact count-mass reduction and uniform lift.

For a finite rectangular lattice `Z_1×…×Z_s` with known cross-binomial moments, Prékopa writes the full atom-mass LP and certifies a bound using a Lagrange interpolation polynomial. The multivariate divided-difference sign conditions are objective- and support-specific; dual feasibility gives a bound, and primal feasibility is still needed for sharpness. The event-specific intersection-of-unions result keeps every mixed binomial moment of total order `≤m`; the reviewed Bonferroni parity bound is used only under `m≥s` and uses the parity of `m+1−s`. In a Boolean block-count application, first prove the exchangeable lift and retain the entire mixed factorial-moment vector; these generic discrete-moment theorems do not supply that lift.


## Accepted revision9 finite-event and shape-constrained interfaces

These three source uses were accepted by R07 for the specific interfaces below. This section supplements the revision10.1 baseline; it does not replace its Boolean k-wise, block-lift, K2, or G14/G15 routing rules.

### Weighted partial pair summaries: Yang–Alajaji–Takahara

For a finite event family, inputs are each `alpha_i=P(A_i)` and the weighted pair row `gamma_i=Σ_j c_j P(A_i∩A_j)`. Require `c(B)=Σ_{j∈B}c_j≠0` for every nonempty atom `B`. Allocate each nonempty atom across its member events with `c_i/c(B)`. For each i, minimize its allocated contribution over a separate nonnegative local LP constrained by its marginal and weighted pair row, then sum the local minima. The actual joint atom law is feasible in every local problem, and each atom’s allocations sum to one, so the sum is a valid lower bound on the union probability. Separate local minimizers need not glue into one joint law.

This is a finite G13.01 moment-LP certificate from partial weighted pair information. Positive-weight algorithmic complexity claims are separate and apply only under the source conditions; this skill uses the finite LP interface and does not claim arbitrary signed-weight runtime. It does not recover all individual pair intersections or imply a k-wise Boolean lift. See the accepted scoped-use snapshot（本机附件：`evidence/current_conditions/EXSRC-af32da40ba0698e8.json`）.

### Count, atom, and block-count moment LPs: Prékopa–Vizvári–Regős–Gao

For a finite event count `nu=Σ_i 1_{A_i}`, write `S_k=E binom(nu,k)` and put a mass on each count `0,…,n`; the dual polynomial must be one-sided on every integer support point. If individual intersections `p_I` are available, a separate Boolean atom LP uses `Σ_{J⊇I}v_J=p_I`. If only partitioned block counts `X_1,…,X_s` are retained, keep **every supplied mixed moment** `S_alpha=E∏_j binom(X_j,alpha_j)` of total degree `|alpha|≤m`. The dual is `q(x)=y_0+Σ_{0<|alpha|≤m}y_alpha∏_j binom(x_j,alpha_j)` and must satisfy its one-sided inequality at every product-grid point, including the origin.

The paper establishes a chain of bounds and stated optimum-value relations between formulations. Do not infer equality of feasible sets from those relations or claim a general reverse lift from block counts to prescribed heterogeneous labels. When a Boolean k-wise application is intended, first prove the within-block symmetrization/lift and retain all cross-block mixed constraints. The block-count LP alone is a partial-information relaxation. See the accepted scoped-use snapshot（本机附件：`evidence/current_conditions/EXSRC-c492142f2878aea0.json`）.

### Known finite-support shape constraints: Subasi–Subasi–Prékopa

For a count law `p_i=P(xi=i)` on `{0,…,n}`, solve the finite moment LP with `Σ_i binom(i,j)p_i=S_j` for `j=0,…,m`, `p_i≥0`, and the requested tail or point-mass objective. Add shape only when it is independently known. For a supplied mode `k`, impose all original-variable inequalities `p_0≤…≤p_k≥p_{k+1}≥…≥p_n`; `k` is fixed and known. For a complete LP certificate, a pointwise bound on every original count site is valid with shape multipliers set to zero. If the certificate uses shape rows Gp≥0, use the correct signs: a lower certificate has c=Aᵀy+Gᵀz, and an upper certificate c=Aᵀy−Gᵀz, with z≥0.

The paper’s successive-difference parameterization may be used only with its full constraints. In the known-mode split representation this includes the bridge `Σ_{i≤k}v_i≥Σ_{i>k}v_i`. Omitting it is not equivalent. The printed split-difference/closed-form branch is not used here; no m=2 formula is imported without checking its displayed primal feasibility conditions. The audited safe interface is the original-p finite LP and its exact primal/dual certificate. See the accepted scoped-use snapshot（本机附件：`evidence/current_conditions/EXSRC-f3f334daabbbce21.json`）.

### Exact checks kept with the reader evidence

The source-use positive and missing-condition cases are recorded in positive examples（本机附件：`evidence/project/expansions/20261115/readers/L07/revision16_1/skill_snapshots/probability-moment-polynomial-duality/examples/positive.md`） and negative examples（本机附件：`evidence/project/expansions/20261115/readers/L07/revision16_1/skill_snapshots/probability-moment-polynomial-duality/examples/negative.md`）. The exact n=4 known-mode example and difference-model relaxation are reproduced in `l07_r9_exact_shape_lp.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision9_1/math/l07_r9_exact_shape_lp.py`） and `R07_shape_bridge_check.out.json`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision9_1/math/R07_shape_bridge_check.out.json`）. For the 2008 source’s original-p safe core, supply the mode and retain all adjacent inequalities and any bridge used by a transformed model. A pointwise majorant at every original site remains valid with zero shape multipliers. The tail interval `[6/25,19/50]` is a derived objective; the independently checked source-union example is `[43/50,24/25]`.


## Revision11 scoped interfaces: finite event-count moments and event LPs (R07 accepted)

The revision11 batch documented eight complete reads with source-scoped uses later accepted by R07. Subsequent correction snapshots preserve those reads and tighten card conditions; this revision16 integration adds no source reads or source-use decisions. The baseline rules on complete mixed cross-block constraints, K2, Boolean Fourier handoff, and G15 routing remain in force.

### Refined inclusion–exclusion from low-order event data

For a finite event family and count X, write S_j=E binom(X,j); verify indicator identities at every x∈{0,…,n} before taking expectations. The Adler–Karp–Ross Theorems 1–4 give parity-directed finite truncations, with the exact residual bound requiring the named additional moment or labeled intersections. Theorem 5 uses ranked (k+1)-fold joint-intersection probabilities extending each fixed k-subset, averaged over orderings; these are not conditional probabilities obtained by dividing by the prefix intersection. Its one-sided union-bound direction follows the theorem’s parity conditions. R07 accepts these scoped interfaces with the theorem-specific r,k ranges and input requirements. Isolate its physical-p.7 table values 0.1896/0.7871: the exact formula outputs correction 129023/1250000 and lower bound 437949/625000 for that display, while the product law gives union 1197392257/1562500000 and remainder 263798507/1562500000. See the corrected card（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/cards/EXSRC-8bbf4cf5c3ac0b5b.md`） and R07 review（本机附件：`evidence/reviews/20c2e01fe03168e3_EXSRC-8bbf4cf5c3ac0b5b.review.json`）.

### Finite count LPs with supplementary information

When the objective and constraints depend only on N=Σ_i1_{A_i}, use masses p_0,…,p_n with normalization, supplied moments, tail caps, and any independently known shape rows. A dual pointwise bound on every grid site may set shape multipliers to zero; when using shape rows, use correct-sign nonnegative multipliers. Hoppe–Nediak gives a sharp finite normalized LP with aggregate mean plus tail cap. Prékopa–Subasi–Subasi gives a complete original-variable LP for a separately supplied mode; its transformed forms retain explicit bridge rows. Do not infer mode from mean. Conditional uniform-subset lifting realizes exchangeable count data, not arbitrary labeled marginals.

### Convex-hull geometry of count moments

For fixed finite support {0,…,n}, the vector of expectations of specified functions f_1,…,f_s is exactly the convex hull of their grid-value vectors. This gives a finite feasibility test and sharp moment projection after the convex hull is computed. It does not imply a closed form for arbitrary coordinates, nor does it preserve unrecorded cross-block/labeled moments. Móri–Székely is a candidate foundational finite-grid result; one exact n=4 slice is computed in the local math evidence.

### k-wise count-LP support reflection

For one permutation-invariant block with common Bernoulli(p) k-wise constraints, even 2≤k≤n−1 and 0<p<1, Hermann’s Theorem 1 reflects the displayed adjacent-pair basis I=J∪{n}. The paired weight factor is p(n−s)/((1−p)(s+1)); every basic weight must be nonnegative for feasible support. This is interior basis/support feasibility, not equality of the optimal objective at p and 1−p, and it does not cover odd k, arbitrary bases, multiple blocks, or unsymmetrized laws. See the corrected card（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/cards/EXSRC-f8669d7cb4c3980d.md`） and R07 review（本机附件：`evidence/reviews/60273fde64aeb163_EXSRC-f8669d7cb4c3980d.review.json`）.

### Labeled partial-intersection LP and projection strengthening

With labeled intersections through order m, keep the atom LP or a rigorously projected relaxation. Qiu–Ahmed–Dey uses two scales: unscaled u_{ij}=P(μ=i,X_j=1) and main-text scaled v_{ij}=u_{ij}/i. Under the scaled convention, keep p0+Σ_{i≥1,j}v_{ij}=1, moment rows Σ_{i≥t}C(i,t)v_{ij}=s_t^j/t, and the corresponding tail objective Σ_{i≥k,j}v_{ij}; the unscaled forms are respectively the s_t^j rows with C(i−1,t−1)u and objective Σu/i. Fixed-layer projection cuts are homogeneous, with separate n−1/n boundaries. SPAM strengthens but is not generally exact. Kaski–Mannila–Mohapatra give a critical computational boundary: for feasible rational partial-intersection input with sets of size≤2, each generic union endpoint optimization is NP-hard. Do not transfer this to symmetric count LPs, weighted aggregate models, or every special case. See the corrected Qiu card（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/cards/EXSRC-4325834dadfe0555.md`） and R07 review（本机附件：`evidence/reviews/9eedd963e1e074af_EXSRC-4325834dadfe0555.review.json`）.

### Adjacent PGF route, not a polynomial-dual shortcut

Móri (1996) supplies an accepted concrete G13.04 transport: independent event thinning maps a universal finite-degree one-sided polynomial certificate for the no-event indicator to a certificate for z^N, multiplying each subset-M coefficient by (1−z)^|M| without increasing degree. It preserves direction and requires the original named intersections. The separate coefficient-comparison theory does not enter this scope; uniform PGF/coefficientwise closeness alone does not imply total variation without summable/tail control. See the corrected card（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/cards/EXSRC-214cc090409e7434.md`）.

### Exact checks and scope

The revision11 exact rational check is `l07_rev11_exact_checks.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision11/math/l07_rev11_exact_checks.py`）, with its saved run output `l07_rev11_exact_checks.run.json`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision11/math/l07_rev11_exact_checks.run.json`）. They verify finite examples and small generator sets only. Every general result above still depends on its source proof and conditions.


## Revision12 candidate: multivariate disaggregation of event-count moments

For a finite event family partitioned into blocks E_j, define ξ_j=Σ_{i∈E_j}1_{A_i} and retain every supplied mixed binomial moment S_α=E∏_j binom(ξ_j,α_j) through the stated total order. Expanding the product counts distinct event selections in each block, so S_α is the sum of the corresponding labeled joint-intersection probabilities. Prékopa–Vizvári–Regős formulates a product-grid count LP and binomial-basis dual polynomials; the method places a selected block-count relaxation between fully aggregated moments and the fully labeled atom model. Theorem 4.1 gives sufficient dual-feasibility bases when m≤n_j and all total-order (m+1) divided differences have the stated common sign. It does not characterize all optimal bases.

For a proposed normalized product-grid certificate, include every supplied index 0≤|α|≤m, in particular α=0 with S_0=1 and y_0, and check Q(z)=Σ_|α|≤m y_α∏_jC(z_j,α_j) at every lattice site including the origin. The report’s positive-degree/nonzero-site Eq. (22) alone is not the normalized dual; physical p.13 Eq. (23) and its paragraph explicitly assign any constant term to S_{0,…,0}=1. Theorem 4.1 gives a sufficient corner-basis route; construct its interpolant from the actual nonsingular system and verify the full grid. Do not implement the printed physical-p.17 Eq. (29) or later misnumbered special displays. See the corrected PVR card（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/cards/EXSRC-735090b4fe10dedc.md`） and R07 scoped conditions（本机附件：`evidence/current_conditions/EXSRC-735090b4fe10dedc.json`）.

An exact two-block size-2 example is in `l07_pvr_1998_exact_block_moments.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/math/l07_pvr_1998_exact_block_moments.py`）: two count laws have the same full Bin(4,1/2) total-count distribution but different E[ξ_1ξ_2]. This demonstrates why matching total-count moments does not encode all cross-block constraints. The report recommends searching over partitions for the strongest bound, but its numerical work uses only a few trial partitions; do not claim global partition optimality unless that search is actually carried out. R07 accepted this scoped LP/dual use. Root-wide reconciliation of the current 30 lane-local work-family records remains pending.


## Revision15.1: bounded-independence product approximation (R07 accepted G13.04 auxiliary use)

For finite-support factors `X_i∈[-1,1]` with means `μ_i`, variances `σ_i²`, and `σ²=Σ_iσ_i²`, Gopalan–Yehudayoff Theorem 1.1 gives under any k-wise law `|E_D∏X_i−∏μ_i|≤(c₁σ)^(c₂k)` for existential absolute constants `c₁>1`, `0<c₂<1`; if `σ<1/(2c₁)`, order `O(log(1/δ))` suffices for error δ. This is an approximate expectation-error ingredient for low-degree approximation (G13.04), not a pointwise sandwich, finite LP dual, or tensor/tree recursion.

For centered finite-support `Z_i`, integer `m≥1`, `0<σ_Z²=Σ Var(Z_i)<1`, `(2m+2)`-wise independence, `t>0`, and `16etσ_Z<1`, Theorem 1.6 gives `Pr[Σ_{ℓ=m}^n|S_ℓ(Z)|≥2(8etσ_Z)^m]≤2t^(−2m)`. If `σ_Z²=0`, all centered coordinates are deterministic zero and the tail is handled directly. Do not infer an expectation bound for the high-degree absolute tail.

For the product proof route, use the reviewer-derived sufficient original independence order `12m`: after conditioning on fewer than `2m` head coordinates, at least `10m` remains; the tail bound at index `4m` uses `8m+2`, the squared truncated polynomial uses `8m`, and expectation matching of the degree-`4m` polynomial alone uses `4m`. This safe budget is a reviewer derivation, not a claim of the theorem’s minimal order. Do not assert the isolated printed Claim 4.2 under only `4m` independence. Precise locators and scope are in the corrected card（本机附件：`evidence/localized_markdown/401f8c3ef1cd79ab_EXSRC-2a57ae3cd3e6d02e.md`） and R07 conditions（本机附件：`evidence/current_conditions/EXSRC-2a57ae3cd3e6d02e.json`）.

## Revision15.1: extremal finite-marginal atom LP (R07 accepted G13.01 scope)

When only discrete one-coordinate marginals are specified and dependence is unrestricted, let `θ(c)` be a nonnegative mass on each point of the finite product support `C=∏_i C_i`. Impose `Σ_c θ(c)=1` and every marginal equality `Σ_{c:c_i=a}θ(c)=p_i(a)`. For a fixed finite nonempty `X` and `Z(c)=max_{x∈X}cᵀx`, maximize `Σ_cθ(c)1{Z(c)≥r}`. The normalized finite atom primal is on physical p.4 of the read source (unnumbered). Its dual, physical p.5 Eqs. (2.1)–(2.2), minimizes `λ+Σ_{{i,a}}α_{{i,a}}p_i(a)` with `λ+Σ_{{i,a}}α_{{i,a}}1{{c_i=a}}≥1` on event atoms and `≥0` on every product-support atom. Finite strong duality gives equality of optima; a matching primal/dual pair proves sharpness.

R07 accepted only this G13.01 normalized atom LP and its full-domain marginal-indicator dual. The compact V-polytope/Bernoulli/PERT formulas and all samplers, complexity claims, weighted convolutions, and numerical plots remain outside this admission. The exact three-bit primal/dual example and excluded directions are in the corrected card（本机附件：`evidence/localized_markdown/d798215f00bd451d_EXSRC-835ff2bde42fd431.md`）.


## Prior-hold boundary

The L07 prior-hold disposition excludes the W10/L04 decomposition and anchor findings from G13, G14, G15, and quota use. This skill imports none of those findings as positive evidence. The origin-anchored interpolation basis in a finite-grid moment theorem is admitted only with that source's finite support, full moment map, and pointwise grid inequality; it is not a general anchor repair for an absolute process supremum. Do not transfer VC, decomposition, or anchor conclusions outside their source hypotheses, and do not use them as a substitute for cross-block moment rows or a proved tree-message recursion.
