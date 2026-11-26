# Tree convexity-deficit accounting

Source: *Endpoint convergence for the planar Schrödinger equation*, family 080, SHA-256 `68d6affc8c3cc3bcfe6878f64c12d8127274ce0f3b1971255d6ca8fd19673ab3`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/paper.pdf), physical p. 77, equation (9.15).

Use this when a finite binary mass tree already has designated heavier children and the target sum is over the dropped lighter children. For an exponent \(\alpha>1\), child masses \(a\ge b\ge0\) satisfy
\[
(a+b)^\alpha-a^\alpha-b^\alpha\ge(2^\alpha-2)b^\alpha.
\]
Sum the nonnegative parent-minus-children deficits only over distinct parents. This bounds the selected lighter-child \(\alpha\)-masses by the root mass to the power \(\alpha\), divided by \(2^\alpha-2\). In a cross-layer construction, record absolute depth: different relative-depth requests must not silently reuse the same parent.

Output a finite ledger containing selected parents, dropped child masses, and the resulting budget. The helper `../scripts/convexity_deficit.py` checks the integer-exponent arithmetic subcase exactly.

Boundary: this is not a Schrödinger maximal estimate, packet decomposition, or endpoint \(p=2\) argument. At \(\alpha=1\) the coefficient vanishes, so the method gives no lighter-child gain.
