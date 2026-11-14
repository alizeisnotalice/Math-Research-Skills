> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-033 — Stability of twisted states in the continuum Kuramoto model

## Identity and reading evidence

- **Mother mirror status:** R02 final helper-stage passed; mother hash binding pending; no quota increment.
- **Read file:** `../pdfs/PGEL-033.pdf`
- **Exact local version:** arXiv:1606.07857v1, 25 June 2016; 18 physical pages; SHA-256 `920906a63714c95e17b8fcd3182e489f9fca2ac09ccf1c1ead37715e0e64a5bc`.
- **Metadata:** The local first page and official arXiv record agree on title/authors/version. The associated journal article is SIAM Journal on Applied Dynamical Systems 16(1) (2017), DOI 10.1137/16M1059175; the read PDF is the arXiv v1 author version. No equivalence with a later version is asserted.
- **Reading status:** Complete physical PDF pp. 1–18, including proofs, application, conclusion, and references. Statements and key formulas were checked against rendered pp. 3–5, 8–10, and 14–16. For this narrow revision, the unchanged local PDF was rechecked by SHA-256, and rendered source pages p. 3, pp. 8–9, and pp. 14–16 were visually checked again. No additional full-read claim is made.

## Continuum model and Theorem 1

The scalar phase field is 1-periodic in $x\in\mathbb T=\mathbb R/\mathbb Z$ and obeys
\[
\partial_tu(x,t)=\int_{\mathbb T}K(y-x)\sin\bigl(2\pi(u(y,t)-u(x,t))\bigr)\,dy.
\]
Assume $K\in L^2_{\rm per}$ is even. The continuous $q$-twisted steady state is $u^{(q,c)}(x)=(qx+c)\bmod 1$, for $q\in\mathbb Z$ and $c\in\mathbb R$. This is a continuum equation, not a finite-graph theorem.

For $m\in\mathbb Z$, define
\[
\widetilde K(m)=\int_{\mathbb T}K(x)\cos(2\pi mx)\,dx,\qquad
\lambda(q,m)=\widetilde K(m+q)-2\widetilde K(q)+\widetilde K(q-m).
\]
The source's condition (1.8), PDF p. 3, is: for fixed $q$, there is $\lambda_q<0$ such that $\lambda(q,m)\le\lambda_q$ for every positive integer $m$. Since $K$ is real and even, negative Fourier modes have the same real eigenvalues. This is a uniform strict gap over every nonzero mode, not a finite-mode check.

**Theorem 1 (PDF p. 3).** If $K$ is even in $L^2_{\rm per}$ and (1.8) holds, then for $X=H^1_{\rm per}$ or $BV_{\rm per}$ there are $\delta,b,C>0$ such that, with
\[
\mu=\int_{\mathbb T}(u_0(y)-u^{(q,c)}(y))\,dy,
\]
the condition $\|u_0-\mu-u^{(q,c)}\|_X\le\delta$ implies
\[
\sup_{t\ge0}e^{bt}\|u(\cdot,t)-\mu-u^{(q,c)}(\cdot)\|_X
\le C\|u_0-\mu-u^{(q,c)}\|_X.
\]
This is local exponential nonlinear stability modulo the conserved mean/phase shift, not global attraction.

## Linearization and exact generator clock

Writing $u=u^{(q,c)}+\eta$, direct differentiation of the displayed equation—not the intermediate Fourier notation on pp. 8–9—gives
\[
(L\xi)(x)=2\pi\int_{\mathbb T}K(z)\cos(2\pi qz)\,[\xi(x+z)-\xi(x)]\,dz.
\]
For the mode $e^{2\pi imx}$, evenness of $K$ gives
\[
\int K(z)\cos(2\pi qz)\cos(2\pi mz)\,dz
=\tfrac12\bigl(\widetilde K(m+q)+\widetilde K(q-m)\bigr),
\]
so the **actual generator multiplier** is
\[
\boxed{\;\pi[\widetilde K(m+q)-2\widetilde K(q)+\widetilde K(q-m)]
=\pi\lambda(q,m).\;}
\]
Equivalently, with $K^{(q)}(z)=2\pi K(z)\cos(2\pi qz)$, the consistent loss scalar is $\gamma_q=2\pi\widetilde K(q)$, while $\widehat K^{(q)}(m)=\pi[\widetilde K(m+q)+\widetilde K(q-m)]$; thus the mode multiplier is $\widehat K^{(q)}(m)-\gamma_q=\pi\lambda(q,m)$.
The sign-gap criterion (1.8) is unchanged, but the exact exponential clock is scaled by $\pi$: in $H^1_{\rm per,0}$ the direct Fourier semigroup bound is $\|e^{tL}\|\le e^{\pi\lambda_qt}$; the source's $BV$ convolution/variation argument, with the directly derived multiplier, gives any rate $b'<-\pi\lambda_q$. For example, $K\equiv1$, $q=0$, $m=1$ gives source sign symbol $\lambda=-2$, while the actual generator multiplier is $-2\pi$.

The source's intermediate notation is inconsistent: on p. 8 it defines $K^{(q)}(x)=2\pi K(x)\cos(2\pi qx)$, but prints $\gamma=2\pi\int K(y)\cos(2\pi y)\,dy$, omitting $q$; p. 9 then uses $2\pi\widehat K^{(q)}(k)-\gamma$ as the multiplier. These literal displays do not reproduce the directly derived multiplier above under the stated model and Fourier convention. Keep the source's sign criterion separate from this exact clock calculation; do not transfer its displayed intermediate rate as an exact decay exponent.

## Proof mechanism for Theorem 1

1. Lemma 3 (PDF pp. 6, 13) proves smoothness of the perturbation vector field on either Banach algebra $H^1_{\rm per}$ or $BV_{\rm per}$, using sine/cosine substitution, convolution by $L^2$ kernels, and multiplication estimates.
2. Evenness of $K$ and oddness of sine imply conservation of the mean perturbation (Lemma 4, PDF pp. 6–7). Subtract this neutral constant mode and work on the closed mean-zero subspace.
3. The direct Fourier calculation above diagonalizes the linearization, with multipliers $\pi\lambda(q,m)$. Condition (1.8) supplies a uniform negative gap; the positive scalar $\pi$ preserves the gap sign and scales its rate.
4. In $H^1_{\rm per,0}$, Parseval gives the semigroup bound. In $BV_{\rm per,0}$, the source does not invoke a general bounded Fourier-multiplier theorem; it writes the semigroup as a scalar exponential plus convolution with an $L^2$ kernel and applies a variation estimate (PDF pp. 9–10).
5. The nonlinear remainder $N=\Phi-L$ has $N(0)=N'(0)=0$. A local Lipschitz bound on $N'$ yields the quadratic difference estimate required by the abstract contraction/variation-of-constants theorem (Theorem 2, PDF pp. 4–6).

## Theorem 7: literal statement, scope finding, and retained route

For the circular kernel (PDF pp. 13–16),
\[
K_{r,p}(x)=(1-2p)\mathbf1_{(-r,r)}(x)+p\mathbf1_{(-1/2,1/2)}(x),
\qquad 0<r<1/2,\quad 0\le p<1/2.
\]
The literal statement on PDF p. 14 is:

> (a) $u^{(0)}$ is stable for every $r\in(0,1/2)$ and $p\in[0,1/2)$.
> (b) For each $q\in\mathbb N$, there exist $r_q,p_q\in(0,1/2)$ such that $u^{(q)}$ is a stable steady state for every $r\in(0,r_q)$ and $p\in[0,p_q)$.

For $p=0$, the source obtains $\widetilde K_r(m)=2r f(2\pi mr)$, $f(x)=\sin(x)/x$, and
\[
\lambda(q,m)=2r\,g(2\pi mr,2\pi qr),\qquad
g(x,y)=f(y+x)-2f(y)+f(y-x).
\]
Lemma 8 (PDF pp. 14–16) proves negativity for the all-mode spectrum at fixed $q$ when $r$ is sufficiently small. For each such **fixed** $r$, the p. 15 proof has a gap $\lambda_q(r)<0$, then obtains a sufficient small-$p$ condition
\[
0\le p<\frac{-\lambda_q(r)}{2(1-2\lambda_q(r))}.
\]
This threshold depends on the fixed-$r$ gap. It supports a conditional route: fix sufficiently small $r$, then take $p$ sufficiently small depending on that $r$, and verify the full all-mode strict gap. It does not supply one positive $p_q$ valid uniformly over every $0<r<r_q$.

There is an exact obstruction to such a uniform rectangle for the strict-gap / Theorem 1 exponential-stability use. At the allowed mode $m=q\ge1$, direct substitution into the symbol gives
\[
\lambda(q,q;r,p)=p+(1-2p)\left[2r-\frac{2\sin(2\pi qr)}{\pi q}
+\frac{\sin(4\pi qr)}{2\pi q}\right].
\]
Equivalently, the bracket is
\[
\int_{-r}^{r}\left[\cos(4\pi qz)-2\cos(2\pi qz)+1\right]dz.
\]
With $a=2\pi qz$, the integrand $2\cos(a)(\cos(a)-1)\ge-a^2$ for all real $a$: it is nonnegative if $\cos(a)<0$; otherwise use $\cos(a)\le1$ and $2(\cos(a)-1)\ge-a^2$. Therefore, for $0\le p<1/2$,
\[
\lambda(q,q;r,p)\ge p-\frac{8\pi^2q^2}{3}r^3.
\]
In particular, for every fixed $p>0$, $\lambda(q,q;r,p)\to p>0$ as $r\downarrow0$. Given any proposed $r_q,p_q>0$, take $p_* = \min(p_q/2,1/4)>0$, then choose
\[
0<r<\min\left(r_q,\left(\frac{3p_*}{16\pi^2q^2}\right)^{1/3}\right).
\]
Then $p_*<p_q$ and $\lambda(q,q;r,p_*)>p_*/2>0$. Thus the literal uniform rectangle cannot guarantee the source's all-mode strict negative gap. For the concrete admissible values $q=1,r=p=1/1000$, $\pi^2<10$ gives the strict rational bound
\[
\lambda(1,1;1/1000,1/1000)>\frac{37499}{37500000}>0.
\]
The exact source-based bound and a finite MATLAB numerical sanity check are recorded in `../math/pgel_l10_b9_verify_pgel033_revision.m` and `../math/pgel_l10_b9_revision_results.txt`; the floating-point values are diagnostic only. The independent neutral review's symbolic check is `../../audit/review-index.json`.

A positive generator multiplier $\pi\lambda(q,q;r,p)>0$ rules out the **Theorem 1 type local exponential estimate** at these parameters: differentiability of the flow at the equilibrium and division of the estimate for initial data $\varepsilon\cos(2\pi qx)$ by $\varepsilon$, followed by $\varepsilon\to0$ at fixed time, would force $e^{at}\le C e^{-bt}$ for all $t\ge0$, with $a>0$, which is impossible. This adjudicates the uniform strict-gap/exponential-stability route, not every possible meaning of the unqualified word “stable.” It does not refute all of Theorem 7, every nonlinear stability notion, or any finite-graph theorem.

Theorem 7(a) remains available: the direct corrected symbol for $q=0,m>0$ is
\[
\lambda(0,m;r,p)=(1-2p)\lambda(0,m;r,0)-2p,
\]
so the $p=0$ strict negativity from the fixed-$r$ argument remains strict. Theorem 1 itself is retained under its stated all-nonzero-mode strict-gap hypothesis, using the corrected generator clock. For $q>0$, only the fixed-$r$, then $p=p(r)$-small route with a full strict-gap check is retained; no repaired uniform theorem is asserted.

## Separate localized source discrepancy: equation (4.5), PDF p. 15

This is independent of the uniform-rectangle issue. The rendered source prints
\[
\lambda(q,m;p)=(1-2p)\lambda(q,m)+p\,\delta_{q,0}
\tag{printed (4.5)}
\]
but the following inequality uses $p\delta_{m,q}$. Directly applying the same page's kernel Fourier coefficients
\[
\widetilde K_{r,p}(k)=(1-2p)\widetilde K_r(k)+p\delta_{k,0}
\]
gives
\[
\lambda(q,m;p)=(1-2p)\lambda(q,m;0)
+p\bigl(\delta_{m+q,0}-2\delta_{q,0}+\delta_{q-m,0}\bigr).
\]
For positive $q,m$, this is $(1-2p)\lambda(q,m;0)+p\delta_{m,q}$; for $q=0,m>0$, it is $(1-2p)\lambda(0,m;0)-2p$. This localized source formula discrepancy is recorded separately and is not used as the proof of the uniform-rectangle obstruction.

## Transfer limits and verification

- Theorem 1 requires an even $L^2$ periodic kernel, the continuum equation, a fixed integer twist, and a uniform strict gap over all nonzero Fourier modes. Use the directly derived generator multiplier $\pi\lambda$ for clock-dependent rates.
- Theorem 7 is a continuum-kernel argument. Finite Fourier checks do not prove its infinite-mode premise, and no finite-$n$ probability or signed-graph statement follows.
- For positive $q$, do not use Theorem 7(b)'s literal uniform $(r,p)$ rectangle as a strict-gap/exponential-stability certificate. The $p=0$, fixed-$r$ route followed by a sufficiently small $p(r)$ remains a conditional source method.
- `../math/pgel_l10_b9_verification_results.txt` contains previously run MATLAB diagnostics for PGEL-030 and the equation (4.5) comparison. The revision's exact rational arithmetic check and MATLAB diagnostics are in `../math/pgel_l10_b9_revision_results.txt`; numerical output does not substitute for the analytic inequalities above.
- No C118/C106/C107 finite signed-graph interface is proved by this source.
