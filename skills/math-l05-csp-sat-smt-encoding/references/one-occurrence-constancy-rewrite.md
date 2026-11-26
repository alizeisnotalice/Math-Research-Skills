# One-occurrence constancy rewrite

For a universally quantified magma identity \(s=t\), if a variable occurs in \(t\) and does not occur in \(s\), then \(t\) is independent of that variable in every magma satisfying the identity.  Fix all other variables and apply the identity at two values of the remaining variable.  Both right-hand values equal the fixed value of \(s\).

`scripts/one_occurrence_constancy.py` checks this implication for a supplied finite operation table after first checking the universal identity by exhaustive enumeration.  It neither produces Lean certificates nor establishes benchmark coverage.

Source use. Thakur, *The Verdict Is Free*, physical pp. 4–5, Proposition 1. The source's dataset counts, ETP lattice, harness, and Lean judge remain separate dependencies.
