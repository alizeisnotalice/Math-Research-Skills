# Curvature and cone transfer

This reference supplies two source-located interfaces. Both were extracted from OpenAI preprints in the fixed archive. They are usable at their displayed hypotheses, while the preprints' headline results require further arguments and are not certified by this page.

## Anisotropic positive curvature

Let \(S\) be a positive-definite matrix and let \(U:\mathbb R^n\to(-\infty,+\infty]\) be proper, lower-semicontinuous, and convex. Suppose

\[
d\pi(x)=Z^{-1}\exp\{-\tfrac12\langle x,Sx\rangle-U(x)\}\,dx
\]

is a probability measure with full-dimensional support. Then, first for compact smooth \(f\),

\[
\operatorname{Ent}_\pi(f^2)
 \le 2\,\mathbb E_\pi\langle\nabla f,S^{-1}\nabla f\rangle,
\qquad
\operatorname{Var}_\pi(f)
 \le\mathbb E_\pi\langle\nabla f,S^{-1}\nabla f\rangle.
\]

The same statements hold for functions reached by finite-energy approximation. This is a direct anisotropic curvature criterion. It requires an actual matrix \(S\succ0\) in the displayed density. Subgaussian tails, log-concavity, or a covariance bound alone do not supply such a decomposition.

For smooth \(U\) with bounded Hessian, whiten to \(S=I\). The Langevin derivative flow satisfies \(\|J_t\|_{\mathrm{op}}\le e^{-t}\), which gives the semigroup gradient contraction. Entropy dissipation then integrates to the logarithmic Sobolev inequality. For nonsmooth \(U\), use quadratic infimal convolutions, then smooth convex mollifications. Their affine lower bounds yield an integrable Gaussian-linear dominator, so normalized densities converge in \(L^1\). The compact-test bound passes to the limit. Full-dimensionality matters because the boundary of a full-dimensional convex support has Lebesgue measure zero in this passage.

For a Gaussian check with \(U=0\), \(S=\operatorname{diag}(2,3)\), and \(f(x)=u^\top x\) for \(u=(5/3,-7/4)\), both sides of the Poincaré equality are

\[
u^\top S^{-1}u=\frac{347}{144}.
\]

This exact rational calculation was run locally with SymPy 1.14.0. It checks the anisotropic normalization, and does not prove the general inequality.

## Exponential cone lift for a centered convex body

Let \(K\subset\mathbb R^n\) be a convex body with centroid zero, \(X\) uniform on \(K\), and \(\Sigma_K=\operatorname{Cov}(X)\). Define

\[
C_K=\{(tx,t):x\in K,\ t\ge0\},
\qquad
f_K(y,t)=\frac{e^{-t}}{n!\,|K|}\mathbf 1_{C_K}(y,t).
\]

The substitution \(y=tx\), with Jacobian \(t^n\), proves that \(f_K\) is a probability density and the law of \((TX,T)\), where \(T\sim\operatorname{Gamma}(n+1,1)\) is independent of \(X\). Therefore

\[
h(f_K)=n+1+\log(n!|K|),
\]

and, using \(\mathbb EX=0\),

\[
\operatorname{Cov}(f_K)=
\begin{pmatrix}
(n+1)(n+2)\Sigma_K&0\\
0&n+1
\end{pmatrix},
\qquad
\det\operatorname{Cov}(f_K)
=(n+1)^{n+1}(n+2)^n\det\Sigma_K.
\]

This is a transfer rule. Apply it only after checking that the proposed \((n+1)\)-dimensional entropy inequality accepts this log-concave cone density with its covariance convention. Keep the direction of the entropy inequality when translating it to a body-volume or isotropic-constant statement. The lift itself neither proves an entropy inequality nor selects an extremal body.

For \(n=1\) and \(K=[-1,1]\), local `Fraction` arithmetic gives

\[
\operatorname{Var}(X)=\frac13,
\quad \operatorname{Var}(TX)=2,
\quad \operatorname{Var}(T)=2,
\quad \det\operatorname{Cov}(f_K)=4,
\]

which agrees with the determinant formula. The entropy specializes to \(2+\log2\). This is a normalization check only.

## Source and verification scope

- OpenAI, *A dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures*, PDF pp. 6–7, Lemma 2.1. The local PDF hash is `767a5eb7cd819af7e33c8b867c41403aac36ec015c89c1d2beb186abca9ec89e`. [Fixed-version PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf)
- OpenAI, *A sharp entropy bound and the simplex inequality for isotropic constants*, PDF p. 31, equations (7.1)–(7.5). The local PDF hash is `b6cb0115cd04d4eb0c24db7e600ba8dd9519848a92e87fa8a661f435e41e95a0`. [Fixed-version PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf)

The first source's later dimension-free subgaussian conclusion and the second source's sharp entropy and simplex conclusions are outside this reference's verified interface.
