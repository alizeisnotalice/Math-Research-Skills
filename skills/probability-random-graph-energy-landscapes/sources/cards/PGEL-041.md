> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-041 — On the Stability of the Kuramoto Model of Coupled Nonlinear Oscillators

**Read basis.** Jadbabaie–Motee–Barahona, author-hosted ACC 2004 full-paper manuscript, DOI [10.23919/ACC.2004.1383983](https://doi.org/10.23919/ACC.2004.1383983), 8 physical pages, SHA-256 c4b9b8fff56834009a041db1122e68b0bade7fd2a39dcaa0b97c156c1c40cd3f. All eight pages, including conclusions, acknowledgments, and references, were read and visually inspected. The p. 3 weighted-Laplacian inequality and p. 7 Theorem 2 proof were checked from renders because the PDF text layer needed xref correction.

## Model, hypotheses, and conclusions

The paper studies \(N\) phases on an arbitrary connected undirected graph with incidence matrix \(B\), Laplacian \(L=BB^T\), and positive coupling \(K\):
\[
\dot\theta=\omega-\frac K N B\sin(B^T\theta).
\]
For identical frequencies, a rotating frame sets the centered frequency to zero. Theorem 1 (physical p. 3) states that for every \(K>0\), every trajectory converges to the **set** of equilibria, the synchronized state is locally asymptotically stable, and its local approach rate is at least \((2K/(\pi N))\lambda_2(L)\). It does not assert that every trajectory converges to synchrony: the proof itself notes other locally stable equilibria may occur (e.g. ring twists).

The proof uses
\[
U_1=1-r^2=\frac4{N^2}\left\|\sin\frac{B^T\theta}{2}\right\|_2^2,
\qquad \dot U_1=-\frac{2}{KN}\|\dot\theta\|_2^2\le0,
\]
then LaSalle. For the local rate it introduces \(W(\phi)=\mathrm{diag}(\mathrm{sinc}(\phi_i))\), \(\phi=B^T\theta\), so the weighted Laplacian is \(BWB^T\). On the phase-cohesive region \(|\phi_i|<\pi/2\), \(\mathrm{sinc}(\phi_i)\ge 2/\pi\), giving the needed lower spectral comparison by the Rayleigh quotient.

## Source mismatch at physical p. 3

The printed display reads
\[
\lambda_2(BW(\phi)B^T)\;\boldsymbol{\le}\;\frac2\pi\lambda_2(BB^T),
\]
but the adjacent rate estimate requires the reverse lower bound. The printed direction is false even at \(\phi=0\): for the two-node, one-edge graph, \(\lambda_2(BB^T)=2\), \(W=1\), so the left side is \(2\) while the displayed right side is \(4/\pi<2\). The separately derived lower bound is valid on the cohesive region since every diagonal weight is at least \(2/\pi\). Keep the literal source typo/mismatch isolated; it does not by itself refute Theorem 1 or the independently checked Rayleigh-quotient comparison.

## Heterogeneous, time-constant frequencies

The paper treats \(\omega_i\) as fixed but uncertain parameters, not as a random process and not through a probability theorem. It projects to grounded coordinates \(\bar\theta=V^T\theta\), \(\bar\omega=V^T\omega\) to remove common rotation. The reported bounds include:

- For a complete graph, \(K_L>N\|\omega\|_\infty/d_{\max}\), sharpened to \(K_L\ge N\|B^T\omega\|_\infty/[2(N-1)]\), are lower bounds on the critical coupling. They follow from necessary fixed-point constraints and are not, by themselves, sufficient existence tests for every \(K\) above the bound.
- **Printed tree claim isolated (physical p. 6, Remark 10).** The manuscript states \(K_L>\|B^TL^\#\omega\|_\infty\) as necessary and sufficient for a tree, but this displayed threshold omits the factor \(N\) present in the model's \(K/N\) coupling. It is not a verified fixed-point certificate. For the two-vertex one-edge tree, choose the oriented incidence \(B=(1,-1)^T\), centered \(\omega=(1,-1)\), and \(K_L=3/2\). Then \(L^\#=\frac14\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), so the printed threshold is \(K_L>1\), which holds. Yet equilibrium requires \(\omega=(K_L/N)B\sin(B^T\theta)\), so \(\omega_1=(K_L/2)\sin(\theta_1-\theta_2)\), requiring \(\sin(\theta_1-\theta_2)=4/3\), impossible. Keep this source statement quarantined; the Brouwer existence result below is separate and remains independently described. For a general graph the paper says the displayed tree bound is only necessary.
- A Brouwer argument gives a stated existence bound \(K\ge 2\sqrt N\|\omega\|_2/\lambda_2(L)\).
- Theorem 2 (physical p. 7) states that this last condition gives at least one fixed point with either \( |\theta_i|<\pi/4\) for all vertices or \( |(B^T\theta)_i|<\pi/2\) for all edges, and that \(K\ge (\pi^2/4)N\lambda_{\max}(L)\|\omega\|_2/\lambda_2(L)^2\) gives only one stable fixed point modulo common phase and an increasing order parameter. The Banach-contraction proof derives a **strict** \(K>(\pi^2/4)N\lambda_{\max}(L)\|\omega\|_2/\lambda_2(L)^2\) at its final contraction step. Preserve this equality-endpoint gap; do not silently upgrade the strict proof to equality.

The theorem is deterministic conditional on the graph and frequency vector. The conclusion explicitly leaves distributional frequency bounds for future work.

## Proof route and limits

For identical frequencies, the order-parameter Lyapunov function and weighted graph Laplacian give convergence to the equilibrium set and local synchronization rate. For nonidentical frequencies, the authors use grounded coordinates, Laplacian pseudoinverse estimates, Brouwer for existence, and a Lipschitz estimate for the sinc-weighted map plus Banach for uniqueness at sufficiently large coupling. The latter is only a sufficient condition and depends on positive cohesive weights and the given graph's spectral gap.

For random-graph use, one must separately establish high-probability bounds for \(\lambda_2(L)\), \(\lambda_{\max}(L)\), and any frequency norm. The paper does not provide such probability estimates. Its theorem also does not rule out stable nonsynchronous states in the identical-frequency model. The p. 6 printed tree threshold is excluded as a verified certificate by the explicit counterexample above; this local issue does not invalidate the separately proved Brouwer statement.

## Local exact check

The script ../math/pgel_l12_b10_verify_examples.py uses exact SymPy arithmetic for the two-node graph: it checks the printed p. 3 direction \(2>4/\pi\), and the p. 6 witness \(\|B^TL^\#\omega\|_\infty=1<K_L=3/2\) while the fixed-point equation requires \(\sin\delta=4/3\). It also checks the three-node path cut-vertex Jacobian only as a finite diagnostic. These exact finite checks do not replace the paper's general stability proof.
