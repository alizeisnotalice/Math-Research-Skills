# Method notes

## Identify the mathematical object first

Before invoking a theorem, record:

1. The graph/lattice, dimension, edge or vertex weights, and whether paths minimize or maximize.
2. The law: i.i.d. or stationary dependent; nonnegative or strictly positive; continuous, atomic, or mixed; atom at zero/minimum; required moment or exponential-tail condition.
3. The endpoint regime: point-to-point, point-to-boundary, cylinder crossing, half-plane, a fixed direction, or a random direction.
4. The exact quantifiers and limit order. “For every fixed direction, almost surely” does not assert one event on which every direction is unique. A limit in endpoint distance need not be uniform over direction or over the weight law.

## Time constants and shapes

Use subadditive ergodic results only after checking stationarity/ergodicity and the integrability condition. In i.i.d. nearest-neighbor FPP on \(\mathbb Z^d\), the standard time-constant condition can be stated using the minimum of \(2d\) independent edge weights; the shape theorem needs its own \(d\)-th-moment condition and positivity \(F(0)<p_c\). Do not replace these with \(E\tau_e<\infty\) without a cited theorem. Existence of a norm/limit shape does not compute its values, prove strict convexity, or give a fluctuation exponent.

For critical FPP, specify the dimension, lattice, and distribution. The planar square-lattice invasion/RSW arguments in the 2D critical source do not transfer to the 3D Bernoulli question. A zero time constant is compatible with passage times that diverge logarithmically, remain bounded, or have other distribution-dependent behavior.

## Geodesics and Busemann functions

Distinguish a finite minimizer from an infinite ray, a doubly infinite geodesic, and a ray with an asymptotic direction. Compactness gives rays only when the assumptions prevent minimizing paths from escaping through arbitrarily long zero-cost segments. Uniqueness of finite geodesics often uses continuous weights, but a continuous law alone does not guarantee uniqueness of all infinite rays.

For a specified ray \(x_0,x_1,\dots\), the ray Busemann function is a limit of differences \(T(x,x_n)-T(y,x_n)\); its existence follows in the basic setup from monotonicity and boundedness along that ray. This does not imply the limit is independent of the chosen ray, exists for every direction, or is stationary. Some planar results construct subsequential limits in distribution and then use shape differentiability to obtain directed rays and coalescence. Mark the exact shape regularity and continuity assumptions.

Planar ordering and competition-interface arguments are not dimension-free. If a theorem states uniqueness/coalescence for a deterministic full-measure direction set, do not present that theorem as already covering every fixed direction. The archived C097 target is the pointwise quantifier: for each deterministic direction fixed in advance, uniqueness holds almost surely; the probability-one event may depend on that direction. C097 does **not** ask for one common probability-one event on which uniqueness holds simultaneously for all directions. Directed exponential LPP results use vertex weights, coordinatewise paths, and max-plus recursion; they do not establish the matching claim for undirected edge FPP.

For directed-polymer/LPP cocycle variational formulas, check each hypothesis in the theorem itself. Georgiou–Rassoul-Agha–Seppäläinen, Theorem 4.4 (W06-033, physical p. 17) assumes \(V_0\in\mathcal L\), ergodicity, \(g_{pl}^{\beta}(0)<\infty\), and velocity \(\xi\in\operatorname{ri}U\). The finite zero-tilt value is an explicit assumption, separate from class-\(\mathcal L\) membership; do not infer it from the class condition. This directed-path formula does not transfer directly to undirected edge-FPP.

## Variance, KPZ, and limit theorems

Keep variance bounds, tail concentration, exponent existence, and exponent values separate. The BKS \(n/\log n\) variance bound is for equal-probability two-point edge weights. Damron–Hanson–Sosoe obtain the same logarithmic variance improvement for broader laws under \(\mathbb E[t_e^2(\log t_e)_+]<\infty\) and \(F(0)<p_c(d)\). Their separate concentration paper gives a \(\sqrt{n/\log n}\) scale: two-sided exponential-in-\(\lambda\) tails require an exponential moment, while the lower-tail-only inequality needs the stated \(2+\log\) moment. Neither result identifies a polynomial exponent. The current R04 scope for Chatterjee (W06-019) admits only the lower exponent-index relation \(\chi_a\ge 2\xi_b-1\), under the paper's nearly-gamma law, local exponential-moment condition, and upper/lower index definitions. The reverse relation and equality are outside this accepted use; exponent existence and numerical KPZ values are not established for ordinary FPP.

An FPP thin-cylinder CLT applies to a specified width regime and passage-time moment assumptions. The unrestricted width threshold remains a separate problem. Exact Tracy–Widom, Airy, or \(1/3\)-fluctuation results for integrable directed LPP/KPZ models are comparison results only unless the target model is explicitly covered.

## Thin-cylinder FPP CLTs and integrable comparisons

For undirected edge FPP across \([0,n]\times[-h_n,h_n]^{d-1}\), Chatterjee–Dey Theorem 1.1 gives a sufficient Gaussian-CLT range under i.i.d. nonnegative nondegenerate weights, \(F(\lambda)<p_c(d)\), and \(E[\omega^p]<\infty\) for some \(p>2\): \(h_n=o(n^\alpha)\) with \(\alpha<1/(d+1+2(d-1)/(p-2))\). All finite moments allow every strict \(\alpha<1/(d+1)\). This is a sufficient width, not a sharp maximum. Their wider \(\xi\)-threshold theorem is conditional on unproved fluctuation/transversal exponent controls, a shape-regularity bound, and a width-monotonicity assumption for cylinder variance; retain these conditions. See the W06-018 current scope（本机附件：`references/current_scopes.md`）.

Geometric/exponential vertex-LPP and uniform-permutation LIS results (Johansson; Baik–Deift–Johansson) provide exact \(F_2\)/Airy benchmarks. They do not establish Tracy–Widom fluctuations or KPZ exponents for undirected edge FPP. W06-013, W06-018, and W06-034 cards record the exact models and scales.

## Proof-boundary checks from reviewed FPP sources

- In Damron–Hanson–Sosoe, *Subdiffusive Concentration*, Theorem 1.1 uses the threshold `λ√(‖x‖₁ / log ‖x‖₁)` (PDF p. 3). The logarithm is in the denominator. The two-sided tail uses an exponential moment; the lower-tail-only bound uses the stated `E[t²(log t)₊]` condition, and neither bound is a fluctuation-exponent theorem.
- In Cerf–Théret, *Lower Large Deviations for the Maximal Flow* (W06-016), the p. 16 covering step sums local probabilities `P(G(x_i,r_i,v_i))` over a finite cover. It does not multiply probabilities of local balls or assume those ball events independent. For the companion upper-deviation paper W06-017, retain the independently reviewed scope: local cylinder upper-tail inputs plus optimization over order-`n` disjoint connector-candidate sets; connector-capacity events are independent of the layer choice, while cylinder deviations enter through union bounds and imported volume estimates. Do not use the old card’s broad parallel-layer-probability-product wording as the proof interface. The exact reader overlay and R04 binding are in the W06-017 current scoped use（本机附件：`references/current_scopes.md`）.
- In Auffinger–Damron, *Differentiability at the Edge of the Percolation Cone*, the current R04 scoped-use overlay admits Theorem 2.1 and Corollary 2.1 (PDF p. 4): endpoint differentiability and accumulating extreme points under the planar minimum-atom law. Theorem 2.2 (PDF p. 6), on coexistence of infinitely many species, and Theorem 2.3, on infinite ends, remain in the R03-era source card but are outside this batch's direct proof-use certification. Keep all FPP infection-time results separate from exponential vertex-clock Eden's uniform-frontier transition rule; see the W06-011 current scope（本机附件：`references/current_scopes.md`）.
- For directed corner-growth comparison, W06-030 v2 contains an “Appendix A: Auxiliary technical results” on physical p. 30; its A.1 uniform ergodic theorem and A.2 gradient monotonicity lemma were read. The separate detailed coalescence proof identified by the arXiv v2 note as omitted and available in v1 remains unread; do not conflate these two appendices. W06-012 proves half-plane/subgraph results and does not supply full-plane per-direction coalescence.

## Growth, competition, and flow

“Eden growth” can use either of two clock conventions. With one rate-one exponential clock per distinct exposed vertex, the next vertex is uniform among the current frontier sites. With one rate-one exponential clock per exposed edge, a vertex with `k` incident edges from the infected cluster has total infection rate `k`, so the next infection is weighted by its number of infected neighbors. These are definitions of different processes, not interchangeable Eden theorems. Archived C100 uses exponential edge FPP. For theorem transfers, keep the exact scope of the edge-clock results: Bertrand–Pertinand Theorem 1, PDF p. 2, states the strict axis/diagonal comparison at d=22. This is the source-stated theorem; its finite recursion/table is reported on PDF p. 9, and L04 has not independently rerun the authors’ C++ computation, so this package contains no independent d=22 computational certificate. The abstract's higher-dimensional wording should not be upgraded to an all-d≥22 claim unless a separate dimension-extension argument is stated and checked. Couronné–Enriquez–Gerin's current accepted use is the constructive edge-FPP path upper bound in Theorem 1, PDF pp. 3–4, together with its independent-slab extension; the corrected Theorem 2 constant contains `sqrt(alpha_*^2-1)/(2sqrt(d))`. Its Corollary 4/d≥35 statement and displayed d=35 comparison are source-reported side branches, not independently certified by the displayed numerical comparison. See the W06-007 current scope（本机附件：`references/current_scopes.md`） and W06-008 current scope（本机附件：`references/current_scopes.md`）.

The cited/read W06 results do not resolve dimensions 2–21 of archived C100; this is a boundary of the current evidence set, not a claim about global open-problem status. Do not infer the Markov property for other passage-time laws. Same-speed coexistence, unequal-speed competition, and the location/shape of a competition interface are separate questions with separate assumptions.

For finite networks, max-flow/min-cut is exact. Continuum-domain undirected FPP max-flow limit theorems concern capacity cuts with surface-order scaling and moment/domain conditions. Aldous's oriented Bernoulli flow has a different graph, source/sink convention, and \(p\uparrow1\) two-limit problem; those theorems do not supply its square-root coefficient.

## Evidence discipline

For every imported claim, log theorem/lemma number, PDF page and printed page, source version, exact constants/order, and the proof steps actually used. Record any missing interface explicitly. Read the paper itself before writing a theorem card; mark merely acquired items as unread. Browse official arXiv/publisher/author pages for current metadata and later results when the answer depends on whether a question remains open.

Use MATLAB/Python for finite graph enumeration, symbolic checks, or numerical exploration when relevant. Save the script and output. Label these results as numerical or finite-volume evidence; they cannot prove an infinite-volume limit or an asymptotic exponent. The bundled finite calculations are examples only; their outputs cannot prove an infinite-volume limit or an asymptotic exponent.


## General directed vertex-LPP tail comparison (new L04 draft note)

Ganguly–Hegde (2024), Theorem 1, gives an upper-tail bound under Assumptions 2 and 3a for iid nonnegative **vertex-weight** up-right LPP. Preserve the exact range θ₀ ≤ θ ≤ r^ζ, with ζ=ζ(α)∈(0,2/25], tending to zero as α→0 and equal to 2/25 for α≥1, and the exponent θ^(3/2)(log θ)^(-1/2). Assumption 2 includes parabolic expected profile curvature and a non-random r^(1/3) fluctuation window; Assumption 3a is a direction-uniform stretched-exponential upper-tail input. Do not shorten this to a pure optimal 3/2 tail or to the entire moderate-deviation range.

Their Theorem 1.11, under Assumptions 2 and the full Assumption 3, gives a high-probability construction of pairwise vertex-disjoint up-right paths with specified endpoints, transversal bounds and a collective weight lower bound. It does not assert that each constructed path is an individually maximizing geodesic. The construction uses vertex weights and is not a capacity flow covering a prescribed set of closed edges. The R04-accepted W06-029 conditional comparison（本机附件：`references/W06-029_use.md`） binds the statement to the 51-page arXiv v2 PDF and exact SHA. It is an additional directed vertex-LPP comparison outside the original 30-work baseline, not a flow or edge-FPP theorem.


## Directed edge-flow and poset boundary

Directed Bernoulli edge-flow, poset-cover identities, and sparse-Poisson limits are treated in the separate `probability-flow-poset-growth` entry. Keep that model separate from undirected edge-FPP and the continuum-domain capacity-flow results here. W06-039 contributes only its accepted continuum Poisson-chain benchmark; it does not prove the discrete boundary-preserving edge-flow comparison. The current scoped-use register（本机附件：`references/current_scopes.md`） records the exact interface and remaining gap.
