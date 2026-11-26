# Exact Krylov certificate for switched main eigenvalues

Source: Horace Dong, *The switching conjecture for main eigenvalues holds for
trees of diameter at most 4*, version 2 (local PDF SHA-256
`376072720e813cbb0ada3d9e20c9a6e5910a4de72049f77403f879b8774c2a54`),
physical pp. 3--4, Lemmas 2.1--2.2.

For an integer symmetric matrix `A` with `d` distinct eigenvalues and a sign
vector `s` in `{+1,-1}^n`, form
`K = [s, A s, ..., A^(d-1) s]`.  Orthogonal spectral projections and the
Vandermonde matrix show that `rank_Q(K)` equals the number of eigenvalues
whose projection of `s` is nonzero.  Therefore `rank_Q(K)=d` certifies that
every distinct eigenvalue of `diag(s) A diag(s)` is main.  This reference
uses only that finite-dimensional linear-algebra argument; it does not import
the source's diameter-four tree existence theorem or its finite enumeration.

The helper computes `d` as the degree of the square-free part of the exact
characteristic polynomial and computes the rank over the rationals.  It is a
certificate for a supplied matrix and sign vector, not a search algorithm for
a good switching and not a claim for nonsymmetric matrices.
