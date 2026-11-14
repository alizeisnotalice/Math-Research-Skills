# ALEX1995MSF — percolation and minimal spanning forests

**Source:** Kenneth S. Alexander, “Percolation and Minimal Spanning Forests in Infinite Graphs,” *Annals of Probability* 23(1) (1995), 87–104. Complete 19-page local scan read (SHA-256 `a8354c571eaeb9404a1a5c1e0cbdcd4e1eabf2bc724c33ac88446041ab3da3a7`). The cover and the theorem pages were checked from rendered originals; cited PDF pages are physical pages and printed page numbers appear parenthetically where useful.

## Model and edge criterion

The paper works with stationary random labeled graphs in Euclidean space, with finite site density and ambiguity-free labels in the relevant results. For a bond (b=\langle x,y\rangle), the minimax/creek-crossing criterion says (b\) belongs to the MSF iff every path from (x) to (y) has a bond with label at least (f(b)). Proposition 2.1 (PDF pp. 5–6) derives the cut and locally minimax characterizations. Equivalence with invasion and strict-sublevel-cluster criteria uses **strict simultaneous uniqueness**, meaning at most one infinite strict (r)-cluster simultaneously for every level (r); fixed-level a.s. uniqueness is not the same assertion (see Lemma 2.3, PDF p. 7).

## Theorem 2.6: planar dual percolation

“Lattice-like” is a defined hypothesis, not a synonym for planar: (G) is embedded in \(\mathbb R^2\), locally finite, every site has finite degree, connected, planar, has no loop bonds, and every face is bounded (definition and theorem on physical PDF p. 8, printed p. 93). A dual graph is built by placing a face-site in each face and joining face-sites across each bond separating distinct faces. A dual bond is strictly occupied at level (r) when its primal label is at least (r).

Theorem 2.6 states: if (G) is an **ambiguity-free lattice-like labeled graph in \(\mathbb R^2\)** and its MSF has more than one tree, then the corresponding dual percolation has an infinite cluster of strictly occupied bonds at critical level (r_c(G)). This is not a generic planar-graph consequence. The proof uses dual crossings/critical percolation structure for the stated embedding and bounded-face framework.

## Theorem 4.2: invasion equivalences and required uniqueness

Theorem 4.2 (PDF pp. 14–16, printed pp. 99–101) assumes (X) is as in Theorem 2.5 **and strict simultaneous uniqueness holds almost surely**. Under these assumptions: (i) an invaded bond is a breakout bond iff it belongs to the MSF; (ii) the limiting invaded set from (x) contains the corresponding strict-critical cluster; and (iii) the symmetric difference of the limiting invasion sets from (x,y) is finite iff (x,y) lie in the same MSF tree. Preserve Theorem 2.5's stationary random labeled-graph, finite-site-density and ambiguity-free framework, as well as this strict simultaneous uniqueness condition, whenever using the invasion equivalence.

For (i), a breakout bond is an MSF bond by the minimax criterion; a backfill bond has an alternate path of breakout bonds, so cannot also lie in the acyclic MSF. For (ii), in a one-ended tree, cutting an MSF bond leaves only finitely many bonds reachable from a vertex without crossing it; in a two-ended tree, the argument inducts along both trunk rays using that bonds below criticality do not lie in infinite strict clusters. For (iii), invasion sets from distinct trees are disjoint by (i). Within one-ended or two-ended trees, the proof compares the successive (f)-minimizing breakout bonds and uses the connected finite portions plus finite-degree hypotheses; strict simultaneous uniqueness supplies the critical-cluster input. The theorem does not assert the equivalence under only per-level uniqueness.

## Other theorem and proof mechanisms read

Theorem 2.5 (PDF pp. 7–8) controls MSF component ends under the paper's simultaneous-uniqueness hypothesis; if a two-ended tree occurs, its trunk is in the critical percolation cluster. Theorem 5.1 (PDF pp. 17–18) proves that two ambiguity-free, locally finite labeled graphs agreeing outside a bounded region have MSFs differing by finitely many bonds; its stationary conclusion about equivalence relations additionally assumes strict simultaneous uniqueness a.s. Theorem 5.1 is a finite-box stability result, not license to omit its global assumptions.

## Reading coverage

Complete scan read: §1 setup (PDF pp. 2–4); §2 minimax criteria, label uniqueness and planar duality (pp. 4–9); §3 stationary structure and proof of Theorem 2.5 (pp. 9–13); §4 invasion percolation and Theorem 4.2 proof (pp. 13–16); §5 finite-box stability and proof (pp. 16–18); references (p. 19). The lattice-like definition and Theorem 2.6 were visually checked on rendered PDF p. 8; Theorem 4.2 and its strict-uniqueness hypothesis on rendered PDF p. 14.

## Scope boundary

For Theorem 2.6, verify every lattice-like condition and the ambiguity-free labeling. For Theorem 4.2 and the strict-level characterizations, explicitly verify strict simultaneous uniqueness a.s.; ordinary uniqueness at each fixed level is not a drop-in replacement. Retain stationarity, finite site density, and other Theorem 2.5 hypotheses when transferring conclusions.
