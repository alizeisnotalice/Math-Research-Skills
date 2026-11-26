# Ordered Gaussian cascade derivative interface

For a finite overlap hierarchy with ordered nonnegative covariance increments
and interval weights, use the draft's finite cascade calculus only after the
caller supplies its covariance matrix and differentiability path.  With
conditional means `m_i(Z_i)` and `B_i=E[m_i(Z_i)^2]`, the stated derivative
is

`d ell(h) = -(1/2) sum_i w_i B_i(h) d h_i`,

with `0<=B_0<=...<=B_{k-1}<=1`; constant-interval subdivision preserves the
value.  This is an interpolation derivative component, not a pressure formula
for arbitrary orthogonally invariant models.

Source: *All-temperature pressure for orthogonally invariant Ising spin
glasses*, SHA-256 `ecaeb31108feca6fa7f9768de75adf73990407ccdd2bb70e9416bb51c5762d57`,
physical pp. 12--14, Proposition 3.1; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/paper.pdf).
