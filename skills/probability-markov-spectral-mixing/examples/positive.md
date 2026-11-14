# Positive example: state the A040 boundary exactly

> For a finite cycle with zero external field and random-site discrete heat-bath updates, Nacu proves that the per-site-rate-one relaxation time is non-decreasing in each positive edge coupling. Kargin's paper states a homogeneous complete-graph theorem with uniform field, but its audited proof uses the reflection `f_k=−f_{n−k}`; this evidence pack applies the proof only at `H=0` and leaves the stated nonzero-field case unresolved. LPW's Chapter 26 Question 2 asks whether the edgewise gap monotonicity holds on every graph. Shirai's fixed-time single-spin counterexample refutes a stronger expectation claim only; it does not decide the gap question.

This report keeps geometry, fields, parameter path and clock visible. It leaves arbitrary-graph A040 open in this evidence pack.

For a finite reversible kernel, a path comparison is applied to that fixed kernel: verify `π`, `Q`, the chosen path family and edge congestion, and use `β₁≤1−1/κ` for the Poincaré gap. If the claim is discrete-time worst-case TV, also control `β_min` (for example by odd-return paths) or prove the actual kernel is lazy/positive semidefinite. A comparison of two kernels' mixing times uses an odd flow unless the target chain has no negative-endpoint obstruction. These are fixed-model inequalities, not an ordering in an Ising edge parameter.
