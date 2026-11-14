> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-008 — The lower bound of the network connectivity guaranteeing in-phase synchronization

## Identity and reading record

Ryosuke Yoneda, Tsuyoshi Tatsukawa, and Jun-nosuke Teramae, arXiv:2104.05954v2 (28 May 2021), DOI [10.1063/5.0054271](https://doi.org/10.1063/5.0054271); [official arXiv record](https://arxiv.org/abs/2104.05954). The physical p. 1 displays both “The lower bound of the critical connectivity” and “The lower bound of the network connectivity guaranteeing in-phase synchronization”; the latter is the sourcepool/official-record citation title. The local PDF has 10 physical pages, SHA-256 e4968f7cd2858b9154ad630eb72661b2dd1418c05ba5a2ee8cf4cac3cef5ef47. Reader L14 read pp. 1–10, including Appendix A, data statement, and references. Coverage/render evidence is recorded in ../../reading_coverage.json. No exact-title, arXiv-ID, or hash match was found in the accepted canonical-read index. R05 helper-stage review passed; mother hash binding is pending.

## Model and exact stability notion

The model is identical Kuramoto oscillators after removing the common natural frequency:
\[
\dot\theta_i=\sum_{j=1}^N a_{ij}\sin(\theta_j-\theta_i).
\]
The graph is undirected, unweighted, and positive: \(a_{ij}=a_{ji}\in\{0,1\}\), \(a_{ii}=0\). Connectivity is minimum degree divided by \(N-1\). The paper considers only circulant networks \(a_{ij}=x_{j-i}\), with \(x_0=0\) and \(x_l=x_{N-l}\). The p-twisted equilibrium is
\[
\theta_p^*=(0,2\pi p/N,\ldots,2\pi p(N-1)/N),\qquad
1\le p\le\lfloor N/2\rfloor .
\]
Its symmetric circulant Jacobian has one rotational eigenvalue \(\lambda_0=0\) and
\[
\lambda_k=\sum_{l=1}^{N-1}x_l\cos(2\pi pl/N)\{-1+\cos(2\pi kl/N)\},
\quad 1\le k\le N-1.
\]
Here “linearly stable” means every one of the other \(N-1\) eigenvalues is strictly negative. If additional eigenvalues are zero, the authors say linear analysis is inconclusive; they do not classify nonlinear stability in that case. No general directed-graph or signed-edge model is treated.

## Theorems and proof chain

**Theorem 1 (PDF p. 4; proof §V, pp. 4–6).** Fix \(N\ge2\), \(1\le p\le\lfloor N/2\rfloor\), let \(m=\gcd(N,p)\), and \(\widetilde N=N/m\). For \(\widetilde N\le4\), the strict linear-stability integer program has no feasible network. For \(\widetilde N\ge5\), define
\[
s_k=\sum_{l=1}^k\left[-\cos(2\pi l/\widetilde N)+\cos^2(2\pi l/\widetilde N)\right],
\qquad k_c=\min\{k:s_k\ge0\}.
\]
Then the maximum connectivity among circulant networks for which this fixed p-twisted state is linearly stable is
\[
\mu(N,p)=
\frac{m(2k_c-1)-3-2\left\lfloor
\displaystyle\frac{m s_{k_c-1}}{s_{k_c}-s_{k_c-1}}
\right\rfloor}{N-1}.
\]
The optimizer is over symmetric binary edge indicators, so this is an undirected, unweighted graph formula.

The proof takes the DFT eigenvalues above and encodes strict stability by linear inequalities in \(x\); the symmetry constraint is \(x_l=x_{N-l}\). For noncritical eigenvalue rows the coefficients have the favorable sign, so the binding condition reduces to a single strict scalar inequality involving
\(b_l=-\cos(2\pi pl/N)+\cos^2(2\pi pl/N)\).
The proof then splits into \(p=1\), \(p=m\), coprime \(m=1,p\ne1\), and \(m\ne1,p\ne m\). The first case selects symmetric indices up to \(k_c-1\); the \(p=m\) case decomposes the index set into \(m\) periodic blocks, adds the zero-coefficient indices, and counts the remaining pairs allowed by the strict inequality. The two remaining cases reduce by permutation/periodicity to those first cases. This produces the floor term; replacing the strict constraint by a non-strict one can change the integer count.

**Theorem 2 (PDF p. 6; §VI pp. 6–7; Appendix A p. 9).** Over the considered circulant network sizes and twisted states,
\[
\sup_{N,p}\mu(N,p)=
\frac{11}{19}
-\frac{2}{19}
\frac{\displaystyle\sum_{l=1}^{5}
[-\cos(2\pi l/19)+\cos^2(2\pi l/19)]}
{-\cos(12\pi/19)+\cos^2(12\pi/19)}
=0.6838758207\ldots .
\]
The supremum is approached by the family \((N,p)=(19m,m)\) as \(m\to\infty\), with the m-twisted state. Thus this is a constructive lower bound on the universal critical connectivity \(\mu_c\): for those positive circulant graphs, a nonsynchronous twisted state is linearly stable at connectivity tending to this value. It is not a theorem that every stable state in every network is a twisted state, nor does it identify the exact \(\mu_c\).

Appendix A states the bound
\[
\frac{k_c}{\widetilde N}\le K_c+\frac1{2\widetilde N}
+\frac{2\pi}{3\widetilde N^2},
\]
where \(K_c\) solves \(8\pi t(K_c)=4\pi K_c+\sin(4\pi K_c)-4\sin(2\pi K_c)=0\), \(t(x)=\int_0^x[-\cos(2\pi y)+\cos^2(2\pi y)]\,dy\), and the authors report \(K_c\approx0.34046\). However, the displayed A13-to-A14 step on physical p. 9 is unsupported as written. A13 gives
\[
t(K_c-h)>-h\,b(K_c),\qquad h=\frac1{2\widetilde N}-\frac{2\pi}{3\widetilde N^2}>0.
\]
Expanding the right side gives \(-b(K_c)/(2\widetilde N)+2\pi b(K_c)/(3\widetilde N^2)\). Since \(b(K_c)\le2\), the positive second term is bounded above by \(4\pi/(3\widetilde N^2)\), not below by it; A14 uses that replacement to claim a lower bound. The independent 60-digit check saved in ../../audit/review-index.json at \(\widetilde N=1001\) records \(t(K_c-h)=-0.00041050043198720561397809896604197940693176950019214784373809\) and the printed A14 right side \(-0.000409410760850223274569152963775366018349198502155752387873941\), so the printed strict inequality fails at that argument. This isolates a gap in the displayed Appendix A derivation; it does not establish that A1 or Theorem 2 is false. Keep Theorem 2 as the source-reported circulant result, but do not treat this Appendix A step as a verified proof of its large-\(\widetilde N\) bound. The finite comparison and the local numerical checks below do not repair that gap.

## Numerical source check and limits

The source’s PDF p. 8 gives the finite example \((N,p)=(1900,100)\), with maximum connectivity \(1297/1899=0.6829910479\ldots\). A Python standard-library calculation saved with this batch evaluates the Theorem 2 expression and this rational value; see ../math/pgel_008_numeric_check.py and its JSON output. This numerical check is not a proof of Theorems 1–2. Section VII also plots five small perturbation simulations. Those trajectories are illustrations, not a basin-of-attraction theorem.

## Reusable method and C118 transfer gap

Reusable for symmetric circulant positive graphs: diagonalize the Jacobian by Fourier modes, translate strict linear stability into a binary feasibility problem, exploit reflection symmetry and the gcd period, then count the maximum feasible edges exactly. This is a structured counterexample construction and a lower-bound method for a critical density. C118 asks for a signed random complete-graph landscape threshold; it has neither the circulant symmetry nor the positive edge coefficients used in the sign reduction. These results cannot be applied to signed weights or taken as a global-synchronization theorem. At most they provide a template for finding structured signed counterexamples after a separate signed-spectrum analysis.
