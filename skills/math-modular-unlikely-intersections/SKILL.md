---
name: math-modular-unlikely-intersections
description: Route a specified modular-curve or abelian-family unlikely-intersection problem through the available degeneration, height, Galois-orbit and conditional Lang--Trotter theorems.
---

# Modular unlikely intersections

Use this skill only after the caller supplies the algebraic family, base field,
curve, non-special or Hodge-generic condition, boundary degeneration and the
precise special points or subvarieties. Select one source theorem whose exact
moduli space and conclusion match the data.

- For an irreducible non-special curve in \(Y(1)^n\) defined over \(\mathbb Q\) and meeting \((\infty,\ldots,\infty)\), use the
  multiplicative-degeneration route.
- For a Hodge-generic curve in \(\mathcal A_g\), use the PEL large-Galois-
  orbit route only with its endomorphism and degeneration hypotheses.
- For a one-parameter principally polarized abelian-surface family, use the
  local \(v\)-adic G-function relation and height route after checking good
  reduction and the stated distinguished point.
- For effective class-number bounds on selected \(Y(1)^n\) curves, verify the
  smooth boundary model and the source's Binyamini input.
- For \(Y(1)^3\), distinguish a boundary strongly-special intersection from
  the separate supersingular-reduction branch.
- The Lang--Trotter route is conditional and must name the assumed pairwise
  conjecture.

The theorems are not numerical G-function certificates and do not yield a
route to Euler's constant. Read the relevant source notes before stating a
finiteness or height conclusion.

## Source routes

- [Multiplicative degeneration in \(Y(1)^n\)](references/ext0234-zilber-pink-degeneration.md)
- [PEL large Galois orbits](references/ext0236-large-galois-orbits.md)
- [\(v\)-adic G-function relations](references/ext0237-v-adic-gfunctions.md)
- [Effective Brauer--Siegel](references/ext0248-effective-brauer-siegel.md)
- [New \(Y(1)^3\) cases](references/ext0252-zilber-pink-y113.md)
- [Conditional Lang--Trotter case](references/ext0258-lang-trotter-unlikely-intersections.md)
