# Counting and sampling method

## 1. Fix the model before counting

For a finite simple graph `G=(V,E)`, a labeling is a bijection `L:V→{1,…,N}`. A graph peak is a vertex `v` with `L(v)>L(u)` for every neighbor `u~v`. The peak set and number depend on the graph adjacency, including its boundary convention. In a free `n×n` square, use only in-square nearest-neighbor edges; do not add wraparound edges.

For a permutation written as a sequence, an index peak instead compares adjacent sequence positions. Do not use one-dimensional peak formulas for a graph unless its graph is exactly the path graph under the same endpoint convention.

## 2. Exact descending-order recurrence for graph peaks

Represent a labeling by its vertex order from largest label to smallest. Let `R⊆V` be the vertices not yet selected, and let `k` be the number of peaks still required. For `v∈R`, define

$$
\delta(v,R)=\mathbf 1\{N(v)\subseteq R\}.
$$

At the moment `v` is selected, every vertex in `R` will receive a smaller label; a neighbor selected earlier has a larger label. Thus `v` is a peak exactly when all its neighbors remain in `R`.

Define `D(R,k)` as the number of descending orders of `R` that create exactly `k` further peaks. Then

$$
D(\varnothing,k)=\mathbf 1\{k=0\},\qquad
D(R,k)=\sum_{v\in R}D\bigl(R\setminus\{v\},\,k-\delta(v,R)\bigr).
$$

Use `D(R,k)=0` for `k<0`. Every order has one unique first vertex, so the recurrence partitions the orders without overcounting. The desired count is `D(V,m)`.

A direct memoized implementation has at most `(m+1)2^N` states and `O(N)` transitions per state. This is an exact finite algorithm, not a polynomial-time guarantee. Exploit graph symmetry or separators only after proving that the quotient/transfer recurrence retains orbit weights and all dependencies.

### Exact uniform branch sampler

At state `(R,k)`, choose `v` with probability

$$
\frac{D\bigl(R\setminus\{v\},\,k-\delta(v,R)\bigr)}{D(R,k)},
$$

then recurse. If the integer draw is uniform, each complete target order has probability `1/D(V,m)`, by telescoping completion-count ratios. Do not choose uniformly among currently available vertices unless all branches have equal completion counts.

To sample a statistic such as the distance between the two peaks, augment the state with enough information to identify the first and second selected peak vertices, or compute a separate exact count indexed by that statistic. Verify that the augmentation does not merge states with different future completion counts.

### Separate source-based recursion for a prescribed peak set

The subset dynamic program `D(R,k)` above is the skill's direct finite recurrence. It is distinct from the M0002 `GraphPeakSetAlgorithm`. **The peak predicates differ:** the direct recurrence calls `v` a peak whenever every neighbor is lower, so it includes leaves and isolated vertices; M0002's physical-p.2 source definition excludes vertices of degree 0 or 1 from being peaks. Do not use that source algorithm to count the direct recurrence's target without reconciling the difference. R05 accepted the latter only for a finite simple graph with a **known `G`-admissible** required peak set `S`, with `V_{<2}(G)⊆L⊆V`. For an exact-set call initialize `L=V_{<2}(G)` and use the source's update `L←(L∪N(v))∩(V\{v})`. Keep separate branch-local copies of `S`, `L`, and the labeling state, and collect every recursion leaf.

Required vertices having degree at least two and `S` being independent are necessary checks, not a complete test of `G`-admissibility. Do not pass an arbitrary set through the source recursion on the strength of these two checks alone. This scoped use provides no polynomial-time guarantee or sampler. Exact accepted conditions and locators are in the M0002 scope row（本机附件：`references/accepted_scope_register.md`）.

## 3. Linear extensions of a fixed poset

For a finite poset `P`, every linear extension ends in a maximal element. Hence

$$
e(\varnothing)=1,\qquad e(P)=\sum_{x\in\max(P)}e(P\setminus\{x\}).
$$

Equivalently, dynamic-program over order ideals, adding one currently available minimal element. For exact uniform sampling, choose the last maximal element `x` with probability `e(P\{x\})/e(P)`, then recurse. This is exact when the counts are exact.

A fixed conjunction of comparisons is a poset event and can be counted as a linear-extension problem. Exact graph-peak constraints generally are not: every nonpeak must have at least one larger neighbor, a disjunction over neighbors. Any reduction to a union of posets must prove disjointness or correct overlap weights.

## 4. Entropy and concentration

For a uniform finite target set `Ω`, `H=log|Ω|`. Shearer-type inequalities and graph entropy can upper-bound `H` or a restricted count. To prove a normalized peak distance tends to zero, one still needs:

1. a lower bound for the total number of labelings in `Ω`;
2. an upper bound for labelings whose peaks are separated by at least `εn`;
3. a strict exponent gap, uniform over possible locations and boundary strata;
4. control of the number of location/shape classes so the union bound does not erase the gap.

An upper entropy bound alone, or a most-likely configuration alone, does not imply concentration.

## 5. Exact, approximate, and perfect sampling checks

Before claiming a sampler is exact, identify its target set and prove its stationary law or recursive branch weights. Before claiming CFTP works, use the same random map for every start state at each past time and every enlarged horizon; verify that certified coalescence occurs almost surely. A monotone bounding pair is valid only if the update coupling preserves the required order.

A rapidly mixing chain yields an approximate sample after a proven mixing bound. A perfect sampler gives an exact stationary sample but may have large or unbounded practical runtime unless its expected runtime is analyzed. An approximate count, exact sampler, and approximate sampler are different deliverables.

## 6. Verification protocol for finite cases

For each small graph:
- independently construct its adjacency;
- compare the DP with full permutation enumeration where feasible;
- verify each returned order has the stated number of peaks;
- check exact distance counts sum to the exact conditional count;
- use an unbiased integer draw for branch weights;
- save code, run output, parameters, and hashes.

Finite checks can detect errors in recurrences and boundary handling. They cannot establish an asymptotic limit.
