# FRIEDGUT2004 — influential tribes conjectures

**Source.** Ehud Friedgut, “Influences in Product Spaces: KKL and BKKKL Revisited,” *Combinatorics, Probability and Computing* 13 (2004), 17–29, DOI 10.1017/S0963548303005832. Cambridge metadata and an author-uploaded copy were checked; the exact conjecture below was read in the full-text view. Selected sections only, so status is partial.

## Two distinct conjectures

**Conjecture 2.2 (continuous cube).** For monotone Boolean \(f:[0,1]^n\to\{0,1\}\), there is a coalition of \(o(n)\) coordinates which can be fixed so that \(f\) is forced to one of its two values with probability \(1-o(1)\). This is the conjecture addressed by the 2026 continuous-cube papers; their bounds are not the discrete \(O(\log n)\) statement below.

**Conjecture 2.6 (uniform Boolean cube).** For every \(c>0\) and fixed \(\epsilon>0\), there is \(b=b(c,\epsilon)>0\) such that for Boolean \(f:\{0,1\}^n\to\{0,1\}\) with \(\mathrm{Inf}_i(f)\le c\log(n)/n\) for all \(i\), a set \(J\subseteq[n]\) with \(|J|\le b\log n\) satisfies either
\[
\mathbb E[f\mid X_J=0^J]\le\epsilon
\quad\text{or}\quad
\mathbb E[f\mid X_J=1^J]\ge1-\epsilon.
\]
The source calls this a conjecture. In §1 Friedgut says the paper restricts to monotone functions but claims that KKL shifting causes no loss for its purposes; Conjecture 2.6's displayed line does not repeat monotonicity. Keep this standing context visible. A nonmonotone version where the coalition chooses an arbitrary favorable assignment is a separate formulation; do not assume equivalence without proving the reduction. Do not replace this with the looser Simons-compilation display, where the premise contains (\epsilon) but the conclusion uses unparameterized (o(1)).

The paper's theorem on \(p\)-biased product spaces (Theorem 1.4) is a different coalition-influence result. It cannot be used as a proof of Conjecture 2.6 without an additional argument converting coalition influence into the stated conditional-bias forcing conclusion.

**Read:** conjectures 2.2 and 2.6, nearby discussion, and Theorem 1.4 (author-uploaded full text); whole paper not read.
