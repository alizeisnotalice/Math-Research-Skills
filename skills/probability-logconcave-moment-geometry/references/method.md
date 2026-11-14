# Method note: log-concave moments and $Z_p$ expansion

## Input normalization

Write down the dimension, law, centering/symmetry/isotropy, norm and dual norm, moment range, and target constant before using any inequality. If a result is affine-invariant, record the linear map and how it changes the norm and centroid body. Whitening a general law while leaving a requested norm unchanged is not a valid invariance argument.

For $X\sim\mu$, set
$$
h_{Z_p(\mu)}(v)=\|\langle v,X\rangle\|_p,\qquad
\sigma_{||\cdot||,X}(p)=\sup_{||v||_*\le1}\|\langle v,X\rangle\|_p.
$$
When moments are $\alpha$-regular, retain the exact convention and range from the source. For symmetric log-concave laws the standard regularity used in the cited results is $1$-regular; centered log-concave laws are $2$-regular; arbitrary log-concave laws are $3$-regular.

## Two target problems

C153 asks for a dimension-free comparison for every log-concave vector, every norm, every $p\ge1$:
$$
\|X\|_{L_p(||\cdot||)}\le C\{E||X||+\sigma_{||\cdot||,X}(p)\}.
$$
The source states this as Latała's Conjecture 12. Verify whether the cited theorem applies to arbitrary covariance and arbitrary norm. Results on $||X||_2$, finite $\ell_r$ with $C_r$, unconditional product laws, or fixed isotropic gauges leave a gap.

C154 asks for a single $\beta$ for every symmetric log-concave $\mu$, all $p\ge2$, and all Borel $A$:
$$
\mu(A+\beta Z_p(\mu))\ge\min\{1/2,e^p\mu(A)\}.
$$
The equivalent CI form is $\mu(A)\ge1/2\Rightarrow1-\mu(A+\beta Z_p(\mu))\le e^{-p}(1-\mu(A))$. Keep the shape $Z_p(\mu)$ and every-set quantifier explicit.

## Valid theorem chain currently sourced

1. If CI($\beta$) and $\alpha$-regularity are actually available, Latała–Wojtaszczyk Proposition 3.15 yields a median-centered arbitrary-norm moment deviation bound for $p\ge2$ with factor $2\alpha\beta$.
2. The independent-coordinate log-concave-tail class has convex IC with a universal constant; together with regular moments this yields a first-moment coefficient exactly $1$ for $p\ge2$. This class is much narrower than arbitrary dependent log-concave vectors.
3. For centered log-concave measures, the 2017 chapter gives only $\beta\le C\sqrt n$ in the general CI statement. Its dimension loss cannot be dropped.
4. The 2026 centroid-entropy paper gives useful gauge comparisons and, in Theorem 1.3, the arbitrary-norm estimate $\|Y\|_{L_p}\le C\bigl(n^{1/4}\sqrt{\log(en)}\log(e+\log(en))\,\mathbb E\|X\|+\sigma_p(Y)\bigr)$ under isotropic log-concave $X$, weak linear-moment domination, and $p\ge2$, where $\sigma_p(Y)=\sup_{\|t\|_*\le1}\|\langle t,Y\rangle\|_p$. The outside $C$ multiplies the entire parenthesis. This has no absolute C153 constant and is no C154 CI theorem.

## Additional checked tools and their exact limits

- **Paouris / Euclidean moments:** M0280 Theorem 1.1 is an isotropic log-concave Euclidean tail bound for $t\ge1$; Theorem 1.2 gives $\|X\|_{L_p(\ell_2)}\le C(E\|X\|_2+\sigma_{\ell_2,X}(p))$ for general log-concave $X$. It is Euclidean only. See [M0280](../evidence/W11/cards/M0280.md).
- **Order statistics:** M0274 Theorem 4 uses the positive-side count $N_X(t)=\sum_i1_{\{X_i\ge t\}}$; a modulus-count version requires applying the theorem to both $X$ and $-X$ and invoking Minkowski. M0290 Theorem 2, including $c(\alpha)=[36(5+4\alpha)(1+2\alpha)]^{-1}$, is a separate pairwise-tail-decorrelation result. M0290 Theorems 4–5 require mean-zero log-concave $X$ with uncorrelated coordinates; its general upper expectation is at $t^*(k-\frac12k^{5/6},X)$, with the subtraction inside the argument. Do not mix these sources or erase these hypotheses. See [M0274](../evidence/W11/cards/M0274.md) and [M0290](../evidence/W11/cards/M0290.md).
- **Sudakov and coordinate moments:** M0282 proves a weighted coordinate $\ell_\infty$ moment comparison for isotropic log-concave vectors and Sudakov minoration under cardinality/separation hypotheses; Theorem 3.6 requires $|T|\ge\exp(\exp(p))$, while its invariant and unconditional cases have their own stated restrictions. M0285's weak/strong moment theorem assumes independent centered coordinates with $\|X_i\|_{2q}\le\alpha\|X_i\|_q$ for every $q\ge2$. Neither is a theorem for arbitrary dependent log-concave vectors and arbitrary norms. See [M0282](../evidence/W11/cards/M0282.md) and [M0285](../evidence/W11/cards/M0285.md).
- **Convex infimum convolution:** M0322 characterizes a one-dimensional symmetric tail-ratio class and tensorizes its *convex* ICI to products, yielding $B_2+B_1$ enlargement for convex sets. In Theorem 1, (3)$\Rightarrow$(2) has $C_P=C_\tau^2/2$; Corollary 3 has exponent $-\frac18\min\{t/b,t^2/a^2\}$. This is not an ICI theorem for every dependent log-concave law and does not supply C154's $Z_p$ shape. See [M0322](../evidence/W11/cards/M0322.md).
- **A second product-space ICI framework:** M0328's $Q_\alpha/R_\alpha$ inequalities and entropy transport bound apply to product probability measures with the stated sequential-kernel measurability conditions. Keep its two costs/operators distinct; this is not a theorem for arbitrary dependent log-concave measures or C154's all-set $Z_p$ expansion. See [M0328](../evidence/W11/cards/M0328.md).
- **KLS via localization:** M0301 proves $\psi_p\le C(\operatorname{Tr}A^2)^{1/4}$ for log-concave densities with covariance $A$, hence $O(n^{1/4})$ for isotropic laws. This is a dimension-dependent isoperimetric/spectral statement, not an arbitrary-norm moment estimate or a $Z_p$ enlargement theorem. See [M0301](../evidence/W11/cards/M0301.md).
- **KLS and deviations:** M0304 gives a conditional implication from certain norm LDPs to failure of KLS and MDPs for Euclidean projections of $\ell_p^n$ balls. Retain the sequence, speed, $p$ range, projection model and isotropy assumptions. The preprint's piecewise critical-scale formulas use $m_p$ without defining it in that notation; do not silently replace it by $M_p(2)$. These asymptotic results do not settle C153/C154. See [M0304](../evidence/W11/cards/M0304.md).
- **Convex-body perturbations:** M0270 gives $d(K,T)<1+\varepsilon$ and $L_T<c/\sqrt{\varepsilon}$ for a nearby convex body, then derives an $O(n^{1/4})$ slicing bound. This concerns isotropic constants; it does not establish a dimension-free moment theorem for a fixed law. Its local author manuscript is complete, while publisher-version equivalence remains unverified. See [M0270](../evidence/W11/cards/M0270.md).
- **Information density:** M0332 proves exponential concentration of $-\log f(X)$ around differential entropy for log-concave densities. This is not a norm tail bound and does not imply C153 or C154. See [M0332](../evidence/W11/cards/M0332.md).
- **Entropy and spectral gap:** M0333 gives a Shannon–Stam entropy jump for isotropic log-concave laws under an assumed spectral gap and derives an isotropic-constant bound. The law-specific Poincaré constant remains in the estimate; it does not imply arbitrary-norm C153 or C154. See [M0333](../evidence/W11/cards/M0333.md).

## Batch 7 source interfaces and formula-scale correction

- **Interpolated Poincaré/log-Sobolev inequalities:** M0261 tensorizes an assumed $I(a)$ inequality and derives Euclidean Lipschitz concentration with tail exponent $2/(2-a)$. The hypothesis is an inequality for every nonnegative smooth test function and every $p\in[1,2)$; its generalized-Gaussian theorem is a separate product-law result. Do not treat this as a universal functional inequality for all log-concave laws or an arbitrary-norm bound. The local 23-page author manuscript is a contribution published in LNM 1745 (2000), pp. 147–168; page equivalence is not claimed. See [M0261](../evidence/W11/cards/M0261.md).
- **Log-concave matrix rows:** M0272 Theorem 6 assumes independent isotropic log-concave rows, $1\le n\le N$, $k\le n$, $m\le N$, and $t\ge1$; it controls the sparse-submatrix parameter $\Gamma_{k,m}$ with $\lambda=\sqrt{\log\log(3m)}\sqrt m\log(eN/m)+\sqrt k\log(en/k)$. Theorem 7 also assumes $1\le n\le N$ and gives a sparse RIP regime with $m\log^2(2N/m)\log\log(3m)\le c(\theta)n$. This is a row-independent sparse-matrix statement, not a general norm-moment comparison. The complete local seven-page author manuscript differs in pagination from the four-page journal contribution; no equivalence claim is made. See [M0272](../evidence/W11/cards/M0272.md).
- **KLS lower bound:** M0291 Theorem 1 gives $\psi(p)\ge([c\ell(\log d+1)]^{\ell/2}d^{16/\ell}\sqrt{\rho(p)})^{-1}$ for every log-concave density on $\mathbb R^d$ and integer $\ell\ge1$, where $\rho(p)$ is the covariance spectral norm. It is a dimension-dependent Cheeger bound from stochastic localization, not dimension-free KLS or arbitrary-norm C153. The exponent $16/\ell$ was visually checked on a fresh render of published PDF p. 4 (`evidence/W11/notes/visual-audit/M0291-pdf4-batch8.png`). See [M0291](../evidence/W11/cards/M0291.md).
- **Weibull Chevet and submatrix norms:** M0295 Theorem 1.1 is a two-sided expectation comparison for independent symmetric Weibull entries with exact tail $e^{-t^r}$, $r\in[1,2]$, and bounded index sets. Its log-concave matrix corollary requires an isotropic unconditional matrix law; maximal submatrix results retain the stated entry assumptions. It does not extend to every dependent log-concave vector/norm. See [M0295](../evidence/W11/cards/M0295.md).
- **Orlicz centroid geometry:** M0331 minimizes $|\Gamma_\phi K|/|K|$ over convex bodies containing the origin in their interior, with equality exactly at origin-centered ellipsoids. Its $\Gamma_\phi K$ is formed from normalized uniform volume on a body and is not the probabilistic $Z_p(\mu)$ moment body; §4's star-body extension remains open in this paper. See [M0331](../evidence/W11/cards/M0331.md).
- **M0340 conditional transport scale (corrected):** On physical PDF p. 9, (4.2) states $1/(3\operatorname{Var}(X))\le\lambda_\gamma^2\le2/\operatorname{Var}(X)$. Equation (4.3) sets $\lambda_i^2(x_{<i})=1/[3\operatorname{Var}(X_i\mid X_{<i}=x_{<i})]$, so the cost uses the normalized displacement $\lambda_i(S(x))(x_i-y_i)$ with $\lambda_i=1/\sqrt{3\operatorname{Var}(X_i\mid X_{<i})}$. Do not replace this reciprocal scale by variance/3 or multiply displacement by a standard-deviation weight. The saved Laplace computation is only a one-example scale check. See [M0340](../evidence/W11/cards/M0340.md) and `evidence/W11/notes/M0340-scale-check-batch7.txt`.

R06 has accepted 31 complete source readings and the scoped mathematical uses described here. Five partial readings are not counted as completed sources. Reader-side `review_status` fields remain separate declarations; consult the [independent audit](../evidence/review/review.json) for source-level verdicts.

## Certificate discipline

- Label the statement as theorem, conjecture, corollary, or numerical check exactly as the source does.
- Copy the theorem number, PDF/printed page, constants and all assumptions into the working proof.
- If using transport or infimum convolution, establish whether the source proves ordinary ICI or only convex ICI and whether tensorization, symmetry, or one-dimensional log-concave tails are required.
- For a numerical example, derive exact moments where possible, state the norm/dual norm and the scope, and do not extrapolate from finite dimension.

## Batch 5 source interfaces

- **Convex-measure Euclidean moments:** M0276 Theorem 4.2 reduces the Euclidean strong/weak moment estimate to its H(p,λ) gauge condition; Theorem 5.1 supplies that condition for centered (−1/r)-concave laws with 0<p<r. Corollary 5.3 gives the universal Euclidean log-concave estimate. Its negative-moment/small-ball results have additional centering, dimension and p-range assumptions. None asserts C153 for arbitrary norms. See [M0276](../evidence/W11/cards/M0276.md).
- **Log-concave projections and matrices:** M0278 Theorem 3.1 is explicitly Euclidean; Theorem 3.2 uses a one-sided coordinate count, and Theorem 5.1 assumes independent isotropic log-concave rows. Do not use it as an arbitrary-norm comparison. See [M0278](../evidence/W11/cards/M0278.md).
- **Centroid-body geometry:** M0284 assumes isotropic log-concavity and proves inradius only after choosing a proportional-dimensional projection; its covering and mean-norm estimates retain q, n and isotropic-constant ranges. That projection inclusion is not C154's enlargement for every Borel set. See [M0284](../evidence/W11/cards/M0284.md).
- **Zp norm of a random vector:** M0287's general bound remains an open problem in the paper. Theorem 4 and Corollary 6 prove the expected scale only for unconditional log-concave vectors; separate entropy propositions require semiconvex density or an assumed L2-Sudakov bound. See [M0287](../evidence/W11/cards/M0287.md).
- **Transport remainder:** M0321 Proposition 1 uses the asymmetric Bregman-type cost c_V; Theorem 3 adds a Cheeger-scaled min(t²,t) remainder under a same-barycenter constraint, and Proposition 5 has its own vector-centering hypothesis. This is not an all-set Zp enlargement theorem. See [M0321](../evidence/W11/cards/M0321.md).
- **M0304 version-specific issue:** The official Zaragoza PostPrint page 4 reproduces the arXiv v1 Theorem B(b1) display. The printed expression is negative at p=1, x=1 under the source's own M_p(2) definition; isolate that subclaim and do not silently repair it or infer that all of Theorem B is false. Theorems A and C are separate statements. See [M0304](../evidence/W11/cards/M0304.md) and the saved symbolic check.


## Batch 6 source interfaces

- **Sparse matrix norms:** M0278 Theorem 5.1 assumes independent isotropic log-concave rows and uses
  $\lambda_{k,m}=\sqrt{\log\log(3m)}\sqrt m\log(e\max\{N,n\}/m)+\sqrt k\log(en/k)$.
  The ordinary logarithmic factors in both summands are outside the square roots; only the displayed $\log\log(3m)$ factor is under its square root. This is a matrix supremum bound under the paper's stated dimensions and $t\ge1$, not an arbitrary-norm moment estimate. See [M0278](../evidence/W11/cards/M0278.md).
- **$Z_p$-norm covering:** M0287 Proposition 14 states $N(M_p(X),(eC_X/\sqrt p)B_2^n)\le e^p$ for $p\ge2$ when $C_X$ is an $L_2$-Sudakov minoration constant. Keep the factor $p^{-1/2}$ and that premise; it is distinct from the unconditional-vector moment theorem. See [M0287](../evidence/W11/cards/M0287.md).
- **Transport and weighted Poincaré:** M0340's weighted inequality applies to sequentially recentered coordinates $\bar X_i=X_i-\mathbb E[X_i\mid X_{<i}]$; applying it directly to $X$ requires $X=\bar X$ (for example, centered independent coordinates or log-concave martingale differences). Its transport proof uses a triangular Knothe map and a conditional one-dimensional cost. M0342 instead bounds Brenier maps from Gaussian measure to centered isotropic log-concave targets, with stronger Hessian assumptions for derivative estimates. Neither proves C154's all-Borel-set $Z_p$ enlargement. See [M0340](../evidence/W11/cards/M0340.md) and [M0342](../evidence/W11/cards/M0342.md).
- **Entropy inequalities:** M0339 proves a reverse entropy-power inequality for symmetric log-concave vectors with exponent $\kappa=1/5$, yielding a seminorm $e^{S(\langle v,X\rangle)/5}$; it leaves the full entropy norm as a conjecture. M0343's quantitative entropy and information jumps require independent isotropic log-concave inputs and retain the larger Poincaré constant in the denominator. Neither is a norm-moment comparison. See [M0339](../evidence/W11/cards/M0339.md) and [M0343](../evidence/W11/cards/M0343.md).
- **General $L_p$ centroid bodies:** M0341 compares quermassintegrals of asymmetric centroid bodies of star bodies under $L_p$ Brunn–Minkowski operations. Its $\Gamma_p^\tau K$ is a uniform-volume geometric construction, not the probabilistic $Z_p(\mu)$ body. See [M0341](../evidence/W11/cards/M0341.md).
- **Version boundaries:** The local M0284 file is a 29-page author-hosted manuscript, while the journal record has 25 printed pages; equivalence and page mapping are unverified. M0340's 19-page arXiv v1 and M0342's 13-page arXiv v1 were read in full; their respective journal records have 25 and 16 printed pages, and equivalence was not asserted. See the source/version statements in [M0284](../evidence/W11/cards/M0284.md), [M0340](../evidence/W11/cards/M0340.md), and [M0342](../evidence/W11/cards/M0342.md).
