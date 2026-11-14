# dctzd16 — Sharpness on \(\mathbb Z^d\)

**Reading status:** `fulltext_read`, complete six-page note, PDF pp. 1–6. Bibliographic identity matched the PDF title page and arXiv record. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Hugo Duminil-Copin and Vincent Tassion, “A New Proof of the Sharpness of the Phase Transition for Bernoulli Percolation on \(\mathbb Z^d\),” arXiv:1502.03051v1 (2015); *Enseign. Math.* 62 (2016), 199–206, DOI [10.4171/LEM/62-1/2-12](https://doi.org/10.4171/LEM/62-1/2-12).

## Result and scope

Theorem 1.1 (PDF pp. 2–3) concerns nearest-neighbour **iid bond** percolation on \(\mathbb Z^d\), \(d\ge2\). It proves \(\widetilde p_c=p_c\), that for every \(p<p_c\) there is \(c(p)>0\) with

\[
\mathbb P_p(0\leftrightarrow \partial\Lambda_n)\le e^{-c(p)n},
\]

and, for \(p>p_c\),

\[
\theta(p)\ge \frac{p-p_c}{p(1-p_c)}.
\]

Here \(\widetilde p_c=\sup\{p:\exists\text{ finite }S\ni0,\ \phi_p(S)<1\}\), with

\[
\phi_p(S)=p\sum_{\substack{x\in S,\ y\notin S\\ |x-y|_1=1}}
\mathbb P_p(0\leftrightarrow x\text{ by a path contained in }S).
\]

The sum is over the outward **oriented edge boundary**. This is not a result for dependent percolation, arbitrary transitive graphs, oriented max-flow, or bootstrap rules.

## Proof chain read

1. If \(p<p_c=\widetilde p_c\), choose a finite witness \(S\) with \(\phi_p(S)<1\). Put \(S\) in a box of scale \(L\).
2. Reveal the cluster of 0 inside successive translates of \(S\). Decompose according to the cluster’s internal boundary; the boundary-edge states and unexplored exterior remain independent under product bond measure.
3. The resulting one-step estimate multiplies the one-arm probability by at most \(\phi_p(S)\). Iteration across \(k\) blocks gives geometric decay in \(k\), hence \(e^{-cn}\) after changing constants by the fixed block scale.
4. For the supercritical lower bound, Lemma 2.1 (PDF pp. 4–5) combines Russo’s formula with a pivotal-boundary estimate:

   \[
   \frac{d}{dp}\mathbb P_p(0\leftrightarrow\partial\Lambda_n)
   \ge \frac{\inf_{S\subseteq\Lambda_n,\,0\in S}\phi_p(S)}{p(1-p)}
   \bigl(1-\mathbb P_p(0\leftrightarrow\partial\Lambda_n)\bigr).
   \]

   Integrating from \(\widetilde p_c\) to \(p\), then sending \(n\to\infty\), yields the stated lower bound.

## Use in this skill

This supplies a model-specific finite-size criterion and sharpness proof pattern. A transfer to A030, C115, C116 or a bootstrap process needs a separate coupling, pivotal formula, and boundary/independence argument. Merely finding a finite set with a numerically small boundary expression does not establish the infinite-volume theorem.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/dctzd16`).
