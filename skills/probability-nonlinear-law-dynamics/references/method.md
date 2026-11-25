# Method reference: type the operator before using a theorem

## 1. Operator ledger

For a target map on probability laws, record the state space `E`, the law space `P(E)`, its sigma-field/topology, parameter domain, and the exact update. Similar-looking fixedpoint equations may describe different dynamics.

### A. Nested stationary-law map

Let `K_theta` be a Markov kernel with parameter `theta` held fixed, and let `pi(theta)` solve

`pi(theta) K_theta = pi(theta)`.

The outer operator is `Phi(theta) = pi(theta)`, and its dynamics are

`theta[n+1] = Phi(theta[n])`.

There are two different iterations here. Fixed-parameter mixing estimates control `nu K_theta^t -> pi(theta)` while `theta` remains unchanged. They do not control repeated updates of `theta` through `Phi`.

### B. Nonlinear Markov law update

A common discrete-time nonlinear Markov update is

`N(mu) = mu K_mu`,

with `mu[n+1] = N(mu[n])`. Continuous-time McKean–Vlasov/mean-field models instead evolve a law by a nonlinear semigroup or forward equation. Their equilibrium equation may be `mu K_mu = mu`, but their trajectory is generally not the nested map `Phi`.

### C. Recursive distributional equation

An RDE has the form

`T(mu) = Law(g(xi, X_1, ..., X_m))`,

where the `X_i` are independent with common law `mu` and are independent of the innovation(s) `xi`, with all dependence and conditioning specified. A fixedpoint theorem for `T` requires that exact recursive representation, its moment/state-space assumptions, and its metric or monotone structure. Equality of fixedpoint equations at one law does not identify their iterates.

## 2. Proof obligations

Treat these as distinct claims; prove only the one requested.

1. **Well-definedness:** show each update maps the stated law class into itself and is measurable where needed.
2. **Inner invariant law:** for a frozen Markov kernel, establish existence/uniqueness under the actual recurrence, compactness, minorization, or coupling hypotheses.
3. **Outer-map regularity:** prove continuity/Lipschitz bounds for `theta -> pi(K_theta)` using a kernel perturbation estimate or a direct coupling. Check that communicating/recurrent-class structure remains controlled. A uniform mixing rate for each frozen kernel is not itself a bound on `K_theta-K_eta` or on `pi(K_theta)-pi(K_eta)`.
4. **Fixedpoint existence:** for Schauder/Brouwer, verify a compact convex invariant domain and continuity of the actual map. For Kakutani, verify the correspondence is nonempty, compact-convex-valued, and upper hemicontinuous. A full-support subset is usually not weakly closed; do not apply compact fixedpoint theorems to it without a replacement closed invariant class.
5. **Uniqueness:** identify the mechanism (strict contraction in a stated metric, monotonicity/order, degree argument with the correct index hypotheses, or a direct structural classification). Existence alone does not imply uniqueness.
6. **Local stability:** compute/estimate the derivative or a local contraction near a fixed law and state the topology. Local stability does not imply all initial laws converge.
7. **Global iteration:** use a global contraction, strict Lyapunov function, monotone order, or a justified omega-limit/no-cycle argument. Compactness gives cluster points. For a continuous map the omega-limit set is forward invariant, but its individual points need not be fixed. If the whole orbit converges, continuity makes its limit a fixed point. To prove every cluster point is fixed, establish asymptotic regularity `d(Phi(x_n), x_n) -> 0` (then continuity identifies each cluster point as fixed), or separately exclude nontrivial cycles/recurrent sets.
8. **Almost-everywhere convergence:** specify the reference measure on the parameter simplex/law space and prove that the nonconvergent basins have zero measure, e.g. through a valid invariant-stratum or stable-manifold argument. Finite simulations and convergence from selected initial points are not basin proofs.
9. **Support classification:** distinguish atoms, absolutely continuous laws, singular continuous laws, and mixed laws. A density equation or a grid-supported example cannot rule out or establish all Borel full-support laws.

## 3. Transfer gates for neighboring methods

### Nonlinear Markov methods

Before applying a nonlinear Markov theorem, compare its exact update (`mu K_mu`, or a continuous-time equation) with the target. Match the topology/metric, law-dependent kernel, irreducibility or minorization assumptions, moment bounds, and meaning of equilibrium. The finite-state literature supplies existence, degree, Dobrushin, or ergodicity methods for stated nonlinear operators; it does not silently yield outer convergence for `Phi(theta)=pi(K_theta)`.

### RDE and contraction methods

Before using an RDE result, write the independent-copy distributional identity and identify all innovations, weights, normalization, and moments. Verify the contraction coefficient in the chosen metric and that the metric space is complete and invariant. If the target has no such recursive-copy representation, use the source only as a method analogy, not as a theorem application. Shift-invariant RDE convergence is convergence in a quotient/normalized sense; preserve that qualification.

**Concrete total-variation criterion (W21-004).** For the discrete update `N(μ)=μP_μ`, compare both (i) all cross-state/law pairs, `sup_(μ,ν) d_TV(P_μ(x,·),P_ν(y,·))≤2(1−α)`, and (ii) same-state sensitivity, `d_TV(P_μ(x,·),P_ν(x,·))≤λd_TV(μ,ν)`. The targeted proof accepts geometric convergence if `λ<α`, with a `2/(λn)` bound at `λ=α>0`; use an actual `β<1` at the sharpness endpoint `λ=1`. The literal SDE Theorem 3.1 proof route is held at the truncated-W2 versus squared-TV step: its stated law-Lipschitz condition does not justify the p.13 squared-TV integrand. R10 confirms this local gap; this is not a counterexample to the SDE theorem conclusion. See the W21-004 overlay（本机附件：`evidence/review_authority_scope.md`） and canonical card（本机附件：`evidence/usage_views/active/W21-004.md`）.

**Invariant-law limits of varying systems (W21-007).** Require fixed-time conditional convergence for **every subsequence** `N_k→∞` and **every** `x_k∈E_(N_k)` with `x_k→x`: the conditional law of `Y^(N_k)(t)` given `x_k` must converge weakly to `δ_(φ_t(x))`. The targeted proof then passes invariant laws to a limit by Skorohod representation and bounded convergence. A full-index-only hypothesis is not sufficient for the proof's subsequence step. The Dirac-limit corollary additionally needs tightness, a continuous semiflow, and global attraction. This is an `N→∞` stationary-regime result, not an iteration theorem for a fixed `Φ`. See the W21-007 overlay（本机附件：`evidence/review_authority_scope.md`） and canonical card（本机附件：`evidence/usage_views/active/W21-007.md`）.

**Reflection-coupling template (W21-012).** Diffusion contractions combine a one-sided curvature bound with a Lyapunov drift and either an additive cost or a multiplicative semimetric; the latter's proof cancels a cross-variation term using a logarithmic-gradient bound. Keep each theorem's own cost and radii: the multiplicative theorem's `S1/S2` differ from the additive theorem. Preserve the stated moment and interaction bounds, the “for each `R`, there exists `τ0(R)`” quantifier, and the separate all-initial-law moment-squared remainder. The subgeometric tail requires both Assumptions 2.8 and 2.9; its displayed TV is set-sup (double for full variation) and is not a `W_rho1` contraction. The broader local-Lipschitz extension relies on an R15-derived cutoff proof not independently checked here; until a separate review, use only a subcase where short-distance regularity is justified directly (for example, a globally Lipschitz drift). See the W21-012 overlay（本机附件：`evidence/review_authority_scope.md`）, canonical card（本机附件：`evidence/usage_views/active/W21-012.md`）, and Theorems 2.1–2.4; printed Theorem 2.2 repeats assumption 2.2, while setup/proof uses 2.1, 2.2 and 2.4.

**W21-025 and W21-027: two separate recursive-law interfaces.** W21-025 is used only for Lemma 7.3's local-to-global Laplace comparison when the branching product has a strict moment `p(a)=EΣA_i^a<1` and `φ≤ψ` on `(0,t₀]`; this is not its fixed-point classification, a critical case, or a target-selector theorem. W21-027 is a separate centered Quicksort-cost contraction with its own independent-copy recursion and common-uniform-pivot coupling. Neither identity has been derived for a stationary-law map. See W21-025（本机附件：`evidence/usage_views/active/W21-025.md`）, W21-027（本机附件：`evidence/usage_views/active/W21-027.md`）, and the [scoped source ledger](sources.md).

### Finite-state MFG equilibrium and adjustment (W21-013/014)

Neumann’s W21-013 Theorem 4.1 proves stationary-MFE existence for a finite state/action discounted game under A1 (Lipschitz transition-rate coordinates and continuous rewards) by a Kakutani correspondence built from optimal stationary policies and stationary population laws. Its Theorem 5.2 assumes irreducibility of `Q^d(m)` for **every deterministic stationary strategy** `d∈D^s`, not only the optimal ones, and identifies the response set as the convex hull of the optimal deterministic policies’ stationary laws. The reverse inclusion mixes occupation arrays `z_{ia}=Σ_k λ_k x_i^{d_k} 1_{a=d_k(i)}` and state masses `x_i=Σ_k λ_k x_i^{d_k}`, then recovers the randomized policy by `π_{ia}=z_{ia}/x_i` on positive-mass rows (choosing an optimal action on zero-mass rows); balance mixes linearly. Do not infer that a convex mixture of policies has the mixture of their stationary laws. W21-014 studies a different object: a continuous-time set-valued myopic-adjustment inclusion. Its local exponential-stability theorems require either a constant irreducible generator at a unique-policy equilibrium or a differentiable vector field with one neutral mass direction and all transverse eigenvalues stable. Its global Theorem 5.1 assumes exactly two uniquely optimal policies in regions, a regular switching surface, and convergence of both nonlinear flows; one sign case still permits eventual motion on the switching boundary. These are MFG-specific existence/stability results, not an iteration theorem for `theta -> pi(K_theta)`. See W21-013（本机附件：`evidence/usage_views/active/W21-013.md`） and W21-014（本机附件：`evidence/usage_views/active/W21-014.md`）.

### Simplex dynamical systems

A finite-dimensional law map may be polynomial, rational, or piecewise algebraic. A QSO theorem applies only if the target is proved to satisfy the QSO's stochastic coefficients and any special Volterra, tournament, group, or doubly-stochastic hypotheses. Do not infer QSO structure merely because both maps act on a simplex. Preserve distinctions among convergence of iterates, convergence of Cesàro means, regularity, and ergodicity.

### Other simplex QSO scope checks (W21-015/019/021)

Zakharevich’s W21-015 is a specific three-coordinate quadratic map on the 2-simplex. The source's regions satisfy `U_1∩U_2∩U_3=∅`, not pairwise disjointness. Its geometric product estimate is stated outside a neighborhood of the center, not near it; the source's inference that the orbit eventually stays outside that neighborhood is asserted without a separate justification. Theorem 2's Cesàro contradiction depends on this Theorem 1 step, so keep the conclusion as the source's claim with that proof gap. Note 1's claim that the Cesàro cluster set lies among fixed points while containing all three vertices conflicts with connectedness of cluster sets for bounded sequences whose increments tend to zero. Do not use Note 1 as evidence. These exact-map statements do not transfer to a rational stationary-law map. See W21-015（本机附件：`evidence/usage_views/active/W21-015.md`）.

**W21-019 (accepted derived direction only).** For an exact finite Volterra QSO with the source's skew stochastic coefficients, standing transversality, and a transitive tournament on the positive initial support with winner `w` and `a_wi>0`, the R15-derived sufficient argument gives `x_w^{next}≥x_w[1+a_min(1−x_w)]` and convergence to that winner. The source's proof-free four-way equivalence and converse directions are not accepted; no tie/zero-edge extension is included. The source does not label its introductory example non-Volterra. This route applies only after proving the target is that exact QSO. See W21-019（本机附件：`evidence/usage_views/active/W21-019.md`）.

**W21-021 (three narrow interfaces; Corollary 4.3 excluded).** The accepted uses are: Theorem 3.6's quadratic-form bounds for symmetric nonnegative `A` with every principal-subset sum at most its size and full sum `m`; Theorem 3.8's row-capped `U_k` bounds when joint uses include compatible witnesses; and Theorem 4.1's particular completion `A_i=(E−A_1)/(m−1)`, `T_i=(E−T_1)/(m−1)` for `i≥2`. R14's neutral review rejected Corollary 4.3's general sufficient direction, so normalized slices alone are not a majorization certificate. None of these statements implies orbit convergence or applies to A121 without an exact QSO representation. See W21-021（本机附件：`evidence/usage_views/active/W21-021.md`） and its R14 neutral record（本机附件：`evidence/scoped_raw_dependencies/4c2f4f7263b76b40_review.json`）.

### Stationary-law perturbation

For `Phi(theta)=pi(K_theta)`, finite-chain fundamental-matrix or ergodicity-coefficient bounds are a plausible bridge. First prove uniqueness/controlled recurrent-class structure for every kernel in the relevant stratum. Then bound the transition-matrix perturbation and compose it with a stationary-law sensitivity estimate. Constants may deteriorate near reducible boundary strata. Even a global Lipschitz bound for `Phi` proves iteration convergence only if its contraction constant is strictly below one (or a different global dynamics argument is supplied).

### Uniformly ergodic stationary-law sensitivity (W21-039)

Mitrophanov's Theorem 3.1 and Corollary 3.1 bound finite-time and invariant-law perturbations for a base kernel `P` satisfying `sup_x ||δ_xP^n−π|| ≤ Cρ^n`, with the perturbed chain required to have an invariant law for the stationary estimate. Use `C≥1`, enlarging it if necessary. Theorem 3.2 instead uses an `m` with `τ(P^m)<1`. The norm is full variation, twice the set-sup total-variation convention. For the finite `k`-sample rank kernel, the card separately proves `||K_θ−K_η||_op≤k||θ−η||` by product maximal coupling; composing the statements is valid only when the selected base kernel's exact mixing hypothesis holds. A uniform outer Lipschitz constant needs uniform mixing constants across the parameter region. This is a source-level method template, not a proof of A121 orbit convergence. See the W21-039 overlay（本机附件：`evidence/review_authority_scope.md`）, canonical card（本机附件：`evidence/usage_views/active/W21-039.md`）, physical pp.3–6, and its coverage.

### Centered affine RDE contraction (W21-029)

For \(T(\mu)=\mathcal L(\sum_i T_iX_i+C)\), with iid child variables independent of the entire coefficient family, the source's Lemma 1 gives
\[
\ell_2(T\mu,T\nu)^2\le \left(\sum_i\mathbb E T_i^2\right)\ell_2(\mu,\nu)^2
\]
for centered finite-second-moment laws. If \(\mathbb E C=0\), \(\mathbb E C^2<\infty\), and \(\sum_i\mathbb E T_i^2<1\), Theorem 3 gives a unique fixedpoint and geometric iteration convergence in the complete centered \(\mathcal M_2^0\) Mallows/W2 space. The coupling uses common coefficients and quantile-coupled child copies; centering removes cross terms. Do not transfer the result without the independent-copy affine recursion, moment class, and strict coefficient bound. See W21-029（本机附件：`evidence/usage_views/active/W21-029.md`）, Lemma 1 and Theorem 3.

### Finite-state coefficient bound (W21-038)

Seneta's equation (3) states that for finite row-stochastic \(P,\widetilde P\), each with one irreducible class, and scrambling base matrix \(\tau_1(P)<1\),
\[
\|\widetilde\pi-\pi\|_1\le \frac{\|\widetilde P-P\|_1}{1-\tau_1(P)},\qquad
\tau_1(P)=\tfrac12\max_{i,j}\sum_s|p_{is}-p_{js}|.
\]
Equation (4) gives the analogous `p`-norm estimate when `τ_p(P)<1`. The maximum absolute row sum is the induced row-action matrix norm for `p=1`; other `p` use their own induced norm. For a parameter family, the denominator uses the base kernel and must be uniformly bounded away from zero; one must also bound the matrix perturbation itself. See the W21-038 overlay（本机附件：`evidence/review_authority_scope.md`） and canonical card（本机附件：`evidence/usage_views/active/W21-038.md`）, equations (3)–(4).

### Wasserstein chain perturbation (W21-040)

Under geometric Wasserstein ergodicity `τ(P^n)≤Cρ^n` for all `n≥0` with `C≥1`, a Lyapunov drift for the perturbed kernel, finite weighted one-step error, and the required invariant laws/moments, W21-040 Theorem 3.1 gives its Wasserstein finite-time perturbation bound and stationary consequence. The row does not admit the separate total-variation Theorem 3.2. Common uniform constants and a strict outer sensitivity bound would still have to be proved before deriving outer iteration convergence. See W21-040（本机附件：`evidence/usage_views/active/W21-040.md`）.

## 4. Full-text proof patterns and exact scope

These papers provide concrete proof mechanisms for neighboring operators. Use their hypotheses as gates, not as labels for a target that merely acts on probability laws.

### Finite-state nonlinear Markov generators

Neumann's W21-003 accepted interface is the finite continuous-time nonlinear flow `m˙=mQ(m)`: continuity of the conservative generator correspondence gives an invariant law by Kakutani; uniqueness additionally requires every `Q(m)` irreducible, a `C¹` reduced selector difference, and a nonsingular reduced Jacobian using the corrected reduced barycenter `c=(1/S)1` in the correct codomain. The printed reference homotopy is excluded. The row does not approve the source's unlisted two- or three-state ergodicity branches and gives no nested stationary-law iteration theorem. See W21-003（本机附件：`evidence/usage_views/active/W21-003.md`）.

### Finite-simplex and measure-valued quadratic stochastic operators

Blath–Jamilov–Scheutzow W21-018 assumes the exact group-indexed coefficients `p_ij,k = μ_(k−i−j)`. Support grows by `s(Vx)=s(x)+s(x)+s(μ)` until its size stabilizes at a coset of an `s(μ)`-invariant subgroup. The coset itself can keep moving by `g+U ↦ 2g+a+U` and can be periodic. Theorem 3.9 proves convergence to the uniform law on the **current** support at each iterate, not necessarily convergence to one fixed coset law. For full-support simplex points the support is always `G`, giving convergence to the center almost everywhere. The printed Theorem 3.11 expression `limsup (1/n) log log ||error|| ≤ log 2` is undefined once the error norm is below 1; the proof recurrence `ε_next≤k ε²` instead yields the derived `liminf (1/n)log(−log ε_n)≥log 2` after rescaling, unless exact uniformity occurs earlier. Keep the source's formula and the proof-derived consequence distinct. Its regularity criteria are group-theoretic. See the full card（本机附件：`evidence/usage_views/active/W21-018.md`）, §§3.6–3.13.

Ganikhodjaev–Saburov–Muhitdinov W21-023 is not one consistent asymmetric endpoint-selection specification as printed. Eq. (2.1) assigns `p` to both outcomes despite `p+q=1`; §3.1's two-atom recurrence corresponds to lower-point `p` / upper-point `q`, while §3.2's interval, density, and CDF equations correspond to lower-point `q` / upper-point `p`. The CDF recursion may be used as a derived identity for the continuous subsection's explicitly corrected convention, but it cannot reconcile the finite and continuous sections. Moreover, Theorem 4.6's claim for every continuous initial law lacks a support hypothesis: any valid parent-selection update preserves a closed support interval, so an atomless law supported in `[1/4,3/4]` cannot converge even weakly to `delta_0` or `delta_1`. The proof of the expanding-interval density bound also uses control of `g_λ(x)` that does not follow from `x≤B_n`. The state-space declaration `0,1)` conflicts with `delta_1`, and “strong limit” has no specified topology. These source issues and the isolated support counterexample are recorded in [the full card（本机附件：`evidence/usage_views/active/W21-023.md`）; do not silently repair the paper or transfer its endpoint claim to `Phi`.

### Centered-QSO weak-limit method (W21-044)

For `Q_G(F)=Law((X_1+X_2)/2+η)` with iid `X_1,X_2∼F` independent of fixed noise `G`, Theorem 1 identifies fixed points through `φ_H(s)=φ_H(s/2)^2φ_G(s)` and gives the limit-is-fixedpoint implication when iterates converge weakly. The weak-continuity argument is conditional on this exact characteristic-function update. Theorem 5's exponential-decay conclusion requires **both** its local modulus bound and existence of `G^{ {∞} }=w-lim_n G^{ {n} }`; the modulus bound alone is not an existence theorem. For `G=N(m,σ²)` with `m≠0`, the bound holds with `ε=1`, while `G^{ {n} }=N(nm,σ²Σ_{j<n}2^{-j})` has bounded variance and escaping mean, hence is not tight. The target order-statistic stationary map has no established centered-parental-average/noise representation, so only the general continuity lemma could be reused after proving target continuity. See W21-044（本机附件：`evidence/usage_views/active/W21-044.md`）, physical pp.5–13 and the local check.

### Smoothing and Poisson RDEs

Durrett–Liggett W21-024 is used only for the finite-mean nonnegative smoothing-transform branch: finite fixed `N`, a joint nonnegative weight vector, iid child laws independent of the whole vector, `m(1)=1`, `v′(1)<0`, and `E W_i^γ<∞` for some `γ>1`. Under these conditions it supplies nontrivial fixed-point existence and the accepted `W₁` iteration/scale-uniqueness and moment-criterion interfaces. Critical derivative-zero, infinite-mean, root-necessity, full lattice/nonlattice, and tail classifications are outside this row. See W21-024（本机附件：`evidence/usage_views/active/W21-024.md`）.

For rate-one Poisson points with iid independent real children and a proper complementary CDF satisfying `∫₀∞F<∞`, W21-036 gives the exact `d`-th-minimum survival transform and its smoothing regularity; its shift identity reflects `[m,M]` to `[-M,-m]`. In the additionally gated `D₁` bounded-envelope class, applying the transform twice makes the even-iterate lower envelope nondecreasing and upper envelope nonincreasing. For `d=1`, the logistic fixed point and its nonzero-shift two-cycles are exact. These accepted facts do **not** establish all-`d` uniqueness/global shifted limits or global interval-width collapse. See W21-036（本机附件：`evidence/usage_views/active/W21-036.md`） and the scope record（本机附件：`evidence/review_authority_scope.md`）.

### Additional smoothing-transform proof templates (W21-041/042/043/045)

These are four separate works on exact recursive operators; their overlap in topic does not create an A121/A122 recursion.

- **W21-041:** use only the conditional regular-case disintegration under the accepted branching, `L¹` martingale-limit, function-class, explicit near-zero tameness, and nonarithmetic tilted-walk assumptions. The checked formula is `G(x)=e^{+αx}E[-log M(e^{-x})]`, with the named Choquet–Deny dependency, giving the stated `f(t)=E exp(-cWt^α)` form. This does not admit full Theorem 1.2/tameness necessity, arithmetic profiles, or boundary Proposition 4.1 classification.
- **W21-042:** use only the noninteger `1<α<2` Laplace-remainder/renewal comparison and its multiplier `1/[1−ρ(α)]`, with the row's full weight and child moments and the local sign correction accepted by R12. Integer/higher-α proofs and Theorem 1.2's integrated-tail converse are outside scope.
- **W21-043 (arXiv v1 only):** use Proposition 6's integral characteristic-metric contraction on prescribed-mean nonnegative laws for `1<p<2`, with `S=ΣX_i`, `ES=1`, `E S^p<∞`, `ρ_p=EΣX_i^p<1`, iid children independent of the whole point process, and the corrected factor `E B^{p−1}`. The metric-completeness dependency remains explicit. The previously adjudicated Proposition 1(b) and 3(c) exclusions remain isolated; this row is not an elementary fixed-point/tail classification, and the journal version was not compared.
- **W21-045:** use only finite-mean conditional projection when the exact invariant RTP is nodewise endogenous and `0<EW<∞`, plus pathwise identification for two finite nonnegative endogenous RTPs on the same innovations after their equal or scaled marginals are independently established. Uniform-integrability additive martingales provide the stated endogenous mean-one construction. No automatic endogeny, general marginal-law uniqueness, or full A1–A5/critical/infinite-mean classification is admitted.

R15 accepts these four exact scoped uses; each remains subject to a proved weighted independent-child or min-type identity before application, and none establishes an A121/A122 target interface (the target-interface flags remain false). R12's neutral review applies only to the local formulas W21-041/042/043. See the [31-row scoped source ledger](sources.md).

## 5. A121/A122 anchor: current proven limits

The formal problems concern the order-statistic kernel on a finite metric space and on `[0,1]`.

- In W21-001, Aldous–Feng Theorem 1 (PDF p.5, proof pp.5–6) gives a unique invariant law for each frozen `theta`, a geometric total-variation bound, and support comparisons. R15 retains the finite binary-tree Theorem 7 only with its stated tree/full-support/distinct-distance restrictions and the derived endpoint identity `1/2−C=b(1/2−b)+c(1/2−c)>0`; see the overlay（本机附件：`evidence/review_authority_scope.md`）. The same paper's Theorem 3 (PDF pp.8–9) identifies the `j=1,2`, `k=2` invariant sets; Theorem 4 classifies interval fixed laws for `k=2` as point masses or equal two-point laws (PDF p.10, proof pp.10–12). The source Lemma 5 proof has a farthest/nearest direction typo; the W21-001 card records the justified repair by first transferring invariance via Theorem 3 and then using the nearest kernel. This is not a classification for general `k`.
- The no-distance-tie continuity assertion is Proposition 2 of W21-002 (statement PDF p.7; proof pp.8–9), not a proposition in W21-001. R15's finite-`k` proof controls the current state and all fresh sample coordinates; R14/R15 identify the physical-p.8 printed event as invalid and keep the repair derived. Continuity holds only at the stated tie-free laws, and neither paper proves outer `Phi`-orbit convergence. See the W21-002 overlay（本机附件：`evidence/review_authority_scope.md`）.
- W21-002 Conjecture 5 (PDF pp.13–14) is the A121 almost-everywhere convergence statement, not a theorem. Its general-k interval question remains open there. The additional parameter inequality in §7.3 (PDF p.22) is density-specific and cannot be upgraded to arbitrary singular/full-support laws.

Use these as a scope check, not as a substitute for a proof of the requested operator-specific statement. Full source cards and exact page coverage are linked in [the source ledger](sources.md).


**Exact recursive-law interfaces (W21-030/031/032/034/035).** W21-030 admits only Lemma 3.1's ideal-`ζ_s` contraction and centered Corollary 3.4 fixed-point classes, with `K<∞`, `0<s≤3`, the independent tuple/children and `ξ=EΣ||A_r||^s<1`; mean and covariance normalization are imposed only for the stated `s` ranges. It does not admit finite-recursion transfer or nonzero-mean/L² extensions. W21-031 admits only Lemma 3.1's closure of the exact nonnegative `L_δ`-weighted error recursion under negative log-index drift and its stated remainder; it does not certify the one-branch CLT residual proof or the multi-branch sketch. W21-032 admits only the finite-variance Gaussian fixed-law class for deterministic real weights with `sup|T_j|<1`, `ΣT_j²=1`, at least two nonzero weights, and the stated mean-compatibility equation when the mean is nonzero; no full Lévy/Choquet/stable/group classification is admitted. W21-034 admits only Lemma 2.1's positive-minimum support barrier and Proposition 2.3 A1/A3 cases, including `inf_j T_j≥1` for A1; it does not admit A2/A4, Choquet–Deny/Weibull, sign or random-weight classification. W21-035 admits only Theorem 5.3's prescribed-mean complex product-`W₂` contraction and cyclic Lemmas 6.8/.9's scalar-law identification under their exact moment/mean gates; no joint covariance inference or finite-urn Theorem 6.10 transfer is admitted. None is a theorem for `Φ(θ)=π(K_θ)`. See the [scoped source ledger](sources.md) and the linked source views.


## 7. New G21 method interfaces — pending source review

The following are proof obligations for the newly assigned interfaces. The checklist does not itself validate a source theorem or earn source credit. Link a primary source only after its exact statement, physical/printed pages, proof dependencies, and target bridge have been read and reviewed.

### G21.01 Markov-chain tree theorem and rational stationary selector

For a finite irreducible row-stochastic matrix `P`, define `τ_j` as the sum of products of transition probabilities over directed spanning trees oriented toward state `j`. The stationary law is `π_j=τ_j/Σ_i τ_i`. For parameterized `P_θ`, this is a rational selector wherever the denominator is positive. At reducible or boundary parameters, recurrent classes can change and denominators for individual class formulas can vanish; partition the parameter space into closed-class/support strata before claiming a single rational map. A formula for `π(P_θ)` is still only an inner stationary selector. It says nothing by itself about iteration of `θ↦π(P_θ)`.

### G21.02 Jacobian, Schur stability, and stable manifolds

Write the outer map explicitly on a simplex or other declared state manifold. Differentiate in tangent coordinates (for the simplex, `Σ_i v_i=0`), and check the map is differentiable on the relevant stratum. Eigenvalues strictly inside the unit disk give local asymptotic stability under the applicable discrete-time linearization theorem; a hyperbolic fixed point with unstable directions has a local stable manifold of lower dimension. These are local results. A boundary fixed point needs a one-sided/tangent-cone analysis; do not use a full-space Jacobian without checking boundary invariance. Local stability is not global attraction or a basin-measure theorem.

### G21.03 Lyapunov functions, LaSalle, and chain recurrence

On a compact positively invariant set, verify a continuous `V` with `V(Φ(x))−V(x)≤0`. LaSalle-type conclusions concern the largest invariant subset of the zero-decrease set. To conclude convergence to one fixed point, show that this invariant subset is a singleton or add a valid convergence argument; nonincrease alone can leave cycles or continua. Chain-recurrence exclusions need the exact continuity/compactness and strict-decrease hypotheses. State whether the result is for the whole simplex or a single invariant face.

### G21.04 Monotone maps and Hilbert projective metric

Specify the ordered cone and prove the target map preserves it. Hilbert’s projective metric applies to positive cone interiors; a contraction conclusion requires a finite projective diameter or another explicit contraction coefficient. Check that the map sends the relevant interior into itself, quantify distance to the boundary, and handle boundary faces separately. An order-preserving probability map is not automatically a strict contraction.

### G21.05 Transfer operators, fixed points, and support invariance

Define the operator on the exact measure class and prove its pushforward/update formula. Calculate how supports transform, including atoms and singular-continuous parts. Full-support probabilities are not weakly closed: on `[0,1]`, `(1−1/n)δ₀+(1/n)Leb` has full support and converges weakly to `δ₀`. Thus a weak compactness argument over a full-support class can leave the class. A density-only equation cannot exclude singular or mixed full-support invariant laws.

### G21.06 Bifurcations and certified periodic orbits

For a period-`q` candidate, solve `Φ^q(x)=x` while excluding all lower periods; verify the orbit remains in the intended invariant stratum. Numerical root finding only proposes a cycle. A proof needs exact algebra, interval Newton/Krawczyk bounds, or another validated enclosure, together with certified multipliers/Jacobian bounds for stability. For a parameter bifurcation, state the nondegeneracy and transversality conditions. Keep existence, local stability, global basin, and completeness of the cycle list as separate claims.

### G21.07 Real algebraic geometry and semialgebraic basins

If `Φ` is rational, clear denominators only on strata where their signs and nonvanishing are proved. State the polynomial equalities/inequalities and quantifiers used for fixed points, cycles, and invariant regions. Quantifier elimination can decide a stated first-order real-algebraic question, but an infinite basin described as `⋃_{n≥0} Φ^{-n}(U)` need not itself be semialgebraic. A finite exact computation on a grid is not a semialgebraic proof.

**Current source mapping:** none of the 31 inherited W21 full reads is linked to these seven methods merely by topic. Their original exact W21 uses remain in the L13 source-use crosswalk（本机附件：`evidence/G21_new_method_zero_mapping.md`）; new method links stay empty until reviewed.

For card-level proof obligations, counterexamples, and evidence boundaries, see the G21 method-interface cards（本机附件：`evidence/G21_new_method_zero_mapping.md`） and the 31-source high-review provenance gap index（本机附件：`evidence/review_authority_scope.md`）.
