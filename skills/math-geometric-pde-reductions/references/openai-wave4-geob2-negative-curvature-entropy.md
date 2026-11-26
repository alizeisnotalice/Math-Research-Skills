# Entropy equality: formal-to-smooth Anosov interface

Source: *Entropy equality and local symmetry in negative curvature*, OpenAI
(23 September 2026), SHA-256
`8658ab8209a8aa0c0f472b6793ecb738a30ffeec74821915e82d08a185b0ca97`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/paper.pdf).

## Scoped interface

This records the paper's final rigidity interface.  Its theorem applies to a
closed connected smooth Riemannian manifold of dimension at least three with
strictly negative sectional curvature: normalized Liouville measure has
maximal entropy for the unit-speed geodesic flow iff the metric is locally
symmetric.  The reference is not a numerical entropy test and does not
replace the source's constructions of affine families, holonomies, or formal
crossings.

The coefficientwise conversion used at physical p. 60 is

\[
 \sum_{k\geq0}q_k(P_{s_0,r}(t),r)[t^k]=q_0(s_0,r). \tag{8.5}
\]

At degree `l`, the only term involving `q_l` is
`q_l(s_0,r)[t^l]`; all other terms involve lower `q_k`, their `s` derivatives
of order at most `l-k`, and polynomially controlled derivatives of `P`.
Thus use induction only when the source's uniform graph-derivative bounds and
formal crossing inversion hypotheses are present.

## Transfer sequence

1. Start with the finite alternative and actual graph identity (8.2), not a
   merely formal splitting.
2. Apply the degree induction from (8.5), then polarization, to obtain the
   needed smoothness of the transverse data.
3. Use Theorem 8.8 (physical p. 62): on the universal-cover direction sphere,
   the restriction of `q` is weak-unstable holonomy followed by a smooth
   transverse coordinate map.  Its local-homeomorphism and lower-derivative
   inputs yield smooth actual `E^u` and `E^s`.
4. For the remaining time-change correction, verify that all periods of the
   one-form `beta` vanish.  The source then writes `beta=db` and uses the
   orbit shift `x mapsto phi_0^{b(x)/a_0(x)}(x)` (physical p. 63) to remove
   the exact correction before the final Benoist--Foulon--Labourie implication.

## Record boundary

Each item above is conditional on the source's entropy-equality hypotheses,
the finite alternative, and the cited rigidity theorem.  Do not use it to
claim local symmetry from a finite collection of periodic-orbit data.

Locators: physical pp. 1--3, 60, 62--63; (8.5) and Theorem 8.8.
