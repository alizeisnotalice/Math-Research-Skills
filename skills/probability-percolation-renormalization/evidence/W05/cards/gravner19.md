# gravner19 — Maximal spanning time for neighborhood growth on the Hamming plane

**Reading status:** `fulltext_read`; complete 22-page arXiv v1, PDF pp. 1–22, read. Main theorem statements and the upper/lower-bound mechanisms were checked on rendered PDF pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Janko Gravner, J. E. Paguyo, and Erik Slivken, “Maximal Spanning Time for Neighborhood Growth on the Hamming Plane,” arXiv:1708.01855v1 (2017); *SIAM Journal on Discrete Mathematics* 33(2) (2019), 976–993, DOI [10.1137/17M1153807](https://doi.org/10.1137/17M1153807). Local PDF SHA-256: `8779c413da4ec12f02adb8ad9bca20d2114ebcff12e822755d3c306e126daafb`.

## Model and theorems

The state space is the Hamming plane \(\mathbb Z_+^2\): the neighbourhood of \((i,j)\) consists of its entire horizontal and vertical lines. A finite zero-set \(Z\), a Young diagram formed as a finite union of rectangles, specifies the update: an empty site becomes occupied when its pair of current row/column counts lies outside \(Z\); occupied sites remain occupied. Let \(\tau(Z,A)\) be the first time a finite spanning seed \(A\) fills the plane and \(\mu(Z)=\sup_A\tau(Z,A)\). For the largest square \(R_{s,s}\subseteq Z\), Theorems 1.1–1.4 give:

\[
Z\subseteq R_{m,n}\Longrightarrow \mu(Z)\le 2mn+5;
\qquad \mu_{\rm en}(Z)-2\le\mu_{\rm th}(Z)\le2\mu_{\rm en}(Z);
\]

\[
\mu_{\rm en}(Z)\le4s+1,\quad \mu_{\rm th}(Z)\le8s+2,
\qquad
\mu_{\rm en}(Z)\ge\sqrt{s},\quad
\mu(Z)\ge\mu_{\rm th}(Z)\ge\sqrt{s-1}\quad(Z\ne\varnothing).
\]

Here \(\mu_{\rm th}\) restricts to finite spanning thin initial sets, and \(\mu_{\rm en}\) is the maximum time from the empty set in the enhanced process, which adds fixed weakly decreasing row/column offsets of finite support. The two quantities compare the time dynamics with seed geometry; \(\mu(Z)\) itself is not monotone under inclusion of zero-sets.

## Proof mechanisms and boundary

Theorem 1.1 counts the times when a row or column becomes saturated/covered, then uses a cross-line lemma: among two non-neighbouring new sites, at least one of the row-column intersection sites was already occupied. This forces enough lines to be covered within the stated \(2mn+5\) bound. For the enhanced comparison, the authors encode offsets as Young diagrams and use infimal sums; spanning is equivalent to \(Z\subseteq R\mathbin{\Box}C\). A thin-set comparison proves Theorem 1.2, and counting distinct row/column lengths gives \(4s+1\) and \(8s+2\). The lower bound uses staircase Young diagrams and a product rule for their infimal sum to construct slowly filling enhanced processes, then transfers to thin seeds.

This paper proves finite-time bounds for a specific Hamming-plane neighbourhood rule. It does not bound the minimum cardinality \(\gamma(Z)\) of a spanning seed or prove \(\gamma(Z)\ge |Z|/2\). For A200, the 2017 Gravner–Sivakoff–Slivken paper supplies the rectangle-to-plane spanning equivalence and finite-box reduction for the same rule; the stronger general seed-size bound still requires a separate proof or counterexample.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/gravner19`).
