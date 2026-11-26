# Finite progression-coordinate residue sieve

## Source identity

- Source: OpenAI, *A quadratic bound for Jacobsthal's function*, 25 September
  2026, local original `paper.pdf`, SHA-256
  `f80267eebc82a9b8905057b45b35ef8734485b2b0b7b809a3051c06240cf0b1e`.
- Fixed source URL:
  <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf>.
- Physical p. 4 gives the translation/CRT equivalence for finitely many
  forbidden residue classes.  Physical p. 81, Appendix B, proof of Lemma B.4,
  writes an arithmetic progression as `a+qj`: when `p` is coprime to `q`, each
  sieve prime excludes exactly one coordinate class modulo `p`, and CRT makes
  the intersections single classes modulo their square-free product.

## Accepted finite component

Let `q >= 1`, `(a,q)=1`, and let `S` be a finite set of distinct primes with
`p ∤ q` for every `p in S`.  For a finite coordinate interval
`I = {j in Z: L < j <= U}`, put `P = product(S)`.  Each `p` has the exact bad
coordinate class

`r_p = -a q^{-1} (mod p)`.

For every square-free `d | P`, CRT gives its unique simultaneous class
`r_d = -a q^{-1} (mod d)`.  Thus the number of finite coordinate survivors is
the exact integer identity

`sum_(d | P) mu(d) [floor((U-r_d)/d) - floor((L-r_d)/d)]`.

Equivalently, modulo `P` there are exactly
`product_(p in S)(p-1) = phi(P)` survivor classes.  Consequently the finite
count differs from `(U-L) phi(P)/P` by at most `2^|S|`, directly from the
inclusion--exclusion summands.  The script
`scripts/progression_residue_sieve.py` evaluates these identities in exact
integer arithmetic and, for bounded inputs, independently enumerates both the
coordinate interval and a full period.

## Explicit boundary

This component counts values of `j` for which none of the selected primes
divides `a+qj`.  It does **not** say that those values, or `a+qj`, are prime.
It supplies no Mertens estimate, fundamental-lemma remainder, uniform sieve
bound, or bound for Jacobsthal's function.

In particular, the prime count asserted in Lemma B.4 also invokes the
fundamental lemma (physical p. 6, Lemma 2.1) and a Mertens product estimate;
it is not accepted here.  The paper's main uniform Jacobsthal bound (physical
pp. 71--73) depends additionally on its stopped-tree, local-prime, inverse,
variance, and owner propositions, and remains outside this finite component.
