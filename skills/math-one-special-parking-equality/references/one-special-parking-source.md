# Finite one-special parking checker from the equality manuscript

Source record `44988b0c7471819b7c884a320f0296b75c5a472684b4299ceccb59a3c87ab1c8`,
*The equality case of Chen's bound for invariant parking with one special preference*,
author manuscript dated 22 November 2026.

Physical pages 1--6 define \(W(y)\), prove the residual reduction, and state the equality
criterion. The source reports a Lean formalisation on p. 7, yet the pinned repository and
build were unavailable to this review. The checker therefore performs the finite parking
definition itself and exposes the source criterion separately.

For \(n\ge2\), write \(y=(a,b,u)\), \(D=\sum u\), \(\delta=a-b\), and let \(T\) be the subset
sums of \(u\). The source states equality \(|W(y)|=2^{n-1}\) precisely when \(a\ge b\),
\((b,u)\) is superdecreasing, and either \(\delta\ge D\) or \(D-\delta\) is a symmetric
member of \(T\). Direct enumeration remains the certificate for each finite input.
