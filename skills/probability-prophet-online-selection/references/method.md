# Method and evidence boundaries

## Start with the model tuple

For each claim record a tuple such as

`(X_i independent?; identical?; order: adversarial/random/permutation/free; capacity k; decisions: adaptive/static/with cancellation; comparator; objective)`.

The tuple prevents accidental transfer between the principal W13 models:

| Problem family | Order / policy | Capacity or state | Benchmark |
|---|---|---|---|
| Multi-unit prophet (A001, B041) | fixed or sequential order; adaptive | accept at most k irreversibly | expected sum of offline top-k values |
| Prophet secretary/static threshold (A002, B042) | uniform random permutation; static threshold | k accepted values | expected sum of offline top-k values |
| Online stochastic knapsack (A005, B045) | independent known requests; adaptive | capacity one, indivisible unit-density in A005 | the stated ex-ante / fluid LP `UP(H)` |
| OCRS/resource allocation (B043–B046) | exact fixed, random, or batched arrival model | matroid, k-uniform, matchoid, or L-sparse resources | usually an ex-ante relaxation; verify per theorem |
| Dynamic matching with abandonment (B048) | continuous-time Poisson arrivals and exponential departures | agents persist until match or abandonment | omniscient long-run reward rate |
| Online minimum-cost matching on a line (B049) | sequential requests; random point sets | servers are consumed once | expected total distance cost and competitive ratio as specified |
| Cancellation prophet (B052) | independent known distributions; online recourse | one current accepted item, cancellation costs | expected offline maximum |

Never use just “online ratio” as the model description.

## A001: the finite-n versus limiting IID ratio

Let `gamma_{k,n}` be the worst-case online/prophet ratio for `n` IID nonnegative values and capacity `k`, with the distribution allowed to vary in the infimum for each n. The target is

`lim_{n→∞} gamma_{k,n} = inf_{n≥1} gamma_{k,n}` for `k>1`.

Theorem 10 of M0037 proves the equality for `k=1`, with common value `theta*≈0.745` characterized by the Hill–Kertz ODE. The proof uses an exact finite-n LP, a recurrence, and a convergence argument for that one-slot recurrence (M0037 PDF p. 31, proof pp. 58–59). It does not establish the assertion for k>1 and does not prove termwise monotonicity of `gamma_{1,n}`. M0036 Theorem 2 supplies a complementary finite-horizon statement: for every n and IID nonnegative values, an adaptive DP threshold policy has `E[max]≤beta* E[reward]`, with `beta*≈1.341` characterized by an integral equation (PDF pp. 5, 13–14). The resulting `1/beta*≈0.745` is the sharp universal constant as n varies, but it is not a proof of the k>1 infimum/limit interchange. M0036's separate `(1−1/e)` result is for nonadaptive identity-specific thresholds under heterogeneous independent values in a uniform random order (Theorem 1, PDF pp. 4–5); do not transfer that policy model to A001.

For general k, M0037 §1.2 (PDF p. 6) calls the equality a numerical observation/open problem. Its LP calculations, including n=1000, are not a proof. M0038 Theorem 2 gives a large-n lower bound

`gamma_{n,k} ≥ (1 − 24 k (ln n)^2/n) Σ_{j=1}^k theta*_j`

for fixed k and sufficiently large n, through ODE-based dual fitting (PDF pp. 3–4). M0038 expressly leaves the all-n infimum/limit equality open (PDF pp. 28–29). This asymptotic estimate has a finite-n loss and cannot settle a worst-case infimum over every n. A fixed-F extreme-value theorem also cannot control a sequence of near-worst-case distributions `F_n`.

Proof route to investigate: an all-n lower bound by the limiting value would imply the requested identity; do not add monotonicity as an unnecessary strengthening. Track any compactness, uniformity, LP-duality, or quantile-discretization assumptions in that route.

## A002: strict exceedance, ties, and two different calibrations

For a threshold `t` and randomized tie probability `p∈[0,1]`, let `B_i∼Ber(p)` be independent across i and of all values and define the effective count

`D_{t,p}=Σ_i [1{V_i>t}+1{V_i=t}B_i]`.

Its independent Bernoulli summands have probabilities `q_i=P(V_i>t)+pP(V_i=t)`. Use this same effective count for utilization, expected-demand, and stockout calibrations; strict `D_t=Σ_i1{V_i>t}` is valid only when there is no atom at t (or when p=0). Also define `UT_k(d)=min(d/k,1)` and `gamma_k=1−e^(−k) k^k/k!`.

M0062 has three distinct statements:

1. Theorem 1: static thresholds cannot guarantee above `gamma_k` uniformly, up to arbitrarily small epsilon (PDF pp. 4–5).
2. Theorem 2: a threshold with `E[UT_k(D_{t,p})]=gamma_k` guarantees `gamma_k` versus the offline top-k prophet (PDF pp. 16–18). The proof reduces to an extremal Poisson-binomial problem with Bernoulli probabilities `q_i` and uses the `Bin(n,k/n)→Pois(k)` limit.
3. Theorem 3: the separate calibration `E[D_{t,p}]=k` guarantees `min(k/(k+1),gamma_k)`; it reaches `gamma_k` for k>4 (PDF pp. 19–20).

The assigned A002 instead calibrates the stockout event `P(D_{t,p}≥k)=P(Pois(k)≥k)`. M0062 §5.2 explicitly conjectures the desired guarantee for k>1 (PDF p. 24); it is not a proved fourth theorem. For k=1 it agrees with the utilization calibration. Randomized tie breaking independently includes each equality at t with probability p, so all three calibration events use `D_{t,p}`, not raw strict exceedances.

The finite-support probe in `evidence/W13/numeric_probe_a002.py` exhaustively sums the finite outcome space for each generated independent distribution on `{0,1,H}`; probabilities and expectations are evaluated in floating point, and the common atom tie probability is found by bisection. Its output is saved in `evidence/W13/numeric_probe_a002.out`. It found no counterexample among 1,191 feasible sampled instances for k=1 (minimum ratio 0.645871), 644 for k=2 (minimum 0.793117), and only 13 for k=3 (minimum 0.912443). This is a finite numerical search over a restricted family, not an exact-arithmetic certificate or a proof; the very small k=3 sample is especially weak evidence.

## A005: report the LP gap as a gap

In the M0060 unit-density special case, each request's reward equals its size, requests are independent, capacity is one, and arrivals are indivisible. The comparator is the paper's ex-ante/flow relaxation `UP(H)`, not the expected integer offline knapsack optimum. Section 5.2 constructs a non-increasing service-probability schedule from an empty-path invariant and reports a numerical guarantee of `0.3557` relative to `UP(H)`; Proposition 3 gives an upper bound `(1−e^(−2))/2≈0.4323` for all online algorithms against the same relaxation (PDF pp. 29–31 and Appendix D.2–D.4). The interval is unresolved. Neither `≈0.4323` nor a different integral-benchmark result should be called the optimal ratio. The same paper's general knapsack OCRS has a tight `1/(3+e^(−2))≈0.319` guarantee, and its k-unit OCRS has an ODE-defined LP-tight `gamma*_k`; both depend on their own query-selectability model and online-adversary assumptions (M0060 PDF pp. 10–24).

## Online allocation and OCRS transfer audit

Before using an OCRS or prophet result, answer all of these:

- Is the offline relaxation ex-ante feasible for the same downward-closed family and same capacity constraints?
- Is each random element revealed individually or in a batch? Are the items independent, negatively correlated, or sampled from an arrival process?
- Is the order fixed adversarially, uniformly random, selected by an adversary before values, or adaptively changed after observations?
- What does “selectable” mean: unconditional marginal, conditional on prior rejections, or against an almighty/online adversary?
- Does feasibility mean a matroid, k-uniform matroid, matchoid, polymatroid, network capacity, or multiple resource usage per request?

An OCRS theorem proves only its stated arrival and adversary model. M0060's algorithms withstand an online adversary that chooses the next query without seeing future realizations, but not an almighty adversary that sees all realizations before ordering. Its k-unit γ-conservative rule chooses paths with least used capacity, while its knapsack best-fit rule chooses paths with most used capacity among those where the observed size still fits. A 1−1/e matroid random-order guarantee does not automatically extend to arbitrary L-sparse online allocation. For M0060's knapsack and B045, preserve the LP denominator and unit-density or L-sparsity hypothesis separately.

## OCRS, SRR, and resource-allocation evidence

S001 Theorem 1.4 transfers an ex-ante prophet factor to OCRS/RCRS only for the same downward-closed packing family and stated arrival model; its matroid results are 1/2 under adversarial order known to the algorithm and 1−1/e under uniformly random order. The paper leaves an almighty/online-adversary 1/2 OCRS open. Do not transfer either factor to arbitrary packing families or alter the order adversary.

S005 is Will Ma's tutorial on sequential randomized rounding. Its ratios are tied to distinct relaxations: random-order k-unit fair-offer selectability, a hiring LP, a time-indexed stochastic-knapsack LP, and a sequential-matching LP. In particular, the general random-order k-unit offer factor is 1−e^(−k)k^k/k!, Theorem 6 gives exactly half of its stochastic-knapsack LP, and Theorem 7 gives half of its sequential matching LP. These are different models and denominators from A005's unit-density online-knapsack gap.

S006 distinguishes standard OCRS/RCRS with singleton arrivals from random-element batches. Its 1/(1+L) random-element OCRS factor is tight for prime-power L, while the standard OCRS recursion strictly beats that factor; random-element RCRS has its own attenuation guarantee and open optimum. The Poisson-NRM transfer uses an inactive-oblivious RCRS, and conversion from standard to epsilon-bounded batches carries the loss in Theorem 2.8. Preserve the bundle-size bound L, batch mass epsilon, number of batches T, and fluid-LP benchmark.

## B048 and B049: separate matching models

S002's dynamic graph is a market of types with Poisson arrival rates and exponential abandonment rates; match rewards can be type-dependent. Its omniscient benchmark knows the full arrival/departure sequence and maximizes long-run reward rate. Theorem 1 gives 1/2 under equal departure rates or bipartite compatibility with common rates within each side. Theorem 3 extends 1/2 to two types with equal cross-type rewards without homogeneous rates. Theorem 2's formal upper-bound quantifier is over Markovian policies; do not silently broaden that statement. Conjecture 1 leaves arbitrary multi-type heterogeneous departures unresolved; simulations are not proof.

S003's B049 is a one-dimensional minimum-cost assignment process: request and server positions are uniform on [0,1] in the fully random model, and greedy consumes the nearest free server immediately. For n requests and n random servers, the hybrid proof gives greedy expected cost O(sqrt(n)), compared with expected offline optimum Theta(sqrt(n)). With a fixed positive linear excess fraction epsilon, the paper separately proves a constant competitive ratio; its constants need not be uniform as epsilon tends to zero. Keep separate (i) both point sets fully random, (ii) random requests and adversarial servers, and (iii) linear excess supply. In the random-requests model the ratio is Theta(log n). Appendix A.4 leaves fully random sublinear excess n+s_n with s_n=o(n) open. Cost and reward ratios cannot be interchanged without the paper's normalization.
## B052: version-sensitive result

M0065 arXiv v3, revised 2026-10-12, states an optimal characterization for every `f≥0` using a parameterized differential equation, together with a matching randomized adaptive policy and finite lower-bound instances. Its model is independent known distributions with a linear buyback penalty `f` times each canceled value; the offline comparator is the maximum realized reward. For `f≥1`, the ratio is `(1+f)/(1+2f)`. For `0<f<1` the current theorem gives an exact implicit ODE characterization; do not report “open” based on v1/v2, and do not claim an elementary closed form across the entire interval. Version and net-reward convention are material.

## B058: general monotone-norm probing gap

S019 (arXiv:2504.15547v2) studies independent known nonnegative coordinates and a prefix-closed feasible family of probe sequences. For a monotone norm objective, let n be the ground-set size and r the maximum feasible sequence length, with 2≤r≤n. Corollary 6.5 gives an adaptive/nonadaptive adaptivity-gap upper bound O(log r · log n / log log n). Section 7 reports the best known lower bound Ω(log n / log log n) and leaves the remaining O(log r) factor open. This is an adaptivity comparison between two probing policies, not the online/offline prophet ratio.

The paper resolves adjacent cases—Bernoulli probing with binary-XOS objectives at Θ(log n / log log n), and monotone symmetric norms at O(1)—but neither closes the general monotone-norm question. The B058 card records only selected theorem, open-problem and Appendix C pages; its review is pending and it is not yet a complete read. Preserve the source's prefix-closed model, independent coordinate distributions, reward f(X_P), parameter r, and adaptive/nonadaptive denominator when exploring the gap.

## Numerical and symbolic checks

Use exact enumeration or rational arithmetic for small discrete instances when they can reveal sign errors or counterexamples. Save code, input family, random seed, tolerance, and output. Clearly distinguish:

- exact finite-instance calculations;
- floating-point numerical search or ODE solving;
- a proof valid for the full theorem's quantified class.

The A002 probe is the only numerical artifact in this W13 batch. It cannot validate the universal stockout conjecture. For LP claims, a floating-point primal-dual pair is evidence only unless feasibility and the objective gap are enclosed or an exact rational certificate is produced.


## Classical stop-rule factors, multiple choices, and finite-n limits

M0034 Theorem A gives a **finite-n, IID, one-choice** comparison: for every `n>1` and nonnegative IID law with finite expectation, `E[max_i X_i]≤a_n V_n(F)`, where `a_n=1+α_n` is the paper's sharp recurrence-defined constant. Its Theorem B is a separate bounded-support additive inequality. The authors state that monotonicity and the limits of the recurrence constants are believed but unproved. Their fixed-law conclusion `E[max_iX_i]/V_n(F)→1` is pointwise in `F`, not uniform over laws. Therefore keep `inf_F V_n(F)/E[max_iX_i]` at each finite `n` separate from a limit where the near-extremizing `F` may vary with `n`. M0037's one-choice equality is a separate result; neither source proves the `k>1` infimum/limit identity.

M0048 Theorem 3.1 is a different k-choice mortal problem: independent nonnegative values, no recall, at most k stops, and objective `max` of the chosen values. Exact atom-aware `j/(k+1)` thresholds give expected reward at least `k/(k+1)` times `E[max_i X_i]`. Remark 3.2 (PDF p. 8, printed p. 1091) is an impossibility example: the prophet/mortal ratio approaches 5/4, so no uniform mortal/prophet guarantee strictly above 4/5 exists; it does not give a policy achieving 4/5. It is not the `sum` of the best k choices and not the online resource-allocation theorem.

M0051 Theorem 6's displayed strict-threshold equation `Σ_iP(V_i>τ)=k` is stated under the footnote 11 assumption of no point masses. The authors say point masses need “slight modifications”; if atoms make the strict equation unsolvable, an independent tie/quantile adjustment appropriate to the independent-item model is needed and the displayed formulation cannot be applied unchanged.

## Order and information adversaries for matroids and samples

M0049's 1/2 matroid guarantee assumes independent known nonnegative weights and immediate feasible accept/reject decisions; it works in a fixed prespecified order and against its online weight-adaptive adversary, which chooses the next item using only earlier items and values, before learning the current value. It does not cover an arbitrary permutation selected after seeing all realized values. For p matroid intersections, its simple `α=2p` choice gives `1/(4p−2)`. M0050 is a distinct limited-information model: the algorithm has one sample per distribution, and the order adversary may see the realized values before choosing order. Its `1−O(1/√k)` Rehearsal result and degree-d matching `4/27` guarantee require their stated sample/order/feasibility assumptions. Do not transfer constants between the adversary models.

M0046 is a 1992 historical survey. It may help locate proof methods and identify questions as open *at that time*, but it does not establish present-day open status; check later primary sources.


## Recent allocation results and benchmark boundaries

S013 separates three statements: large girth alone does not improve the fixed-order matroid prophet factor; k-fold matroid unions admit an almighty-adversary OCRS/profit guarantee; its bicriterion concentration bound is for down-scaled independent Bernoulli input with benchmark `E f(X)`. S014's matchoid theorem assumes independent weighted activations and an ex-ante relaxation: `1/(k+1)` for fixed adversarial order and `(1−e^(−k))/k` for uniform random order; its random-element extension additionally needs independent batches with at most one active element per batch. These are not interchangeable arrival models or integral prophet denominators.

S015 defines a worst-case stopping ratio against the **average of the top ℓ order statistics**. For single stopping, its integral equation gives the exact limiting ratio; for selecting up to k items it proves only the stated asymptotic lower bound, not tightness. Its static-threshold guarantee is a separate result. Do not replace this benchmark with the offline maximum unless `ℓ=1`.

S016 characterizes stationary OCRS implementability. Its Theorem 1 gives a 1/3-selectable stationary scheme for general graph matchings, with optimality left open; Theorem 2 proves the optimal factor only for bipartite matchings, and Theorem 3 proves the optimal factor for a k-uniform matroid. In its simulate-then-replace algorithm, an active addable element is selected with a fresh coin of probability `ρ_e/x_e`; feasibility alone does not imply acceptance. S017 compares divisible-item allocations to two different benchmarks: the 2/3 theorem is against the online philosopher optimum, while the 1/2 theorem is against the offline prophet. Keep its finite-support, independent-player, concave DR-submodular assumptions and benchmark labels explicit. These five L09 cards are full-text evidence but remain pending independent review.
