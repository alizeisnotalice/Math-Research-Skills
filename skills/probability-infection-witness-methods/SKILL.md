---
name: probability-infection-witness-methods
description: Build and audit finite causal witnesses for deterministic monotone infection closures, with separate model routes for random-set zero forcing, synchronous graph-H bootstrap, and Hamming-plane Young growth.
---

# Infection witnesses and closure certificates

Use this skill when a proof needs to show how a specified vertex, edge, or site becomes active under a fixed deterministic infection rule. Start by fixing the host/domain, state object, initial set or law, update rule, clock, target observable, and finite/infinite setting. Route probability thresholds, minimum seed size, maximal synchronous time, and exact finite certificates as separate questions. Choose the model by its state object and rule, not by the word “percolation.”

| Input model | Route | First boundary to check |
|---|---|---|
| A fixed finite graph with iid initially blue vertices and deterministic unique-white-neighbor forcing | G28 | Randomness is in the initial set; probabilistic forcing and random-host laws are different models. |
| A fixed vertex set with synchronous edge-H bootstrap | G29 | Each round adds all currently eligible missing edges; weak saturation is a sequential edge count, and random-host threshold is another observable. |
| Hamming-plane row/column growth from a finite Young zero-set | G30 | Preserve the exact row/column count rule; finite-rectangle theorems need not imply infinite-plane spanning. |
| A finite LP, interval, SOS, SAT/SMT, or exhaustive proof object | Use the separate W19 optimization-certificate skill | A verifier can certify its exact finite encoding, but does not select or prove an infection model. |
| Ordinary Bernoulli site/bond percolation, or a specifically named W05 update model that does not match G28/G29/G30 | Use the separate W05 percolation skill only after checking its exact rule | Match state and update rule first; a critical-probability or lattice keyword never reroutes a G28, G29, or G30 threshold question. |


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Shared finite certificate interface

For a fixed host (U) and a fixed family of finite-premise rules (P\to h), define

\[
B_{t+1}=B_t\cup\{h:\text{some rule }(P\to h)\text{ has }P\subseteq B_t\}.
\]

An activation certificate is a finite acyclic directed graph with two leaf types: initial facts in (B_0) at depth 0, and rule-labelled zero-premise applications at depth 1. A node for a rule with nonempty premise set has depth one plus the maximum premise depth. Check every premise against the exact host and rule. Its depth proves the target activates **by at most that many synchronous rounds**. Empty premises are vacuously satisfied at time 0 and trigger in round 1. It proves no slow-time lower bound and does not establish that the target activates for every initial set.

On a fixed host, the rule closure is monotone in the initial set: if (B_0\subseteq C_0), induction gives (B_t\subseteq C_t) at each time. This does not imply monotonicity under changing the host, because an added edge can change the rule premises.

## Model routes

### Random-set zero forcing (G28)

The host is a deterministic finite graph (G); each vertex is initially blue independently with probability (p); a blue (u) forces (v) only when (v) is its unique white neighbor. Encode a potential force (u\to v) by premises

\[
\{u\}\cup(N_G(u)\setminus\{v\}).
\]

The host and its neighborhoods must remain fixed. The least fixed point of these positive rules has the same all-vertices closure event as existence of a legal standard forcing order on the finite graph; standard zero-forcing-set papers count that closure event, not synchronous round time. If synchronous rounds are introduced as a derived clock, label them separately. A forcing chain or chronological list is valid only when every step is legal in the coloring at that step. For probability bounds, state whether the source bounds a first successful force, counts forcing sets, or proves a whole-graph threshold; these are different claims. On a fixed host, a fort is a nonempty vertex set F such that every outside vertex has 0 or at least 2 neighbors in F. An initial set is zero-forcing iff it hits every minimal fort. Under iid Bernoulli-p, a specified fort is missed with probability (1−p)^|F|; a size-resolved union bound over missed forts is a reader-derived probability estimate, not a threshold theorem. Fort-count lower bounds alone do not give a failure upper bound, and finite fort-cover LP/IP models do not imply submodularity. Boyer et al. define the zero-forcing polynomial Z(G;x)=Σ_i z(G;i)x^i, where z counts size-i zero-forcing sets. For a fixed n-vertex host and iid Bernoulli(p) initial blue set, derive the exact success probability Σ_i z(G;i)p^i(1−p)^(n−i) by grouping initial sets by size; this weighting identity is a reader derivation, not a threshold theorem stated in that paper. Do not substitute probabilistic zero forcing, which randomizes the forcing events from a fixed initial set. German proves coefficientwise path extremality for distance-hereditary graphs and the exact prime-bag classes in its theorems; Menon–Singh prove it for outerplanar and threshold graphs by explicit graph-operation injections. These class hypotheses transfer to the fixed-host Bernoulli success probability through the nonnegative coefficient weights. Newton–Brimkov give a graph family whose zero-forcing polynomial is nonunimodal for every integer t≥24, so do not assume global coefficient unimodality.

### Synchronous graph-\(H\) bootstrap (G29)

The state is an edge subset on a fixed vertex set. For an embedded copy of (H) and one missing edge (e), the premises are all the other edges of that copy, (E(H-e)). A round uses only the graph at the start of that round and adds every currently eligible edge simultaneously.

A **complete saturating** legal (m)-step sequential edge-addition schedule—listing every edge in closure minus the initial edge set and ending at a closed state—certifies that the synchronous process reaches the same closure in at most (m) rounds. A legal prefix only bounds activation of its listed targets; it cannot bound total stabilization. Neither conclusion gives equal round counts or a slow-time lower bound. For a slow-time construction, give a separate invariant that rules out every unintended (H-e) completion in each earlier round. Weak saturation \(ws\mathrm{at}(n,H)\), random-host threshold (p_c(n,H)), and maximum stabilization time (M_H(n)) are separate observables. A result on at most (C(H)n) vertices needs a separate size-transfer argument before it supports a same-(n) asymptotic. Matzke (2015), `EXSRC-bb3b9d67c2219625`, proves the exact maximum K3 and K4 times and an explicit Ω(n^{3/2}) lower construction for fixed Kr, r≥5. Its C3/C4-free reduced-source argument bounds only that construction framework, not all Kr processes. For minimum-seed lower bounds, Balogh–Bollobás–Morris–Riordan give a linear-algebra method for specified hypergraph bootstrap systems: a vector assignment with a full-support dependence on every update hyperedge yields m(H)≥dim(W), and their exact theorem is for the stated product-grid hypergraphs. Terekhov–Zhukovskii instead study weak F-saturation, with each missing edge added sequentially; their subadditive lower bound applies to weak-saturation counts under its stated graph hypotheses and gives no synchronous slow-time lower bound.

G29.07 has one narrow scale-check route: the accepted fixed-cycle exact-time formula for its stated parity and sufficiently-large-n range. It is not a regular-growth test for arbitrary fixed H and does not supply an n-to-Cn transfer.

### Hamming-plane Young growth (G30)

The host is \(\mathbb Z_+^2\), and the fixed finite Young-diagram zero-set (Z) determines the full-row/full-column count rule. If a site's count pair is outside (Z), use a minimal excluded pair and select finitely many occupied sites on its row and column as premises. Check that the selected row and column sites are distinct and that the target itself is excluded from the premise set.

The 2025 Gravner–Krnc–Milanič–Raymond source `EXSRC-b645ea67b83aef1a` has separate finite-rectangle routes: Definition 2.1/Lemma 2.2 (PDF pp. 7–8) for fixed-rectangle Young corners/duality; Theorem 3.1 (pp. 10–11) only for latency one; Lemma 8.1 (p. 30) for resource counts using the actual longest row and column lengths; and Theorem 1.6/Lemma 8.2 (p. 31) under the stated dimension/latency gates. These do not establish arbitrary infinite-plane spanning or generic compression/LP/half-area bounds. The seed-size and finite-box route is specific to each rule. Gravner–Sivakoff–Slivken (2017), source `PR-310f31dd14f1`, Theorem 1.2 (PDF p. 4), reduces the minimum seed to a rectangle containing (Z); its statement concerns seeds initially supported in that rectangle. The introduction gives the internal-span iff plane-span criterion under the same condition, and Theorem 2.8 (PDF p. 13) gives a (Z)-dependent uniform completion time. Gravner–Paguyo–Slivken (2019), source `PR-2ff6120c6cde`, instead proves maximal spanning-time bounds; its Theorem 1.2 is an enhanced/thin time comparison. Do not cite the latter as the seed rectangle theorem.

## Open method interfaces

The accepted source/use cohort gives restricted routes, not complete coverage of every assigned method. G28.03 (Russo–Margulis), G28.04 (clique first-entry), G28.05 (front automata), G28.06 (second moment/Janson), G29.03 (potential/amortized analysis), G30.03 (linear-algebra weak saturation), and G30.05 (coverage LP/fractional dual) have no accepted infection-source route in this revision. Do not infer those tools from adjacent fort counts, finite optimization encodings, or G29/G30 analogies. G29.07 is limited to the fixed-cycle route above; a general fixed-H growth-scaling method remains open. The six accepted G32 certificate uses belong to W19 and are excluded from the 30-row infection cohort.

## Proof obligations that stay model-specific

- **Random probability:** use the actual initial-set law and the source's threshold definition. A necessary first-force event gives an upper bound on success probability only after the relevant degree/count union bound is proved.
- **Extremal seed size:** a time upper bound is not a seed-size lower bound. Use a source that counts seeds or reduces the exact minimum-seed problem.
- **Slow or exact time:** a valid DAG gives an activation-time upper bound. A sequential schedule bounds the full synchronous closure time only if it is complete/saturating; a prefix bounds only the listed targets. To prove at least (t) rounds, show no target rule fires at every earlier round; for graph-\(H\) processes this means excluding all accidental (H-e) copies.
- **Finite to infinite:** per-site finite activation does not imply a uniform finite time filling an infinite domain. A finite-box closure implies plane spanning only when a theorem for the exact update rule and seed support supplies that implication.
- **Optimization certificates:** exact LP, interval, SOS, SAT/SMT, or exhaustive output certifies only the fully specified finite encoding. It does not prove the infection rule is submodular or supply an asymptotic theorem.

Read [method routing](references/method.md), [source cards and limits](references/sources.md), and the [positive](examples/positive.md) and [negative](examples/negative.md) examples. L15's detailed scope, source mapping, computations, and review status are in scope.json（本机附件：`scope.json`）, the revision 12 freeze（本机附件：`evidence/project/expansions/20261115/readers/L15/revision12/freeze.json`）, and revision 12 status（本机附件：`evidence/project/expansions/20261115/readers/L15/revision12/status.json`）. R15 current index v4 contains 30 accepted restricted infection source-use rows (21 new complete-paper reads and 9 canonical complete-read reuses) with zero held or pending infection rows. Six accepted G32 uses remain in W19 and are excluded. Root capture09 confirms 30 eligible distinct work families; method coverage remains incomplete and global quota credit is zero. This source-use count does not complete G28/G29/G30 methods or approve publication or installation.
