> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-001 — Benign landscapes for synchronization on spheres via normalized Laplacian matrices

## Identity and reading record

- Andrew D. McRae, arXiv:2503.18801v2, manuscript front page dated 24 August 2026; 28-page author manuscript. DOI: 10.48550/arXiv.2503.18801. Official record: <https://arxiv.org/abs/2503.18801v2>.
- Local PDF: ../pdfs/PGEL-001.pdf
- SHA-256: dc1a69bcf5f2dee0be85f4dec77bad21a283a3400201957bb66ddf64f57e1cb1.
- Read all 28 PDF pages, including the full reference list. Key formula pages 6–8, 10–11, 13, 15–19, and 19–24 were checked against rendered pages. Section-by-section record: ../../reading_coverage.json.
- Review status: pending. No claim is made that the preprint has a peer-reviewed version.

## Model and quotient

The paper first studies the real spherical relaxation
\[
\max_{Y\in\mathbb R^{n\times r}}\langle C,YY^\top\rangle
\quad\text{subject to }\|Y_{i,:}\|_2=1\ (1\le i\le n),
\tag{1}
\]
with symmetric \(C\). At \(r=2\), write \(Y_{i,:}=(\cos\theta_i,\sin\theta_i)\); then \((YY^\top)_{ij}=\cos(\theta_i-\theta_j)\). For symmetric couplings the phase dynamics is a gradient flow, and simultaneous rotation of all rows is a symmetry. The natural state is therefore an orbit / phase quotient, not a unique phase vector.

## Exact landscape certificate

**Theorem 2.1 (PDF p. 6).** Let \(z\in\{\pm1\}^n\), and let
\[
L(z)=\operatorname{ddiag}(Czz^\top)-C.
\]
Assume \(L(z)\succeq0\) and \(\lambda_2(L(z))>0\). For any strictly positive diagonal preconditioner \(D\), put \(L_D=D^{-1/2}L(z)D^{-1/2}\). If
\[
r>\lambda_n(L_D)/\lambda_2(L_D),
\]
then every second-order critical point of (1) is a global optimum and satisfies \(YY^\top=zz^\top\). The conclusion is an all-second-order-critical-point landscape statement, not merely an a.e.-initial-condition basin statement.

The proof in §6.1 (PDF pp. 19–22) uses the diagonal-scaled Laplacian certificate and a tangent direction built from a **D-weighted** decomposition. With \(\langle x,y\rangle_D=\langle x,Dy\rangle\), it sets
\[
v=\frac{Y^\top D\mathbf1}{\operatorname{tr}D},\qquad
W=Y-\mathbf1v^\top,
\]
so \(W^\top D\mathbf1=0\). This is weighted column orthogonality; it does **not** assert that every row of \(W\) is orthogonal to \(v\). The second-order condition bounds a quadratic form in \(W\); the first-order condition and a Schur-product/trace estimate then force \(\|v\|=1\), so all rows agree up to the planted signs. The proof is deterministic once the displayed PSD and spectral-gap assumptions hold. §6.2 (pp. 22–24) gives the corresponding complex/Hermitian extension, with the extra requirement \(L(z)z=0\).

## Random signed model and consequence

The symmetric signed Erdős–Rényi model is defined in (6), PDF p. 8: for each unordered pair \(i<j\), independently,
\[
C_{ij}=z_i z_j\text{ with probability }(1+\delta)p/2,\quad
C_{ij}=-z_i z_j\text{ with probability }(1-\delta)p/2,\quad
C_{ij}=0\text{ with probability }1-p,
\]
and \(C_{ji}=C_{ij}\) (diagonal entries are zero). The parameters may depend on \(n\).

**Theorem 3.2 (PDF pp. 8–9).** For fixed \(\eta\in(0,1)\) independent of \(n\), if
\[
\frac{np}{\log n}\left(1-\sqrt{1-(1-\eta)\delta^2}\right)\ge1,
\]
then with probability tending to one every second-order critical \(Y\), for every rank \(r\ge2\), has \(YY^\top=zz^\top\). At \(r=2\) this gives synchronization in the associated symmetric signed Kuramoto phase model. The probability is over the random graph/sign matrix, and the conclusion is stronger than global synchronization from almost every initial condition.

**Transfer limit for C118.** The formal C118 model is the complete-graph special case \(p=1\) with its particular sign bias. The theorem supplies a sufficient regime of order \(\delta\gtrsim\sqrt{2\log n/((1-\eta)n)}\) when \(\delta\) is small. This is about twice the scale \((1+\epsilon)\sqrt{\log n/(2n)}\) asked about in C118 (up to the slack factor); it does not settle that exact threshold. It is a rigorous partial upper regime, not a proof of the conjectured onset.

## Other usable statements and proof boundaries

- **Theorem 3.4 (PDF p. 10).** For symmetric \(A\) with every entry of \(A\mathbf1\) strictly positive, set \(D=\operatorname{diag}(A\mathbf1)\), \(L=D-A\), and \(\mathcal L=I-D^{-1/2}AD^{-1/2}\). If \(\lambda_2(L)>0\), either \(\lambda_n(L)/\lambda_2(L)<2\) or \(\lambda_n(\mathcal L)/\lambda_2(\mathcal L)<2\) implies global synchronization. This is a deterministic sufficient test. The theorem also gives, for every \(\epsilon>0\), connected unweighted regular graphs with condition-number ratios at most \(2+\epsilon\) that are not globally synchronizing; the threshold is sharp for this test, not a universal graph classification.
- **Theorem 3.5 (PDF pp. 10–11).** Nearest-neighbor circulant graphs have stable twisted equilibria in parameter ranges beyond the condition-number threshold. In the proof in §5.2 (physical PDF pp. 16–19), the authors leave several steps to numerical verification: on p. 17, the maximizer of \(H_{L,\mu}[m]\) for \(\mu\ge0.59\) and strict decrease of \(\kappa(\mu)\) on \([0.6,1]\); on p. 18, the bound \(H_{L,\mu}[3]/H_{L,\mu}[1]\ge2.2\) for \(\mu\le0.6\) and the minimum-Fourier-coefficient check for the twisted-state Hessian at \(k\ge0.3n\). Preserve this scope: these are numerical checks/approximations in the proof, not analytic inequalities derived there. PDF p. 20 is already in §6.1's Hessian proof.
- **Theorem 4.1 (PDF p. 13).** A diagonal-normalization comparison gives a normalized-Laplacian condition-number bound in terms of a relative perturbation \(\delta_C\); §5.1 uses \(\delta_C<1/3\) to obtain a condition number below \(2\). The random signed proof in §5.1 (pp. 15–19) explicitly reuses concentration arguments from reference [39], so the random theorem is not self-contained with respect to those concentration estimates.
- The regular-graph application on PDF p. 12 is a sufficient high-degree statement (degree at least 35, via a spectral/Ramanujan estimate). It does not prove synchronization for uniformly random 3-regular graphs.

## Use and non-use

Use this paper for symmetric signed random-matrix landscapes, a deterministic second-order certificate, and the distinction between global landscape benignity and basin-of-attraction synchronization. Do not apply its gradient/Hessian argument to an oriented coupling matrix. Do not replace its signed Erdős–Rényi model by a random 3-regular model. Do not cite it as settling C118 at the prompt's smaller threshold.
