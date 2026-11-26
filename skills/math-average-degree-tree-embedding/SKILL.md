---
name: math-average-degree-tree-embedding
description: 在有限简单无向图中，按平均度严格阈值核对给定树的嵌入，并返回可检查的顶点映射。
---

# Average-degree tree embedding

Use this skill for a finite simple undirected host graph \(G\) and a finite
tree \(T\) with \(t\geq2\) vertices.  First validate both adjacency matrices,
connectedness and acyclicity of \(T\), and the strict hypothesis

\[
 2|E(G)|/|V(G)|>t-2.
\]

Then find an injective map from \(V(T)\) to \(V(G)\) that carries every tree
edge to a host edge.  `scripts/check_average_degree_tree_embedding.py` does
these finite checks in exact integer arithmetic and returns such a map.  Its
exhaustive search is a certificate for its supplied finite input, not an
efficient algorithmic guarantee.

The source-specific counting proof is in
[Average-degree tree containment](references/average-degree-tree-containment.md).
It proves that this strict threshold suffices for every finite simple host
graph and every \(t\)-vertex tree.  Equality is deliberately excluded: the
complete graph on \(t-1\) vertices shows that \(t-2\) cannot be substituted
for a strict inequality.  Multigraphs, directed graphs, forests, approximate
degree data, and a non-tree target are outside the interface.
