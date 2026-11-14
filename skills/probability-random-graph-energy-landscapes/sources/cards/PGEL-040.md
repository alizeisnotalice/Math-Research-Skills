> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-040 — Almost Global Synchronization of Symmetric Kuramoto Coupled Oscillators

**Read basis.** Canale–Monzón, independent formal publisher research chapter, DOI [10.5772/6026](https://doi.org/10.5772/6026), 26-page local PDF, SHA-256 efbf80c3a92afd1af83d45ddad56408c7c17e222cfa994795e707f75d96bf6a3. The official IntechOpen record identifies this named contribution in *Systems, Structure and Control*; the complete chapter PDF includes proofs, references, publisher metadata, and its CC BY-NC-SA 3.0 license. Physical pp. 1–26 were read in sequence. The batch metadata deliberately retains kind_declared=book and full_book_acquired=false: this is one complete formal research contribution, not the full edited volume or a claim to have read it. Physical p. 12 (printed p. 178) was rendered to verify Theorem 5.1 and its standing zero-eigenvalue caveat; physical pp. 17–23 (printed pp. 183–189) were rendered to verify the twin-quotient and subdivision arguments.

## Model and exact scope

The chapter studies a finite undirected symmetric interaction graph \(G=(V,E)\), identical natural frequencies, and sinusoidal pair coupling. A rotating frame removes the common frequency and a time rescaling removes the positive common coupling constant, giving
\[
\dot\theta_i=\sum_{j\in N_i}\sin(\theta_j-\theta_i).
\]
The state is on the phase torus. Synchronization is the diagonal orbit under common phase shifts. “Almost global” means the set of initial phases that fail to converge to the synchronized set has zero Lebesgue measure. The graph assumptions in the results below are finite, connected, undirected, and unweighted unless the cited statement says otherwise.

Writing an oriented incidence matrix \(B\), the energy used in §4 is
\[
U(\theta)=|E|-\mathbf1^T\cos(B^T\theta),\qquad
\dot U=-\|\dot\theta\|_2^2,
\]
and the Jacobian at an equilibrium is
\[
A=-B\,\mathrm{diag}(\cos(B^T\bar\theta))\,B^T.
\]
The common-phase direction always contributes a zero eigenvalue.

## Results and proof chain

- **Proposition 2.1 / Corollary 2.1 (physical pp. 3–4; printed pp. 169–170).** At an equilibrium, the sum of the neighbor phasors at each vertex is parallel to that vertex's phasor. A degree-one vertex therefore has the same or opposite phase as its neighbor. On a tree, iterating this constraint leaves only full or partial consensus equilibria.
- **Lemmas 4.2–4.4 and Theorem 4.1 (physical pp. 7–9; printed pp. 173–175).** If some equilibrium coefficient \(\alpha_i<0\), the symmetric Jacobian has a positive eigenvalue, so the equilibrium is unstable. If all edge phase differences have positive cosine, the weighted Laplacian is positive on the common-phase quotient, so the equilibrium is locally stable. Partial consensus is unstable. A connected tree has trivial cycle space, so its equilibria are only full or partial consensus; hence the synchronized set is almost globally attracting. The final almost-global step uses the gradient flow and the unstable-equilibrium exclusion stated by the authors.
- **Theorem 4.2 (physical p. 9; printed p. 175).** The complete graph is stated to be almost globally synchronizing, but this chapter explicitly sends the proof to prior work. Treat it as a cited theorem, not a proof reproduced here.
- **Lemma 5.1 and Theorem 5.1 (physical pp. 9–13; printed pp. 175–179).** For two graph subproblems joined at one cut vertex, the edge-flow/equilibrium data restrict to each side and can be glued at the common vertex. Theorem 5.1 says an equilibrium is locally stable iff both restrictions are locally stable and agree at the cut vertex. **Standing limitation:** immediately before the theorem the authors assume the full Jacobian has exactly one zero eigenvalue; they say a larger nullity can make linearization fail and do not study it. The proof writes the full Jacobian as the sum of the two embedded subgraph Jacobians and uses their negative semidefinite quadratic forms.
- **Theorem 5.2 through Theorem 5.4 (physical pp. 13–15; printed pp. 179–181).** Almost-global synchronization is preserved/characterized through cut-vertex composition: the joined graph is a.g.s. iff both pieces are; equivalently, a graph is a.g.s. iff each block is. In particular, all-complete blocks imply a.g.s. These inherit the preceding graph/model setting and the §5 single-null-eigenvalue restriction used for the stability decomposition.
- **Lemma 7.1 and Theorem 7.1 (physical pp. 17–19; printed pp. 183–185).** Adjacent twin vertices must share phase at a stable equilibrium. Collapsing adjacent-twin classes sends a stable equilibrium to a weighted equilibrium flow on the quotient, with class-size edge weights. If the quotient is a tree, only consensus can be stable; thus \(G\) is a.g.s. Corollaries cover complete graphs, complete graphs minus one edge, and the stated proper subsets of edges incident to one vertex.
- **Lemma 7.2 / Theorem 7.2 (physical pp. 19–20; printed pp. 185–186).** No nonsynchronous equilibrium can have all phasors in a half-circle; every connected graph admits an a.g.s. twin cover. The latter means an enlargement by twin vertices with the stated quotient property; it is not a claim that every original connected graph is itself a.g.s.
- **Theorem 7.3 (physical pp. 20–22; printed pp. 186–188).** If \(e\) is a non-bridge, sufficiently many subdivisions of \(e\) produce a graph that is not a.g.s. The proof starts from a stable twisted state on a long cycle and continues it to the subdivided graph using an implicit-function argument. This is an obstruction/example family, not a random-graph theorem.
- **§7.2, Lemma 7.3 and Proposition 7.1 (physical pp. 22–23; printed pp. 188–189).** The chapter gives restricted conditions for nonadjacent twins; it does not supply a general classification of a.g.s. graphs.

## Reusable method and transfer boundary

For a finite graph with the exact symmetric sine-coupled model, use the negative weighted-Laplacian Jacobian, equilibrium flow restriction, and cut-vertex/block decomposition as deterministic graph-structure tools. The twin quotient is useful only when the adjacent-twin relation and quotient tree condition are verified. A random-graph application still needs a separate probability estimate for the required graph structure (or a separate deterministic certificate on the sampled graph). The chapter contains no random graph distribution, high-probability bound, signed/oriented interaction theorem, heterogeneous-frequency theorem, or probabilistic basin estimate.

## Local exact check

The script ../math/pgel_l12_b10_verify_examples.py forms the three-vertex path Jacobian at synchrony and its two embedded edge Jacobians. SymPy 1.14.0 returns the exact sum identity and spectrum \(\{-3,-1,0\}\). This illustrates the common-phase null direction and cut-vertex block sum only; it does not prove the general theorem.
