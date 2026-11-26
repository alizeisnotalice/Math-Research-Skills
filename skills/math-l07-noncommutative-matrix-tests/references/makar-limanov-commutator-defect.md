# Shift-commutator rank-defect replay

For an integer `n >= 1`, form matrices over `Z`

\[
 X_n=\sum_{j=1}^{n-1}jE_{j,j+1},\qquad
 Y_n=\sum_{j=1}^{n-1}E_{j+1,j}.
\]

The directly checkable identity is

\[
 I_n-[X_n,Y_n]=nE_{n,n}.
\]

Thus the displayed defect has rank one and normalized rank `1/n`.  Run
`scripts/replay_makar_limanov_defect.py --dimension N` to construct the two
integer matrices and check every entry of the identity.

This is only a finite witness for the particular free polynomial
`1 - [x_1,x_2]`; it neither decides noncommutative rank nor proves a
small-rank theorem for an arbitrary free polynomial.

## Source and audit boundary

Yan--Shen--Yang, *On the asymptotic Makar-Limanov rank conjecture*,
arXiv:2610.06800v2 (6 October 2026), physical pp. 1--2, displays this
construction and identity.  The same manuscript's general asymptotic theorem
uses symbolic differential fields, residual improvement, finite compression,
and field descent (pp. 3, 11--21); none of those global steps is adopted by
this replay.
