---
name: math-one-special-parking-equality
description: Enumerate the invariant one-special-preference parking set for a finite positive length list and check the subset-sum equality criterion.
---

# One-special-preference parking equality

For a supplied positive integer list \(y=(y_1,\ldots,y_n)\), compute the finite set
\(W(y)\) directly. A candidate preference \(w\) is accepted only if the parking simulation
succeeds for every possible car given \(w\), while all other cars prefer the first spot.

Use the result to check a finite instance of the subset-sum equality criterion from the
source. The output labels `criterion_holds` as the source criterion and `direct_equality`
as the independently enumerated equality. It does not establish the source theorem for
arbitrary lists, and it does not depend on the claimed Lean artefact.

Run `scripts/check_one_special_parking.py examples/chen-four-car.json` for the documented
four-car pair. Read [the source scope](references/one-special-parking-source.md) when using
the criterion beyond direct enumeration.
