> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-023 — Equilibria in Kuramoto Oscillator Networks: An Algebraic Approach

**Reader:** L09, W24 helper batch L09_B8; R08 helper-stage passed; mother hash binding pending.  
**Source version:** Nguyen, Budzinski, Doan, Pasini, Minac, and Muller, arXiv:2111.02568v2 (24-page author-version PDF); journal version *SIAM Journal on Applied Dynamical Systems* 22(2) (June 2023), pp. 802–824, DOI 10.1137/21M1457321. The card’s theorem/page locators refer to the exact local arXiv v2 PDF, SHA-256 `ad7a30a2735b823124210a62361906ff06ba6f8cf61d0b2a5ce58bdd28d89cdd`.

## Model distinction

In a rotating frame with homogeneous intrinsic frequencies, the original system is

\[
\dot\theta_i=\epsilon\sum_j a_{ij}\sin(\theta_j-\theta_i).
\]

The paper introduces a **different complex-valued dynamical system** with an added \(-i\cos\) term. Under \(x_i=e^{i\theta_i}\), that complexified system becomes the linear ODE \(\dot x=\epsilon Ax\), with solution \(x(t)=e^{\epsilon tA}x(0)\). Remark 1 (physical p. 4) stresses that the two systems have different trajectories; the paper transfers certain **stationary configurations** to the original nonlinear system. An equilibrium construction is not a stability result.

## Exact eigenvector-to-equilibrium mechanism

Lemma 1 and Proposition 1 (physical p. 5) give the matrix-exponential/eigenvector step for the complexified model. Proposition 2 (physical pp. 5–6) states: if \(A\) is a real matrix and \(x_0=(e^{i\theta_1},\ldots,e^{i\theta_N})\) is an eigenvector of \(A\) with a real eigenvalue \(\lambda\), then \(\theta_0\) is an equilibrium of the original Kuramoto model. The proof conjugates \(Ax_0=\lambda x_0\), uses realness of \(A\) and \(\lambda\), and subtracts the resulting relations to recover the sine-zero equations.

For phase lag \(\phi\), Proposition 7 (physical pp. 11–12) says if the unit-modulus vector \(x_0=e^{i\theta_0}\) is an eigenvector of real \(A\) with eigenvalue \(\lambda\), and

\[
\lambda e^{-i\phi}\in\mathbb R,
\]

then \(\theta_0\) is an equilibrium of the original phase-lag system. On physical p. 12 the proof explicitly reduces the equilibrium residual to \(\lambda e^{-i\phi}-\overline{\lambda e^{-i\phi}}=0\). Proposition 8 (p. 12) allows a rowwise version: for each \(i\), assume \(\sum_j a_{ij}e^{i\theta_j}=\lambda_i e^{i\theta_i}\) and \(\lambda_i e^{-i\phi_i}\in\mathbb R\); then the corresponding row-lag system is stationary. No symmetry assumption is needed for this algebraic cancellation, but a real adjacency matrix and the stated unit-modulus vector are essential.

## Structured equilibrium families

* **Circulants (Proposition 3, physical pp. 6–7):** Fourier eigenvectors of a symmetric circulant matrix yield twisted equilibria. This is existence of equilibria, not a classification of stable states.
* **Complete graphs (Propositions 4–5, physical pp. 8–10):** for the zero-frequency complete-graph model, an equilibrium exists iff either all phase differences are integer multiples of \(\pi\), or the order parameter vanishes:
  \[
  \sum_{i=1}^N e^{i\theta_i}=0.
  \]
  In the proof, the zero-sum case makes the phase vector an eigenvector of the complete-graph adjacency matrix with eigenvalue \(-1\). In the nonzero-sum case, the stationarity equation forces \(e^{2i\theta_i}\) to be independent of \(i\); after a common phase rotation the phases are in \(\{0,\pi\}\). This is a complete equilibrium classification for this model, not a stability classification.
* **Finite-group circulants (Propositions 9–10, physical pp. 15–16):** one-dimensional characters of a finite group give eigenvectors of a group-circulant matrix, with eigenvalue \(Y_\chi=\sum_{\sigma\in G}c_\sigma\chi(\sigma)\). Choosing a common phase lag to make \(Y_\chi e^{-i\phi}\) real gives a phase-lag equilibrium.
* **Two-layer block networks (Propositions 11–12, physical pp. 17–18):** extending a circulant eigenvector into a block matrix gives equilibria; Proposition 12 includes arbitrary real cross-layer constants \(\alpha,\beta\), so the block matrix need not be symmetric when \(\alpha\ne\beta\). The result is still only stationarity. The illustrations use numerical time integration.
* **Random-network section (physical pp. 19–20):** the authors alter a sampled adjacency matrix using an eigendecomposition to design an equilibrium. This does not establish a typical-graph or whp statement for an unmodified random graph.

The computational appendix (physical p. 22) specifies Euler integration with step \(10^{-4}\) and a matrix-exponential computation. These plots illustrate the constructions; they are not evidence of asymptotic probability or stability.

## Practical proof pattern and limits

When a candidate phase vector has unit-modulus coordinates, test whether it is an eigenvector of the real adjacency matrix. For zero lag, a real eigenvalue gives the sine-balance condition; for a common lag, the scalar reality test is \(\lambda e^{-i\phi}\in\mathbb R\). For row-specific lags, apply the same test coordinatewise. This is a sufficient construction method and is not exhaustive outside the complete-graph classification. The complexified linear dynamics do not imply the original nonlinear dynamics are linear or stable.

## Local exact check

`math/verify_w24_examples.py` uses the 4-cycle adjacency matrix and \(x=(1,i,-1,-i)\), verifies \(Ax=0\), and symbolically checks the original phase-lag sine sums vanish for every real \(\phi\). This is one finite exact example of Proposition 7, not its proof. The rendered theorem/classification pages 9, 10, 12, 15, and 18 were viewed; full physical-page coverage is in `reading_coverage.json#sources.PGEL-023`.

## Boundary for W24/C118

The paper gives exact stationary-state constructions and one complete-graph equilibrium classification under the original model’s assumptions. It gives no second-order stability certificate and no random-signed-graph probability theorem. Its eigenvector criterion cannot be applied to a generic eigenvector unless every coordinate has modulus one; the random-network plots follow a matrix modification step.
