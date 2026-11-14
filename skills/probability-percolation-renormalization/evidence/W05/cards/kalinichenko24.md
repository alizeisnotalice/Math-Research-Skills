# kalinichenko24 — Weak saturation numbers in random graphs

**Reading status:** `fulltext_read`; complete arXiv v3, PDF pp. 1–13, read. The central stability statements and sparse-host condition were checked on rendered PDF pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Olga Kalinichenko, Meysam Miralaei, Ali Mohammadian, and Behruz Tayfeh-Rezaie, “Weak Saturation Numbers in Random Graphs,” arXiv:2306.10375v3 (10 March 2024). Local PDF SHA-256: `e46ef8c3d67abb2720ce7406e2f5ad009b87bd7990ab3c573d3c4e4d05293cd6`.

## Results

For fixed graphs \(G,F\), a weakly \((G,F)\)-saturated spanning subgraph contains no copy of \(F\), and its missing edges can be added in a **sequential order** so that each added edge creates a new copy of \(F\). The minimum size is \(\mathrm{wsat}(G,F)\). This sequential process is distinct from the synchronous graph-bootstrap dynamics and its running time.

For every fixed graph \(F\) with \(\delta(F)\ge1\), Theorem 1.3 proves, for fixed \(p\in(0,1)\),

\[
\mathrm{wsat}(G(n,p),F)=\mathrm{wsat}(K_n,F)(1+o(1))
\quad\text{with high probability.}
\]

Theorem 1.4 gives exact stability in a sparser regime under a structural-size hypothesis: if \(\mathrm{wsat}(n,F)\ge(\delta(F)-1)n+D\) for every \(n\), then for some integer \(k\) and constant \(d_F\), \(\mathrm{wsat}(n,F)=(\delta(F)-1)n+d_F\) eventually, and

\[
p\ge n^{-1/(2k+3)}\log n
\quad\Longrightarrow\quad
\mathrm{wsat}(G(n,p),F)=\mathrm{wsat}(n,F)
\]

with high probability. The paper verifies the hypothesis for complete and complete bipartite graphs, all graphs of minimum degree 1, and connected minimum-degree-2 graphs or those without a cut edge. At the other end, Theorem 4.2 shows \(\mathrm{wsat}(G(n,p),F)=e(G(n,p))(1+o(1))\) w.h.p. when \(p\ll n^{-1/\mu(F)}\), with \(\mu(F)=\max\{m(F),(e(F)-1)/(v(F)-2)\}\) (and the stated convention for \(v(F)=2\)).

## Proof routes and limits

For constant \(p\), the proof combines Alon’s linear asymptotic for \(\mathrm{wsat}(n,F)\), a random-graph clique-power partition into growing blocks, and common-neighbour estimates to connect the block constructions while paying only \(o(n)\) additional edges. Exact stability uses upper and lower bounds on \(\mathrm{wsat}(G,F)\), a clique core, and Hamilton-path powers in common neighbourhoods to add edges in an explicit weak-saturation order. The small-\(p\) result counts copies of \(F\) and compares their number with the host edge count.

The results concern the size of a smallest weakly saturated subgraph in a random host. They do not estimate the number of synchronous bootstrap rounds and cannot prove an upper bound on \(M_H(n)\) without a separate order-to-round argument.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/kalinichenko24`).
