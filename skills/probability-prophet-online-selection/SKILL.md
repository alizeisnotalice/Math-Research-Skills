---
name: probability-prophet-online-selection
description: Analyze prophet inequalities, thresholds, online allocation, and stochastic matching while preserving the arrival model and benchmark.
---

# Prophet inequalities and online selection

Use this skill when an online policy accepts random rewards or allocates limited resources and its quality is compared with an offline prophet, an ex-ante or flow LP, or an online dynamic benchmark.

## State the model before selecting a result

Record the following data in the claim or calculation.

- Independence, distribution knowledge, and whether values have atoms.
- Arrival order and who chooses it. Distinguish fixed, random-permutation, value-aware adversarial, and policy-adaptive orders.
- Capacity, feasibility family, irrevocability, and whether a policy is static or adaptive.
- Comparator and denominator. Expected offline top-k value, online dynamic value, ex-ante LP, and long-run reward rate are distinct.
- Tie convention. For threshold arguments, state strict or weak exceedance and any independent randomization at atoms.

Read [method notes](references/method.md) for a theorem-specific transfer and [source status](references/sources.md) to locate the corresponding source. The source records preserve their own versions and scope. A source count or historical reading status is not a mathematical guarantee.

## Route by task

- For IID finite-n ratios, limits, and additive gaps, read the A001, A002, and A005 sections of [method notes](references/method.md). Keep a fixed-law limit separate from an infimum over laws varying with n.
- For threshold demand and stockout calculations, first define the effective Bernoulli indicators and capacity. A Poisson-binomial PGF or tail estimate is finite risk evidence. It does not supply a prophet ratio.
- For the reviewed M0055, M0058, M0067, or M0072 interfaces, read the [preserved narrow use gates](references/method.md#preserved-narrow-use-gates-from-the-historical-review) before combining a threshold, copy, Bernoulli, or submodular argument.
- For OCRS, matching, or resource allocation, use the online-allocation sections of [method notes](references/method.md). Keep the feasibility family, batch model, correlation assumptions, and adversary model with the conclusion.
- For static anonymous prices in a finite subadditive combinatorial auction, use the supplied certificate checker described in [the Cogentic LP card](references/cogentic-subadditive-static-price-lp-certificate.md). It verifies a supplied rational price, distribution, and all subset inequalities. It does not construct a price or prove the asymptotic welfare ratio.

## Boundaries

Do not interchange IID, independent non-identical, random order, or adversarial order. A threshold count, LP feasibility certificate, finite numerical search, or distribution-specific calculation does not establish an online reward ratio without a policy theorem in the same model. For matching and OCRS, specify the resource state and the exact selectability or welfare conclusion.

For a formally published result, verify the cited edition and statement. For a preprint, verify the version, relevant proof route, and assumptions before applying it. Central archive material is described in [evidence and local attachments](../math-research/references/evidence.md).
