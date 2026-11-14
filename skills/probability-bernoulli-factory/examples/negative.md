# Negative examples: claims to reject or narrow

- **“The HNP equivalence holds for every α>0.”** Theorem 8 is stated for noninteger α; the integer-order part gives a necessary Zygmund condition and leaves sufficiency conjectural.
- **“Pointwise `E_p[N^r]<∞` gives the Nacu–Peres smoothness conclusion.”** Their differentiability result uses uniform decay of moment tails on an open parameter set.
- **“An `O(n^{-α/2})` tail implies finite α-th moment.”** The standard tail-sum weights are of order `n^{r-1}` for the r-th moment. The HNP interior rate yields finite r-th moments for `r<α/2` under the stated uniform rate.
- **“The C204 printed sum `Σ n^α P(N>n)` equals `E[N^α]`.”** For deterministic `N=2` and `α=1`, the displayed sum is 1 while the expectation is 2. Use `Σ ((n+1)^r-n^r)P(N>n)` for integer-valued `N>=0`.
- **“Wästlund gives the sharp maximum coin-flipping degree.”** Theorem 4.6 proves finite maxima for fixed polynomial degree; the manuscript does not give a sharp general bound. Its `N(3)=46` is tentative, and the quartic example certifies only `N(4)>=735`.
- **“A finite event is the same as any a.s.-finite factory.”** A fixed finite depth is a strict subclass; do not move a theorem between these models without proof.
- **“Mendo's expected-cost lower bound covers all factories.”** It is stated for differentiable targets and fast factories with sequential-estimator regularity.

For extra open questions on the same author's page, verify the exact access model before routing: approximate degree-doubling questions and automata converses have different interfaces from A202/C204.

- **“Mendo Theorem 4 requires `f(p)/p→∞`.”** The theorem explicitly does not require condition (11); it assumes condition (12). The asymptotic-optimality corollary for Algorithm 1 uses both (11) and (12).
- **“An entropy-rate extraction theorem gives a factory stopping-time moment.”** Peres's iterated von Neumann rate is an almost-sure output-bits/input-bits limit, while Stout–Warren analyze expected costs of specified extraction trees. Neither supplies an arbitrary factory's per-output `r`-moment.
- **“A nonnegative `f`-factory is a Bernoulli factory.”** Jacob–Thiery's bounded-support theorem takes arbitrary iid input laws and returns a nonnegative real unbiased estimator; it does not characterize Bernoulli-valued output or p-coin toss moments.
- **“Exact diffusion point counts are p-coin toss counts.”** Beskos–Roberts (2005) decide alternating Taylor/factorial events by revealing iid uniform points from an area-one rectangle; Beskos–Papaspiliopoulos–Roberts (2006) use Poisson processes. Both use Brownian bridges and drift conditions, and both require a primitive-input cost reduction before applying them to C204.
- **“Peres recursively feeds the von Neumann output bits back into the procedure.”** The recursion in Peres (1992) feeds the pairwise XOR/equality-indicator stream and the retained bits from equal pairs into the two recursive calls; `Ψ₁` is a separate concatenated output block.
- **“Stout–Warren Theorem 1 is the no-E-optimality theorem.”** Theorem 1 improves `Q₃` uniformly with equality only at `p=1/2`; the no-E-optimality conclusion is Theorem 3. Theorem 2 is a separate restriction on continuation sequences.
- **“Jacob–Thiery's impossibility proof matches the input means.”** The proof uses distinct fixed means with different `f` values and rare contamination of one law to make finite prefixes close while retaining its distinct mean.
