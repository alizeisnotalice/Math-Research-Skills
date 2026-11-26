# Finite partition–MST capacity certificate

Use this skill for a finite, connected, simple undirected graph with nonnegative rational edge capacities `z` and a nonnegative rational threshold `q`. It checks

\[
 z(E(P))\ge q(|P|-1)
\]

for every vertex partition `P`, by exact enumeration. It is a finite certificate routine, not an implementation of a polynomial-time separation oracle and not a strong-thin-tree constructor.

Run:

```sh
python3 -B scripts/check_partition_mst.py INPUT.json
```

All numbers are integer or rational strings such as `"7/12"`; JSON floating-point values are rejected. The output records the minimum partition ratio. A one-vertex graph is feasible by vacuity and has a null ratio. On failure it returns a partition `P` and the indicator length `ell` of its crossing edges. Every spanning tree crosses at least `|P|-1` blocks. Kruskal computes the exact value, which can be larger for a partition with a disconnected block. The output certifies

\[
 z\mathbin\cdot\ell < q\,\operatorname{MST}(\ell).
\]

Require a connected graph: otherwise this particular MST certificate has no finite spanning-tree value. For a feasible output, exhaustive partition enumeration is the certificate scope; it does not prove polynomial running time for large graphs.

## Source and route

This is the stated finite identity in OpenAI, *A polynomial-time construction of strong thin trees*, Lemma 3.3, physical p.19, local PDF SHA-256 `da0e75ba53ff393fd57e9028170fce25aed47ae02954131c9eb04513bdffa658`.

Route finite optimization/separation uses to [L04 mathematical programming workflow](../SKILL.md) when installed. Do not claim the paper's signing, iterative, or strong-thin-tree conclusions from this check.
