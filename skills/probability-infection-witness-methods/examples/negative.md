# Negative examples: reject invalid transfers

## Formula domains are part of the theorem

For the empty graph, the initial coloring is already complete, so `P(failure)=0`; the unqualified Ufferman adapter at `n=0` would incorrectly give `(1-p)^1`. Its stated use is for `n≥1`, with the empty host handled directly. On a two-vertex host under K4 bootstrap, no K4 copy exists and stabilization time is 0, while the unqualified expression `n−3` gives `−1`. The displayed K3 and K4 maximum-time formulas therefore retain their ranges `n≥2` and `n≥4`.

## Host-edge addition breaks zero forcing

On (P_3), one blue endpoint forces through the middle and colors all vertices. Add the edge joining the two endpoints to get (K_3); the same singleton now has two white neighbors and cannot force. Initial-set monotonicity holds only for the fixed host. This finite counterexample is also in exact computation output（本机附件：`evidence/project/expansions/20261115/readers/L15/computations/exact_scope_checks.out.json`）.

## A DAG cannot certify slow time

A valid chronological chain proves that its last item activates by the chain depth. It does not show that no other rule fires earlier. For synchronous slow time, prove at every round that each unintended target still has at least one missing premise. In graph-\(H\) bootstrap, rule out every unintended (H-e) copy.

## Sequential edge count is not synchronous time

The K3-bootstrap P4 example has a legal three-edge sequential schedule but only two synchronous rounds. Only a complete saturating sequential (m)-step schedule—listing all closure additions and ending closed—bounds the full synchronous stabilization time by m. An arbitrary legal prefix does not. For K3-bootstrap on P4, the single addition 02 is a legal prefix of length 1, but the complete synchronous process takes 2 rounds; this is an exact counterexample to applying the full-closure bound to a prefix.

## A (C n) construction is not same-(n) equality

Fabian et al. Theorem 4.2 constructs a percolating host with at most (C(H)n) vertices whose time is at least (M_H(n)), for fixed ((2,1))-inseparable (H). It does not imply a same-(n) \(\Theta\) result without a separate size-transfer theorem.

## Finite closure does not imply infinite filling

On an infinite domain with rule (k\to k+1) and seed ({0}), every individual site eventually activates, yet no finite time fills (mathbb N). For the Hamming plane, finite-box-to-plane transfer is valid only under the exact hypotheses of Gravner–Sivakoff–Slivken (2017); do not infer it for another update rule.

## Time bounds do not become seed bounds

The 2019 Hamming-plane maximal-time theorem is about \(\mu(Z)\), not the minimum seed size \(\gamma(Z)\). It does not prove \(\gamma(Z)\ge |Z|/2\). The cited 2017 seed theorem gives \(|Z|/4\le\gamma(Z)\le|Z|\) and states the stronger lower-bound question remains open.


## Weak saturation is not a round count

Terekhov–Zhukovskii define weak F-saturation through a sequential ordering of missing edges, each completing a fresh F-copy. The full weak-saturation order is a complete saturating schedule for its specified K_n closure and so gives an upper bound by its length for that same fixed rule/host. A prefix alone bounds only listed edge activations. It does not imply the synchronous process takes that many rounds, and it cannot prove a slow-time lower bound; earlier parallel triggers must be excluded round by round. Their subadditive lower bound controls edge counts in the stated weak-saturation model only.

## Linear-algebra seed theorem does not automatically match graph-H hosts

Balogh–Bollobás–Morris–Riordan's exact formula is for the specified induced product-grid hypergraphs K(n,d,t,r) and P(n,d,t,r). A graph-H edge process can be encoded as a hypergraph on edges, but that encoding alone does not make its update hyperedges one of those product-grid families or produce the required full-support dependencies. Do not import their exact formula to an arbitrary graph-H model.


## Zero-forcing coefficients need not be unimodal

Newton–Brimkov’s fixed-rule construction has `Z(G_t;x)=x^n +(10+3t)x^{n−1} +(37+30t+3t²)x^{n−2} +(60+99t)x^{n−3} +(36+108t)x^{n−4}`. For `t≥24`, the coefficient pattern has a dip and subsequent rise: `z(G_t;n−4)>z(G_t;n−3)<z(G_t;n−2)`. This blocks an unsupported global-unimodality assumption when studying the exact zero-forcing polynomial. It says nothing about a random-host threshold or typical graphs. See the complete proof and exact `t=24` arithmetic in the source card（本机附件：`evidence/project/expansions/20261115/readers/L15/reader_batches/assigned_primary_B05B06/cards/EXSRC-28ab851ff26380df.md`）.


## Fort counts need sizes and the right inequality direction

A theorem giving many minimal forts does not by itself upper-bound Bernoulli failure: the event of missing their union depends on fort sizes and overlap. To upper-bound failure by a union bound, the fort family must be complete: include every inclusion-minimal fort, or prove every failing seed misses at least one listed fort, and provide the sizes. For a partial family M, its missed-fort union U_M=\bigcup_{F\in M}\{S:S\cap F=\varnothing\} is a subevent of failure, hence P(U_M)\le P(failure). The raw sum of miss probabilities only upper-bounds P(U_M), and it need not lower-bound either the union or total failure. An exact C5 enumeration at p=1/2 gives a proper four-of-five minimal-fort family with miss-probability sum 1/2, union probability 5/16, and whole failure probability 11/32; see the exact counterexample record（本机附件：`evidence/project/expansions/20261115/reviews/R15/revision9_integration/partial_sum_counterexample.json`）. A disjoint fort subfamily independently gives a success upper bound after vertex-disjointness is proved. Do not treat a DP that returns only the total number of minimal forts as a size distribution, and do not substitute exponential counts of arbitrary forts for minimal-fort counts.


## Do not replace random seeds by random hosts

Kalinowski–Kamčev–Sudakov study deterministic zero-forcing numbers of graph hosts and random-host laws such as `G(n,p)`. That samples the graph itself. G28 instead fixes `G` and samples blue vertices independently. A random-host theorem cannot be quoted as a fixed-host Bernoulli-seed threshold without an additional conditional argument that matches the desired observable.

## Minimal generators do not form a disjoint upward-event sum

For `P3`, the two inclusion-minimal zero-forcing sets are endpoint singletons. At `p=1/2`, the probability that the initial set equals one of these two minimal sets is `1/4`, while the full success probability is `3/4`; the strict supersets also succeed. Conversely, summing the two upward events “contains endpoint 0” and “contains endpoint 2” gives `1`, overcounting their overlap. Thus the exact-minimal-seed mass is a valid lower bound only. Use the zero-forcing polynomial or account for overlaps to compute full success.

## Fixed-host finite IP does not transfer to a different rule

The Brimkov–Fast–Hicks time and fort-cover IPs encode the standard graph unique-white-neighbor rule on a finite fixed graph. Replacing vertices by edges does not make the resulting constraints a synchronous graph-H bootstrap model. State the graph, force rule, integer time domain, and complete fort/separation condition before treating an IP optimum as an exact certificate.


## Minimal seeds are not an additive success-probability formula

On P4, the inclusion-minimal zero-forcing seeds are `{0}`, `{3}`, and `{1,2}`. At p=1/2 their upward-event probabilities sum to `1/2+1/2+1/4=5/4`, although the true full success probability is `13/16`. The exact-minimal-configuration mass is `3/16`, a lower bound on success, not the whole probability; overlaps among upward events prevent direct addition. Brimkov–Carlson Corollary 3.5 supplies only an Ω(2^k) lower count in its parameter, not an exact count or size distribution.
