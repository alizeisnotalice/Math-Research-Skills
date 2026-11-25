---
name: probability-poset-counting-sampling
description: Count linear extensions and related finite poset families, derive entropy bounds, or build exact samplers; also use for finite graph-labeling peak constraints that admit a verifiable counting recurrence.
---

# Poset counting and exact sampling

**Portable candidate status (2026-11-16):** this sibling carries 30 R05 high-scoped works, all 30 complete papers; no books are counted, and two older partial-book records remain excluded. R05 accepted 30/30 source-specific uses with 220 binding checks and zero failures. Seven rows carry explicit new method IDs in the R05 source ledger; 23 certify only their named legacy modules. Three R01 supplemental method-scope rows attach to M0006, M0007, and X004, already among these same 30 works; they do not add quota entries. The earlier R05 v5 stage packet and this package’s v1 portability failure remain preserved. This is a single-entry v3 candidate awaiting independent R05 re-review. No release or installation approval is claimed. See the accepted scope register（本机附件：`references/accepted_scope_register.md`）, method coverage（本机附件：`references/method_coverage.md`）, and portable evidence index（本机附件：`evidence/portable_index.md`）.

Use this skill to count linear extensions, finite graph-labeling peak families, or exact samples from a specified finite target. State the poset or graph, strict versus weak order, graph versus sequence peaks, endpoint convention, boundary edges, labels, and conditioning event. Sequence peaks and graph-local maxima are different statistics.

For fixed-poset linear extensions, use the ideal/maximal-element recurrence and weight sampler branches by exact completion counts. For graph peak constraints, use the descending-order recurrence in [method.md](references/method.md), proving that its state retains all future constraints. The direct recurrence's strict local-maximum predicate is different from M0002's source convention, which excludes degree-0 and degree-1 vertices. The M0002 `GraphPeakSetAlgorithm` is approved here only for a known `G`-admissible required set, with branch-local copies and all recursion leaves collected.

A conjunction of comparisons can define one poset event. Exact peak constraints usually contain disjunctions over neighbors, so they do not automatically equal the linear extensions of one fixed poset. Any union encoding needs a disjointness proof or correct overlap weights. Keep exact counting, approximate counting, approximate sampling, and exact sampling distinct.

See the [finite positive cases](examples/positive.md), [model and predicate boundaries](examples/negative.md), the source-specific register（本机附件：`references/accepted_scope_register.md`）, and the [source index](references/sources.md). The method map gives proof obligations for all twelve assigned G01/G02 atoms; the current accepted source associations are partial and explicitly listed.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## A022 boundary

The portable free-boundary square calculation covers n=2,3,4, with independent permutation enumeration through n=3 and one finite exact branch-sampler trace. This is finite evidence, not an asymptotic result. Torus/cycle, Eden-growth, regular-tree, and fixed-metric-graph-subdivision results do not imply a growing free-boundary square theorem without a separate proof.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。

## 有限随机位预算

固定公平位数内近似抽取有限均匀索引时，用[固定随机位的均匀索引逼近](references/fixed-bit-uniform-draw.md)计算全变差和逐次调用的总预算。
