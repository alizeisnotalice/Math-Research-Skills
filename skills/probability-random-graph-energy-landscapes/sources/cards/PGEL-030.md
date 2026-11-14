> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-030 — exact robust phase-cohesion threshold for the complete Kuramoto model

## Identity and reading evidence

- **Mother mirror status:** R02 final helper-stage passed; mother hash binding pending; no quota increment.
- **Read file:** `../pdfs/PGEL-030.pdf`
- **Exact local version:** arXiv:1011.3878v2, 5 May 2011; 27 physical pages; SHA-256 `19892042e73f9b60912f4d47c1e131c2fc0f5091cb29160f0f3d3b169fee9081`.
- **Metadata:** The local title page, D02 identity record, and official arXiv v2 record agree on title, authors and version. The arXiv record gives published DOI 10.1137/10081530X; this read is the author-version PDF, not a separately downloaded publisher copy.
- **Reading status:** Complete physical PDF pp. 1–27, including Sections 1–6 and all references. The theorem and proof pages listed in the coverage file were checked against rendered images from this exact hash.

## Model and synchronization notions

Theorem 4.1 concerns the finite, all-to-all, first-order model on the phase torus, with $n\ge2$, $K>0$, and arbitrary real natural frequencies:
\[
\dot\theta_i=\omega_i-\frac K n\sum_{j=1}^n\sin(\theta_i-\theta_j).
\]
Equivalently the interaction term is $+(K/n)\sum_j\sin(\theta_j-\theta_i)$. This is a complete positive graph with uniform coupling. It is not a random-graph theorem.

The paper distinguishes: phase cohesiveness (all pairwise geodesic distances remain inside an arc of length $\gamma<\pi$); frequency synchronization (all $\dot\theta_i$ converge to one frequency); exponential synchronization (both); and phase synchronization (all phases converge to one angle, modulo rotation). The open set $\Delta(\gamma)$ uses an arc interior; $\overline\Delta(\gamma)$ is its closed version. Do not conflate a positive order parameter with exact phase synchronization.

## Theorem 4.1 — exact universal threshold and quantitative bounds

**Statement (physical pp. 10–11; proof pp. 11–15).** Let $\omega_{\max}=\max_i\omega_i$, $\omega_{\min}=\min_i\omega_i$, and $K_{\rm critical}=\omega_{\max}-\omega_{\min}$. The following are equivalent:

1. $K>K_{\rm critical}$.
2. There is $\gamma_{\max}\in(\pi/2,\pi]$ such that for **all frequency vectors with entries in** $[\omega_{\min},\omega_{\max}]$ and all initial phases in $\Delta(\gamma_{\max})$, the model synchronizes exponentially.
3. There is $\gamma_{\min}\in[0,\pi/2)$ such that for every such frequency vector there is a locally exponentially stable synchronized trajectory in $\overline\Delta(\gamma_{\min})$.

When these conditions hold, $\gamma_{\min}$ and $\gamma_{\max}$ are uniquely specified by
\[
\sin\gamma_{\min}=\sin\gamma_{\max}=K_{\rm critical}/K.
\]
For every $\gamma\in[\gamma_{\min},\gamma_{\max}]$, $\overline\Delta(\gamma)$ is positively invariant, and trajectories initialized in $\Delta(\gamma_{\max})$ approach $\overline\Delta(\gamma_{\min})$. If $r_\infty$ is the limiting magnitude of the complex order parameter, then
\[
1\ge r_\infty\ge\cos(\gamma_{\min}/2)
=\sqrt{\frac{1+\sqrt{1-(K_{\rm critical}/K)^2}}{2}}.
\]
Once phase differences lie in $\overline\Delta(\gamma)$ for a fixed $\gamma<\pi/2$, the frequency-disagreement rate is at least $\lambda_{\rm fs}=K\cos\gamma$.

**Quantifier boundary.** The necessary-and-sufficient statement is for a universal guarantee over all frequency assignments in the interval and all initial phases in the specified arc. For a particular frequency vector, the paper explicitly says this width-based guarantee can be conservative; its exact threshold is characterized implicitly by equations (3.5)–(3.6), not always by the frequency width.

## Proof chain and reusable inequalities

1. Put $V(\theta)=\max_{i,j}|\theta_i-\theta_j|$ (geodesic distance), and choose boundary indices $m,\ell$ attaining the counterclockwise maximum and minimum. The upper Dini derivative is
   \[
   D^+V=\omega_m-\omega_\ell-\frac K n\sum_i\{\sin(\theta_m-\theta_i)+\sin(\theta_i-\theta_\ell)\}.
   \]
2. At $V=\gamma\le\pi$, the trigonometric identity $\sin x+\sin y=2\sin((x+y)/2)\cos((x-y)/2)$ and the fact that all phases lie in the arc give $D^+V\le \omega_{\max}-\omega_{\min}-K\sin\gamma$. Thus the arc is invariant when $K\sin\gamma\ge K_{\rm critical}$; strict inequality gives decrease in the interior of the interval $[\gamma_{\min},\gamma_{\max}]$.
3. Differentiate the ODE. The frequency vector obeys a time-varying consensus equation $\frac d{dt}\dot\theta=-L(t)\dot\theta$ with symmetric complete-graph weights $a_{ij}(t)=(K/n)\cos(\theta_i-\theta_j)$. After entering an arc $\gamma<\pi/2$, all weights are positive and the algebraic connectivity is bounded below by $K\cos\gamma$; consensus on the disagreement subspace yields the stated exponential frequency rate.
4. Necessity is shown by a bipolar frequency assignment and two phase clusters at $\pm\gamma/2$. Direct substitution gives $D^+V=\omega_{\max}-\omega_{\min}-K\sin\gamma$. If $K\le K_{\rm critical}$, the arc length can increase; at equality the locked state has a zero eigenvalue with a Jordan block, so the strict exponential claim fails.
5. The order-parameter estimate follows from the paper’s geometric Lemma 2.1: if phases lie in an arc of length $\gamma$, then $r\ge\cos(\gamma/2)$. The paper separately treats equal natural frequencies and obtains phase synchronization rate $K\,\mathrm{sinc}(\gamma)$, where $\mathrm{sinc}(\gamma)=\sin\gamma/\gamma$ with value 1 at zero.

The Dini-derivative calculation is a sharp, source-proved finite-dimensional argument. It should not be recast as a signed-edge or arbitrary-graph energy landscape certificate.

## Further full-text results retained with scope

- **Time-varying frequencies, §4.2, physical pp. 16–17.** Piecewise-constant frequency switching preserves phase cohesion under the stated common-interval hypotheses. For smooth time-varying frequencies, the paper assumes bounded frequencies and sufficiently small *relative acceleration* $\|\ddot\omega-\ddot\omega_{\rm avg}\mathbf1\|_\infty$; the result is tracking of a Laplacian-pseudoinverse forced disagreement, not generally exact frequency consensus. These are not arbitrary-noise results.
- **Theorem 5.1, physical pp. 18–20.** A parameterized family of forced gradient-like / dissipative-Hamiltonian systems has the same equilibria $\nabla H=F$ and the same Jacobian inertia, determined by $-\nabla^2H$, for every $\lambda\in[0,1]$ and positive-definite damping/inertia matrices. The proof uses nonsingularity of a block transformation, a positive-semidefinite congruence and the main inertia theorem, then continuity at $\lambda=0$.
- **Theorem 5.3, physical pp. 21–23.** Under the source’s hyperbolicity conditions, local exponential synchronization of the mixed first-/second-order multi-rate model is equivalent to that of its first-order multi-rate and scaled Kuramoto models; local topological conjugacy is stated modulo the common-phase symmetry.
- **Theorem 5.5, physical p. 23 onward.** With $\omega_{\rm sync}=\sum_i\omega_i/\sum_iD_i$ and $\bar\omega_i=\omega_i-D_i\omega_{\rm sync}$, the universal local exponential synchronization criterion is $K>\bar\omega_{\max}-\bar\omega_{\min}$ for all positive inertias/dampings and all allowed scaled frequencies. Almost-global phase synchronization is equivalent to $\omega_i/D_i$ being constant across $i$. The theorem does not say inertia has no transient effect; the paper explicitly leaves convergence rates, basins and separatrices dependent on inertia.

## Transfer limits and numerical evidence

- Theorem 4.1 is an all-to-all positive complete-graph result with heterogeneous frequencies, not a random signed graph result and not a claim that every local minimum is synchronous.
- Its robust width threshold should not be substituted for the exact threshold of one fixed frequency vector without checking the hypotheses and the implicit characterization.
- The paper’s statistical comparisons and simulations in §4.1 are numerical/empirical. They do not prove a random-graph high-probability bound.
- The MATLAB calculations saved in `../math/pgel_l10_b9_verification_results.txt` evaluate the bipolar two-cluster Dini formula for three finite parameter choices. They corroborate the algebra at those points only; Theorem 4.1 remains established by its source proof, not by these computations.
