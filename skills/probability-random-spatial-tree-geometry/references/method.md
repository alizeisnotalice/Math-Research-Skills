# Method boundaries for W20

## Tree-biased random walks

- State the transition convention in every argument. A common rooted-tree convention assigns weight λ to the parent and weight 1 to each child, so at a vertex with d children the parent step has probability λ/(λ+d). Some authors parameterize the inverse bias or bias away from the root; do not compare thresholds until the convention is translated.
- Separate the quenched law on a fixed Galton–Watson tree from the annealed law averaging over trees. Record whether the tree is conditioned on survival and whether it has leaves. Offspring mean, extinction probability, and moment/tail assumptions often change the ballistic, zero-speed, and sub-ballistic regimes.
- Keep transience, positive speed, zero speed, a CLT, and a harmonic-measure theorem separate. A transient walk may have zero speed when leaves create deep traps; no-leaves results cannot be moved to the leaves case without checking the statement.
- A stationary law for the environment seen from the particle is a proof input with its own integrability and bias assumptions. Do not replace it by the original Galton–Watson law unless the source proves invariance/equivalence.

## Harmonic measure and tree boundaries

- Name the boundary and its metric. The visual metric on an infinite rooted tree, a level-set metric, a random edge-length metric, and Euclidean embedding metrics lead to different Hausdorff dimensions.
- Distinguish harmonic measure of a transient walk on the boundary of an infinite tree from exit measure on a finite-radius ball and from visibility/branching measure. The Curien–Le Gall random-ball setting is not the same model as biased walks on supercritical Galton–Watson trees.
- Lin (LIN2017HARMONIC) uses a walk biased toward the root: parent probability \(\lambda/(\nu+\lambda)\), each child probability \(1/(\nu+\lambda)\); transience is \(\lambda<m\). Fix λ and the root-bias convention before comparing measures. Strict dimension comparison at one λ does not establish monotonicity as λ varies. The B076 target is the harmonic-measure dimension function; results about the speed function v(λ) are only neighboring context.
- Different dimensions imply singularity only when the measures are compared on the same measurable boundary with the same metric and the relevant exact-dimension statements have been established. Do not use equal dimensions as evidence of equivalence or singularity.

## SIRSN and spatial routes

- Read the source definition before invoking the label SIRSN: identify stationarity, scale invariance, network/path uniqueness, the route-length moment condition, and the precise sampling of endpoint pairs.
- A finite expected length for one sampled route does not imply uniform integrability or finite expectation of the maximum over a countable collection of routes. Keep local window truncation, long detours, and tail bounds explicit. Aldous M0100’s \(\mathbb E D_r=\infty\) concerns the route length between a typical unordered Poisson-point pair sampled from pair intensity conditional on Euclidean separation at most \(r\); the p. 9 pair-count conversion is not a global maximum. This is neither an iid family from a shared fixed origin nor an A136 counterexample.
- Aldous's Open Problem 34 asks whether \(\mathbb E\sup_{i\ge1}\operatorname{len}r(0,U_i)<\infty\) for iid uniform \(U_i\) in the unit disk, and allows additional assumptions or a counterexample. The axiom \(\mathbb E D_1<\infty\) gives an integrable marginal route; isotropy and scaling give \(\mathbb E\operatorname{len}r(0,U_1)=\frac23\mathbb E D_1\). Neither implies the countable supremum is integrable.
- Preserve the endpoint/model distinction in later results: Kahn's Poisson-line SIRSN Theorem 5.1 controls one specified geodesic; Theorem 6.1 controls the local total length of a truncated network joining Poisson-sampled endpoints. Neither theorem states the fixed-origin iid-endpoint supremum. Kendall's earlier planar pre-SIRSN Theorem 6.4 gives almost-sure local finiteness for Poisson-pair networks, not an expected maximum route length.
- Route existence/uniqueness, local traffic intensity, expected route length, optimization attainment, large deviations, speed recurrence of a random flight, and geodesic coalescence are separate conclusions. Kendall M0096 concerns speed recurrence on a Poisson-line SIRSN; Blanc–Curien–Kahn M0102 concerns geodesic structure in a Poisson-roads metric.
- Weak convergence of network laws need not preserve unique routes, finite mean route length, scale invariance, or local finiteness without a closedness/tightness argument tailored to those properties.

## Cross-model transfer

- Growing-ball cover times, compact-group Haar seeding, Beta-splitting trees, Cayley graph biased walks, Galton–Watson trees, SIRSN Euclidean routes, and planar Poisson-road metrics are distinct models. Use source-specific hypotheses and preserve the unresolved interface in the mapping.
- For A027 tree-flow stationarity/ergodicity and A147 boundary-measure comparison, include the measure/environment transformation and its invariant σ-field explicitly. A stationary density or a dimension number alone does not prove ergodicity or mutual singularity.


## Read-source distinctions reinforced in the third batch

- Aldous–Shun M0097 uses \(R=\sup_d\rho(d)\), a worst distance-scale **average stretch**; its \(R\) is not a supremum over realized routes.
- Voss et al. M0098 is read from the 2009 Ulm author manuscript (singular “Density estimation…” title); keep it distinct from the 2011 published “Densities…” record in *Stochastic Models* 27(1), 141–167. Crossref DOI metadata lists publisher Informa UK Limited, while the official Ulm publication list independently matches the published citation. The paper studies a Palm-typical LLC-to-HLC connection in a telecom subscriber-line model, not a route maximum.
- Coupier–Hirsch M0099 proves fixed-direction geodesic coalescence and expected sublinear branch counts for Poisson Delaunay/RNG FPP; those are not path-length maximum bounds.
- Hirsch–Willhalm M0101 treats upper deviations of a normalized sum of power-weighted edges under (FIN), (FIN2), (STA), (CON), and (INF); its local condensation cost is a different random variable from the A136 endpoint maximum.
- Aïdékon AIDEKON2014SPEED computes speed for a toward-root biased walk on a surviving finite-mean Galton–Watson tree in \((\lambda_c,m)\); speed formulae do not establish harmonic-measure-dimension monotonicity.


## Newly verified tree-source boundaries

- Lyons's branching-number criterion is about reversible walks on trees and uses finite-energy flows. For the canonical parent-weight λ walk, only the strict regimes \(\lambda<\operatorname{br}(T)\) and \(\lambda>\operatorname{br}(T)\) are decided by the cited threshold; do not infer the critical case.
- Peres–Zeitouni use parent weight λ, no leaves, and an exponential offspring-moment assumption. In the marked-ray root change, preserve the exact density \((m+d_o)/(2d_o)\), with IGW root law \(kp_k/m\) and IGWR root law \((m+k)p_k/(2m)\); the random denominator \(2d_o\) is part of the normalization. Ben Arous–Fribergh–Gantert–Hammond use child bias \(\beta\) away from the root, \(p_0>0\), and deep traps. In their sub-ballistic regime \(\beta f'(q)>1\), a direct expected-generation calculation gives divergent mean for the raw Q-trap root-relative conductance mass, while the finite variable is the separately defined bottom-relative \(S_\infty=2\sum_i\beta^{-i}(1+\Lambda_i)\), proved finite in expectation by Lemma 3.5 and Proposition 3.1. These are different regimes and normalizations; do not compare them by swapping parameter names.
- Curien–Le Gall concern a critical GW tree conditioned to reach a finite generation and its continuum reduced-tree boundary; the walk is simple random walk. Do not identify this measure with the boundary measure of a transient biased walk on an infinite supercritical GW tree.
- Last–Penrose Chapter 4 defines factorial measures by ordered tuples of distinct occurrence indices; repeated spatial locations can still occur for a non-simple counting measure. Theorem 4.5 deletes one selected occurrence at a time on its left side and leaves the configuration unchanged on its right side. These Mecke/factorial identities support expected Poisson counts but do not control dependence among shared-network routes or an iid-endpoint supremum.

## R04 round-four source normalization checks

- For M0108, the complete 160-page local read is arXiv:1511.03262v2, title page dated 26 Sep. 2016; the book was later published in 2017 as University Lecture Series 68. `full_book_acquired=true`, but do not label the local copy as the typeset publisher file. Separate its lattice-FPP time constants, shape limits, and max-flow/min-cut (a capacity-weighted cutset functional) from route-length suprema in SIRSN. None of these theorems bounds A136 without a new model-transfer argument.


## W20 batch-five method boundaries

- LPP1996 Theorem 5.1 concerns the dimension at each fixed λ and mutual singularity between distinct harmonic measures. Mutual singularity does not order dimensions; the paper's §6 explicitly leaves parameter regularity open. LPP1997 Question 3.4 asks monotonicity on GW trees. Its general-tree counterexamples and one Fibonacci-tree formula do not settle the GW class.
- Bowditch–Tokushige's Girsanov/regeneration method differentiates speed under finite-exponential-offspring and λ in ((\sqrt{\lambda_c},\mu)), where regeneration gaps have uniform (2+\epsilon) moments. The object being differentiated is υλ. Reusing the argument for harmonic dimension requires a separate differentiable invariant boundary-flow law and estimates; do not imply those are provided.
- Aldous's frozen-core connectivity theorem bounds a Poisson pair-sum of route lengths. His shape theorem gives L1 convergence for pair-summed deviations under a uniform L2 pair-sum assumption. The first is not a fixed-origin endpoint maximum; the second's a.s. shape property is conjectural in that paper. Neither result controls (E\sup_i\operatorname{len}r(0,U_i)).
- The LPP 1997 PDF is the complete independently authored edited-volume contribution, physical pp. 1–16 / printed pp. 223–238. It is classified as paper/fulltext_read; the containing volume was not acquired, so this does not claim a whole-book read.


## W20 final-batch model boundaries

- Mehrdad–Sen–Zhu uses childward β bias on no-leaves GW trees and compares speed across stochastically ordered progeny laws only above a high-bias threshold. Translate β to the reciprocal parent-weight convention only after checking direction; speed ordering does not imply harmonic-dimension ordering.
- Faraud–Hu–Shi uses iid random vectors of child-to-parent transition ratios. Its (log n)^3 theorem is for the maximum depth of one recurrent RWRE trajectory up to time n. It is not a maximum over sampled endpoints or a tree-boundary harmonic measure.
- Aïdékon 2008/2010 use elliptic random environments on no-leaves GW trees. Their Λ speed criterion, displacement exponent, regeneration-time tails and quenched/annealed hitting-time rate functions are separate results. They do not prove deterministic λ-biased harmonic-dimension monotonicity.
- Keep the GW setting distinct from the C139 Cayley-graph question: no result in these papers transfers dead-end depth or tail estimates to the target group graph.


## Mapping status boundary

The W20 mapping ledger distinguishes exact primary-question sources from theorem coverage. A136 and B076 have exact source/model records but unresolved targets. All other former direct associations are explicitly candidate-scope, auxiliary-only, or not covered, with read-source uses and missing interfaces recorded per problem. Do not promote a matrix association or an auxiliary comparator to direct theorem support.
