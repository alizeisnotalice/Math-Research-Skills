# Degree-ordered Kruskal non-bridge certificate

Google Cogentic, *Unconditional Edge Reconstruction of Simple Graphs of Linear
Density*, physical pp. 12--14, defines a degree-compatible vertex order and
the associated lexicographic Kruskal spanning tree.  The local source is
`10_Google_Cogentic_2026-11-25/PDF/06_edge_reconstruction.pdf`, 47 physical
pages, SHA-256 `170b2fc1f241cc8325e0b5573d444e061b1b7bb8fb3083a3ac88cabd0ce4f196`.
The fixed first-publication commit is
[4a7bc8ab0bc7](https://github.com/google-research/google-research/commit/4a7bc8ab0bc7).

For a connected finite simple graph, order vertices increasingly by degree
with a declared label tie-break.  Orient each edge towards its larger ordered
endpoint, give it that endpoint's degree as weight, and process edges in the
resulting lexicographic order.  The new script verifies the finite content of
Lemma 3.1(1) at each selected threshold:

- the tree edges of weight below the threshold span every component induced by
  lower-degree vertices
- after contraction, the number of components having at least two tree exits
  is at most `|H|-1`
- the specified tree edges incident to `H` number at most `2|H|-2`
- each one-exit component attaches through the least ordered high-degree
  neighbour

Run the internal enumeration and a supplied instance with exact integer graph
operations.

```sh
python3 -B scripts/check_degree_ordered_kruskal.py --self-test
python3 -B scripts/check_degree_ordered_kruskal.py examples/kruskal-nonregular.json --threshold 3
```

The self-test enumerates all labelled connected graphs on four vertices and a
five-vertex non-regular graph.  The component-label comparison in the command
uses the displayed vertex labels as a rigid sufficient representation.  The
paper's labelled-component isomorphism quotient, Lemma 3.1(2)--(3), and the
global theorem at density `m >= 1000 n` remain source-level dependencies.
