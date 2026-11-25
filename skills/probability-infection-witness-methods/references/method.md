# Method routing and certificate checks

## Intake record

Before using an infection theorem, write down:

1. Host/domain and active object: vertices, edges, or sites.
2. Initial configuration and randomness: fixed set, iid seed law, random host, or random updates.
3. Exact update family, whether the target must already be inactive, and whether the process is sequential or synchronous.
4. Observable: closure event, success probability, threshold, minimum seed, first activation time, stabilization time, or finite optimization value.
5. Scale and quantifiers: fixed (n), sufficiently large (n), (n) versus (C n), finite box versus infinite plane.
6. Required proof: probabilistic bound, deterministic closure, extremal construction, exact arithmetic, or certified interval.

## Building and checking a witness DAG

For a fixed finite-premise rule system, give initial active items depth 0. A node labelled by a zero-premise rule is an axiom leaf at depth 1. For a rule node with nonempty premise set, assign depth 1 plus the maximum depth of its premise nodes; every premise must occur at smaller depth. Empty premises are vacuously satisfied at time 0 and their heads activate in round 1. Induction on depth proves activation by that depth. If simultaneous rule firing is the process clock, depth is a valid upper bound. A legal sequential schedule bounds whole synchronous closure only when it is complete and saturating: it lists every closure addition and ends at a closed state. Its length m then gives closure within at most m rounds because each scheduled rule is eligible once earlier premises have appeared. A proper prefix bounds only the listed targets. Neither certificate gives a lower bound on the process time.

When testing a proposed exact (t)-round or slow process, inspect every absent target at every round and show that every rule has at least one missing premise. A listed chain is insufficient: other rules may fire in parallel. A “no shortcut” invariant must account for every embedding of (H-e), not only the intended chain copies.

## Model adapters

### G28: fixed-host zero forcing

For each proposed force (u\to v), verify (uv\in E(G)), (u) is blue, and every vertex of (N_G(u)\setminus\{v\}) is blue at the start of the force. In the positive-Horn encoding, make these the premises of the head (v). This encoding preserves monotonicity in the initial blue set for fixed (G). Recompute the rule set if (G) changes; the edge-addition P3-to-K3 example shows host monotonicity fails.

The least fixed point of these positive rules has the same all-vertices closure event as existence of a legal standard forcing order on the finite graph; standard zero-forcing-set papers count that closure event, not synchronous round time. If synchronous rounds are introduced as a derived clock, label them separately.

For a fixed finite host, a **fort** is a nonempty set F such that every vertex outside F has either 0 or at least 2 neighbors in F. The source-backed characterization is: S is zero-forcing iff S intersects every fort, equivalently every inclusion-minimal fort. If the host is fixed and S is iid Bernoulli(p), one specified fort is missed with probability (1-p)^|F|. Thus, when M is the complete family of all inclusion-minimal forts (or another proved complete obstruction family such that every failed seed misses some F in M),

\[
\Pr(S\text{ is not ZFS})\le\sum_{F\in M}(1-p)^{|F|},
\]

by a union bound. For an arbitrary partial fort family M, write U_M=\bigcup_{F\in M}\{S:S\cap F=\varnothing\}. Then U_M is a subset of failure, so P(U_M)\le P(failure). The raw sum \sum_{F\in M}(1-p)^{|F|} only upper-bounds P(U_M); overlap means it has no general lower-bound relation to P(failure) and can exceed the whole failure probability. A valid failure lower bound can instead use one missed-fort event, the exact union probability, a justified Bonferroni lower bound for that union, or a sum of miss probabilities after disjointness of those events is proved. For any pairwise vertex-disjoint fort subfamily F₁,…,Fᵣ, success requires hitting each, so

\[
\Pr(S\text{ is ZFS})\le\prod_{i=1}^r[1-(1-p)^{|F_i|}].
\]

These are derived probability bounds, not threshold results from the fort-count papers. For the failure upper bound, both completeness of the obstruction family and its size distribution are required; a total count without size information or a partial size-resolved family does not supply it. The disjoint-fort success upper bound needs only the stated disjoint subfamily. For a random initial-set statement, identify the first successful force if that is the source proof. The event then forces a particular local pattern in the initial iid set. Count candidate vertices/neighborhoods, retain minimum-degree and small-(p) assumptions, and state whether the conclusion bounds \(\Pr(B_p(G)\text{ is ZFS})\) or a threshold (p(G)).

For fort checks, the Cameron et al. fort-hitting theorem is for a fixed finite host; Cameron–Li local characterizations are tree-only, while cited exact-count results retain their graph-class hypotheses. Abiad et al.'s dynamic program returns total minimal-fort count, not a size distribution, and its exponential arbitrary-fort results must not be relabeled as minimal-fort counts. The accepted Dat–Kenter all-n tree/forest count route is attributed to the separate R15 integer-majorant proof independently checked by R06; the source's original reported finite computational base through n=19 is not the proof used. Cameron–Pulaj supplies finite exact encodings, not a Bernoulli law or submodularity theorem.

For coefficient methods, keep the fixed-host condition explicit. German’s Theorem 1 applies to distance-hereditary graphs; its Theorem 2 requires one prime bag with every induced subgraph of its label path-extremal; Theorem 3 has prime-order-at-most-six hypotheses and its stated exceptional label. Menon–Singh prove coefficientwise comparison for outerplanar and threshold graphs through leaf/hanging-cycle/cone/hanging-path operations. For each eligible graph, the iid Bernoulli success probability is the weighted polynomial `Σ_k z(G;k)p^k(1−p)^(n−k)`; this is a reader derivation from the subset partition. Newton–Brimkov’s `G_t` has a nonunimodal polynomial for `t≥24`; do not assume coefficient unimodality for arbitrary fixed hosts. These are coefficient comparisons/boundaries, not asymptotic threshold laws.

### G29: edge-\(H\) bootstrap

For each candidate new edge (e), record the injective (H)-copy in which (e) is the missing edge and list all other edges as premises. Use old-round states for a synchronous proof. Label each transition as “percolates,” “stabilizes,” or “adds a designated edge”; these are not equivalent.

For a lower bound on \(\tau_H(G)\), give a round-by-round invariant and exclude all non-designated (H-e) copies. If a theorem constructs a graph on at most (C(H)n) vertices, retain this size in the result; derive a same-(n) statement only after proving a scaling/embedding lemma. Record weak saturation, random-host threshold, and maximum running time in separate fields.

For synchronous running time, route to the exact target class. Matzke Theorem 1.1 gives exact K3 and K4 maximum times and only a fixed-`r≥5` lower construction. Its K4 proof invokes Lemma 2.6's no-inactive-time condition; it does not establish Lemma 2.7's additional binary-merger restriction. Exclude the false printed `e≥2τ+6` inequality in Theorem 2.9; the G29.02/G29.05 uses do not need it. Matzke's source-intersection graph/Turán estimate constrains the `L_h` construction framework. BPR Theorem 1 gives the exact K4 maximum; Fabian–Morris–Szabó give fixed-cycle time formulae and a tree upper bound; BKP provide a K5 slow-time lower construction; Liu et al. bound general fixed-rule time through Turán density. The 2012 BBM theorem concerns the random-host threshold for eventual closure, not maximum time. The corrected method-ID overlay and six page-use cards are at `readers/L15/reader_batches/G29_graph_bootstrap_reuse_B03_revision2/`; the earlier mapping is retained as a historical frozen snapshot. G29.04 is specifically tree peeling/decomposition/embedding and is assigned only to the Fabian tree upper-bound source. BPR/K5/cycle/Liu results route by their actual causal-chain, sparse-structure, gadget, Turán-density, or scale-check methods. Slow Graph Bootstrap III routes only to G29.02/.05/.06 under its proper-chain, no-shortcut, fixed-H and explicit vertex-budget hypotheses; it is not used for generic G29.07 growth scaling.

G29.07 has one narrow scale-check route: the accepted fixed-cycle exact-time formula for its stated parity and sufficiently-large-n range. It is not a regular-growth test for arbitrary fixed H and does not supply an n-to-Cn transfer.

### G30: Young/Hamming growth

For a finite Hamming rectangle with fixed finite Young zero-set Z, record the full horizontal and vertical counts at the start of each synchronous round. Choose a minimal excluded pair (a,b) below the actual pair; list a occupied sites in the target row and b in the target column, checking distinctness and excluding the target. The 2025 Gravner–Krnc–Milanič–Raymond paper has separate interfaces: Definition 2.1/Lemma 2.2 (physical pp. 7–8) establish the fixed-rectangle Young boundary/concave-corner dual; Theorem 3.1 (pp. 10–11) is only the stated latency-one result; Lemma 8.1 (p. 30) counts resources using the actual longest row and column lengths a,b; and Theorem 1.6 with Lemma 8.2 (p. 31) gives dimension stabilization under its finite-box and latency hypotheses. In the latter, Z⊆R_{a,b}, 2≤L≤∞, and m,n>ab give γ_L(Z,m,n)=γ_L(Z,∞,∞); only with L≥2ab+5 does the eventual equality to γ_∞ and [|Z|/4,|Z|] bound follow, importing GPS2019/GSS2017 inputs. Do not turn these into generic compression, half-area, LP, or infinite-plane theorems.

Use `EXSRC-b645ea67b83aef1a` only at the four anchors and hypotheses above; use `PR-310f31dd14f1` only for its exact Hamming-plane seed rectangle reduction and finite-time statement. Use `PR-2ff6120c6cde` only for the 2019 maximal-time theorem and its enhanced/thin comparison. The two sources' Theorem 1.2 statements differ.

## Open method interfaces

The current L15 infection cohort leaves G28.03-.06, G29.03, G30.03 and G30.05 without accepted method-specific source routes: Russo–Margulis derivatives; clique first-entry; frontier automata; second-moment/Janson; potentials/amortized analysis; linear-algebra weak saturation; and coverage LP/fractional duality. G29.07 has only the named fixed-cycle scale check, not a general fixed-H method. G32 finite verification is routed to the separate W19 skill and does not count toward infection coverage.

## Scope checklist

- A DAG certifies an upper bound on activation time, not an exact time or slow-time lower bound.
- Host-edge changes can destroy a zero-forcing move.
- A complete saturating sequential (m)-step schedule implies synchronous closure by at most (m) rounds; an arbitrary prefix bounds only listed targets, and even the complete schedule does not imply exactly (m) rounds.
- A (C(H)n) construction is not a same-(n) theorem.
- A finite-box-to-plane implication requires the precise source theorem and seed support.
- Maximum spanning time does not imply minimum seed cardinality.
- A coverage LP needs a correct encoding and a proved relaxation. A greedy approximation further needs the claimed submodularity/diminishing-returns hypotheses.
- Finite exact computation verifies only enumerated instances.


## Failed-set and minimal-seed probability adapters

For a fixed finite graph `G`, a failed set `S` has `cl(S) ≠ V(G)`. The closure under the unique-white-neighbor rule is monotone in the initial blue set while the host stays fixed. Therefore every subset `B ⊆ S` is also failed, and iid Bernoulli-`p` initial coloring gives the event inclusion

`{B_p ⊆ S} ⊆ {B_p is not zero-forcing}`,

so `P(failure) ≥ (1-p)^(n−|S|)`. For a nonempty host (`n≥1`), maximizing over failed sets yields `(1-p)^(n−F(G))`; Ufferman–Swanson Theorem 2 supplies `F(G) ≥ floor((n−1)/2)`, hence the reader-derived universal bound `P(failure) ≥ (1-p)^(floor(n/2)+1)`. The empty host is already completely colored and has failure probability 0, so handle it separately. The source proves the graph inequality, while the probability step is an elementary fixed-host event inclusion.

If `M_k(G)` counts inclusion-minimal zero-forcing sets of size `k`, then `Σ_k M_k(G)p^k(1-p)^(n−k)` is exactly the probability that the initial configuration itself equals a minimal zero-forcing set. It is a lower bound on success, not the full probability: every strict superset succeeds too, and the upward events `{F ⊆ B_p}` overlap. Use a zero-forcing polynomial or a separate union calculation for the full event. Preserve “minimal” (inclusion-wise) versus “minimum” (cardinality-wise).

For finite deterministic certification, the Brimkov–Fast–Hicks time-indexed IP uses vertex sources, integer force times `x_v∈{0,…,T}`, and selected arcs `u→v`; a selected arc requires `u` and every `w∈N(u)\{v}` to have smaller time than `v`. Their fort-cover IP minimizes a binary hitting set over every fort; its optimum is the zero-forcing number. Any implementation must verify a complete fort list or a valid violated-fort separation oracle. The formulation does not assume submodularity, and it does not specify an iid seed law or encode G29's H-edge update rule.
