---
name: math-cat0-inductive-barycenters
description: Transfer a finite centred distribution in a complete CAT(0) metric cone into an inductive-barycenter energy bound, with exact Euclidean finite-support replay. Use for certified cone geometry, not generic group-action or sampling claims.
---

# CAT(0) inductive barycenters

Use this method when a finite distribution on a **complete CAT(0) metric cone** has a certified barycenter at the cone vertex. If its second radial moment is `sigma2`, independent draws `V_1,...,V_t` and the recursive geodesic mean

`m_1=V_1`, `m_j=[m_(j-1),V_j]_(1/j)`

satisfy `E ||m_t||^2 <= sigma2/t`. This converts a conditional test into a square-root mean-energy bound without replacing cone geometry by vector addition.

1. Supply the finite support, weights, a cone/barycenter certificate, and `sigma2=E||V||^2`. A zero arithmetic average only certifies the barycenter in a Euclidean specialization; it is not a general CAT(0) certificate.
2. Keep the draws independent. Conditional or coupled leaves require a separate comparison error before this bound is applied.
3. For any fixed `h`, geodesic concavity gives `(1/t) sum_j <h,V_j> <= <h,m_t>`; combine it with Cauchy--Schwarz only after recording the norm bound for `h`.
4. Run `scripts/euclidean_inductive_barycenter.py` only as an exact finite-dimensional Euclidean replay. It rejects nonzero arithmetic barycenter and is not a verifier for arbitrary CAT(0) input.

See [the proof and source boundary](references/inductive-barycenter-energy.md).

## OpenAI 原稿中的方法

- [CAT(0) finite four-point diagnostic from an Artin-action obstruction](references/openai-wave5-artin-cat0.md)

- [CAT(0) cube-grid bound to thin triangles](references/wave4-geoa3-grid-thinness.md)
