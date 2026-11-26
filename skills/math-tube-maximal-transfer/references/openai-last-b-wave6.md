# fixed-phase curved-Kakeya straightening

**Source.** *Every Four-dimensional Kakeya Set Has Full Hausdorff Dimension*,
pp. 3, 20, 168, 170–171, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf).

**Input.** On one fixed chart \(U\times Y\), provide a smooth phase
\(\varphi(x,t;y)=x\cdot y+\psi(t;y)\), mixed-rank condition, nonzero
\(\det\nabla_y^2\partial_t\psi\), and the invariant Bourgain condition with
one common scalar. For each \(y\) supply an anchor \((\omega_y,0)\) whose full
local core is contained in \(E\).

**Procedure.** Invoke the stated phase theorem to obtain a single smooth
coordinate change
\[
\kappa(u,s)=(u+B(\alpha(s)),\alpha(s)),\quad
\varphi\circ\kappa=u\cdot y+sh(y)+q(y)+f(s),
\]
on a smaller interval/direction ball, with \(\det\nabla^2h\ne0\). Gradient
equality turns each retained core into the straight segment
\[
u=(\omega_y-B(0))-s\nabla h(y).
\]
The direction map \(y\mapsto(-\nabla h(y),1)/\sqrt{1+|\nabla h(y)|^2}\)
is locally diffeomorphic, hence covers an open direction patch.

**Output.** The transformed set contains positive-length straight segments in
an open patch of four-dimensional directions; the source's Euclidean Kakeya
theorem then gives full Hausdorff dimension.

**Boundary.** One fixed phase and its localized hypotheses are required. This
does not handle variable phases, off-chart curve portions, or certify the
mixed-rank/curvature/Bourgain identities.

## 固定来源

- 物理页 3, 20, 168, 170, 171。Theorem 1.1; Theorem 2.17; Proposition 10.1; Corollary 11.3 SHA-256 `30d0c186aa9c697d02ab9bf736968028f1ce8a2f164f1d7291398d530035ccde`。[Every four-dimensional Kakeya set has full Hausdorff dimension](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf)
