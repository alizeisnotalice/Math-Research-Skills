# Contract and exact proof

## Source and verified locus

This package distils only Theorem 2.1 of Xiaoyu Xu, Qianqian Xu, Ying Hua,
and Qingzhi Yang, *Sum of Squares Decompositions for Structured Biquadratic
Forms*, arXiv:2512.02734v2 (11 December 2025).  The source used for this
review is the 13-physical-page local PDF with SHA-256
`0866821532b1970e753a4228b30402966ff9a495bb954c2fbecf01d728c1c1ab`.
The theorem and its matrix argument occur on pp. 3--4.  Page 5 labels the
M-biquadratic and B0-biquadratic extensions as conjectures and they are
excluded here.  Primary record: <https://arxiv.org/abs/2512.02734>; PDF:
<https://arxiv.org/pdf/2512.02734v2>.

## Input

For positive `m,n`, encode

\[
B(x,y)=\sum_{i,k=0}^{m-1}\sum_{j,l=0}^{n-1}a_{ijkl}x_i y_jx_k y_l
\]

as `M[i*n+j][k*n+l] = a_ijkl`, using only exact integers or fraction strings.
The tool verifies the source's coefficient equalities
\(a_{ijkl}=a_{kjil}=a_{klij}\), nonnegative diagonal entries, and

\[
a_{ijij}\ge\sum_{(k,l)\ne(i,j)}|a_{ijkl}|.
\]

## Why the output is a certificate

Put \(z_{(i,j)}=x_i y_j\).  Let
\(d_p=M_{pp}-\sum_{q\ne p}|M_{pq}|\).  The checked assumptions make every
\(d_p\) nonnegative.  Exact expansion gives

\[
z^TMz=\sum_pd_pz_p^2+
\sum_{p<q}|M_{pq}|\bigl(z_p+\operatorname{sgn}(M_{pq})z_q\bigr)^2.
\]

Indeed, a cross term contributes \(2M_{pq}z_pz_q\); its diagonal
contributions combine with \(d_p\) to give \(M_{pp}\).  Each square is a
square of a bilinear form in `(x,y)`.  The script rebuilds the entire rational
Gram matrix from its returned terms before accepting, so the output is not a
floating-point PSD claim.

## Scope boundary

This component is more specialized than `math-c03-moment-sos-certificates`:
that existing skill is a general workflow for truncated moment/SOS and Gram
certificates, whereas this package supplies a closed-form exact certificate
for one structured finite matrix class.  It must not be used to infer that an
arbitrary PSD biquadratic form is SOS, that a nonnegative polynomial is SOS,
or that a finite-order hierarchy is complete.
