# Bounded-tree obstruction to asymptotic midpoint uniform convexity

**Status:** proposed skill, not installed. The manuscript result is used as given.

**Pinned original:** *Asymptotic midpoint uniform convexity and unbounded diamond distortion in a reflexive tree space*, SHA-256 `1e08111eaf334a068d25387a687d1236aa74d5775890fa2d6f978b7a3bde5d66`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/manuscript.pdf), physical pp. 2, 4, 6, Lemma 3.2 and (3.1).

## Certified input and output

Input a certificate giving every-height weakly-null branching trees `u_s^(h)`, bounds `m<=||u_s^(h)||<=M`, child separation at least `c`, and an equivalent norm comparison `alpha||x||<=N(x)<=beta||x||`. The source conclusion is

`delta_N(alpha*c/(2*beta*M))=0`.

For a proposed positive modulus increment `gamma`, the finite contradiction threshold is the least `h` with

`alpha*m*(1+gamma/2)^h > beta*M`.

Use the exact helper `scripts/tree_diamond_threshold_wave5.py tree` only to compute this arithmetic threshold; it does not certify the infinite tree hypotheses.
