# Sparse exponent support admission

This route is independent of Hankel determinants, Padé approximants, and Hecke--Mahler rotation differences.  It applies to a binary expansion
\[
\xi=\sum_{n\geq 0} b_n2^{-a_n}
\]
with bounded integer coefficients and a strictly increasing exponent sequence.  The usable source theorem requires the exponent sequence to be both **sparse** and **thin**: for every `q`, sums of at most `q` exponents must have arbitrarily long adjacent gaps, and the number of representations by `q` exponents must be uniformly bounded.  Under those global conditions the source's digit-support argument proves transcendence when infinitely many `b_n` are nonzero.

Run `scripts/sparse_exponent_support_audit.py` on a supplied finite exponent prefix.  It counts ordered finite `q`-term representations exactly, lists representable sums, and reports observed gaps.  This is a finite audit only.  It cannot prove the all-`q`, unbounded-gap, or infinite-coefficient hypotheses, and never turns a finite prefix into a transcendence proof.

## Source boundary

Ashum Kaibkhanov and Arkadiy Skopenkov, *A short proof of the transcendence of the Mahler number*, arXiv:1204.5045v3, local SHA-256 `a1e9de85252534bd83575834e50ac4f3658221603141aae4984658dc678924d7`, physical PDF pp. 2--5.  The locally checked proof first bounds the number of representations of an integer as a sum of `q` powers of two by `(q!)^2`, then separates a nonzero leading digit cluster from the tail.  Its final generalization states the sparse-and-thin criterion above.

The application is not an Euler-constant method.  It may be used only after an exact sparse binary expansion and the global conditions have been independently proved.
