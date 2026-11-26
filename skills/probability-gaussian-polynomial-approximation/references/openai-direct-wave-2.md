# Fixed Gaussian partition amplification

Source: *Unbounded Violations of the Square-Root Degree Bound*, family 192, SHA-256 `4b847d47e281e37df99e6c3c6561cfd1db55380e6504a73e30918ead56b74894`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf), physical pp. 12--15, Lemma 5.1, Theorem 5.2, and Lemma 5.3.

Start with a fixed finite partition of \(\mathbb R^q\) whose cells have Gaussian-null boundaries and coordinate costs. If its conditional-mean variance \(V\) exceeds mean cost \(c\), first choose the partition and only then run the finite block amplification. The transfer to sign blocks requires independent standardized coordinates and retains lower semicontinuity of the conditional-variance term, including cells with zero limiting probability.

Output must state the partition, cell costs, null-boundary evidence, the strict margin \(V-c>0\), degree algebra for every cell indicator, and each finite batch size. Boundary: the method does not manufacture the initial variance advantage or justify a partition with positive-boundary mass.
