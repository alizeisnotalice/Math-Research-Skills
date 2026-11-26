# Method notes and proof interfaces

## 1. Type-2 bounds for random tensors (C120)

The C120 source defines the *diagonal symmetric* norm
\[
\|T\|_{\mathrm{sym}(I_p)}=\sup_{\|x\|_p\le1}|T[x,\ldots,x]|,
\]
for a symmetric real (r)-tensor, and asks for a Gaussian-series bound of order
\[
\widetilde O_{r,p}\!\left(d^{1/2-1/p}\sqrt{\sum_i\|T_i\|_{\mathrm{sym}(I_p)}^2}\right),\qquad p\ge2.
\]
The tilde in the problem hides polylogarithms in (d,n) and constants for fixed (r,p). Do not confuse the geometric (p) with a moment exponent in Gaussian-chaos theorems.

W12-002 defines the type-2 constant for the *full multilinear* norm (\|T\|_{I_p}=\sup_{\|x_j\|_p\le1}T[x_1,\ldots,x_r]). Theorem 1.2 (PDF p. 4) gives
\[
d^{1/2-1/p}\lesssim_{r,p} C_{r,p}(d)
\lesssim_{r,p}d^{1/2-1/\max(p,2r)}\log d.
\]
For symmetric tensors, Proposition 4.15 (PDF p. 35) gives
\[
\|T\|_{\mathrm{sym}(I_p)}\le\|T\|_{I_p}
\le(r^r/r!)\|T\|_{\mathrm{sym}(I_p)}.
\]
So fixed-order norm equivalence transfers the exponent comparison. The type constant controls the expected Gaussian series as well: condition on Gaussian magnitudes and apply the Rademacher type bound to |g_i|(T_i); the reverse comparison uses the standard Kahane–Khintchine estimate. These comparisons only change universal constants.

The upper exponent matches the lower one up to log (d) when (p\ge2r). At (2\le p<2r), it is (1/2-1/(2r)), larger than the target exponent (1/2-1/p); a fixed power of dimension remains. For example, (r=3,p=2) yields a dimension-free lower exponent but an upper (d^{1/3}\log d) factor. This is not a proof of C120.

The proof behind the tensor estimates passes through Gaussian process covering numbers and Dudley’s entropy integral; it derives a variance-profile result before reducing to the type-2 constant. The explicit lower construction is in W12-002 PDF pp. 39–40. W12-003 instead uses a PAC-Bayesian bound in terms of contraction/Frobenius variance parameters. It removes log (d) from one BGJ variance term, but its mixed terms must still be compared with the desired squared injective-norm sum.

### Norm and model checks

- The full and diagonal norms differ for (p>2), even for a symmetric matrix regarded as an order-2 tensor. W12-002 gives a polarization factor depending only on (r); see the exact (2\times2), (p=4) check in `../evidence/W12/checks/norms_lp-proof.md` (workspace relative path: `probability-skills-20261113/evidence/W12/checks/norms_lp-proof.md`).
- Only when (r=p=2) is the full matrix injective norm the Euclidean operator/spectral norm; for symmetric matrices the diagonal quadratic norm equals it by the spectral theorem.
- Independent-entry tensor results (for example W12-006) have extra independence structure and do not automatically cover an arbitrary correlated Gaussian series.

## 2. Matrix concentration as a separate special case

For a self-adjoint Gaussian matrix series (X=\sum_i g_iA_i), noncommutative Khintchine gives a spectral-norm scale controlled by
\(\|\sum_i A_i^2\|_{\mathrm{op}}^{1/2}\) and typically a √(log (d)) factor (W12-002 Remark 1.3; W12-015 Theorem 1.2). For rectangular matrices use the maximum of row and column square sums. Do not drop one of them without symmetry/self-adjointness.

Tropp’s matrix Freedman theorem (W12-014, Theorem 1.2) assumes a self-adjoint matrix martingale, a one-sided increment bound (\lambda_{\max}(X_k)\le R), and predictable quadratic variation (\sum_j\mathbb E_{j-1}X_j^2). Its conclusion is a largest-eigenvalue tail bound. Rectangular versions need self-adjoint dilation and both row/column predictable variations. These hypotheses do not become tensor-type hypotheses after flattening.

For independent self-adjoint summands, Brailovskaya–van Handel (W12-011, Theorem 2.6) compares the spectra of (X) and its covariance-matched Gaussian model (G) in Hausdorff distance, with error terms involving  \(\sigma_*(X),\sigma(X),R(X)\). Their Theorem 2.16 instead gives a one-sided spectral-set inclusion of (X) near the covariance-matched free model (X_{\rm free}); do not call that a Hausdorff bound. Latała–van Handel–Youssef (W12-012, Theorem 1.1) give two-sided estimates for heterogeneous independent-entry Gaussian matrices, with a row-variance term and a row-max term; its operator-norm expression also uses the rearranged row maxima (b^*_{ij}\sqrt{\log i}). These are matrix-model estimates, not type-2 bounds for arbitrary tensor families.

For a continuous matrix Brownian stochastic integral (X_t=\int_0^t\sum_iH_{i,s}\,dB_s^i) with symmetric progressively measurable integrands, Maitre (W12-027, Theorem 1.1) proves  \((\mathbb E\sup_{s\le t}\|X_s\|^p)^{1/p}\le C\sqrt{p+\log n}(\mathbb E\|\langle X\rangle_t\|^{p/2})^{1/p}\), for integer (p\ge1), under the stated trace-local-integrability condition. Theorem 1.4 instead states \(\mathbb E\|X_t\|_{S_{2p}}^2\le(2p-1)\mathbb E\int_0^t\|\sum_iH_{i,s}^2\|_{S_p}\,ds\); its left side is a second moment and its integrand has no extra p-th power. This is not a norm of the integrated quadratic variation. The rectangular version requires both row and column quadratic variations. This continuous Brownian theorem does not automatically cover arbitrary discrete or von Neumann-algebra martingales.

The free-probability refinement W12-009 depends on covariance information \(v(X)\) in addition to the matrix variance. Its Theorem 2.1 is a one-sided inclusion \(\operatorname{sp}(X)\subseteq\operatorname{sp}(X_{\rm free})+[-\varepsilon,\varepsilon]\); it does not give a two-sided spectral Hausdorff bound. Theorem 2.7 separately compares normalized Schatten moments in both directions. W12-010 Theorem 2.2 is a different paper's two-sided spectral Hausdorff result with separate assumptions. All remain matrix/operator-norm results; the spectral norm is the Euclidean matrix operator norm, not a general tensor injective norm.

W12-007 is a product-of-Euclidean-spheres covering bound from fixed-tuple subgaussian tails. W12-008 gives concentration only for simple product tensors whose factors and coordinates satisfy its independence hypotheses; it explicitly does not handle symmetric powers \(x^{\otimes d}\). These sources do not prove the Banach type-2 claim in C120.

## 3. Wishart principal-minor statements (C205/C206)

Fix (X\sim W_p(\alpha,\Sigma)), (\alpha>p-1), Σ positive definite, and disjoint diagonal blocks (X_{ii}) with positive integer sizes (p_i), Σ(p_i=p).

- **C205** asks whether for all ν(_i\ge0), (\mathbb E\prod_i\det(X_{ii})^{\nu_i}\ge\prod_i\mathbb E\det(X_{ii})^{\nu_i}). W12-028 Conjecture 1.1 (PDF p. 5) says (d=2) is known. W12-029 gives an explicit two-minor formula and stronger two-block quantitative inequality.
- **C206** asks a separate lower-orthant inequality for the events (\det(X_{ii})\le t_i) split at (k); W12-028 Conjecture 3.8 (PDF p. 10). Do not derive it from C205. The indicator of a determinant sublevel set is not automatically in the completely-monotone-function class used by the paper’s proved Laplace-order inequalities.
- W12-030 studies the *traces* of diagonal Wishart blocks. Its Conjecture 1 (PDF p. 3) concerns products of powers of those traces; its proved Theorem 1 covers completely monotone functions of trace-Wishart coordinates. These are neighboring trace statements, not determinant moments or determinant lower-orthant events.
- W12-031 Theorem 3.1 is stated on the original PDF p. 4 and proved on pp. 4–5. It gives a finite recursion for joint moments with **nonnegative integer** powers, any finite number of blocks, arbitrary α(>p-1), and arbitrary positive-definite Σ. The Wishart Stein operator lowers polynomial degree. The theorem computes the moment; it neither proves C205’s sign inequality nor covers arbitrary real powers. For noninteger powers the recursion no longer terminates as a polynomial (Remark 3.2, PDF p. 6).
- The [exact polynomial moment tool](wishart-polynomial-moments.md) provides an independent entry-moment recurrence for finite integer powers, including the nonsingular rational-degrees-of-freedom case. Its proof uses Gaussian integration by parts and polynomial continuation, which avoids a dependency on the full Wishart Stein characterization.
- W12-032's title, authors, abstract, v1 designation, page count and hash match the official arXiv abstract record and v1 PDF, checked by D03. The theorem read locally concerns positive absolute powers of jointly Gaussian scalar coordinates. A Wishart block determinant is a nonlinear function of Gaussian data, so this scalar-coordinate statement does not prove C205; it also says nothing about C206's determinant lower-orthant event.

C205 and C206 are formal120 records with display IDs C38 and C39, respectively; they are distinct Wishart claims. The B171 and B172 labels belong to a separate isolated dossier of historical noncommutative-Orlicz endpoint clues, not to formal120. Do not use their numbering or martingale statements as evidence for either Wishart claim.

## 4. Noncommutative martingale and Orlicz interfaces

In the tracial von Neumann algebra setting, Pisier–Xu (W12-018, Theorem 2.1) give the row/column square-function equivalence for \(2\le p<\infty\); for \(1<p<2\) an infimum over decompositions of martingale difference sequences is needed. Junge–Xu (W12-020) also prove independent-sum Rosenthal estimates with this same maximum/infimum split and, for \(p>2\), an \(L_p(\ell_\infty)\) maximal diagonal variant. Junge (W12-019) proves the dual positive-sequence Doob inequality and an \(L_p\) maximal factorization for \(p>1\). Neither result is a cross-2 Orlicz modular theorem. In Randrianantoanina–Wu (W12-021), Theorem 4.4 for \(2<p_\Phi\le q_\Phi<\infty\) has diagonal term \(\sum_n\tau\Phi(|dx_n|)\), not \(\sup_n\tau\Phi(|dx_n|)\); Problem 6.2 on physical p. 30 explicitly discusses replacing that sum with a noncommutative \(\Phi\)-moment maximal term. The square-function form changes at 2.

Cadilhac (W12-025, Theorem 3.1) obtains one row/column decomposition controlling the two (K_t(\cdot,p,\infty)) functionals for every (t\ge0), assuming orthonormal coefficients and a lower Khintchine estimate at some (p\in(0,1]\). Its Theorem 5.1 also constructs a single decomposition of a finite bounded noncommutative martingale that satisfies the strong (L_p) row/column estimate for every (p>1). These K-functional and strong-(L_p) statements are not the specific weak-Φ tail modular in B171 or the cross-2 Φ-moment inequality in B172.

Bekjan–Chen–Liu–Jiao (W12-023) prove weak-Φ moment martingale-transform/BDG estimates under their weak-Orlicz hypotheses. Such estimates are not the same as B171’s one decomposition working for every threshold. Bekjan–Chen (W12-024, PDF p. 15, Remarks 6.1–6.2) record B171 and B172 as historical questions:

- B171 seeks (x=y+z) with a row/column weak-Φ tail bound holding simultaneously for every (t>0).
- B172 asks for the upper Burkholder Φ-moment inequality across (1<p_\Phi\le q_\Phi<\infty), beyond the theorem’s index ranges wholly below or wholly above 2.

Interpolation of Orlicz norms does not automatically preserve a modular inequality for the same Φ. We did not exhaustively audit post-2015 endpoint literature; describe these as leads until that audit is performed.

