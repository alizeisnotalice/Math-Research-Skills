# Active-gradient separation without a sphere minimax swap

Source context: R. Abbasov, *The Unified Separation Condition: A General
Constraint Qualification for Smooth and Nonsmooth Optimization*,
arXiv:2609.16981v1, Lemma 3.1 and Theorem 3.4 (physical pp. 6--8).

For a nonempty compact convex set `K` of active gradients, let `p` be a
closest point of `K` to zero.  The projection inequality gives
`dot(v,p) >= ||p||^2` for every `v in K`.  If `p != 0`, putting
`d=-p/||p||` yields

`max_{v in K} dot(v,d) = -||p||`.

This supplies the finite-dimensional separation identity directly; it does
not use a minimax interchange over the nonconvex unit sphere.  The companion
checker verifies a caller-supplied finite convex-hull projection certificate.

This reference does **not** establish the paper's exact-penalty theorem.  That
step imports a Demyanov result and requires its local attainment, lower-bound,
and continuity hypotheses.
