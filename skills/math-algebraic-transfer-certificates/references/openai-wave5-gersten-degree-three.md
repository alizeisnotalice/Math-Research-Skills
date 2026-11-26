# Degree-three ramified Gersten construction

**Status:** proposed skill, not installed. Source conclusions are used as given; no source proof audit was performed.

**Pinned original:** *An integral degree-three Gersten counterexample*, SHA-256 `c411abf2a5b4f0dd47ce13d1d22c79eca53abbcf1097c0b9e195ddf8b7856f7c`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/paper.pdf), physical pp. 3–5 and 8, Lemma 2.1 and Proposition 3.1.

## Required data

Provide the specified ramified regular local ring `S`, divisor/residue fields, a residue class `beta` in `K_2(L;Z/5)`, extension/valuation data, and certified residue, transfer, norm, and finite-field-localization maps. The interface refuses arbitrary rings without those maps.

## Reusable route

The source forms `a_D=beta_D[t]` after `(1-t)^5=zeta`; Steinberg gives `{1-t,t}=0`. Its coefficient exact sequence is the lift gate from the mod-5 class to an integral degree-three class. Build `a_D`; check its supplied residue; invoke the supplied coefficient sequence; use the finite-field vanishing/lift gate; then test the result with the supplied transfer/norm valuation. Report every target and residue degree.
