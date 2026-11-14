# Source card — Fanuel & Bardenet (2025), “Cycling in the Forest with Wilson’s Algorithm”

**Reading evidence.** Full physical-page read of the complete 41-page arXiv v3 article, including the appendix proof of Proposition 3 and references (PDF pp. 1–41). Local artifact SHA-256: `b21225a1e95d038b21735aa10d179847cbec5ccd58b6b2dc5dd31eb2ceb6d663`. Identity/version checked against the PDF title page and the [official arXiv record](https://arxiv.org/abs/2404.14803): arXiv:2404.14803v3, revised 9 July 2025; title page dated 10 July 2025; Michaël Fanuel and Rémi Bardenet. Rendered and visually inspected physical p. 4 (magnetic Laplacian definition) and p. 16 (normalized form), 11 (Assumptions 3 and Propositions 4–5), 15–16 (Green resolvent and MGF), 21–22 (loop PPP runtime and escape probability), 32 (extremal PRS), and 37 (resampling expectation). Page-by-page coverage is recorded in `../reading_coverage.json (entry local_id=AUX-W07-CYCLE-FORESTS-2024)`.

## Model and sampling law

The article treats a **finite connected undirected graph** G=(V,E), n=|V|>1, with no multiple edges or self-loops and positive symmetric edge weights w_xy. Set deg(x)=sum_y w_xy and p_xy=w_xy/deg(x). A cycle-rooted spanning forest (CRSF) is a spanning subgraph with one cycle in each component. The algorithm outputs an oriented CRSF: each tree edge is oriented toward its component’s oriented cycle. Cycles include length-two backtracks.

For every oriented cycle c, Algorithm 1 uses independent Bernoulli trials of acceptance probability alpha(c). Starting from the first vertex not yet in the current partial forest, run the weighted random walk, loop-erase, and stop upon hitting the current forest or upon forming a cycle whose Bernoulli trial accepts it. Add the resulting branch or lasso and continue. The order of start vertices affects the intermediate decomposition, but Proposition 5 shows the output law is order independent.

The unoriented target has weight

    mu_CRSF,alpha(U) ∝ product_{e in U} w_e × product_{unoriented cycles c in U} (alpha(c)+alpha(reverse c)).

For a U(1) connection Phi, alpha(c)=1−cos(theta(c)), where the product of edge phases around c is exp(−i theta(c)). The magnetic Laplacian is Delta = D−W∘Phi, D_xx=deg(x). Its normalized form is the separate operator Delta_N = D^(−1/2) Delta D^(−1/2). The unoriented determinantal law has normalizer det(Delta) and each unoriented cycle factor 2(1−cos(theta(c))).

## Exact theorem statements and proof chains

### Determinantal case: Propositions 4–7 (physical pp. 11, 15–16)

- **Assumption 1 (nontrivial connection):** at least one cycle has holonomy different from 1; this makes Delta nonsingular. **Assumption 3 (weakly inconsistent cycles):** for every cycle c, cos(theta(c))≥0, so alpha(c)∈[0,1] is a valid acceptance probability. The paper notes Assumption 1 plus Assumption 3 implies the sign-flipped nontriviality Assumption 2.
- With Pi=D^{-1}(W∘Phi), **Proposition 4** gives spectrum(Pi)⊆[−1,1) under Assumption 1 and spectrum(Pi)⊆(−1,1] under Assumption 2. The proof conjugates Pi to Hermitian D^{-1/2}(W∘Phi)D^{-1/2}, bounds both sides using the nonnegative quadratic forms I±Pi', then excludes eigenvalue 1 or −1 using nonsingularity of Delta or the sign-flipped magnetic Laplacian. Under Assumptions 1 and 3, the spectrum is inside (−1,1).
- **Proposition 5 (correctness; physical p. 11; proof pp. 12–16).** For a fixed supported oriented CRSF F, the fixed start order induces stages F_1⊂…⊂F_kappa=F. If V_l is the stage’s vertex set, then (using the paper’s convention that Delta_S deletes rows and columns indexed by S)

    P(T_l=F_l) = det(Delta_{V_l})/det(Delta)
                 × product_{e in F_l} w_e
                 × product_{oriented cycles c in F_l} (1−cos(theta(c))).

  Proof chain: decompose each stage event by the numbers of erased loops between successive lasso/branch vertices (last-exit decomposition, eqs. (17)–(21)); sum each loop segment into the Green generating function G(t,x,x;A)=((I−t Pi_A)^−1)_{xx} (eqs. (26)–(28)); at t=1, G=deg(x)((Delta_A)^−1)_{xx}; multiply the transition probabilities along each branch/lasso and use ((Delta_A)^−1)_{xx}=det(Delta_{A∪{x}})/det(Delta_A) to telescope determinants (eqs. (29)–(30)). At the terminal stage this is the normalized oriented CRSF law; summing the two orientations gives the factor 2 in the unoriented formula. Backtracks have alpha=0, hence are popped with probability one.
- **Proposition 6 (physical p. 16):** under Assumptions 1 and 3 and t∈[−1,1], with T the number of random-walk steps,

    E[t^T] = t^n det(I−Pi)/det(I−t Pi)
           = t^n det(D−W∘Phi)/det(D−t W∘Phi).

  Marking every random-walk step by t and applying the same generalized matrix-tree normalization proves the identity. The interval includes negative t; it uses the strict spectral interval from Assumptions 1 and 3.
- **Proposition 7 (physical p. 16):** writing M=Pi(I−Pi)^−1, E[T]=n+Tr(M)=Tr((I−Pi)^−1) and Var(T)=Tr(M)+Tr(M²). These follow by differentiating the log MGF. The paper also records E[(-1)^T]=det(Pi−I)/det(Pi+I) and E[T]=Tr(Delta_N^−1) for Delta_N=D^−1/2 Delta D^−1/2.

### General cycle weights: loop measures and runtime (Section 5, physical pp. 18–30)

Here no U(1) form is required. Assume each oriented cycle has alpha(c)∈[0,1] and **Assumption 4:** at least one cycle has alpha(c)>0. For a based loop gamma, let q(gamma) be the product of its transition probabilities and let cycles(gamma) be the multiset of cycles removed in chronological loop erasure. Define

    mu_alpha(gamma)=q(gamma) product_{c in cycles(gamma)}(1−alpha(c))

for nontrivial loops and mu_alpha=1 for the trivial zero-length loop. It is multiplicative under concatenation. The Green sum G_alpha(t,x,x;A)=sum_{gamma in BL(A,x)} t^|gamma| mu_alpha(gamma) is finite for t∈(0,1] under Assumption 4.

For an unbased loop, N[gamma] counts its distinct based representatives and need not equal its length. With mult(gamma) the repetition multiplicity, N[gamma]=|gamma|/mult(gamma), and the loop measure is m_alpha([gamma])=mu_alpha([gamma])/|gamma|=mu_alpha(gamma)/mult(gamma) for nontrivial loops (zero for the trivial loop). **Proposition 9 (physical pp. 19–21)** proves

    G_alpha(t,x,x;A)
      = exp(sum_{unbased loops [gamma] in V\\A, x in [gamma]} t^|gamma| m_alpha([gamma])).

  The proof first decomposes a based loop by the number d(gamma) of returns to its basepoint; multiplicativity makes the mass with d=k the kth power of the d=1 mass, so G=(1−s)^−1. Taking logs and converting sums over based representatives to unbased loops uses Lemma 5.4’s exact count #[gamma],x=N[gamma] d_x([gamma])/|gamma|. This is the loop-measure exponential formula, not a determinant formula.
- **Correctness / normalizer (physical p. 21; eqs. (42)–(45)).** For the deterministic sequence of vertices x_1,…,x_n in F, stage probabilities are

    P(T=F) = product_{i=1}^{n−1} p_{x_i x_{i+1}}
             × product_{i=1}^{n} G_alpha(1,x_i,x_i;B_i)
             × product_{cycles c in F} alpha(c),
    B_i={x_1,…,x_{i−1}}.

  Partition all unbased loops by their first vertex in this order. Proposition 9 makes the product of Green terms equal exp(m_alpha(L)). This factor is independent of F, yielding the target oriented CRSF law and Z_alpha^−1=exp(m_alpha(L)).
- **Corollary 2 (physical p. 21):** under Assumption 4,

    T has law n + sum_{[gamma] in X} |gamma|,
    X ~ Poisson(m_alpha,L).

  Equivalently, E[t^T]=t^n exp(sum_{[gamma]}(t^|gamma|−1)m_alpha([gamma])) for 0<t≤1. This T counts Markov-chain steps, not the number of cycles popped.
- **Proposition 10 (physical pp. 22–23):** E[T]=sum_x G_alpha(1,x,x;empty)=sum_x 1/rho_x, where rho_x=P_x(min_c N_cycle(c)≤N_{return to x after 1}) is the probability of accepting a cycle no later than the first return to x. The geometric-return argument gives G=1/rho_x. This is an escape-to-an-accepted-cycle probability, not ordinary escape to infinity.
- Proposition 11 (pp. 23–26) further couples a randomized splitting of erased based loops with an independent Poisson point process of unbased loops and the sampled CRSF.

### Heaps and partial rejection sampling (Sections 5.7–6, physical pp. 26–37)

The heap view encodes chronological popped cycles with pieces ordered when cycles intersect. A pyramid has exactly one maximal piece. Lemmas 5.12–Proposition 13 identify based popped loops with pyramids rooted at their maximal-cycle basepoint and decompose a heap uniquely into ordered empty heaps/pyramids. This yields G_alpha as a sum over pyramids, an MGF as a ratio of heap sums (eq. (62)), an inclusion–exclusion ratio over trivial heaps (eq. (64)), and a Poisson-process representation on pyramids (eq. (65)).

Section 6 recasts the process as extremal partial rejection sampling. Independent variables are each vertex’s chosen outgoing neighbor and each oriented cycle’s Bernoulli variable; each cycle constraint is false only if that cycle is present and its Bernoulli variable rejects. Two simultaneously violated constraints cannot have intersecting scopes, because a functional digraph cannot contain two distinct cycles sharing a vertex; this is the extremality condition. Fixing an order of constraints, resample the scope of the first violated constraint. The path/heap reconstruction in Proposition 14 yields P(H,U*=u)=Z^−1 w(H) product_i P(U_i=u_i), proving the conditioned-product output law; termination a.s. is shown by domination by rejection sampling (Lemma 6.3). **Theorem 6.4 and Corollary 3 (physical pp. 36–37)** give resampling-count MGFs and, in particular, expected resamplings of constraint 1 equal P(bad(U)={1})/P(Phi(U)=true); the expected total number of resampled scopes equals P(|bad(U)|=1)/P(Phi(U)=true). These count resampling scopes/cycles, distinct from step count T.

## Use and transfer limits

Use the paper for finite weighted graph CRSF sampling; the determinant formula only under the stated magnetic-connection assumptions, and the general loop-measure runtime under Assumption 4. It does **not** prove an infinite-graph or locally-finite-network reflection theorem: no infinite-volume limit is taken here. The numerical section (pp. 37–38) reports Monte Carlo checks for n=100, p=.8, 1000 runs, and different noise values; these are simulations, not theorem evidence. Related loop soups, spanning forests, and PRS works cited in the bibliography are not substituted for the proofs in this source.

An exact local arithmetic check is saved at `../reader_batches/L13_final4/math/cyclepopping_triangle_exact_check.py` with output at `../reader_batches/L13_final4/math/cyclepopping_triangle_exact_check.txt`. For the three-vertex unit-weight triangle with holonomy i, it computes det(D−tW∘Phi)=8−6t² and checks the Proposition 6 MGF normalization, mean 9, and variance 48 using rational arithmetic. This checks the formula in that finite example only; it is not an independent proof of the sampling theorem.
