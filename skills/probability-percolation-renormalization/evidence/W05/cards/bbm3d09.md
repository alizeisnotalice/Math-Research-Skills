# bbm3d09 — Bootstrap percolation in three dimensions

**Reading status:** `fulltext_read`; complete local 53-page paper read, PDF pp. 1–53. The critical-threshold formula and the intermediate semi-percolation theorem were checked on rendered original pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** József Balogh, Béla Bollobás, and Robert Morris, “Bootstrap Percolation in Three Dimensions,” *The Annals of Probability* 37(4) (2009), 1329–1380, DOI [10.1214/08-AOP433](https://doi.org/10.1214/08-AOP433); arXiv:0806.4485v2. Local PDF SHA-256: `25f6de418c1896a3c7a5c7565803445211a02b4aedc8563af921f73461867d14`.

## Model and threshold theorem

On the nearest-neighbour grid ([n]^3), initially infected sites are iid Bernoulli((p)); an uninfected site is added when it has at least three infected neighbours. Theorem 1 proves

\[
p_c([n]^3,3)=\frac{\lambda(3,3)+o(1)}{\log\log n},\qquad
\lambda(3,3)\approx0.4039,
\]

as (n\to\infty), with the paper’s natural-log convention. Here the constant is defined from the functions in equations (1)–(3):

\[
\beta_k(u)=\tfrac12-\tfrac12(1-u)^k+\tfrac12\sqrt{1+(4u-2)(1-u)^k+(1-u)^{2k}},\quad
g_k(z)=-\log\beta_k(1-e^{-z}),\quad
\lambda(d,r)=\int_0^\infty g_{r-1}(z^{d-r+1})\,dz.
\]

## Proof architecture and limits

The proof first establishes general upper bounds by recursively growing semi-percolating layers in the structured boxes (C^*([n]^d\times[2]^\ell,r)). The key seed step reduces growth to a lower-dimensional ((r-1))-neighbour semi-percolation event; an (L)-gap recurrence and FKG bounds control its probability. For the lower bound, the authors define internally spanned rectangle hierarchies and a crossing algorithm. They track blockers, savers and last-chance configurations to bound rectangle growth, use Reimer’s inequality where disjoint occurrence is not enough, and obtain the needed rare-event estimate (Theorem 13 and Corollary 14). A two-colour construction and an admissible-sequence count then give the lower bound in dimension three; the general upper-bound theorem supplies the other side.

This is a sharp threshold for one fixed nearest-neighbour vertex-bootstrap rule and random initial states. It does not give an infection-time tail for general update families, nor a maximum-time bound for graph-bootstrap or zero forcing. The proof’s finite geometric construction and dimension-specific estimates must not be treated as a universal renormalization theorem.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bbm3d09`).
