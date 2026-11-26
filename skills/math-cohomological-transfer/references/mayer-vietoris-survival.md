# Mayer--Vietoris survival lemma

Let `X = Y ∪ Z` be a cover by finite simplicial subcomplexes (equivalently, apply
this to stated subcomplexes of an order complex), let `A = Y ∩ Z`, and let `k` be a
field.  In a fixed degree `n`, if the inclusion-induced map

```text
H~_n(A; k) -> H~_n(Y; k)
```

is zero, then `H~_n(Y; k) -> H~_n(X; k)` is injective.

Indeed the reduced Mayer--Vietoris sequence contains

```text
H~_n(A) --(i_Y*,-i_Z*)--> H~_n(Y) ⊕ H~_n(Z) --> H~_n(X).
```

If `y` maps to zero in `H~_n(X)`, then `(y,0)` is in the image of the left
map.  Its first coordinate is `i_Y*(a)=0`, hence `y=0`.  A genuine chain
nullhomotopy of the inclusion, or a genuine topological nullhomotopy, supplies the
zero-map hypothesis.  A merely informal deformation picture does not.

For finite complexes the condition can instead be certified by exact rational (or
finite-field) linear algebra on chain complexes: present a basis of cycles for
`H~_n(A)` and show each included cycle is a boundary in `Y`.  Degree zero requires
using reduced chains; augmented/empty-complex conventions must be stated when the
source uses them.

If a separately verified equivalence says `Y ≃ B * C`, then over a field

```text
H~_n(B * C; k) ≅ ⨁_{p+q=n-1} H~_p(B; k) ⊗ H~_q(C; k).
```

This is the degree-shifted tensor formula for augmented reduced chains.  It only
produces a nonzero class after the relevant factor groups and the equivalence have
been proved; it does not verify a deleted-bottom product/join claim.

Source locus: OpenAI, *Rational homology and Quillen's conjecture*, pinned
`openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, PDF SHA-256
`62d7903055f1b292b960d3e893a770f3847d3b1b1e171f9124ac770652e06f2b`, pp. 60--61,
especially equation (94).  The lemma above is independently proved from the
Mayer--Vietoris exact sequence; the source's group-theoretic construction and its
poset equivalences are not imported as certified facts.
