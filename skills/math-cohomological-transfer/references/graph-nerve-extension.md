# Degree-one extension on a relative graph nerve

## Transfer statement

Let `Z` be compact metric, `A` closed, and let `k` be an abelian group.  Suppose a class in `Čech H¹(A;k)` has been represented on the nerve of a finite relative cover of `A`.  Suppose further that this cover has a finite open refinement `U` of `Z` of multiplicity at most two, with a chosen refinement map, and that after deleting empty restrictions the restricted nerve `N(U|A)` is identified with a subgraph `H` of the graph `G=N(U)`.  Then the pulled-back representative extends to a 1-cocycle of `G` by assigning zero to edges outside `H`.  Its Čech class restricts to the original one.

This is the reusable combinatorial portion of Lemma 10.1 in OpenAI, *The Singer conjecture in dimension four*, `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, PDF SHA-256 `179f73885d0c7f476cf57fa10d3840edea547fda8a372ce6d0480f8df886243e`, p. 41.  The source’s compactness and dimension hypotheses are used to obtain the finite multiplicity-two refinement; they are not checked by the finite script.

## Independent proof

Multiplicity at most two means no point lies in three members of `U`.  Thus `N(U)` has no simplex of dimension two or more, hence is a graph `G`.  Let `c` be the pulled-back 1-cocycle on the subgraph `H`.  Define a 1-cochain `c~` on every oriented edge of `G` by `c~(e)=c(e)` for an edge of `H` and `c~(e)=0` otherwise, extending antisymmetrically when orientations are reversed.  Its restriction is `c`.  Since a graph has no 2-simplices, the cochain differential `d:C¹(G;k)→C²(G;k)` is zero, so `d c~=0`.  Hence `c~` is a 1-cocycle and defines the desired class.  Refinement functoriality gives the prescribed restricted Čech class.

## Exact finite contract

`scripts/extend_graph_h1.py` accepts a finite undirected graph, a listed edge-subgraph, values in `Z/mZ` on its edges, and an explicit list of ambient 2-simplices.  It accepts only if the listed ambient 2-simplices are empty, every subgraph edge belongs to the ambient graph, and the data are nondegenerate.  It then prints the zero extension in a canonical edge order.  This verifies only the final graph-cochain step.

The positive example has a triangular cycle but no filled triangle.  The rejected example supplies a filled 2-simplex, where the argument `C²(G;k)=0` no longer applies.  Neither example certifies that a topological cover has the required nerve.
