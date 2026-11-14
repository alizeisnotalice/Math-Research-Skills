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

Keep variance bounds, tail concentration, exponent existence, and exponent values separate. The BKS \(n/\log n\) variance bound is for equal-probability two-point edge weights. Damron–Hanson–Sosoe obtain the same logarithmic variance improvement for broader laws under \(\mathbb E[t_e^2(\log t_e)_+]<\infty\) and \(F(0)<p_c(d)\). Their separate concentration paper gives a \(\sqrt{n/\log n}\) scale: two-sided exponential-in-\(\lambda\) tails require an exponential moment, while the lower-tail-only inequality needs the stated \(2+\log\) moment. Neither result identifies a polynomial exponent. Chatterjee's \(\chi=2\xi-1\) relation is conditional on strong definitions/existence of the exponents and its hypotheses; it does not prove \(\chi=1/3\) or \(\xi=2/3\) for ordinary FPP.

An FPP thin-cylinder CLT applies to a specified width regime and passage-time moment assumptions. The unrestricted width threshold remains a separate problem. Exact Tracy–Widom, Airy, or \(1/3\)-fluctuation results for integrable directed LPP/KPZ models are comparison results only unless the target model is explicitly covered.

## Thin-cylinder FPP CLTs and integrable comparisons

For undirected edge FPP across \([0,n]\times[-h_n,h_n]^{d-1}\), Chatterjee–Dey Theorem 1.1 gives a sufficient Gaussian-CLT range under i.i.d. nonnegative nondegenerate weights, \(F(\lambda)<p_c(d)\), and \(E[\omega^p]<\infty\) for some \(p>2\): \(h_n=o(n^\alpha)\) with \(\alpha<1/(d+1+2(d-1)/(p-2))\). All finite moments allow every strict \(\alpha<1/(d+1)\). This is a sufficient width, not a sharp maximum. Their wider \(\xi\)-threshold theorem is conditional on unproved fluctuation/transversal exponent controls, a shape-regularity bound, and a width-monotonicity assumption for cylinder variance; retain these conditions. See worker W06-018’s theorem card and section map.

Geometric/exponential vertex-LPP and uniform-permutation LIS results (Johansson; Baik–Deift–Johansson) provide exact \(F_2\)/Airy benchmarks. They do not establish Tracy–Widom fluctuations or KPZ exponents for undirected edge FPP. W06-013, W06-018, and W06-034 cards record the exact models and scales.

## Proof-boundary checks from reviewed FPP sources

- In Damron–Hanson–Sosoe, *Subdiffusive Concentration*, Theorem 1.1 uses the threshold `λ√(‖x‖₁ / log ‖x‖₁)` (PDF p. 3). The logarithm is in the denominator. The two-sided tail uses an exponential moment; the lower-tail-only bound uses the stated `E[t²(log t)₊]` condition, and neither bound is a fluctuation-exponent theorem.
- In Cerf–Théret, *Lower Large Deviations for the Maximal Flow*, the p. 16 covering step sums local probabilities `P(G(x_i,r_i,v_i))` over a finite cover. It does not multiply probabilities of local balls or assume those ball events independent. Independence of separated layers belongs to the companion upper-deviation paper, a different proof.
- In Auffinger–Damron, *Differentiability at the Edge of the Percolation Cone*, Theorem 2.2 (PDF p. 6) gives coexistence of infinitely many infection species for the stated planar minimum-atom law class; Theorem 2.3 is a distinct infinite-ends assertion. Keep both separate from exponential vertex-clock Eden's uniform-frontier transition rule.
- For directed corner-growth comparison, W06-030 v2 contains an “Appendix A: Auxiliary technical results” on physical p. 30; its A.1 uniform ergodic theorem and A.2 gradient monotonicity lemma were read. The separate detailed coalescence proof identified by the arXiv v2 note as omitted and available in v1 remains unread; do not conflate these two appendices. W06-012 proves half-plane/subgraph results and does not supply full-plane per-direction coalescence.

## Growth, competition, and flow

“Eden growth” can mean two different boundary rules; specify which one before importing a result.

- **Vertex-clock / uniform-frontier Eden:** assign i.i.d. Exp(1) weights to sites (with the chosen convention for whether the target site's weight is included). Each distinct healthy boundary site has one fresh exponential clock, so the next site is uniform among distinct boundary sites. This is the version described in Auffinger–Damron–Hanson, *50 Years*, §6.1, PDF pp. 128–129, identity (6.1).
- **Edge-clock / exponential-edge FPP:** assign i.i.d. Exp(1) weights to edges. Each boundary edge has a rate-one clock; a healthy site with k incident edges from the infected cluster is infected at total rate k. Its next-infection probability is proportional to k. This is the rule in Couronné–Enriquez–Gerin and Bertrand–Pertinand, and it matches archived C100.

The two transition laws differ whenever a frontier site has more than one infected neighbor. Exponential memorylessness gives each rule its corresponding Markov process; it does not identify the rules with one another. Do not transfer the survey's vertex-Eden theorem or open question to edge-FPP C100 without an explicit coupling/theorem. In Bertrand–Pertinand, Theorem 1, PDF p. 2, proves the strict axis/diagonal comparison at d=22. The abstract's higher-dimensional wording should not be upgraded to an all-d≥22 claim unless the separate dimension-extension argument is stated and checked. The CEG paper states Corollary 4 for d≥35; its displayed numeric comparison is at d=35.

The cited/read W06 results do not resolve dimensions 2–21 of archived C100; this is a boundary of the current evidence set, not a claim about global open-problem status. Do not infer the Markov property for other passage-time laws. Same-speed coexistence, unequal-speed competition, and the location/shape of a competition interface are separate questions with separate assumptions.

For finite networks, max-flow/min-cut is exact. Continuum-domain undirected FPP max-flow limit theorems concern capacity cuts with surface-order scaling and moment/domain conditions. Aldous's oriented Bernoulli flow has a different graph, source/sink convention, and \(p\uparrow1\) two-limit problem; those theorems do not supply its square-root coefficient.

## Evidence discipline

For every imported claim, log theorem/lemma number, PDF page and printed page, source version, exact constants/order, and the proof steps actually used. Record any missing interface explicitly. Read the paper itself before writing a theorem card; mark merely acquired items as unread. Browse official arXiv/publisher/author pages for current metadata and later results when the answer depends on whether a question remains open.

Use MATLAB/Python for finite graph enumeration, symbolic checks, or numerical exploration when relevant. Save the script and output. Label these results as numerical or finite-volume evidence; they cannot prove an infinite-volume limit or an asymptotic exponent. See the W06 flow calculation and limitations in the worker folder.
