> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-007 — On the Landscape of Synchronization Networks

## Identity and reading record

Shuyang Ling, Ruitu Xu, and Afonso S. Bandeira, “On the Landscape of Synchronization Networks: A Perspective from Nonconvex Optimization,” arXiv:1809.11083v2 (20 Apr 2019), SIAM Journal on Optimization 29(3), 1879–1907 (2019), DOI [10.1137/18M1217644](https://doi.org/10.1137/18M1217644); [official arXiv record](https://arxiv.org/abs/1809.11083). The local 27-page PDF matches the v2 front page and author list; SHA-256 e9545189087e353b84932d5c06dac282bf2ad576b4e55d388af83f1f53fad1bd. Reader L14 read physical pp. 1–27 in order, including all preliminaries, examples, proofs, technical examples, acknowledgment, and references. Coverage and render checks are recorded in ../reading_coverage.json. No exact-title, arXiv-ID, or hash match was found in the accepted canonical-read index. R05 helper-stage review passed; mother hash binding is pending.

## Model, stationarity, and theorem statements

The phase energy is
\[
E(\theta)=\frac12\sum_{i,j=1}^n a_{ij}\{1-\cos(\theta_i-\theta_j)\},
\]
with a simple undirected graph, symmetric nonnegative adjacency \(a_{ij}=a_{ji}\in\{0,1\}\), and no self-loops. The random model in §3 is \(G(n,p)\), with independent positive edge-presence indicators for unordered pairs. This is not a signed-edge model. For \(Q=[\cos\theta,\sin\theta]\), \((QQ^\top)_{ij}=\cos(\theta_i-\theta_j)\), and
\[
\nabla E_i=\sum_j a_{ij}\sin(\theta_i-\theta_j),\qquad
\nabla^2E=\operatorname{ddiag}(AQQ^\top)-A\circ QQ^\top\succeq0
\]
are the first- and second-order necessary conditions at a local minimum. The Hessian is a Laplacian with weights \(a_{ij}\cos(\theta_i-\theta_j)\), which may be negative away from synchrony; the constant vector is its rotational zero mode.

**Theorem 3.1 (PDF p. 10).** For an n-vertex graph whose every degree is at least \(\mu(n-1)\), if
\[
\mu\ge (3-\sqrt2)/2\approx0.792893,
\]
then the only local minimum is \(\theta=\theta_0\), unique modulo common phase translation. This is a deterministic positive-graph landscape theorem.

**Theorem 3.3 (PDF p. 10).** For \(G(n,p)\), if \(p=32\gamma n^{-1/3}\log n\), \(\gamma\ge1\) (with \(p\in[0,1]\)), then \(\theta_0\) is the only local minimum with probability at least
\[
1-4\exp\!\left(n\{\log(100n^{1/3})-2\gamma\log n\}\right)-10n^{-\gamma+1}.
\]
The theorem is finite-n and concerns independent, symmetric, nonnegative edge indicators. The authors explicitly leave \(p=\Omega(n^{-1}\log n)\) as Open Problem 3.4; that conjectured connectivity-scale regime is not the theorem.

## Proof dependency chain

- **Cone criterion, Proposition 5.1 (PDF pp. 12–13).** If the graph is connected and a local minimizer has an order-parameter direction \(\theta_r\) with \(|\sin(\theta_i-\theta_r)|<1/\sqrt2\) for all \(i\), then it is synchronous modulo rotation. The proof puts phases in two opposing quadrants and uses connectedness plus the graph-Laplacian quadratic form along the straight path to show that a nonsynchronous configuration cannot be stationary there.
- **Deterministic dense theorem, §5.1 (PDF pp. 14–15).** Second-order stationarity and rank-two \(QQ^\top\) with trace \(n\) yield
  \[
  \|Q^\top\mathbf1\|^2\ge
  \bigl(2\mu-\tfrac32\bigr)n^2+2(1-\mu)n.
  \]
  First-order stationarity gives
  \[
  \|r\|\,|\sin(\theta_i-\theta_r)|
  \le(1-\mu)(n-1),\qquad r=\sum_j e^{i\theta_j}.
  \]
  Squaring and inserting the first bound gives the source’s upper bound
  \[
  |\sin(\theta_i-\theta_r)|^2
  \le\frac{2(1-\mu)^2}{4\mu-3+4(1-\mu)/n}<\frac12
  \]
  for the stated \(\mu\); Proposition 5.1 finishes.
- **Random theorem roadmap, §5.2 (PDF pp. 15–18).** Lemma 5.3 applies matrix Bernstein to \(A-\mathbb E A\), its row norms, and centered degree errors, with failure probability \(2n^{-\gamma+1}\). Lemma 5.4 obtains the uniform local-minimum overlap bound
  \(\|Q^\top\mathbf1\|^2\ge n^2(1-3n^{-1/3})\), with the exponential failure term appearing in Theorem 3.3. The proof combines that overlap bound with centered-row bounds in the first-order equation to get \(|\sin(\theta_i-\theta_r)|<1/\sqrt2\) for every vertex, then invokes Proposition 5.1 and connectedness.
- **Uniformity mechanism, Lemma 5.6 and proof (PDF pp. 18–22).** The paper proves concentration for fixed rank-two phase matrices, covers the n-torus by an \(\epsilon\)-net, takes a union bound, and extends uniformly by a Lipschitz estimate. It controls inner products with \(QQ^\top\) and \(QQ^\top\circ QQ^\top\), which is the intended uniformity step for the second-order condition. The source’s exact diagonal bookkeeping needs a caveat before reusing this lemma quantitatively: the stated simple no-loop model has \(A_{ii}=0\), while \(X=QQ^\top\) has \(X_{ii}=1\). On physical p. 19 the source writes
  \[
  \langle A,X\circ X\rangle-p\|X\|_F^2
  =\sum_{i\ne j}(a_{ij}-p)X_{ij}^2.
  \]
  Under the no-loop convention, the left side instead equals the displayed off-diagonal sum minus \(pn\). The source also writes \(\mathbb E A=pJ_n\) in the random-graph concentration discussion, although the standard loopless adjacency has \(\mathbb E A=p(J_n-I_n)\). This is a source convention/bookkeeping ambiguity, not a counterexample to Theorem 3.3. Separately, direct algebra gives \(\langle A-p(J_n-I_n),X\circ X\rangle=\sum_{i\ne j}(a_{ij}-p)X_{ij}^2\); equivalently, adding the deterministic diagonal \(pI_n\) gives the same energy and the \(pJ_n\) centering. That reconciliation is our bookkeeping, not a correction stated by the authors; confirm it throughout the proof before reusing exact concentration identities or constants. Theorem 3.3 remains recorded as the source’s theorem statement, and its claim is not refuted by this accounting issue.
- **Counterexamples and examples, §5.3 (PDF pp. 23–24).** Trees have no spurious local minima, whereas a cycle and a k-nearest-neighbor circulant WSG graph can have a twisted local minimum. The Fourier/Hessian calculation shows the WSG twisted state for \(k\lesssim0.34n\) (degree about \(0.68n\)); the approximate 0.34 statement is an example threshold, not a universal exact cutoff.

The theorem’s “only local minimum” is a landscape statement, stronger than a local linear-stability calculation. The paper’s inference to almost-everywhere convergence uses the gradient-flow setting; do not reinterpret it as convergence from every initial condition.

## Reusable method and C118 boundary

For positive undirected graphs, reusable components are the rank-two phase-matrix encoding, second-order overlap lower bound, a first-order row-defect estimate, and a net-based uniform concentration argument. C118 has signed observations. Replacing positive Bernoulli A by signed A changes the Hessian and destroys the nonnegative edge-count and cone-sign comparisons used here. The net architecture may guide a new proof, but this paper supplies neither a signed-Hessian theorem nor the signed complete-graph probability estimate C118 needs. Do not transfer its threshold or theorem directly.
