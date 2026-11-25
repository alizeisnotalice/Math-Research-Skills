# Finite lazy reversible chains: full mixing and observable averages

Use this branch for a **finite**, row-stochastic kernel $P$ with a full-support stationary probability $\pi$. Fix the convention

\[
 \mathcal E_P(h,h)=\langle h,(I-P)h\rangle_\pi
 =\frac12\sum_{x,y}\pi(x)P(x,y)(h(x)-h(y))^2,
\qquad
 \operatorname{Var}_\pi h=\|h-\pi h\|_{L^2(\pi)}^2.
\]

Check detailed balance and the update clock first. The bounds below are discrete-time bounds for this exact $P$, not statements about a generator or an arbitrary nonreversible chain.

## Route A — full-chain Poincaré/conductance to total-variation mixing

Assume that $P$ is finite, irreducible, reversible, and lazy in the pointwise sense
$P(x,x)\geq\tfrac12$ for every state. If, for every real $h$,

\[
 \operatorname{Var}_\pi h\leq K\mathcal E_P(h,h),\qquad K\geq1,
\tag{A1}
\]

then the nonconstant spectrum is in $[0,1-1/K]$, and

\[
 \|P^t(x,\cdot)-\pi\|_{\rm TV}
 \leq \tfrac12\sqrt{\pi(x)^{-1}-1}\,e^{-t/K}
 \leq \pi_{\min}^{-1}e^{-t/K}.
\tag{A2}
\]

The first inequality is normally preferable; the second is a deliberately looser uniform form. Irreducibility supplies full support and removes extra eigenvalue $1$. Laziness is essential for this powers-of-$P$ conclusion: Poincaré alone controls $1-\lambda_2$, not negative eigenvalues or periodic oscillation.

For a cut certificate, set
$Q(A,A^c)=\sum_{x\in A,y\notin A}\pi(x)P(x,y)$. If every nonempty proper $A$ satisfies

\[
 Q(A,A^c)\geq\kappa\min\{\pi(A),\pi(A^c)\},
\tag{A3}
\]

then the coarea/Cauchy--Schwarz argument gives (A1) with $K=2/\kappa^2$. This supplies a sufficient, generally nonsharp, mixing bound after the separate laziness check. Do not replace the cut-flow convention by a directed or ordered-pair sum without adjusting constants.

## Route B — a projected observable has a time-average bound

This route is weaker and has different hypotheses. Assume that $P$ is finite, irreducible, reversible and lazy. Let $Q$ be an $L^2(\pi)$-orthogonal projection with $Q1=1$. Suppose that for every real $H$,

\[
 \operatorname{Var}_\pi(QH)\leq K_{\rm obs}\mathcal E_P(H,H).
\tag{B1}
\]

For an observable $G=QG$ and an initial law $\nu\leq U\pi$ pointwise, every $N\geq1$ obeys

\[
 \mathbb E_\nu\!\left[\left(\frac1N\sum_{t=0}^{N-1}G(X_t)-\pi G\right)^2\right]
 \leq \frac{2U K_{\rm obs}\operatorname{Var}_\pi(G)}{N}.
\tag{B2}
\]

This does **not** show $\operatorname{Var}_\pi H\leq K_{\rm obs}\mathcal E_P(H,H)$ for all $H$, does not bound the full-chain gap, and does not imply TV mixing. In particular, an estimated statistic must first be proved $Q$-measurable; writing down a projection after the fact is insufficient.

For audit, put $g=G-\pi G$. Since $Q$ is orthogonal, preserves constants, and $Qg=g$, (B1) gives

\[
 |\langle g,H\rangle_\pi|^2
 =|\langle g,QH\rangle_\pi|^2
 \leq K_{\rm obs}\operatorname{Var}_\pi(G)\mathcal E_P(H,H).
\]

Taking $H=(I-P)^{-1}g$ on the mean-zero subspace is legitimate by finite irreducibility. Laziness makes its nonconstant eigenvalues lie in $[0,1)$, so the stationary autocovariances are nonnegative and their sum is at most $K_{\rm obs}\operatorname{Var}_\pi(G)$. Expanding the variance of the average yields (B2) for stationarity. The path-law Radon--Nikodym derivative from $\nu$ to stationarity is $d\nu/d\pi(X_0)\leq U$, giving the warm-start factor. No commutation of $Q$ with $P$ is used or implied.

## From transition probabilities to selected move energies

For each state \(x\), let \(J(x)\) list designated moves whose transition probabilities in the actual kernel are at least \(\tau>0\). With moves listed once, directly from the Dirichlet form,
\[
\sum_x\pi(x)\sum_{y\in J(x)}(h(x)-h(y))^2
\le \frac{2}{\tau}\mathcal E_P(h,h).
\]
If several move labels share a destination, use their individual kernel contributions and sum them in the Dirichlet form. The same proof applies. For a Metropolis proposal, \(\tau\) must include both the proposal probability and its acceptance probability, as well as any laziness factor outside those terms.

On a product state \((A,B)\) with stationary law \(\pi\otimes\pi\), an \(A\)-only move applied to \(h(A,B)=f_1(A)+f_2(B)\) cancels \(f_2\). If the transition lower bound holds for every \(B\), the second coordinate can be summed out. The matching manuscript applies this to its safe switches and color moves, with respective \(\tau=A_0^{-2}/(30N^2)\) and \(\tau=A_0^{-1}/(6N)\), and to its discrepancy-cycle moves with \(\tau=1/(3N)\). Each application depends on the corresponding proposal rules and activity ratios.

A separate exact rational check on three states used \(\pi=(1/4,1/2,1/4)\), neighbor transition probabilities \((1/2,1/4,1/4,1/2)\), the remaining half mass holding, and \(h=(-1,0,2)\). It gave selected energy \(15/4\), full Dirichlet form \(5/8\), and \(\tau=1/4\).

## Local sources and finite rational check

The stated components were checked against their local preprint versions. The older 32-work register has a separate scope.

- OpenAI, *Approximate counting of common bases of two matroids*, local corpus `02_Recent_Math_Papers/OpenAI/current/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf`, SHA-256 `7ed3dfdefcfa677a2b06e7fcde5efc1a26d3ff774a4b604166e21082ac2607`, PDF pp. 14--15. Lemma 6.1 supplies the observable/warm-start route and Lemma 6.2 applies a trace-chain variant. Its specific $Q$, $K_{\rm obs}$, and trace constant remain matroid-model dependent.
- OpenAI, *Exact Uniform Sampling of Contingency Tables with Arbitrary Margins*, local corpus `02_Recent_Math_Papers/OpenAI/current/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf`, SHA-256 `be1d677ab515ceb23e7ee9fd369d705345ec0c9254585ac96ded3aa97732cd89`, PDF p. 21. Lemma 5.4 states the full-chain Poincaré/conductance route with the displayed conventions. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf)

- OpenAI, *A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs*, PDF p. 22, Lemma 6.2. The source-local use is the move probability to energy comparison, with the regime-specific proposal rules as inputs. SHA-256 1510b15725ee7e92a6c543484c6c02ce7f26347a32c1a11cd66c5890b94c6de1. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf)

An exact finite check was run with Python 3.13.18 using the uniform three-state lazy path

\[
 P=\begin{pmatrix}3/4&1/4&0\\1/4&1/2&1/4\\0&1/4&3/4\end{pmatrix}.
\]

Enumeration of centered integer test vectors in $[-2,2]^3$ gave the exact maximum $\operatorname{Var}_\pi h/\mathcal E_P(h,h)=4$; the endpoint cut has $\kappa=1/4$, and from endpoint 0, $P^4(0,\cdot)=(63/128,85/256,45/256)$ with TV distance $61/384$ from uniform. This checks one displayed finite instance only; it is neither a proof of (A1)--(B2) nor a certificate for another chain.

## Exclusions

Do not use this branch for a non-lazy periodic kernel without an absolute-gap, explicit aperiodicity, or a separate time-averaging argument. Do not identify an ordered eigenvalue merely from (A1), and do not differentiate a gap from these inequalities. A trace kernel needs its own stationary law, reversibility, holding probability, and comparison proof; it is not automatically covered by the original chain's certificate.
