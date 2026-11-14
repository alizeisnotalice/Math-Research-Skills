# AUX-ALDOUS-SHAPE-2009 — The Shape Theorem for Route-lengths in Connected Spatial Networks on Random Points

**Author:** David J. Aldous. **Read source:** complete arXiv:0911.5301v1, 16 physical pages, SHA-256 `cf7135208cea2652417e5985880501c37449cc5d58111bf5a83a8aca55883efc`. The front banner dates v1 to 27 Nov. 2009, while the title page says 6 Nov. 2018; preserve the discrepancy. Review pending.

## Setup and result

On a unit-intensity planar Poisson process `Ξ`, assign finite symmetric nonnegative pairwise route lengths satisfying the triangle inequality. The full marked structure is translation invariant and each nonzero translation is ergodic. For bounded windows `A,B`, define `S(A,z+B;c) = sum_{ξ∈A} sum_{ξ′∈z+B} |d(ξ,ξ′)−c|`.

Assume the uniform L2 pair-sum bound `sup_z E sum_{ξ∈A,ξ′∈z+B} d(ξ,ξ′)² / max(1,|z|²) < ∞` for all bounded `A,B`. **Theorem 1 (physical p. 4; proof §2, pp. 7–10)** gives directional constants `ρ(θ)`, Lipschitz in `θ`, such that `r_z⁻¹ E S(A,z+B;r_z ρ(θ_z)) → 0`. This is an L1, pair-summed shape property.

## Proof chain

Select a uniform point in each translated window when it is nonempty; otherwise set the route length to infinity. The resulting array satisfies subadditivity when all three windows are occupied, Bernoulli occupancy independence, stationarity/ergodicity, and the second-moment bound. Proposition 4 (§3, pp. 11–15) is a “Kingman theorem with missing values”: replace each gap between adjacent bad indices by a penalty `K`, take the minimum over good-index chains to get an everywhere finite subadditive array, apply Kingman, then send `K→∞`. The L2 estimate controls bad runs touched by a minimizing chain and yields L1 convergence. A window-counting lemma transfers the selected-pair limit to the sum over all point pairs; L2 uniform integrability upgrades probability convergence to expectation convergence.

The paper states **Conjecture 3**, not a theorem, for an almost-sure shape set under the weaker linear L1 bound plus `d(ξ,ξ′)≥|ξ−ξ′|`. Its sparse exceptional-distance example explains why a planted pair at exact distance `r` can fail to converge even when typical-pair behavior is regular.

## A136 boundary

The theorem concerns a typical long pair after averaging over Poisson windows. It does not estimate `E sup_i d(0,U_i)`, impose a common fixed origin and iid endpoints, or provide a countable-family maximum tail. The a.s. shape property is explicitly conjectural in this source.

**Rendered check:** original physical p. 4, hypotheses (1)–(4) and Theorem 1; complete section coverage is in `evidence/W20/reading_coverage.json`.
