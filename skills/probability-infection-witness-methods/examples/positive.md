# Positive examples: use a certificate in its exact model

## Fixed-host random-set zero forcing

On (P_3) with vertices (0-1-2), initial blue set ({0}) forces (1), then (2). The force (0\to1) has premises ({0}\cup(N(0)\setminus\{1\})={0}); the next force (1\to2) has premises ({1,0}). The two-level DAG proves activation by two rounds on this fixed host. Under the Bernoulli initial-set law, Curtis et al. Theorem 1.1 (PDF p. 2) gives a source-backed probability bound when the graph has minimum degree \(\delta\ge1\); do not replace that probabilistic theorem with the single (P_3) example.

## Empty-premise rules activate in round one

In edge-H bootstrap with `H=K2` on a fixed vertex set of size `n≥2`, every missing edge has the empty premise set `E(H−e)=∅`, so all such edges activate in round 1. In the Hamming rule with empty Young zero-set `Z=∅`, every site is excluded and the empty seed activates each site in round 1. In the shared DAG, these are rule-axiom leaves at depth 1; ordinary initial-seed leaves remain depth 0.

## Synchronous graph-H bootstrap

For K3 bootstrap on P4 with edges (01,12,23), first synchronous round adds (02,13); second adds (03). A complete legal saturating schedule adds (02,13,03), one at a time, and ends at the closed graph K4. It certifies the same closure by no more than three synchronous rounds, while the true synchronous time is two. The completeness condition is essential for an upper bound on total stabilization; a proper prefix only certifies the listed edge activations. For a lower bound on time, the Fabian et al. Theorem 4.2 proof (PDF pp. 17–21) supplies the stronger ingredient: a stable trigger gadget, a high-girth bipartite incidence structure, and an induction proving no extra (H-e) trigger before the designated last edge. Its conclusion assumes fixed ((2,1))-inseparable (H) and allows (C(H)n) vertices. Other exact target-class routes stay separate: BPR Theorem 1 gives M4(n)=n−3; Fabian–Morris–Szabó Theorem 1.2 gives a fixed-cycle formula for sufficiently large n; Fabian’s tree theorem is an upper bound for n≥2t; and Liu et al. give a Turán-density upper bound for fixed H. The K5 construction is a lower bound, while the 2012 p_c theorem is for random-host eventual closure. See the B03 page-use cards.

## Hamming-plane seed reduction

For a finite Young zero-set (Zsubseteq R_{a_0,b_0}), Gravner–Sivakoff–Slivken (2017), Theorem 1.2 (PDF p. 4), permits the minimum spanning-seed search to be restricted to (R_{a_0,b_0}). This positive transfer is for the full-row/full-column Hamming-plane rule, a finite zero-set, and a seed supported in the containing rectangle. Gravner–Paguyo–Slivken (2019), Theorem 1.1 (PDF pp. 4, 16–17), instead certifies a maximum time \(\mu(Z)\le2mn+5\) when (Zsubseteq R_{m,n}); it uses saturation and row/column crossing counts. Keep the two observables separate.


## Exact fixed-host success probability from a zero-forcing polynomial

For P3, the source's path formula gives Z(P3;x)=2x+3x²+x³: two singleton endpoints, all three 2-sets, and the full set are zero-forcing. If each vertex is independently blue with probability p, summing the probabilities of those disjoint initial sets gives the reader-derived identity Pr(Bp is zero-forcing)=2p(1−p)²+3p²(1−p)+p³=2p−p². This is an exact finite-host calculation, not a claim about host-edge monotonicity or an asymptotic threshold. The coefficient source is Boyer et al., Proposition 5 (PDF p. 5); the finite SymPy check for all labeled graphs through order 4 is recorded in the exact computation（本机附件：`evidence/project/expansions/20261115/readers/L15/computations/zero_forcing_polynomial_exact.out.json`）, with its general justification stated as a subset partition.

## Minimum-seed lower bound from linear algebra

In a finite hypergraph bootstrap instance, if vectors indexed by sites span W and every update hyperedge has a linear dependence with every coefficient nonzero, then a legal infection order shows each newly activated vector lies in the span of the earlier ones. Thus any percolating initial set has size at least dim(W). Balogh–Bollobás–Morris–Riordan prove this lemma and construct such vectors for their product-grid systems. Apply only after the target model's update hyperedges and dependencies have been verified; this method certifies seed cardinality, not synchronous running time.


## Finite Young-rule certificate and latency

For a fixed downward-closed zero-set Z on K_m □ K_n, the Gravner–Krnc–Milanič–Raymond rule adds a site synchronously when its horizontal and vertical occupied counts leave Z. At a proposed activation, choose a minimal excluded pair (a,b) beneath its count pair and list a distinct set of a occupied row sites and b occupied column sites, excluding the target. This is a finite witness for that activation. The paper’s γ_L theorem concerns filling the finite rectangle within the stated latency; it does not on its own transfer the result to the infinite Hamming plane.


## Coefficientwise comparison to a path and its fixed-host Bernoulli consequence

For a distance-hereditary `n`-vertex host, German’s Theorem 1 gives `z(G;k)≤z(P_n;k)` for every `k`. Menon–Singh prove the same comparison for every outerplanar or threshold host. Under iid Bernoulli-`p` initial blue vertices, partition the initial sets by size to get `P_G(ZFS)=Σ_k z(G;k)p^k(1−p)^{n−k}≤Σ_k z(P_n;k)p^k(1−p)^{n−k}`. The sum identity is a reader derivation; the cited papers prove coefficient inequalities in the named graph classes, not a threshold theorem. The exact finite check and `P_3` simplification are in the saved computation（本机附件：`evidence/project/expansions/20261115/readers/L15/computations/zero_forcing_bernoulli_weighting_exact.json`）.

## Synchronous clique-bootstrap maximum time

On the fixed synchronous edge-`K_r` rule, Matzke’s Theorem 1.1 gives `τ_max(n,K_3)=⌈log_2(n−1)⌉` for `n≥2` and `τ_max(n,K_4)=n−3` for `n≥4`; evaluate smaller orders directly (for K4 on fewer than four vertices, no update is possible and the time is 0). For fixed `r≥5` it gives an explicit construction implying only `τ_max(n,K_r)=Ω(n^{3/2})`. The `L_h` source/bridge recurrence is a causal-delay construction. The paper’s C3/C4-free reduced-source estimate controls only that construction framework; it is not a general upper bound on `τ_max`. See the B05/B06 source card for proof hypotheses and page anchors.


## Fixed-host fort obstruction and Bernoulli bounds

For a finite fixed host G, an initial set is zero-forcing exactly when it hits every fort (equivalently every inclusion-minimal fort). If M is the family of inclusion-minimal forts, then iid Bernoulli-p gives the reader-derived bound `P(failure) ≤ Σ_{F∈M}(1−p)^|F|`; it is a union bound, so overlapping forts are allowed but may make it loose. For any pairwise vertex-disjoint fort subfamily F₁,…,Fᵣ, success requires hitting every Fᵢ, hence `P(success) ≤ Πᵢ[1−(1−p)^|Fᵢ|]`. On P₃ the only minimal fort is the pair of endpoints, giving `P(success)=1−(1−p)²=2p−p²`. On K₃ the three two-vertex sets are minimal forts and the formula is `3p²−2p³`. The identities are derived from the fixed-host fort characterization; no host-edge monotonicity follows. Exact checks over all labeled simple graphs through order four are in the reproducible computation（本机附件：`evidence/project/expansions/20261115/readers/L15/computations/fort_obstruction_exact.py`） and its output（本机附件：`evidence/project/expansions/20261115/readers/L15/computations/fort_obstruction_exact.out.json`）; those checks validate finite instances only.


## Failed-set lower bound on the fixed host P3

Let `G=P3` with vertices `0-1-2`. The initial singleton `{1}` is failed, so `F(P3)=1`; the other two singleton endpoint seeds force the whole path. The exact polynomial counts are `[0,2,3,1]` by seed size. For iid `p=1/3`, exact enumeration gives `P(failure)=4/9`, matching the derived bound `(1-p)^(3−F)=4/9` and the Ufferman–Swanson universal exponent `floor(3/2)+1=2`; `P(success)=5/9`. The probability implication follows from fixed-host monotonicity of the closure, not from a source-stated Bernoulli theorem. The exact rational computation checks all 75 labeled graphs through order four and is saved in the L15 packet（本机附件：`evidence/project/expansions/20261115/readers/L15/reader_batches/assigned_fort_B12B13/computations/zero_forcing_probability_exact.out.json`）.

## Minimal-seed configurations give a success lower bound

On the same `P3`, the two minimal zero-forcing sets are the endpoint singletons. At `p=1/3`, the probability that the seed equals one of those minimal sets is `2·p·(1-p)^2=8/27`; this is a subset of the full success event, whose probability is `5/9`. Brimkov–Carlson's minimal-fort-cover characterization supplies the deterministic family, while the Bernoulli weighting is derived by summing disjoint exact configurations.


## Exact two-round standard forcing certificate

Let adjacent vertices u,v in a finite simple graph satisfy N[u] properly contained in N[v], and start with every vertex except u,v blue. Choose x in N[v]\N[u]. Then x is blue, adjacent to v, and not adjacent to u, so x forces v in the first synchronous round. At time 0 every blue neighbor w of u also lies in N[v], so it sees both u and v white and cannot force u; thus the process has not finished in one round. After v turns blue, v sees u as its only white neighbor and forces u in round 2. This is the exact Lemma 5.1 route of Ferrero et al. (PDF physical p. 13), under the standard unique-white-neighbor rule and that seed; it is not a PSD or graph-H clock.

## Minimal-seed size polynomial and a one-sided Bernoulli contribution

On P4, the inclusion-minimal zero-forcing sets are the two endpoint singletons and the middle pair, so the minimal-seed size polynomial is `2z+z^2`. At p=1/2, the probability that the initial set is exactly one of these minimal configurations is `3/16`; full success is `13/16` after including strict supersets. On the disjoint union P4∪P2, the componentwise minimal-seed polynomial is `(2z+z^2)(2z)=4z^2+2z^3`; the isolated-component convention would contribute its own factor z. This finite calculation is reader/reviewer-derived from Brimkov–Carlson Proposition 2.8 and Proposition 3.4, not a formula asserted by Corollary 3.5. The exact Python `Fraction` computation is saved here（本机附件：`evidence/project/expansions/20261115/readers/L15/reader_batches/Fort_BrimkovCarlson_delta_v1/computations/minimal_seed_probability_exact.out.json`）, with its script alongside it.
