---
name: math-holomorphic-local-to-global-transfer
description: Transfer specified holomorphic local data to descent, gluing, integrability, or universal-cover product conclusions only after the matching geometric gate has been established. Not for arbitrary local charts or holomorphic distributions.
---

# Holomorphic local-to-global transfer

Choose the narrow route that matches the supplied data.  Do not combine their conclusions: a finite-cover descent is not spray gluing, bracket annihilation is not global product continuation, and local product charts do not remove monodromy.

## Finite-cover trace descent

Use this route only for a finite surjection from a smooth complex source to a normal connected target.  Define trace using local generic degrees and rational coefficients.  Check that trace after constant-section inclusion is multiplication by the degree before using the direct-summand statement or proper-base-change transfer of local rational-homology concentration.  A construction of the cover is separate from this transfer.

## Buffered spray gluing

Use this route only when holomorphic sprays and their transition `id+c` are already supplied on buffered overlap geometry.  Record the fibre radius, base/fibre margin `h`, the split loss, and a smallness budget for `||c||`.  The Cousin split costs a factor of the form `C h^{-p}`, and the nonlinear correction is useful only when the resulting quadratic error fits the remaining margins.  This route does not construct sprays, a separated cover, or a small transition.

## Holomorphic-distribution integrability

For a specified splitting `TX=E_1\oplus E_2`, use a tangent-box argument only after the supplied holomorphic curves, factor-direction transport, marked-point vanishing/spanning data, and rational-connectedness extension are available.  The conclusion is the vanishing of the relevant bracket tensor; it is not automatic from a pointwise splitting or from formal local coordinates.

## Universal-cover product continuation

Use this route only after complementary holomorphic subbundles are integrable, local product boxes have compatible blockwise transitions, and their mutually inverse germs can be continued along the required paths.  On the ordinary simply connected covers, apply monodromy continuation and then the identity theorem to the wrong-factor differentials.  Keep compact Kähler and cover hypotheses explicit.  Finite local product charts alone do not yield a global product.

For the exact hypotheses, constants, and source-specific constructions, read the corresponding finite-cover, spray, distribution, and continuation references before applying a route.

## OpenAI 原稿中的方法

- [Buffered holomorphic-spray gluing](references/buffered-spray-contraction-wave5.md)
- [Finite smooth-cover trace descent](references/finite-smooth-cover-trace-descent-wave5.md)
- [Product-chart monodromy continuation](references/product-chart-monodromy-continuation-wave5.md)
- [Tangent boxes and rational-curve bracket annihilation](references/tangent-box-bracket-annihilation-wave5.md)
