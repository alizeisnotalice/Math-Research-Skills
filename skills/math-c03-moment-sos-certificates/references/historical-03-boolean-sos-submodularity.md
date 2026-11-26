# Boolean SOS mixed-derivative gate for submodularity

Let \(f:2^{[n]}\to\mathbb R\) have multilinear extension \(F\), and let
\[
 I_2[x_{-i,j}]=\langle x_k^2-x_k:k\ne i,j\rangle.
\]
For every distinct \(i,j\), suppose an exact certificate is supplied:
\[
 -\partial_{ij}^2F(x)\equiv\sum_r q_{r,ij}(x_{-i,j})^2
 \pmod {I_2[x_{-i,j}]},\qquad \deg q_{r,ij}\le t.
\]
Then \(f\) is submodular.

The proof is finite algebra on the Boolean cube.  Telescoping one coordinate
at a time expresses a difference of first derivatives as a sum of
\((y_j-x_j)(-\partial_{ij}^2F)\) terms.  On Boolean variables,
\((y_j-x_j)^2\equiv y_j-x_j\) in the corresponding product ideal.  Each
summand becomes a square
\((y_j-x_j)q_{r,ij}([xy]^j_{-i,j})\)^2.  Therefore the first-derivative
differences have the required nonnegative sign on Boolean assignments, and
the standard telescoping identity for \(F(x)-F(y)\) gives the discrete
submodularity inequality.

Certificate gate: give the full multilinear \(F\), every pair \((i,j)\),
the Boolean-ideal congruence, and exact PSD Gram/SOS data.  A floating SDP
status is not a certificate.  This gate does not invoke the paper's imported
finite-order Lasserre completeness result.

Source: *Sum of Squares Submodularity*, arXiv:2510.24550v2, physical pp.6–7
(Definitions 3–6) and pp.31–32 (Lemma 5 and Theorem 1 proof), source SHA-256
`22ee0c0eb9f8ca40979a7eee88dbb7d655bda13c4952d974f0946eb29b66439f`.
