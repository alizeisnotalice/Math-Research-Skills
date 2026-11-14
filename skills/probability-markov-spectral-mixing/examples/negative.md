# Negative example: invalid static-to-dynamic transfer

> GKS/FKG gives positive correlations in the stationary ferromagnetic Ising measure, so increasing one J_uv must increase every fixed-time spin expectation and therefore make the spectral gap smaller on every graph.

This is invalid. FKG orders stationary increasing observables; it is not a theorem about finite-time semigroup expectations or the second eigenvalue. Shirai proves the fixed-time single-spin assertion can fail on a graph containing a length-3 path. That counterexample does not itself contradict spectral-gap monotonicity. To prove a gap claim, fix the clock and control the changing Dirichlet form and variance (or the relevant eigenvalue branch) directly.

> For an arbitrary finite reversible discrete-time chain, `k>0` (or a positive Poincaré gap below eigenvalue `+1`) automatically gives geometric total-variation mixing.

This ignores the bottom of the spectrum: the simple random walk on a connected bipartite graph can have eigenvalue `−1`, and a nearly bipartite chain can mix slowly despite a good upper-endpoint bound. Use an absolute-gap bound, odd-return paths, an odd-flow comparison, or verify laziness/nonnegative spectrum. Continuous-time Poissonization has a different spectral decay formula and a specified jump-rate normalization.

> Diaconis–Stroock Proposition 6 gives `β₁≤1−h²` for every finite reversible ergodic chain, so that sharper upper bound may always be used.

The paper prints this inequality, but its §3C proof gives only `β₁≤1−h²/2`; moreover an exact four-state reversible, irreducible and aperiodic kernel violates the printed `h²` version. Use the proof-supported factor `1/2` unless independent review finds a missing hypothesis or correction. The exact cut enumeration and eigenvalue comparison are recorded in `evidence/W04/numerical/s027_cheeger_printed_bound_audit.json`.
