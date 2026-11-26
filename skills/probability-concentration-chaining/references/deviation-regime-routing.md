# Deviation-regime routing

Choose the dependence model and the requested conclusion before selecting a concentration inequality. This table routes proof objects; it does not transfer assumptions, constants, or source scope between rows.

| Dependence and claim | Required gate | Route |
| --- | --- | --- |
| Independent centered sum, fixed terminal upper/lower/two-sided tail | Prove product MGF or a matching bounded/Bernstein hypothesis; retain range and variance scale. | [H05](../../math-h05-chernoff-hoeffding-bernstein/SKILL.md) |
| Filtered increments, fixed terminal nonasymptotic Bernstein tail | Conditional centering, conditional factorial moments, common deterministic scale, and deterministic predictable-variance budget. | [I01](../../math-i01-ordered-increment-conditional-bernstein/SKILL.md) |
| Martingale relative normal-tail/moderate-deviation expansion | Fan–Grama–Liu A1/A2, variance closeness, sign and exact \(x\) range. | [H03](../../math-h03-fan-grama-liu-martingale-expansion/SKILL.md) |
| Independent/triangular-array uniform Cramér or a named model-specific MDP | Uniform exponential-moment, variance, and moving-deviation range; retain whether output is logarithmic, relative, or a rate only. | [H01](../../math-h01-uniform-cramer-moderate-deviations/SKILL.md) |
| Conditionally independent array with the admitted shrinking-cutoff Lugannani–Rice result | Conditional array theorem, high-probability saddlepoint root, shrinking threshold and the exact LR expression. | [H02](../../math-h02-exponential-tilting-saddlepoint/SKILL.md) |
| Time-uniform crossing or stopping/maximum statement | A valid nonnegative supermartingale, filtration, scale process, and initial normalizer; preserve the theorem's process-wide event. | This skill: P004/P034/Freedman scoped rows |
| Supremum with common mixed-tail increments \(\sqrt u d_2+u d_1\) | Two semimetrics, \(\gamma_2,\gamma_1\), diameters, basepoint, and measurability/separability. | [K03](../../math-k03-dirksen-mixed-tail-generic-chaining/SKILL.md) |
| Supremum under a specific generic source-card increment condition | Match the exact P002 \(\psi_\alpha\)/mixed-tail or P015 finite sub-Gaussian condition and retain its basepoint term. | This skill: P002/P015 scoped rows |

## Non-substitution rules

- A fixed-time conditional MGF argument may prove a terminal bound; it is not a time-uniform crossing theorem.
- An exponential rate, a Bernstein tail, and a relative normal-tail or Lugannani–Rice expansion are different outputs.
- A saddlepoint identity alone does not supply Gaussian local approximation, lattice correction, or a prefactor.
- One tail metric does not create Dirksen's two-metric mixed-tail premise.
- All source-specific conditions and held findings remain in their owning skill or this skill's accepted theorem ledger.
