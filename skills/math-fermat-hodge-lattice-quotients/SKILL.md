---
name: math-fermat-hodge-lattice-quotients
description: Reduce a certified Fermat middle-Hodge lattice quotient to an explicit group-ring quotient, while preserving the geometric and arithmetic premises needed for the reduction.
---

# Fermat Hodge-lattice quotients

Use this skill when a problem already supplies, or asks to audit, the homology-to-group-ring and Hodge-character identifications for an even-dimensional Fermat variety. It is a conditional reduction tool; it does not establish Pham's homology theorem, Hodge-type classifications, or an integral Hodge conjecture.

## Required input certificate

Before using the quotient identity, record the exact Fermat variety `X`, degree `m >= 3`, even dimension `2k`, group `G`, coefficient ring, and conventions for the character subsets. Require all of the following in the form actually used:

1. a marked/primitive homology presentation `H^circ ~= Z[G]/I_A` and the map relating it to `H`;
2. character-ideal identifications `Hdg^circ = I_T e` and `T(X) = I_B e` (including the chosen idempotent or augmentation convention);
3. a unimodular ambient lattice `H`, with `Hdg(X)` primitive and nondegenerate; and
4. the standard class or complementary summand used to pass between primitive and full homology.

With those caller-certified premises and compatible conventions, the displayed algebraic reduction gives

`Hdg(X)^vee / Hdg(X) ~= Z[G] / (I_B + I_T)`.

Keep this as a conditional conclusion: the cited source derives it from the four inputs but sources those inputs to Pham/Looijenga and classical Hodge calculations. Read [the lattice-quotient source card](references/watermark-lattice-quotient.md) before applying it.

## Algebraic matching quotient

For an independently specified group ring `R`, use the Chaise Longue result only after checking that the supplied generators `psi_J`, the *full* matching family `J`, and the count `Q_k(m)` match its definitions. The source claims the following algebraic statement:

`R / (psi_J : J in J)` is free abelian of rank `m^(2k+1) - Q_k(m)`

for `m >= 3`, `k >= 1`. Once that exact statement has been supplied as a premise, deductions within its stated group-ring type are conditional algebraic consequences. It is not a substitute for a replayed Lean build or the geometric comparison theorem. Read [the algebraic-quotient source card](references/chaise-longue-algebraic-quotient.md) for its exact boundary.

## Audit output

State separately:

- which hypotheses were directly checked, cited, or merely assumed;
- whether a conclusion is an algebraic quotient identity, a computed discriminant exponent, or a geometric statement; and
- any retained external dependency (in particular Pham/Looijenga, Hodge-character work, Degtyarev–Shimada, or BRR).

For an optional odd-prime discriminant exponent, use only the exact character data and hypotheses from the source. Arithmetic evaluation of its formula is a consistency check, not evidence that the lattice hypotheses hold.
