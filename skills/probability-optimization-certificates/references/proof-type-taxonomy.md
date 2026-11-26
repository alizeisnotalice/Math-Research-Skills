# Proof-type taxonomy for probability certificates

Use this page to select the proof object before selecting a solver, checker, or theorem. It is a routing aid, not a theorem that transfers a certificate between types.

| Type | Proof object and required output | Owning skill |
| --- | --- | --- |
| A | A supplied finite rational/interval residual, primal-dual LP or cone witness, or exhaustive finite arithmetic check. State exact data or actual outward rounding and the bound direction. | [L03](../../math-l03-rational-and-interval-certificates/SKILL.md) |
| B | A quadratic or rank-one model, its PSD/Shor lift, inclusion direction, and (if claimed) a rank/exactness proof. | [C01](../../math-c01-semidefinite-lifting/SKILL.md) |
| C | An unknown probability measure with support/structural class, generalized moments, conditional-event denominator, and measure-level duality or attainment question. | [B03](../../math-b03-generalized-moments/SKILL.md) |
| D | A fully finite Boolean/count/marginal law with the complete constrained map and pointwise atom/grid polynomial dual inequality. | [Finite moment duality](../../probability-moment-polynomial-duality/SKILL.md) |
| E | A finite probability encoding plus an explicit statement of what remains to transfer back to the stochastic, infinite, asymptotic, or online model. | This skill |

Polynomial SOS or moment-hierarchy certificates are a separate proof object; route their degree, compactness/Archimedean assumptions, Gram identity, and relaxation order to [moment-SOS certificates](../../math-c03-moment-sos-certificates/SKILL.md).

## Handoff rules

1. Keep the original finite encoding beside every delegated certificate. A type-A arithmetic check validates that encoded witness, not the choice of model.
2. A type-B relaxation bound needs its inclusion direction; a type-C or type-D dual needs its own primal/support and moment hypotheses. Do not use one type's strong-duality or exactness conditions for another.
3. Assemble the final probability proof only after recording the finite conclusion and the remaining model/limit/selection/attainment gap. If that transfer is absent, report the finite certificate alone.
