# grimmett-problems — Selected Problems in Probability

**Reading status:** `fulltext_read`; all 15 PDF pages were read, including §6 on enhancement path surgery. This is an author-selected problems paper rather than a theorem paper or the *Percolation* textbook. Publication year is not established. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Geoffrey R. Grimmett, “Selected Problems in Probability,” author-hosted PDF. Local PDF SHA-256: `5d13ba96c4e6cc1d549b9320db03a355742fbc027bd640714922f5d26ce4e3c4`.

## Enhancement path-surgery question

Section 6, Question 6.1 (PDF pp. 10–11) asks whether, for every `m ≥ 1` and `d ≥ 2`, there is a radius `R > m` such that every site configuration containing a doubly infinite, non-self-touching path through the origin can be changed only inside `B_R` to produce two singly infinite paths starting at `−m e_1` and `m e_1`, respectively, with no other vertices in `B_m`, and with the two paths non-touching. The required radius is uniform over the allowed external configuration. The point is to turn a pivotal open site into a configuration where a local enhancement is pivotal, enabling Russo-derivative comparison and then a strict critical-point shift.

This source explicitly says the graph-theoretic details in Aizenman–Grimmett’s site-percolation application were omitted. It reports that the surgery is straightforward in `d=2`, proved in `d=3` by Balister–Bollobás–Riordan (2014), and appears open for `d≥4` at the time of writing. The analogous bond-percolation step is treated in Grimmett’s *Percolation*, Chapter 3. Thus Question 6.1 is a problem statement with a dimension-specific status report, not a general path-surgery theorem. For mapped C116 use, an independent lemma matching the exact model and dimension is still required.

## Other sections actually read

The paper also surveys selected problems on self-avoiding walks, Lorentz gas/wind-tree models, stochastic inequalities, randomly oriented square-lattice percolation, and two diffusion epidemics. These sections are problem provenance and context; open questions and analogies in them are not theorem evidence. In §7 (PDF pp. 11–12), Grimmett specifically notes that monotonicity present in the delayed-diffusion epidemic is absent in the diffusion model, so conclusions do not transfer between those dynamics automatically.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/grimmett-problems`).
