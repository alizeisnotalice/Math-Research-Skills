# holroyd03 — Sharp metastability threshold for two-dimensional bootstrap percolation

**Reading status:** `fulltext_read`; complete 40-page article read (PDF pp. 1–40). Theorem statements, rate-function formulas, and the upper-bound hierarchy exponent were visually checked from rendered pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Alexander E. Holroyd, “Sharp Metastability Threshold for Two-Dimensional Bootstrap Percolation,” *Probability Theory and Related Fields* 125 (2003), 195–224, DOI [10.1007/s00440-002-0239-x](https://doi.org/10.1007/s00440-002-0239-x), arXiv [math/0206132](https://arxiv.org/abs/math/0206132). Local PDF SHA-256: `3670dee8d74bd8cdcd8f1ed0094f3260c3445320cabab7980bf4d4e0a84f2767`.

## Model and exact threshold

Take iid initially occupied sites of density $p$ in the square $[L]^2\subset\mathbb Z^2$. At each discrete update, an unoccupied site becomes occupied if at least two of its four nearest neighbours are occupied. The square is **internally spanned** when the closure of its initially occupied sites under this rule is all of $[L]^2$.

Theorem 1 (PDF p. 2) identifies the sharp constant. Section 2 defines

\[
f(z)=-\log(1-e^{-z}),\qquad
\beta(u)=\frac{u+\sqrt{u(4-3u)}}2,\qquad
 g(z)=-\log\beta(1-e^{-z}),
\]

and Proposition 5(ii) (PDF pp. 8–9) proves

\[
\lambda=\int_0^\infty g(z)\,dz=\frac{\pi^2}{18}.
\]

For sequences $L_n\to\infty$ and $p_n\to0$, internal spanning has probability tending to 1 when $\liminf p_n\log L_n>\lambda$, and to 0 when $\limsup p_n\log L_n<\lambda$. This is a strict-side threshold asymptotic, not a statement at the critical window. Theorem 3 (PDF p. 3) gives the corresponding strict-side threshold for the event that the origin is occupied by time $t_n$, with $p_n\log t_n$ compared to the same constant. The modified two-neighbour rule requiring at least one occupied neighbour in each opposite coordinate pair has constant $\lambda'=\pi^2/6$ (Theorem 4, PDF p. 3); its proof is omitted as almost identical.

## Main proof ingredients

For the supercritical bound on internal spanning, a large occupied corner seed grows unless there are adjacent pairs of empty rows or columns. A probability estimate for these obstructions and FKG for the increasing growth events yield the lower bound on spanning probability.

For the subcritical bound, use rectangles and define traversability by whether the rectangle can be internally spanned after adding the specified border. The disjoint occurrence/BK bound controls the probability that two smaller rectangles jointly span a larger one. A hierarchy records nested or splitting rectangle growth. A variational weight $W$ for scale changes is a path integral involving $g$ and is minimized by diagonal growth because $g$ is convex. A “pod” seed controls the initial perimeter cost. The hierarchy bound (43), PDF p. 37, is $P_p(\mathcal H\text{ occurs})\le Q_2^M\exp[-2(1-2c)q^{-1}\int_A^B g(z)\,dz]$, where $q=-\log(1-p)$. Its exponential coefficient tends to $2\lambda/q\sim2\lambda/p$ when the auxiliary limits $c\downarrow0$, $A\downarrow0$, $B\to\infty$, and then $p\downarrow0$ are taken in the paper’s required order. The paper chooses the auxiliary scales $B,A,Z,T$ before the final $p\downarrow0$ limit; this makes the hierarchy-counting error negligible and yields the required upper probability bound. The displayed exponent (43), PDF p. 37, was visually checked in the rendered page.

**Visual checks:** rendered PDF p. 2 for Theorem 1, p. 8 for the exact definitions of $f,\beta,g$, p. 9 for Proposition 5’s integral, and PDF p. 37 for the hierarchy upper-bound exponent. A local Simpson calculation after $z=t^2$, with 200,000 panels on $[0,8]$, gave $0.548311355370$ versus $\pi^2/18=0.548311355616$ (absolute difference $2.46\times10^{-10}$); this is only a numerical consistency check, not a proof.

## Transfer limits

This is nearest-neighbour 2D deterministic two-neighbour bootstrap with iid initial density. It does not prove an infection-time tail for arbitrary update families, dimensions, random hosts, or strategic path games. Internal spanning of a finite square, origin infection by time $t$, and a global critical probability are distinct events; preserve the paper’s finite-volume/time formulation when using it. The threshold constant is not a substitute for controlling a possible interval between $q_c$ and an auxiliary exponential-decay threshold in another model.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/holroyd03`).
