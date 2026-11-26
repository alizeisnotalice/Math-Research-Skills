# Flint Hills sine-distance sandwich

Source: M.-A. Garab, *A Geometric--Arithmetic Framework for the Flint Hills
Series*, arXiv:2510.27041v1, local PDF SHA-256
`0bb819e6c749091b0a7e0119f8a53fa328a74a13b5a91235aa4f61936d8c4245`,
physical p. 2, Theorem 2.1.

For an integer `n >= 1`, put `d(n)=dist(n, pi Z)`.  Since `pi` is irrational,
`d(n)>0`; reducing modulo `pi` gives `d(n) in [0,pi/2]`.  The elementary
chord and tangent bounds on that interval give

`(2/pi)d(n) <= |sin n| <= d(n)`.

Consequently, for every finite set of nonnegative coefficients `c_n`,

`sum c_n/(n^3 d(n)^2) <= sum c_n/(n^3 sin(n)^2) <= (pi^2/4) sum c_n/(n^3 d(n)^2)`.

The same assertion holds for increasing limits of nonnegative partial sums.
It is a comparison/obstruction-isolation tool only: it does not bound the
exceptionally small distances `d(n)`, prove convergence of the Flint Hills
series, or validate the source's weighted-series corollary.
