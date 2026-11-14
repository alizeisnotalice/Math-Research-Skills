> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-045 — The Kuramoto Model on the Sierpinski Gasket II: Twisted States

**Read basis.** Medvedev–Mizuhara, Springer Nature version of record, *Journal of Nonlinear Science* 36 (2026), article 70, DOI [10.1007/s00332-026-10285-5](https://doi.org/10.1007/s00332-026-10285-5), published 15 June 2026. The 33-page PDF SHA-256 is 8d635dd3c083972a6a1f8fff2df2a8e0fb0693b81f5568d07f11d6984457af49. Physical pp. 1–33 were read in order, including references and declarations. The harmonic extension matrix, Γ-limit proof, stable-equilibrium approximation theorem, p.c.f. assumptions, and Theorems 7.1/7.3 were checked against renders (notably physical pp. 3–13, 17–20, 25–32).

## Model and main SG theorem

For the level-\(n\) nearest-neighbor graph \(\Gamma_n=(V_n,E_n)\) approximating the Sierpinski gasket \(K\), the authors study
\[
\dot u(t,v_i)=\left(\frac53\right)^n\sum_{j\sim_n i}
\sin\bigl(2\pi(u(t,v_j)-u(t,v_i))\bigr),
\qquad
J_n(u)=\frac{(5/3)^n}{4\pi^2}
\sum_{\{i,j\}\in E_n}(1-\cos(2\pi(u(v_j)-u(v_i)))).
\]
Each undirected edge is counted once. The system is a gradient flow \(\dot u=-2\pi\nabla J_n\); the phase \(u(v_1)=0\) fixes the common-rotation symmetry. The graph sequence, coupling, and continuum limit are deterministic.

A map \(f:K\to\mathbb T\) has a finitely supported integer degree vector \(\bar\omega(f)\), built from winding numbers on the enumerated triangular loops. Theorem 1.4 (physical p. 5; quoted from Part I) identifies homotopy classes by equality of these degree vectors and gives the unique harmonic circle-valued map for a prescribed degree vector with the pinned value and natural zero-Neumann boundary conditions.

**Theorem 1.5 (physical p. 6).** Fix a finitely supported degree vector \(\omega^*\in\mathbb Z^*\) and its harmonic map \(u^*\in C(K,\mathbb T)\) solving (1.12)–(1.15): \(\Delta u^*=0\), \(u^*(v_1)=0\), \(\partial_nu^*(v_i)=0\) for \(i=1,2,3\), and \(\bar\omega(u^*)=\omega^*\). For every \(\varepsilon>0\), there is \(N\) such that for every \(n\ge N\), the KM on \(\Gamma_n\) has a stable steady state \(u_n\) with a continuous extension \(\tilde u_n\) satisfying the same degree and
\[
\max_{x\in K}|\tilde u_n(x)-u^*(x)|<\varepsilon.
\]
This is an existence/approximation theorem; it does not assert uniqueness of the discrete stable state.

## Proof mechanism and supporting results

- **SG harmonic structure (§2, physical pp. 7–9).** The graph Dirichlet energy is renormalized by \((5/3)^n\), and the harmonic extension formula (2.9, p. 8) maps boundary values \((a,b,c)\) to the three inserted values by
  \[
  \begin{pmatrix}f(x)\\f(y)\\f(z)\end{pmatrix}
  =
  \begin{pmatrix}
  2/5&2/5&1/5\\
  1/5&2/5&2/5\\
  2/5&1/5&2/5
  \end{pmatrix}
  \begin{pmatrix}f(a)\\f(b)\\f(c)\end{pmatrix}.
  \]
  Lemma 2.2 gives the energy-to-Hölder bound with exponent \(\beta=\log(5/3)/(2\log2)\).
- **Theorem 3.3 (§3, physical pp. 9–12).** On continuous real-valued functions with fixed Dirichlet data at \(V_0\), the authors invoke the known Γ-convergence of the discrete Dirichlet energies \(E_n\) to the SG form \(E\) and prove that the Kuramoto energies \(J_n\) have the same Γ-limit in the sup norm. The liminf proof uses uniform convergence/equicontinuity to make neighboring increments small, Taylor's formula \(1-\cos(2\pi x)=2\pi^2x^2(1+g(x))\), and \(|g(x)|\le\pi^2|x|^2/3\). The constant recovery sequence gives the limsup. Convergent sequences of minimizers then limit to harmonic minimizers.
- **Theorem 3.4 (§3, physical pp. 12–13): printed step and derived completion.** The source's boundary-minimizer contradiction uses compactness, \(\Gamma\)-convergence, and uniqueness, but the physical p. 13 passage from uniform convergence to convergence in the fixed \(C^\beta\) norm is not justified there as printed. R06's neutral adjudication supplies a separate energy completion for the original Sierpinski-gasket real Dirichlet problem. Let \(h_n\) be the harmonic-spline minimizers, \(u^*\) the continuum harmonic minimizer, and
  \[
  \delta_n=\max_{\{v_i,v_j\}\in E_n}|h_n(v_i)-h_n(v_j)|.
  \]
  Under the assumed boundary alternative, all \(h_n\) lie in the fixed \(C^\beta\) ball, so the source's Hölder estimate gives \(\delta_n\le M2^{-n\beta}\), with fixed \(M=\|u^*\|_\beta+\epsilon\). Thus \(\eta_n=c\delta_n^2\to0\), where \(c=\pi^2/3\). The cosine comparison gives
  \[
  (1-\eta_n)\,\mathcal E(h_n)=(1-\eta_n)\mathcal E_n(h_n)
  \le J_n(h_n)\le J_n(u^*)\le\mathcal E_n(u^*)=\mathcal E(u^*).
  \]
  These are the source-specific harmonic-spline premises: \(h_n\in X_n\) gives \(\mathcal E(h_n)=\mathcal E_n(h_n)\), and \(u^*\in X_n\) is an admissible competitor with harmonic compatibility \(\mathcal E_n(u^*)=\mathcal E(u^*)\). Dirichlet minimization gives \(\mathcal E(h_n)\ge\mathcal E(u^*)\), hence
  \[
  0\le\mathcal E(h_n)-\mathcal E(u^*)\le
  \frac{\eta_n}{1-\eta_n}\mathcal E(u^*)\longrightarrow0
  \]
  for large \(n\) with \(\eta_n<1\). If \(\mathcal E(u^*)=0\), the comparison directly forces zero energy. Since \(h_n-u^*\) vanishes on the fixed boundary and \(u^*\) is harmonic, first-variation orthogonality yields \(\mathcal E(h_n-u^*)=\mathcal E(h_n)-\mathcal E(u^*)\to0\). Lemma 2.2 then gives \([h_n-u^*]_\beta\le C\sqrt{\mathcal E(h_n-u^*)}\); the fixed boundary pinning also controls the sup norm, so \(h_n\to u^*\) in the full \(C^\beta\) norm. This contradicts a fixed positive boundary radius. This is an adjudicated derived proof step, not text supplied by the paper at p. 13. Its scope is the §3 SG real-valued fixed-Dirichlet setting and its stated harmonic/energy hypotheses; §6's fixed-degree affine lift uses it conditionally with the same fixed finite-cell setup. §7's p.c.f. extension remains conditional on its stated energy, cut-point, fixed-cycle-basis, and Hölder assumptions; this check does not independently verify every p.c.f. instance or make the result automatic for all p.c.f. sets.
- **§4, nearest-neighbor ring comparison (physical pp. 13–18).** The authors lift a fixed winding-\(q\) class to real-valued functions with endpoint jump \(q\), prove Γ-convergence on that constrained space (Theorem 4.2), and transfer minimizer convergence. Half-twisted states are separately identified as saddles; do not conflate them with stable twists.
- **§5 (physical pp. 18–25), circle-valued harmonic maps.** A covering-space fundamental domain is cut along selected loops; the fixed jump/winding data become boundary conditions on the cut domain. Harmonic minimization and harmonic extension produce the map, and Lemma 5.3 verifies natural zero-Neumann conditions. The higher-order degree construction uses a cycle-space basis and cut points and invokes cited results from Medvedev–Mizuhara (2026); it is not a proof for an arbitrary unstructured graph.
- **§6 (physical pp. 25–27), proof of Theorem 1.5.** On the cut fundamental domain, the discrete \(J_n\) Γ-converge to the corresponding Dirichlet form. The proof combines this with the Hölder/compactness estimates, finite-dimensional harmonic-spline minimization, and the no-boundary-minimizer contradiction from Theorem 3.4, then projects the lift to the circle. The fixed degree is preserved.
- **§7, p.c.f. fractals (physical pp. 27–32).** The extension assumes a nonempty connected compact self-similar set with contractive similitudes, finite post-critical boundary, a harmonic structure, energy scaling (7.3) with \(0<r_i<1\), and the exact minimization compatibility (7.4). Theorem 7.1 constructs a harmonic circle map for a **fixed** cycle-basis degree vector; Lemma 7.2 gives a Hölder estimate on the finite-cell fundamental domain through the effective-resistance metric; Theorem 7.3 then gives the same fixed-degree stable-equilibrium approximation on the deterministic graph sequence. The argument is said to follow §§5–6 and uses the finite cycle basis/cut-point construction.
- **End matter (physical pp. 32–33).** References, author contributions, funding, data availability, conflict declaration, and publisher note were read.

## Transfer boundary

The results concern deterministic nearest-neighbor graphs approximating SG and, conditionally, deterministic p.c.f. graph approximations with the stated harmonic-structure and cycle-basis assumptions. The paper has no random graph law, high-probability claim, or random-graph limit theorem. Its usable method contribution is broader than a boundary-only caveat: harmonic extension, renormalized energy comparison, Γ-convergence, and fixed-topology minimizer arguments can inform deterministic graph-landscape analysis when the matching energy and topology hypotheses are proved. It still gives no random-graph theorem and does not resolve C118. Do not transfer its \((5/3)^n\) scaling, homotopy classification, or stable-state approximation to random graphs without proving matching energy renormalization, compactness, and topology assumptions. The paper's abstract discusses uniqueness in each continuum homotopy class; Theorem 1.5 as used here asserts existence of approximating discrete stable states, not uniqueness at finite \(n\).

## Local exact check

The script ../math/pgel_l12_b10_verify_examples.py verifies the p. 8 extension matrix exactly: each inserted value is the average of its four level-one neighbors, and the unscaled refined energy is \(E_1=(3/5)E_0\), consistent with the \((5/3)\) renormalization. This finite SymPy check does not prove the general Γ-convergence or Theorem 1.5.
