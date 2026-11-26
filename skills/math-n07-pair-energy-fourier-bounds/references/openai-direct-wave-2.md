# Finite-field affine-line second moment

Source: *A counterexample to Ryser's covering conjecture*, family 162, SHA-256 `ba76ca1f7af545c68090e0cfa1defba423af058cb4c0ac6087e563b5123b1eb7`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf), physical p. 24, equation (59).

For \(U\subseteq\mathbb F_q^2\), form every affine-line slice count across all \(q+1\) directions. The summed directional variance is exactly \(|U|-|U|^2/q^2\). This identity can be used as an exact finite energy normalization before probabilistic selection.

Input specifies a prime-power field model and a finite point subset; output is the all-line second-moment ledger. Do not replace a supplied martingale or independence hypothesis by this deterministic identity.
