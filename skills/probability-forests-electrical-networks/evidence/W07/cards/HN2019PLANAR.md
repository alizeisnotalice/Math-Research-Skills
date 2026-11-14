# HN2019PLANAR — uniform spanning forests of planar graphs

**Source:** Tom Hutchcroft and Asaf Nachmias, “Uniform Spanning Forests of Planar Graphs,” *Forum of Mathematics, Sigma* 7 (2019), e29, DOI 10.1017/fms.2019.14; arXiv:1603.07320v2. Complete 39-page PDF read (SHA-256 `b0b28509f05baaa418e00cd0cf8cb58ca16dc5e22ef738a37bcac61bf1fe3f15`).

## Main results and hypotheses

Theorem 1.1 (PDF p. 2) states that the FUSF is almost surely connected on a bounded-degree proper plane network with edge conductances bounded above. Theorem 1.2 (PDF p. 2) states that every WUSF component is almost surely one-ended on a bounded-codegree proper plane network with edge resistances bounded above. These are dual but separately formulated hypotheses; do not silently replace a conductance bound by a resistance bound or drop properness/degree assumptions.

Under the additional transient polyhedral proper-plane and bounded-local-geometry condition (M_G<\infty), Theorems 1.3–1.5 (PDF pp. 5–6) give critical-radius tail estimates of order (R^{-1}) for the hyperbolic diameter of FUSF paths and WUSF pasts, and order (R^{-1/2}) for WUSF hyperbolic past area. Corollary 1.6 gives an (R^{-1/2}) tail for the graph-length of FUSF paths under uniform transience. The constants and radii depend on the stated graph geometry; these are not universal estimates for arbitrary planar graphs.

## Proof of WUSF one-endedness

The reduction and circle-packing setup are in §3 (PDF pp. 13–19). After removing peninsula obstructions and triangulating, the proof studies the event (A_e) that an edge separates two infinite WUSF components. For a compact set (K), expose the local leftmost/rightmost finite-tree paths from the endpoint sides to the boundary at scale ε. The strong spatial Markov property and Kirchhoff’s formula bound the conditional probability of (e\in F) by its conductance times an effective resistance between the two exposed paths in the remaining wired domain. Random circle/ring-annulus estimates and the random-set energy lemma force this resistance to (O(1/n(\epsilon))\to0). Thus (P(A_e)=0); planar duality then yields FUSF connectivity and the WUSF one-ended conclusion in the dual statement.

## Quantitative sections read

Sections 4.1–4.2 (PDF pp. 20–21) establish the double-circle-packing/ring-lemma framework. Sections 4.3–4.5 (pp. 22–34) combine random-walk/Brownian estimates, short-lived sets, Wilson’s algorithm, and second moments to obtain the WUSF-past and dual FUSF-path tail exponents. Section 4.6 (pp. 34–36) relates the required hypotheses to uniform transience. Section 5 (pp. 36–38) gives non-universal circle-packing/parabolic examples and open questions.

## Reading coverage

Complete PDF read: introduction and Theorems 1.1–1.6, §1 (PDF pp. 1–7); reductions and one-endedness/connectivity proof, §3 (pp. 13–19); quantitative circle-packing and tail proofs, §§4.1–4.6 (pp. 20–36); counterexamples/open questions, §5 (pp. 36–38); bibliography and closing matter (pp. 38–39). The intervening preliminaries in §2 (pp. 8–12) were also read. Physical PDF pages are cited.

## Scope boundary

These results exploit planarity, proper embeddings, and bounded local geometry. They do not establish connectivity or end structure on general Cayley graphs, nor do they resolve FSF/WSF mutual singularity in arbitrary unimodular settings.
