# Exact row-split criterion for 2-by-n bar multisets

**Source status:** author-hosted preprint. **Source:** Horace Dong, *Multisets of bars that do not tile a 2 x n rectangle: the optimal growth order*, SHA-256 `d7f50c9bd23a6b583397fc9a7b5f32fcbd4c33b15976c4860d6b2bf83507930b`, physical pp. 3–4, [source PDF](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/bar-tiling-defect/note.pdf).

This gives L05 a specialized exact feasibility encoding rather than a general tiling solver. For a nonnegative count vector `m=(m_1,...,m_k)` of total area `2n`, a **row split** is `m=a+b+v` with nonnegative integer vectors, `v` supported only at length 2, and

`sum ell*a_ell+v_2=n=sum ell*b_ell+v_2`.

Proposition 1 (pp. 3–4) proves: the multiset tiles `[0,2] x [0,n]` iff it has a row split. Forward construction places `v_2` transverse dominoes then packs `a,b` end-to-end in the two rows. Conversely, bars touching one boundary yield the required split; the argument permits real placements and proves no unrecorded grid restriction.

Encode `a_ell,b_ell,v_2` as integer variables with the displayed equalities and nonnegativity, then validate a satisfying split by direct sums. Failure of an unproved search procedure is not an infeasibility certificate. This reference does not adopt the source's asymptotic defect theorem or its Lean claim.
