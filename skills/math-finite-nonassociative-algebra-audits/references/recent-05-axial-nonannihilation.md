# A four-dimensional axial-algebra replay

Scoped reference for the finite multiplication-table component of Horace Maxwell,
*A simple primitive axial algebra with a disconnected non-annihilation graph, and a
decomposable axial block* (September 2026 author manuscript), SHA-256
`6e02d61590ee5b2efe3a3325f0bae35c3a6b5f4c86ec24232028be96a518f304`.

## Source locus and extracted operation

Theorem A (p. 2) specifies a commutative algebra over \(\mathbb Q\), on ordered
basis \((a,b,x,c)\), by

\[
\begin{aligned}
&a^2=a,\quad b^2=b,\quad x^2=x,\quad c^2=c,\\
&ab=\tfrac14(a+b-x),\quad ax=\tfrac14(a-b+x),\\
&bx=\tfrac14(-a+b+x),\quad ac=bc=0,\\
&cx=\tfrac12(-a-b+x)-\tfrac14c.
\end{aligned}
\]

Sections 2--3 (pp. 4--5) give the finite checks replayed here.  For the axes
\(a,b,c\), they provide the indicated \(1,0,1/2\)-eigenvectors, selected
eigenvector-square identities, and a simplicity test.  The latter uses
\(P_c=2\operatorname{ad}_c^2-\operatorname{ad}_c\), so that
\(P_c(u)=\varphi(u)c\).  The four functionals
\(\varphi,\varphi\!\circ\!\operatorname{ad}_a,
\varphi\!\circ\!\operatorname{ad}_b,
\varphi\!\circ\!\operatorname{ad}_x\) have coefficient rows

\[
(0,0,-\tfrac12,1),\quad (0,\tfrac18,-\tfrac18,0),\quad
(\tfrac18,0,-\tfrac18,0),\quad
(-\tfrac18,-\tfrac18,-\tfrac12,-\tfrac12),
\]

of rank four.  The listed reconstruction identities then recover \(a,b,x\)
from \(c\) inside every nonzero ideal.

## Replay boundary

`scripts/replay_recent05_axial_nonannihilation.py --self-test` uses exact rational
arithmetic only.  It verifies the source's displayed table, the eigenvector and
fusion products used in the proof, the rank-four functional test, the
reconstruction identities, and the non-annihilating cross product \(xc\ne0\).
Its negative test changes only that cross product and must be rejected.

This is a checker for this supplied finite table; it does not classify arbitrary
axial algebras, establish a general fusion-law theorem, or transfer the result to
other fields or parameters.
