# Method selection and proof obligations

Use this guide after identifying a candidate source from the [source guide](source-guide.md). The full cards and PDFs are local under `../sources/`; the complete section/page coverage is in [`../reading_coverage.json`](../reading_coverage.json).

## Record the model before choosing a theorem

For a phase system, write the equation with its actual normalization, for example
\[
\dot\theta_i=\omega_i+\sum_j K_{ij}\sin(\theta_j-\theta_i-\alpha_{ij}),
\]
and record:

- whether the graph is finite or a graphon/continuum object; simple or with loops; connected; directed or undirected; weighted or unweighted;
- whether `K_ij=K_ji`, whether edge weights can be negative, and whether phase lags permit a potential;
- the exact coupling scaling (`K`, `K/N`, or another convention), frequency assumptions, and phase domain;
- whether common phase rotation is quotiented out, and the tangent space used for Hessian or Jacobian claims;
- the probability space: graph draw, edge signs, vertex positions, or initial phases; specify which randomness each “with high probability” quantifier refers to;
- the target: existence of an equilibrium, count of roots, local stability, attraction from almost every initial phase, every second-order critical point, a strict energy gap, or a continuum spectral-gap theorem.

Do not call an oriented or nonsymmetric system a gradient flow without checking integrability. A signed but symmetric edge model may have an energy; a directed signed model generally does not inherit the same Hessian proof.

## Separate result types and quantifiers

A statement “for a random graph, with high probability, globally synchronizing” usually combines two quantifiers: probability over the graph and almost every initial phase for each graph. It is not automatically a claim that every critical point is synchronous. Conversely, an all-second-order-critical-point result is a landscape statement and is stronger than almost-every-initial-condition convergence under a separate gradient-flow theorem.

Keep these outputs distinct:

1. **Stationary-state construction/classification.** This says which configurations solve the equilibrium equations. It gives no stability conclusion unless a Jacobian/Hessian test is also proved.
2. **Strict local stability modulo rotation.** For the standard symmetric zero-lag energy
   \[
   E(\theta)=-\sum_{\{i,j\}\in E}w_{ij}\cos(\theta_i-\theta_j),
   \]
   the quotient Hessian is the weighted Laplacian with edge weights \(w_{ij}\cos(\theta_i-\theta_j)\), and the ODE Jacobian is its negative. Connectedness plus strict positivity of every effective edge weight gives a positive Hessian on \(\mathbf1^\perp\), hence a strictly stable Jacobian there. Zero modes, negative weights, phase lags, disconnected graphs, or boundary cosines need separate analysis.
3. **Almost-global synchronization.** This also needs the flow structure, convergence, and a measure-zero saddle/basin argument in the stated phase space. Do not infer it from a local Jacobian certificate.
4. **Benign landscape / every-SOSP.** Verify the objective, rank, PSD second-order condition, and symmetry quotient exactly. “No nonglobal local minima” is not the same statement as “every SOSP is global” unless the theorem proves it.
5. **High-probability graph theorem.** Preserve the graph distribution, parameter range, asymptotic regime, constants, and whether the conclusion is conditional on a deterministic graph criterion.
6. **Complex algebraic root count.** A root in \((\mathbb C^*)^n\) need not be a real phase vector on the unit torus, a stable equilibrium, or an energy minimum.
7. **Cycle/winding count.** State graph topology, cycle coordinates, admissible inverse-sine branches, frequency compatibility, and whether the map is injective or has nontrivial fibers.

## Route by model family

### Symmetric signed random landscape

For the exact independent symmetric signed Erdős–Rényi construction, PGEL-001 Theorem 3.2 gives a sufficient condition for every second-order critical point of the rank-\(r\) sphere relaxation (all \(r\ge2\)) to be globally optimal. At rank two this yields the associated phase statement. Keep the fixed \(\eta\), \(p\), \(\delta\), and logarithmic inequality from the [card](../sources/cards/PGEL-001.md); the theorem is a sufficient regime. It does not settle C118’s smaller threshold. Do not use this gradient/Hessian proof for oriented couplings.

### Positive undirected graph synchronization

PGEL-002 and PGEL-003 use expansion/global-flow arguments for positive unweighted graphs. PGEL-004 and PGEL-005 give deterministic spectral or minimum-degree criteria and random-graph applications under their own hypotheses. PGEL-006/007 provide dense-graph landscape arguments; PGEL-032 is a connected threshold-graph theorem. These do not establish signed-graph results. Keep exact degree/expansion hypotheses, `log n` powers, and source numerical checks: PGEL-003’s sharper 0.0816 regular-expander constant relies on numerical parameter checks, and PGEL-004’s proof gives \(p\gg \log^2 n/n\), not its numerically explored \(p\gg\log n/n\) scale.

### Twists, cycles, and winding

For circulant or cycle models, use Fourier diagonalization only with the source’s edge set and strict spectral sign. PGEL-008 is a positive symmetric circulant connectivity optimization, with an unsupported Appendix A step isolated in its card. PGEL-009’s simplified Eq. (6) is for \(m\ge2\); handle \(K_2\) from Eq. (5). PGEL-010 constructs stable winding-sector minima in its random geometric circle model, with its printed normalization issue isolated. PGEL-017 is single-loop; keep the formal PSD count separate from the finite-injection limit at \(4\mid n\). PGEL-018 assumes connected planar equal-frequency graphs, quotient by one common phase, and has tree-appendage reduction and all-gap/graph-condition requirements. PGEL-020 requires \(\omega\in\operatorname{im}B\); its general branch map can have fibers, while the independent injectivity/local-stability certificate is only for connected positive weights and strict principal branches.

### Spectral, topology, algebraic, continuum, and fractal methods

- PGEL-011 is a high-dimensional positive random-geometric graph theorem with explicit dimension/degree assumptions; it is not a fixed-low-dimensional or signed result. PGEL-012 is a smooth-initial-data \(S^2\) scaling route; preserve the kernel/heat-clock normalization issue and do not convert it to an all-equilibria landscape theorem.
- PGEL-019’s cycle-space inertia identity needs nonsingularity hypotheses; exact triangle examples quarantine unrestricted displays. PGEL-021 is an explicit positive-graph stable-manifold existence construction, not a typical-graph probability statement.
- PGEL-022 addresses **whole-Jacobian-zero** equilibria with a cubic energy-saddle perturbation, not all semidefinite Hessians. PGEL-023 constructs stationary states from real-adjacency eigenvectors with unit-modulus entries and the scalar reality condition; it does not certify stability. PGEL-024 is a tree/cycle isolated-root method; PGEL-026 counts generic complex torus-algebra roots under its genericity hypotheses.
- PGEL-030 is finite complete-graph phase cohesion with heterogeneous frequencies. PGEL-031 computes graphon spectra while importing several convergence/threshold results and includes numerical analysis. PGEL-033 converts a uniform all-nonzero-mode Fourier gap to local nonlinear stability for a fixed twist and even \(L^2\) kernel; do not use its printed positive-\(q\) uniform rectangle as a strict-gap certificate. PGEL-045 is deterministic Sierpinski-gasket analysis; its separately derived energy completion is limited to the stated SG/fixed-boundary/degree conditions and the stated conditional p.c.f. hypotheses.
- PGEL-040 is one complete formal publisher research contribution, counted as a paper contribution, not a whole-book read. PGEL-041 uses the stated ODE normalization; preserve its exact \(N=2\) counterexample to the printed tree threshold. PGEL-015 keeps the source date discrepancy and intended-correction-only counterexample; its Theorems 7.2/7.5 proof interfaces remain unverified. PGEL-016’s Ansatz/global-search argument is unproved; the reusable certificate is only its exact-equilibrium local Jacobian test. PGEL-020’s arbitrary-branch injectivity, weighted facet count, unrestricted Theorem 4 proof, and Theorem 6 constant remain quarantined.

## Evidence and computations

Cite physical PDF pages, not just printed page labels. The per-source card records theorem locations, assumptions, proof chain, constants, visually checked pages, and source issues. `reading_coverage.json` records complete page/section reading evidence and portable local render links.

Use the local math artifacts for exact finite witnesses, algebra, normalization comparisons, and numerical checks. Label each result by what was actually computed. A finite graph counterexample can refute a universal statement if it satisfies every literal hypothesis, but it cannot establish a random asymptotic theorem. Do not use a numeric optimization to prove an analytic bound or a source’s stated proof step.

For a missing hypothesis, stop at a conditional method: state the exact premise still needed (for example, a uniform-in-phase net bound, graph-law coupling, nonsingularity, strict quotient gap, or branch injectivity) and do not claim the target theorem.
