> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-002 — The random graph process is globally synchronizing

## Identity and reading record

- Vishesh Jain, Clayton Mizgerd, Mehtaab Sawhney. arXiv:2501.12205v1, 21 January 2025; 11-page author version. Published DOI: 10.1112/blms.70226. Official record: <https://arxiv.org/abs/2501.12205v1>.
- Local PDF: ../pdfs/PGEL-002.pdf
- SHA-256: efcbd4e7c7e68d3460a5cd9cbbe2e5b418f95fd4c7b958dc360424af33d136b5.
- Read all 11 PDF pages. Theorem statements and constants on pages 2–3 and the random-process proof on pages 9–11 were checked against rendered pages. Coverage: ../reading_coverage.json.
- Review pending. The source read is arXiv v1; no claim is made that every displayed statement matches the later journal version.

## Model, energy, and meaning of “global”

For a finite undirected graph \(G=(V,E)\), the model has identical natural frequencies, unit positive coupling on each edge, and bidirectional interactions. The phase equation is the gradient flow of
\[
E_G(\theta)=\frac12\sum_{u,v}A_{uv}\bigl(1-\cos(\theta_u-\theta_v)\bigr),
\]
up to the paper's sign convention for gradient descent. A common phase shift leaves the energy and dynamics unchanged; the authors work modulo this symmetry (or on a fixed-sum slice).

The definition on PDF p. 1 is probabilistic in the initial condition: a fixed graph is **globally synchronizing** when for almost every initial phase vector in \((S^1)^V\), the dynamics converges to full in-phase synchronization. This is not the assertion that every initial condition synchronizes, nor that the energy has no other critical points. “With high probability” in Theorem 1.2 is a separate probability over the random graph process.

## Main random-process theorem

Let \(G(n,m)\) be built from the empty graph by adding a uniformly chosen missing edge at each step, and let \(\tau=\min\{m:G(n,m)\text{ is connected}\}\). **Theorem 1.2 (PDF p. 2)** states that with high probability, **simultaneously for every \(m\ge\tau\)**, \(G(n,m)\) is globally synchronizing. This simultaneous quantifier is stronger than a separate high-probability statement for each fixed \(m\), and matters because synchronization is not monotone under adding edges.

The proof (§3, PDF pp. 9–11) couples the process to \(G_p\) using independent uniform edge labels. Around the random connectivity parameter \(\lambda\), it takes a low-degree defect set \(B\) in a narrow window \((\sigma,\omega)\) and \(W=V\setminus B\). With high probability \(B\) is small, has no internal edges, has at most one neighbor per vertex, and degrees are bounded; the core has spectral expansion and controlled degrees. The deterministic defective-expander theorem applies to all \(p\in[\lambda,\omega)\) at once. For \(p\ge\omega=5\log n/n\), the proof invokes the earlier expander synchronization results and a union bound over the process. The probability statement concerns the random graph; each resulting graph's synchronization property still quantifies almost every initial phase.

## Deterministic defective-expander interface

Definition 1.3 (PDF p. 2) calls \(G\) an \((n,d,\alpha)\)-expander if
\[
|V|=n,\qquad \|A_G-(d/n)J\|\le \alpha d/2.
\]

**Theorem 1.6 (numbered statement on PDF p. 3; proof pp. 4–8).** Fix \(\epsilon\in(0,1)\), \(\alpha\in(0,1/5)\), and \(d\) with \(\alpha d\ge1\). Let \(V=W\cup B\); assume \(G\) has no isolated vertices and is an \((n,d,\alpha)\)-expander. Let \(d_{\max}\) and \(d_{\min}\) be the maximum and minimum degrees in \(G[W]\), with \(d_{\min}\ge \ell:=2(\epsilon+\alpha)d\). Set
\[
\delta=\frac{\epsilon d}{d_{\max}-2\epsilon d}.
\]
Assume
\[
\frac{8(1+\delta)(d_{\max}+1)}
{\delta^2\exp\!\left(\frac{\epsilon}{40\alpha}\log(1+\delta)\right)}\le1,
\qquad
\frac{8}{d_{\max}-4\epsilon d}\le1.
\]
Also assume (B1) \(|B|\le\alpha n\); (B2) no edge has both endpoints in \(B\); (B3) \(\deg(v)\le d_{\max}+1\) for each \(v\in B\); and (B4) every \(v\in V\) has at most one neighbor in \(B\). Then \(G\) is globally synchronizing.

The proof excludes non-synchronous stable states using the geometry of phase arcs, expansion bounds on the core, and an iterative angular-growth argument. It handles low-degree defects through (B1)–(B4); it is not a signed-graph theorem. The separate Theorem 1.5 (PDF p. 3) gives a uniform-degree expander criterion but does not apply at the connectivity hitting time, where degree-one vertices occur with high probability.

## Scope and transfer limits

- This paper studies **symmetric, positive, unit-strength** edges. It neither addresses signed weights nor directed/oriented couplings.
- It proves an a.e.-initial-condition synchronization property, not a landscape theorem that every critical point is synchronous.
- It does not settle C118's signed complete graph or any random 3-regular conjecture. Its useful role here is the exact quantifier distinction and a comparison theorem for positive undirected sparse graphs.
- The proof depends on prior deterministic expander results for the dense part of the process. Treat those cited results as external dependencies, not as newly proved lemmas in this paper.
