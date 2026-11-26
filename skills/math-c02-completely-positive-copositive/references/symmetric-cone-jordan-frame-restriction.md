# Jordan-frame restriction to an orthant copositive cone

Source: M. Nishijima, *Copositive and completely positive cones over symmetric
cones of rank at least 5*, arXiv:2602.23725v3, Lemma 3.1 (physical p. 11).
This is a preprint source statement; the reduction below is included in the
source proof.

Let `K` be self-dual and let pairwise orthogonal extreme-ray generators
`delta_1,...,delta_r` be supplied.  Define

`f(M) = sum_{i,j} M_ij delta_i tensor delta_j`.

On the indicated span, `COP(K) intersect V = f(COP_r)`.  For the forward
inclusion set `y_i=<delta_i,x>` for `x in K`; self-duality gives `y>=0` and
`q_f(M)(x)=y^T M y`.  Conversely, for a prescribed `y>=0`, use
`x=sum_i y_i delta_i/<delta_i,delta_i>`; orthogonality gives
`q_f(M)(x)=y^T M y`.

This is an exact restriction identity, not a general copositivity decision
procedure and not the paper's non-spectrahedral-shadow conclusion.  The caller
must supply exact inner products, membership of the rays in the self-dual cone,
and their pairwise orthogonality.
