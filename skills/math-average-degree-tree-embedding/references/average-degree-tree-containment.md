# Average-degree tree containment

Let \(G\) be a finite simple undirected graph with \(n\) vertices and \(m\)
edges, and let \(T\) be a tree on \(t\geq2\) vertices.  If
\(2m/n>t-2\), then \(G\) contains every such \(T\).

Here is the checked counting route.  Let \(M(G)\) consist of pairs
\((\pi,i)\), where \(\pi=(v_1,\ldots,v_n)\) is an ordering and
\(v_1v_i\) is an edge.  Direct edge counting gives
\(|M(G)|=2m(n-1)!\).  For a rooted tree \((T,r)\), let \(R(T,r)\) be
the pairs for which the initial segment through \(i\) contains a rooted copy
of \(T\) mapping \(r\) to \(v_1\).  Induction on \(t\) establishes

\[
 |M(G)|\leq |R(T,r)|+(t-2)n!.
\]

For a leaf root, reverse the first \(i\) positions after excluding the first
successful initial segment; the excluded choices number at most \(n!\), and
the reversal is injective.  For a non-leaf root, split \(T\) into two rooted
subtrees meeting only at the root.  Moving the block between the first two
successful segment indices gives an injection into
\(M(G)\setminus R(T_2,r)\), again losing at most \(n!\) first choices.
Combining the two induction bounds proves the displayed inequality.  If no
copy of \(T\) existed then \(R(T,r)\) would be empty, giving
\(2m/n\leq t-2\), a contradiction.

This is a complete proof route for the stated finite simple-graph theorem;
the external GPT/Lean attribution in the exposition is not used as a premise.
The accompanying script independently checks only individual finite inputs by
exhaustive embedding search; it does not formalize the counting proof.

Source checked: David R. Wood, *The Erdős--Sós Theorem*, arXiv:2609.17877v1
(17 September 2026), physical pp. 2--4, SHA-256
`65c23edb27fe836023ea27fd6c176c43748a88bffd46d8cc8ef4f057a77b428d`.
Physical p. 1 states the theorem and scope; pp. 2--4 give the definitions,
two injections, and induction used above.
