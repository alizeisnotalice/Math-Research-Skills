# Positive example: exact rational LP optimality

Consider

`min 3x₁ + 2x₂` subject to `x₁ + x₂ = 1`, `x₁,x₂ ≥ 0`.

The primal point `(0,1)` is feasible with value `2`. A dual point `π=2` is feasible because its dual constraints are `π≤3` and `π≤2`; its value is `2`. Exact feasibility and equal objective values certify optimality by weak duality. The certificate is finite and rational; no solver tolerance is involved.

Machine-checkable demonstration: [evidence/W19/exact_lp_certificate_probe.py](../evidence/W19/exact_lp_certificate_probe.py), with actual output at `evidence/W19/exact_lp_certificate_probe.out`.
