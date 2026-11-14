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

S019's finite termination has a separate KKT-hierarchy dependency. Identity (3.12) establishes Archimedeanity of the simplex constraint module; it does not alone imply finite convergence. S019 invokes Nie [38, Theorem 3.3] for finite exactness of the auxiliary critical-set hierarchy. That theorem requires a nonempty critical set, polynomial expressions for KKT multipliers on it, and one of the stated Archimedean/separator alternatives. In S019, compactness of the simplex gives a minimizer; homogeneity yields polynomial multipliers p_i=∂_iA−mA; and (3.12) supplies the original-constraint Archimedean condition. The paper then transfers the external hierarchy's eventual equality to its v_k through (3.11). The cited theorem statement was consulted, but its full proof was not independently audited in the W19 reading. The ordinary Lasserre comparison sequence remains only ν_k≤v_k≤v*; do not assign its finite exactness to that hierarchy. For symmetric forms whose number of variables tends to infinity, name the transition maps and limit cone: the limit can depend on that identification, and a conjectured equality in all degrees must remain a conjecture.

In quasi branch-and-bound, check the exact quantifier of a quasi-lower-bound rule. For the qBnB rules in S023, the bound is required to be below the global minimum only on boxes containing a global minimizer, not on every box. A pruning proof must preserve a box containing a global minimizer in the active tree. Appendix Theorem 2 gives finite termination for every fixed positive tolerance when the sampling/bound discrepancy has a modulus tending to zero with box radius. qBnB(3)'s third-order gap supplies the modulus \(\psi(r)=3L_3r^3\); its finite \(\varepsilon\)-termination does not require nondegeneracy. Nondegeneracy is needed for the distinct eventual-exactness claim. The qBnB(2) formula also assumes an unconstrained minimizer; boundary-aware constrained rules are separate. qBnB(3) requires its stated smoothness, Hessian-Lipschitz, and neighborhood conditions, and numerical Newton termination adds its own correction.

A proof-assistant formalization of simplex/polyhedral results (S027) establishes correctness of the specified exact implementation and derived theorems in its ordered-field model. It does not validate arbitrary floating-point solver output, conic SDP relaxations, or the stochastic policy interface. Keep formal proof, exact rational checking of one finite instance, and interval validation of numerical data as distinct evidence types.

For M0349 Theorem 14.2, first inspect each block residual D_j=C_j−Σ_i y_iA_ij and its certified lower eigenvalue bound d_j≤λ_min(D_j). If every d_j≥0, then every D_j is positive semidefinite, y is dual feasible, and weak duality directly gives p*≥bᵀy; this useful zero-correction case requires no primal-point spectral cap. For negative residual blocks, the source's correction term uses block size and an upper eigenvalue ceiling. A pointwise ceiling at one feasible tuple does not itself bound a global optimum p*=inf_{θ∈Θ}f(θ): the source's printed Eq. (14.8) leaves its infimum index set unspecified, and its theorem statement's one known primal feasible tuple does not say the cap is uniform over optimizers or a minimizing sequence. Use a nonzero correction only after proving uniform/optimal-approximation ceilings on the relevant feasible tuples, or derive a separate global bound. The exact two-scalar-block probe shows only that one fixed candidate expression from a single feasible point can exceed the true optimum; it does not refute Eq. (14.8) under a separately specified infimum domain that supplies suitable uniform bounds.

For M0349 §16.1 Theorem 16.1, the abstract setting assumes two real Hilbert spaces X and Y and a Frechet-differentiable map; its dual-and-symmetric branch uses the Riesz isomorphism X→X′ and inner-product symmetry. Banach spaces also appear as the space of bounded operators and in the Banach fixed-point theorem, but this does not extend the theorem's hypotheses to arbitrary Banach X,Y.

For Farkas-type image tests, distinguish membership in the closure from exact image membership: a zero-polar/support condition may characterize only `b ∈ cl(A(P))`, while exact membership can require one uniform residual constant or a closed-image hypothesis (S003). In moment cones, check compactness before using a dual-cone characterization as a representation theorem. S011 §3 explicitly scopes its algorithm and Proposition 1 discussion to compact basic semialgebraic sets; Proposition 1’s local display does not repeat that standing compactness assumption. Example 1 on `K=R` illustrates a nonclosed noncompact moment cone and rules out unconditional extension, but is not a counterexample to the compact-scoped proposition. Example 3 separately shows that Corollary 2’s SOS certificate cannot be assumed without its Archimedean hypothesis. For conditional mean–variance bounds, S010 Proposition 1’s infinite branch is for positive variance; at zero variance the law is `delta_mu`, so conditioning on `X ≥ t` is defined with mean `mu` for `t ≤ mu` and undefined for `t > mu`. For Farkas certificates, check the multiplier signs, exact derived inequality, and strict contradiction. Finite generation/closedness assumptions matter. For MIP certificates, check exact input data, integer feasibility, each inference/rounding step, each branch disjunction, and the coverage/combination of all leaves. A branch bound is only global when the tree covers every feasible integer point.

When useful, run a small exact-rational script or an available local mathematical tool (e.g. Python rational arithmetic or MATLAB) and save the input and output. Label the evidence as exact, interval-certified, or floating-point exploratory. Computation verifies only the encoded finite instance.

## 4. Preserve the analytic interface

After obtaining a finite certificate, name what remains unproved. Typical gaps include:

- uniform validity over all probability laws, adversarial distributions, or unbounded support;
- compactness, tightness, measurable selection, attainment, or a minimax exchange;
- feasibility of the finite relaxation as a representation of the original stochastic policy;
- treatment of arrival order, ties, simultaneous atoms, or event-time conventions;
- an error bound uniform in `n`, a limit interchange, or convergence to an online benchmark.

Never promote a finite numerical example to a universal inequality or an exact asymptotic ratio.

## 5. Probability-model interfaces and read scope

For conditional generalized-moment objectives, preserve the event denominator and its positivity. A sharp ratio bound, strong duality, a basic-distribution reduction, and attainment are distinct statements; check the source's bounded objective, uniform positive event-probability, and moment-interiority assumptions before transferring them. In moment/SOS hierarchies, the infinite GMP and each finite relaxation have separate attainment hypotheses.

For conic residual bounds, identify the cone class, face chain, PPS condition, and any norm bound used by the facial residual function. A theorem for symmetric cones or a lifted DNN cone does not automatically cover an arbitrary cone intersection; a facial-reduction step count is not itself a numerical certificate.

When quoting the quartic boundary example in S021, independently check the source's functional pairing: the arXiv v4 and DOI version of record both print data for which exact substitution gives \(\ell(f^{(n)})=13/400\), despite stating zero. The printed PSD blocks are separately feasible, but that displayed functional therefore does not certify the example is on the SOS boundary. This is a source-local issue in the example, not by itself a disproof of the paper's Theorem 5.5; do not use that example as a verified certificate until the discrepancy is independently resolved.

The current read set contains complete reads of Sion, Kager, Forsgren–Wright, Zălinescu, Basu–Martin–Ryan (both papers), Guo–He–Jiang–Wang, Oustry–Cerulli, Harwood, van Eekelen, Henrion–Naldi–Safey El Din, Halaseh–Magron–Skomra, Pataki, Lourenço (Amenable cones), Lourenço–Muramatsu–Tsuchiya, Blekherman–Riener, Ahmadi–Majumdar, Dym, Mohammadi–Peet, Allamigeon–Katz, Cheung–Gleixner–Steffy, Eifler–Gleixner, Burer, Lasserre (Lagrangian hierarchies), Lasserre (copositive approximation), Nie, Hildebrand, and Rump; the complete selected Chapter 5 of Boyd–Vandenberghe. Check `evidence/W19/reading_coverage.json` and each card for exact page scope and reader provenance. Reading is distinct from independent auditing: R08 has now accepted this 30-source set and the current skill, while reader-side status fields remain pending. The rest of `evidence/W19/sources.json` is a tracked candidate inventory and must not be cited as theorem evidence read in this pass.
