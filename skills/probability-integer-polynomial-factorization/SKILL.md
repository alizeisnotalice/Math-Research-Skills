---
name: probability-integer-polynomial-factorization
description: Analyze finite-support integer convolution through probability-generating polynomials, monic nonnegative-real factors, and exact bounded algebraic certificates; preserve support gaps and coefficient-domain assumptions.
---

# Integer convolution and 0–1 polynomial factors

Use this skill when independent finitely supported integer-valued random variables have a sum that is uniform on its support, or when a finite 0–1 polynomial is factored into nonnegative-real polynomials.

First translate each support by its minimum; gaps remain allowed. For independent `X,Y` with PGFs `P_X,P_Y`, if `X+Y` is uniform on its support `S`, then

`P_X(z)P_Y(z) = |S|^{-1} F(z)`, where `F(z)=Σ_{s∈S}z^s` is a 0–1 mask polynomial.

Equivalently, `F=A B` for monic polynomials `A,B` with nonnegative real coefficients. The arbitrary raw probability factors are not themselves monic. Given `F=G H`, with positive leading coefficients, set `A=G/lc(G)` and `B=lc(G)H`. This reciprocal positive scaling preserves the product and makes both factors monic.

If the target has a zero constant term, first factor off its maximal monomial `z^r` and allocate the corresponding valuations of the two factors; apply constant-term arguments to the remaining mask, whose constant term is 1. For monic nonnegative `A,B` with `F(0)=1`, the coefficient of `z^{deg A}` bounds `B(0)≤1`, and the coefficient of `z^{deg B}` bounds `A(0)≤1`; since `A(0)B(0)=1`, both equal 1. Then the coefficient of `z^i` in `F` is at least `A_i B(0)=A_i`, and likewise at least `B_i`, so each factor coefficient is in `[0,1]`. This is a derived normalization bound. It does **not** imply factor coefficients are integers or are 0–1.

The general question whether every such real nonnegative factor of a 0–1 mask must itself be 0–1 remains unresolved in this scope. Theorem 4 of Hasanbegović gives a conditional result for a separated two-block family, after monic normalization and excluding the overlapping `v=w=1,n=0` case. Do not extend it to arbitrary masks with gaps.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## Method routes

- Translate convolution into PGF multiplication and preserve the full support mask.
- Write diagonal coefficient equations exactly. A finite recurrence, `0/1/*` propagation, Gröbner basis, or real quantifier elimination certifies only its encoded degree and factor-shape bounds.
- Use cyclotomic, root-geometry, integer-monoid, and tiling results only after independently proving their coefficient-field, monicity, root, divisibility, group-law, and no-wrap hypotheses.
- Track factor coefficients as nonnegative reals unless a theorem proves integrality. A signed epsilon-factor construction is outside this model.

See [method notes](references/method.md), [source status](references/sources.md), the [gapped-support positive example](examples/positive.md), and the [raw-scaling and signed-factor counterexample](examples/negative.md).

**Evidence status:** 33 distinct work families have complete prior reading evidence and R14 high scoped-use acceptance, including the R03 closure for EXT003. The general convolution problem remains open within the recorded scope. Current approval conditions are in the source index; original reading records are retained as provenance.
## Inputs and required output

Request the two finite supports, exact coefficient field, normalization, degree bounds and the specific target claim. Return the exact PGF or polynomial reduction, the selected method with a cited source locator, all verified hypotheses, the certificate or proof, and any remaining transfer condition. A finite enumeration or solver result must state its encoded domain.

The optional finite-check script requires Python 3 with SymPy 1.14.0; use an existing local mathematical environment.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
