# Littlewood off-band correction

Source: *Nearly minimal maxima and positive minima of Littlewood polynomials*,
SHA `639fe69dbb6e6e93441af292dde643b1a508658a43692bee514229433d706969`,
physical pp. 9 and 23.

For pairwise nonparallel nonzero integer forms `a_i` and positive widths `w_i`
with `2 sum_i w_i < 1`, the source supplies a finite collection of torus
points whose signed intervals `I(+- a_i dot theta_h,w_i/H)` are pairwise
disjoint. The strict inequality and pairwise nonparallel condition are input
requirements, not conclusions of the packing step.

For a separately supplied piecewise correction with the endpoint and derivative
budgets used in the source, its twice-integrated calculation yields
`|Rhat_N(k)| <= C_delta w^(-1)(N+|k|)^(-2)` off the degree band, hence an
`O_delta((Nw)^(-1))` tail after summation. This reference does not construct
the correction, establish a Littlewood extremum, or perform the rounding step.

## 固定来源

- 物理页 9, 23。Lemma 3.1 is the signed-interval packing statement; equation (64) and the following calculation give the off-band Fourier bound. SHA-256 `639fe69dbb6e6e93441af292dde643b1a508658a43692bee514229433d706969`。[Nearly minimal maxima and positive minima of Littlewood polynomials](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/littlewood-lower-envelope.pdf)
