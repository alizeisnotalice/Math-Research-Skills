> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-015 — Stability of twisted states in the Kuramoto model on Cayley and random graphs

## Source and reading evidence

- Georgi S. Medvedev and Xuezhi Tang, arXiv:1407.3990v3, published DOI 10.1007/s00332-015-9252-y. The exact local PDF's page-1 margin carries the arXiv v3 stamp dated 10 May 2015, while the title-page body says August 8, 2018. Preserve this internal date discrepancy; the local file was not treated as a verified copy of the journal pagination/version.
- Exact local source: ../pdfs/PGEL-015.pdf, 36 physical pages, SHA-256 b6aede88f5a5ade09c8e53f8acbf923f5e0c4fa51b0e5c027beefa6c38cb1538. Rendered physical p. 1 visibly confirms both dates.
- Complete physical PDF pp. 1–36 read in order, including proofs, conclusion, and references. Section-by-section coverage and rendered-page hashes are in reading_coverage.json#sources.PGEL-015.
- Canonical full-read index was checked before reading; no accepted exact-title, arXiv-ID, or source-hash match was found. This is a new full-text read, pending independent review.

## Model and conventions

The paper studies the homogeneous Kuramoto equation on complete, Paley, symmetric Cayley, and Erdős–Rényi graphs. Its Cayley model is on Z_n with a symmetric generating set S=-S; the coupling sign is indexed by α∈{0,1}, with α=0 attractive and α=1 repulsive. A q-twisted state has phases proportional to qx/n modulo one. The graph and coupling conventions matter: the Fourier diagonalization in §§2–3 uses an undirected symmetric Cayley graph.

## Results read from the source

1. **Cayley twisted-state criterion (Theorem 3.4, physical pp. 13–14, Eq. (3.14)).** The q-twist is a stable equilibrium if, for every nonzero x∈Z_n,
   \[
   (-1)^\alpha\sum_{y\in S}\left[
   \cos\!\frac{2\pi(q+x)y}{n}-2\cos\!\frac{2\pi qy}{n}
   +\cos\!\frac{2\pi(q-x)y}{n}\right]<0.
   \]
   Proof mechanism: Fourier diagonalize the linearization at the twist. The constant vector is the zero mode from phase-rotation symmetry; the strict inequalities make every other eigenvalue negative. The proof then uses invariance of the orthogonal complement of the constant vector to infer stability. This is an exact condition for the stated symmetric Cayley model; it is not a condition for arbitrary directed or signed graphs.

2. **Variational conclusions (Theorems 3.7–3.8, physical p. 16).** For an undirected graph, synchrony is stable for attractive coupling and unstable for repulsive coupling. For a cyclic Cayley graph, twists belonging to the largest Laplacian eigenvalue are stable for repulsive and unstable for attractive coupling. These are stability conclusions from the energy/variational formulation; neither is a global-attraction theorem.

3. **Attractive synchrony (Theorem 4.2, physical pp. 17–18).** The synchrony subspace is asymptotically stable for attractive coupling and unstable for repulsive coupling. The proof uses a Lyapunov function, Laplacian spectral gap, and invariant neighborhoods of the synchrony orbit.

4. **Largest-eigenvalue twist (Theorem 4.3, physical p. 19).** On the cyclic Cayley graph, if a twist associated with the largest Laplacian eigenvalue has a simple zero eigenvalue in -H(Φ)(u_m), its rotational orbit is asymptotically stable. The proof invokes a local Lyapunov landscape near the nondegenerate extremum. The simplicity hypothesis is essential to this statement.

5. **Complete graph (Theorem 5.3, physical pp. 22–23).** For odd n, all q-twisted states with q=1,…,n−1 are stable under repulsive coupling. The linearization has two negative eigenvalues and n−2 zero eigenvalues. The proof uses a regular-value argument to obtain a local (n−2)-dimensional manifold of equilibria and a reduction argument for stability. Thus “stable” here does not mean an isolated strict energy minimum.

6. **Paley graph (Corollary 6.2 and Table 2, physical pp. 23–24).** A q that is not a quadratic residue modulo the graph order gives an unstable q-twist for repulsive coupling. The table leaves the quadratic-residue attractive case unresolved; do not extend this corollary into a full classification.

7. **ER finite-time comparison (Theorem 7.2, physical pp. 25–28).** For solutions on the complete graph and G(n,p) with the same initial condition, assume for fixed T>0 that the empirical average of D(v_nj−v_ni)^2 over i,j stays between positive constants C1,C2 in the stated liminf/limsup sense on [0,T]. The printed conclusion is a probability tending to zero for a uniform-in-time deviation at least C n^(-1/2), with C=C(L,T)>0, where L is the Lipschitz constant of D. The proof subtracts the ODEs, obtains an energy inequality, applies Grönwall, and estimates the random forcing through Lemma 7.3. The literal lemma statement and a sign/limit in the proof are flagged below; therefore this proof chain is not accepted as a verified theorem interface here. In any event it concerns a fixed finite horizon and does not prove uniform-in-time, global, or all-initial-condition synchronization on ER graphs.

8. **ER twisted-state residual (Theorem 7.4, physical pp. 29–30).** For each fixed q and fixed vertex i, a fourth-moment bound E S_ni^4≤3n^2, Markov's inequality, and Borel–Cantelli yield vanishing normalized residual almost surely along the ER graph sequence. The proof is coordinatewise for fixed q,i; it gives no uniformity over vertices, q growing with n, or arbitrary phases. The displayed definition (7.20) itself inserts an inner limit while the theorem and proof treat the normalized finite-n sequence, so the normalization notation is not used as a broader uniform statement.

9. **Finite-horizon metastability (Theorem 7.5, physical pp. 30–31).** For fixed tolerances, horizon T, and twist q, sufficiently close initial data remain near that twist on [0,T] with high probability for sufficiently large n. The proof compares a random-graph trajectory to the corresponding complete-graph trajectory and relies on Theorem 7.2. The printed N=N(ε1,ε2) omits T and q even though the theorem first fixes both and the proof uses them. Preserve this parameter-dependence caveat. This is finite-time metastability, not infinite-time attraction or global stability.

## Source issues and independent verification

- **Lemma 7.3 notation (physical p. 26) and the scope of the local check.** The printed variance formula sums over i while retaining i as the row label; the likely intended row variance sums over j. Separately, the source prints \(z_{ni}^2=(1/n)\sum_j(\xi_{nij}-p)f_{nij}\), with no square on the right-hand row average. The saved exact counterexample silently uses neither literal display: it changes the variance sum to the intended rowwise sum over j and reads the row-average on the right as \(z_{ni}=(1/n)\sum_j(\xi_{nij}-p)f_{nij}\), with \(S_n=\sum_i z_{ni}^2\). Under this **doubly corrected intended interpretation only**, choose p=1/2, independent Bernoulli entries, and \(f_{ni1}=\sqrt n,\ f_{nij}=0\) for j>1, constant in time. Every coefficient is in \(L^\infty\) for each n; rows are independent; the intended row variance and its average equal 1/4; and \(S_n=1/4\) deterministically. Hence the resulting centered standardized variable is identically zero rather than standard normal. This is not a counterexample to the literal malformed displays and is not a counterexample to the application-specific sinusoidal coefficient structure in Theorem 7.2. It only shows that the lemma interface under this natural corrected reading still needs additional assumptions or proof.
- **Equations (7.18)–(7.19), physical p. 27.** From (7.17), the text prints an upper bound on the probability of the small-noise event by a probability of the complementary deviation event, then concludes that this small-noise probability tends to zero. That direction cannot deliver the small-noise estimate required in the preceding Grönwall step. Equation (7.19) then prints limit zero for the small-noise event, although the intended estimate needs probability tending to one. Further, uniform-in-t marginal tail convergence alone does not control a supremum over the continuum of times; a temporal process-control argument is missing from the displayed inference. The finite-time proof interfaces for Theorem 7.2 and dependent Theorem 7.5 therefore remain unverified. These findings do not establish either theorem false.
- **Equation (7.20), physical p. 29.** The source places a limit inside the definition of R_ni and then states another limit in n. The proof instead works with S_ni/(np) at finite n. The card keeps the intended coordinatewise residual scope separate from the literal display.
- Visual formula review: rendered and viewed physical pp. 13, 16, 19, 21–31. The exact Eq. (3.14), local stability theorem statements, ER assumptions, Lemma 7.3 normalizer/index, (7.18)–(7.19), and the fixed-q residual were checked on the source images. Full-page reading remains the basis for coverage, not text extraction alone.
- Actual calculation: ../math/pgel_l03_b7_checks.py was run with the project Python environment. Its exact counterexample is limited to the doubly corrected intended interpretation described above; it is not a literal-display counterexample or a test of Theorem 7.2's sinusoidal-coefficient application.

## Use and transfer boundary

Useful as a source-specific toolkit for Fourier spectra and local stability of twists on symmetric Cayley graphs; it also illustrates why graph-limit or finite-time ODE closeness does not by itself settle long-time attractor structure. For ER graphs, retain only the stated fixed-horizon and fixed-coordinate regimes, and keep Theorem 7.2's proof interface pending. No uniform ER theorem is asserted. This source does not establish signed-graph stability or resolve C106/C107.

## Review state

Full-page reading evidence was accepted by R02. The literal/intended display distinction and proof-interface scope above are revised and await R02 re-review. No mother ledger or skill has been changed.
