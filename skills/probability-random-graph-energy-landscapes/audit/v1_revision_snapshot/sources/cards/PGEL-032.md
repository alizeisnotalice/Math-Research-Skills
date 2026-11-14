> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-032 — threshold graphs are second-order globally synchronizing

## Identity and reading record

- **Read file:** `../pdfs/PGEL-032.pdf`
- **Reader/review:** L02 (W24); R05 helper-stage review passed and reading evidence accepted; mother-hash binding remains pending. R05 metadata_verified=false.
- **Mother coverage:** `../reading_coverage.json` entry for PGEL-032; helper evidence path `../reading_coverage.json#PGEL-032`.
- **Exact local version:** arXiv:2511.12646v6, with PDF front-page date June 18, 2026 and arXiv stamp June 16, 2026; 24 physical pages; SHA-256 `ecdffbee9a5350c5ffc1d8dbb603df8791cb725f352a02f3262e6caf7d25a1b4`. This identifies the read preprint version only; it does not infer a later publication.
- **Reading status:** full text read, physical pp. 1–24 in order, including proofs, references, and author/affiliation page. The theorem/proof formulas were also checked in page renders from the exact local PDF.

## Model and definitions

The graph $G=(V,E)$ is a finite simple **unweighted undirected** graph with adjacency matrix $A$. The homogeneous Kuramoto flow is
$$\dot\theta_i=\sum_j A_{ij}\sin(\theta_j-\theta_i),$$
and its energy is $E_G(\theta)=\tfrac12\sum_{i,j}A_{ij}(1-\cos(\theta_i-\theta_j))$. A second-order stationary point (SOSP) has $\nabla E_G=0$ and $\nabla^2E_G\succeq0$. “Fully synchronized” means all phases agree modulo $2\pi$, with the global phase rotation understood.

A threshold graph is built from one vertex by adding isolated (0) or dominating (1) vertices. The main theorem is stated for **connected** threshold graphs; in the construction, the last bit must be 1 (apart from the one-vertex base case). No random-graph, weight, sign, orientation, or frequency-heterogeneity assumption is covered by the theorem.

## Main theorem and proof chain

**Theorem 1.3 (PDF p. 4; full proof §6, pp. 20–22).** Every connected threshold graph is second-order globally synchronizing: every SOSP of $E_G$ is fully synchronized. The paper then invokes the analytic-gradient-flow result described in §1 (Łojasiewicz gradient inequality plus center-manifold argument, cited to [GLPR25, Lemma A.1]) to infer convergence to synchrony from almost every initial condition. The combinatorial theorem is proved in this paper; the general measure-zero convergence implication is cited, not re-proved in full here.

The proof dependencies are:

1. **Lemma 4.1 (PDF pp. 11–12):** at equilibrium, each node’s neighbor phasor sum obeys $\sum_{j\in N(i)}v_j=\mu_i v_i$, with $v_i=(\cos\theta_i,\sin\theta_i)$ and $\mu_i=\sum_{j\in N(i)}\cos(\theta_j-\theta_i)$. The proof rewrites the relation in complex coordinates and equates it to the sine equilibrium condition.
2. **Lemma 4.4 (PDF p. 13):** at an SOSP, $\mu_i\ge0$ for every node; otherwise the corresponding Hessian diagonal entry is negative. The zero-sum case is retained: the neighbor phasor sum may be zero.
3. **Lemma 5.1 / Corollary 5.2 (PDF pp. 14–15):** if unit phasors satisfy $v_b+q=\mu_a v_a$ and $v_a+q=\mu_b v_b$, subtraction gives $(\mu_a+1)v_a=(\mu_b+1)v_b$. The possibilities are equal phasors with equal scalars, antipodal phasors with $\mu_a+\mu_b=-2$ (excluding $(-1,-1)$), or $\mu_a=\mu_b=-1$ and $v_a+v_b+q=0$. If both scalars are nonnegative, only $v_a=v_b$ remains.
4. **Corollary 5.4 (PDF p. 15):** graph-theoretic closed twins synchronize at any SOSP. Their common neighbors contribute the same vector sum, so the two equilibrium identities fit Corollary 5.2 with nonnegative coefficients.
5. **Lemma 5.8 (PDF pp. 17–18):** under the partition $W=Q\sqcup S\sqcup P$, (i) every $Q$-vertex neighbors only $S$, (ii) each $S$-neighborhood is $P\sqcup N_Q(i)\sqcup(S\setminus\{i\})$, and (iii) $Q\sqcup S$ is synchronized at an SOSP, the sum $\sum_{j\in P}v_j$ is aligned with the common phasor or zero. The proof inserts the neighborhood decomposition into Lemma 4.4 and tests the Hessian with the indicator vector of $Q\sqcup S$; a negative scalar coefficient would make that quadratic form negative.
6. **Lemma 5.9 (PDF pp. 19–20):** for $W=Q\sqcup S_1\sqcup S_2\sqcup P$, the unambiguous explicit condition printed in (iii) is
   $$N(i)=P\sqcup N_Q(i)\sqcup((S_1\sqcup S_2)\setminus\{i\}),\qquad i\in S_1\sqcup S_2,$$
   together with (i) every $Q$-vertex having all neighbors in $S_1$ and the stated SOSP with $Q\sqcup S_1$ synchronized. Under these conditions $S_1\sqcup S_2$ synchronizes. Step A applies Lemma 5.8 to align the $S_2\sqcup P$ phasor sum, Step B adds the synchronized $S_1\setminus\{i\}$ vertices, and Step C combines this with each $S_2$ SOSP condition and Corollary 5.2. The neighborhood conditions are essential; this is not a generic graph propagation rule.
7. **§6 induction (PDF pp. 20–22):** decompose the threshold construction sequence into maximal 1-blocks $U_j$ and 0-blocks $I_j$, read from the end. The last 1-block is a closed-twin class, hence synchronized. Lemma 4.4 synchronizes the adjacent 0-blocks. The threshold construction then supplies $Q,S_1,S_2,P$ satisfying Lemma 5.9, so the preceding 1-block synchronizes with the already aligned suffix. Induction over the number of 1-blocks proves every SOSP is synchronous. The eight-step sequence $01010101$ on pp. 20–21 is a worked illustration; p. 22 gives the general argument.

Other results read in full: Theorem 2.2 characterizes threshold graphs, including exclusion of induced $P_4,C_4,2K_2$; Lemma 2.5 and Theorem 2.7 show every admissible edge count and every minimum degree $1,\ldots,n-1$ can occur for a connected threshold graph (PDF pp. 7–9); Theorem 5.6 proves the windmill subclass result (p. 16).

## Source-stated issues and safe use

- **Proposition 3.2 (PDF p. 9) is not used as a proof step.** The printed statement says an equilibrium is stable if its Jacobian $J$ is negative semidefinite, but the accompanying proof only differentiates the vector field to compute the entries of $J$. It does not establish nonlinear stability from the semidefinite condition. Record this as a source proof gap; do not rely on that proposition to justify Theorem 1.3. The main theorem instead directly excludes nonsynchronous SOSPs using the Hessian and phasor arguments above.
- **Lemma 5.9 notation issue (PDF p. 19):** condition (ii) uses $S\setminus\{i\}$ although the lemma has introduced $S_1,S_2$ and has not defined $S$. Condition (iii) immediately states the explicit decomposition using $S_1\sqcup S_2$. This card records (iii) as the operative neighborhood hypothesis and does not silently treat the undefined $S$ in (ii) as source text that was correct.
- The equivalence between stable equilibria and local energy minima is attributed in §3.3 to Absil–Kurdyka [AK06]; it is not a new proof in this paper. Likewise the almost-everywhere convergence implication is supported by the cited analytic-gradient result.
- The result is for connected threshold graphs in the homogeneous positive symmetric model. Do not migrate to signed/oriented graphs, arbitrary weighted graphs, or general graphs based on local lemmas alone. Lemma 5.9 needs all its partition/neighborhood conditions.
- Saved SymPy checks on the 3-vertex path and the algebraic subtraction in Lemma 5.1 are finite-instance checks only, not a proof of Theorem 1.3.
