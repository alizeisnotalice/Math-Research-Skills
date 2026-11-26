---
name: math-finite-permutation-terrace-certificates
description: Verify a supplied ordering of all even permutations as a finite directed-terrace certificate; includes a reader for the public packed A7 witness format.
---

# Finite alternating-group terrace certificates

Use this skill only for a caller-supplied, fully explicit ordering of the
alternating group in permutation notation. It checks the finite statement; it
does not construct terraces or imply a result for other groups.

The JSON input has `degree` and `rows`, where every row is a zero-based image
list. The checker verifies that the rows are precisely all even permutations,
begin with the identity, and that the consecutive quotients meet the directed
terrace count condition. Composition convention is stated in the checker.

```sh
python3 scripts/check_terrace.py examples/a3-positive.json
python3 scripts/check_terrace.py examples/a3-duplicate-boundary.json
```

The second command must fail: it is a boundary case showing that a duplicate
row is rejected before quotient counts are used.

For the packed public A7 source format, use

```sh
python3 scripts/replay_packed_a7.py PATH/TO/Data.lean
```

It is deliberately tied to the documented 21-bit/base-8 encoding, checks all
2,520 decoded rows independently, and has no Lean dependency. The source and
the exact limits of this replay are recorded in
[the A7 source note](references/a7-packed-witness.md).
