# Identity-corner commutator assembly


## Use when

You work over a unital algebra (or a concrete matrix algebra) and have exact
elements (A,D,F,U,V,Z,T,Q), a nonzero scalar σ, and want to certify the
finite algebraic assembly used in Proposition 3.2 of the source.  The input
must satisfy


\[
A+D=[U,V]+[Z,T],\qquad
\sigma(Q-D_0)=Q^2-DQ+Q(A-U)+D_1,
\]

where

\[
D_0=[U,V]-A,\quad
D_1=[Z,V]+D_0U-Z+[U,TZ]-F,\quad \widetilde U=\sigma1+U.
\]

## Procedure

1. Keep the coefficient algebra and all products explicit; do not commute
   symbols unless the coefficient algebra is known commutative.
2. Check both displayed identities exactly.  A numerical residual is not a
   certificate for this tool.
3. Form

\[
B_c=\begin{pmatrix}\widetilde U&1\\Z&0\end{pmatrix},\quad
C_c=\begin{pmatrix}V&T\\Q-D_0+TZ&V+1-\widetilde UT\end{pmatrix},\quad
S=\begin{pmatrix}1&0\\Q&1\end{pmatrix}.
\]

4. Return (B=SB_cS^{-1}), (C=SC_cS^{-1}), and verify directly that
   ([B,C]=\begin{psmallmatrix}A&1\\F&D\end{psmallmatrix}).

## Included exact witness

`scripts/check_identity_corner_scalar_witness.py` verifies the nonzero scalar instance

\[
(A,D,F)=(1,-1,-1),\quad U=V=Z=T=0,\quad Q=-1,\quad \sigma=122.
\]

It proves the two algebraic certificates and the resulting exact commutator
using rational arithmetic.  It also verifies ‖\(\begin{psmallmatrix}1&1\\-1&-1\end{psmallmatrix}\)‖\(_2=2\).

## Scope gate

This is only the finite algebraic conclusion conditional on an exact
certificate (Q).  The source obtains a bounded (Q) from a Banach fixed
point argument under norm hypotheses.  This skill neither re-proves that
analytic existence argument nor transfers the result to a finite von Neumann
algebra, and it gives no uniform commutator bound.

## Provenance

The source record below gives the original locator.  The formula is Proposition 3.2 (physical page
5) of the locally supplied 23-page source.  The witness is independently
checked and is not claimed to be an instance of its global von-Neumann-algebra
theorem.

## Block identity before conjugation

Direct multiplication gives the four blocks of \([B_c,C_c]\) in order as
\(A+Q,\ 1,\ DQ+F-QA-Q^2,\ D-Q\). The lower-left simplification uses the
stated Riccati identity and preserves the order of \(DQ,QA\). These are the
blocks of \(S^{-1}\left(\begin{smallmatrix} A&1\\F&D\end{smallmatrix}\right)S\).

~~~sh
python3 -B scripts/check_identity_corner_scalar_witness.py
~~~

## Source record

- Local filename: `uni-com-bound.pdf`
- SHA-256: `d7531760c01c791767e436c45998ef69733fe883203b2e88431bf06d9ca71b01`
- Physical pages: 23
- Used portion: Proposition 3.2, physical page 5 (with the Sylvester setup on
  physical page 4).

The adopted material is the displayed algebraic construction conditional on a
solution of equation (3.4).  The surrounding fixed-point existence and
operator-norm estimates remain source-dependent and are excluded from this
finite exact witness.
