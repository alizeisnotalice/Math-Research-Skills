# Exact conditional bridge: additive gluing implies near-one gluing

Source identity: supplied percolation guide SHA-256
`5540fee046a4dfff0247410630aec8d6b42c8f3c074c19e98a3b66f8f9410a75`,
formal-math commit `795efb86f191735c5481675763537cfb4ff37e55`.

This note proves a genuinely complete but conditional component of the formal
route.  It does not prove the new additive-gluing inequality or the conditioned
slack hierarchy.

## Exact source interfaces

At the pinned commit:

* `Statements.lean` defines `AdditiveGluing` as: for every finite weighted
  graph, relay set `A`, vertices `o,b`, and `t >= 0`, if every relay has
  `P(a <-> b) >= 1-t`, then
  `P(o <-> A)-t <= P(o <-> b)`.
* The same file defines `NearOneGluing`: for every `epsilon>0` there is a
  graph-size-independent `delta>0` such that strict hypotheses
  `1-delta < P(o <-> A)` and `1-delta < P(a <-> b)` for every relay imply
  `1-epsilon < P(o <-> b)`.
* `AdditiveGluing/Suffices.lean`, lines 19--25, is the intended Lean theorem
  `additiveGluingSuffices_proof`.  Its source SHA-256 is
  `9b2d4cf3d2f39030a3f8df95e4b0facfc1f21566091cafa85c35d4a9cfbe901b`.

The central quantifier distinction is preserved: the additive statement has a
weak `>=` relay hypothesis and conclusion, whereas the near-one statement has
strict `>` hypotheses and conclusion.

## Proof

Assume `AdditiveGluing`.  Let `epsilon>0` and choose `delta=epsilon/2`.
Then `delta>0`.  Fix arbitrary `n,w,A,o,b`, and suppose

```
1-delta < P(o <-> A),
1-delta < P(a <-> b) for every a in A.
```

The second strict inequality implies the weak hypothesis required by
`AdditiveGluing` with `t=delta`; hence

```
P(o <-> A) - delta <= P(o <-> b).
```

Subtracting `delta` from the first strict inequality gives

```
1-epsilon = 1-delta-delta < P(o <-> A)-delta.
```

Transitivity proves `1-epsilon < P(o <-> b)`.  This establishes the exact
`NearOneGluing` interface with a `delta` independent of the graph and relay
set.  No measure-theory, CSH, or limit argument is used in this bridge.

The local exact-rational regression

```sh
python3 -B scripts/verify_additive_gluing_transfer.py
```

checks the scalar direction on 2,592 rational instances and verifies the
boundary failure if `P(o <-> A)` is weakened from strict to equality.  It is a
sign/strictness guard only; the displayed symbolic proof, not the finite test,
establishes the universally quantified bridge.

## What remains

The indispensable unproved component is
`CSH.additiveGluing_holds`, with the source path
`CSH.cshAll -> additiveGluing_of_csh -> additiveGluing_holds`.  It contains
the new conditioned-slack hierarchy and cannot be replaced by this scalar
bridge.  Downstream, `NearOneGluing` is connected to the Kozma--Nitzan
conditional Theorem 6 from the 2024 arXiv preprint; this note makes no claim about that
renormalisation, the lattice theorem, or the Lean kernel status.
