> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-010 — The energy landscape of the Kuramoto model in random geometric graphs in a circle

## Identity and reading record

- Cecilia De Vita, Julián Fernández Bonder, Pablo Groisman. arXiv:2402.06744v2, 22 July 2024; published in SIAM Journal on Applied Dynamical Systems 24(1) (2025), DOI 10.1137/24M1642111. Official record: <https://arxiv.org/abs/2402.06744>.
- Local PDF: ../pdfs/PGEL-010.pdf
- SHA-256: e8cdbd8c6b0d36b8a3eb87b7ac21b7a2318c2f3ae72addaebd82cc741132effc.
- Read all 15 PDF pages, including references. Pages 2–3, 5–7, 9–12 were visually checked; formula pages 6–7 and the energy comparison on p. 10 were rendered. Coverage: ../reading_coverage.json.
- Review pending. No claim is made that the arXiv pagination is identical to the journal pagination.

## Model, phase quotient, and theorem quantifiers

Take \(n\) iid uniform points on the circle and connect two vertices when their geodesic distance is less than \(\epsilon_n\). The theorem assumes
\[
n\epsilon_n^2\longrightarrow0,\qquad
\frac{n\epsilon_n}{\log n}\longrightarrow\infty.
\tag{1.1}
\]
Thus the range shrinks while the graph is connected with high probability. The homogeneous, symmetric, positive, unit-edge Kuramoto equation is (1.2), PDF p. 2. Its gradient energy, with each undirected edge counted twice in the displayed ordered sum, is
\[
E_n(\theta)=\frac{\pi}{2n^2\epsilon_n^3}
\sum_{i=1}^n\sum_{j\sim i}\bigl(1-\cos(\theta_j-\theta_i)\bigr).
\]
Common phase shifts are a symmetry. The authors restrict to the invariant zero-sum slice; strict stability is consequently understood on that slice / modulo the common rotation.

**Theorem 1.1 (PDF p. 3).** For each fixed \(q\in\mathbb Z\),
\[
\Pr\{\text{the random-graph ODE (1.2) has an asymptotically stable equilibrium of index }q\}\to1.
\]
The probability is over the iid vertex sample. The statement is per fixed \(q\); it does not say that all \(q\)'s are realized simultaneously at finite \(n\), and it does not assert global synchronization. For each fixed nonzero \(q\), it yields a nonsynchronous stable state with high probability, so the sampled graphs fail the a.e.-initial-condition global-synchronization property. The \(q=0\) case is the synchronous state: under (1.1) the graph is connected with high probability, and its graph-Laplacian Hessian is positive on the zero-sum slice. It should not be routed through the strict test event \(E_n(u_q)<q^2/5\), which becomes the impossible \(0<0\).

## Winding sectors and existence/stability proof

Section 2 (PDF pp. 4–5) removes configurations with adjacent antipodal phases, where the shortest phase geodesic is ambiguous, and defines the integer winding index \(I\). The open sets \(K_q=\{I=q\}\) are the connected components of the admissible part of the phase torus. Their boundaries contain an adjacent antipodal pair. The global-rotation symmetry is handled by the zero-sum slice.

The proof on PDF pp. 9–11 has three ingredients:

1. A Bernstein/union-bound estimate for neighbor counts and common-neighbor counts. Under (1.1), it shows the minimum energy on \(\partial K_q\) diverges almost surely; the explicit lower scale in (3.7) is \(1/(8n\epsilon_n^2)\).
2. The test lift \(u_q(x)=qx\) lies in \(K_q\). If its energy is below \(q^2/5\), the minimum of \(E_n\) on \(\overline K_q\) cannot lie on the boundary, so an interior local minimum exists.
3. If any edge's **shortest circular phase difference** at that minimizer has magnitude at least \(\pi/2\), the common-neighbor lower bound forces its energy to diverge, contradicting the bounded \(q^2/5\) test energy. Thus every edge's shortest representative is strictly below \(\pi/2\); the weighted graph Laplacian Hessian is positive on the zero-sum slice. This gives a strict local minimum and asymptotic stability modulo rotation.

The source cites Proposition 3.1 for the test energy. That proposition has a factor-two normalization error as printed; details and an independent correction follow.

## Source defect: Proposition 3.1 normalization

**Printed claim (PDF p. 5).** For \(u\in C^2([0,2\pi],\mathbb R)\),
\[
E_n(u)\xrightarrow{\mathbb P}\frac1{12\pi}\int_0^{2\pi}|u'(x)|^2\,dx.
\]
For \(u_q(x)=qx\), this is \(q^2/6\). The proof begins with a Poissonized energy \(E(u)\) carrying the same \(\pi/(2n^2\epsilon_n^3)\) coefficient as \(E_n\) on p. 5, and claims \(E(u)-E_n(u)\to0\).

**Mismatch in the printed proof.** On PDF p. 7 the auxiliary variables are defined by
\[
Z_i^n=\frac{\pi}{n\epsilon_n^3}\sum_{j\in\mathcal N(i)}\zeta_j^i,
\qquad E(u)=\frac1n\sum_{i=1}^N Z_i^n.
\]
This makes the auxiliary expression \(\pi/(n^2\epsilon_n^3)\) times the ordered neighbor sum, twice the finite-graph energy displayed on PDF pp. 2 and 5. The subsequent conditional-expectation calculation on p. 7 follows this doubled normalization.

**Independent exact check.** For fixed nonzero integer \(q\), \(0<\epsilon<\pi\), let
\[
h_q(x,y)=\mathbf1_{\{d(x,y)<\epsilon\}}\bigl(1-\cos(q(y-x))\bigr).
\]
For iid uniform circle points, translation invariance and the ordered-pair sum give
\[
\mathbb E E_n(u_q)
=\frac{n-1}{4n\epsilon^3}\int_{-\epsilon}^{\epsilon}(1-\cos(qz))\,dz
=\frac{n-1}{2n\epsilon^3}\left(\epsilon-\frac{\sin(q\epsilon)}q\right)
\longrightarrow\frac{q^2}{12}.
\]
The local SymPy calculation is saved at ../math/pgel010_energy_normalization.py, with output in ../math/pgel010_energy_normalization.json. It evaluates the integral exactly as \(2\epsilon-2\sin(q\epsilon)/q\).

This is also convergence in \(L^2\), not merely an expectation comparison. For an unordered edge kernel \(h_q\), \(0\le h_q\le q^2\epsilon^2/2\) and \(\Pr(d(X,Y)<\epsilon)=\epsilon/\pi\), so \(\mathbb E h_q^2\le q^4\epsilon^5/(4\pi)\). Conditional on one endpoint, \(\mathbb E[h_q(X,Y)\mid X]\) is constant by rotation invariance; hence distinct unordered-edge terms have zero covariance even when they share one vertex. Therefore
\[
\operatorname{Var}(E_n(u_q))
\le\frac{\pi q^4(n-1)}{8n^3\epsilon_n}\longrightarrow0
\]
under (1.1). Thus \(E_n(u_q)\to q^2/12\) in probability for every fixed nonzero \(q\). The p. 7 doubled auxiliary normalization instead has limit \(q^2/6\). This special test-function calculation falsifies the stated universal Proposition 3.1; it does not by itself establish a corrected limit for every \(u\in C^2\).

**Consequence for use.** Proposition 3.1 is false with the displayed normalization and should not be cited as written. This error does not by itself refute Theorem 1.1: the main proof on p. 10 only needs \(E_n(u_q)<q^2/5\), and the corrected limit \(q^2/12\), together with the variance bound above, supplies that event with probability tending to one. The p. 9–11 boundary and Hessian steps then retain their stated energy slack. This is a local repair of that proof interface, not a claim that the paper's printed proposition is correct.

## Scope limits

- The theorem is for a one-dimensional circle geometric graph in the specific regime (1.1), not an arbitrary random graph or signed graph.
- The per-fixed-\(q\) high-probability existence statement is distinct from probability-one-in-initial-state global synchronization.
- Section 4 (PDF pp. 11–13) discusses k-nearest-neighbor, Boolean, weighted, and higher-dimensional extensions as expected/proposed extensions with additional arguments; do not upgrade those discussion claims to Theorem 1.1.
