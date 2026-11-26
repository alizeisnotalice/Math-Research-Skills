# Flow lenses for filtered closed-geodesic Morse data

Source: *Infinitely many closed geodesic images on every Riemannian sphere*,
OpenAI (24 September 2026), SHA-256
`123ee5276415debb732951573b23d8dbe7ee63112ec7246478de53715fe699e2`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf).

## Scoped interface

Use this only in the contradiction branch in which the source assumes a
finite collection of prime geodesic images and has its stated
Palais--Smale/normalized-energy-flow input.  For prime representatives
`c_i` of lengths `ell_i`, its positive critical values are `m ell_i`; there
are `O(1+b)` labels below energy `b` and `O(1+D)` labels in an interval of
width `D` (physical p. 9).  These are source-specific finite-list bounds.

## Procedure

1. In a closed energy band choose invariant critical neighborhoods and a
   complete bounded equivariant strict descending flow.  Lemma 3.6 (physical
   p. 10) is the common-flow `flow lenses` device for local restriction maps;
   its hypotheses include a good pair and the indicated compact-group action.
2. Supply the Palais--Smale drop separation (or the stated finite-polygon
   compactness substitute).  This is what verifies the lens drop hypotheses,
   rather than a formal choice of a gradient-like vector field.
3. Invoke Theorem 3.7 only under finitely many prime images: sufficiently
   tight crossings decompose into unoriented labels `(i,m)`, and the theorem
   gives the paper's uniform local control of their ordinary pairs.
4. In the terminal filtered contradiction, retain only the asserted
   monotonicity under doubling.  On a no-critical interval, the source uses
   `T(x)>=T(x/2^k)` and concludes equality between `x` and `x/2` at the
   selected regular points; it explicitly does not assert monotonicity
   between arbitrary cuts (physical p. 48).

## Record boundary

This is a source-bound filtered-Morse mechanism.  It does not provide a
generic theorem for arbitrary free-loop functionals, nor can finite sampling
verify the Palais--Smale input.

Locators: physical pp. 9--11 and 48; Lemma 3.6 and Theorem 3.7.
