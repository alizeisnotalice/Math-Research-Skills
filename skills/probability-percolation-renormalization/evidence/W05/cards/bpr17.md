# bpr17 — Exact K4 running time and graph-bootstrap baseline

**Reading status:** `fulltext_read`; complete 17-page article read (PDF pp. 1–17), including the K4 upper induction, the random long-chain lower bound, and deterministic constructions. Theorem statements and the fixed-$r$ exponent were visually checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Béla Bollobás, Michal Przykucki, Oliver Riordan, and Julian Sahasrabudhe, “On the Maximum Running Time in Graph Bootstrap Percolation,” *Electronic Journal of Combinatorics* 24(2) (2017), P2.16, arXiv [1510.07096](https://arxiv.org/abs/1510.07096). Local PDF SHA-256: `e5b9cfa59cebf8349becbe7b99a701caea7c963f956affb0d130a05f815fb8cd`.

## Model and exact results

For fixed $H=K_r$, start with any $G_0\subseteq K_n$. In each synchronous round add **all** missing edges whose addition completes a new $K_r$ using edges present at the beginning of the round. $M_r(n)$ is the maximum number of non-stationary rounds over all initial graphs, whether or not the closure is complete.

Theorem 1 (PDF p. 3) proves

\[
M_4(n)=n-3\quad(n\ge3).
\]

The proof gives a slow construction and an upper bound via clique merging and an induction on the time of the last-added edges (PDF pp. 3–5). The introduction records $M_3(n)=\lceil\log_2(n-1)\rceil$. Theorem 2 (PDF p. 3) proves, for each fixed $r\ge5$,

\[
M_r(n)\ge n^{2-\alpha_r-o(1)},\qquad
\alpha_r=\frac{r-2}{\binom r2-2}.
\]

It does not prove an exact exponent or an upper bound $o(n^2)$ for every fixed $r\ge5$.

## Lower-bound proof mechanisms

For Theorem 2, define a good $K_r$-chain: each new $K_r$ introduces a designated new edge without an external $K_r^{-}$ that would create an earlier shortcut. A minimal-chain incidence count gives $\alpha_r(b-1)\le c-2$, relating the number $b$ of added edges to the number $c$ of candidate $K_r$'s. A union bound makes dangerous subsets unlikely; candidate completions are exposed independently, with success probability bounded below (at least .99 after the global bad events in the selected regime). Trying $m=\lceil\log n\rceil$ candidates per step yields a chain of length $n^{2-\alpha_r-o(1)}$ with positive probability. Section 4 supplies deterministic lower constructions: for $K_5$, at least $n^{3/2}/200$, extended to $r\ge6$ with constants depending on $r$. A set-system argument controls external triangles and degrees so only the prescribed next edge is added in each round.

**Visual check:** rendered PDF p. 3 and checked both theorem statements and $\alpha_r$ against the page image. The complete proof sections, not only these displayed conclusions, were read.

## Scope

This is synchronous **edge** bootstrap. It is not vertex-threshold bootstrap, random-set zero forcing, PZF, or weak saturation’s sequential edge-ordering problem. The theorem maximizes over all initial graphs, so it must not be silently restated only for percolating initial graphs. For C189, the paper gives a fixed-$r$ lower bound; it does not settle whether $M_{K_5}(n)=o(n^2)$. Exhaustive small-$n$ enumeration is only a finite audit and cannot replace the all-$n$ proof.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bpr17`).
