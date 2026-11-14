# janson12 — Bootstrap percolation on the random graph $G(n,p)$

**Reading status:** `fulltext_read`; complete 59-page electronic reprint read (PDF pp. 1–59). Theorem formulas and the external-infection formula were visually checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Svante Janson, Tomasz Łuczak, Tatyana Turova, and Thomas Vallier, “Bootstrap Percolation on the Random Graph $G_{n,p}$,” *Annals of Applied Probability* 22(5) (2012), 1989–2047, DOI [10.1214/11-AAP822](https://doi.org/10.1214/11-AAP822), arXiv [1012.3535](https://arxiv.org/abs/1012.3535). The staged electronic reprint has 59 PDF pages; the journal pagination and reprint typography differ. Local PDF SHA-256: `b5e9b50bc1eb5752959f9b0f3f8c3bacef8873c961c768d6e3fe8d6979440d37`.

## Model and exploration representation

On $G(n,p)$, choose a deterministic initial active set of size $a$, and repeatedly activate any vertex with at least $r\ge2$ active neighbours. By exchangeability, the final-size law depends on the initial set only through $a$. The authors expose edges sequentially by exploring one active vertex per exploration step. Each unexposed edge contributes an independent Bernoulli-$p$ mark; the hitting time $Y_i$ at which a nonseed vertex accumulates $r$ marks is negative-binomial, iid across vertices in this representation. Thus

\[
S(t)=\sum_{i=1}^{n-a}\mathbf 1\{Y_i\le t\}\sim\operatorname{Bin}(n-a,\pi(t)),\qquad A(t)=a+S(t),
\]

and the exploration stops at $T=\min\{t:A(t)=t\}$; the final active-set size is exactly $A^*=T$. This $t$ is an exploration clock and must not be silently identified with synchronous generation count.

## Threshold theorems read

In the sparse range $n^{-1}\ll p\ll n^{-1/r}$, define

\[
t_c=\left(\frac{(r-1)!}{n p^r}\right)^{1/(r-1)},\quad
 a_c=\left(1-\frac1r\right)t_c,\quad
 b_c=\frac{n(np)^{r-1}e^{-np}}{(r-1)!}.
\]

Theorem 3.1 (PDF p. 9): if $a/a_c\to\alpha<1$, then

\[
 A^*=(\phi(\alpha)+o_p(1))t_c,
\]

where $\phi(\alpha)$ is the unique root in $[0,1]$ of $r\phi-\phi^r=(r-1)\alpha$. For $r=2$, $\phi(\alpha)=1-\sqrt{1-\alpha}$. If $a/a_c\ge1+\delta$ for a fixed $\delta>0$, then $A^*=n-o_p(n)$, with the sharper remainder $n-A^*=O_p(b_c)$. For $a\le n/2$, complete percolation occurs with high probability exactly in the stated asymptotic regime $b_c\to0$, equivalently

\[
np-\log n-(r-1)\log\log n\longrightarrow+\infty.
\]

Theorem 3.2 (PDF p. 9) assumes the same sparse range $n^{-1}\ll p\ll n^{-1/r}$, $a=o(n)$, and almost percolation $A^*=n-o_p(n)$ with high probability (for example, Theorem 3.1(ii)). If $b_c\to\infty$, then $n-A^*=b_c(1+o_p(1))$; if $b_c\to0$, then complete percolation holds whp; if $b_c\to b\in(0,\infty)$, then the *final inactive count* $n-A^*$ converges in distribution to $\operatorname{Poisson}(b)$ and $P(A^*=n)\to e^{-b}$. The paper also states a more general version conditioned on having at least $3t_c$ active vertices, even without whp almost percolation. This is a final inactive-tail law, not a Poisson law for the initial-seed critical window. Theorem 3.4 (PDF p. 10), for $a\to\infty$, $a=o(n)$, gives the critical edge-density scale

\[
p_c=\left(\frac{(r-1)^{r-1}(r-1)!}{r^{r-1}}\right)^{1/r}(na^{r-1})^{-1/r},
\]

with subcritical/supercritical alternatives and a separate complete-percolation threshold. The printed scope conditions in the theorem must accompany any use.

Theorem 4.4 (PDF p. 16) treats a process that starts with all vertices inactive and uninfected, then adds external infections one at a time by sampling vertices independently and with replacement; internal spreading occurs between attempts. Activation requires $r$ infections **in total**, whether external or internal. Let $J_0$ be the number of external infections until the active set first becomes “big” as defined in §4.1. If $r\ge2$ and $n^{-1}\ll p\ll n^{-1/r}$, then $J_0/(np a_c)\to_p1$; for $r=2$, $J_0\sim1/(2p)$ in the stated regime. This is a separate external-seeding mechanism, not an identity for lattice infection.

## Proof route and limits

The paper controls the empirical hitting-time curve $A(t)$ around its deterministic mean. Concentration and martingale estimates locate the first crossing $A(t)=t$ near the bottleneck $t_c$; subcritical initial conditions stop near the smaller root, while supercritical conditions escape and infect almost all vertices. Further arguments handle the sparse final tail, a CLT/Poisson critical window, and synchronous generation growth separately. PDF pp. 7, 9, 10 and 16 were rendered and checked for the definitions, Theorems 3.1–3.4 and Theorem 4.4 formulas.

The host is $G(n,p)$, not a lattice or arbitrary graph. The result concerns final size, complete percolation, and in specified sections generations/external infections; it does not yield Holroyd’s finite-square threshold or a general infection-time tail. Theorem hypotheses and asymptotic regimes are essential.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/janson12`).
