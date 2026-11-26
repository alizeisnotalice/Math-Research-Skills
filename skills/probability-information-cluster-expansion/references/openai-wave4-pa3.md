# Wave 4 PA3: power-mean tree insertion interface

## The Mezard--Parisi formula for diluted spin glasses

Source SHA-256 `f415bacf0f91bf5aa188cb80f95e00fac1142996fe70d3d8c5c1372b3262a8e5`, physical pp. 6--7 and 10--11, Lemmas 3.1, 3.5, and 3.6.  For positive leaf insertion `A`, backward power means satisfy
\[
Y_L=A,\qquad Y_{d-1}=(K_dY_d^{m_d})^{1/m_d},
\quad K_d^A=(Y_d/Y_{d-1})^{m_d}K_d.
\]
For an internal tree vertex `\beta`, with `n_\beta` children, its updated density is
\[
W_T(A)=\prod_{a\in\mathrm{Leaves}(T)}A_a
\prod_{\beta\in\mathrm{Int}(T)}Y_\beta^{\gamma_\beta},
\qquad \gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}.
\]
Differentiation inserts either a protected leaf or an independent fresh path.  For the uniform mesh `m_d=d/L`, a prescribed `b` fresh unary split configuration has total absolute coefficient `O_{q,k}(L^{-b})`; nonregular sampled shapes have probability `O_k(\eta+L^{-1})`.

**Scope.** Scoped reference. It requires positive bounded insertion (or the source's stated analytic neighborhood), the exact iterated power-mean kernels, fixed finite depth/tree size, and the prescribed cancellation/protection convention.  It does not establish the Mezard--Parisi formula or a continuum tree expansion.

## 固定来源

- 物理页 6, 7, 10, 11。Lemma 3.1; Lemmas 3.5--3.6 SHA-256 `f415bacf0f91bf5aa188cb80f95e00fac1142996fe70d3d8c5c1372b3262a8e5`。[The Mézard–Parisi formula for diluted spin glasses](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf)
