# Method guide: queue stability, polling, heavy traffic, BAR

This is a model-checking guide, not a queueing textbook. For exact theorem scope, use the numbered W14 source cards linked in `sources.md` and consult the original pages.

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

For Dai’s fluid-limit theorem ([W14-008](../evidence/W14/cards/W14-008.md)), check the complete state and assumptions (1.2)–(1.5): independent IID primitives, finite means, and unbounded spread-out interarrivals. Theorem 4.2 transfers stability of the fluid-limit model (not automatically every formal fluid-model solution) using compactness, uniform integrability, and the Lyapunov-to-Harris criterion in Theorem 3.1. For the setting of Schönlein ([W14-024](../evidence/W14/cards/W14-024.md)), check the HL/infinite-buffer model, IID mutually independent primitives, finite means, routing spectral radius below one, and unbounded/spread-out interarrivals. The associated fluid level set must also have Lipschitz, scaling, shift, closedness, concatenation, and lower-semicontinuity properties. Its construction is $W(x)=w_2^{-1}(V_L(q))+\|u\|+\|v\|$, followed by a state-dependent sampling drift and a petite sublevel set. Do not cite “fluid stable implies positive Harris” without verifying the hypotheses of the theorem being used.

For drift proofs, compute the actual one-step or generator drift, keep boundary/wasted-service terms, and specify whether the bound is a sufficient condition, necessary condition, or iff. A non-tight fluid inequality creates a gap; simulations and matched-moment examples can motivate a conjecture but cannot close it.

The converse direction has its own conditions. Gamarnik–Hasenbein [W14-011](../evidence/W14/cards/W14-011.md) prove that a non-weakly-stable associated fluid model yields a fluid path with linear growth; their stochastic instability theorem additionally assumes A, B, C and the fluid-decomposition property (FDP). FDP is proved for two-station networks, yielding rate instability under some non-idling policy. This is not a positive-Harris transience theorem for every fixed policy, and FDP remains an interface for general station count. Gamarnik [W14-039](../evidence/W14/cards/W14-039.md) separately proves algorithmic undecidability for a deterministic single-station queue under a generalized state-dependent priority rule that may intentionally idle, and for constrained homogeneous walks. The paper leaves undecidability for ordinary FIFO and ordinary priority as a conjecture; do not transfer its result to those policies.

## 3. Polling systems

At polling epochs, write the embedded state and the full recursion before manipulating PGFs. A branching-type visit replaces each initial customer independently by an offspring population. Gated and exhaustive service have standard branching-type PGFs; one-limited service generally does not. Resing ([W14-020](../evidence/W14/cards/W14-020.md)) shows that with switch-over times the visit-epoch process has immigration in every state, while with zero switch-over times immigration is only in state zero; use the corresponding distinct branching PGF formula. Its boundary correction (empty-queue term) must remain in the functional equation.

For a PGF question, distinguish a marginal PGF, a joint PGF, a queue length at a visit beginning, a queue length at a visit completion, and arbitrary-time waiting time. Do not move an equation between observation epochs without an arrival-epoch or service-time argument. In A006 the shifted bivariate equation is open; the paper's suggested shifted boundary-value problem is a research route, not a known solution.

For large switch-over time, state which quantities grow, their fixed ratios, the normalization, and the arrival law. The Poisson branching-polling limit in Boon–Boxma–Winands Eq. (7) is not a proof for renewal arrivals. The renewal conjecture needs uniform control of residual interarrival ages and a justification for the long-run/large-switch-over limit interchange. Keep their stochastic simulation evidence separate from a theorem.

Polling workload decomposition and pseudo-conservation laws control selected work or mean-waiting-time combinations; they do not determine an arbitrary joint queue-length PGF.

## 4. Heavy traffic, CRP, SSC, and stationary limits

Specify the load parameter $\epsilon\downarrow0$, the capacity boundary point, the arrival/service covariance scaling, the scheduling rule, and the stationary law $\pi^\epsilon$. State the SSC cone/subspace and prove or cite the exact stationary/process-level SSC property needed. CRP gives a one-dimensional workload; non-CRP may leave a multidimensional normal cone and multiple collapsed directions.

Separate these steps:

1. stability and stationary existence for every prelimit $\epsilon>0$;
2. tightness of scaled stationary queues and convergence of SSC residuals;
3. characterization of all subsequential limits (often via a drift equation/BAR);
4. uniqueness within the correct admissible class;
5. identification of the limiting law and any interchange of limits.

Mean drift identities, low-order moments, or polynomial test functions may determine only linear combinations of queues. They are not substitutes for joint-distribution identification. The queue-differential limit in Singh–Stolyar is a different process and scaling from the full scaled queue-length distribution. Iglehart–Whitt [W14-030](../evidence/W14/cards/W14-030.md) and [W14-031](../evidence/W14/cards/W14-031.md) give functional weak limits for multiple-channel queue processes and extensions to sequences, networks, and batches; these are process-level limit theorems under their input convergence assumptions, not stationary total-variation or coupling results. In W14-031 Theorem 1(c), the negative-drift zero limit requires the limiting net-input path to lie in $C[0,1]$ almost surely; the proof uses this to obtain C-tightness, not to assume nonnegative-path support. In W14-030, Theorem 2.2 is stated on physical p. 7 (printed p. 156), and its proof continues on physical p. 8 (printed p. 157); cite the statement page separately from the proof range. For steady-state multiclass SBP limits, Braverman–Dai–Miyazawa [W14-042](../evidence/W14/cards/W14-042.md), Theorem 5.1, needs prelimit stability, moment-SSC, the stated heavy-traffic and moment assumptions, positive-definite limiting covariance, and a tight completely-S Schur-complement system; BAR uniqueness is within that probability class.

For CRP switches, Stolyar [W14-012](../evidence/W14/cards/W14-012.md) proves a pathwise diffusion limit and process-level SSC under a one-dimensional workload condition. Its heavy-traffic assumptions control the normal projection $r(\zeta\cdot\lambda^r-\zeta\cdot\lambda)\to a$, require per-flow IID arrivals, second-moment convergence and the uniform second-tail condition (14), and do not require bounded arrivals. Theorem 1(ii) compares with any allowed discipline $G$; the stationary limit in Conjecture 1 is an RBM workload multiplied by the invariant-manifold vector, not a deterministic point. For non-CRP switches, Hurtado-Lange–Maguluri [W14-014](../evidence/W14/cards/W14-014.md) obtain tight heavy-traffic means for selected linear combinations after multidimensional SSC, while their polynomial-drift system can leave individual means underdetermined. Eryilmaz–Srikant [W14-016](../evidence/W14/cards/W14-016.md) prove moment SSC and matching first-moment bounds for JSQ/MW; neither source identifies a joint transform. The supermarket result [W14-018](../evidence/W14/cards/W14-018.md) is a contrasting deterministic infinite-ODE process limit under its own Poisson/exponential and initial-state assumptions, with no stationary interchange theorem.

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

With Dai–Harrison’s [W14-021](../evidence/W14/cards/W14-021.md) local-time convention, Eq. (7) has a factor $1/2$ on the face integrals: their Eq. (6) defines the local-time rate measure $v_i$ by $\mathbb E_\pi\int_0^t1_A(Z(s))\,dL_i(s)=t v_i(A)/2$. Thus the generic formula above uses $\nu_i=v_i/2$ when translated to their notation; retain the factor. Dai–Harrison prove the BAR converse only when the interior term is a probability density and the face terms are nonnegative integrable densities. Their broader nonnegativity claim is Conjecture 1, and the projection algorithm is conditional on its stated L2 assumptions. Dai–Williams [W14-022](../evidence/W14/cards/W14-022.md) establish SRBM well-posedness under their polyhedral geometric condition; necessity remains open for nonsimple polyhedra. Bramson–Dai–Harrison [W14-023](../evidence/W14/cards/W14-023.md) give a necessary-and-sufficient positive-recurrence classification only in dimension three. Do not transfer that converse or their LCP/spiral tests to arbitrary-dimensional SRBMs. The 2005 correction note merged into [W14-022](../evidence/W14/cards/W14-022.md) restricts Lemma 4.1 to sufficiently small $\epsilon$ and replaces the global Lemma 4.3 oscillation estimate with a local one; the authors state these corrected forms suffice for their main results. Atar–Budhiraja–Dupuis [W14-040](../evidence/W14/cards/W14-040.md) prove positive recurrence and a unique invariant probability for their constrained diffusion under the stated Lipschitz Skorokhod-map, inward-drift, and nondegeneracy hypotheses. Atar–Budhiraja [W14-041](../evidence/W14/cards/W14-041.md) give return/invariant-measure results for constrained jump diffusions under a compact-interior drift condition and the source’s additional well-posedness/moment hypotheses; Harris recurrence and invariant-law uniqueness require their extra assumptions. Bramson [W14-043](../evidence/W14/cards/W14-043.md) gave a six-dimensional example; Heyda [W14-044](../evidence/W14/cards/W14-044.md) lowers the threshold to a four-dimensional example with correlated covariance and gives a five-dimensional identity-covariance example. Heyda also proves that, for fixed four-dimensional drift and reflection data, positive recurrence can change when the covariance changes. The source leaves the four-dimensional identity-covariance counterexample open. Thus positive recurrence implies fluid-family convergence through dimension three, but this converse fails from dimension four onward; these SRBM examples do not prove queueing-network stability or B054 transform uniqueness.

The reflected diffusion's BAR and the B054 queueing-switch Eq. (7) are distinct identities. In B054, $M_k$ is a scaled unused-service boundary term from the prelimit switch. Do not relabel it as an SRBM boundary transform without a derived diffusion-limit interface. Explicit 2D stationary solutions and product-form criteria require their own assumptions; they do not automatically extend to $n$-dimensional SRBM or a queueing switch. In particular, Dai–Harrison [W14-021](../evidence/W14/cards/W14-021.md), Proposition 9, states the product-form criterion for a *standard* SRBM as defined there: $\operatorname{diag}(\Gamma)=\operatorname{diag}(R)=I$, invertible $R$, and $\max_i |(R^{-1}\mu)_i|=1$. For those normalized data the criterion is $\gamma=-R^{-1}\mu>0$ and $2\Gamma_{jk}=R_{kj}+R_{jk}$ for $j\ne k$, yielding $p_0(z)=C\exp(-2\gamma\cdot z)$. Do not insert $\gamma_j,\gamma_k$ factors into that equation or use it directly for arbitrary unnormalized $(\Gamma,R)$; if reducing general data, check Proposition 8's scaling hypotheses first.

## 6. B054 transform admissibility and uniqueness

For B054 use the exact source domain and equation in [W14-005](../evidence/W14/cards/W14-005.md). The paper's \(\mathcal L(\Theta)\) consists of nonzero bounded holomorphic continuous functions; it is an analytic class, not a synonym for “Laplace transform of a probability law.” Its Conjecture 1 asks uniqueness of \((L,M)\) in that class.

The model input must identify the switch size \(n\), queue indexing, arrival law and covariance, heavy-traffic boundary vector \(\nu\), the family \(\lambda=(1-\epsilon)\nu\) with all \(\nu_{ij}>0\), stationary laws \(\pi^\epsilon\), and the scheduling rule with the paper's SSC property. The source assumes IID-in-time arrivals, independence across input-output pairs, uniformly bounded arrivals, and an irreducible/aperiodic queue chain; state these before invoking Theorem 3. Keep its \(\Theta=\{\theta\in S:\operatorname{Re}(B^T\theta)\le0\}\) and Eq. (7) convention fixed.

Before discussing uniqueness, say which class is the target. In the literal printed Eq. (8) class, Eq. (7) is homogeneous: every nonzero scalar multiple \((cL,cM)\) of a solution is another solution, so that statement cannot be unique. Theorem 3's queue-derived \(L\) is normalized by its expectation-limit definition and has \(L(0)=1\), but Conjecture 1 does not state this condition in its analytic-class formulation. Treat this as a source-level normalization ambiguity; it is not a solution of the intended probability-class problem. One may separately ask for uniqueness in (i) an augmented analytic class with \(L(0)=1\), or (ii) the queue-derived probability-admissible class. Normalization alone removes scalar rescaling, not other non-probability analytic solutions.

For probability-admissible uniqueness, require $L$ to be a probability Laplace transform supported on the nonnegative SSC cone, with $L(0)=1$ and the relevant positivity/complete-monotonicity and exponential-domain bounds. Require each $M_k$ to come from an admissible weak limit of the prelimit measures \(\epsilon^{-1}\mathbb E_{\pi^\epsilon}[u_k\,\cdot]\); because \(u_k=1\) only when queue \(k\) has zero backlog and its scheduled service is unused, verify the limiting measure's nonnegativity, face support, tightness, and uniform integrability. Do not assume these properties from a formal solution of Eq. (7). A uniqueness theorem in the normalized analytic class would imply uniqueness in the probability-admissible subclass only if membership of every admissible pair in that analytic class is proved; that inclusion has not been verified here. The paper's class-(8) conjecture, its normalized analytic variant, and probability-class uniqueness remain distinct claims until this is settled.

Theorem 4, PDF p. 16, proves that the displayed candidate transform solves Eq. (7) under symmetric variance; identifying it as the unique heavy-traffic law requires the stated uniqueness premise. Since Conjecture 1 as literally printed has the scalar obstruction, do not present its conditional uniqueness clause as a consistent literal implication without stating the intended normalization/admissible interpretation. The three-queue and N-system uniqueness proofs are separate low-dimensional cases.

## 7. Computation and proof boundaries

Use symbolic tools to check algebraic expansions, dimensions, rank and candidate transforms; use simulation only to compare finite-sample moments/CDFs with a derived candidate law. Record seed, sample size, parameters, and diagnostics. State exactly what the run checks and what it cannot check. The saved MATLAB experiment checks one B054 candidate marginal for $n=3$; it does not verify SSC, stationarity, Theorem 4, or uniqueness.

For undecidability constructions, track the encoding of queue classes, routing, priority order, initial conditions, service-time positivity, buffer capacity, and stability definition line by line. A small perturbation of a zero service time or finite-buffer counter does not preserve an undecidability reduction unless the simulation and halting correspondence are re-proved.
