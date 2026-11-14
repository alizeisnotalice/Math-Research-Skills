# AUX-W07-WCD-2015 — wired cycle-breaking dynamics

**Source and read copy.** Tom Hutchcroft, “Wired Cycle-Breaking Dynamics for Uniform Spanning Forests,” arXiv:1504.03928v1 (2015); journal version *Annals of Probability* 44(6) (2016), 3879–3892, DOI 10.1214/15-AOP1063. Complete 15-page local arXiv PDF read, SHA-256 `8b361e93707ec376138d410eb3a3c1236af379b1480c4aa9c553ea0bf8f21f4d`. This is a supplementary W07 source, not a replacement for another ledger item.

## Network, oriented WUSF, and update (§§1–3; PDF pp. 1–9)

The base object is a transient, locally finite, connected network with positive conductances. A network random walk chooses each incident edge in proportion to its conductance; loops count twice in vertex conductance (c(v)). The WUSF is obtained through wired finite exhaustions. The oriented WUSF directs every edge toward infinity in its component. For an oriented edge (e), the update (U(F,e)) adds (e) and breaks the resulting cycle by deleting the edge selected by the wired cycle-breaking rule; orientations along the affected path are updated so the result again points toward infinity. When the edge creates no cycle, the outgoing edge at its tail is removed. The random-rooted dynamics at (v) selects an oriented edge leaving (v) with probability proportional to its conductance.

**Proposition 5 (PDF pp. 7–9).** The oriented WUSF is stationary for each vertex-rooted wired cycle-breaking dynamics. The proof first establishes finite wired-tree detailed balance (Lemma 6, p. 7): for two oriented trees related by a single update, their transition probabilities multiplied by their tree conductance products agree. For an exhaustion, couple the finite oriented wired trees and the infinite oriented WUSF so they converge almost surely. The update at a fixed edge converges in probability: outside a large ball the finite and infinite forests agree locally, and Lemma 7 (pp. 8–9) controls the event that the edge’s past reaches far enough to affect the update. Taking the limit of finite stationarity proves Proposition 5.

Corollary 8 (PDF p. 9) is update-tolerance: for every measurable forest event (A) and oriented edge (e),
\[
\mathrm{OWUSF}_G(U(A,e))\ge \frac{c(e)}{c(e_-)}\,\mathrm{OWUSF}_G(A),
\]
where (e_-) is the tail of (e). This is the positive-probability preservation estimate used by the end-count argument; it is not invariance of each event under the update.

## End-count results and proofs (§§4–5; PDF pp. 10–14)

**Theorem 3 (statement PDF p. 3; proof §4, pp. 10–11).** For any network, if the WUSF has more than one two-ended component with positive probability, then it has a component with at least three ends with positive probability. The proof chooses a finite sequence of edges crossing between two trunks. Repeatedly update along that sequence. At each step the component containing the next trunk vertex retains at least two ends; the final updated component has at least three ends. Corollary 8 multiplies the positive conductance ratios along this finite sequence, so the event remains positive probability.

**Theorem 1 (statement PDF p. 2; proof §5, pp. 11–13).** If ((G,\rho)) is a transient reversible random rooted network and \(\mathbb E[c(\rho)^{-1}]<\infty\), then every WUSF component is one-ended almost surely. The inverse-conductance bias (c(\rho)^{-1}/\mathbb E[c(\rho)^{-1}]) turns the reversible law into an equivalent unimodular law. The cited unimodular end theorem implies that each WUSF component has at most two ends; Theorem 3 then implies there is at most one two-ended component. If such a component existed with positive probability, stationarity of the network viewed from random walk and reversibility bound the probability that both the root and (X_n) lie in its trunk by twice a return-probability tail, which tends to zero by transience. The ergodic theorem would then force the probability that the root lies on the trunk to vanish, contradicting the assumed positive probability. Corollary 2 (p. 2) applies this to supercritical Galton–Watson trees conditioned to survive.

Example 9 (PDF pp. 13–14) shows the finite inverse-root-conductance moment is necessary: attach an infinite path at each vertex of a 3-regular tree, set the (n)-th path-edge conductance to (2^{-n}), and choose the reversible root law with infinite reciprocal-conductance expectation. The WUSF then has components with infinitely many ends with positive probability. The example is a boundary on the moment assumption, not a counterexample to Theorem 1.

## Full reading coverage and scope

Complete physical PDF pp. 1–15 were read. Coverage: introduction and statements (§1, pp. 1–3); network/forest and update definitions (§2, pp. 4–6); stationarity and update-tolerance (§3, pp. 6–9); Theorem 3 proof (§4, pp. 10–11); Theorem 1 proof and Example 9 (§5, pp. 11–14); references (p. 15). Rendered pp. 2, 7–10, and 12–13 to check theorem hypotheses, detailed balance, update-tolerance, and the two proof mechanisms.

The paper treats WUSF, not WMSF. The one-endedness theorem requires transience, reversibility, and finite expected inverse root conductance; retain all three. Its stationarity method does not by itself settle WMSF one-endedness on nonunimodular transitive graphs.
