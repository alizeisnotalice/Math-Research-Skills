# bkp26 — The maximum length of \(K_r\)-bootstrap percolation

**Reading status:** `fulltext_read`; complete 10-page arXiv PDF read, PDF pp. 1–10. Main constructions and bounds were checked on rendered PDF pp. 2–3, 6, and 9. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** József Balogh, Gal Kronenberg, Alexey Pokrovskiy, and Tibor Szabó, “The Maximum Length of \(K_r\)-Bootstrap Percolation,” arXiv:1907.04559 (2019); *Proceedings of the American Mathematical Society* 154 (2026), 1359–1371, DOI [10.1090/proc/15130](https://doi.org/10.1090/proc/15130). Local PDF SHA-256: `dd122366f97677603fa06945a715487c328f255b791d00041409b412ba6b9db7`.

## Process and bounds

Let \(M_r(n)\) be the maximum stabilization time of the synchronous \(K_r\)-edge-bootstrap process on \(K_n\), taken over all initial edge sets whose process is non-stationary. Theorem 4 proves that for every fixed \(r\ge6\) and all sufficiently large \(n\),

\[
M_r(n)\ge n^2/2500.
\]

Theorem 5 gives

\[
M_5(n)\ge \frac{n r_3(n)}{1200}
\ge n^{2-O(1/\sqrt{\log n})},
\]

where \(r_3(n)\) is the maximum size of a 3-term-arithmetic-progression-free subset of \([n]\); the second inequality uses Behrend’s construction. Thus the paper disproves the conjectured universal \(o(n^2)\) bound for each fixed \(r\ge6\), but leaves the \(K_5\) question unresolved.

## Construction and limits

The key lemma in §2 converts an ordered \(r\)-uniform hypergraph into a slow bootstrap construction. Its term “induced \(H\)-free” is a **special hypergraph condition**, not ordinary induced-freeness of the 2-skeleton: Definition 7 says every copy of \(H\) in the 2-skeleton (the copy need not be induced there) is contained in some single hyperedge. In the application \(H=K_r^-\). The ordered hyperedges \(e_1,\ldots,e_m\) also have designated pairs \(f_i\subset e_i\) such that \(f_i\subset e_j\) exactly when \(i=j=m\), or when \(i<m\) and \(j\in\{i,i+1\}\). Lemma 8 inducts over rounds: before round \(i\), the missing designated pairs are \(f_i,\ldots,f_m\); the copy of \(K_r^-\) within \(e_i\) makes \(f_i\) eligible, while the special containment condition rules out any other new pair. Thus the process lasts at least \(m=e(\mathcal H)\) rounds. For \(r=6\), a 6-uniform construction on \(4n+40\) vertices has \(\lfloor n^2/100\rfloor\) ordered hyperedges; the proof verifies the custom containment condition by controlling intersections of its two cyclic coordinate blocks. For \(r=5\), chains are assembled using a 3-AP-free set and turning gadgets, preserving the same custom condition and a linear-in-\(n|B|\) edge count.

These are lower-bound constructions for **maximum synchronous edge-bootstrap time**. They do not give a matching upper bound, settle \(M_5(n)=o(n^2)\), or imply a threshold or infection-time result for random initial conditions. The finite hypergraph construction is a proof ingredient, not a finite-enumeration extrapolation.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bkp26`).
