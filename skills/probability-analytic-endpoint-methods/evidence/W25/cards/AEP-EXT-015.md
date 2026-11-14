> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-015 — Domingo-Salazar, Lacey & Rey (arXiv v2, 2015; journal version 2016)

## Identity and reading evidence

Carlos Domingo-Salazar, Michael Lacey, and Guillermo Rey, “Borderline weak type estimates for singular integrals and square functions,” *Bulletin of the London Mathematical Society* 48(1) (2016), 63–73, DOI [10.1112/blms/bdv090](https://doi.org/10.1112/blms/bdv090). Read the complete author preprint arXiv:1505.01804v2 [math.CA], dated 26 May 2015, 13 physical pages; this is not the publisher-layout PDF. The official Oxford record is https://academic.oup.com/blms/article/48/1/63/2849712 and the arXiv record is https://arxiv.org/abs/1505.01804. PDF SHA256: `234e8dd09cdcdccc2aa6f2a214dd0df1936a8a97d4cc4fb653c6c41e19ad740b`. All physical pages, including references and author information, were read; see [reading_coverage.json](../reading_coverage.json). Rendered and visually checked physical pp. 3–12 for exact statements and proof equations. **Identity note:** the preprint's title page names Guillermo Rey, in agreement with the official record; its running heads on pp. 2–13 repeat “M. Lacey” as the third author. The running-head inconsistency is recorded rather than silently corrected in the source description.

## Setting and main estimates

In $ℝ^d$, the paper assumes $T$ is a Calderón–Zygmund operator with $|K(x,y)|≤|x-y|^{-d}$, Dini smoothness in each variable (the two symmetric difference estimates in §2), and $L^2$ operator norm at most 1 (physical p. 5). The maximal truncation is
$$T^*f(x)=\sup_{δ>0}\left|\int_{|x-y|>δ}K(x,y)f(y)dy\right|.$$
Constants in the sparse domination and estimates are implicit and depend on dimension and CZO structural/Dini data.

- **Theorem 1.6 (physical p. 3).** Let $φ$ be a Young function, with complementary function $ψ$, and assume $\lim_{t\to\infty}φ(t)/t=\infty$, so $ψ$ is finite. If
$$c_φ:=\sum_{k=1}^{\infty}\frac{1}{ψ^{-1}(2^{2^k})}<\infty,\tag{1.7}$$
then for every such $T$, every weight $w$ on $ℝ^d$, and $λ>0$,
$$λw\{x:T^*f(x)>λ\}\lesssim c_φ\int_{ℝ^d}|f(x)|M_{φ(L)}w(x)\,dx.$$
Here $M_{φ(L)}$ is the Orlicz maximal operator defined using the Luxemburg $φ$-average. The input is the maximal truncation; this is stronger than a bound for $Tf$ alone. The condition contains the double exponential $2^{2^k}$.
- **Corollary 1.8 (physical p. 3).** For $1<α<2$, the theorem yields bounds with constants $\lesssim1/(α-1)$ and maximal bumps $M_{L(\log_2L)^α}w$, and also $M_{L\log_2L(\log_3L)^α}w$ (formulas (1.9)–(1.10)). The paper defines iterated logarithms by $\log_1t=1+\log^+t$ and $\log_kt=\log_1(\log_{k-1}t)$ for $k>1$. This is weighted/log-bumped control; at $w=1$ it gives an unweighted weak-$L^1$ consequence for $T^*$, while for general $w$ the bump on $w$ must be retained.
- **Theorem 1.11 (physical p. 4).** For intrinsic square function $G_α$, $0<α<1$, every $w∈A_p$, and $1≤p<∞$,
$$\|G_αf\|_{L^{p,∞}(w)}≤C_p(w)\|f\|_{L^p(w)},\qquad
C_p(w)=\begin{cases}
[w]_{A_p}^{1/p},&1≤p<2,\\
[w]_{A_p}^{1/2}(\log_1[w]_{A_∞})^{1/2},&2≤p<∞.
\end{cases}$$
At $p=1$, the statement includes $w\in A_1$ and the weighted weak-$(1,1)$ estimate with constant $[w]_{A_1}$ for this intrinsic square function. The range $1\le p<2$ is cited to Lacey–Scurry rather than proved in this article. The square-function result is separate from the maximal-truncation theorem; its $p=1$ member is not a scalar Riesz-transform assertion.

## Source print defects and operational definitions

Several definitions on the printed pages are internally inconsistent and must be separated from the operational method. On physical p. 4, the intrinsic-square-function display prints $\Gamma(x)=\{(y,t):|y|<t\}$, which omits the center $x$, and $\gamma_t(z)=t^{-d}\gamma(zt^{-d})$, which is not the standard dilation. For any operational reference to the usual Wilson intrinsic square function, use the centered cone $\Gamma_{\rm std}(x)=\{(y,t):|x-y|<t\}$ and the standard scale $\gamma_t(z)=t^{-d}\gamma(z/t)$. These corrected formulas are not the literal source print; no theorem is claimed for the literal malformed expressions.

On physical p. 5, the paper calls $\omega$ a “decreasing” Dini modulus. A continuity modulus in this CZO hypothesis must be nondecreasing, vanish at zero in the usual convention, and satisfy $\int_0^1\omega(t)\,dt/t<\infty$. The displayed two-sided difference inequalities are used only under that standard operational Dini-modulus convention; the printed monotonicity word is recorded as a source defect.

On physical p. 6, Theorem 2.4 literally prints $r(w)=1+c[w]_{A_\infty}$. That exponent is incompatible with the reverse-Hölder application on physical p. 11, which raises the small-set ratio to an exponent of order $1/[w]_{A_\infty}$ and derives $\exp(-c 2^{m_0+m}/[w]_{A_\infty})$. The operational reverse-Hölder input needed by that proof has the conventional reciprocal-order form $r(w)=1+1/(C_d[w]_{A_\infty})$, so that $1/r'(w)\asymp1/[w]_{A_\infty}$. The p. 6 line is not silently rewritten as source text: treat it as a printed inconsistency and cite the Hytönen–Pérez reverse-Hölder result externally in the corrected form. The square-function proof is conditional on this standard input; this local defect alone is not a blanket invalidation of the theorem.

## Proof dependencies and mechanism

1. **Sparse reduction, §2 (physical pp. 5–6).** Under the standard operational CZO assumptions described above (in particular a nondecreasing Dini modulus), $T$ and $T^*$ are dominated pointwise by sums of at most $3^d$ sparse operators, each with sparse sets $E_Q\subset Q$ satisfying $|E_Q|\ge(1-8^{-1})|Q|$. An analogous sparse square function dominates the standard intrinsic square function. Lemma 2.3 follows from Orlicz Hölder and bounds averages of $w1_E$ by $\|w\|_{\phi(L),Q}/\psi^{-1}(|Q|/|E|)$. Theorem 2.4 is cited for reverse Hölder, but its literal p. 6 exponent conflicts with the reciprocal-order exponent used on p. 11; see “Source print defects and operational definitions” above.
2. **Theorem 1.6 proof, §3 (physical pp. 6–9).** Reduce to nonnegative $f$ and a sparse positive operator. Use a restricted weak-type set $E=\{4<Tf≤8\}\setminus\{Mf>2^{-2}\}$, Fefferman–Stein's inequality, and split sparse cubes by $\langle f\rangle_Q$ into layers $S_k$. Within each layer, organize nested cubes as $S_{k,v}$ and use disjoint remainders $E_Q$. For $u=2^k$, sparsity gives $|Q_u|≤8^{-u}|Q|$; Lemma 2.3 converts that small-set estimate into $1/ψ^{-1}(2^{2^k})$. The remaining layer contribution is at most $2^{-k}w(E)$. Sum over $k$ and absorb the $w(E)$ term. Corollary 1.8 follows because $ψ^{-1}(t)\simeq L(t)$ for the selected $φ$, followed by comparisons with $\sum k^{-α}$ and $\sum[k(\log k)^α]^{-1}$.
3. **Theorem 1.11 proof, §4 (physical pp. 9–12).** The range $1\le p<2$, including $p=1,w\in A_1$, is cited to Lacey–Scurry; the authors focus on $p\ge2$. Decompose the sparse square function into levels $S_m$ by average size. For moderate levels $0<m\lesssim\log_1[w]_{A_\infty}$, weighted duality and the $A_2$ condition give $\|S_mf\|_{L^p(w)}\lesssim[w]_{A_p}^{1/2}\|f\|_{L^p(w)}$. For large $m$, sparsity yields local exponential integrability; convert Lebesgue measure decay to $w$-measure using the standard reciprocal-order $A_\infty$ reverse-Hölder input (the source p. 11 uses exponent of order $1/[w]_{A_\infty}$), then sum the tail. Do not use the literal p. 6 printed $r(w)=1+c[w]_{A_\infty}$ formula. Choosing $m_0\simeq\log_1[w]_{A_\infty}$ gives the $\sqrt{\log A_\infty}$ loss. Thus the proof of the theorem's $p<2$ range is imported, not supplied in this paper.
4. **References and terminal material, physical p. 13.** Read; contains bibliography, affiliations, and contact addresses. No separate deferred appendix or supplementary proof document occurs in this acquired version.

## Tool use and transfer boundary

This is an **auxiliary endpoint and weighted distribution source** for probability-analytic-endpoint-methods. Its maximal-truncation theorem applies to Dini CZO kernels with the stated $L^2$ normalization and gives a bumped weighted estimate; it does not assert a sharp dimension-uniform constant for C208. A Riesz kernel is a possible CZO instance after checking normalization, Dini constants, and scalar/vector formulation, but resulting constants inherit those structural dependencies. The intrinsic square-function theorem has its own $0<α<1$, $A_p$, and $p$-range assumptions and must not be read as a Riesz-transform statement.

## Reading status

`fulltext_read` for all 13 physical pages. Formula-bearing pages were visually checked against the rendered PDF. Review remains pending; this card does not claim independent acceptance or source-quota credit.
