# Finite individualization--refinement canonical-form contract

This reference gives a finite, exhaustive canonical-form interface for a
coloured simple graph.  It does not give a polynomial-time bound, certify an
arbitrary heuristic pruning rule, or replace an explicit isomorphism witness.

## Source and version

Brendan D. McKay and Adolfo Piperno, *Practical graph isomorphism, II*,
*Journal of Symbolic Computation* **60** (2014), 94--112, DOI
<https://doi.org/10.1016/j.jsc.2013.09.003>.  The supplied object is
arXiv:1301.1493v1, SHA-256
`2173fcd10d99c269eec4d28d2089887452eb972456c52a1b961a2bf186194029`,
22 physical pages.  The formal conditions and proof are on physical pp. 5--7;
an equitable-refinement realization and a valid invariant construction are on
pp. 8--10.

## Contract

For a finite vertex set, begin with a coloured graph `(G, pi0)`.  An
individualization/refinement implementation can return a canonical form only
after supplying all of the following equivariant data.

1. A refinement `R(G, pi0, nu)` that refines `pi0`, makes every vertex in the
   individualization sequence `nu` a singleton, and satisfies
   `R(G^g, pi0^g, nu^g)=R(G, pi0, nu)^g` for every relabelling `g`.
2. A target-cell selector `T` that returns the empty set exactly for a discrete
   refinement, otherwise a non-singleton cell, and commutes with relabelling.
   Build the finite search tree by branching over every vertex in `T`.
3. A totally ordered node invariant `phi` that is relabelling invariant and
   prefix-monotone at equal depth: a strict comparison between two nodes must
   persist for every pair of their descendant leaves.  On discrete leaves,
   equal `phi` must be equivalent to equality of the *labelled* graphs
   `G^pi` (not merely isomorphism).

With exhaustive leaves, choose any leaf of maximal `phi` and output the
corresponding relabelled coloured graph.  The source's Lemma 4 proves that the
result is independent of the maximizing leaf and is a canonical form.  Equal
maximal leaf invariants also give the stated automorphism recovery formula.

For ordinary equitable refinement, individualize one vertex and repeatedly
split each colour cell by its vector of neighbour counts into an active cell;
the cited realization is only valid when its ordering/tie rules preserve the
equivariance above.  A trace based on equivariantly produced cell split data,
with the labelled leaf graph appended, is one valid way to meet the node-
invariant conditions.

Do not infer that a graph isomorphism solver is polynomial-time, that a
non-equivariant tie-break is canonical, or that a pruning step is sound merely
because it is empirically effective.  The source's pruning theorem requires
its named `PA`, `PB`, or automorphism-backed `PC` operations and their
invariant comparisons.
