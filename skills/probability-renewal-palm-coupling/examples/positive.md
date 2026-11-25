# Positive example: keep the target and input law aligned

For an adaptive polling model, first record the arrival/service/walk assumptions, cycle rule, visit discipline, and target notion. In Chernova–Foss–Kim, `ζ>ζ*` is global; standard cycles are `1→2→3→1`, reduced cycles `1→3→1`, and an empty queue 2 in a standard cycle triggers the reduced next cycle. State the independent IID finite-mean primitives, unbounded-support/spread-out interarrivals, and augmented strong-Markov state. For limited service test all three strict stability inequalities; the iff occurs only at `l_2=1`. At equality in an instability inequality report instability; report transience only under a strict inequality. Gated/exhaustive service has its separate `ρ_0<1` iff threshold.

For a stationary-ergodic scalar Lindley recursion, verify that the **net increments themselves** are two-sided stationary ergodic with strictly negative mean. Then the Györfi–Morvai pullback supremum gives a stationary recursion and finite-a.s. eventual coalescence from a finite initial value. Stop the claim at the scalar workload: this does not establish positive Harris recurrence or TV convergence of a larger state.

For a discrete-time marked point process, state time-stationarity versus point-stationarity, positive finite intensity, ergodicity, and within-slot ordering before applying Sigman–Whitt's Palm formula. Preserve batch-size bias and phase-specific intensities in periodic Little's law.

For a unit-intensity translation-invariant ergodic simple point process, Holroyd–Peres gives a nonrandomized shift selected from the same configuration that changes its stationary view to the Palm law. Unit intensity is the paper's standing hypothesis for Theorem 1, not only for the explicit balanced-allocation construction. The allocation gives one unit of Lebesgue volume to each point and uses mass transport to verify the shifted Palm law. A nonunit-intensity use requires separate normalization; this shift construction does not supply a displacement moment or a queue's stationary law.

For FIFO GI/GI/c, check iid renewal gaps, independent iid service, `ρ<c`, and which moment/positivity conditions are needed for finite expected termination. Explain the RA dominator and backward algorithm, retain equilibrium residual interarrival in the continuous-time stationary conversion, and invoke PASTA only in the Poisson special case.

For large deterministic setups, cite Winands Theorem 3.3 only under Poisson input and branching-type visits. Label the uniform weak limit as tagged-customer waiting time; label the separate deterministic limit as the queue length at its own polling epoch. Do not transfer either theorem to general renewal input.

For a total-variation claim, exhibit two correct marginal chains coupled on one space, start one from the target invariant law, and prove they coalesce while remaining together thereafter. State `d_TV ≤ P(T_couple>t)` only after these checks. If the proof provides only common-noise closeness or weak convergence, report that weaker topology.

For a finite chain, select the transition rule, invariant law, metric, and update randomness before using path coupling or CFTP. A path-coupling contraction can give an approximate TV bound under the source metric and contraction estimate; exact sampling requires the separate random-map invariance and whole-state collapse conditions. Do not upgrade one route to the other.

For a general-renewal large-switch-over limit, present the Poisson theorem as a benchmark and identify the missing uniform residual-age and stationary-tightness bounds. Keep the source conjecture open until those steps are proved.
