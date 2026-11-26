# Finite Neumann cell-occupancy form contract

## Source and scope

This is the independently reproduced finite part of Lemma 3.1 on physical page 6 of *A density-uniform condensate bound for dilute Bose gases* (OpenAI preprint, 27 September 2026, SHA-256 `5dceb5d5d293d6dcbc651560e65a2475219bf7ed9489ad55d9b5e49e75b1b0b0`). The source proof is used only for the local form statement below. No later path-representation, entropy, thermodynamic, or condensate step is included.

## Contract

Let \(v:\mathbb R^3\to[0,\infty)\) be bounded, radial, finite range, and not identically zero in \(L^\infty\). Let \(R\) contain its support, and let \(Q\) be a cube of side \(b\ge\max(1,2R)\). Then a constant \(c_v>0\), depending only on \(v\), exists such that for every \(y\in Q\) and \(f\in H^1(Q)\),

\[
  \int_Q\left(|\nabla f(x)|^2+v(x-y)|f(x)|^2\right)\,dx
  \ge c_v b^{-3}\int_Q|f(x)|^2\,dx. \tag{1}
\]

For a finite disjoint cube partition of a configuration-space sector, the kinetic energy plus nonnegative within-cell pair energy consequently dominates, in quadratic-form order,

\[
 c'_v b^{-3}\sum_Qn_Q\mathbf1_{\{n_Q\ge2\}}, \tag{2}
\]

for another \(c'_v>0\). The same argument permits fixed positive multipliers on kinetic and pair terms, with a changed constant. A torus cell smaller than the torus is allowed only after checking that its periodized nonnegative interaction dominates the Euclidean interaction used in (1); Dirichlet states can be extended by zero before applying the argument.

## Proof of (1)

Because \(v\ge0\) is not identically zero, choose \(\nu>0\) for which \(A=\{x:v(x)\ge\nu\}\) has positive measure. For each coordinate, select the direction from \(y\) whose available length in \(Q\) is at least \(b/2\). Radiality and \(b/2\ge R\) put the correspondingly oriented octant \(A_y\) inside \(Q\), with \(a:=|A_y|=|A|/8>0\).

Write \(f_Q=|Q|^{-1}\int_Qf\). Scale-invariant Sobolev--Poincare and Holder give

\[
\begin{aligned}
 a|f_Q|^2
 &\le 2\int_{A_y}|f|^2+2\int_{A_y}|f-f_Q|^2\\
 &\le 2\nu^{-1}\int_Qv(x-y)|f(x)|^2\,dx
       +C a^{2/3}\int_Q|\nabla f|^2\,dx. \tag{3}
\end{aligned}
\]

Poincare also gives \(\|f-f_Q\|_2^2\le Cb^2\|\nabla f\|_2^2\). From \(\|f\|_2^2\le2\|f-f_Q\|_2^2+2b^3|f_Q|^2\), insert (3), use \(b\ge1\), and absorb fixed coefficients into a finite constant \(C_v\):
\[
 \|f\|_2^2\le C_vb^3\left(\|\nabla f\|_2^2+
     \int_Qv(x-y)|f(x)|^2\,dx\right).
\]
This is (1) with \(c_v=C_v^{-1}\). Notice that this proof needs a uniform oriented positive-measure subset; radiality is the stated sufficient way to obtain one.

## Proof of (2)

Restrict the form to sectors indexed by the cube containing each coordinate and discard cross-cell interactions. These restrictions use no boundary condition across artificial cuts, hence are the Neumann-bracketed form. In a cell with \(j\ge2\) coordinates, choose \(\lfloor j/2\rfloor\) disjoint coordinate pairs. Hold all remaining variables and the second coordinate of each pair fixed, apply (1) to the first coordinate, and integrate. The pairs are disjoint, so neither a kinetic term nor a pair interaction is charged twice. Finally \(\lfloor j/2\rfloor\ge j/3\) for every integer \(j\ge2\). Sum over cells and rename \(c_v/3\) as \(c'_v\).

## Boundary checks

- A cell with \(j=1\) has no within-cell pair and must contribute zero; replacing the indicator in (2) by \(1\) for all occupied cells is false for a constant Neumann one-particle function.
- If \(v\equiv0\), the same constant function makes the left side of (1) zero while its right side is positive. Thus nontriviality of \(v\) is essential.
- If a potential is not radial, (1) is not licensed by this contract merely from nonnegativity and finite range: a new uniform-in-\(y\) positive-measure-in-cube argument is required.
