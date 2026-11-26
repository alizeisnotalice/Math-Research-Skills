# Watermark: conditional Hodge-lattice quotient

## Source and audit

- Rafael Amichis Luengo, *The Watermark in Every Even Dimension*, v2, 1 October 2026, 16 pages; local-source SHA-256 `0b47b0127e542c7aa21b6c457d819674fee4a127cf1f73a921b65382bdf51d8e`.
- Status in the source: author public paper, not refereed. Its own final status table says that Theorems 1, 2, 3(a), and 4 are proved modulo Pham/Looijenga and classical Hodge facts; Theorem 3(b) additionally uses BRR Proposition 2.12.

## Reusable derivation

For an even-dimensional Fermat variety, the source's proof of Theorem 1 starts from the four input certificates listed in the skill. It uses the primitive presentation and the character ideals to identify the relevant orthogonal quotient, then uses the unimodular ambient lattice, primitivity/nondegeneracy, and a standard class of intersection one to lift from primitive to full homology. Its resulting conditional identity is

`Hdg(X)^vee / Hdg(X) ~= Z[G] / (I_B + I_T)`.

The derivation is reusable only when the symbols, annihilators, and integral conventions have been matched to the caller's data. It cannot be used to manufacture any of its four premises.

## Optional arithmetic branch

For odd prime degree `p`, the source prints an exponent formula of the form

`E = 1 + (2k(p - 2) - 1) B - 2 delta_B`.

Its Theorem 3 separates a lower bound from an equality whose general form requires BRR Proposition 2.12. In this review, exact integer evaluation gives `E = 9, 25, 81` for the displayed formula at `(k,p) = (1,5), (1,7), (2,5)` respectively. These are arithmetic checks only; they do not verify the geometric inputs or the source's Hodge-theoretic interpretation.

## Dependencies retained

- Pham/Looijenga for the homology model;
- Shioda/Ran and the cited Hodge-character material for the character ideals;
- Degtyarev–Shimada where the source invokes its corollary;
- BRR Proposition 2.12 for the stated all-prime equality branch.
