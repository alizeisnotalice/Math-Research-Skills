# Split full-cross Gram certificate

For the real \(2\times2\) biquadratic form

\[
 f=a_{11}x_1^2y_1^2+a_{12}x_1^2y_2^2+a_{21}x_2^2y_1^2
   +a_{22}x_2^2y_2^2-bx_1x_2y_1y_2,
\]

accept rational numbers \(b_{uz},b_{vw}\) satisfying

\[
 b=b_{uz}+b_{vw},\qquad
 \begin{pmatrix}a_{11}&-b_{uz}/2\\-b_{uz}/2&a_{22}\end{pmatrix}\succeq0,
 \quad
 \begin{pmatrix}a_{12}&-b_{vw}/2\\-b_{vw}/2&a_{21}\end{pmatrix}\succeq0.
\]

The supplied matrices are Gram matrices in the bilinear pairs
\((x_1y_1,x_2y_2)\) and \((x_1y_2,x_2y_1)\). Their sum represents \(f\),
since both mixed monomials equal \(x_1x_2y_1y_2\). Thus this is an
exact SOS certificate. The checker uses the rational \(2\times2\) PSD
criterion consisting of nonnegative diagonal entries and nonnegative
determinant.

This is a certificate for a supplied split. It does not decide general
biquadratic PSD or SOS, and it does not construct a split merely from the
source's square-root criterion. The split form is extracted from physical
pp. 13--14 of Cui, *Positive Semidefinite and Sum of Squares Biquadratic
Polynomials*, arXiv:2506.17260v4. The algebraic verification above is
independent of the paper's use of its earlier PSD-to-SOS theorem.

Run `python3 scripts/check_split_full_cross_biquadratic.py
examples/split-full-cross-positive.json`. A rejected split exits with status 2.
