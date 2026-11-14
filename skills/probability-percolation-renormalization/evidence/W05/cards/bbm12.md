# bbm12 — Graph bootstrap percolation

**Reading status:** `fulltext_read`; complete corrected arXiv v2, PDF pp. 1–27, read. The threshold statements and key estimates were checked on rendered pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** József Balogh, Béla Bollobás, and Robert Morris, “Graph Bootstrap Percolation,” arXiv:1107.1381v2 (2012); *Random Structures & Algorithms* 41 (2012), 413–440, DOI [10.1002/rsa.20458](https://doi.org/10.1002/rsa.20458). Local PDF SHA-256: `d3835e6e8274f94eb883d1f58c6451ba457f634c1c32fa14af7bd1a7a54db2f6`.

## Model and threshold results

For a fixed graph \(H\), the synchronous \(H\)-edge-bootstrap process on \(K_n\) starts from \(G_0\) and adds at round \(t+1\) every missing edge that completes a copy of \(H\) whose other edges are already in \(G_t\). The critical probability \(p_c(n,H)\) is the infimum of \(p\) for which \(G(n,p)\) percolates with probability at least \(1/2\). This paper studies the probability of eventual complete closure, not the maximum number of rounds over starting graphs.

For \(r\ge4\), set

\[
\lambda(r)=\frac{\binom r2-2}{r-2}.
\]

Theorem 1 gives, for fixed \(r\) and all sufficiently large \(n\),

\[
c(r)^{-1}(\log n)^{-1}n^{-1/\lambda(r)}\le p_c(n,K_r)
\le (\log n)n^{-1/\lambda(r)}.
\]

For \(K_4\), Theorem 2 sharpens this to

\[
\frac{1}{4\sqrt{n\log n}}\le p_c(n,K_4)
\le\frac{24}{\sqrt{n\log n}}.
\]

The local PDF is the corrected arXiv v2. Its p. 3 note says the published version stated a stronger upper bound because of an error in the proof of Proposition 23; do not import that superseded claim. The \(K_3\) process is exactly graph connectivity, so its threshold is the Erdős–Rényi connectivity threshold.

## Proof mechanisms and scope

For the general upper bound (§2), the authors use balanced graphs and construct a chain of overlapping copies of \(H\), rooted at a specified edge. A first- and second-moment count finds a small internally spanned copy; a sprinkling stage grows it until all but a negligible fraction of edges are infected, and a final dense-set argument completes the graph. For the lower bound (§3), a witness-set exploration traces the earlier edges needed to infect a target edge. Extremal bounds on the witness graph and an Aizenman–Lebowitz intermediate-scale lemma permit a first-moment estimate showing that a fixed edge is unlikely to become infected below the claimed scale.

The separate \(K_4\) proof (§4) uses a clique-merging process. Internal-spanning edge counts give the lower bound; the upper bound counts internally spanned cliques by a second-moment argument and then uses sprinkling to grow a logarithmic clique to a linear one and finish. Section 5 treats other graphs and lists open problems.

The theorem is about eventual percolation from an Erdős–Rényi **edge** host. It does not bound maximum running time, vertex-bootstrap time, zero-forcing time, or a dependent infection process. The balanced-graph upper-bound argument and the special \(K_4\) argument have different scopes.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bbm12`).
