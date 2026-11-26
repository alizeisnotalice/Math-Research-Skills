# Ordered Andrews--Curtis trace contract

Source: Amey Thakur, *Length as Priority, Not Constraint: Search Geometry of the Andrews--Curtis Challenge Pool*, author manuscript, 18 physical pages; reviewed physical pp. 1--5.  Local source identity: SHA-256 `f3d6dfde39e6e5a214c8f98a59a16e7f0061b27a6f1e4cbb27677364ff9bafd9`.

The source defines a rank-two state as an **ordered** pair of freely reduced words \((r_0,r_1)\) in the free group on \(x,y\), with standard target \((x,y)\).  It uses exactly these moves on one relator at a time:

\[
r_i\mapsto r_i^{-1},\qquad
r_i\mapsto r_i r_j^{\pm1}\ (j\ne i),\qquad
r_i\mapsto c r_i c^{-1}\ (c\in\{x,x^{-1},y,y^{-1}\}).
\]

After each move, adjacent inverse letters are freely reduced.  Every move has an explicit inverse: inversion is self-inverse, right multiplication changes its sign, and conjugation replaces \(c\) by \(c^{-1}\).  The source emphasizes that `(y,x)` is not the ordered target.

## Finite replay boundary

`check_ac_trace.py` implements exactly this rank-two syntax.  It verifies a submitted trace and its reverse, so an accepted result is a finite, exact edge-by-edge certificate in the stated move graph.  It does not inspect a claimed SAIR pool, a reference verifier, a search frontier, a state count, a length optimum, or a no-reduction assertion.
