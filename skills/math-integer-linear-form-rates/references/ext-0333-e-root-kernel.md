# Formal e-root Hermite--Pade kernel

Source: `EXT-0333`, arXiv:2303.05542v1, physical pp. 4--6 (19 pages total), SHA-256 `4729a0e94ea80cfce088c54b843c58a55fbc607882155aa76b52192f2ec45103`.

For fixed (k\geq n\geq2), positive multiplicities \(\ell_j\), and \(\alpha_j=j/n\), the source's construction begins with

\[
\Omega(x)=\prod_{j=0}^{k}(\alpha_j-x)^{\ell_j}=\sum_i\sigma_i x^i,
\qquad A_0(t)=\sum_i i!\sigma_i t^{L-i}.
\]

The accompanying exact script obtains each translated integral polynomial (A_j) and verifies, coefficient-by-coefficient through degree (L), that (e^{\alpha_jt}A_0(t)-A_j(t)) has zero coefficients below its remainder order.  On `n=2,k=2,ell=[2,2,2]`, this check passes; its rational-coefficient denominator lcm is 8.

This verifies only the unscaled formal kernel.  It deliberately does not claim the source's scaled integrality, determinant/nonvanishing, common-factor, size bounds, or transcendence measure.  The global theorem still has an indispensable unresolved physical-p.18 uniform inequality step delegated there to WolframAlpha.
