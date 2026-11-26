# Positive-height completion factorization

**Source locus.** Lemma 2.1, PDF p. 4, *Counterexamples to weak chromatic splitting: sphere kernels and descent exponents* (OpenAI Math preprint, pinned commit `3344da59991ed94f9ba711217b29c1d760badfa6`).  Local source SHA-256: `f646b6facb641430247503dbf66178811726f0d0f3080f44e1bb48ac1cc7c2f4`.

## Transfer statement

Fix a prime `p`.  Let `X = S_p^` be the derived p-complete sphere and let `c: S -> X` be its completion map.  For every positive Morava height `a >= 1`, `c` is a `K(a)`-equivalence.  Consequently, if `Y` is a `K(t)`-local spectrum and `1 <= t <= r`, then every map `S -> Y` has a factorization

`S --c--> X --> L_r X --> Y`.

Here the final arrow is an existence assertion in the stable homotopy category.  The statement assumes the standard `K(t)` and Johnson–Wilson `L_r` localizations; it does not assert that a supplied object has the required locality.

## Proof

Taking the homotopy limit of the cofiber sequences for multiplication by `p^j` identifies the fiber `C` of `c` with `F(S[1/p], S)`.  Multiplication by `p` is an equivalence on `S[1/p]`; by contravariance in the first variable it is therefore an equivalence on `C`, and hence on `K(a) smash C`.

On the other hand, `pi_*(K(a) smash C)` is a module over `K(a)_*`, whose coefficient ring has characteristic `p`.  Thus multiplication by `p` is zero on that homotopy group.  An automorphism that is zero forces this group to vanish, so `K(a) smash C` is contractible.  Hence `c` is a `K(a)`-equivalence.

Set `a=t`.  A `K(t)`-equivalence induces an equivalence of mapping spectra into a `K(t)`-local target, so a map `S -> Y` extends across `c`.  If `t <= r`, every `L_r`-acyclic is `K(t)`-acyclic.  Therefore a `K(t)`-local target is `L_r`-local, and its map out of `X` factors through the `L_r`-localization unit `X -> L_r X`.

## Exact algebraic sanity check

The decisive implication above is elementary and does not certify the topological hypotheses: if an abelian group is simultaneously a `Z[1/p]`-module (so multiplication by `p` is bijective) and an `F_p`-vector space (so multiplication by `p` is zero), it is zero.  For example, the only additive group satisfying both structures at `p = 3` is zero: for any `x`, choose `y` with `3y=x`, then `x=3y=0`.  In the transfer proof this calculation is applied to `pi_*(K(a) smash C)` after the independently supplied fiber identification and Morava-K module structure.

## Use boundary

Do not use this lemma to infer that a target is `K(t)`-local, to replace `L_r` by an arbitrary localization, or to claim that a detected class survives.  Those are separate inputs.  In particular, no chromatic-splitting counterexample follows from this factorization alone.
