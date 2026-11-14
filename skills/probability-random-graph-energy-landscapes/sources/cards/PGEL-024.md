> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-024 — Counting equilibria of the Kuramoto model using birationally invariant intersection index

**Authors:** Tianran Chen, Robert Davis, Dhagash Mehta. **Read artifact:** arXiv:1708.09246v1, 13-page author PDF (submitted 30 Aug 2017); published bibliographic record: *SIAM Journal on Applied Algebra and Geometry* 2(4) (2018), 489–507, DOI 10.1137/17M1145665. The mathematical page references below refer to the local arXiv-v1 PDF, not a claim of page-for-page identity with the journal typesetting.

**PDF identity:** ../pdfs/PGEL-024.pdf; SHA-256 17fc44e9b76f147c1ba06dd1278a5f99d9f6f0aaefe9e2245955e01121351662; 13 physical pages. Strict local parse, first-page title/authors/version, last-page bibliography, D02 identity record, and recomputed hash agree. Extracted full text is ../text/PGEL-024.txt.

**Reader:** L09, W24 helper batch L09_B8b; R08 helper-stage passed; mother hash binding pending.
**Coverage:** ../../reading_coverage.json#PGEL-024 (helper section/page evidence retained).

## Tool-use result

Input: the Laurent/rational Kuramoto stationary system on a **specified tree** $T_N$ or **specified cycle** $C_N$, with $N=n+1$, a pinned phase $x_0=1$, and the graph-neighbor monomial support in equation (3). Form the graph adjacency polytope

\[
\nabla_G=\operatorname{conv}\{\pm(e_i-e_j):(i,j)\in E(G)\}\subset\mathbb R^n.
\]

Its normalized volume is an upper bound on the number of isolated $(\mathbb C^*)^n$ roots (Proposition 6, p. 5). For the exact tree and cycle classes, the paper proves this upper bound equals the birationally invariant intersection index of the corresponding function spaces $L_{G,i}$ (Theorems 11 and 15, pp. 7 and 11). Thus the reusable output is a topology-specific algebraic root-count bound / generic root count, not a stability or minimum count.

## Model and scope

The real Kuramoto equilibrium equations, after fixing the rotational gauge $\theta_0=0$, are (2), p. 1. With $x_i=e^{\mathrm i\theta_i}$ and $a'_{ij}=a_{ij}/(2\mathrm i)$, they become the Laurent equations

\[
F_{G,i}(x)=\omega_i-\sum_{j\in N_G(i)}a'_{ij}\left(\frac{x_i}{x_j}-\frac{x_j}{x_i}\right)=0,\qquad x_0=1,\quad i=1,\ldots,n. \tag{3}
\]

They are defined on $(\mathbb C^*)^n$; real phase configurations correspond only to the unit-torus subset $|x_i|=1$. The paper’s algebraic problem allows nonzero constants and complex weights. It defines

\[
L_{G,i}=\operatorname{span}\bigl(\{1\}\cup\{x_i x_j^{-1}-x_i^{-1}x_j:j\in N_G(i)\}\bigr) \tag{4}
\]

and studies the birationally invariant intersection index $[L_{G,1},\ldots,L_{G,n}]$, the generic common-root count in $(\mathbb C^*)^n$ for one generic rational function from each space. The source’s bound chain (5), p. 5, is real count $\le$ complex-torus count $\le$ intersection index $\le$ BKK bound $\le$ adjacency-polytope (AP) bound.

**Do not transfer the numerical count without the graph/support assumptions.** The tree/cycle formulas are not a theorem for arbitrary graphs. An isolated complex root need not lie on the unit torus and says nothing about whether a real equilibrium is stable, a local minimum, or a global minimum. The generic intersection index is not a graph-randomness probability statement. No theorem here addresses C118’s complete signed-random ensemble or its every-second-order-critical-point condition.

## Tree case: exact input, theorem, and proof chain

For a rooted tree, number vertices so each parent precedes its children. Let $\pi(i)$ be the parent and $d(i)$ the depth. Lemma 7, p. 5, defines

\[
\phi_i(y)=y_i\prod_{k=1}^{d(i)-1}y_{\pi^k(i)},\qquad x_i=\phi_i(y).
\]

The exponent matrix is triangular with diagonal 1, hence unimodular. Its inverse is integral; the map is a biholomorphism of $(\mathbb C^*)^n$ (p. 6), so it preserves root count, local multiplicity, and local dimension. Crucially, for every tree edge,

\[
x_i/x_{\pi(i)}=y_i.
\]

The transformed edge exponents are therefore $\pm e_i$. The AP becomes the free sum of the $n$ segments $[-e_i,e_i]$. Lemma 1 (p. 4) factors normalized volume over free sums under its stated interior-point/reflexivity condition; the source applies it here, with each segment having normalized length 2. Theorem 8 (p. 6) obtains

\[
\operatorname{NVol}(\nabla_{T_N})=2^n=2^{N-1}.
\]

To show this AP bound is attained within the algebraic family, Lemma 9 (pp. 6–7) removes leaves inductively: add $a'_{n-1,n}/a'_{n,n-1}$ times the leaf equation (7) to (8), absorbing the leaf contribution into a new constant. This leaves an equivalent system with one equation per parent edge. Under $x=\phi(y)$, it is

\[
\omega_i^*-a'_{i,\pi(i)}(y_i-y_i^{-1})=0,\quad i=1,\ldots,n. \tag{9}
\]

Multiplying equation (9) by $y_i\ne0$ derives the equivalent quadratic
$\omega_i^*y_i-a'_{i,\pi(i)}y_i^2+a'_{i,\pi(i)}=0$ for each coordinate. **Printed/derived distinction (Lemma 10, physical p. 7):** the source literally prints
$\omega_i^*-a'_{i,\pi(i)}y_i^2+a'_{i,\pi(i)}=0$, with no $y_i$ multiplying $\omega_i^*$. That printed expression is not the result of multiplying (9) by $y_i$; the displayed derived equation is the one equivalent to (9). The printed quadratic can separately have two distinct nonzero roots for generic scalar coefficients, but it must not be silently substituted for the equation derived from (9). For the derived independent quadratics, generic coefficients give two distinct nonzero roots each; the product system has $2^n$ nonsingular isolated torus roots (Lemma 10, p. 7). Together with the bound chain this gives Theorem 11 (p. 7):

\[
[L_{T_N,1},\ldots,L_{T_N,n}]=2^n=2^{N-1}.
\]

**Proof boundary:** the construction in Lemma 10 explicitly permits complex coefficients. It establishes algebraic attainability, not that every physical real/symmetric/positive-coupling instance has $2^{N-1}$ roots. The introduction recalls a real tree-equilibrium maximum, but that is not the coefficient construction used in Lemma 10.

## Cycle case: exact input, theorem, and proof chain

For $C_N$, a unimodular lower-triangular coordinate transformation sends the adjacency polytope to

\[
P_N=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n,\pm(e_1+\cdots+e_n)\}\subset\mathbb R^n
\]

(p. 8). Since the origin is interior, a unimodular triangulation of the boundary cones to one of the full polytope, with normalized volume equal to the number of unimodular simplices.

* If $N$ is odd, $P_N$ is the simplicial del Pezzo polytope. The source uses its known facet count and unimodularity to obtain $N\binom{N-1}{(N-1)/2}$.
* If $N$ is even, Proposition 12 (pp. 8–9) describes the facets as
  \[
  \left\{\pm\operatorname{conv}\{\lambda_1e_1,\ldots,\lambda_ne_n,\sum_i e_i\}:\lambda_i\in\{-1,1\},\ \sum_i\lambda_i=1\right\}.
  \]
  The proof rules out other facet vertex sets by a supporting-hyperplane argument. It counts $2\binom{N-1}{N/2-1}$ facets. Proposition 13 and Theorem 14 (p. 10) give normalized facet volume $N/2$, hence
  \[
  \operatorname{NVol}(\nabla_{C_N})=N\binom{N-1}{\lfloor(N-1)/2\rfloor}.
  \]

**Source-local label inconsistency, preserved rather than silently repaired:** on p. 9, the displayed definitions make $G_2=\operatorname{conv}\{0,-e_{(n+1)/2},\ldots,-e_{n-1}\}$, a standard simplex, and $G_1=\operatorname{conv}\{e_1,\ldots,e_{(n-1)/2},-\sum_{i=1}^{n-1}e_i\}$. On p. 10 the prose first correctly calls $G_2$ a standard simplex of normalized volume 1, but then writes $\operatorname{NVol}(\bar F_0)=\operatorname{NVol}(G_1)\operatorname{NVol}(G_2)=\operatorname{NVol}(G_2)$, and says the remaining $G_2$ is unimodularly equivalent to a simplex of volume $(n+1)/2$. These last two occurrences conflict with the definitions and with the immediately preceding $G_2$ statement: the factor of volume $(n+1)/2$ is $G_1$, while $G_2$ contributes 1. This appears to be a $G_1/G_2$ label slip; the intended product and Proposition 13 are unambiguous when read with the displayed definitions. The exact $N=4$ projected facet check in math/verification_results.json gives normalized area 2, consistent with $N/2$. Independent review should decide whether the proof-text label repair is acceptable.

Theorem 15 (p. 11) proves the cycle intersection index equals the AP bound, not only that the AP is an upper bound. Its proof takes a generic $F_{C_N,i}\in L_{C_N,i}$ and checks every nonzero initial direction $v\in\mathbb R^n$. If all support minima are zero, connectedness forces $v=0$. Otherwise a negative minimum at one vertex forces negative minima across adjacent vertices and then all vertices of the connected cycle. Thus, for each edge, the initial system can contain at most one of the two opposing monomials $x_i/x_j,x_j/x_i$; the source concludes its surviving monomials have independent generic coefficients. Lemma 4 then gives no $(\mathbb C^*)^n$ root for any nonzero initial direction, and Bernstein’s criterion (Theorem 3) makes the generic BKK count exact. Using equality of the cycle BKK and AP bounds from the cited adjacency-polytope result yields

\[
[L_{C_N,1},\ldots,L_{C_N,n}]=N\binom{N-1}{\lfloor(N-1)/2\rfloor}.
\]

## Conditions, constants, and limitations

- $N=n+1$; a global phase is removed by $x_0=1$. Tree/cycle claims use these exact graph supports.
- The formulas are exact for the AP volume and birationally invariant intersection index in the stated families. For a fixed non-generic coefficient instance, use the AP volume as an upper bound for isolated torus roots; the number of roots may be smaller, multiple, or non-isolated (the latter are outside an isolated-root count).
- “Generic” means generic choices in the corresponding coefficient/rational-function spaces, outside the exceptional algebraic set. It is not a claim about a random signed graph or about a discrete coefficient law.
- Real phase solutions are a subset of the complex-torus solutions through $|x_i|=1$. The complex count does not itself prove a count of physical phase solutions.
- No Hessian/Jacobian sign, Lyapunov stability, energy-minimum classification, basin estimate, or probability estimate is supplied. Root count is not a stable-equilibrium count.
- The even-cycle p. 10 $G_1/G_2$ label inconsistency is explicitly isolated above. The theorem formula is also checked by exact finite arithmetic; no universal geometry claim is inferred from that computation.

## Reusable method card

For a deterministic graph exactly in the tree/cycle classes: (1) encode the stationary equations by their Laurent support; (2) build the signed edge-difference adjacency polytope; (3) use a unimodular monomial map to reduce tree edges to independent coordinates, or a unimodular polytope map plus facet decomposition for cycles; (4) compute normalized volume; (5) use the AP inequality for a fixed parameter instance and the BI-index/BKK argument only for generic root counts/equality. Keep unit-torus reality and stability as separate tasks.

**Local math evidence:** math/verification_results.json and math/verify_pgel024.py. Python/SymPy exact arithmetic checks several finite rooted-tree exponent matrices and edge ratios, the $2^n$ signed-simplex count, the cycle facet-count formula for $N=3,\ldots,20$, and a projected $N=4$ facet area. These computations are examples/arithmetic checks only; the general tree and cycle claims rely on the source’s proofs.

**Review:** pending. This card is an L09 helper contribution; it is not integrated into the W24 mother ledger or installed skill.

