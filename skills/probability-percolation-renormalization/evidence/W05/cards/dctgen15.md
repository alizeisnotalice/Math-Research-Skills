# dctgen15 — Sharpness on transitive graphs

**Reading status:** `fulltext_read`; complete 23-page arXiv v3 was read (PDF pp. 1–23). The main percolation theorem and finite-set differential inequality were visually checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Hugo Duminil-Copin and Vincent Tassion, “A New Proof of the Sharpness of the Phase Transition for Bernoulli Percolation and the Ising Model,” arXiv [1502.03050](https://arxiv.org/abs/1502.03050), v3 (21 January 2018). Local PDF SHA-256: `8c204312d67bfd156d09ac803316922bffa629c64c65f9c6a1121d95123aae04`.

## Bernoulli percolation theorem

Let \(G=(V,E)\) be a locally finite infinite vertex-transitive graph with a transitive group preserving symmetric nonnegative couplings \(J_{x,y}\). For \(\beta\ge0\), edges are independent and \(\{x,y\}\) is open with probability \(1-e^{-\beta J_{x,y}}\). Define \(\beta_c=\inf\{\beta:\mathbb P_\beta(0\leftrightarrow\infty)>0\}\), and, for finite \(S\ni0\),

\[
\phi_\beta(S)=\sum_{x\in S,\,y\notin S}(1-e^{-\beta J_{x,y}})\,\mathbb P_\beta(0\stackrel{S}{\longleftrightarrow}x),\qquad
\widetilde\beta_c=\sup\{\beta:\phi_\beta(S)<1\text{ for some finite }S\ni0\}.
\]

Theorem 1.1 (PDF p. 2) proves \(\widetilde\beta_c=\beta_c\), the mean-field lower bound \(\mathbb P_\beta(0\leftrightarrow\infty)\ge(\beta-\beta_c)/\beta\) for \(\beta>\beta_c\), and finite susceptibility \(\sum_x\mathbb P_\beta(0\leftrightarrow x)<\infty\) for \(\beta<\beta_c\). Exponential one-arm decay is asserted only for finite-range couplings. For nearest-neighbour bond parameter \(p=1-e^{-\beta}\), §1.2 gives the sharper translated form \(\theta(p)\ge(p-p_c)/(p(1-p_c))\) and explains the site-percolation adaptation with a degree-dependent factor.

The proof introduces the finite-set criterion, applies Russo’s formula to a finite-volume connection event, and isolates the random set of vertices disconnected from the exterior. The independence of internal and boundary edges turns pivotal probabilities into \(\phi_\beta(S)\) times the probability of the explored set. Integrating the differential inequality above \(\widetilde\beta_c\) gives the survival lower bound. Below \(\widetilde\beta_c\), a BK boundary decomposition yields a contraction of susceptibility; in finite range, iterating that contraction gives exponential spatial decay. Thus the finite-set witness is the organizing tool, while BK independence and finite range are essential to the stated conclusions.

## External-field corollaries read

In §1.5 (PDF pp. 8–9), Proposition 1.3 concerns the ghost vertex \(g\) added for field \(h>0\), with \(M(\beta,h)=\mathbb P_{\beta,h}(0\leftrightarrow g)\). Lemma 1.6 gives

\[
\partial_\beta M\le\Bigl(\sum_{x\in V}J_{0,x}\Bigr)M\,\partial_h M.
\]

Combining this with the finite-set differential inequality \(\partial_\beta M\ge(1-M)/\beta\) for \(\beta\ge\beta_c\), then using the critical boundary value and integrating in \(h\), yields \(M(\beta_c,h)\ge c\sqrt h\). This is the Bernoulli ghost-field connection estimate; it is distinct from site adaptation, which is discussed in §1.2.

## Ising extension and scope

Theorem 2.1 (PDF p. 9) treats ferromagnetic Ising models on the same transitive graph setting. It proves the mean-field magnetization bound \(\langle\sigma_0\rangle_\beta^+\ge\sqrt{\beta^2-\beta_c^2}/\beta\) for \(\beta>\beta_c\), finite susceptibility for \(\beta<\beta_c\), and exponential two-point decay in the finite-range case. The proof in §§2.3–2.5 uses random-current expansion, the switching lemma, and a modified Simon inequality (replacing the BK step). In §2.6 (PDF pp. 21–22), Proposition 2.3 gives an additional critical-field bound \(\langle\sigma_0\rangle_{\beta_c,h}\ge c h^{1/3}\). The paper defines \(M(\beta,h)=\langle\sigma_0\rangle_{\beta,h}\), combines Lemma 2.6’s lower differential inequality \(M\partial_\beta M\ge 2(1-M^2)/\beta\) at \(\beta\ge\beta_c\) with the GHS-based bound \(\partial_\beta M\le(\sum_yJ_{0,y})M\partial_hM\), and integrates the resulting inequality in \(h\). The authors explicitly warn that finite susceptibility and exponential decay are not comparable for general infinite-range interactions; dependent percolation does not inherit the proof just by analogy.

**Visual checks:** rendered PDF p. 2 for Theorem 1.1 and \(\phi_\beta\), pp. 8–9 for the ghost-field \(c\sqrt h\) proof, and p. 21 for the Ising \(ch^{1/3}\) proof; read the random-current proof chain in PDF pp. 11–21.

## Transfer limits

This is independent Bernoulli percolation (or the separately treated ferromagnetic Ising model) on a locally finite transitive graph. It is not a sharpness theorem for dependent oriented edges, bootstrap infection rules, random percolation clusters, or arbitrary quasi-transitive graphs. The exponential conclusions require finite range; no direct conclusion about an infection-time tail follows.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/dctgen15`).
