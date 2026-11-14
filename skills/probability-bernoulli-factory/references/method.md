# Method notes

## Choose the correct factory model

Record whether the procedure sees iid unknown-bias tosses only or may also use independent fair coins/uniforms. Record whether output is exact, the stopping-time filtration, and which tosses `N` counts. A theorem for a fair-coin-assisted construction or an exponentially tailed (“fast”) subclass cannot silently be transferred to every a.s.-terminating factory. Holtz–Nazarov–Peres uses paired p-coin/fair-coin input stages; its open moment question on PDF p.28 describes `N` as counting tosses of both kinds. Preserve this convention and convert to p-only or primitive-toss cost only after stating the implementation’s per-stage cost.

## Exact envelope mechanism

For a factory on the unknown-bias coin, write the stage-n lower and upper Bernstein polynomials as

`g_n(p)=Σ_k binom(n,k)a(n,k)p^k(1-p)^(n-k)` and
`h_n(p)=Σ_k binom(n,k)b(n,k)p^k(1-p)^(n-k)`.

The discrete coefficients must satisfy the paper's range, integrality, and degree-elevation consistency conditions. Then `g_n<=f<=h_n` and `P_p(N>n)=h_n(p)-g_n(p)`. Conversely, a valid nested envelope construction yields an exact factory with that tail. Keep the envelope criterion separate from conclusions derived under extra uniformity or smoothness assumptions.

For integer-valued `N>=0` and `r>0`, use

`E[N^r]=Σ_{n>=0} ((n+1)^r-n^r) P(N>n)`.

The weights are asymptotic to `r n^(r-1)` for large n, not `n^r`. Check endpoint conventions if the source starts counting at one. A pointwise bound with a p-dependent constant gives pointwise moments only; a uniform moment claim needs a uniform bound or an appropriate uniform-integrability/tail condition.

## Finite coin-flipping degree

For a finite event of depth N, count accepting words by their number of heads. Its unnormalized degree-N Bernstein coefficients `a_{N,j}` are integers with `0<=a_{N,j}<=binom(N,j)`. Conversely, such coefficients specify an event by choosing that many words from each head-count class. For a proposed polynomial, degree elevation gives an exact finite-N test. Wästlund's integer-polynomial characterization establishes that eligible integer-coefficient polynomials have some finite event representation; his compactness theorem establishes only finiteness of the maximum degree at each fixed algebraic degree.

Keep the following claims apart:

- existence of some finite depth;
- the least depth for one polynomial;
- finiteness of the maximum over all eligible degree-d polynomials;
- a sharp explicit upper bound or exact maximum `N(d)`.

Only the first three are supported by the read Wästlund manuscript; the last is the A202 target.

## Regularity and moment limits

Nacu–Peres prove smoothness consequences from uniform moment-tail decay, not from bare pointwise finiteness of moments. Holtz–Nazarov–Peres prove a tail-rate characterization for noninteger smoothness order `α`, with `Δ_n(p)=max(sqrt(p(1-p)/n),1/n)` and a uniform-in-p tail constant under their fair-coin-assisted model. For fixed interior p, the rate is `O(n^{-α/2})`; at endpoints it is `O(n^{-α})`. Their fair-coin-assisted coefficient condition (ii′) requires multiples of `2^{-n}`, unlike the pure p-coin integer condition (ii). By the standard tail formula the interior bound implies finite r-th moments for `r<α/2` under the theorem’s stage-cost convention. Their integer-order sufficiency is conjectural, not proved.

Mendo's sequential Cramér–Rao lower bound requires differentiability and the paper's fast-factory/sequential-estimator hypotheses. The reverse-time martingale construction of Łatuszyński et al. does not assume pathwise `L_n≤s≤U_n`; it requires ordered bounds, expectation limits, and stated reverse-time conditional inequalities. Its Theorem 2.7 assumes uniform boundedness in `[-M,M]` and affine rescaling, not a variance condition. Algorithm 4’s tail identity counts iterations; translating it into input-toss moments requires stage-cost control, except where the Bernoulli-factory specialization explicitly ties stage n to a p-coin prefix. Neither source closes the general C204 classification.

Do not use the parenthetical tail identity printed with the C204 question in HNP PDF p.28 as the standard moment formula; it is mathematically different. See the exact check in `evidence/W17/experiments/exact_checks.out`.


## Fixed depth, expected cost, and iteration cost are different quantities

Goyal–Sigman Theorem 2.3 gives a fixed computable-in-advance sample-size criterion: normalized Bernstein coefficients must lie in `[0,1]`; it does not cover random stopping. Wästlund’s finite-event criterion uses integer unnormalized coefficients. Keep these two coefficient conventions distinct.

Huber’s 2016 and 2017 papers give target-specific linear-factory cost results on their stated domains. Huber (2016) Theorem 1's exact factory and `9.5 C/ε` expected-cost upper bound remain usable. Do **not** import its Theorem 2 lower bound: Lemma 11's `(√ε,1/4)` precision claim has an exact admissible counterexample (`C=2,p=1/4,ε=1/100`, success `35/256<3/4`), so the proof route is not certified; the displayed Theorem 2 and p.17 proof also differ. In Huber (2017), Lemma 10's heading prints 7.67 while the proof sums to `469/62≤7.57`; retain that source discrepancy. Flegal–Herbei Theorem 1 prints a tail indexed by `n` called iterations, while the algorithm doubles a known p-prefix and Appendix A derives the envelope gap at that prefix index. The paper does not reconcile the indices, so do not present the display as an accepted iteration- or input-toss tail until the indexing is resolved.

Mossel–Peres’ finite-automaton and pushdown-automaton results are kept as an isolated B201 boundary: finite automata give rational functions, while pushdown simulation implies algebraicity, but the algebraic-to-pushdown converse is not proved. This source is not used to open A203 or to claim progress on A202/C204.


Theorem 4 of Mendo (2019) assumes condition (12), `f'(p)=Ω(f(p)/p)` as `p↓0`, but does **not** require condition (11), `f(p)/p→∞`; the proof substitutes the derivative bound into Theorem 3's sequential Cramér–Rao inequality. Corollary 1's order-optimality statement for the specified power-series algorithm requires both (11) and (12). Keep those statements separate.

Peres (1992) and Stout–Warren (1984) concern extracting fair bits or a finite uniform outcome from biased coin tosses. Peres's exact recursion applies to pairwise XOR/equality indicators and equal-pair retained bits; its entropy result is an almost-sure long-run rate. In Stout–Warren, Theorem 1 improves `Q₃` uniformly, Theorem 2 excludes a specified continuation-sequence class, and Theorem 3 proves no E-optimal algorithm exists; do not conflate these claims. Their rates and expected costs for specified extraction trees are not higher-moment bounds for a general Bernoulli factory. If a construction uses auxiliary fair bits/uniforms, conversion to p-only input cost must be proved for the actual composed stopping rule. Beskos–Roberts (2005) use an iid sequence of uniform points on a rectangle and a Taylor/factorial event construction; Beskos–Papaspiliopoulos–Roberts (2006) use Poisson processes in their exact-diffusion algorithm. Their computational counts are not coin-toss counts.

Jacob–Thiery define an `f`-factory for arbitrary iid input laws supported on `X`, with output a nonnegative unbiased real estimator. Their random truncation theorem also requires `N` independent of `(S_n)`. Their real-line impossibility proof uses two distinct fixed means and rare contamination making any finite prefix agree with high probability; it does not assume the means match. Their bounded-interval criterion is not the existence criterion for a Bernoulli-valued output under p-coin tosses. Use it only as a model boundary unless a cost- and output-preserving reduction is supplied.


## Auxiliary exact-simulation constructions

Morina et al. (X007) give a reversible CFTP chain once a valid fine connected ladder is supplied. Their Theorem 3.1 is literally stated for all open-simplex rational maps, but its displayed proof constructs a finite fixed aggregation of ladder coordinates whose common denominator has no zeros on the closed simplex. R02 exhibited a rational map with incompatible boundary path limits and an open-positive homogeneous polynomial that fails the claimed Pólya coefficient conclusion, so use this conversion only for verified closed-positive-denominator/nonnegative-representation subclasses; this does not disprove factory existence or the CFTP results for valid ladders. For the scalar case, Corollary 3.11 bounds the source-defined p-input update count uniformly in p after degree elevation; Proposition 3.12 gives a separate parameter-dependent geometric tail for that same update count. The update also uses an independent uniform. Appendix A synthesizes fair bits by pairwise die comparisons; charging those extra tosses adds mean `1/[p(1−p)]` per fair bit for a binary p-coin, diverging at the endpoints. Thus the uniform CFTP-update bound alone is not a uniform total die-only cost. Theorem 3.9 gives eventual strict log-concavity but no effective sharp augmentation depth.

Other applications have their own output and cost variables. Vats et al. (X047) count portkey loops; for each fixed `β<1`, loop termination has probability at least `1−β`, so the loop and bounded coin-opportunity counts have all moments uniformly over local coin biases. This does not bound nested primitive costs for generating the local coins; `β→1` also removes the bound. Schmon et al. (X048) output a categorical index proportional to `c_i b_i`, with geometric trial mean `1/ρ_N`; their `O(N)` regime needs a nonvanishing success rate. Propositions 4–5's estimator `(N−1)/(Σ C_i−1)` requires `N≥2`; the `N=1` indicator estimator is separate derived evidence. Flajolet et al. (X049) define realizability by finite expected coin count and strong realizability by a pointwise exponential tail, and Theorem 1.1's finite-graph construction uses unbounded-precision arithmetic. Their Theorem 2.1 cost `C` excludes calls to the external `λ`-Bernoulli generator. None of these output-specific results supplies a general pointwise higher-moment iff.

Guan–Wang (X046) prove approximation estimates for smooth functions using positive **real** coefficients. These approximation polynomials are not the integer unnormalized Bernstein coefficients required by the finite-event criterion; no finite-depth factory follows without a separate exact conversion.


## More construction-specific cost models

Thomas–Blanchet (N001) implement scalar factories by nested Bernstein envelope/string-set cascades for stated linear, concave or convex targets. Their p.16 footnote gives exponential-tail envelopes only for small `p` and polynomial tails elsewhere; the fifth example checkpoint is `n₅=2^37`. Keep the practical construction, asymptotic existence argument, and example checkpoint separate.

Koskela et al. (N003) construct a bounded unbiased estimator from a smooth target’s compatible lower Bernstein coefficients using an independent power-law truncation `L`. Their Theorem 2 requires `ρ>3`, `1<λ<(ρ−1)/2`, and a sufficiently large start `k₀`; `ψ∈[0,1]` is part of the theorem under these assumptions. Since `P(L=n)∝n^(−λ)`, the construction has finite `r`th input-count moment when one can choose `r+1<λ<(ρ−1)/2`, i.e. `ρ>2r+3`. This is a derived sufficient condition for that construction, not an iff for arbitrary factories.

Koskela–Łatuszyński–Spanò (N002) use a polynomial-bounded factory in Wright–Fisher limits and Bernstein duality. On p.2, `[0,3/4]` bounds the unscaled residual before multiplication by `4/3`, so the next function lies in `[0,1]`; Algorithm 1 prints `BinCount/L` while Eq. (2)/prose use `BinCount/η(f,L)`. Keep both source discrepancies explicit and use the adjacent sample-mean construction. Their Theorem 4 statement points to a PDE with reaction `λf(u)`, while the branching proof derives `λ[f(q)−q]`; do not claim the proof establishes the printed equation. Their `η(f,L)` input count has no growth bound, so exactness/duality does not imply finite moments.

Stumpf-Fétizon–Gonçalves (N004) analyze recursive two-coin factories inside a factorized Barker-within-Gibbs algorithm. Their complexity results require the stated iid latent DGP, conditional independence, local smoothness/MGF, posterior concentration, proposal and cost assumptions. Theorem 1 gives stochastic boundedness of scaled merge overhead; the paper warns its expectation may still be infinite without stronger tails. Appendix C Proposition 7's Jensen lower bound is direct. Proposition 8's martingale tail conclusion (86)–(87) is not certified under its printed unconditional positive-mean condition: its martingale is centered by a random predictable compensator, with no stated control of that compensator around the unconditional mean. Do not use the `O(ρⁿ)` consequence without that missing interface. Huber (N005) proves a local-correctness FTPS criterion and applies it to one linear factory under a domain restriction; a.s. termination proves exactness but not finite expectation generally. Its Lemma 11 cost display is retained literally, but the p.16 ceiling-sum proof and closing constant note do not establish the displayed RHS as written; do not use that exact bound as proof-verified.

For other vector-valued factory examples, keep model, tail quantifiers and implementation separate. Niazadeh–Paes Leme–Schneider (X044) has pointwise geometric moments for its finite bounded-per-round race, compact-interior uniformity by a positive minimum, and a source-uniform strong property for generic sections; the non-generic construction is only pointwise a.s. Their Theorem E.1 excludes a single exponential rate uniform over all depths and inputs, not pointwise parameter-dependent exponential tails. For X045, do not equate the literal conditional-uniform-tree Algorithm 1 with the common-weight race justified by Theorem 3: the former adds an `f`-dependent tree-count denominator and R02's exact example has marginal `179/875` rather than `1/5`. This does not refute the polynomial identities themselves.

Dughmi et al. (X039) Theorem 3.5's basic exponential race has exact geometric input cost `λm/Σ_i exp(λ(v_i−1))`; the displayed `λm exp(λ(1−v_max))` follows as an upper bound from the largest summand. Preserve the source-stated bound but do not write it as an exact equality.
