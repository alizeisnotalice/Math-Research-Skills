# Finite-cell thermodynamic interface

For the draft's radial pair-potential class, retain the exact assumptions:
the stated stable core inequality, common attraction-mass bound, and compact
thermodynamic parameter set.  Under those inputs, the source provides a
canonical/free-energy and grand-canonical pressure interface:

`H_phi(beta,d) = -lim log Z_{L,n}(beta)/(t L^3)` along `n/L^3 -> d`,
with `Q_phi(beta,h)=sup_{d>=0}(h d-H_phi(beta,d))`, and the reverse
Legendre formula recorded in the source.

The entry is only for a caller that independently verifies the potential-class
constants and normalization.  It does not assert a continuum phase
singularity, Kac-range limit, or nonanalyticity.

Source: *A continuum temperature singularity for a radial pair potential*,
SHA-256 `d3c00f7387c84c306cde835b975962752138b0aca201fce5b8d5fc2a2021b0c4`,
physical pp. 7--12, especially Proposition 2.3; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/paper.pdf).
