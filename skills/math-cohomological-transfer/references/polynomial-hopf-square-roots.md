# Polynomial Hopf square roots in characteristic two

## Transfer theorem

Let \(H\) be a connected graded commutative Hopf algebra over \(\mathbb F_2\), polynomial as an algebra on homogeneous generators \(y_i\) of positive degree. If \(f\in (H^+)^2\) is primitive, then there is a unique \(z\in H\) with \(f=z^2\), and \(z\) is primitive.

If, in addition, homology Steenrod operations act on \(H\) and obey the homology Cartan formula, then \(f=z^2\) being annihilated by every positive Steenrod operation implies the same for \(z\).

### Proof

Put \(QH=H^+/(H^+)^2\), let \(\pi:H\to QH\) send \(1\) to zero, and set
\[
 \partial=(1\otimes\pi)\Delta:H\longrightarrow H\otimes QH.
\]
The identity \(\pi(ab)=\epsilon(a)\pi(b)+\epsilon(b)\pi(a)\) makes \(\partial\) a derivation. Positive grading gives
\[
 \partial y_i=1\otimes[y_i]+\text{terms whose second factor has smaller positive degree}.
\]
For a polynomial \(g\), inspect successively the coefficients of \([y_i]\), starting at the largest generator degrees occurring in \(g\). If \(\partial g=0\), this triangular form forces every ordinary polynomial derivative \(\partial g/\partial y_i\) to vanish. Over \(\mathbb F_2\), every monomial exponent is then even, so \(g=z^2\) for a unique polynomial \(z\).

For the stated \(f\), primitivity and decomposability give \(\partial f=1\otimes\pi(f)=0\), hence \(f=z^2\). Write \(r=\Delta z-z\otimes1-1\otimes z\). Since \(f\) is primitive, \(r^2=0\). But \(H\otimes H\) is again a polynomial algebra, so Frobenius is injective and \(r=0\); thus \(z\) is primitive.

Finally, Cartan gives
\[
 Sq_*^{2a}(z^2)=(Sq_*^a z)^2,\qquad Sq_*^{2a+1}(z^2)=0.
\]
If every positive operation kills \(z^2\), Frobenius injectivity forces \(Sq_*^a z=0\) for every \(a>0\).

## Exact finite models

The replay script verifies the coproduct algebraically in two small connected graded models.

* In \(\mathbb F_2[x,y]\), with \(|x|=1\), \(|y|=2\), \(x\) primitive and \(\overline\Delta y=x\otimes x\), the class \(x^2\) is a decomposable primitive and its root \(x\) is primitive.
* In \(\mathbb F_2[x,y]/(x^2)\) with the same formulas, \(y^2\) is a decomposable primitive while \(y\) is not primitive: its reduced coproduct is \(x\otimes x\ne0\), whose square is zero. This is a boundary counterexample showing why polynomiality (equivalently here, Frobenius injectivity) cannot be removed.

## Source and boundary

Distilled from *The Stable Hurewicz Image of the Sphere at Two*, Lemma 2.9, PDF p. 13; pinned local PDF SHA-256 `4234ea3418d229fb128003bf03c65398c2be92bb94878f7969bbfde9f99b2116`, official version [OpenAI/math preprint](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/paper.pdf).

The source applies its algebra hypothesis to particular infinite-loop-space homology algebras. This note does **not** verify those presentations, any Steenrod action on a new input, or the paper's later mapping-cone and stable-Hurewicz arguments.
