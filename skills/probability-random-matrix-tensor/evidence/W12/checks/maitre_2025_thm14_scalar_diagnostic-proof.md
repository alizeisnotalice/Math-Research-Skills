# W12-027 Theorem 1.4 scalar diagnostic

This is a falsification check for the two incorrect power placements that appeared in the first transcription; it is not a proof of Maitre's matrix theorem.

For a one-dimensional Brownian integral with constant scalar integrand `H=c`, `X_t=c B_t`. The exact Gaussian moments are `E|B_t|^2=t` and `E|B_t|^4=3t^2`.

- With `p=2`, `t=2`, `c=1`, the printed theorem gives `2 <= (2p-1)·2 = 6`.
- Replacing the printed second moment by the `2p`-moment gives `12 <= 6`, which is false.
- Keeping the second moment but raising the integrand Schatten-`p` norm to `p`, at `c=1/2`, gives `0.5 <= 0.375`, also false.

The values were evaluated in MATLAB by `maitre_2025_thm14_scalar_diagnostic.m`; the captured output is `maitre_2025_thm14_scalar_diagnostic.out`. The exact Gaussian moment formulas and the rendered source statement are the mathematical basis; computation only checks the arithmetic and demonstrates that the erroneous variants fail in these scalar cases.
