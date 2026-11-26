# Exact folding of a polynomial continued-fraction layer

This is a **scoped finite matrix identity**, not a certificate that a proposed
continued fraction converges to, or represents, a named constant.

## Source and version

Ofir Razon, Yoav Harris, Shahar Gottlieb, Dan Carmon, Ofir David, and Ido
Kaminer, *Automated Search for Conjectures on Mathematical Constants using
Analysis of Integer Sequences*, Proceedings of Machine Learning Research 202
(ICML 2023), 28809--28842.  Official formal record:
<https://proceedings.mlr.press/v202/razon23a.html>.  The supplied object is
the manuscript labelled arXiv:2212.09470v2 in the source inventory, SHA-256
`32f641cc293405fea0ee0b98710aa00a2c47e0bca7bcd6fc7fc79ee019186480`,
physical pp. 18--20.  The formal transform and its calculation occur in
Appendix B.2, equations (26)--(29).

## Exact interface

Let

\[
 M_n=\begin{pmatrix}c_n&d_n\\e_n&f_n\end{pmatrix},\qquad
 e_n e_{n+1}\ne0,
\]

with entries in a commutative exact coefficient ring.  Define

\[
 U_n=\begin{pmatrix}1&c_n\\0&e_n\end{pmatrix},\qquad
 U_{n-1}=\begin{pmatrix}e_n&-c_n\\0&1\end{pmatrix}.
\]

Direct multiplication gives the source's folding layer

\[
 U_{n-1}M_nU_{n+1}=
 \begin{pmatrix}
 0&e_{n+1}(e_nd_n-c_nf_n)\\
 e_n&e_nc_{n+1}+f_ne_{n+1}
 \end{pmatrix}.
\]

If an independently justified continued-fraction equivalence transform uses
the nonzero factors `g_n=e_n`, the normalized layer is

\[
 \begin{pmatrix}
 0&e_{n-1}e_{n+1}(e_nd_n-c_nf_n)\\
 1&e_nc_{n+1}+f_ne_{n+1}
 \end{pmatrix}.
\]

Run `scripts/supp_14_folding_layer.py` on exact integer input to audit this
one-layer identity.  It does not establish the infinite product limit, the
Möbius value in (26), polynomiality outside the supplied layer, or an
irrationality claim.  In particular, an ESMA/PSLQ-generated candidate must
still have an independent identity and convergence proof.

The source's p. 20 example has
`(c,d,e,f,c_next,e_next,e_prev)=(4,5,5,6,6,7,3)` and normalizes to
`[[0,21],[1,72]]`.
