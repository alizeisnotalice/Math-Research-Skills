# HN2017USF — indistinguishability of uniform spanning forest components

**Source:** Tom Hutchcroft and Asaf Nachmias, *Indistinguishability of Trees in Uniform Spanning Forests*, Probability Theory and Related Fields 168 (2017), 113–152, DOI 10.1007/s00440-016-0707-3. The locally stored 43-page manuscript has an arXiv:1506.00556v2 header dated 22 May 2016 and its own version date of 8 Oct. 2018 on PDF p. 1. Full-paper reading: PDF pp. 1–43.

## Main theorem and necessary integrability

**Theorem 1.9 (PDF p. 10).** Let ((G,\rho)) be a unimodular random network with ℙ[(c(\rho))]<∞, and let (F) have law FUSF(_G) or WUSF(_G). For every Borel component property (A), invariant under rerooting within a component, either all components of (F) have (A) or none do, almost surely.

The theorem is stated in terms of component properties on rooted marked networks, so it applies beyond automorphism-invariant properties on a fixed transitive graph. The finite expected root conductance is essential: Section 1.3.3 (PDF pp. 13–14) constructs a unimodular random network with distinguishable WUSF components when this assumption is removed.

Related conclusions under the same unimodular/integrability assumptions:

- **Theorem 1.10 (PDF p. 11):** FUSF is a.s. connected or has infinitely many components.
- **Theorem 1.11 (PDF p. 11):** if FUSF is disconnected a.s., component membership probability decays to zero along some sequence of vertices.
- **Theorem 1.12 (PDF p. 11):** when FUSF and WUSF differ, every FUSF component is transient and infinitely-ended, both with inherited conductances and with unit conductances.
- **Theorem 1.20 (PDF p. 13):** for a stationary network whose WUSF components are one-ended, WUSF components are indistinguishable by tail component properties even without unimodularity.

## Proof structure

For FUSF with FUSF≠WUSF, Section 2 establishes update tolerance and then proves Theorem 2.8 (PDF pp. 21–23). A single-edge update adds a selected edge and removes an edge incident to its tail; Lemma 2.3 and Corollary 2.4 give the absolute-continuity bound with factor (c(e)/c(e^-)). Theorem 1.12 supplies transient infinitely-ended components. Lemma 2.7 turns coexistence of a property and its complement into a positive-probability pivotal edge at a core vertex. Biasing the root by its FUSF degree makes a two-sided walk stationary. Approximate (A) by a finite-radius event; at a distant walk location a pivotal update changes the component type with uniformly positive probability, while update tolerance compares the updated law back to the original. Stationarity then contradicts arbitrarily good finite-radius approximation. If FUSF=WUSF, the WUSF argument applies.

For WUSF, the proof splits properties into tail and non-tail cases. Theorem 1.20 uses Wilson’s algorithm and spatial Markov resampling: after exposing a finite ball and the future of vertices far away, one-endedness makes the remaining changes finite, so a tail property seen at the root agrees with the property seen by a walk far away; stationarity and the ergodic theorem force conditional probability 0 or 1. For non-tail properties, Lemma 4.4 (PDF pp. 33–35) shows that failure of a good pivotal edge would make the property equivalent to a tail property. The proof then uses finite Bernoulli clusters, mass transport to shift the root to a sampled vertex, and the WUSF update-tolerance inequality (Corollary 4.3, p. 32) to obtain the same contradiction with finite-radius approximation (Theorem 4.5, pp. 35–40).

## Boundaries

The theorem does not imply FSF/WSF mutual singularity or equality. The FUSF geometry conclusions require FUSF≠WUSF; the WUSF tail-property result instead requires stationarity and one-ended components. Check finite expected conductance before applying Theorem 1.9.
