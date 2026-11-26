---
name: math-four-square-witness-certificates
description: Produce or verify an exact finite four-square witness while explicitly separating that certificate from the incomplete descent in the source note.
---

# Four-square witness certificates

Use this skill when an explicit witness is needed for a fixed nonnegative integer \(n\). The exact verifier checks \(a^2+b^2+c^2+d^2=n\); the bounded search emits a witness if it finds one.

```sh
python3 -B scripts/four_squares.py search 7
python3 -B scripts/four_squares.py verify 7 1 1 1 2
```

The output is an independently checkable certificate for that input. It does **not** validate the source's Lemmas 1--2, establish that the source descent terminates, or replace a proof of Lagrange's theorem. The only safely reused source ingredient is the explicitly checkable Euler four-square composition identity, documented in [the source record](references/bachet-note-scope.md).
