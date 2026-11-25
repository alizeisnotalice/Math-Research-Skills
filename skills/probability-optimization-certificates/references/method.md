# Method: optimization bounds as proof certificates

## 1. Fix the exact model first

Write the finite optimization problem in a canonical sign convention and retain the original constraints beside any transformed model. Record:

- objective direction (minimize or maximize), all variable domains, and whether data are rational, real, interval-valued, or estimated;
- inequality directions and multiplier signs, equality multipliers, cone and dual-cone conventions;
- whether the target is a feasible point, an upper/lower bound, optimality, infeasibility, or attainment.

For a minimization LP `min cᵀx` subject to `Ax=b, x≥0`, the dual is `max bᵀπ` subject to `Aᵀπ≤c`, with free `π`. The exact identity

`cᵀx − bᵀπ = (c−Aᵀπ)ᵀx + πᵀ(Ax−b)`

proves weak duality for primal-feasible `x` and dual-feasible `π`. Use the analogous identity for the actual model; do not port signs from a different convention.

## 2. Separate the logical claims

Weak duality follows from feasible primal/dual points under the stated cone and sign conventions. Strong duality, attainment, complementary slackness, and KKT require their own hypotheses. For convex problems, check a relevant Slater/relative-interior condition; for conic problems without strict feasibility, consider facial reduction or an extended dual and verify its hypotheses. Do not infer a finite dual optimum merely because the primal is feasible and bounded unless the cited theorem applies.

For minimax exchange, state the compactness, convexity/convexlikeness, and semicontinuity assumptions in the exact topology. A finite LP duality theorem does not provide these properties for a space of probability distributions or randomized online policies.

## 3. Turn candidates into certificates

For an LP certificate, independently check:

1. primal feasibility, including equality residuals and nonnegativity;
2. dual feasibility, including multiplier signs and all dual inequalities;
3. the objective ordering and, for claimed optimality, an exact or rigorously bounded zero gap.

Use `fractions.Fraction`, integer-scaled arithmetic, or another exact rational checker when data are rational. For irrational or floating-point input, use interval arithmetic or a proved error bound with outward rounding. Confirm the enclosure contains the true value and that every denominator used is strictly positive. A tolerance check on rounded residuals is not an exact feasibility proof.

For SDP bounds, validate the primal matrix constraints and PSD enclosures, and rigorously bound the minimum eigenvalues of dual residual blocks. If the lower bound includes a negative-eigenvalue correction, verify the signs, block sizes, and any finite upper eigenvalue bounds required by the theorem. An approximate dual point need not be feasible only when the cited correction theorem explicitly permits it.

For polynomial nonnegativity, an SOS Gram matrix gives an SDP certificate. DSOS and SDSOS replace it by diagonally dominant/scaled-diagonally-dominant Gram constraints and hence LP/SOCP certificates, but these are inner approximations and can reject an SOS or nonnegative polynomial. A convergent SOS/moment hierarchy still needs its compactness/Archimedean hypotheses and a sufficiently high order; a finite level is a bound unless exactness is proved. For S018's measure-based criterion on a closed set K, verify that the finite Borel measure has support exactly K. Compact K permits an arbitrary such finite measure; noncompact K additionally requires the cited moment-growth condition, whose exact criterion is not supplied in S018. For homogeneous forms on the nonnegative orthant, S018 explicitly uses a compact simplex-supported measure as a special alternative. Do not transfer that shortcut to a general noncompact K without a valid compact base or the cited growth hypothesis.

S019’s finite termination has a separate KKT-hierarchy dependency. Identity (3.12) establishes Archimedeanity of the simplex constraint module; it does not alone imply finite convergence. S019 invokes Nie [38, Theorem 3.3] for finite exactness of the auxiliary critical-set hierarchy. That theorem requires a nonempty critical set, polynomial expressions for KKT multipliers on it, and one of the stated Archimedean/separator alternatives. In S019, compactness of the simplex gives a minimizer; homogeneity yields polynomial multipliers p_i=∂_iA−mA; and (3.12) supplies the original-constraint Archimedean condition. The paper then transfers the external hierarchy's eventual equality to its v_k through (3.11). The cited theorem statement was consulted, but its full proof was not independently audited in the W19 reading. The ordinary Lasserre comparison sequence remains only ν_k≤v_k≤v*; do not assign its finite exactness to that hierarchy. For symmetric forms whose number of variables tends to infinity, name the transition maps and limit cone: the limit can depend on that identification, and a conjectured equality in all degrees must remain a conjecture.

For S023 quasi branch-and-bound, preserve the quantifier: a quasi-lower bound is needed only on boxes containing a global minimizer, and pruning must retain at least one such box. The independently checked scope is qBnB2, the constrained sampler, longest-edge breadth-first coverage, and Appendix Theorem 2 for each fixed positive tolerance when the sampling/bound discrepancy has a uniform modulus `ψ(r)→0`. In the constrained geometry, the line through a sample and a global minimizer may extend past that minimizer inside the original box `C0`; do not assert that the extension stays in each smaller cell. After finite warmup, the accepted gap is at most `2 L2 r²`. qBnB3, Newton termination, and eventual exactness are outside the current accepted use.

A proof-assistant formalization of simplex/polyhedral results (S027) establishes correctness of the specified exact implementation and derived theorems in its ordered-field model. It does not validate arbitrary floating-point solver output, conic SDP relaxations, or the stochastic policy interface. Keep formal proof, exact rational checking of one finite instance, and interval validation of numerical data as distinct evidence types.

For M0349, the current accepted certificate interface is Theorem 13.3 (physical p. 89): use the source's Krawczyk map with its minus sign, a valid interval Jacobian enclosure, `0∈X`, `x̃+X⊂D`, and strict inclusion `S(X,x̃)⊂int(X)`. It certifies a root and uniqueness only on the stated finite-dimensional box. The negative-residual correction of Theorem 14.2 and the Hilbert-space Theorem 16.1 are not included as current high-reviewed method routes; do not present them as certified interfaces here.

For Farkas-type image tests, distinguish membership in the closure from exact image membership: a zero-polar/support condition may characterize only `b ∈ cl(A(P))`, while exact membership can require one uniform residual constant or a closed-image hypothesis (S003). In moment cones, check compactness before using a dual-cone characterization as a representation theorem. S011 §3 states its algorithm and Proposition 1 discussion for compact basic semialgebraic sets; Proposition 1’s local display does not repeat that standing compactness assumption. The current admitted measure interface is narrower: for a supplied finite measure certificate, check nonnegative weights, support membership, and every moment identity exactly. Algorithm 3’s signed-weight pseudocode and a general extraction guarantee are not independently admitted here. Example 1 on `K=R` illustrates a nonclosed noncompact moment cone and rules out unconditional extension, but is not a counterexample to the compact-scoped proposition. Example 3 separately shows that Corollary 2’s SOS certificate cannot be assumed without its Archimedean hypothesis. For conditional mean–variance bounds, S010 Proposition 1’s infinite branch is for positive variance; at zero variance the law is `delta_mu`, so conditioning on `X ≥ t` is defined with mean `mu` for `t ≤ mu` and undefined for `t > mu`. For Farkas certificates, check the multiplier signs, exact derived inequality, and strict contradiction. Finite generation/closedness assumptions matter. For MIP certificates, check exact input data, integer feasibility, each inference/rounding step, each branch disjunction, and the coverage/combination of all leaves. A branch bound is only global when the tree covers every feasible integer point.

When useful, run a small exact-rational script or an available local mathematical tool (e.g. Python rational arithmetic or MATLAB) and save the input and output. Label the evidence as exact, interval-certified, or floating-point exploratory. Computation verifies only the encoded finite instance.

## 4. Preserve the analytic interface

After obtaining a finite certificate, name what remains unproved. Typical gaps include:

- uniform validity over all probability laws, adversarial distributions, or unbounded support;
- compactness, tightness, measurable selection, attainment, or a minimax exchange;
- feasibility of the finite relaxation as a representation of the original stochastic policy;
- treatment of arrival order, ties, simultaneous atoms, or event-time conventions;
- an error bound uniform in `n`, a limit interchange, or convergence to an online benchmark.

Never promote a finite numerical example to a universal inequality or an exact asymptotic ratio.

## 5. Probability-model interfaces and accepted source scopes

For conditional generalized-moment objectives, preserve the event denominator and its positivity. A sharp ratio bound, strong duality, a basic-distribution reduction, and attainment are distinct statements; check the source's bounded objective, uniform positive event-probability, and moment-interiority assumptions before transferring them. In moment/SOS hierarchies, the infinite GMP and each finite relaxation have separate attainment hypotheses.

For conic residual bounds, identify the cone class, face chain, PPS condition, and any norm bound used by the facial residual function. A theorem for symmetric cones or a lifted DNN cone does not automatically cover an arbitrary cone intersection; a facial-reduction step count is not itself a numerical certificate.

For S021, keep the accepted scope to the nonnegative finite weight-grid and simplex-weight characterization recorded in the source table. The strict-positive branch, quartic-limit equality, and Example 5.4 are outside the current scoped use; do not use that example as a verified boundary certificate or label it an independently established source error.

The original W19 baseline comprises 29 complete papers and one complete acquired book whose entire used unit, Chapter 5, is 58 physical pages (229–286). R04 independently high-reviewed 30 exact source identities for their narrow scopes. The old W19 reading cards and page-coverage records are preserved under `../evidence/W19/`; the current proof locators, accepted uses, and limitations are in [`sources.md`](sources.md). The six prior R15 G32 source uses are explicitly supplemental and remain separate from the baseline.

### Additional independently checked interfaces

- **S024:** the current use is an exact finite SOS lower certificate and the degree-preserving inclusion/monotonicity of nested boxes. A finite identity proves `f−λ≥0` on the declared set, with equality allowed. Strict positivity and supremum-based descriptions of the idealized GLB / quadratic-module positivity range are different claims. The source's full extraction/termination algorithm is not included.
- **S026:** exact rational primal repair for a fixed integer assignment gives an incumbent only after exact feasibility; a rigorous dual lower bound can support minimization pruning, and the proof log must cover all branches. If a true activity `a·x` is enclosed by `[s−μ,s+μ]`, confirm satisfaction of `a·x≥b` only if `s−μ≥b`, confirm violation only if `s+μ<b`, and otherwise fall back to exact arithmetic. Solver/presolve implementations remain external dependencies. The local PDF is byte-identical to arXiv `2101.09141v1`, not asserted to be a publisher version of record.
- **M0359:** an explicit feasible primal/dual pair with valid signs, stationarity and complementary slackness is sufficient for global optimality in the stated convex differentiable setting. Slater and attainment conditions are used for the distinct necessity/strong-duality direction. The only complete book unit credited is Chapter 5, physical pp. 229–286.
- **S021:** only the nonnegative finite weight-grid and simplex-weight characterization are accepted. Strict positivity, quartic-limit equality and Example 5.4 are not adopted as verified interfaces.
- **S023:** qBnB3/Newton and eventual exactness are not accepted routes here; use the qBnB2/constrained-sampler/BFS scope above.

## L15 G32 finite-certificate route

1. **Freeze the finite mathematical model.** Record the universe, variables, domains, constraints, objective direction, coefficients, and all symmetry reductions. For an infection certificate, identify exactly which finite process statement the variables encode.
2. **Choose a certificate that matches the claim.** Use exact rational primal/dual or Farkas multipliers for rational LP claims; interval enclosures with directed rounding for floating computations; exact Gram/SOS identities for polynomial positivity; and a complete proof tree for integer/exhaustive claims. A decimal optimizer, solver status, or finite search log is not enough by itself.
3. **Check the direction.** For a minimization LP, a feasible primal point is an upper bound and a feasible dual point is a lower bound. Verify signs and the weak-duality inequality exactly. For a relaxation, prove set inclusion and objective direction before transferring a bound.
4. **Check completeness and transfer separately.** A branch tree must cover every integer case; an interval root proof must isolate all roots in the target domain; an SOS proof needs the displayed polynomial identity and positivity of each Gram matrix. A finite result does not prove an all-(n), infinite-plane, or probabilistic statement without an induction, compactness, limiting, or model-specific transfer theorem.

### Coverage LPs and submodularity

For a finite set-cover encoding, let (A_{ij}=1) when candidate (j) covers requirement (i). The binary minimization model `min cᵀx` subject to `Ax≥1`, `x∈{0,1}^m` is relaxed by `x∈[0,1]^m`; the relaxation is a lower bound because its feasible region contains the integer feasible region. For any feasible integer cover, the rational multipliers `y≥0`, `Aᵀy≤c` give a checkable lower-bound certificate: `1ᵀy≤yᵀAx=xᵀAᵀy≤cᵀx`. This is a valid certificate by weak duality; it is not the complete dual of the capped relaxation `0≤x≤1`, whose upper-bound constraints would have their own dual multipliers. Do not assert submodularity or a greedy ratio unless the actual objective satisfies the theorem's diminishing-returns assumptions.

In the K3 zero-forcing closure example, `f(S)=|closure(S)|` is not submodular: for `A={0}`, `B={1}`, `f(A)+f(B)=2`, while `f(A∪B)+f(A∩B)=3`. This is an exact finite counterexample, not a claim about every coverage function.

### G32 method-specific status

- **G32.01 rational primal/dual and Farkas:** exact feasibility, multiplier signs, and objective comparison; sources S001/S002/S025/S027.
- **G32.02 interval/Taylor:** not an active route in this candidate. A prior R15 record has a restricted outward-interval/Taylor-coefficient use (M0349 physical p.82), but it is not a general Taylor-model remainder certificate and was not rebound as a current high-scoped use here.
- **G32.03 SOS/SDP:** verify the polynomial identity, rational Gram matrix, and PSD certificate; retain degree and compactness assumptions. SOS is sufficient, not automatically exact.
- **G32.04 Sturm isolation:** bind the exact polynomial, target interval convention, signed remainder or Sturm–Habicht sequence, endpoint multiplicities, and exact sign arithmetic. Pébay–Rojas–Thompson Theorem 1.2 gives the distinct-root count in `(a,b]` as `V_f(a)−V_f(b)` when `f` is nonzero, `a≤b`, and neither endpoint is a multiple root; handle constants and degenerate intervals separately. The original revision2 source-proof row was held because Lemma 1.4(2)'s printed `P_f=(1/g)P_(f/g)` identity is false; R15 later accepted the independently derived generalized-PRS correction in the source-only Sturm delta. Do not cite that lemma. Use the independent proof（本机附件：`evidence/G32/independent_endpoint_proof.txt`）: for monic `g=gcd(f,f′)`, form `F=f/g` and `H=f′/g`, then use the raw signed remainder sequence `P(f,f′)=g·PRS(F,H)`. At a root r, `H(r)=m_r F′(r)`, which preserves the crossing orientation. Do not call `PRS(F,H)` the ordinary Sturm sequence of `(F,F′)`; those pairs differ in general. Require ordinary signed Euclidean remainders, stop at the first zero and ignore zero entries; exact/certified sign and zero tests are required. Constants and `a=b` are handled directly. Isolate the source's unused example errors: `(x²−1)²` has both roots −1 and +1 in `(−2,1]`; the factorization in Example 1.3 is `(x−1)²(x−3)`. Emiris–Tsigaridas supplies a separate accepted univariate square-free/Sturm–Habicht and algebraic-number comparison route. For Theorem 19 retain `d=O(τ)` (or pad with `τ*=max(d,τ)`), joint degree/coefficient-bit bounds for P,Q, and isolating endpoint bit-size `O(dτ*)`. Its generic sign query needs square-free P, `gcd(P,Q)=1`, and endpoints not roots of P; split shared-root/`Q(α)=0` cases first and evaluate rational endpoints exactly or use strict isolation. Theorem 16's printed upper Mahler-gap inequality is false (`x²−1` gives `1≥2`); only the lower separation inequality used in Proposition 17 is adopted. R15 accepted this restricted Emiris route and the corrected Pébay–Rojas–Thompson endpoint proof as separate scoped uses. No bivariate/general solver or implementation certification follows.
- **G32.05 SAT/SMT:** encode the finite statement and bind the input formula, active clauses, theory atoms, preprocessing, and checker boundary. DRAT-trim is propositional implementation evidence: RUP additions are entailed by the active CNF, whereas RAT additions preserve satisfiability but need not be logical consequences; a full refutation must check the empty clause. LRAT gives explicit CNF hints and a Coq checker theorem for CNF; at physical p.9 its partial function named `entail` proves `ICNF_reduces` (a satisfiability reduction), not that each added clause is individually entailed. Carcara retains `valid`/`holey`/`invalid`; importing cvc5 elaboration when a step is not invalid can still leave holes, and all LIA-elaborated benchmarks on pp.15–16 have rewrite holes. eDRAT/VALIDO separates RUP-only Boolean core checking from validation of every theory lemma; only the described QF_LRA and QF_UF validators are covered, and preprocessing/CNF conversion need separate certificates. Correct its Theorem 2 certificate to `μ₀+Σ_i λ_iF_i+Σ_{j=1}^m μ_jG_j=0`, `μ₀+Σ_{j=1}^m μ_j=1`; correct printed page locators to physical page +17. R15 accepted these four restricted uses. No arbitrary SMT, quantified arithmetic, end-to-end checker correctness, or universal solver certification follows.
- **G32.06 interval Newton/Krawczyk:** Theorem 13.3 of M0349 (physical PDF p.89) states a Krawczyk inclusion criterion: with continuously differentiable f, 0∈X, x̃+X⊂D, and S(X,x̃)=−Rf(x̃)+(I−RJf(x̃+X))X⊂int(X), the stated Jacobian interval matrices are nonsingular and there is a unique root in x̃+S(X,x̃). The sign is essential: the source and its proof use −Rf(x̃). With f(x)=x, x̃=1/4, R=1, X=[−1,1], the correct S={−1/4} gives x̃+S={0}; the incorrect positive sign gives S={1/4}⊂int(X) but x̃+S={1/2}, which excludes the actual root. The exact rational check is in the exact rational sign case in [examples/positive.md](../examples/positive.md). Verify every interval enclosure with outward rounding; failure of inclusion is inconclusive.
- **G32.07 certified enumeration:** make the finite domain and every symmetry reduction explicit; keep finite classification separate from an unrestricted theorem.



For exact work/version identity, original page images, current reviewer receipts, and each accepted row’s source-specific scope, use the local [source register](sources.md) and the immutable files it links. Do not infer an accepted theorem from an older source card or from the source’s full theorem list.
