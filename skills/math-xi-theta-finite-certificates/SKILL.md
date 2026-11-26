---
name: math-xi-theta-finite-certificates
description: Audit finite Xi/theta positivity components from supplied moment envelopes and exact polynomial inequalities; do not infer a zero-free strip or RH.
---

# Finite Xi/theta certificate components

Use this skill only for a finite component whose analytic hypotheses and numerical enclosures are supplied separately.  It isolates two reusable gates: a mesh-to-polynomial lower bound, and an exact degree-10 cross-endpoint polynomial implication.

The included script has no special-function evaluation and does not locate a zero of \(\Xi\).  It exactly proves the stated polynomial consequence of five already-certified rational moment-ratio inequalities.  It therefore cannot replace the Arb enclosure from which those inequalities originate.

```sh
python3 scripts/check_cross_endpoint_polynomial.py
```

Read the source contracts before use:

- [Mesh-to-polynomial positivity gate](references/van-hemert-theta-mesh-gate.md)
- [Exact degree-10 cross-endpoint polynomial sublemma](references/van-hemert-degree10-sublemma.md)
- [Wronskian-to-Hankel-minor transfer](references/sra-wronskian-hankel-transfer.md)
