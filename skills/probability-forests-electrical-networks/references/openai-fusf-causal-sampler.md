# Finite-tree response and causal Brownian sampler

Source: OpenAI, *The free uniform spanning forest is a factor of IID*,
version dated 25 September 2026, PDF SHA-256
`478f5137621e0b3b41f2b9ab0bd45133d6d03f2c4e68a1eecc8fbc60344aac84`.
The source file is 19 PDF pages.  The finite weighted-tree calculation is
Lemma 2.1 on PDF pp. 4--5; the deterministic inverse is Lemma 4.1 on pp.
11--12; the sampler is Proposition 4.2 on pp. 12--13.
Pinned primary source: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf>.

For a finite connected graph, give a spanning tree (T) mass proportional to
(prod_{f\in T}c_f), where all (c_f>0), and put (h_f=\log c_f).  The
matrix-tree theorem gives

\[
  \partial_{h_f}p_e=\operatorname{Cov}(1_{e\in T},1_{f\in T}).
\]

For distinct edges the determinant differentiation in (2.3) makes this
covariance nonpositive.  Because every tree has fixed cardinality,
(\sum_f\operatorname{Cov}(1_{e\in T},1_{f\in T})=0).  The diagonal is
(p_e(1-p_e)); hence

\[
 \sum_f|\partial_{h_f}p_e|=2p_e(1-p_e)\leq\tfrac12.
\]

The checker in `scripts/check_finite_tree_response.py` independently verifies
this exact finite identity by rational spanning-tree enumeration.  It is a
finite audit only: it does not prove a free-exhaustion limit, a
strongly-Rayleigh extension, or an FIID coding.

For the causal sampler, Lemma 4.1 requires a countable coordinate set and a
jointly Borel drift (b:[0,\infty)\times\mathbb R^I\to[0,1]^I) satisfying
one sup-norm Lipschitz bound (L<\infty) on pairs with bounded coordinate
differences.  Picard iterates converge uniformly across coordinates on each
finite time interval, yielding a unique Borel causal inverse.  Proposition
4.2 additionally requires finite tilts along sitewise finite exhaustions with
that same response constant.  It then maps independent Brownian paths to the
target binary law by integer-time slopes.  For FUSF the source obtains
(L=1/2) through a separately proved free-exhaustion response construction.
No finitary radius follows; arbitrary infinite laws and the paper's
strongly-Rayleigh/determinantal extension require their stated extra work.
