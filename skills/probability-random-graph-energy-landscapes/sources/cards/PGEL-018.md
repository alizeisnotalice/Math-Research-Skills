> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-018 — planar cycle basis and a restricted stable-state count

## Identity and reading record

- **Read file:** `../pdfs/PGEL-018.pdf`
- **Reader/review:** L02 (W24); R05 helper-stage review passed and reading evidence accepted; mother-hash binding remains pending. R05 metadata_verified=false.
- **Mother coverage:** `../../reading_coverage.json` entry for PGEL-018; helper evidence path `../../reading_coverage.json#PGEL-018`.
- **Exact local version:** arXiv:1609.02359v2; 13 physical PDF pages; SHA-256 `8546628e25dfe3798eb8b62fcd49bb02df2b1a5a489c1a4fb9d8961c36df81c3`.
- **Reading status:** full text read, physical pp. 1–13 in order, including all theorem proofs, numerical examples, conclusion, acknowledgment, and references. Formula pages were rendered from this same PDF and visually checked.

## Model and notation

The paper studies the homogeneous/equal-frequency Kuramoto model on a finite **connected planar graph**. After passing to the rotating frame and rescaling the common positive coupling $K$, the displayed fixed-point equations use unit edge coupling. Fixed points are counted modulo a common phase shift; the paper does not cover disconnected graphs, whose components retain independent rotations after quotienting by just one common phase. On p. 5 the authors explicitly restrict to connected planar graphs, choose a facial fundamental-cycle basis, and remove tree-like appendages: edge angle differences on those appendages are uniquely determined and the appendage is absorbed into its attachment vertex. The stability matrix is the symmetric linearization, with a rotational zero mode. The central flow/count argument uses this face-cycle basis and **only counts stable fixed points whose every edge difference lies in the closed interval** $[-\pi/2,\pi/2]$.

Orient each face cycle consistently with the planar embedding and encode edge flows with the signed cycle-edge incidence matrix $S$. Under this facial orientation convention, an edge shared by two faces receives the difference of their two vortex-flow coordinates; with an arbitrary cycle-basis orientation, retain the signs in $S\epsilon$ rather than copying an unsigned $\epsilon_k-\epsilon_i$ formula.

## Main results and proof chains

1. **Proposition II.1 (PDF p. 7).** For a winding vector $q\in\mathbb Z^c$, stable fixed points with every gap in $[-\pi/2,\pi/2]$ correspond one-to-one to vortex-flow vectors $\epsilon\in Q(q)$, where $Q(q)$ is the intersection of the flow-domain constraints and winding level sets. The gap restriction lets the edge-angle map use the single-valued principal branch $\Delta_e(\epsilon)=\arcsin((S\epsilon)_e)$. Injectivity follows from $S(\eta-\mu)=0$ and linear independence of the cycle-basis columns.

2. **Theorem III.1 (PDF pp. 7–8).** For a planar graph and its facial cycle basis, for each fixed winding vector $q$, the intersection of the quantization level sets is empty or a singleton. In the source’s coherent face orientation convention,
   $$A_k(\epsilon)=m_k\arcsin(\epsilon_k)+\sum_{i\ne k}m_{ki}\arcsin(\epsilon_k-\epsilon_i)=2\pi q_k,$$
   where $m_k$ counts edges belonging only to face $k$, and $m_{ki}$ counts edges shared by faces $k,i$. If two distinct points $\eta,\mu$ solved the same system, set $\xi=\mu-\eta$ and choose a maximal positive coordinate $\xi_1$. Along the segment $\eta+\alpha\xi$, the directional derivative of $A_1$ is strictly positive when $m_1>0$. If $m_1=0$, either all cycle-coordinate differences are equal and some cycle has a private edge, or connectivity of the face-adjacency structure gives adjacent cycles $k_0,k_1$ with $m_{k_0k_1}>0$ and $\xi_{k_0}>\xi_{k_1}$; using $A_{k_0}$ then gives a strictly positive derivative. This contradicts equality of endpoint level values. The argument uses the planar facial incidence structure and the principal-arcsine domain.

3. **Corollary III.2 (PDF p. 8).** For any planar graph, the number $N^*$ of stable fixed points with all edge gaps in $[-\pi/2,\pi/2]$ satisfies
   $$N^*\le\prod_{k=1}^c\left(2\lfloor n_k/4\rfloor+1\right),$$
   where $n_k$ is the length of face cycle $k$. There are at most the displayed number of winding vectors because $A_k$ ranges over $[-n_k\pi/2,n_k\pi/2]$; Theorem III.1 gives at most one flow vector for each $q$, and Proposition II.1 transfers that to the restricted stable solutions.

4. **Lemma III.4 and Corollary III.5 (PDF p. 9).** If no pair of vertices of degree at least 3 is joined by a single edge, then every stable state has all edge gaps in $[-\pi/2,\pi/2]$, so the same product bound applies to the **total** number $N$ of stable fixed points. The proof combines the cut necessary condition from Lemma III.3,
   $$\sum_{e\text{ crossing }(U,U^c)}\cos\Delta_e\ge0,$$
   with the degree-2 equilibrium relation: if adjacent gaps straddle $\pi/2$, their sines force complementary angles and opposite cosines, producing a negative $2\times2$ principal minor of $-M$. The graph hypothesis excludes the remaining single-shared-edge configuration.

## Counterexamples, conjecture, and limits

- **§IV, PDF pp. 10–11:** A planar theta graph with two cycles sharing one edge has a numerically exhibited stable state with the shared-edge gap $\pi/2+0.149$ and reported winding vector $(-1,1)$. The figure/example is numerical. The authors also distinguish a stable $q=1$ vortex on a larger triangular lattice from the unstable $q=1$ twist on the simple triangle. For the simple 3-cycle with all three gaps $2\pi/3$, the $K=1$ Jacobian eigenvalues are $0,3/2,3/2$, so this state is unstable.
- **Eq. (5.1), §V PDF pp. 11–12:** the product bound involving shared-edge counts $n'_k$ for generic planar graphs is explicitly a **conjecture**. The authors say they cannot prove the one-to-one correspondence when some edge gaps exceed $\pi/2$. Do not report this formula as a theorem or as proved for all planar graphs.
- All theorems here concern positive symmetric equal-frequency dynamics on connected planar graphs, with tree-like appendages reduced as described on p. 5. Disconnected graphs and counts modulo fewer than the independent component phases are outside scope. No signed/oriented or nonreciprocal transfer is established. A finite numerical example is not a general existence theorem for all one-edge-sharing planar graphs.

## Computation

The saved SymPy script checks the exact spectra for the $n=5$ positive cycle and the simple triangular $q=1$ twist. These checks corroborate the source’s limited examples; they do not prove the planar theorem or validate its generic conjecture.
