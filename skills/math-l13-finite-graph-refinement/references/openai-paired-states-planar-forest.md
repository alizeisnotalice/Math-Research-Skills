# Paired states and planar forest extraction

Source: OpenAI, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, SHA-256 \`b519ff0c2b1f1554f34f01e644cd67651749826d43919862db6c42303701db18\`, physical pp. 4-8, Section 3, Lemma 4.1 and Proposition 5.1.

The source first uses integral max-flow to obtain a degree-two incidence subgraph.  It then defines antisymmetric \(\delta(v,w)\) by the black face to the left of a directed edge.  Under its rooted planar-triangulation hypotheses, each simple chosen-edge cycle avoids the roots and has \(\delta\)-sum \(-3\) counterclockwise or \(3\) clockwise.

It weights state pairs exponentially, cancels every pair with cyclic \(Q_s\), and uses a positive spoke-cycle weighting to make a remaining coefficient nonzero; hence some pair has \(Q_s\) a forest.  Check the embedding, roots, states, and disk identity before use.

## 固定来源

- 物理页 4, 5, 6, 7, 8。Section 3; Lemma 4.1; Proposition 5.1 SHA-256 `b519ff0c2b1f1554f34f01e644cd67651749826d43919862db6c42303701db18`。[Paired states and Hamiltonian cycles in cubic bipartite planar graphs](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf)
