# Positive example — a uniform convolution with a gapped sum support

Let `X` be uniform on `{0,1}` and `Y` be uniform on `{0,3}`. Their PGFs are

`P_X(z)=(1+z)/2`, `P_Y(z)=(1+z^3)/2`.

Therefore

`P_X(z)P_Y(z)=(1+z+z^3+z^4)/4`.

The four sums `0,1,3,4` each have probability `1/4`; the sum is uniform on its support, which has a gap at 2. The unnormalized mask is the monic 0–1 polynomial `F(z)=1+z+z^3+z^4=(1+z)(1+z^3)`. This is a valid factorization into 0–1 factors; no interval-support premise is needed.

The example checks the PGF reduction and support bookkeeping only. It does not imply every nonnegative-real factor of every 0–1 mask has 0–1 coefficients.
