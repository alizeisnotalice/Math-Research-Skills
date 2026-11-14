> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-009 — Osękowski (2011)

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/6488e9308fe5c77f-AEP-EXT-009.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and reading evidence

Adam Osękowski, “A Weak-Type Inequality for Orthogonal Submartingales and Subharmonic Functions,” *Bulletin of the Polish Academy of Sciences: Mathematics* 59(3) (2011), 261–274, DOI [10.4064/ba59-3-7](https://doi.org/10.4064/ba59-3-7). Read the complete official IMPAN-hosted journal PDF at ../../../../../scope/source_snapshot/downloads/D04/analytic_B5/papers/impan-85443.pdf: 14 physical pages, SHA-256 5b8d63ba6ffc16189ef9e717a333d0c5587a8a8279205db5a60e11039a0adbcc. Physical pages 1–14 were read, including acknowledgements, all references, and author address. Text extraction is in [text/AEP-EXT-009.txt](../../../references/local-assets.md#asset-3a8ed5c844e1); continuous page coverage and visual checks are in [reading_coverage.json](../reading_coverage.json). Title/author/DOI and print-page span were checked on physical p. 1; theorem, Bellman construction, stochastic proof and application pages were rendered and checked.

## Model and results

For adapted real càdlàg semimartingales $X,Y$, the paper calls $Y$ differentially subordinate to $X$ when $[X,X]-[Y,Y]$ is nonnegative and nondecreasing. It calls $X,Y$ orthogonal when $[X,Y]$ is almost surely constant. For a submartingale $X$, write its Doob–Meyer decomposition $X=X_0+M+A$ with predictable $A$; write $Y=Y_0+N+C$. Strong differential subordination requires ordinary differential subordination and a decomposition of $Y$ for which $A_t-|C|_t$ is nondecreasing, where $|C|_t$ is total variation through time $t$. The paper works with processes started at zero and defines
\[
X^*=\sup_{t\ge0}|X_t|,\qquad \|X\|_1=\sup_{t\ge0}\mathbb E|X_t|.
\]

**Theorem 1.2 (physical p. 3; printed p. 263).** If $X$ is a submartingale with $X_0=0$ and $Y$ is a semimartingale orthogonal and strongly differentially subordinate to $X$, then
\[
\mathbb P(Y^*\ge1)\le c\|X\|_1.
\]
The source states that $c$ is best possible even for the Itô processes in (1.4), but the printed sharpness construction has a stopping-domain error and the printed selector estimate needs a separate error budget. A separately attributed correction is given below; this does not make the printed construction correct as written. The paper explicitly does not know whether $c$ is optimal in the smooth-function estimate of Theorem 4.1. It gives the stronger consequence $\mathbb P(Y^*\ge1)\le c\|X_+\|_1$ in Remark 3.2 (physical p. 11). The constant is source-defined by a conformal-map/Poisson integral: $R\in(0,1)$ is the unique solution of
\[
\int_0^R\frac{\sqrt{1+s^4}}{1-s^4}\,ds=\frac{\sqrt2}{2}\int_0^1\frac{\sqrt{1-s^4}}{1+s^4}\,ds,
\]
and
\[
c=-\left[\frac1{2\pi}\int_0^{2\pi}
\frac{1-R^2}{1-2R\cos(t+\pi/4)+R^2}h(F(e^{it}))\,dt\right]^{-1}
=3.375\ldots
\]
(eqs. (2.1)–(2.2), physical pp. 4–5). Here $F(z)=\alpha\int_0^z\sqrt{1-w^4}/(1+w^4)\,dw$, with $\alpha=\sqrt{2i}\left(\int_0^1\sqrt{1-t^4}/(1+t^4)\,dt\right)^{-1}$. The map $F$ sends the unit disk conformally onto the cross-shaped $K=\{|\Re z|\le1\text{ or }|\Im z|\le1\}$; on its boundary outside the central square, $h(x,\pm1)=1-|x|$ and $h(\pm1,y)=|y|-1$.

**Theorem 4.1 (physical pp. 12–13; printed pp. 272–273).** For an open connected $D\subset\mathbb R^n$, real $C^2$ functions $u,v$, a base point $\xi$, and every $x\in D$, assume $u(\xi)=v(\xi)=0$, $u$ is subharmonic, and
\[
\nabla u\cdot\nabla v=0,\qquad |\nabla v|\le|\nabla u|,\qquad |\Delta v|\le|\Delta u|.
\]
For every bounded subdomain $D_0\Subset D$ containing $\xi$, the harmonic-measure estimate is
\[
\mu^{D_0}_\xi\{x\in\partial D_0:|v(x)|\ge1\}
\le c\int_{\partial D_0}|u(x)|\,d\mu^{D_0}_\xi(x).
\]
The source explicitly says it does not know whether $c$ is optimal for this smooth-function estimate.

## Proof route and dependencies

- **Bellman function (Theorem 2.1; physical pp. 4–9).** On the wedge $J=\{|\Im z|\le1,\ |\Im z|\le\Re z\}$ inside $K$, the source forms a harmonic function by Poisson extension of boundary data transported by $F$. Symmetry and boundary comparisons yield on $J$: $|y|-x\le U(x,y)\le\min(1-x,0)$, $U_x\pm U_y\le0$, and $U_{xx}\le0$. Extending by the stated piecewise definition gives a continuous superharmonic $U:\mathbb R^2\to\mathbb R$, nonincreasing along both diagonal directions, concave on horizontal lines, with $U(0,0)=-c^{-1}$ and $U(x,y)\ge U(0,0)1_{\{|y|<1\}}-x_+$.
- **Smoothing and stopping (proof of (1.5), physical pp. 9–11).** Radial convolution produces smooth $U^\delta$ preserving superharmonicity, diagonal monotonicity and horizontal concavity. Stop at the first time $|Y_t|\ge1+\varepsilon$ or $|X_t|\ge\ell$. Itô’s formula splits into a local-martingale term, a finite-variation term, a continuous bracket term and a jump remainder. The martingale term has mean zero after localization; strong subordination and $U_x^\delta+|U_y^\delta|\le0$ make the finite-variation contribution nonpositive; orthogonality removes the mixed bracket term and superharmonicity plus bracket domination control the remaining continuous term; horizontal concavity controls jumps. The source’s first line of (3.2) prints $+(x+\delta r)_+$, contrary to Theorem 2.1(v); the following inequality requires $-(x+\delta r)_+$. Using that sign, $-(x+\delta r)_+\ge-(x_++\delta)$ for $|r|\le1$. The majorization gives
\[
c^{-1}\mathbb P(|Y_{\tau\wedge t}|\ge1+\delta)
\le\mathbb E(X_{\tau\wedge t}^++\delta)
\le\mathbb E|X_t|+\delta.
\]
Taking limits, removing the $\ell$-stop and scaling yields Theorem 1.2.
- **Printed sharpness and its source-local defect (physical pp. 11–12).** The paper defines $J=\{(x,y):|y|\le1,\ |y|\le x\}$ and prints $\tau=\inf\{t:B_t\in\partial J\}$. Since $B_0=(0,0)\in\partial J$, this literal stopping time is $0$; the claimed Brownian phase does not occur. The final Bellman function is harmonic on $J-1$, not on $J$. The printed stopping domain therefore cannot certify the sharpness construction.
- **Independent operational correction, not attributed to the source.** Use $D=\operatorname{int}(J-1)=\{(x,y):|y|<1,\ |y|<x+1\}$ and $\tau_D=\inf\{t:B_t\notin D\}$, starting at $(0,0)\in D$. Since $D\subset\{|y|<1\}$, $\tau_D$ is bounded by $\sigma=\inf\{t:|B_t^{(2)}|=1\}$, which has an exponential tail. Thus $\mathbb E\sup_{s\le\tau_D}|B_s^{(1)}|<\infty$. Theorem 2.1 makes $U$ harmonic on $D$; its boundary values are $U(x,\pm1)=-x$ on horizontal sides ($x\ge0$) and $U(|y|-1,y)=0$ on sloping sides ($|y|\le1$). The bound $U\le0$ and $U(x,y)\ge-c^{-1}-x_+$ on $D$ give an integrable dominating variable for $U(B_{t\wedge\tau_D})$. Optional stopping therefore gives $\mathbb E U(B_{\tau_D})=U(0,0)=-c^{-1}$.
  
  Retain the source’s drift segment after exit: if $B_{\tau_D}^{(1)}<0$, run drift $(1,\operatorname{sgn}B_{\tau_D}^{(2)})$ for time $-B_{\tau_D}^{(1)}=1-|B_{\tau_D}^{(2)}|$, reaching $(0,\operatorname{sgn}B_{\tau_D}^{(2)})$; if exit is on a horizontal side, stop. Choose either sign at the probability-zero corner $B_{\tau_D}^{(2)}=0$. Up to $\tau_D$, $X,Y$ are the two independent Brownian coordinates; on the drift interval $dA=dt$ and $d|C|=dt$, so $A-|C|$ stays nondecreasing, and afterwards the pair is constant. Thus $X$ is a submartingale, $[X,X]=[Y,Y]$, $[X,Y]=0$, the pair is orthogonal and strongly differentially subordinate, and $Y^*\ge1$ almost surely. The terminal $X_\infty=B_{\tau_D}^{(1)+}$ satisfies $U(B_{\tau_D})=-X_\infty$, so $\mathbb E|X_\infty|=c^{-1}$. The base process has $M:=\sup_t\mathbb E|X_t|<\infty$ by the same Brownian maximum bound plus drift length at most $1$, and $\mathbb E|X_t|\to c^{-1}$ by dominated convergence.
  
  To complete the near-extremizer argument with two error budgets, fix $\varepsilon>0$. Choose $T$ so $\mathbb E|X_t|\le c^{-1}+\varepsilon/2$ for $t\ge T$, and set $T_j=jT$. For $j=0,\ldots,k-1$, use the corrected base pair driven by $B_t^j=0$ for $t\le T_j$ and $B_t^j=B_t-B_{T_j}$ for $t>T_j$. Select one copy by an independent uniform $J_0\in\{0,\ldots,k-1\}$ known at time zero. At any fixed time at most one copy is in its first $T$ units; earlier copies are in the tail range and later copies are zero. Therefore
  $$
  \mathbb E|X_t^{J_0}|\le \frac{k-1}{k}(c^{-1}+\varepsilon/2)+\frac{M}{k}\le c^{-1}+\varepsilon
  $$
  if $k\ge2M/\varepsilon$. Every selected copy has $\mathbb P((Y^{J_0})^*\ge1)=1$. This separately derived construction establishes sharpness for the process theorem; it does not certify the printed stopping line or the smooth-function application, whose sharpness the source leaves open.
## Relevance and transfer limits

This is an auxiliary probability representation and weak-endpoint Bellman method. For **C208**, its orthogonal martingale/harmonic-function weak-type mechanism is endpoint context only: the paper does not prove the target dimension-uniform weak-$(1,1)$ inequality for a scalar Euclidean Riesz transform. For formal **C207**, it supplies martingale endpoint calibration only; it has no $1<p<\infty$ vector $L^p$ norm theorem and does not determine the best $A_p$. Do not identify the scalar harmonic-conjugate/smooth-function statements with the Euclidean vector Riesz operator.

## Reading status

Complete standalone source read. The earlier R01 findings on the printed sharpness shift/sign and selector error budget were addressed in the current helper revision; the operational correction above remains explicitly reader-derived. R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. No separate supplement or appendix is required for this version.
