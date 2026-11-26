# Arb certificate for the centered-square comparison kernel

Use this workflow for the planar axis-parallel centered square maximal
operator in Tomar, *Bounds for the weak type (1,1) constant of the centred
maximal operator over squares*, physical pp. 2–8. Fix the rotation-scale
map \(T(u,v)=(u+v,u-v)\), whose Jacobian has absolute value 2, and the
diamond \(D=\{(u,v):|u|+|v|\le1\}\). Lin's comparison principle, Theorem 2.2,
uses an even integrable kernel \(K\) with \(K\ge0\), \(K\ge1\) on \(D\), and
\(AK\ge0\) distributionally off the origin. It gives \(c_2\le\tfrac12\int K\).

For the source kernel use \(h=1/32\), \(\alpha=47/40\), and \(R=33/20\).
Use the positive second-difference operator \(A\) of (2.1).
Section 5 proves nonnegativity outside the kernel support from \(K\ge0\).
Lemma 3.1 transfers the almost-everywhere sign to the distributional sign.
Keep these steps when using the finite cell checks.

At revision 3af09fc359ce262f4a7f63d34b0d97e6d4d95d1a, the upper input file
has SHA-256 bd8d91b535e0a91fed777251afa6c4d73d78b1e7d14aee7288e5950d8ad28db3.

~~~sh
python3.12 -B -I checker/cert_run.py cert/cert_h32_a4740_R3320_3p59123.json --Q 8 --maxdepth 7 --procs 6
python3.12 -B -I checker/independent/hl_check.py cert/cert_h32_a4740_R3320_3p59123.json --claim 3.59123 --procs 6
~~~

Both terminated successfully using Python 3.12.13 and python-flint 0.9.0.
The first bounds \(\tfrac12\int K\) by the Arb ball
\([3.59122432750645234527147802\pm2.23\times10^{-27}]\) and tests 219732
\(AK\) subcells with zero failures. The second tests 443754 \(AK\) leaves
with zero failures and independently accepts the \(3.59123\) mass claim.
The resulting application of Theorem 2.2 is for this plane, centering and
basis. The authors also provide a separate Lean route.
[Fixed certificate repository](https://github.com/tejasvi/square-maximal-weak-type/tree/3af09fc359ce262f4a7f63d34b0d97e6d4d95d1a).
