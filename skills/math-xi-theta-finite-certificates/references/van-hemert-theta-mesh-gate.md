# Mesh-to-polynomial positivity gate

Source: Leonard van Hemert, *Exact Zero Detection and Compact Arithmetic Realizations for the Riemann Xi Function*, author manuscript v1.0.0, 208 physical pages; reviewed physical pp. 15--17.  Local source identity: SHA-256 `5c6d8d3e070a56576ef938c2dcfe47a7e2a8a1c6ed429612eac503b5a30ee04d`.

Theorem 12 gives a finite lower-polynomial gate for the source's normalized theta defect \(C_y(x)/A_0(y)\).  On a cell \(I=[\alpha,\beta]\), it uses supplied lower and upper moment products

\[
\ell_j(I)=A_{2j}(\alpha)A_0(\beta),\qquad
u_j(I)=A_{2j}(\beta)A_0(\alpha),
\]

with alternating Taylor-coefficient choices to form \(P_{m,I}\).  The source proves \(P_{m,I}\) is a lower bound and gives a compact-rectangle error gate \(T_m(R)+C_R\delta\), where \(\delta\) is the partition mesh.  Corollary 13 turns an independently supplied positive margin into a finite all-cell positivity certificate.

## Required caller evidence

Supply the normalization of \(C_y\) and \(A_{2j}\), certified endpoint moment envelopes, a proved positive lower bound for \(A_0\), a tail bound \(T_m(R)\), and the modulus constant \(C_R\).  Check exact cell coverage and the strict margin.  The cited manuscript explicitly leaves the corresponding global positivity step open; this finite gate neither detects arbitrary Xi zeros nor proves RH.
