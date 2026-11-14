# Positive examples

## A low-ℓp tensor query

Suppose the user asks whether the C120 target follows for fixed order (r=3), (p=2), arbitrary deterministic symmetric (T_i), and standard Gaussian coefficients.

1. Write the target norm as the diagonal symmetric ℓ(_2) injective norm. Compare it with the full multilinear norm using W12-002 Proposition 4.15; the factor depends on (r=3) only.
2. Theorem 1.2 gives (d^{1/2-1/p}=d^0) as its lower type exponent, but its general upper exponent is (d^{1/2-1/(2r)}=d^{1/3}), up to log (d).
3. State precisely that the cited theorem leaves a (d^{1/3}) power gap; do not claim the conjectured polylogarithmic bound. Mention that a bound for independent entries is a narrower model.

## The Euclidean matrix special case

For (r=p=2), the full bilinear norm is the matrix operator norm, and for symmetric (A_i) the diagonal quadratic norm is the same by the spectral theorem. Tropp’s matrix Gaussian-series inequality gives a tail controlled by (\sigma^2=\|\sum_iA_i^2\|_{\rm op}), hence an expectation (\lesssim\sqrt{\log(2d)}\,\sigma). Since
\[
\sigma^2\le\sum_i\|A_i\|_{\rm op}^2,
\]
this proves the requested matrix-family estimate with a √(log (d)) factor. State that this is the (r=p=2) specialization.

