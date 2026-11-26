# Integral coefficient K-theory transfer obstruction

**Status:** proposed skill, not installed. This is a theorem-use interface, not a verification of the manuscript proof.

**Pinned original:** *An integral counterexample to Gersten's conjecture*, SHA-256 `c2fa194c832cce8cadb81dd45dfc1910bd385a1aa6456cdcac48315edbe04d61`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf), physical pp. 4–6, Lemmas 2.1–2.3.

## Input contract

Supply a scheme/ring localization diagram, a coefficient prime `ell=5`, and certificates for the coefficient exact sequence, product compatibility with localization triangles, finite-transfer/flat-base-change compatibility, and strong convergence of the displayed motivic spectral sequence. Do not infer these merely from a Bott class.

## Portable calculation

For each field `H`, the source records

`0 -> K_i(H)/5 -> K_i(H;5) -> K_{i-1}(H)[5] -> 0`,

with `K_1(H;5)=H*/H*^5` and `K_0(H;5)=Z/5`; under its convergence condition,

`E_2^{p,q}=H^{p-q}(H,Z/5(-q)) => K_{-p-q}(H;5)`.

Procedure: instantiate the coefficient sequence; record each localization term; apply products only with certified projection/base-change rules; use the spectral sequence only after its convergence and bidegrees are checked; then state the nonzero class with its integral versus mod-5 target. Missing certificate = stop condition.
