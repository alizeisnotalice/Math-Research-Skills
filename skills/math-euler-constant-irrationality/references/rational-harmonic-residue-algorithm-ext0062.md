# Rational harmonic Euler sums by finite residues (EXT-0062)

Verified source: arXiv:2604.02384v1 (dated 2026-04-01 in the local PDF), local SHA-256 `d62d00c9b89110ddc21423e8e427f9d3f517cd2676dbb0f8ac2413c3d5fc62a7`, 23 physical pages. This is a preprint; the proof dependency is retained below.

Physical p.3, Proposition 1: if a rational `R(z)` is `O(z^-2)` at infinity and has no integer poles other than possibly zero, then

`sum_{k>=1} R(k) H_k = (1/2) sum_{alpha pole of R} Res_{s=alpha}[R'(s)(psi(-s)+gamma)-R(s)(psi(-s)+gamma)^2]`.

Physical p.4's `HarmonicSum` procedure first reduces `P/Q`, square-free-factorizes `Q`, makes local Taylor/Laurent expansions at algebraic poles, extracts each residue, sums conjugates, and returns the finite total. Its actual proof step is the combination of the two residue summation identities quoted from reference [12], equations (2-6) and (2-9); the source explicitly cancels the possible zero-pole residue. Physical p.6, Theorem 1 supplies the simple-pole partial-fraction specialization `T(t,1)` under `sum C_j=0`.

Use this as a special-function evaluation tool, not an irrationality proof: after exact residue computation, any conversion of digamma/polygamma terms to zeta values, logarithms, or Euler's constant requires separate identities.
