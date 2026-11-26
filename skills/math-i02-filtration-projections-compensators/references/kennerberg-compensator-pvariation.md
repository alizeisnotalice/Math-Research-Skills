# Canonical p-variation stability for compensator integrals

Use this source-specific contract when a compensator integral is already defined on one filtered probability space. Let `p > 1`, let `X, X_n` be real adapted cadlag processes with jump measures and predictable compensators `(mu, nu)` and `(mu_n, nu_n)`, and fix a finite horizon `t`.

Theorem 4.2 of Kennerberg, arXiv:2605.11783v3, gives
`[f_n * nu_n - f * nu]^(p)_t -> 0` in probability when all three processes `X`, `X_n`, and `X_n-X` have finite canonical p-variation, the last variation tends to zero in probability, both integrals are locally finite variation, and all of the following are checked.

- `LG0` supplies a locally bounded predictable linear bound near zero.
- `LU` supplies local uniform convergence of the predictable integrands.
- `JC` excludes discontinuities of `f(s, .)` at jumps of `X`.
- `BEp` supplies the barycentric tail bounds at predictable atoms.

For `BEp`, a locally bounded conditional `L^(p/(p-1))` tail bound is a sufficient certificate by Holder's inequality. The source's deterministic-time example on pp. 9--11 shows that convergence of realised p-variation neither forces convergence of predictable p-energy nor uniform integrability of that realised variation. Do not replace the four conditions by an unqualified projection or ucp claim.

The proof’s reusable interfaces are threshold-separated jump alignment on pp. 62--64 and the split of the compensator-atom difference into fixed-compensator integrand and changing-compensator terms on pp. 70--71. The rest of the tail/localization proof must be checked for the target process.

Source checked from the local 84-page arXiv:2605.11783v3 PDF. This is a preprint-specific theorem contract.
