# W24 method-source guide

R05 accepted 31 distinct complete reads as a mother set and scoped 30 for the method-source count. This guide lists those 30 eligible sources; PGEL-029 is documented separately below as full-text background, excluded from the count. Source cards contain theorem statements, exact PDF locations, assumptions, proof chains, constants, and source-specific issues. [`reading_coverage.json`](../reading_coverage.json) gives the full physical-page/section read log. The current card review-state paragraphs may preserve an earlier helper stage; the package-level R05 binding record is authoritative for mother acceptance.

## Eligible method sources (30)

### [PGEL-001 — Benign landscapes for synchronization on spheres via normalized Laplacian matrices](../sources/cards/PGEL-001.md)

**Identity:** Andrew D. McRae; 2025; [source record](https://arxiv.org/abs/2503.18801v2); DOI 10.48550/arXiv.2503.18801. Exact local read: PDF pp. 1-28, complete; 28 physical PDF pages; [PDF](local-assets.md#asset-3dcebd9ee888).

**Reusable method:** Direct deterministic second-order landscape certificate and symmetric signed Erdős–Rényi theorem; gives a sufficient random signed regime relevant to C118 while leaving its smaller proposed threshold open.

**Scope / caveat:** Direct method-family source; C118 transfer remains auxiliary because the theorem's sufficient threshold is stronger than the problem threshold.

### [PGEL-002 — The random graph process is globally synchronizing](../sources/cards/PGEL-002.md)

**Identity:** Vishesh Jain, Clayton Mizgerd, Mehtaab Sawhney; 2025; [source record](https://arxiv.org/abs/2501.12205v1); DOI 10.1112/blms.70226. Exact local read: PDF pp. 1-11, complete; 11 physical PDF pages; [PDF](local-assets.md#asset-ebad0378aa46).

**Reusable method:** Rigorous comparison source for the distinction between global synchronization (a.e. initial phase) and landscape benignity, with a simultaneous whp theorem for the positive undirected random graph process.

**Scope / caveat:** Reusable positive-graph comparison method; not a signed-graph theorem and not an all-critical-points landscape result.

### [PGEL-003 — Expander graphs are globally synchronizing](../sources/cards/PGEL-003.md)

**Identity:** Pedro Abdalla, Afonso S. Bandeira, Martin Kassabov, Victor Souza, Steven H. Strogatz, Alex Townsend; 2026; [source record](https://arxiv.org/abs/2210.12788); DOI 10.1016/j.aim.2025.110773. Exact local read: PDF pp. 1-35, complete; 35 physical PDF pages; [PDF](local-assets.md#asset-1e5e26e42ed6).

**Reusable method:** Core positive-undirected graph method: converts spectral expansion into a.e.-initial-condition global synchronization, including the sharp connectivity-scale G(n,p) sufficient regime.

**Scope / caveat:** Direct method-family source for positive undirected phase graphs; no transfer to signed C118 or directed/nonpotential models. The 0.0816 expander constant uses the source's numerical parameter checks.

### [PGEL-004 — A global synchronization theorem for oscillators on a random graph](../sources/cards/PGEL-004.md)

**Identity:** Martin Kassabov, Steven H. Strogatz, Alex Townsend; 2022; [source record](https://arxiv.org/abs/2203.03152); DOI 10.1063/5.0090443. Exact local read: PDF pp. 1-9, complete; 9 physical PDF pages; [PDF](local-assets.md#asset-ae2eec8f6234).

**Reusable method:** Reusable deterministic spectral-norm criterion for positive undirected graph synchronization, plus an explicit ER finite-size calculation and a weaker asymptotic threshold for comparison with the later expander result.

**Scope / caveat:** Direct positive-undirected method source. The p>>log(n)/n numerical evidence is not the proved p>>log^2(n)/n result and neither transfers to signed/oriented systems.

### [PGEL-005 — Sufficiently dense Kuramoto networks are globally synchronizing](../sources/cards/PGEL-005.md)

**Identity:** Martin Kassabov, Steven H. Strogatz, Alex Townsend; 2021; [source record](https://arxiv.org/abs/2105.11406); DOI 10.1063/5.0057659. Exact local read: PDF pp. 1-6, complete; 6 physical PDF pages; [PDF](local-assets.md#asset-79c35eb7e199).

**Reusable method:** Deterministic minimum-degree criterion for global synchronization on positive undirected networks; establishes the strict finite-n threshold conversion and its 3/4 asymptotic upper bound.

**Scope / caveat:** Direct deterministic positive-undirected method source, not a random-graph theorem. The below-3/4 four-cluster discussion is explicitly only a rough sketch.

### [PGEL-006 — Synchronization of Kuramoto Oscillators in Dense Networks](../sources/cards/PGEL-006.md)

**Identity:** Jianfeng Lu, Stefan Steinerberger; 2020; [source record](https://arxiv.org/abs/1911.12336); DOI 10.1088/1361-6544/ab9baa. Exact local read: PDF pp. 1-13, complete; 13 physical PDF pages; [PDF](local-assets.md#asset-fd654c99e3e3).

**Reusable method:** Deterministic positive-undirected dense-graph landscape theorem and reusable good-vertex/Hessian test-vector proof architecture; signed C118 transfer remains unproved.

**Scope / caveat:** Dense connected simple positive-undirected model only; source parameter margins are reported as Mathematica checks without an independent interval certificate; no signed C118 transfer.

### [PGEL-007 — On the Landscape of Synchronization Networks: A Perspective from Nonconvex Optimization](../sources/cards/PGEL-007.md)

**Identity:** Shuyang Ling, Ruitu Xu, Afonso S. Bandeira; 2019; [source record](https://arxiv.org/abs/1809.11083); DOI 10.1137/18M1217644. Exact local read: PDF pp. 1-27, complete; 27 physical PDF pages; [PDF](local-assets.md#asset-f78e0b21c5ca).

**Reusable method:** Core deterministic and ER positive-graph landscape theorems; reusable rank-two Hessian, order-parameter, and uniform-net proof architecture, with an explicit boundary against signed C118.

**Scope / caveat:** Positive simple no-loop graphs only. Source PDF p.19 centered identity omits -pn under Aii=0, Xii=1; exact standalone concentration identities/constants need diagonal-convention reconciliation. Theorem 3.3 is not refuted and no signed transfer is claimed.

### [PGEL-008 — The lower bound of the network connectivity guaranteeing in-phase synchronization](../sources/cards/PGEL-008.md)

**Identity:** Ryosuke Yoneda, Tsuyoshi Tatsukawa, Jun-nosuke Teramae; 2021; [source record](https://arxiv.org/abs/2104.05954); DOI 10.1063/5.0054271. Exact local read: PDF pp. 1-10, complete; 10 physical PDF pages; [PDF](local-assets.md#asset-e34e6678bcba).

**Reusable method:** Exact Fourier/integer-program method for maximizing linearly stable twisted-state connectivity in positive circulant graphs; a constructive lower-bound method, not a signed or universal landscape theorem.

**Scope / caveat:** Symmetric positive circulant graphs and strict linear stability only; Appendix A p.9 A13-to-A14 step is unsupported as printed. Does not classify general graph landscapes, nonlinear attraction, or signed C118.

### [PGEL-009 — Dense networks that do not synchronize and sparse ones that do](../sources/cards/PGEL-009.md)

**Identity:** Alex Townsend, Michael Stillman, Steven H. Strogatz; 2020; [source record](https://arxiv.org/abs/1906.10627); DOI 10.1063/5.0018322. Exact local read: Physical PDF pp. 1-6, complete; 6 physical PDF pages; [PDF](local-assets.md#asset-a3c4a93bfc02).

**Reusable method:** Gives exact Fourier/Jacobian tests for twisted states in symmetric positive circulant graphs, a sparse O(n log n)-edge family destabilizing every twisted state, and a dense near-75%-connectivity family with unresolved zero modes.

**Scope / caveat:** The simplified Eq. (6) and its cosine proof require m>=2. At n=2 (m=1), handle K2 directly from Eq. (5), whose nonzero twist eigenvalue is 2; literal Eq. (6) extension gives 3. Strict instability still holds in this boundary case. For m>=2, Eq. (6) destabilizes twisted states in this sparse family only; other equilibria remain unclassified for general n.

### [PGEL-010 — The energy landscape of the Kuramoto model in random geometric graphs in a circle](../sources/cards/PGEL-010.md)

**Identity:** Cecilia De Vita, Julián Fernández Bonder, Pablo Groisman; 2024; [source record](https://arxiv.org/abs/2402.06744); DOI 10.1137/24M1642111. Exact local read: PDF pp. 1-15, complete; 15 physical PDF pages; [PDF](local-assets.md#asset-e78037db75cd).

**Reusable method:** Direct random geometric graph construction of stable winding-sector minima; supplies a counterpoint to global synchronization and an explicit phase-sector/boundary argument.

**Scope / caveat:** Direct method-family source. Proposition 3.1's printed normalization is contradicted by an exact expectation/variance check; the local theorem use has slack and is separately qualified in the card.

### [PGEL-011 — Guarantees for Spontaneous Synchronization on Random Geometric Graphs](../sources/cards/PGEL-011.md)

**Identity:** Pedro Abdalla, Afonso S. Bandeira, Clara Invernizzi; 2024; [source record](https://arxiv.org/abs/2208.12246); DOI 10.1137/23M1559270. Exact local read: Physical PDF pp. 1-14, complete; 14 physical PDF pages; [PDF](local-assets.md#asset-08fb950b2bff).

**Reusable method:** Provides a precise positive-graph landscape criterion and high-probability synchronization guarantees for high-dimensional random geometric graphs, with explicit degree/dimension regimes and a proof using ER sandwiching and spectral concentration.

**Scope / caveat:** Definition 1 is a landscape property for positive symmetric graphs. Theorem 3 requires d >= Cd(n^2p^2+log^4 n)log^4 n, alpha/n < p < 1/2, and np >= Cp log^2 n; Theorem 4's explicit corollary is recorded separately. No signed-graph or fixed-low-dimensional transfer is established.

### [PGEL-012 — Phase Synchronization in Random Geometric Graphs on the 2D Sphere](../sources/cards/PGEL-012.md)

**Identity:** Cecilia De Vita, Pablo Groisman, Ruojun Huang; 2025; [source record](https://arxiv.org/abs/2504.01151); DOI 10.48550/arXiv.2504.01151. Exact local read: Physical PDF pp. 1-18, complete; 18 physical PDF pages; [PDF](local-assets.md#asset-ed1e03515edd).

**Reusable method:** Gives a low-dimensional S^2 scaling-limit route from a weighted random-geometric Kuramoto system to the heat equation and an eventual-synchronization result for initial data converging to a smooth limit.

**Scope / caveat:** The paper states eventual synchronization for initial-condition sequences summably close to a smooth C^{2,alpha}(S^2) profile; it is not a landscape theorem for all equilibria. Preserve Eq. (2.6) kappa=pi/8 as source-reported. With sigma unnormalized, uniform sampling sigma/(4pi), unweighted N_i, and allowed indicator K, the exact Eq. (2.8) north-pole v=y_3 test is -1/4 while printed kappa*Delta v=-pi/4, a nonvanishing residual (pi-1)/4 against Lemma 3.7. Exact diffusivity/Theorem 2.1 quantitative reuse is pending reconciliation. The single-test coefficient 1/8 is not a general repair. Theorem 2.4 is not declared false; its proof uses the exact heat clock and needs reconciliation. Eq. (2.2) prints n epsilon/4 versus exact (n-1) epsilon/4.

### [PGEL-015 — Stability of twisted states in the Kuramoto model on Cayley and random graphs](../sources/cards/PGEL-015.md)

**Identity:** Georgi S. Medvedev, Xuezhi Tang; 2015; [source record](https://arxiv.org/abs/1407.3990); DOI 10.1007/s00332-015-9252-y. Exact local read: Physical PDF pp. 1–36, complete, read in order.; 36 physical PDF pages; [PDF](local-assets.md#asset-92684911ebdd).

**Reusable method:** Exact Fourier/Jacobian criteria for q-twist stability on symmetric Cayley graphs and a source-specific finite-horizon comparison with G(n,p); the ER proof interface remains pending because Lemma 7.3 as printed admits an exact counterexample.

**Scope / caveat:** 

### [PGEL-016 — When is sync globally stable in sparse networks of identical Kuramoto oscillators?](../sources/cards/PGEL-016.md)

**Identity:** Yury Sokolov, G. Bard Ermentrout; 2018; [source record](https://arxiv.org/abs/1812.08153); DOI 10.1016/j.physa.2019.122070. Exact local read: Physical PDF pp. 1–23, complete, read in order.; 23 physical PDF pages; [PDF](local-assets.md#asset-eadf5e48288f).

**Reusable method:** Full-text countercheck of an algorithmic/heuristic approach to nonsynchronous phase-locked states on positive undirected graphs; central Ansatz 1 is explicitly unproved and stochastic-block evidence is finite-sample numerical.

**Scope / caveat:** 

### [PGEL-017 — Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks](../sources/cards/PGEL-017.md)

**Identity:** Robin Delabays, Tommaso Coletta, Philippe Jacquod; 2016; [source record](https://arxiv.org/abs/1512.04266v2); DOI 10.1063/1.4943296. Exact local read: Physical PDF pp. 1–25, complete; all pages read in order.; 25 physical PDF pages; [PDF](local-assets.md#asset-19db7f312c13).

**Reusable method:** Exact cycle-space flow representation and cycle-only stability/count theorem; includes the finite-capacity large-gap boundary needed to prevent an unjustified all-gaps-small assumption.

**Scope / caveat:** Proposed as a reusable cycle-energy/stability source; count and nonlinear claims remain restricted to positive symmetric single-cycle dynamics. Corollary IV.4's literal fixed-injection limit equality is isolated at the 4|n endpoint pending reconciliation; its formal count, finite upper bound, and monotonicity are kept distinct.

### [PGEL-018 — Multistability of Phase-Locking in Equal-Frequency Kuramoto Models on Planar Graphs](../sources/cards/PGEL-018.md)

**Identity:** Robin Delabays, Tommaso Coletta, Philippe Jacquod; 2017; [source record](https://arxiv.org/abs/1609.02359v2); DOI 10.1063/1.4978697. Exact local read: Physical PDF pp. 1–13, complete; all pages read in order.; 13 physical PDF pages; [PDF](local-assets.md#asset-c335bfdb1e66).

**Reusable method:** For connected planar graphs, facial-cycle quantization gives a product bound under an explicit all-edge-gap condition; tree-like appendages are absorbed at their attachment vertex, while counterexamples show why the unrestricted planar case needs a separate argument.

**Scope / caveat:** Proposed as a reusable planar energy-landscape source for connected graphs, modulo one common phase, with tree-like appendages reduced as stated on p. 5; the proved global count for total stable states needs the stated graph condition, and the generic planar extension is only conjectured.

### [PGEL-019 — Graph Homology and Stability of Coupled Oscillator Networks](../sources/cards/PGEL-019.md)

**Identity:** Jared C. Bronski, Lee DeVille, Timothy Ferguson; 2016; [source record](https://arxiv.org/abs/1508.01507); DOI 10.1137/15M1034258. Exact local read: Physical PDF pp. 1-18, complete; 18 physical PDF pages; [PDF](local-assets.md#asset-3651b7667cbf).

**Reusable method:** Provides a cycle-space inertia method and low-cycle signed-Laplacian criteria in nondegenerate applications; the read arXiv v1 unrestricted Theorem 2.6 and an auxiliary bridge-edge inequality have singular/counterexample boundaries, and Theorem 2.8 is separately quarantined after exact checks.

**Scope / caveat:** In the read arXiv v1 PDF, the literal unrestricted Theorem 2.6 fails on the exact (1,1,-1/2) triangle at a singular restriction; use its proof only after independently checking Haynsworth's nonsingularity hypotheses. The p.4 auxiliary n_+(L)<=negative-bridge-count line fails on the all-negative triangle. The stable bound m_-<=C for n_+(L)=0 is independently derived in the usage card, not attributed as a verified consequence of the singular identity. Theorem 2.8 Eq. (2.3) also fails the exact unit-triangle check. The publisher full text was not read.

### [PGEL-020 — Topological States in the Kuramoto Model](../sources/cards/PGEL-020.md)

**Identity:** Timothy Ferguson; 2017; [source record](https://arxiv.org/abs/1704.02294); DOI 10.1137/17M112484X. Exact local read: Physical PDF pp. 1–10, complete, read in order.; 10 physical PDF pages; [PDF](local-assets.md#asset-15a1c7fa73c6).

**Reusable method:** Deterministic cycle-winding classification and lattice-counting results for fixed weighted graphs, including subdivision asymptotics and a sign-matched sufficient stable-state count construction; Theorem 6 is isolated from verified use.

**Scope / caveat:** 

### [PGEL-021 — Kuramoto Networks with Infinitely Many Stable Equilibria](../sources/cards/PGEL-021.md)

**Identity:** Davide Sclosa; 2023; [source record](https://arxiv.org/abs/2207.08182); DOI 10.1137/23M155400X. Exact local read: Physical PDF pp. 1-17, complete; 17 physical PDF pages; [PDF](local-assets.md#asset-1606055734a5).

**Reusable method:** Constructs connected positive unweighted graphs with stable equilibrium manifolds of arbitrary dimension, showing stable equilibria need not be isolated; not a random-graph claim.

**Scope / caveat:** Existence result for explicit connected positive unweighted graphs, not typical-graph probability or a basin-size theorem. Conjecture 1.3 remains open; larger graph eigenvalue/heteroclinic illustrations are numerical.

### [PGEL-022 — Completely Degenerate Equilibria of the Kuramoto Model on Networks](../sources/cards/PGEL-022.md)

**Identity:** Davide Sclosa; 2024; [source record](https://arxiv.org/abs/2112.12034v3); DOI 10.1088/1361-6544/ad694a. Exact local read: [1, 2, 3, 4, 5, 6, 7, 8]; 8 physical PDF pages; [PDF](local-assets.md#asset-627acd6c590d).

**Reusable method:** Theorem 8 proves a completely degenerate Kuramoto equilibrium is a nonlinear energy saddle by an explicit sign-changing cubic perturbation; Theorem 11 extends the argument to arbitrary frequencies within the stated model. Useful boundary against treating a zero/semidefinite linearization as a nonlinear stability certificate.

**Scope / caveat:** A concrete reusable nonlinear-stability failure-mode proof for a flat/zero Jacobian in the Kuramoto edge-energy model. It is not a general semidefinite-Hessian theorem and does not transfer directly to C118's signed random ensemble.

### [PGEL-023 — Equilibria in Kuramoto oscillator networks: An algebraic approach](../sources/cards/PGEL-023.md)

**Identity:** Tung T. Nguyen, Roberto C. Budzinski, Jacqueline Doan, Federico W. Pasini, Jan Minac, Lyle E. Muller; 2023; [source record](https://arxiv.org/abs/2111.02568v2); DOI 10.1137/21M1457321. Exact local read: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]; 24 physical PDF pages; [PDF](local-assets.md#asset-aa73253f1ec8).

**Reusable method:** Provides a precise eigenvector-to-stationary-state criterion, a full equilibrium classification for the complete graph, and structured phase-lag/circulant/block constructions. Useful for constructing or checking stationary points before any separate stability analysis.

**Scope / caveat:** A concrete exact construction of Kuramoto stationary points from real-matrix eigenvectors, including the phase-lag reality test and complete-graph classification. It provides no stability certificate or C118 random-signed probability result.

### [PGEL-024 — Counting equilibria of the Kuramoto model using birationally invariant intersection index](../sources/cards/PGEL-024.md)

**Identity:** Tianran Chen, Robert Davis, Dhagash Mehta; 2018; [source record](https://arxiv.org/abs/1708.09246v1); DOI 10.1137/17M1145665. Exact local read: Physical PDF pp. 1–13 (complete, in order).; 13 physical PDF pages; [PDF](local-assets.md#asset-cc7b2bdd327b).

**Reusable method:** For a deterministic graph whose support is exactly a tree or cycle, computes the adjacency-polytope normalized-volume upper bound and proves equality with the birationally invariant intersection index. The tree proof uses a unimodular monomial map to independent edge coordinates; the cycle proof uses an explicit facet-volume calculation and a generic initial-system/Bernstein argument.

**Scope / caveat:** A reusable, fully specified graph-to-adjacency-polytope root-count method for exact tree/cycle graph supports. Eligibility is proposed because the source gives explicit transformations, formulas, and proof interfaces; it remains auxiliary to C118, whose signed complete graph, probability law, real/unit-torus restriction, and stability/minimum condition are not covered.

Its inclusion in the 30-source count is based on R05’s independent scoped-method eligibility decision. The earlier R08 `quota_approved=false` remains part of the review history and is not represented as approval.

### [PGEL-026 — On the typical and atypical solutions to the Kuramoto equations](../sources/cards/PGEL-026.md)

**Identity:** Tianran Chen, Evgeniia Korchevskaia, Julia Lindberg; 2024; [source record](https://arxiv.org/abs/2210.00784v3); DOI 10.48550/arXiv.2210.00784. Exact local read: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; 30 physical PDF pages; [PDF](local-assets.md#asset-df9f694ac394).

**Reusable method:** Develops a graph-adjacency-polytope count for generic complex stationary roots, an exact circulation/balancing criterion for exceptional couplings, and explicit constructions of positive-dimensional root families.

**Scope / caveat:** A reusable exact complex-root counting and exceptional-parameter method for symmetric nonzero couplings. It counts C-star roots, not unit-torus minima, and does not transfer to C118's discrete signed ensemble without a separate proof.

### [PGEL-030 — On the Critical Coupling for Kuramoto Oscillators](../sources/cards/PGEL-030.md)

**Identity:** Florian Dörfler, Francesco Bullo; 2011; [source record](https://arxiv.org/abs/1011.3878v2); DOI 10.1137/10081530X. Exact local read: Physical PDF pp. 1–27 (complete).; 27 physical PDF pages; [PDF](local-assets.md#asset-351081c571a9).

**Reusable method:** Theorem 4.1 proves a sharp necessary-and-sufficient universal frequency-width threshold for exponential synchronization on the finite all-to-all positive complete graph, with a Dini-derivative and consensus-Laplacian proof. It is a complete-graph method boundary, not a signed random-graph theorem.

**Scope / caveat:** Proposed reusable deterministic synchronization method. The theorem is complete-graph/all-to-all with heterogeneous frequencies and does not certify every energy minimum or any signed random graph; source-count eligibility awaits independent review.

### [PGEL-031 — Bifurcations in the Kuramoto model on graphs](../sources/cards/PGEL-031.md)

**Identity:** Hayato Chiba, Georgi S. Medvedev, Matthew S. Mizuhara; 2018; [source record](https://arxiv.org/abs/1805.03786v1); DOI 10.1063/1.5039609. Exact local read: Physical PDF pp. 1–18 (complete).; 18 physical PDF pages; [PDF](local-assets.md#asset-a67b31e3310a).

**Reusable method:** The paper develops graph-sequence examples and computes the exact Fourier spectrum of a small-world graphon, giving a reusable bridge from graphon eigenvalues to quoted incoherent-state thresholds. It carefully separates this continuum method from finite-n probability claims.

**Scope / caveat:** Proposed as a graphon/spectral method source. Empirical-measure convergence, linear-stability threshold and center-manifold branches are cited from prior papers; Section 4 is numerical. No finite-n uniform, signed, or energy-landscape theorem is claimed; source-count eligibility awaits independent review.

### [PGEL-032 — Global synchronization beyond dense graphs: the case of threshold graphs](../sources/cards/PGEL-032.md)

**Identity:** Hongjin Wu, Ulrik Brandes; 2026; [source record](https://arxiv.org/abs/2511.12646v6); DOI 10.48550/arXiv.2511.12646. Exact local read: Physical PDF pp. 1–24, complete; all pages read in order.; 24 physical PDF pages; [PDF](local-assets.md#asset-d120551253df).

**Reusable method:** A structural phasor/Hessian certificate proves that every SOSP on a connected threshold graph is synchronous, illustrating a local-to-global deterministic energy-landscape argument; it is not a random-graph theorem.

**Scope / caveat:** Proposed as a deterministic landscape-method source; source-specific to connected threshold graphs and not a signed, oriented, weighted, or probabilistic result.

### [PGEL-033 — Stability of twisted states in the continuum Kuramoto model](../sources/cards/PGEL-033.md)

**Identity:** Georgi S. Medvedev, J. Douglas Wright; 2017; [source record](https://arxiv.org/abs/1606.07857v1); DOI 10.1137/16M1059175. Exact local read: Physical PDF pp. 1–18 (complete).; 18 physical PDF pages; [PDF](local-assets.md#asset-42cd16a34ff4).

**Reusable method:** Theorem 1 proves local nonlinear exponential stability in H1 or BV from a uniform all-mode Fourier gap for a fixed twist and even L2 continuum kernel. Theorem 7(a) and the fixed-r-then-small-p route remain usable; its printed uniform positive-q r,p rectangle is quarantined for the strict-gap/exponential route. This is not a finite random-graph result.

**Scope / caveat:** Proposed reusable continuum spectral-gap-to-local-nonlinear-stability method under the all-nonzero-mode strict gap, with the directly derived generator multiplier pi*lambda. For positive q, do not use the printed uniform r,p rectangle as a strict-gap/Thm1 exponential certificate; retain only fixed sufficiently small r followed by p sufficiently small depending on r and a full gap check. Equation (4.5) delta issue is separate. No finite-n probability or global energy-landscape statement is claimed; quota remains pending independent review.

### [PGEL-040 — Almost Global Synchronization of Symmetric Kuramoto Coupled Oscillators](../sources/cards/PGEL-040.md)

**Identity:** Eduardo Canale, Pablo Monzón; 2008; [source record](https://www.intechopen.com/chapters/5346); DOI 10.5772/6026. Exact local read: Physical PDF pp. 1–26, complete and read in order.; 26 physical PDF pages; [PDF](local-assets.md#asset-e7b99ed913b1).

**Reusable method:** Provides finite symmetric Kuramoto graph energy/Jacobian and exact cut-vertex, block, adjacent-twin quotient, and subdivision criteria useful as deterministic landscape structure tools; random graph transfer requires a separate probability argument.

**Scope / caveat:** R05 type audit passed this exact complete 26-page formal chapter as one independent research contribution. It is not the full edited volume. Deterministic cut-block and adjacent-twin methods may be useful; no random graph law or probability estimate is supplied. Mother binding remains pending.

R05 counts this exact SHA-256 as one complete formal publisher research contribution (canonical package type `paper`); the declared metadata remains `kind_declared=book`, `full_book_acquired=false`, and no whole edited volume is claimed.

### [PGEL-041 — On the Stability of the Kuramoto Model of Coupled Nonlinear Oscillators](../sources/cards/PGEL-041.md)

**Identity:** Ali Jadbabaie, Nader Motee, Mauricio Barahona; 2004; [source record](https://doi.org/10.23919/ACC.2004.1383983); DOI 10.23919/ACC.2004.1383983. Exact local read: Physical PDF pp. 1–8, complete and read in order.; 8 physical PDF pages; [PDF](local-assets.md#asset-9f6dfbdaac3d).

**Reusable method:** Gives deterministic connected-graph spectral-gap and grounded-coordinate methods for synchronization stability and heterogeneous fixed-point bounds; source p. 3 has an isolated weighted-gap inequality direction mismatch and the proof has an equality-endpoint gap.

**Scope / caveat:** The deterministic spectral and grounded-coordinate methods remain candidates only after independent review; the literal p. 6 tree sufficiency threshold is quarantined by the exact N=2 counterexample. No random-graph probability theorem is supplied.

### [PGEL-045 — The Kuramoto Model on the Sierpinski Gasket II: Twisted States](../sources/cards/PGEL-045.md)

**Identity:** Georgi S. Medvedev, Matthew S. Mizuhara; 2026; [source record](https://link.springer.com/article/10.1007/s00332-026-10285-5); DOI 10.1007/s00332-026-10285-5. Exact local read: Physical PDF pp. 1–33, complete and read in order.; 33 physical PDF pages; [PDF](local-assets.md#asset-6e989143cdca).

**Reusable method:** Proves deterministic SG twisted-state approximation through harmonic energy, Gamma convergence, and compactness; retained as a precise deterministic fractal boundary, not transferred as a random-graph theorem.

**Scope / caveat:** R06 adjudication supports a deterministic method contribution: harmonic extension, renormalized energy comparison, Gamma convergence, and fixed-topology minimizer arguments, with the specific derived energy completion recorded in the card. Scope is deterministic SG and conditional stated p.c.f. settings only; no random-graph theorem or C118 solution.

## Full-text background outside the quota

### [PGEL-029 — The Kuramoto model on oriented and signed graphs](../sources/cards/PGEL-029.md)

**Identity:** Robin Delabays, Philippe Jacquod, Florian Dörfler; 2019; [source record](https://arxiv.org/abs/1807.11410); full-text read, 20 pages; [PDF](local-assets.md#asset-d8e9606637df).

**Why retained:** Provides exact acyclic and oriented-cycle synchronization results for signed directed dynamics; the read-v2 DAG theorem and one-cycle LaSalle result are kept at scope, while exact signed-cycle witnesses quarantine Lemma 3.4 necessity and Proposition 3.6 exhaustiveness.

**Counting boundary:** Boundary-support source only; R05 explicitly sets current strong-tool-quota eligibility false. Full-text read and source issue are retained, but it does not count toward strong tool quota absent future operational use and review.

This source remains a genuine read and a model-boundary reference; it is not one of the 30 eligible method sources.
