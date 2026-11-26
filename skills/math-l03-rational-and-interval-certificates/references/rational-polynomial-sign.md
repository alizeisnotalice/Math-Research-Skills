# Source and scope note

This interface is not distilled from an OpenAI or Google theorem.  Its immediate motivation is the active Euler--Mascheroni project, `T2/euler-gamma-irrationality/rounds/010.md`, whose stated next question asks whether a polynomial formed from adjacent leading terms has a strict sign on `0<t<=1/16` and specifically proposes Bernstein coefficients or integral estimates.

The finite certificate here uses only the elementary Bernstein identity

\[
  q(u)=\sum_{k=0}^d b_k\binom d k u^k(1-u)^{d-k},\qquad 0\leq u\leq1.
\]

All basis functions are strictly positive for `0<u<1`.  Hence nonnegative `b_k` with at least one positive coefficient imply strict positivity in the open interval; exact endpoint evaluation controls endpoints that belong to the requested domain.  The statement is derived directly in the checker and README; no external literature claim is being adopted.

It certifies only a finite supplied polynomial.  It does not construct a Sondow kernel, prove its norm is subexponential, establish an infinite family, prove any remainder representation, or prove irrationality of the Euler--Mascheroni constant.
