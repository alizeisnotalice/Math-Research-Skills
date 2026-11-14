# LPS2006MSF — minimal spanning forests

**Source/version.** Russell Lyons, Yuval Peres, and Oded Schramm, “Minimal Spanning Forests,” *Annals of Probability* 34(5) (2006), 1665–1692, DOI 10.1214/009117906000000269. Read the complete 28-page local PDF, including all six sections and references. Local PDF pagination is used.

## Model and definitions (§§1–2; PDF pp. 1–6)

The paper works with connected locally finite graphs and i.i.d. continuous uniform edge labels \(U(e)\). FMSF removes an edge that is maximal on a finite cycle; WMSF uses the extended-cycle/cut characterization that also detects a bi-infinite alternative path. These are undirected forests; the orientation used in the invasion-tree proof is auxiliary. Each component is infinite. The labels have no conductance weights: do not conflate these constructions with weighted UST/FSF/WSF.

## Equality criterion: almost-everywhere uniqueness (§3; PDF p. 9)

**Proposition 3.6.** On any connected graph, FMSF=WMSF iff Bernoulli bond percolation has a.s. at most one infinite cluster for **Lebesgue-a.e.** parameter \(p\in(0,1)\). This is not uniqueness a.s. for every \(p\). For each edge \(e=\{x,y\}\), let \(Z_w(e),Z_f(e)\) be its wired/free cycle thresholds. The forests differ iff for some edge \(e\),

\[
\mathbb P[Z_w(e)<U(e)\le Z_f(e)]>0.
\]

Let \(A(e)\) be the event that \(x,y\) lie in distinct infinite clusters of \((G\setminus e)[U(e)]\). The proof sandwiches \(A(e)\) between the strict-threshold event and its closed-endpoint version; equality endpoints have probability zero because \(U(e)\) is continuous. Countability of \(E\), followed by integration over the edge’s uniform label, identifies disagreement with failure of uniqueness on a positive-Lebesgue-measure parameter set. On quasi-transitive graphs the criterion is equivalent to \(p_c=p_u\).

## WMSF one-endedness (§3; PDF pp. 11–13)

**Theorem 3.12 / Theorem 1.1.** For a unimodular quasi-transitive locally finite graph, if \(\theta(p_c)=0\), every WMSF component is one-ended a.s.; in the transitive case its expected degree is 2. The proof enumerates invasion-tree edges in order of addition and uses Lemma 3.11 (every invasion tree meets an infinite \(p\)-cluster for \(p>p_c\)) to show the limsup edge label is \(p_c\). Orient each WMSF edge toward the invasion end; MTP gives expected indegree one and hence expected undirected degree two. Together with the at-most-two-ends input, a hypothetical two-ended trunk would have a last edge above \(p_c+\varepsilon\); sending mass along the trunk to that edge violates MTP. The quasi-transitive-to-transitive reduction uses an auxiliary random relabeling of orbit representatives; this is why local finiteness/quasi-transitivity and unimodularity remain hypotheses.

## FMSF augmentation: theorem and resampling proof (§3; PDF pp. 16–17)

**Theorem 3.22.** For every connected locally finite graph and \(\varepsilon\in(0,1)\), if \(\mathcal F_f\) is FMSF and \(\omega\) is an independent Bernoulli(\(\varepsilon\)) edge set, then \(\mathcal F_f\cup\omega\) is connected a.s. The crucial input is Lemma 3.23, not an independent-copy path-union argument: conditional on \(\mathcal F_f\), on a finite edge set \(A\) absent from FMSF, the normalized residual labels

\[
\left\{\frac{1-U(e)}{1-Z_f(e)}:e\in A\right\}
\]

are i.i.d. uniform on \([0,1]\). To prove this, replace \(U(e)\) by 1 on \(A\); if \(A\cap\mathcal F_f=\varnothing\), every cut minimum and the forest/cut thresholds are unchanged. Absence is equivalent to the strict threshold inequalities, giving the conditional product-uniform law. This resampling couples the augmentation to

\[
\xi=\{e:1-U(e)\ge(1-\varepsilon)(1-Z_f(e))\}.
\]

For a nonempty cut \(C\), put \(\alpha=\inf_{e\in C}U(e)\) and choose \(e\in C\) with \(1-U(e)>(1-\varepsilon)(1-\alpha)\). Since \(Z_f(e)\ge\alpha\), \(e\in\xi\). Thus every nonempty cut is crossed, proving connectivity. The theorem is FMSF plus independent Bernoulli edges; it is not an FSF invariant-augmentation result.

## Other full-text results and limits (§§3–6; PDF pp. 6–28)

The complete read also covers the percolation-cluster correspondence, tail triviality of FMSF/WMSF, WMSF “thinness” at \(p_c\), planar duality, and examples/questions. Proposition 3.13 says each FMSF component meets at most one infinite \(p_u\)-cluster, with equality under quasi-transitivity and \(p_u>p_c\). Proposition 3.5(e) says a unimodular transitive graph with WMSF\(\ne\)FMSF has an FMSF component with uncountably many ends a.s. Planar Proposition 4.4 makes FMSF a tree under its planar hypotheses. Proposition 5.1 gives the exact finite MST positive-correlation example; the local rational enumeration is in `evidence/W07/examples/verify_finite_examples.py` and is only a finite check.

The paper invokes earlier end-count and percolation results at specific points; where a proof is referred out or left to the reader, the card does not reclassify that step as a new proof. Do not transfer these minimal-forest conclusions to uniform forests, or use the FMSF-plus-noise theorem as a statement about FSF.
