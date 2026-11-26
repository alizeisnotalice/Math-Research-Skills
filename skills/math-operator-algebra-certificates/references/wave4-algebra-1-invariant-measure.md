# Wave 4 algebra-1: two-generator invariant-measure obstruction

OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, SHA-256 `af1c052828ec09138c76a64edeed05edd429e4634bf61a4fecdda9d86fd1eb9b`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf), physical pp. 5, 13, and 16--17, Lemmas 2.1 and 5.1--5.3.

The source chooses `A,B in SL_2(C)` with `tr(A)=tr(B)=1`, `tr(A^-1B)=-sqrt(2)`, and `tr(AB)=1+sqrt(2)>2`; `A,B` have no common eigenline. A nonzero fiberwise Hermitian quadratic psh function yields a nonzero squared seminorm invariant under their lifts, then a finite positive invariant Borel measure on `P^1` of mass `2 pi b`.

For `T=AB`, projectively conjugate to `z |-> lambda z` with `|lambda|>1`, the half-open annuli `C_n={R^n<=|z|<R^(n+1)}` are translates. Finiteness forces their common invariant mass to vanish, so the measure is supported on the at-most-two fixed points of `T`. The projective order-three actions of `A,B` then fix that support pointwise, yielding a forbidden common eigenline.

This finite dynamics test is useful only after exact matrices and the seminorm-to-measure construction are supplied. It does not construct the bundle, prove psh regularity, or certify the paper's Griffiths-positivity conclusion.
