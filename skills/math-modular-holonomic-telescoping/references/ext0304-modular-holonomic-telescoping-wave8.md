# Meromorphic-modular creative telescoping (EXT-0304)

Source: [Kam Cheong Au, *Holonomic Sequences Arising from Meromorphic Modular
Forms*, arXiv:2610.17240v1](https://arxiv.org/abs/2610.17240v1), physical
pp. 27--31: Proposition 5.1, proof of Theorem 1.2, Lemma 5.2, and the two
algorithms in §5.2. Source byte SHA-256:
`1e4c1c53dcf36aa229904832debaf88de8ba438d8801b5ad46453f6ba21cc73e`.

## Scoped reference

This is an algorithmic transfer only for supplied meromorphic modular data:
a group `Γ`, support set `S`, nonconstant weight-zero `t` whose divisor is
supported on `S`, weight `k>=2`, and exact q-expansion access to the required
spaces `L_k(D)`.  It does **not** provide q-expansion integrality, a modular
parametrization, nonvanishing of a resulting linear form, or an irrationality
criterion.

## Source-derived procedure

1. For a divisor `D` supported on `S`, Proposition 5.1 proves that
   \(D^{k-1}(t^n h)/t^n\) lies in a fixed finite-dimensional space and has
   q-coefficients polynomial in `n`: writing `a=Dt/t`, it is
   \((D+na)^{k-1}h\).  The proof appears on pp. 27--28.
2. Theorem 1.2's proof takes enough classes among
   `g,tg,...,t^d g` in the quotient by this image.  Finite-dimensional linear
   dependence gives rational functions `r_j(n)` and a certificate `R_n` with
   \[\sum_j r_j(n)t^jg=D^{k-1}(t^nR_n)/t^n.\]
   Consequently \(L=\sum_jr_j(n)S_n^j\) annihilates the extracted sequence.
   This is pp. 28--29; it relies on the stated Bol identity and
   Riemann--Roch dimension calculation.
3. To compute rather than merely assert that relation, Lemma 5.2 gives a
   valence bound `B`: equality of forms in the stated `L_k` space follows
   from matching q-coefficients through `q^B`.  Use the five-step algorithm
   on p. 30: compute bounded q-expansions, a spanning set in `L_{2-k}(D_2)`,
   expand `(D+na)^{k-1}v_i`, and solve the coefficient equations over
   `C(n)`.  Increase `j` as on p. 31 until a relation is found.

## Required output and check

Emit the recurrence coefficients, every divisor and valence bound used, the
truncated q-expansions, and `R_n`. Verify the displayed identity through the
specific bound `B`; only then infer the recurrence for the explicitly defined
sequence. A finite q-check cannot prove any unprovided modular-space basis,
integrality assertion, or asymptotic/irrationality consequence.
