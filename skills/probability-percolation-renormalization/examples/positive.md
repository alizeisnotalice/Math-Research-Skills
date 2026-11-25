# Positive examples

These examples use the exact source scopes in [the source register](../references/sources.md); each identifies whether the claim is direct or derived.

## Supercritical chemical distance: joint event

For nearest-neighbour iid bond percolation on Z^d, fixed d≥2 and p>p_c(d), Antal–Pisztora Theorem 1.1 (physical PDF p.3, printed p.1037, Eq. (1.3)) supplies ρ=ρ(p,d)≥1 such that

    limsup_{|y|₁→∞} |y|₁⁻¹ log P(0↔y, D(0,y)>ρ|y|₁) < 0.

This is a joint-event tail. Its proof needs the source blocks R_i(N) AND S_i(N), conditional domination, bad-cluster repair, and exponential cluster-mass moments. It is not directly a conditional estimate. For the same iid model, FKG and uniqueness yield P(0↔y)≥θ(p,d)^2; dividing by this positive lower bound gives a conditional corollary with a changed prefactor. That last implication is derived, not the verbatim theorem. No dependent-model or other-geometry transfer follows.

## Finite-set Bernoulli sharpness criterion

For nearest-neighbour iid bond percolation on Z^d, use the accepted Duminil-Copin–Tassion finite-set criterion with a finite S containing 0 and its precise cut-edge functional. If one such S has φ_p(S)<1, the reviewed finite-set criterion gives the subcritical contraction in its stated model. A single finite numerical check in another graph is not a replacement for the all-hypotheses theorem. The source row isolates the final inequality and does not rely on the questioned intermediate display.

## Explicit product positive association

For finitely many independent Bernoulli coordinates and increasing events A,B, Kesten Chapter 4 Proposition 4.1 gives P(A∩B)≥P(A)P(B). For example, if A={X₁=1} and B={X₁=1 or X₂=1}, then the product-law inequality follows by coordinate conditioning. The theorem is for a product law; the dependent counterexample in the negative cases shows why matching marginals is insufficient.

## Synchronous closure versus an ordered schedule

For the K₃ edge-bootstrap rule on P₄, simultaneous rounds have edge-count trajectory 3→5→6, so closure takes two rounds. A complete legal sequential schedule can use three edge additions. Both facts are valid but measure different clocks. The reviewed graph-bootstrap sources retain this distinction in their exact scope.

## Finite computation archive

The included exact computations enumerate small graph/seed instances and test finite algebraic identities. They are reproducibility checks only; the source proofs establish the general statements.
