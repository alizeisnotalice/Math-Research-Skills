# Exact expected-improvement non-density construction

## Source and scope

D. Yarotsky, *Examples of inconsistency in optimization by expected
improvement*, Journal of Global Optimization 56(4) (2013), 1773--1790,
DOI 10.1007/s10898-012-9936-x. The checked local version is
arXiv:1109.1320v2. Physical pp. 6--7 and 16--19 are used.

This is a one-dimensional, noiseless, fixed-kernel failure-mode template. It
does not apply to noisy Bayesian optimization, kernel fitting, approximate EI
maximization, or unspecified tie rules.

## Callable construction

Let the domain be `[-1,1]` and let `G` be a centered stationary Gaussian
process covariance whose spectral density is `exp(-S(|t|))`, with `S` twice
continuously differentiable, `S' >= 0`, `S'' >= 0`, and `S'(t) -> infinity`.
Start exact expected improvement at `x_1 = 0` with objective
`f(x) = -G(x)`.

Theorem 3 proves that the exact EI trajectory converges to zero and hence is
not dense. The crucial identity is algebraic: at every stage the noiseless
posterior interpolant equals `f`, because `f(x) = -G(x-x_1)` is already in
the kernel span. The conditional-variance bounds of Theorem 2 then drive the
EI comparison used in the convergence proof.

For the Gaussian kernel, the source's smooth inconsistency corollary uses a
separate `C-infinity` modification away from the constructed trajectory; do
not identify that modified objective with the analytic function `-G`.

## Boundary

A replay must supply a concrete kernel satisfying the displayed spectral
conditions, an exact posterior, global EI maximization, and a deterministic
tie rule. A finite floating-point trajectory is not a certificate of the
non-density conclusion.
