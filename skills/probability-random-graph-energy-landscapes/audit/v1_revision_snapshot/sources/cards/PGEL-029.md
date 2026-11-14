> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-029 — The Kuramoto model on oriented and signed graphs

## Identity and reading record
Robin Delabays, Philippe Jacquod, and Florian Dörfler, “The Kuramoto model on oriented and signed graphs,” read local arXiv:1807.11410v2 (22 January 2019); published as *SIAM Journal on Applied Dynamical Systems* 18(1):458–480 (2019), DOI [10.1137/18M1203055](https://doi.org/10.1137/18M1203055). [Official arXiv record](https://arxiv.org/abs/1807.11410); [SIAM publication page](https://epubs.siam.org/doi/abs/10.1137/18M1203055). The exact local 20-page arXiv v2 PDF, SHA-256 `1df63bb7365423ec4d2cea7de6609536960c619b3d4e4d388cd984bf49d96049`, was read in physical-page order through Appendix A and references. Publisher full text was not read, and no journal-version assertion is made. The canonical full-read index had no exact title/hash match before this read. R05 helper stage passed; mother-hash binding is pending (R05 metadata_verified=false). R05/R08 both retain the signed-cycle counterexample boundaries; this source is full-text read but excluded from the strong tool quota.
## Typed model boundary

The state is (\theta\in\mathbb T^n), and the flow is

\[
\dot\theta_i=\omega_i-\sum_j a_{ij}\sin(\theta_i-\theta_j).
\]

The graph is finite, directed, weighted, real-valued/signed, has no self-loops, and is **oriented**: $a_{ij}\ne0\Rightarrow a_{ji}=0$. The paper calls $i$ the parent/source and (j) its child/target; by its indexing convention, oscillator $i$'s dynamics depend on its children. “Synchronization” means frequency synchronization (all frequencies agree and angle differences are constant), not necessarily equal angles (physical p. 5). This is a nonsymmetric directed model and in general has no symmetric scalar gradient energy or Hessian certificate. The oriented-cycle Lyapunov function below is a special dynamical argument, not evidence of a global gradient structure.

## Acyclic result

For a vertex (j), let $d_j^{out}=\sum_k|a_{jk}|$. Sort its outgoing magnitudes $|a_{j1}|\ge\cdots\ge|a_{jn_j}|$, and define the residual outgoing weight

\[
\rho_j=\max\left(0, |a_{j1}|-\sum_{k=2}^{n_j}|a_{jk}|\right).
\]

The local order parameter $r_je^{i\psi_j}=\sum_k a_{jk}e^{i\theta_k}$ always has amplitude $r_j\in[\rho_j,d_j^{out}]$, with both endpoints attainable (Proposition 1.2, physical pp. 3–4). A necessary condition for a synchronous state on a graph with leaders is that all leaders share a natural frequency $\omega_L$ and $|\omega_i-\omega_L|\le d_i^{out}$ for each vertex (Proposition 1.4, physical p. 5).

**Theorem 2.2 (physical p. 6).** For a finite oriented acyclic weighted signed graph, rotate to the common leader frequency so leaders have $\omega_i=0$. If, for every vertex $i$, $|\omega_i|<\rho_i$ whenever $\rho_i>0$, and $\omega_i=0$ whenever $\rho_i=0$, then the system synchronizes exponentially from almost all initial conditions. It is an almost-global sufficient theorem, not convergence from every initial state and not a necessary criterion in arbitrary acyclic graphs. The stronger necessary bound in Proposition 1.4 uses $d_i^{out}$, not $\rho_i$.

Proof route (physical pp. 6–8): topologically order the DAG so the Jacobian is triangular; recursively treat each oscillator as a scalar nonautonomous equation driven by children already converging exponentially. The local order magnitude is bounded below by ρ_i, so the strict frequency inequality leaves a stable branch with a uniform asymptotic margin. The alternative scalar branch has a positive Jacobian direction and a lower-dimensional stable manifold. The proof invokes asymptotically autonomous semiflow results summarized in Appendix A (physical pp. 17–18; imported from [30]); this is the dependency behind the almost-all-initial-conditions statement. Corollary 2.4 (physical p. 8) specializes to at most one outgoing edge per vertex, where ρ_i=d_i^{out}=|a_{ij}|.

## Oriented cycle result

For one directed cycle with nonzero real edge weights $a_{i,i+1}$ and identical natural frequencies, Theorem 3.1 (physical pp. 10–11) proves every trajectory converges to a frequency-synchronous state. Its Lyapunov function is $V=2\sum_i a_{i,i+1}[1-\cos(\theta_i-\theta_{i+1})]$, and the paper derives

\[
\dot V=-\sum_i(\dot\theta_{i-1}-\dot\theta_i)^2\le0.
\]

Compactness of $\mathbb T^n$ and LaSalle’s invariance principle give convergence to the synchronous set. The common frequency may be nonzero and the angles need not coincide.

The frequency bounds and stable-state classification are separate:

* Proposition 3.2 (physical p. 11): $\omega_s\in[-a_{\min},a_{\min}]$, where $a_{\min}=\min_i|a_{i,i+1}|$.
* **Lemma 3.4 (physical p. 12) is a source-claimed iff, quarantined on the signed model.** The read v2 states that local exponential stability holds iff $a_{i,i+1}\cos(\theta_i^*-\theta_{i+1}^*)>0$ for every edge, and then gives the branch $\Delta_{i,i+1}^{\omega_s}=-\arcsin(\omega_s/a_{i,i+1})$ when $a_{i,i+1}>0$ and $\pi+\arcsin(\omega_s/a_{i,i+1})$ when $a_{i,i+1}<0$ (Eq. (46)). A legal signed-cycle witness below disproves necessity in this general signed scope. The all-positive edge-coefficient branch remains a source-reported sufficient case; do not use the iff or treat Eq. (46) as an exhaustive stable-state classification. Do not infer stability or instability from a zero cosine here without checking the actual nonlinear Jacobian.
* **Proposition 3.6 (physical p. 13) is an exhaustive-count claim, also quarantined for arbitrary signed weights.** With $n_-$ negative edge weights and $\sigma=(2\pi)^{-1}\sum_i\arcsin(a_{\min}/|a_{i,i+1}|)$, the source claims stable frequencies are indexed by integers $q\in(n_-/2-\sigma,n_-/2+\sigma)$. For each such $q$, its claimed equation is

\[
\sum_i\arcsin(\omega_s/|a_{i,i+1}|)=(n_- -2q)\pi.
\]

The source proof uses the winding constraint, the strict branch from Lemma 3.4, monotonicity of the left side, and exclusion of $\omega_s=\pm a_{\min}$. The following exact signed example shows that this branch-based interval is not exhaustive as stated. It does not disprove the separate assertion that some fixed signed cycle has only finitely many stable frequencies. The frequency count is not a count of all equilibria; unstable synchronous states can form a continuum (Remark 3.3, physical p. 12).

### Exact signed-cycle witness and source boundary

For the oriented 3-cycle with weights $(a_{12},a_{23},a_{31})=(-1/10,1,1)$, identical natural frequencies $\omega_i=0$, and $\theta=(0,0,0)$, the state is an exact synchronous equilibrium with $\omega_s=0$ and edge differences zero. In the paper's child-direction convention, its Jacobian is

\[
J=\begin{pmatrix}1/10&-1/10&0\\0&-1&1\\1&0&-1\end{pmatrix},\qquad
\det(\lambda I-J)=\lambda(\lambda^2+19\lambda/10+4/5).
\]

The common-rotation eigenvalue is simple. In difference coordinates $(x,y)=(\theta_1-\theta_2,\theta_2-\theta_3)$, the linearization is $\begin{psmallmatrix}1/10&1\\-1&-2\end{psmallmatrix}$ with trace $-19/10$, determinant $4/5$, and eigenvalues $(-19\pm\sqrt{41})/20<0$. Thus the equilibrium is locally exponentially stable modulo common rotation by the ordinary hyperbolic-equilibrium linearization theorem. Yet the edge coefficients $a_i\cos\Delta_i=(-1/10,1,1)$ are not all positive. This is a model-matching exact counterexample to the necessity direction of the read-v2 Lemma 3.4; it is not a numerical simulation and does not concern a journal version.

For the same cycle, $a_{\min}=1/10$, $n_-=1$, and $\sigma=1/4+\arcsin(1/10)/\pi$. Since $0<\arcsin(1/10)<\pi/4$, the stated open interval is

\[
\left(\frac14-\frac{\arcsin(1/10)}\pi,\;\frac34+\frac{\arcsin(1/10)}\pi\right)\subset(0,1),
\]

so it contains no integer, although the locally exponentially stable state at frequency $\omega_s=0$ exists (with winding $q=0$); Eq. (53) would require $0=\pi$ for this state. Therefore the printed exhaustive interval/count and Eq. (53) cannot be used as a stable-frequency classification for all signed weights in the read v2. The proof's dependence on the restricted branch of Lemma 3.4 pinpoints the gap. This local witness does not establish that the source's separate finiteness assertion is false.
Section 3.4’s correlation between initial and final winding numbers and its Gaussian/variance observations are **simulation findings** (physical pp. 13–14), not theorem statements. Section 4 (physical pp. 15–17) gives additional model-specific compositions: one large leading cycle and multiple short leading cycles admit almost-global extensions under stated conditions, whereas examples with multiple large cycles show initial-condition dependence. Do not extrapolate the DAG or single-cycle theorem to arbitrary oriented graphs.

## Transfer limits

This source is useful as a **typed nonpotential boundary**: it distinguishes directed signed dynamics from positive symmetric graph-energy landscape results. Keep the model oriented/signed and retain its frequency-synchronization definition. Do not use its cycle Lyapunov function as a general potential, or its DAG/single-cycle conditions as a theorem for general digraphs. A local numerical identity check for Eq. (39) and an exact uniform-positive 4-cycle frequency-count check are saved in `../math/exact_checks.py`; they are checks of examples/formulas, not substitutes for the proofs.

Coverage: all physical pages 1–20 were read, including Appendix A and references. Rendered formula pages and coverage are recorded in the batch `../reading_coverage.json` (mother entry; rendered images remain under `../renders/PGEL-029/`). Review is pending.
