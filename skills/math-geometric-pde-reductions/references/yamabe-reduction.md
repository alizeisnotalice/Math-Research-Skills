# Conditional Yamabe reduction to an integral curvature bound

## Statement

Let \(n\ge3\). Assume for every closed connected oriented smooth \(n\)-manifold \(M\):

1. each smooth \(h\) with \(\operatorname{Scal}_h=-1\) obeys \(\lVert M\rVert\le C_n\operatorname{Vol}_h(M)\), for one finite dimension-only \(C_n\);
2. a smooth metric with \(\operatorname{Scal}\ge0\) forces \(\lVert M\rVert=0\).

For every smooth \(g\) on \(M\),
\[
 \lVert M\rVert\le C_n\int_M(\operatorname{Scal}_g^-)^{n/2}\,dV_g.
\]

This is the independently checked transfer in Proposition 2.2 of the pinned source below. It does not prove either hypothesis.

## Derivation

Put \(A=\int_M(\operatorname{Scal}_g^-)^{n/2}\,dV_g\). The claim is trivial if \(\lVert M\rVert=0\). Otherwise the second assumption rules out every nonnegative-scalar-curvature metric and, in particular, a nonnegative constant-scalar-curvature Yamabe minimizer in \([g]\). Yamabe attainment supplies a negative constant-scalar-curvature minimizer; a constant rescaling gives \(h\in[g]\) with \(\operatorname{Scal}_h=-1\).

For its Yamabe constant, evaluation at the constant function gives
\[
Y(M,[g])=Y(M,[h])=-\operatorname{Vol}_h(M)^{2/n}.
\]
For any \(u>0\), Hölder with \(p=n/2\), \(q=n/(n-2)\) gives
\[
\int_M\operatorname{Scal}_g u^2dV_g
\ge-A^{2/n}\left(\int_Mu^{2n/(n-2)}dV_g\right)^{(n-2)/n}.
\]
Adding the nonnegative Yamabe gradient term, dividing by the Yamabe denominator, and taking the infimum gives \(Y(M,[g])\ge-A^{2/n}\). Thus \(\operatorname{Vol}_h(M)^{2/n}\le A^{2/n}\), hence \(\operatorname{Vol}_h(M)\le A\). Assumption 1 proves the conclusion.

The exponents are valid exactly for \(n\ge3\); no assertion is made for \(n=2\), nonclosed manifolds, nonsmooth metrics, or missing Yamabe attainment.

## Source identity and locus

OpenAI, *An integral scalar curvature bound for real simplicial volume*, 5 October 2026, pinned OpenAI Math commit `3344da59991ed94f9ba711217b29c1d760badfa6`, PDF SHA-256 `d5ed8374cef6389d2d54c921422a4523ecc11216b65887ede13bdf25a38ea6f1`.

Official pinned PDF: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf>. The conditional proposition and proof are on PDF p. 5; the cited nonnegative-scalar-curvature vanishing input is also stated there, with theorem-level context on pp. 2–3. The local reviewed object has 84 PDF pages.
