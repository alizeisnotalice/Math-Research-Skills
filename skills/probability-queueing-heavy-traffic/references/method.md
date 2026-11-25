# Method guide: queue stability, polling, heavy traffic, BAR

This is a model-checking guide, not a queueing textbook. For exact theorem scope, use the current numbered W14 identity table and R06 operational allowlist in [sources_scoped_20261116_delta01.md](sources.md), then consult the original pages.

## Current R06 operational scope

For a W14 result in this queueing tool, open its exact accepted L06 use card in sources_scoped_20261116_delta01.md. That card controls the theorem, assumptions, proof route and transfer limits available for execution. Wider source results, numerical side claims, and unreviewed theorem families are cited_background_not_operationally_certified: do not execute them or claim method credit. The aggregate contains 30 accepted source uses; it does not approve this whole skill.

## 1. Fix the model and the target first

Record: number of classes/queues and servers; routing; buffer capacities; whether time is discrete or continuous; external arrival and service processes and their dependence; switch-over/reconfiguration times; service discipline; embedded observation epoch; state variables needed for Markovianity; and the initial state.

Keep these targets distinct:

- stability as positive Harris recurrence;
- recurrence or transience of an embedded chain;
- boundedness of a deterministic queue trajectory;
- rate stability and fluid-model stability;
- weak convergence, total-variation convergence, or process-level diffusion convergence;
- stationary mean bounds versus a full joint stationary law.

Never replace a source's stability definition with a more familiar one. In particular, B157 uses deterministic boundedness for each network/policy/initial-state triplet, not positive Harris recurrence.

## 2. Stability through fluid limits and Lyapunov functions

For a multiclass network, expand the Markov state to include residual arrival/service times and other discipline state before invoking Harris-chain results. Derive fluid equations from functional strong laws, including routing and work-conserving constraints. State whether the proof concerns actual fluid limits or the larger associated fluid network; the latter can contain trajectories that are not realized stochastic limits and can be nonunique.

A fluid-stability route usually needs all of the following, stated at the right level:

1. a fluid scaling and compactness/subsequence argument;
2. a precise finite-drainage definition, e.g. $Q(t)=0$ for all $t\ge\tau\|Q(0)\|$;
3. a theorem transferring fluid stability to positive Harris recurrence under its independence, moment, irreducibility, and spread-out assumptions;
4. a Lyapunov decrease or fluid integral inequality that verifies stability for every allowed fluid solution.

For Dai's actual fluid-limit theorem, use W14-008 scoped use（本机附件：`cards/uses/W14-008.md`）: it transfers stability of the actual fluid-limit model only under its full primitive, compactness and uniform-integrability assumptions. A non-draining path in a larger associated fluid-model solution set alone proves neither an actual fluid-limit counterexample nor stochastic instability. For the standalone variable-step Foster route, use W14-024 scoped use（本机附件：`cards/uses/W14-024.md`）: require the source Borel-right strong Markov setup, finite global W >= delta_0, the all-state sampled drift, a closed petite sublevel, and the corrected return bound. The separate fluid-to-W application remains outside that row.

For Dai–Meyn's fluid/moment route (W14-009 scoped use（本机附件：`cards/uses/W14-009.md`）), take integer `p≥1` and retain A1 independent IID primitives and A2 finite `(p+1)`-st moments. Fluid stability first yields time-average p-moment bounds; positive Harris recurrence and moment convergence additionally require A3 or A3′ small-set/aperiodicity assumptions. Theorem 6.2 gives pointwise `f_p`-variation convergence with `f_p=R(1+|.|^p)` for its resolvent `R`; it is not uniform geometric convergence and does not itself prove stationary-family tightness or limit interchange. This is a G11.02/G11.03 interface, not G11.06.

For reentrant-line fluid Lyapunov arguments, Dai–Weiss W14-010 scoped use（本机附件：`cards/uses/W14-010.md`） construct the maximum of linear workload forms. The three-buffer route `1→2→1→3→1` has a uniform drainage certificate when `m₁+m₃<1` and `m₂<1`; the four-buffer route `1→2→2→1` has a non-draining periodic boundary at `m₂+m₄=1` and diverges under the exhibited work-conserving policy when `m₂+m₄>1`. Theorem 1.1's stochastic positive-Harris transfer adds independent IID primitive vectors, finite means, unbounded/spread-out interarrivals and the complete state. A fluid counterexample for one policy alone is not a stochastic transience proof.

For the converse direction, Gamarnik–Hasenbein W14-011 scoped use（本机附件：`cards/uses/W14-011.md`） use global weak fluid instability, primitive concentration and delayed-renewal bounds (A/B), level-hitting condition (C), and the fluid-decomposition property (FDP). Under these conditions they construct, for each initial state, some nonidling policy with almost-sure positive linear queue growth; FDP is proved for two stations. This does not imply instability under every policy or under the same static policy used in a different example.

For W14-016（本机附件：`cards/uses/W14-016.md`）, the accepted interface is fixed-L JSQ: route each entire incoming batch to one currently shortest queue, not sequentially within the batch. Under the card's bounded independent IID primitive, stationary-class, small-ε, and moment gates, combine its uniform perpendicular second-moment bound with the scalar quadratic drift to obtain the source/reviewer-audited upper and lower bounds for the leading total mean. This row does not admit an MW result, moving-L extension, sequential-within-batch JSQ, arbitrary full-vector-tightness claim, or limit identification; preserve the card's exact assumptions and constants.

General diffusion/Markov-chain reflection coupling and path-coupling methods have no accepted queueing-use row in this stage. Route those interfaces to their separately audited module; older queueing notes are cited_background_not_operationally_certified here.

For drift proofs, compute the actual one-step or generator drift, keep boundary/wasted-service terms, and specify whether the bound is a sufficient condition, necessary condition, or iff. A non-tight fluid inequality creates a gap; simulations and matched-moment examples can motivate a conjecture but cannot close it.

For the W14 converse use W14-011 scoped use（本机附件：`cards/uses/W14-011.md`） only for its conditional Theorems 6-7 scope. For deterministic generalized-priority undecidability use W14-039 scoped use（本机附件：`cards/uses/W14-039.md`） only for the source exact state-dependent policy class and stability definition. Ordinary FIFO and static priorities are outside that result.

## 3. Polling systems

At polling epochs, write the embedded state and the full recursion before manipulating PGFs. A branching-type visit replaces each initial customer independently by an offspring population. Gated and exhaustive service have standard branching-type PGFs; one-limited service generally does not. Resing (W14-020 scoped use（本机附件：`cards/uses/W14-020.md`）) shows that with switch-over times the visit-epoch process has immigration in every state, while with zero switch-over times immigration is only in state zero; use the corresponding distinct branching PGF formula.

For a PGF question, distinguish a marginal PGF, a joint PGF, a queue length at a visit beginning, a queue length at a visit completion, and arbitrary-time waiting time. Do not move an equation between observation epochs without an arrival-epoch or service-time argument. In A006, assume joint steady state has already been established, then keep `F_1` and `F_2` as the phase-specific joint queue-length PGFs at the exact source-defined server-arrival/polling epochs and write the embedded index explicitly. The allocated G09 interface is method-only: derive the kernel equation for that exact polling discipline, eliminate boundary traces only when the boundary equations justify it, and check that the recovered probability vector is normalized and has nonnegative coefficients. Preserve the source Eq. (4) term `F_2(z_1,0)`, which records the empty-queue boundary contribution. The general shifted G/1-L equation remains open; a Riemann–Hilbert problem with shift is a suggested analytic route, not a solved formula. This interface does not prove stability or create a stationary law. Any conversion from a polling/arrival epoch to visit completion or arbitrary time needs an independently proved epoch/Palm mapping; use the renewal/Palm material only after stationarity or that mapping has been established. Stability is a separate G11 obligation.

The current queueing rows do not operationally certify a general large-switch-over theorem or a workload decomposition beyond the exact pseudo-conservation interface below. For the precise Poisson versus own-polling-epoch distinctions in W14-001, consult its accepted same-phase PGF card; the waiting-time limit and general-renewal conjecture remain cited_background_not_operationally_certified here. General-renewal large-switch-over transfer belongs to the separately installed renewal/Palm v3 skill and is not imported as queueing-stage source credit.

The exact W14-019 pseudo-conservation use（本机附件：`cards/uses/W14-019.md`） controls the accepted selected mean-waiting-time combinations under its cyclic Poisson/stationarity gates; it does not determine an arbitrary joint queue-length PGF.

### Renewal input, Palm epochs, and state augmentation

At renewal arrivals, distinguish event/Palm epochs from the ordinary-time stationary law, and include age or residual-life information when it is needed to make the specified renewal model Markov. PASTA is Poisson-specific and requires its nonanticipation hypotheses. The general renewal/Palm, arbitrary-epoch conversion, and exact-coupling interfaces are handled by the separately installed renewal/Palm v3 skill; they are not imported here without a queueing-specific row in the current R06 allowlist.

For the two accepted A008 adaptive-polling interfaces, use W14-002's exact three-queue fluid criteria（本机附件：`cards/uses/W14-002.md`） and W14-004's exact two-queue saturated-cycle return-rate criterion（本机附件：`cards/uses/W14-004.md`）. Keep their different policies and hypotheses separate; neither card supplies a general renewal-input stability theorem.

### Exact coupling and total variation

This queueing stage has no accepted source-use row for queue-level exact coupling, CFTP, or total-variation convergence. Use the separately installed renewal/Palm v3 skill for its audited interfaces. Any broader coupling statements retained in older queueing notes are cited_background_not_operationally_certified and carry no method credit here.

## 4. Heavy traffic, CRP, SSC, and stationary limits

Specify the load parameter $\epsilon\downarrow0$, the capacity boundary point, the arrival/service covariance scaling, the scheduling rule, and the stationary law $\pi^\epsilon$. State the SSC cone/subspace and prove or cite the exact stationary/process-level SSC property needed. CRP gives a one-dimensional workload; non-CRP may leave a multidimensional normal cone and multiple collapsed directions.

Separate these steps:

1. stability and stationary existence for every prelimit $\epsilon>0$;
2. tightness of scaled stationary queues and convergence of SSC residuals;
3. characterization of all subsequential limits (often via a drift equation/BAR);
4. uniqueness within the correct admissible class;
5. identification of the limiting law and any interchange of limits.

Mean drift identities, low-order moments, or polynomial test functions may determine only linear combinations of queues. Iglehart–Whitt W14-030 scoped use（本机附件：`cards/uses/W14-030.md`） admits the specified weak finite-horizon process limit and shared-primitive transfer; W14-031 scoped use（本机附件：`cards/uses/W14-031.md`） admits the continuous-limit finite-horizon reflection interface with its separate C-tightness gate. Neither is a stationary total-variation result. Braverman–Dai–Miyazawa W14-042 scoped use（本机附件：`cards/uses/W14-042.md`） admits only the stationary residual-state event-Palm BAR in Section 6.1, under an existing stationary law and exact event-intensity/tie-order conditions; Theorem 5.1 stationary heavy traffic is cited_background_not_operationally_certified.

For CRP switches, use W14-012 scoped use（本机附件：`cards/uses/W14-012.md`） for the RP MaxWeight one-workload diffusion/SSC and workload comparison under its source projection, attraction, and moment assumptions. Its nonnegative workload normal may have zero coordinates; CRP is the strictly positive-normal special case and should not be assumed for the whole RP result. The stationary limit remains a conjecture. For non-CRP switches, W14-014 scoped use（本机附件：`cards/uses/W14-014.md`） admits selected tight heavy-traffic means through its repaired covariance interface and uniform SSC, not individual-mean or joint-transform identification. W14-016 scoped use（本机附件：`cards/uses/W14-016.md`） is the guarded fixed-L JSQ first-moment use; W14-018 scoped use（本机附件：`cards/uses/W14-018.md`） is the finite-horizon supermarket ODE limit under its complete initial-state gates.

## 5. BAR and reflected diffusion transforms

For an SRBM in the orthant, fix one convention explicitly, for example

\[
Z(t)=Z(0)+\mu t+B(t)+R L(t),
\]

where each component of $L$ is nondecreasing and increases only on its corresponding boundary face, and the columns of $R$ point into the state space. The interior generator is

\[
\mathcal A f(z)=\mu^T\nabla f(z)+\tfrac12\operatorname{tr}(\Sigma D^2f(z)).
\]

With compatible stationary boundary measures \(\nu_i\), derive the BAR from the stationary semimartingale formula:

\[
0=\int \mathcal A f(z)\,\pi(dz)+\sum_i\int_{F_i} r_i^T\nabla f(z)\,\nu_i(dz).
\]

For $f(z)=e^{\theta^Tz}$ on a domain where all integrals exist, this gives

\[
0=\bigl(\mu^T\theta+\tfrac12\theta^T\Sigma\theta\bigr)\phi(\theta)+\sum_i(r_i^T\theta)\phi_i(\theta),
\]

where $\phi$ is the stationary Laplace transform and $\phi_i$ are boundary transforms under the chosen normalization. Recheck signs if the reflection directions or BAR boundary measures use a different convention. State the transform domain and integrability conditions; the formula alone is not a uniqueness theorem.

For orthant SRBM stationary BAR use W14-021 scoped use（本机附件：`cards/uses/W14-021.md`） only for Proposition 3 necessity and Proposition 2 as a uniqueness dependency. Retain the exact one-half boundary normalization. Proposition 4 may be mentioned only as a `cited_dependency_statement_only` Dai–Kurtz nonnegative-density converse; it is not operationally established here and earns no independent proof credit. Proposition 9 product form, the numerical projection algorithm, and broader analytic/nonnegativity claims are cited_background_not_operationally_certified. Dai–Williams W14-022 scoped use（本机附件：`cards/uses/W14-022.md`） admits Theorem 1.3 well-posedness under both corrected polyhedral face conditions S.a and S.b. Bramson–Dai–Harrison W14-023 scoped use（本机附件：`cards/uses/W14-023.md`） admits only the exact three-dimensional spiral Theorem 3 obstruction at beta >= 1; the full LCP classification and iff portfolio are cited_background_not_operationally_certified. The 2005 W14-022 correction restricts Lemma 4.1 to sufficiently small epsilon and Lemma 4.3 to its local oscillation bound; use only the corrected form in the card. Atar–Budhiraja–Dupuis W14-040 scoped use（本机附件：`cards/uses/W14-040.md`） admits only deterministic constrained-ODE decay/drain and the hitting-time Lyapunov from Theorem 3.2/Lemma 3.1, not stochastic recurrence or invariant-law uniqueness. Atar–Budhiraja W14-041 scoped use（本机附件：`cards/uses/W14-041.md`） admits only Theorem 2.11(1) finite-mean reflected-Levy escape outside the negative-reflection cone; finite return, invariant existence, Harris recurrence and uniqueness are outside that row. Bramson W14-043 scoped use（本机附件：`cards/uses/W14-043.md`） admits only Proposition 3.4 sampled Foster return with the corrected M_0 and state-return index; the full six-dimensional recurrence example is cited_background_not_operationally_certified. Heyda W14-044 scoped use（本机附件：`cards/uses/W14-044.md`） admits only the fixed beta >= 3 analytic capture-to-four-dimensional stopping bound; full four-dimensional recurrence, five-dimensional threshold and covariance comparison are cited_background_not_operationally_certified. These scoped SRBM results do not prove queueing-network stability or B054 transform uniqueness.

The reflected-diffusion BAR and the B054 queueing-switch Eq. (7) are distinct identities. In B054, M_k is a scaled unused-service boundary term from the prelimit switch; do not relabel it as an SRBM boundary transform without deriving the diffusion-limit interface. W14-021 Proposition 9 and its product-form/numerical-algorithm portfolio are cited_background_not_operationally_certified for this tool; they are not operational instructions or method credit. Any special two-dimensional solution needs its own source-approved scope and exact normalization.

## 6. B054 transform admissibility and uniqueness

For B054 use the exact source domain and equation in W14-005 scoped use（本机附件：`cards/uses/W14-005.md`）. The paper's \(\mathcal L(\Theta)\) consists of nonzero bounded holomorphic continuous functions; it is an analytic class, not a synonym for “Laplace transform of a probability law.” Its Conjecture 1 asks uniqueness of \((L,M)\) in that class.

The model input must identify the switch size \(n\), queue indexing, arrival law and covariance, heavy-traffic boundary vector \(\nu\), the family \(\lambda=(1-\epsilon)\nu\) with all \(\nu_{ij}>0\), stationary laws \(\pi^\epsilon\), and the scheduling rule with the paper's SSC property. The source assumes IID-in-time arrivals, independence across input-output pairs, uniformly bounded arrivals, and an irreducible/aperiodic queue chain; state these before invoking Theorem 3. Keep its \(\Theta=\{\theta\in S:\operatorname{Re}(B^T\theta)\le0\}\) and Eq. (7) convention fixed.

Before discussing uniqueness, say which class is the target. In the literal printed Eq. (8) class, Eq. (7) is homogeneous: every nonzero scalar multiple \((cL,cM)\) of a solution is another solution, so that statement cannot be unique. Theorem 3's queue-derived \(L\) is normalized by its expectation-limit definition and has \(L(0)=1\), but Conjecture 1 does not state this condition in its analytic-class formulation. Treat this as a source-level normalization ambiguity; it is not a solution of the intended probability-class problem. One may separately ask for uniqueness in (i) an augmented analytic class with \(L(0)=1\), or (ii) the queue-derived probability-admissible class. Normalization alone removes scalar rescaling, not other non-probability analytic solutions.

For probability-admissible uniqueness, require $L$ to be a probability Laplace transform supported on the nonnegative SSC cone, with $L(0)=1$ and the relevant positivity/complete-monotonicity and exponential-domain bounds. Require each $M_k$ to come from an admissible weak limit of the prelimit measures \(\epsilon^{-1}\mathbb E_{\pi^\epsilon}[u_k\,\cdot]\); because \(u_k=1\) only when queue \(k\) has zero backlog and its scheduled service is unused, verify the limiting measure's nonnegativity, face support, tightness, and uniform integrability. Do not assume these properties from a formal solution of Eq. (7). A uniqueness theorem in the normalized analytic class would imply uniqueness in the probability-admissible subclass only if membership of every admissible pair in that analytic class is proved; that inclusion has not been verified here. The paper's class-(8) conjecture, its normalized analytic variant, and probability-class uniqueness remain distinct claims until this is settled.

Theorem 4, PDF p. 16, proves that the displayed candidate transform solves Eq. (7) under symmetric variance; identifying it as the unique heavy-traffic law requires the stated uniqueness premise. Since Conjecture 1 as literally printed has the scalar obstruction, do not present its conditional uniqueness clause as a consistent literal implication without stating the intended normalization/admissible interpretation. The three-queue and N-system uniqueness proofs are separate low-dimensional cases.

## 7. Computation and proof boundaries

Use symbolic tools to check algebraic expansions, dimensions, rank and candidate transforms; use simulation only to compare finite-sample moments/CDFs with a derived candidate law. Record seed, sample size, parameters, and diagnostics. State exactly what the run checks and what it cannot check. The saved MATLAB experiment checks one B054 candidate marginal for $n=3$; it does not verify SSC, stationarity, Theorem 4, or uniqueness.

For undecidability constructions, track the encoding of queue classes, routing, priority order, initial conditions, service-time positivity, buffer capacity, and stability definition line by line. A small perturbation of a zero service time or finite-buffer counter does not preserve an undecidability reduction unless the simulation and halting correspondence are re-proved.
