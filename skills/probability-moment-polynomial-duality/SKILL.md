---
name: probability-moment-polynomial-duality
description: Build finite-support probability bounds for Boolean k-wise laws, event/count moment data, and degree-bounded polynomial duals. Use when the support and full constrained marginal or moment map can be stated; route Fourier and invariance proofs to the existing Boolean skill, and treat tensor/tree recursion as uncovered here.
---

# Finite moments and polynomial duality

Use this skill when a probability question has a finite support or explicit finite moment model and the goal is a sharp event bound, a one-sided polynomial certificate, or a justified k-wise Boolean reduction.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Choose the route

- For labeled Boolean k-wise laws, keep one constraint for every coordinate subset through the independence order, then use the finite cube LP and its degree-bounded dual.
- For exchangeable one-block all-ones events, reduce to the integer count grid only after proving symmetry; use named Krawtchouk or adjacent-pair results only under their exact parity and parameter conditions.
- For partitioned event counts, keep the entire supplied mixed-moment vector. A count-grid result is exact for the Boolean model only after a separate within-block symmetrization and lift proof.
- For partial union summaries, use the source-specific finite LP or inclusion-exclusion certificate that matches the available data. It does not recover missing intersections or general k-wise marginals.
- For arbitrary dependence with specified discrete marginals, use the full finite atom LP and require pointwise dual inequalities on every atom.
- For bounded factors under limited independence, use the reviewed product-approximation or tail interface only as an auxiliary error bound. It is not an exact factorization or an LP sandwich.
- For tensor moments with tree-shaped message recursion or multilevel error propagation, report that this skill has no admitted G13.05/G13.06 method. Do not substitute the Gopalan–Yehudayoff approximation result.
- For Fourier, influence, invariance, PTF, or coefficient-sparsity claims, hand off to probability-boolean-fourier-invariance. For additive-support and inverse Littlewood–Offord questions, route outside unless a proved finite Boolean model bridge is supplied.

## Core workflow

1. State the finite support, reference law, unknown joint law, event/objective, and every supplied moment or marginal constraint.
2. Write the full primal mass LP. For k-wise Bernoulli(p) bits, include the all-one moment for every subset S with |S| at most k; inclusion-exclusion then fixes each pattern on S. Never replace these rows with moments of the total count alone.
3. Write the matching dual on the same support. A pointwise majorant bounds a maximized event probability above; a pointwise minorant bounds it below. Check every support point, including the origin and complement atoms.
4. Reduce to counts only when the objective and constraints share the stated symmetry. For multiple blocks retain every mixed falling-factorial constraint and prove the labeled lift before claiming an exact Boolean result.
5. Keep each theorem's support, parity, order, constants, and boundary case with the formula. Distinguish exact results from continuous relaxations, asymptotic estimates, reviewer-derived calculations, and finite computations.
6. Route questions by the selection table in the method reference; use the source ledger and its R07 scoped-use index to find admitted source conditions.

## Status

The current R07 exports contain 30 source-scoped accepted uses with 30 source IDs and 30 work-family IDs distinct within this L07 admission set. Root-wide identity/version reconciliation and quota export remain pending. G13.05 and G13.06 have no admitted source coverage. Individual use acceptance is not whole-skill release approval.

See the positive and negative examples for exact certificates and failure cases.

## 偶阶计数矩的成对支持反射

给定内点有理参数及相邻成对支持时，用[偶阶反射](references/even-count-moment-reflection.md)解两侧矩方程，核对精确反射乘子及每个整数计数点上的对偶可行性。
