# Four-slope integer reconstruction and quadratic cancellation

Source: *Triple ergodic averages with distinct integer slopes*, family 154, SHA-256 `883a45bc7b95cfafd7049d00ebd2b26ca233a089e6aa03e19c0c16b25bfda74e`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/triple-ergodic-distinct-slopes.pdf), physical p. 4, Lemma 2.3.

Given primitive distinct integer slopes \(b_0=0,b_1,b_2,b_3\), construct integral Bezout coefficients \(e_j\) with \(\sum e_j=0\) and \(\sum e_jb_j=1\). Construct nonzero common-denominator Vandermonde coefficients \(c_j\) satisfying \(\sum c_jb_j^a=0\) for \(a=0,1,2\). Then \(y_j=x+b_jt\) recovers the integral step as \(t=\sum e_jy_j\), while \(\sum c_jy_j^2=0\).

Record primitivity, distinctness, exact coefficients, and the cancellation checks. Pair-coordinate maps remain injective on \(\mathbb Z^2\), but this does not make a pair determinant unimodular.

Boundary: this only supplies the integer/algebraic transference interface; it does not supply the source's scheduled multilinear analytic estimate or its ergodic convergence theorem.
