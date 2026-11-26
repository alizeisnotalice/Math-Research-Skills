# Unitary fixed-space incidence interface

Scoped reference. *Nonsingular systems of equations over arbitrary groups*
(OpenAI, 5 Oct 2026), SHA-256
`732c93a33db2c8c7da84a2bc8505ac9e00f7fe345731cf9a4bfe00b82c17cea2`,
physical pp. 4--7, Theorem 2.1 and its proof.  Given an integer matrix `B`
of row rank `r`, block sizes `k_i`, and words whose block occurrences are
the entries `b_ij`, form

`D = product_i U(k_i)` and `F_j(X)=diag_(i,s in B_j)(X_i^s) P_j`.

After selecting nonzero leading minors and setting `l_(j_t)=k_t`, the source
uses `H*(U(d);Q)=Lambda(e_1,d,...,e_d,d)`, with
`mu*e_a=e_a tensor 1+1 tensor e_a`, and the fixed-plane incidence class
`alpha(d,l)=PD(p_*[R(d,l)])`.  Its leading term is
`c_(d,l)e_1,d...e_l,d`, `c_(d,l) != 0`.  The product pullback has top
coefficient equal, up to sign, to the product of these coefficients and the
chosen leading minors.  Its nonzero intersection gives
`sum_j dim_C ker(F_j(X)-I) >= sum_i k_i` for some `X`.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf).

This is an incidence/cohomology transfer only after the supplied words,
block lists, row-rank/minor certificate, unitary factors, and orientations
have been fixed.  It neither supplies those data nor converts a fixed-space
intersection into a statement about an arbitrary group presentation.
