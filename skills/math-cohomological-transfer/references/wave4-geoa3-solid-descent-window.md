# Finite solid descent window for compact p-adic analytic groups

**Source.** OpenAI, *A rational obstruction to strong chromatic splitting at height three*, Lemma 2.1 and the finite Postnikov-window argument in §7.1, PDF pp. 8--9, 36; SHA-256 `6d0bd23f35dc42a1f645f99f7054f2e2f8d0033b78f3e3803b86774fc0558184`.

## Input contract

Take a compact p-adic analytic group `G` with no element of order `p`, its completed group ring `Lambda_G=Z_p[[G]]`, and a derived-solid `Z_p`-complex `K` with continuous `G`-action.  For the scalar statement, require that `K` is bounded below and that an operator `gamma` commutes with `G` and acts by `lambda_j in Q_p` on `H^j(K)(*)[1/p]`.

## Reuse

Choose the finite projective profinite `Lambda_G`-resolution of `Z_p` of length `dim G`.  The source identifies
`R Gamma(G,K)(*)` with the finite total complex `Hom_(Lambda_G)(P.,K)`; the descent spectral-sequence row from `H^j(K)` retains scalar `lambda_j` after rationalization.  In a fixed abutment degree `q`, the §7.1 argument permits truncation to the finite Postnikov interval `[q,q+dim G]`, rather than exchanging rationalization with an infinite totalization.

This is a coefficient/descent interface.  It does not supply a finite resolution for a group with p-torsion, an action not continuous in the stated solid sense, or a scalar action on condensed sheaves merely from an unchecked pointwise identity.

## 固定来源

- 物理页 8, 9, 36。Lemma 2.1; equation (7.5) and Section 7.1 finite-window argument SHA-256 `6d0bd23f35dc42a1f645f99f7054f2e2f8d0033b78f3e3803b86774fc0558184`。[A rational obstruction to strong chromatic splitting at height three](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/paper.pdf)
