# Finite Lipschitz-free coefficient bounds

Let `(N,d,o)` be a finite pointed metric space, with `d(x,y) >= 1` for distinct points, and let
`B >= diam(N)`.  For coefficients `c_o=0`, put `Jc = sum_x c_x delta_x` in the Lipschitz-free
space `F(N)`.  Then `(1/2) ||c||_1 <= ||Jc|| <= B ||c||_1`.

For the upper bound, `||delta_x||=d(x,o)<=B`, so the triangle inequality gives the claim.  For
the lower bound define `f(o)=0` and, for every nonbasepoint with nonzero coefficient,
`f(x)=sign(c_x)/2` (and use zero at a zero coefficient).  Every pair of values differs by at
most one.  The separation assumption therefore makes `f` 1-Lipschitz, and dual evaluation gives
`||Jc|| >= (Jc)(f) = (1/2) sum_x |c_x|`.

The checker verifies the finite metric axioms, separation, the diameter bound, and this exact
test-function computation over rational input.  It does not compute the norm or transfer the
finite calculation to a countable space or to an approximation-property assertion.

Source audited: *A uniformly discrete counterexample to bounded approximation in Lipschitz-free
spaces*, OpenAI preprint, pinned commit `3344da59991ed94f9ba711217b29c1d760badfa6`, PDF p.5,
Proposition 2.1 (local SHA-256 `aa4ce066ba72c12f5984b7f401355a7030c1cecc9d9148278113a29e89914083`).
