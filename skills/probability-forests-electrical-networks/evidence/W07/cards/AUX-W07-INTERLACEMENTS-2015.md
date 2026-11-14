# AUX-W07-INTERLACEMENTS-2015 — random interlacements and the WUSF

**Source and read copy.** Tom Hutchcroft, “Interlacements and the Wired Uniform Spanning Forest,” arXiv:1512.08509v2 (18 Oct. 2016); published in *Annals of Probability* 46(2) (2018), 1170–1200, DOI [10.1214/17-AOP1203](https://doi.org/10.1214/17-AOP1203). Read the complete 25-physical-page arXiv v2 PDF at evidence/fulltexts/AUX-W07-INTERLACEMENTS-2015.pdf, SHA-256 817dafd0a8f0e09534835885af6c87f9fb1263a2c0e2b7e488f8b83f8bf2c948, including the references. D05 checked acquisition identity only; W07 read the mathematical text. Render-checked physical pp. 4 and 6 for Theorems 2.1 and 2.4.

## Interlacement Aldous–Broder sampler and one-endedness

The paper works with infinite, locally finite, connected graphs for its basic WUSF construction, then formulates the network extensions where stated. For a transient graph, the interlacement process replaces the walk in Aldous–Broder: at time \(t\), let \(e_t(v)\) be the oriented edge used by the first interlacement trajectory with label greater than \(t\) when it enters \(v\). Theorem 1.1 (PDF p. 2) states that \(AB_t(\mathcal I)=\{-e_t(v):v\in V\}\) has the oriented WUSF law. The minus sign reverses the entering edge, so the tree edge is oriented outward from \(v\) toward the predecessor on that trajectory. The process is built from the Poisson point process on doubly infinite trajectories modulo time-shift, with the Sznitman intensity measure; for a finite vertex set \(K\), the probability it is hit in a time interval of length \(s\) is \(1-e^{-s\operatorname{Cap}(K)}\) (Lemma 3.4, PDF pp. 8–9).

Theorem 2.1 (PDF pp. 4–5) gives a sufficient anchored-isoperimetric condition for every WUSF component to be one-ended. In the notation of the paper, the graph has \(c_0=\inf_e c(e)>0\), satisfies the anchored \(f\)-isoperimetric inequality for an increasing \(f\) with \(f(t)\le t\) and \(f(2t)\le\alpha f(t)\), and \(f\) satisfies both
\[
\int_{c_0}^{\infty} f(t)^{-2}\,dt<\infty,
\qquad
\int_{c_0}^{\infty}\exp\!\left[-\varepsilon\left(\int_s^{\infty} f(t)^{-2}\,dt\right)^{-1}\right]ds<\infty\quad\text{for every }\varepsilon>0.
\]
The anchored-expansion and anchored \(d\)-dimensional isoperimetric examples with \(d>2\) are consequences, not replacements for the displayed hypotheses.

Proof chain: the interlacement process gives the exact capacity formula; the capacity lower bound in Theorem 5.2 turns anchored isoperimetry into a lower bound for the capacity of finite connected sets. Lemma 5.5 converts the resulting path/capacity estimate into finiteness of the component in the past after a positive-time interlacement cut. Lemma 5.1 is the final one-endedness criterion: if for every vertex and every \(\varepsilon>0\) that cut-past component is finite almost surely, every WUSF component is one-ended. These steps depend on the interlacement Aldous–Broder dynamics and are specific to the wired forest.

## Ends, unimodularity, and limits of transfer

Theorem 2.2 (PDF pp. 5–6) says the total number of excessive ends, defined as the sum over components of (number of ends minus one), is almost surely a nonrandom constant for every graph in the stated setting; its proof separates destructible and indestructible ends and uses stationarity/ergodicity of the Aldous–Broder dynamics. Corollary 2.3 says finite edge additions or deletions preserve this number almost surely. Theorem 2.4 (PDF p. 6) proves that every WUSF component is one-ended almost surely for a transient unimodular random rooted network, without a finite expected root-degree assumption; the proof combines the interlacement dynamics with the mass-transport principle.

Theorem 6.1 (PDF pp. 17–19) constructs bounded-degree rough-isometric graphs with different WUSF end behavior. Stretching edges according to distance from the root and duplicating path edges changes the branching survival probabilities; for the paper's parameters, one graph has an uncountably-ended WUSF component while another has all components one-ended. Thus rough isometry alone does not preserve WUSF one-endedness.

**W07 use boundary.** This is a WUSF result for transient graphs/networks. It provides proof techniques and a model boundary for W07 end questions, but it proves no FMSF/WMSF assertion and cannot be transferred solely because both objects are forests. In particular, it does not settle a minimal-forest connectivity or end-count interface.

## Full reading coverage

All 25 physical PDF pages were read. evidence/W07/reading_coverage.json records: introduction and setup (pp. 1–3); anchored-isoperimetric and excessive-end results (pp. 4–6); interlacement trajectory space, intensity, and capacity lemmas (pp. 7–10); sampler and dynamics (pp. 10–12); one-endedness criteria and proofs (pp. 12–17); rough-isometry counterexample (pp. 17–20); concluding discussion (pp. 20–22); acknowledgements and references (pp. 23–25). Review status is pending.
