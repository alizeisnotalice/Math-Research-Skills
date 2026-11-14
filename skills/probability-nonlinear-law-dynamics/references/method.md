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

**Concrete total-variation criterion (W21-004).** For `N(μ)=μP_μ`, compare both (i) all cross-state/law pairs, `sup_(μ,ν) d_TV(P_μ(x,·),P_ν(y,·))≤2(1−α)`, and (ii) same-state sensitivity, `d_TV(P_μ(x,·),P_ν(x,·))≤λd_TV(μ,ν)`. The source proves a unique invariant law and geometric convergence if `λ<α`, with a `2/(λn)` bound at `λ=α`; the threshold is sharp. A122's equation `θK_θ=θ` matches the invariant-law equation if `P_μ=K_μ`, but transfer requires proving both inequalities for the target. It does not bound the outer map `θ↦π(K_θ)`. See [W21-004](../evidence/W21/cards/W21-004.md), Theorem 2.2 and §4 proof.

**Invariant-law limits of varying systems (W21-007).** If `Y^N` are Feller systems on a Polish space, their fixed-time conditional laws converge from every converging sequence of initial states to a deterministic measurable `φ_t`, and `Π_N` are invariant, then each weak limit point of `Π_N` is invariant for `φ`. The proof is Skorohod representation plus bounded convergence. The theorem needs neither continuity nor a semiflow; the Dirac-limit corollary additionally needs tightness and a continuous globally attracting semiflow. This is an `N→∞` stationary-regime result, not an iteration theorem for a fixed `Φ`. See [W21-007](../evidence/W21/cards/W21-007.md), Theorem 1 and Corollary 1.

**Reflection-coupling template (W21-012).** Diffusion contractions combine a one-sided curvature bound with a Lyapunov drift and either an additive cost or a multiplicative semimetric; the latter's proof cancels a cross-variation term using a logarithmic-gradient bound. McKean–Vlasov contractions require a Lipschitz interaction and, in the quadratic-dissipativity theorem, a sufficiently small interaction parameter. These constants belong to the specified diffusion law flow. See [W21-012](../evidence/W21/cards/W21-012.md), Theorems 2.1–2.4; the printed Theorem 2.2 repeats assumption 2.2, while its setup/proof uses 2.1, 2.2 and 2.4.

**Two exact recursive-law examples (W21-025, W21-027).** Liu's smoothing-transform classification assumes `T(μ)=Law(Σ_i A_i Z_i)` with conditionally iid copies, nonnegative weights, and explicit `p(α)`/moment/lattice hypotheses. Rösler's Quicksort map contracts centered finite-variance laws by `√(2/3)` because the two independent recursive copies are weighted by `τ` and `1−τ` for a common uniform `τ`. Neither identity has been derived for a stationary-law map. See [W21-025](../evidence/W21/cards/W21-025.md) and [W21-027](../evidence/W21/cards/W21-027.md).

### Finite-state MFG equilibrium and adjustment (W21-013/014)

Neumann’s W21-013 Theorem 4.1 proves stationary-MFE existence for a finite state/action discounted game under A1 (Lipschitz transition-rate coordinates and continuous rewards) by a Kakutani correspondence built from optimal stationary policies and stationary population laws. Its Theorem 5.2 assumes irreducibility of `Q^d(m)` for **every deterministic stationary strategy** `d∈D^s`, not only the optimal ones, and identifies the response set as the convex hull of the optimal deterministic policies’ stationary laws. The reverse inclusion mixes occupation arrays `z_{ia}=Σ_k λ_k x_i^{d_k} 1_{a=d_k(i)}` and state masses `x_i=Σ_k λ_k x_i^{d_k}`, then recovers the randomized policy by `π_{ia}=z_{ia}/x_i` on positive-mass rows (choosing an optimal action on zero-mass rows); balance mixes linearly. Do not infer that a convex mixture of policies has the mixture of their stationary laws. W21-014 studies a different object: a continuous-time set-valued myopic-adjustment inclusion. Its local exponential-stability theorems require either a constant irreducible generator at a unique-policy equilibrium or a differentiable vector field with one neutral mass direction and all transverse eigenvalues stable. Its global Theorem 5.1 assumes exactly two uniquely optimal policies in regions, a regular switching surface, and convergence of both nonlinear flows; one sign case still permits eventual motion on the switching boundary. These are MFG-specific existence/stability results, not an iteration theorem for `theta -> pi(K_theta)`. See [W21-013](../evidence/W21/cards/W21-013.md) and [W21-014](../evidence/W21/cards/W21-014.md).

### Simplex dynamical systems

A finite-dimensional law map may be polynomial, rational, or piecewise algebraic. A QSO theorem applies only if the target is proved to satisfy the QSO's stochastic coefficients and any special Volterra, tournament, group, or doubly-stochastic hypotheses. Do not infer QSO structure merely because both maps act on a simplex. Preserve distinctions among convergence of iterates, convergence of Cesàro means, regularity, and ergodicity.

### Other simplex QSO scope checks (W21-015/019/021)

Zakharevich’s W21-015 is a specific three-coordinate quadratic map on the 2-simplex. The source's regions satisfy `U_1∩U_2∩U_3=∅`, not pairwise disjointness. Its geometric product estimate is stated outside a neighborhood of the center, not near it; the source's inference that the orbit eventually stays outside that neighborhood is asserted without a separate justification. Theorem 2's Cesàro contradiction depends on this Theorem 1 step, so keep the conclusion as the source's claim with that proof gap. Note 1's claim that the Cesàro cluster set lies among fixed points while containing all three vertices conflicts with connectedness of cluster sets for bounded sequences whose increments tend to zero. Do not use Note 1 as evidence. These exact-map statements do not transfer to a rational stationary-law map. See [W21-015](../evidence/W21/cards/W21-015.md).

W21-019 states an equivalence for transversal Volterra QSOs between regularity, tournament transitivity, the equal-support Ergodic principle, and asymptotic regularity; physical p.4 makes transversality a global standing assumption for the p.5 theorem. The five-page manuscript contains no proof, and cited [3–4] were not audited. Its introduction calls a displayed cyclic simplex QSO non-Volterra, but direct factorization shows it is Volterra and transversal; isolate that source classification error rather than treating it as a theorem counterexample. See [W21-019](../evidence/W21/cards/W21-019.md).

W21-021 treats doubly stochastic QSOs in the majorization sense `Vx ≺ x`. Its Corollary 4.3 uses normalized symmetric nonnegative coefficient slices `A_k in U_1` with `sum_k A_k=E`; Theorem 3.6 explicitly requires both all subset-sum inequalities and total mass `sum_(i,j) a_ij=m` for its quadratic-form bound. Theorem 3.4’s printed statement does not display this normalization, although `U_1` is defined with it and the proof invokes `A in U_1`; treat this as a possible scope omission pending review and rely on the explicit normalized formulations. No such majorization structure is established for A121. See [W21-021](../evidence/W21/cards/W21-021.md).

### Stationary-law perturbation

For `Phi(theta)=pi(K_theta)`, finite-chain fundamental-matrix or ergodicity-coefficient bounds are a plausible bridge. First prove uniqueness/controlled recurrent-class structure for every kernel in the relevant stratum. Then bound the transition-matrix perturbation and compose it with a stationary-law sensitivity estimate. Constants may deteriorate near reducible boundary strata. Even a global Lipschitz bound for `Phi` proves iteration convergence only if its contraction constant is strictly below one (or a different global dynamics argument is supplied).

### Uniformly ergodic stationary-law sensitivity (W21-039)

Mitrophanov's Theorem 3.1 and Corollary 3.1 bound finite-time and invariant-law perturbations for a base kernel `P` satisfying `sup_x ||δ_xP^n−π|| ≤ Cρ^n`, with the perturbed chain required to have an invariant law for the stationary estimate. Theorem 3.2 instead uses an `m` with `τ(P^m)<1`. The norm is full variation, twice the set-sup total-variation convention. For the finite `k`-sample rank kernel, the card separately proves `||K_θ−K_η||_op≤k||θ−η||` by product maximal coupling; composing the statements is valid only when the selected base kernel's exact mixing hypothesis holds. A uniform outer Lipschitz constant needs uniform mixing constants across the parameter region. This is a source-level method template, not a proof of A121 orbit convergence. See [W21-039](../evidence/W21/cards/W21-039.md), physical pp.3–6, and its coverage.

### Centered affine RDE contraction (W21-029)

For \(T(\mu)=\mathcal L(\sum_i T_iX_i+C)\), with iid child variables independent of the entire coefficient family, the source's Lemma 1 gives
\[
\ell_2(T\mu,T\nu)^2\le \left(\sum_i\mathbb E T_i^2\right)\ell_2(\mu,\nu)^2
\]
for centered finite-second-moment laws. If \(\mathbb E C=0\), \(\mathbb E C^2<\infty\), and \(\sum_i\mathbb E T_i^2<1\), Theorem 3 gives a unique fixedpoint and geometric iteration convergence in the complete centered \(\mathcal M_2^0\) Mallows/W2 space. The coupling uses common coefficients and quantile-coupled child copies; centering removes cross terms. Do not transfer the result without the independent-copy affine recursion, moment class, and strict coefficient bound. See [W21-029](../evidence/W21/cards/W21-029.md), Lemma 1 and Theorem 3.

### Finite-state coefficient bound (W21-038)

Seneta's equation (3) states that for finite row-stochastic \(P,\widetilde P\), each with one irreducible class, and scrambling base matrix \(\tau_1(P)<1\),
\[
\|\widetilde\pi-\pi\|_1\le \frac{\|\widetilde P-P\|_1}{1-\tau_1(P)},\qquad
\tau_1(P)=\tfrac12\max_{i,j}\sum_s|p_{is}-p_{js}|.
\]
Equation (4) gives the analogous \(p\)-norm estimate when \(\tau_p(P)<1\). In the source row-vector convention, the matrix norm is the maximum absolute row sum. For a parameter family, the denominator uses the base kernel and must be uniformly bounded away from zero; one must also bound the matrix perturbation itself. See [W21-038](../evidence/W21/cards/W21-038.md), equations (3)–(4).

### Wasserstein chain perturbation (W21-040)

Under geometric Wasserstein ergodicity `τ(P^n)≤Cρ^n` and a Lyapunov drift `P~V~≤δV~+L`, Theorem 3.1 controls finite-time law differences using `γ=sup_x W(δ_xP,δ_xP~)/V~(x)`; its stationary corollary gives `W(π,π~)≤C′γL/[(1−ρ)(1−δ)]` when both stationary laws and the required moments exist, with `C′=max(C,1)` under the positive-integer reading. The source writes `n∈N`, then defines `N_0={0,1,...}` but never explicitly defines `N`; under the positive-integer reading, the telescoping proofs of both Theorems 3.1 and 3.2 use a zero-power term and must use `C'=max(C,1)`, including in the stationary corollary. The original formulas can fail for `C<1`; exact two-state witnesses are recorded in the card/check. The total-variation Theorem 3.2 otherwise has distinct `V~`-uniform-ergodicity and two-drift hypotheses. These are two-kernel perturbation estimates, not outer contraction results until parameter-to-kernel error and uniform constants are proved. See [W21-040](../evidence/W21/cards/W21-040.md), Theorems 3.1–3.2.

## 4. Full-text proof patterns and exact scope

These papers provide concrete proof mechanisms for neighboring operators. Use their hypotheses as gates, not as labels for a target that merely acts on probability laws.

### Finite-state nonlinear Markov generators

Neumann's W21-003 studies the continuous-time ODE `m˙ = m Q(m)` on a finite simplex. Continuity of the generator-valued map gives an invariant law by Kakutani applied to `s(m)={x:xᵀQ(m)=0}`; irreducibility plus a nonsingular reduced Jacobian gives uniqueness by a Brouwer-degree argument. For two states, a continuous scalar field with one equilibrium gives strong ergodicity by a sign argument. For three states, the paper reduces to a planar field and combines a one-sign nonzero divergence with a local non-saddle condition, Bendixson, and Poincaré–Bendixson. See [the full card](../evidence/W21/cards/W21-003.md), Theorems 3.1–3.2 and 5.1–5.2. These conclusions apply to that nonlinear Markov flow, not to `theta -> pi(K_theta)` without an exact reduction.

### Finite-simplex and measure-valued quadratic stochastic operators

Blath–Jamilov–Scheutzow W21-018 assumes the exact group-indexed coefficients `p_ij,k = μ_(k−i−j)`. Support grows by `s(Vx)=s(x)+s(x)+s(μ)` until its size stabilizes at a coset of an `s(μ)`-invariant subgroup. The coset itself can keep moving by `g+U ↦ 2g+a+U` and can be periodic. Theorem 3.9 proves convergence to the uniform law on the **current** support at each iterate, not necessarily convergence to one fixed coset law. For full-support simplex points the support is always `G`, giving convergence to the center almost everywhere. The printed Theorem 3.11 expression `limsup (1/n) log log ||error|| ≤ log 2` is undefined once the error norm is below 1; the proof recurrence `ε_next≤k ε²` instead yields the derived `liminf (1/n)log(−log ε_n)≥log 2` after rescaling, unless exact uniformity occurs earlier. Keep the source's formula and the proof-derived consequence distinct. Its regularity criteria are group-theoretic. See [the full card](../evidence/W21/cards/W21-018.md), §§3.6–3.13.

Ganikhodjaev–Saburov–Muhitdinov W21-023 is not one consistent asymmetric endpoint-selection specification as printed. Eq. (2.1) assigns `p` to both outcomes despite `p+q=1`; §3.1's two-atom recurrence corresponds to lower-point `p` / upper-point `q`, while §3.2's interval, density, and CDF equations correspond to lower-point `q` / upper-point `p`. The CDF recursion may be used as a derived identity for the continuous subsection's explicitly corrected convention, but it cannot reconcile the finite and continuous sections. Moreover, Theorem 4.6's claim for every continuous initial law lacks a support hypothesis: any valid parent-selection update preserves a closed support interval, so an atomless law supported in `[1/4,3/4]` cannot converge even weakly to `delta_0` or `delta_1`. The proof of the expanding-interval density bound also uses control of `g_λ(x)` that does not follow from `x≤B_n`. The state-space declaration `[0,1)` conflicts with `delta_1`, and “strong limit” has no specified topology. These source issues and the isolated support counterexample are recorded in [the full card](../evidence/W21/cards/W21-023.md); do not silently repair the paper or transfer its endpoint claim to `Phi`.

### Centered-QSO weak-limit method (W21-044)

For `Q_G(F)=Law((X_1+X_2)/2+η)` with iid `X_1,X_2∼F` independent of fixed noise `G`, Theorem 1 identifies fixed points through `φ_H(s)=φ_H(s/2)^2φ_G(s)` and gives the limit-is-fixedpoint implication when iterates converge weakly. The weak-continuity argument is conditional on this exact characteristic-function update. Theorem 5's exponential-decay conclusion requires **both** its local modulus bound and existence of `G^{ {∞} }=w-lim_n G^{ {n} }`; the modulus bound alone is not an existence theorem. For `G=N(m,σ²)` with `m≠0`, the bound holds with `ε=1`, while `G^{ {n} }=N(nm,σ²Σ_{j<n}2^{-j})` has bounded variance and escaping mean, hence is not tight. The target order-statistic stationary map has no established centered-parental-average/noise representation, so only the general continuity lemma could be reused after proving target continuity. See [W21-044](../evidence/W21/cards/W21-044.md), physical pp.5–13 and the local check.

### Smoothing and Poisson RDEs

Durrett–Liggett W21-024 treats `T(mu)=Law(sum_i W_i X_i)` with iid `X_i~mu`, independent of a nonnegative weight vector, and a finite moment of order greater than one. Its criterion `v(alpha)=0, v'(alpha)<=0` characterizes nontrivial fixedpoint existence; its convergence theorem additionally matches the Laplace-transform asymptotic at zero. Lattice periodicity and the moment criterion are part of the result. See [the full card](../evidence/W21/cards/W21-024.md), Theorems 1–3.

Khandwawala W21-036 treats the Poisson d-th-minimum RDE for mean-field d-factor/TSP problems. On complementary CDFs, a shift-envelope method, strict sup/inf improvement, uniform tail control, and compactness prove a unique fixedpoint and convergence of even/odd iterates to opposite translates. The theorem requires the exact Poisson recursion and its integrability domain; convergence is modulo a shift. Endogeny remains open in the source for d>=2. See [the full card](../evidence/W21/cards/W21-036.md), Theorem 1 and proof §2.

### Additional smoothing-transform proof templates (W21-041/042/043/045)

These are four separate works on exact recursive operators; their overlap in topic does not create an A121/A122 recursion.

- **W21-041 (Alsmeyer–Mallein):** Theorem 1.2 classifies the source's nontrivial, nonincreasing **left-continuous** solutions of `f(t)=E∏_j f(tT_j)`; its periodic parameter `h` must also be left-continuous. The assumptions are (2),(3),(10),(11),(12), while Theorem 1.5 uses (2),(3),(14),(16) and the derivative-martingale limit. For Proposition 4.1, use its harmonic-uniqueness conclusion only as a proof-supported restricted lemma after independently proving `sup_(x>0)|G(x)|/(1+x)<∞`, along with the nontrivial centered finite-second-moment walk, right-continuity, killed boundary, and harmonicity. The source's printed supremum is over `x≤0` (where `G=0`), despite its preceding at-most-linear-growth prose; preserve that discrepancy and do not use Prop. 4.1's uniqueness without the positive-side bound. Theorem 1.5's own application does supply this gate: §5 Lemma 5.1 gives Eq. (51), `-log M^(a)(t)≤C Z^(a)(t)`; uniform integrability yields `F^(a)(t)=E[-log M^(a)(t)]≤C t^α H(-log(t/a))`. On p.29 this becomes a right-continuous killed-harmonic `g^(a)(x)≤C H(x)`, and Eq. (36) gives `H(x)∼x`. This certifies positive-side linear growth for that constructed input only, not a general repair of Prop. 4.1. The proof uses product-martingale disintegration, a many-to-one tilted walk, and Choquet–Deny.
- **W21-042 (Liang–Liu):** for `Z =d Σ_{i=1}^N A_i Z_i`, with independent iid children and `EΣA_i=1`, Theorem 1.1 transfers regular variation under `α>1`, `ρ(α)<1`, a finite `(α+δ)` weight moment, and its stated slow-variation/tail assumptions; Theorem 1.2 is one-way and has separate `ρ′(1)` and integrated-tail conditions. It is a tail theorem, not an iteration or general fixedpoint theorem.
- **W21-043 (Iksanov, arXiv v1 only):** Theorem 2 is an existence criterion for α-elementary fixed points of the point-process BRW smoothing transform, `0<α≤1`, with `β₁=α`, `EΣ X_i^α=1`, and one of the stated tilted-random-walk/integrability alternatives; its equivalent random-walk condition is full drift `S_n→−∞`, unlike Prop. 1's weaker `liminf S_n→−∞`. Neutral review confirms a source-admissible lattice example contradicts the literal full regular-variation assertion in Prop. 1(b) and the all-fixed-points claim in Prop. 3(c). Isolate only those two source-version claims: Theorem 2, Prop. 3(a)–(b), and Props. 4/6 are not refuted and retain their own hypotheses. The journal version was not compared; see the [card's adjudication record](../evidence/W21/cards/W21-043.md).
- **W21-045 (Alsmeyer–Biggins–Meiners):** Theorem 2.2 classifies decreasing solutions under A1–A5 and records geometric-span periodic factors; Laplace/survival subclasses have additional restrictions. In A4a the xlogx assumption is `E[(Σ_i T_i^α)log⁺(Σ_i T_i^α)]<∞`, applied to the total weight, alongside `m′(α)∈(−∞,0)`. Theorem 8.3's BRW disintegration/endogeny proof uses the weighted tree, stopping lines and tilted-walk structure.

All require a proved weighted independent-child or min-type identity before application. Their source-level tool eligibility is provisional pending R02; A121/A122 exact-interface flags remain false for these four. See the cards and physical-page coverage in [the source map](sources.md).

## 5. A121/A122 anchor: current proven limits

The formal problems concern the order-statistic kernel on a finite metric space and on `[0,1]`.

- In W21-001, Aldous–Feng Theorem 1 (PDF p.5, proof pp.5–6) gives a unique invariant law for each frozen `theta`, a geometric total-variation bound, and support comparisons. The same paper's Theorem 3 (PDF pp.8–9) identifies the `j=1,2`, `k=2` invariant sets; Theorem 4 classifies interval fixed laws for `k=2` as point masses or equal two-point laws (PDF p.10, proof pp.10–12). The source Lemma 5 proof has a farthest/nearest direction typo; the W21-001 card records the justified repair by first transferring invariance via Theorem 3 and then using the nearest kernel. This is not a classification for general `k`.
- The no-distance-tie continuity assertion is Proposition 2 of W21-002 (statement PDF p.7; proof pp.8–9), not a proposition in W21-001. It proves continuity only at the stated tie-free laws, and neither paper proves outer `Phi`-orbit convergence.
- W21-002 Conjecture 5 (PDF pp.13–14) is the A121 almost-everywhere convergence statement, not a theorem. Its general-k interval question remains open there. The additional parameter inequality in §7.3 (PDF p.22) is density-specific and cannot be upgraded to arbitrary singular/full-support laws.

Use these as a scope check, not as a substitute for a proof of the requested operator-specific statement. Full source cards and exact page coverage are linked in `references/sources.md`.


**Additional recursive-law comparators (W21-030/031/032/034/035).** Neininger–Rüschendorf W21-030 transfers a genuinely recursive vector/scalar sequence to an affine RDE fixed point only with L_s convergence of coefficient/toll tuples, strict Zolotarev contraction, and a low-index/self-index boundary condition; W21-031 handles a degenerate one-branch normal limit only with negative log-index drift and explicit L3/mean/variance/toll rates (its multi-branch proof is a sketch). Alsmeyer–Rösler W21-032 classifies deterministic-weight countable-sum RDEs through infinite divisibility and multiplicative harmonic measures, with continuous/discrete group and drift cases kept separate; W21-034 treats exact weighted-minimum/maximum equations, not generic laws. Knape–Neininger W21-035 derives its affine system from balanced urn trees, proves separate real/normal/complex contraction results, and includes an asymptotically phase-periodic cyclic-urn limit. These are conditional templates: no such recursive representation is known for A121/A122, and W21-035’s rotating phase is a warning against asserting a single limit. See the linked full cards in [the source map](sources.md).
