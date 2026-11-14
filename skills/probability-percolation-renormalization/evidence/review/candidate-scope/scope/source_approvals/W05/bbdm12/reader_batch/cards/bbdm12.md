# bbdm12 — The Sharp Threshold for Bootstrap Percolation in All Dimensions

**Reader declaration:** complete full-text read of the existing 36-page PDF, physical pp. 1–36. The old stable source ID **bbdm12** is retained; this batch completes its prior partial-read record and is not a new work. Independent review and mother-ledger integration are pending.

**Citation:** József Balogh, Béla Bollobás, Hugo Duminil-Copin, and Robert Morris, “The Sharp Threshold for Bootstrap Percolation in All Dimensions,” *Transactions of the American Mathematical Society* 364(5) (2012), 2667–2701, DOI [10.1090/S0002-9947-2011-05552-2](https://doi.org/10.1090/S0002-9947-2011-05552-2), arXiv:1010.3326. The local file is `papers/W05/bbdm-sharp-threshold.pdf`, SHA-256 5599d289240e3f2ba310f9bcb29f9ef9309ab3aafbd46056ae76997569ae4b1d (36 physical pages). This is the existing 36-page 2010-10-15 author manuscript, not the 37-page arXiv v2 or a byte-identified journal file.

## Model and main theorem

For a graph $G$, an initial set $A$ of independently infected vertices evolves by synchronous nearest-neighbour $r$-bootstrap percolation: at each step every vertex with at least $r$ infected neighbours becomes infected. The closure is $[A]$, and percolation means $[A]=V(G)$. Under the product Bernoulli-$p$ law, the paper defines
$$
p_c(G,r)=\inf\{p:\mathbb P_p(A\text{ percolates})\ge 1/2\}.
$$

For $k\in\mathbb N$, define
$$
\beta_k(u)=\tfrac12\left(1-(1-u)^k+\sqrt{1+(4u-2)(1-u)^k+(1-u)^{2k}}\right),
\qquad g_k(z)=-\log\beta_k(1-e^{-z}),
$$
and, for $d\ge r\ge2$,
$$
\lambda(d,r)=\int_0^\infty g_{r-1}(z^{d-r+1})\,dz. \tag{1}
$$
Theorem 1 (PDF p. 3) states, for each fixed pair of integers $d\ge r\ge2$,
$$
p_c([n]^d,r)=\left(\frac{\lambda(d,r)+o(1)}{\log_{(r-1)} n}\right)^{d-r+1},
\qquad n\to\infty,
$$
where $\log_{(j)}$ is the $j$-fold iterated natural logarithm. In particular, $\lambda(2,2)=\pi^2/18$. The theorem is for the finite box with the ordinary nearest-neighbour $r$-rule and fixed $d,r$; it is not a statement about infection times or arbitrary update families.

Remark 1 on PDF p. 3 also gives a subcritical probability bound: for each fixed $\varepsilon>0$, if $p=(1-\varepsilon)p_c$, then $\mathbb P_p(A\text{ percolates})\le n^{-d(r-2)-\delta(\varepsilon)}$ for some $\delta(\varepsilon)>0$ (using Corollary 23 and Theorem 27). The displayed supercritical bound in that remark is explicitly attributed to prior work [6], rather than proved anew here. At PDF p. 31 the authors likewise say Theorem 1’s upper bound was proved in [6], while their Theorem 27 supplies the lower bound.

## Proof architecture and exact intermediate claims

The paper strengthens induction in a family of auxiliary **bootstrap structures** $C([n]^d\times[k]^\ell,r)$, not simply the ordinary grid: the graph is induced by the nearest-neighbour lattice on $[n]^d\times[k]^\ell$, and a vertex $(x,y)$ has threshold $r+|\{j\le\ell:y_j\notin\{1,k\}\}|$ (definition on PDF p. 4). These variable thresholds create a controlled extra thickness for the induction.

1. **Thin-thickening base case (Theorem 2, PDF p. 5).** For fixed $d\ge2$, $\ell\in\mathbb N$, and $\varepsilon>0$, with $B>0$ and $k\ge k_0(B)$ sufficiently large, iid initial infection of $C([n]^d\times[k]^\ell,2)$ at density
   $$
   p(n)\le\left(\frac{\lambda(d+\ell,\ell+2)-\varepsilon}{\log n}\right)^{d-1}
   $$
   implies $\mathbb P_p(\operatorname{diam}([A])\ge B\log n)\to0$. The relevant use has a positive numerator. This is a subcritical diameter bound for the auxiliary threshold structure, not the final theorem on an arbitrary graph.

2. **Rectangle geometry and hierarchies (PDF §§2–3, pp. 5–8).** Rectangles have side-length vector $\operatorname{dim}(R)$ and semi-perimeter $\phi(R)$; the span $\langle A\rangle$ is the collection of smallest rectangles containing connected components of $[A]$. “Internally spans” means $R\in\langle A\cap R\rangle$. The paper sets $q=-\log(1-p)$ and $u(x)=1-e^{-qx}$. The PDF calls $u(x)$ the probability a set of size $x$ is empty (not occupied), but the displayed formula equals the probability it is occupied; subsequent identities and uses are consistent with occupancy. This source-text inconsistency is flagged rather than silently corrected. The identity $\beta_k(1-(1-p)^n)=e^{-g_k(nq)}$ is equation (2), PDF p. 6. A good hierarchy is an oriented rooted tree of nested rectangles with at most $\ell+2$ children, small prescribed changes in $\phi$, and small-side seeds. Lemma 3 says every internally spanned rectangle has a good hierarchy that occurs; Lemma 4 bounds the number of such hierarchies by a fixed power of $1/p$; Lemma 5 combines disjoint witness events with van den Berg–Kesten (BK) to upper-bound the span probability by a sum of products over hierarchies (PDF pp. 7–8).

3. **Crossing estimate (PDF §4, pp. 8–15).** A direction-$j$ crossing is defined after infecting the external face on one side. Lemma 6 (PDF p. 9) bounds the probability, even conditioned on any specified $t$-set $W\subseteq R$ being initially infected, by
   $$
   \mathbb P_p(H^{\to(1)}(R))\le h^{(1)}(R,t)\le
   \beta_{\ell+1}(u_1(R))^{(1-\delta)a_1-kt},
   $$
   where $R$ has dimensions $(a_1,\dots,a_d)$, $a_i\le Bp^{-1/(d-1)}$ for every $i\ne1$, $k$ is sufficiently large, and $p$ sufficiently small; $u_1(R)=u(\prod_{i=2}^d a_i)$. The lemma also records the lower bound $\beta_{\ell+1}(u_1(R))^{a_1+1}\le\mathbb P_p(H^{\to(1)}(R))$.

   The proof cuts a long rectangle into width-$s$ blocks and couples each block to a lower-threshold structure $C([m]\times[k],1)$. The deterministic blocker lemma (Lemma 7, PDF p. 11) says a crossing forces either two initial infected vertices within graph distance at most two, an unblocked boundary edge, or a boundary edge not fully blocked. Lemmas 8–10 (PDF pp. 12–14) turn blocker failures into powers of $\beta_{\ell+1}(u(S))$, using the recurrence in Lemma 9. The final block independence and conditioning argument yields Lemma 6 on pp. 14–15. This is a model-specific finite-lattice geometric estimate, not a general crossing theorem.

4. **Analytic cost and Theorem 2 (PDF §§5–6, pp. 15–26).** For increasing piecewise-linear paths in $\mathbb R_+^d$, the paper defines a line-integral infimum $W_f(a,b)$ and rescales it to $U_f(R,R')$ (equation (3), PDF p. 15). Proposition 11 (PDF p. 16) compresses a hierarchy into a “pod” rectangle and lower-bounds the sum of its transition costs by a single pod-to-root integral, up to an explicit branching error. Proposition 12 (PDF pp. 16–19) lower-bounds the integral by the diagonal integral $d\int g_\ell(z^{d-1})\,dz$, minus a boundary correction; its proof uses monotonicity and convexity of $g_\ell$, discretization, coordinate rearrangement, and a diagonal path. These are the analytic ingredients producing $\lambda(d+\ell,\ell+2)$.

   Theorem 17 (PDF pp. 20–25) is the key large-rectangle estimate: for fixed $d\ge2$, $\ell\in\mathbb N$, $\varepsilon>0$, there are $B_0,k_0(B)$ so that for $B\ge B_0$, $k\ge k_0(B)$, small $p$, and a rectangle $R\subset C([n]^d\times[k]^\ell,2)$ with $\operatorname{long}(R)=Bp^{-1/(d-1)}$,
   $$
   \mathbb P_p(R\in\langle A\cap R\rangle)\le
   \exp\!\left(-\frac{d\lambda(d+\ell,\ell+2)-\varepsilon}{p^{1/(d-1)}}\right).
   $$
   The proof sums over good hierarchies (Lemma 5), uses Lemma 6 for each transition, and splits hierarchies into three cases: large total seed semi-perimeter, a long-thin pod, or the remaining case where Proposition 12 yields the integral cost. The polynomial number of candidate hierarchies is absorbed into the exponential error. Corollary 23 (PDF pp. 25–26) plus a count of possible internally spanned rectangles yields Theorem 2.

5. **Cerf–Cirillo induction (PDF §§7–8, pp. 26–31).** Lemma 24 (Cerf–Cirillo; PDF p. 27) concerns a random sequence $\mathcal P=(G_1,\ldots,G_m)$ of independent admissible two-coloured graphs on $S\times[2]$. For fixed $0<\alpha<1/2$, $\varepsilon>0$, choose $\delta>0$; for all $m$ and finite $S$ with $\alpha^4|S|^\varepsilon\ge1$, its BK hypothesis is the full source event: for each layer $t$, integer $r\ge1$, and listed pairs $x_j,y_j\in V(G_t)$,
   $$
   \mathbb P\!\left(\bigcap_{j=1}^r\{x_j\sim y_j\}\;\cap\!\bigcap_{j\ne j'}\{x_j\not\sim x_{j'}\}\;\cap\{E^b(G_t)=\varnothing\}\right)\le\prod_{j=1}^r\mathbb P(x_j\sim y_j).
   $$
   Here $\sim$ means a good edge. The cross nonconnection of every pair of distinct $x_j$'s is part of this hypothesis; different endpoints alone do not state it. Along with independent layers, $\mathbb P(E^b(G_t)\ne\varnothing)\le|S|^{-\varepsilon}$, and expected good degree at most $\delta$ for each vertex, Lemma 24 concludes $\mathbb P(X(\mathcal P))\le\alpha^m|S|$. The condition is a lower bound on $\alpha^4|S|^\varepsilon$, not an upper bound.

   Lemma 25 (PDF p. 28; cited as Lemma 36 of [6]) supplies the base-case local bound: for $d\ge2$, $B>0$, $G=C([n]^d\times[k]^\ell,2)$, iid $A\sim\mathrm{Bin}(V(G),p)$, and sufficiently small $p$,
   $$
   \mathbb E_p|\Gamma_G(A,B/p^{1/(d-1)},v)|\le c(B,d,k,\ell)\,p\,(\log(1/p))^{3d+\ell+1}
   $$
   for every vertex $v$. The factor is $p$ times the logarithmic power (not a reciprocal power).

   Theorem 27 (PDF pp. 28–31) inducts on $r$. For fixed $d\ge r\ge2$, $\ell\in\mathbb N$, and sufficiently small $\varepsilon>0$, choose $B$ and sufficiently large $k\ge k_0(B)$. If
   $$
   p(n)\le\left(\frac{\lambda(d+\ell,\ell+r)-\varepsilon}{\log_{(r-1)}n}\right)^{d-r+1},
   $$
   then, in $G=C([n]^d\times[k]^\ell,r)$,
   $$
   \mathbb P_p(\operatorname{diam}([A])\ge B\log n)\le n^{-(r-2)d-\varepsilon},\qquad
   \mathbb E_p|\Gamma_G(A,B\log n,v)|=o(1)
   $$
   as $n\to\infty$, uniformly in $v\in V(G)$. Here $\Gamma_G(A,m,v)$ is the set of vertices connected to $v$ through a connected internally filled component of diameter at most $m$. The base case is Corollary 23 together with Lemma 25’s local expected-neighbour bound. For $r\ge3$, the proof partitions an internally spanned rectangle into width-$k$ blocks, lowers boundary thresholds so the block processes couple above to $C([m]^{d-1}\times[k]^{\ell+1},r-1)$, and uses induction to show bad edges are rare and expected good degree is small. The proof says the BK condition follows from disjointness of witnesses when there are no bad edges; Lemma 24 requires the full cross-nonconnection event displayed above. Lemma 26 converts a large closure diameter into an internally filled connected set, and a union/sum bound finishes both conclusions. Taking $\ell=0$ gives the lower-threshold half of Theorem 1; the paper cites [6] for the matching upper bound.

   **Local good-edge scale caveat (PDF pp. 28, 30).** The print is inconsistent: Remark 4 on p. 28 introduces $S=[N]^{d-1}\times[k]^\ell$ and calls an edge good when its endpoints lie in an internally filled component of diameter $<B\log N$; equation (9) on p. 30 bounds the expected good degree using the local cutoff $B^{(r-1)}(d-1,\ell+1,\varepsilon)\log m$ for a block of side parameter $m$. But the p. 30 definition of $x\sim y$ uses diameter at most $B^{(r-1)}(d-1,\ell+1,\varepsilon)\log n$. These printed scales are not identical. Do not silently replace one by another or claim the displayed definition directly supplies the local-scale estimate: in any reuse of the induction template, verify the expected good-degree bound at the actual local block scale (the $m$/$N$ scale used for the layer set).

## Reuse map and limits

- **W05 percolation/renormalization tool:** eligible as a completed primary source for fixed-dimensional finite-grid bootstrap thresholds, hierarchical rectangle decompositions, crossing estimates, and the Cerf–Cirillo induction pattern. These are reusable only under the source’s product-measure, nearest-neighbour, finite-grid, and stated auxiliary-structure assumptions.
- **B179:** auxiliary background at most. B179 asks for an infection-time tail for general finite update families; Theorems 1 and 27 concern eventual closure/percolation probabilities in the specific nearest-neighbour $r$-rule and say nothing about the tail of the infection time.
- **A200:** no direct theorem transfer. A200 is the Hamming-neighbourhood Young-diagram rule and a minimum-seed question; BBDM’s ordinary nearest-neighbour fixed-$r$ rule does not establish its finite-box-to-plane interface or the proposed $\gamma(Z)\ge |Z|/2$ bound.
- **Broader models discussed in §9 are not proved here.** Theorem 29 (PDF p. 33), attributed to Duminil-Copin–Holroyd [18], concerns a finite convex symmetric neighbourhood $N\subset\mathbb Z^2$ containing $0$ and a balanced critical $(r,N)$ rule; with $\ell_1(N)$ the maximal number of points of $N$ on a line through $0$ and $\gamma_1=r-(|N|-\ell_1(N))/2$, it states $p_c([n]^2,r,N)=((\Lambda+o(1))/\log n)^{1/\gamma_1}$ for some $\Lambda\in(0,\infty)$. Theorem 30 (PDF p. 34), attributed to Gravner–Holroyd–Morris [29], gives for constants $C,c>0$ and every $n\in\mathbb N$ the sharper $r=2,d=2$ bounds
  $$
  \frac{\pi^2}{18\log n}-\frac{C(\log\log n)^3}{(\log n)^{3/2}}\le p_c([n]^2,2)\le \frac{\pi^2}{18\log n}-\frac{c}{(\log n)^{3/2}}.
  $$
  These are contextual cited results, not results proved by BBDM.
- The result does not apply automatically to arbitrary update families, random graphs, zero forcing, oriented models, or graph-bootstrap infection-time questions. Finite numerical checks below only corroborate a special constant and an algebraic recurrence; they are not evidence for the all-$n$, all-$d,r$ theorem.

## Bounded mathematical check

Equation (1), Theorem 1, PDF p. 3 gives the exact $\lambda(2,2)=\pi^2/18$ value by reference to earlier work. I evaluated its defining integral independently in the existing local MATLAB using the positive root $\beta_1(u)=(u+\sqrt{4u-3u^2})/2$, obtained from the paper’s displayed relation $\beta_1(u)^2=u\beta_1(u)+u(1-u)$. The script is math/check_lambda22.m; output is math/lambda22_result.txt. Numerical quadrature over $[10^{-10},\infty)$ gave 0.548311354415026 versus $\pi^2/18=0.548311355616075$ (absolute difference $1.20105\times10^{-9}$); the sampled positive-root identity residual was $4.23516\times10^{-22}$. The omitted interval at zero and floating-point quadrature mean this is only a numerical consistency check, not a rigorous integral evaluation or proof of Theorem 1.

## Full-text evidence

Page-marked extraction is in text/bbdm12.txt; all 36 pages were read in physical-page order. All 36 physical pages were rendered to rendered/p01.png–rendered/p36.png. Theorem/definition and proof formulas were visually checked against the rendered PDF on physical pp. 2–6, 9–15, and 16–36. The article has no appendix; references occupy physical pp. 34–35 and the final page (p. 36) contains author affiliations. Section-by-section reading evidence is in reading_coverage.json#sources.bbdm12.

