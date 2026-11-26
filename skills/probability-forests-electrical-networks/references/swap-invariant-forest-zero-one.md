# Swap-invariant events in free and wired spanning forests

Use this component for a zero--one conclusion about an event of a free spanning forest (FSF) or wired spanning forest (WSF) that is invariant under one valid edge swap.  It does not apply to arbitrary determinantal measures or to an event that is merely invariant under relabelling.

## Conditional one-edge transfer

Let `G` be a connected, locally finite network with positive conductances, let `mu` be its FSF or WSF law, and let `e` satisfy `0 < mu(e in F) < 1`.  If the event `A` is unchanged whenever two spanning forests differ by one deletion and one insertion, then

```
mu(A | e in F) = mu(A | e not in F) = mu(A).
```

The same equality is available after conditioning on finitely many already revealed edge states, provided that conditioning is consistent and the next edge has nontrivial conditional inclusion probability.  Revealing a countable edge enumeration and applying martingale convergence then gives `mu(A) in {0,1}` for a globally swap-invariant event.

## Required representation premise

The source proof is conditional on two imported projection-determinantal facts: the appropriate FSF/WSF projection representation and the nested codimension-one coupling of the contraction and deletion laws.  Check those premises for the chosen boundary condition rather than treating a finite UST calculation as an infinite-network proof.

For WSF, deletion can disconnect the graph.  The relevant deletion law is the independent union of WSFs of the components, with block-diagonal projection kernel; this is compatible with the common-boundary wired finite approximation.  Do not replace this by a connected-graph argument.

## Boundaries

This result does not establish the projection representation, the contraction/deletion identities, or any claim for general determinantal processes.  It also does not show that component-count, end-count, or another proposed event is swap-invariant; verify that property directly.

## Provenance

- S. Beringer and R. Lyons, *A zero-one law for swap-invariant events in uniform spanning forests*, arXiv:2610.00938v2 (2026), Lemma 2.5, Remark 2.6, Corollary 2.7, and Remark 2.8, physical pp. 4--5; the martingale conclusion is on p. 5.
- The assigned local source was v1.  The v2 primary version was compared for the WSF argument: it explicitly supplies the projected-star quotient and the disconnected-deletion/block-diagonal step on p. 5.
- Primary record: <https://arxiv.org/abs/2610.00938>.
