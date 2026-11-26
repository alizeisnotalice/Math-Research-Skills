# CAT(0) cube-grid bound to thin triangles

**Source.** OpenAI, *Nonhomeomorphic closed aspherical four-manifolds with the same homotopy type*, Lemma 6.3 and Proposition 6.4, PDF pp. 24--25; SHA-256 `4d578110a4422046846d608ea43b06b9d2a68a4b6a76abadc5f60e637f623cec`.

## Input contract

Let `Y` be a CAT(0) cube complex.  Supply an integer `K>=0` such that every isometrically embedded square grid in its edge graph has side length at most `K`.  Work with the unit-edge graph metric and vertex geodesic triangles.

## Reuse

For `v,v'` in the interval `I(x,y)` at equal distance from `x`, use hyperplane-separation sets and medians to construct an isometric `n` by `n` grid, where `2n=d(v,v')`.  The grid hypothesis gives `d(v,v')<=2K`.  Consequently every edge-geodesic triangle is `4K`-thin at vertices.

This is a CAT(0) cube-complex lemma, distinct from the barycenter-energy mode of this skill.  It does not give a grid bound from local combinatorics; in the source that input is separately obtained before invoking Lemma 6.3.

## 固定来源

- 物理页 24, 25。Lemma 6.3; Proposition 6.4 SHA-256 `4d578110a4422046846d608ea43b06b9d2a68a4b6a76abadc5f60e637f623cec`。[Nonhomeomorphic closed aspherical four-manifolds with the same homotopy type](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf)
