> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-010 — Osękowski (2013)

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/08ca510204a86c40-AEP-EXT-010.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and reading evidence

Adam Osękowski, “Maximal Weak-Type Inequality for Orthogonal Harmonic Functions and Martingales,” *Bulletin of the Polish Academy of Sciences: Mathematics* 61(3–4) (2013), 209–218, DOI [10.4064/ba61-3-3](https://doi.org/10.4064/ba61-3-3). Read the complete official IMPAN-hosted journal PDF at ../../../../../scope/source_snapshot/downloads/D04/analytic_B5/papers/impan-85763.pdf: 10 physical pages, SHA-256 4a201da5da712393496bca82f399e302264154e74d545cb4a786fd9431fcfc34. Physical pages 1–10 were read through the terminal references and author address. Text extraction is in [text/AEP-EXT-010.txt](../../../references/local-assets.md#asset-ce09ba242558); page-by-page coverage and visual checks are in [reading_coverage.json](../reading_coverage.json). The title page and terminal page, theorem formula, Poisson/Bellman construction and proof pages were checked against rendered PDF images.

## Model and exact endpoint statement

Let $D\subset\mathbb R^N$ be open and connected, $u,v$ real harmonic functions on $D$, and $\xi$ a base point. The source assumptions are
\[
|\nabla v(x)|\le|\nabla u(x)|,\qquad
\nabla u(x)\cdot\nabla v(x)=0\quad(x\in D),\qquad
u(\xi)=v(\xi)=0.
\]
For $N$-dimensional Brownian motion $B$ started at $\xi$, let $\tau$ be its first exit time from $D$, and define the one-sided and two-sided Brownian maxima
\[
u^*=\sup_{0\le t\le\tau}u(B_t),\qquad
|v|^*=\sup_{0\le t\le\tau}|v(B_t)|.
\]
**Theorem 1.2 (physical p. 3; printed p. 211).** For every $\lambda>0$,
\[
\lambda\,\mathbb P(|v|^*\ge\lambda)\le C\,\mathbb E u^*,
\]
where
\[
C=\frac{1+3^{-2}+5^{-2}+7^{-2}+\cdots}
{1-3^{-2}+5^{-2}-7^{-2}+\cdots}=1.346\ldots
\]
is Davis’ constant (eq. (1.6)); the source says the estimate is sharp. The right side uses the **one-sided** maximum $u^*$, not $\sup_{t\le\tau}|u(B_t)|$.

The auxiliary **Theorem 3.1** (physical pp. 6–9) states the probabilistic form: for continuous-path real martingales $X,Y$ with $X_0=Y_0=0$, constant bracket $[X,Y]$ (orthogonality), and $[X,X]-[Y,Y]$ nonnegative and nondecreasing,
\[
\mathbb P(|Y|^*\ge1)\le C\,\mathbb E X^*,
\qquad X^*=\sup_{t\ge0}X_t,
\]
where $X^*$ is also one-sided.

For comparison, **Theorem 1.1** (physical p. 2; printed p. 210) is a different, non-maximal harmonic-measure weak-$(1,1)$ norm statement: for the same gradient and normalization assumptions, $\|v\|_{1,\infty}\le C\|u\|_1$, where both norms take suprema over the bounded connected subdomains $D_0\Subset D$ containing $\xi$. This does not replace Theorem 1.2’s pathwise maximal event.

## Proof route and dependencies

- **Auxiliary Bellman function (Section 2, physical pp. 3–6).** On the strip $S=\mathbb R\times[-1,1]$, start with the Poisson integral
\[
W(\alpha,\beta)=\frac2{\pi^2}\int_{|t|\ge1}
\frac{\beta\log|t|}{(\alpha-t)^2+\beta^2}\,dt
\]
in the upper half-plane and transport it through
\[
\phi(x,y)=\left(-e^{\pi x/2}\sin(\pi y/2),\ e^{\pi x/2}\cos(\pi y/2)\right).
\]
Set $W(x,y)=W(\phi(x,y))$ for $|y|<1$ and $W(x,y)=x_+$ for $|y|\ge1$. Rendered Lemma 2.1 gives evenness in $y$, $W_{xx}\ge0$, $W_{yy}\le0$ inside the strip, $W(x,y)\le W(0,0)=1/(2C)$ for $x\le0$, and $W_x(0,y)=1/2$ for $|y|<1$. The identity $W(0,0)=1/(2C)$ follows from (2.6) and the odd-reciprocal-square series.
- **Martingale maximal estimate (Theorem 3.1 proof, physical pp. 6–9).** Stop $Y$ so it lies in $[-1,1]$, reduce by a stopping-at-$\varepsilon$ argument to a fixed-time estimate, and set $Z_t=(X_t,Y_t,X_t^*)$ with $X_t^*=\sup_{s\le t}X_s$. Use $U(x,y,z)=1-2C W(x-z,y)-Cz$. Itô’s formula gives the local-martingale term, the $dX^*$ term, the mixed bracket term and second-derivative bracket terms. The first has expectation zero; the $dX^*$ integrand vanishes because $X=X^*$ on its increase set and $U_z(z,y,z)=2CW_x(0,y)-C=0$; orthogonality kills the mixed term; differential subordination and the signs of $W_{xx},W_{yy}$ make the remaining second-order terms nonpositive. The source majorization $U(x,y,z)\ge1_{\{|y|\ge1\}}-Cz$ for $x\le z$, together with $\mathbb E U(Z_t)\le0$, proves the event bound.
- **Brownian representation and source sharpness claim (physical pp. 8–9).** Stopped Brownian compositions of harmonic $u,v$ are martingales; their brackets are the integrals of $|\nabla u|^2$, $|\nabla v|^2$, and $\nabla u\cdot\nabla v$, so the assumed gradient conditions give differential subordination and orthogonality. The source’s sharpness paragraph prints the closed strip $D=\mathbb R\times[-1,1]$ and asserts equality; this literal domain is not open. The legal open-domain equality example is separately derived below and is not silently attributed to the source.

## Source-text note and independent open-domain example

The source sharpness paragraph on physical p. 9 prints $D=\mathbb R\times[-1,1]$, although its standing hypothesis requires $D$ open. The closed strip as printed is not an admissible instance of that hypothesis. The following is a separately derived legal example, not a silent correction of the source text.

Take $D=\mathbb R\times(-1,1)$, $\xi=(0,0)$, and harmonic functions $u(x,y)=x$, $v(x,y)=y$, which are globally defined on $\mathbb R^2$ and hence continuously extend to the exit boundary. They satisfy the hypotheses: $u(\xi)=v(\xi)=0$, $|\nabla u|=|\nabla v|=1$, and $\nabla u\cdot\nabla v=0$. Let $\tau=\inf\{t:|B_t^{(2)}|=1\}$. Both coordinates extend continuously to $\overline D$, so evaluate the stopped process at the exit boundary by this extension; equivalently, take the same suprema as limits from $t<\tau$. Then $|v|^*=1$ almost surely. Since $\tau$ is independent of $B^{(1)}$, conditional reflection gives
\[
\mathbb E u^*=\mathbb E\sup_{s\le\tau}B_s^{(1)}=\mathbb E|B_\tau^{(1)}|.
\]
The strip-exit transform is $\mathbb E e^{i\xi B_\tau^{(1)}}=\operatorname{sech}(\xi)$, so $B_\tau^{(1)}$ has density $[2\cosh(\pi x/2)]^{-1}$. Hence
\[
\mathbb E|B_\tau^{(1)}|=\int_0^\infty\frac{x}{\cosh(\pi x/2)}\,dx=\frac{8G}{\pi^2}=C^{-1},
\]
where $G$ is Catalan’s constant and $C$ is the source’s Davis constant. This proves equality for a legal open-domain example and recovers sharpness of Theorem 1.2 within its stated open-domain class. This analytic strip argument is independent of the PDF’s closed-strip notation; the saved numerical quadrature checks only the moment identity, not the domain argument or theorem proof.
## Relevance and transfer limits

This is an auxiliary Brownian/martingale maximal weak-endpoint source. It is relevant to **C208** only as endpoint-method context; it does not give a dimension-uniform scalar Riesz-transform weak-$(1,1)$ bound. For formal **C207**, it is probability/martingale calibration only: there is no $1<p<\infty$ best vector $L^p$ constant here. Preserve the one-sided $u^*$ and the maximal versus harmonic-measure norm distinction in any reuse.

## Reading status

Complete standalone source read; no external supplement is needed. The earlier R01 finding that the printed closed-strip example does not literally meet the open-domain hypothesis is addressed by the separately attributed open-strip example above. R01 final mother30 source binding approved; this source contributes one of the 30 accepted works.
