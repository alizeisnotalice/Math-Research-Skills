# Formal problem boundary: C118

## Recorded question

The formal120 input records C118, “带负边随机同步的阈值,” as asking whether independently generated symmetric edge signs with mean parameter \(\delta\) yield high-probability global synchronization of the random-sign complete graph when
\[
\delta\ge(1+\epsilon)\sqrt{\frac{\log n}{2n}}.
\]
The cited problem source is *Randomstrasse101: Open Problems of 2024*, Conjecture 4, PDF p. 3. The exact source locator and statement are carried in the local [C118 formal record](../problem-inputs/C118_record.json); this W24 package does not claim a fresh full-text read of that problem-list paper. The local 2025 Randomstrasse collection is a different edition and is not substituted for it.

## Mapping

- **Role:** auxiliary / unresolved. No W24 result is presented as solving C118.
- **Closest direct model-family method:** PGEL-001, Theorem 3.2, for the independent symmetric signed Erdős–Rényi model and its rank-\(r\) sphere relaxation. The exact sufficient inequality, fixed-\(\eta\) quantifier, probability space, and proof dependency are in the [source card](../sources/cards/PGEL-001.md).
- **Unproved transfer:** at \(p=1\), that sufficient regime is about twice the proposed small-bias threshold (up to the fixed slack). It does not establish the target threshold, necessity, or a matching window.
- **Main interface still missing:** a uniform-in-phase/configuration proof at the target scale, with a valid approximation/discretization bound and a rigorous route to the requested synchronization conclusion. Pointwise concentration alone is insufficient.
- **No signed/oriented transfer:** positive undirected expansion or dense-graph methods in PGEL-002–012 and PGEL-017/018/032 are not evidence for the signed complete graph. PGEL-029 is an oriented signed deterministic model and is retained only as nonquota background; its DAG and single-cycle statements do not imply a random complete-graph threshold.

The other source methods remain in their own scopes: PGEL-019 is a deterministic signed-Laplacian/cycle-space source with exact triangle boundaries; PGEL-021 constructs explicit positive graphs rather than typical random graphs; PGEL-022–026 concern specified degeneracy, stationary-state, or complex-root questions; PGEL-030/031/033/040/041/045 use distinct complete-graph, graphon, continuum, deterministic graph, or fractal models. Their precise conditions and quarantined source issues are indexed in the [source guide](source-guide.md) and cards.

## Scope statement

This skill can identify a sufficient method and state the missing interface. It cannot turn an auxiliary theorem, a finite example, a cited high-rank background result, or a numerically tested condition into a proof of C118. The open threshold remains open relative to this evidence set.
