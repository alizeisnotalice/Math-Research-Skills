# Finite hypergraph-support capture

This is the precise finite combinatorial component of Lemma 3.2 in *A
uniform influence bound for hypergraph properties* (OpenAI Math preprint,
5 October 2026, physical PDF pp. 5--6; local SHA-256
`64d690bef14f4214272df2f04ab9cf843646b472171b68fb7869d7889203cb99`).
The pinned source is
<https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf>.

Let `S` be a nonempty collection of distinct `r`-edges of `[n]`, with
`n >= r >= 3`, and let `B` be uniform among the `m`-subsets of `[n]`.  Put
`F_B={e:e intersect B is nonempty}`.  For real `k>0`, set
\(L=(k/r)^{r/(r-1)}\).  If \(1\le m\le n\),
\(1\le |S|\le L\), and
\[
 rL\frac{m-1}{n-1}\le\frac12,
\]
then
\[
 \Pr_B\{1\le |S\cap F_B|\le k\}\ge\frac{m}{2n}.
\]

For completeness, write `s=|S|`, `V` for the union of its edges, and `v=|V|`.
Since \(s\le {v\choose r}\le v^r\), some vertex \(u\in V\) has degree
between 1 and \(rs/v\le rs^{(r-1)/r}\le k\).  Conditional on `u in B`, a
union bound gives
\[
 \Pr(B\cap V=\{u\})\ge\frac mn\left(1-(v-1)\frac{m-1}{n-1}\right)
 \ge\frac m{2n},
\]
because \(v\le rs\le rL\).  On this event exactly the support edges through
`u` meet `B`, and their number is in `[1,k]`.

`scripts/check_hypergraph_support_capture.py` is an exact finite replay for
integer `k`: it validates the lemma's sufficient hypotheses using rational
powered comparisons and enumerates all blocks.  It is a certificate for the
given finite input, not a replacement for the general proof.

This component does **not** establish the paper's restriction/orbit-to-
influence bridge, its Fourier estimate, or a general uniform-influence / sharp
threshold theorem.  Those require the separate Boolean-product model and the
remaining hypotheses on the property.
