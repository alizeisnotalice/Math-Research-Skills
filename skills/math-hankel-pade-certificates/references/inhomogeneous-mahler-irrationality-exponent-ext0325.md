# Inhomogeneous Mahler irrationality-exponent transfer

Source checked: Andrew Rajchert, *On the Irrationality Exponents of Mahler Numbers*, arXiv:2411.10733v1 (2024), Lemma 3.12 and Theorem 3.13 (physical pp. 22--26). This is a B.Sc. thesis/preprint, not a replacement for an independently established continued-fraction or orbit calculation.

## Certified caller contract

This conditional result applies only after the caller has proved all of the following.

- A non-rational $f\in\mathbb Q((z^{-1}))$ converges at the selected integer $b$, with $|b|\ge2$, and satisfies
  \[
  f(z)=A(z)f(z^d)+C(z)/B(z),\qquad d\ge2,
  \]
  for the source's polynomial hypotheses.
- The full forward orbit has no pole or zero obstruction: $A(b^{d^t})B(b^{d^t})\ne0$ for every $t\ge0$.
- A proved Laurent-continued-fraction analysis supplies the denominator degrees $d_k=\deg q_k$ and the two approximation sequences used in Lemma 3.12. In particular, the growth, error, and interlacing estimates required there are proved, rather than guessed from a finite convergent table.

Under that contract, the source proves
\[
 \mu(f(b))=1+\limsup_{k\to\infty}\frac{d_{k+1}}{d_k}.
\]

## Audit boundary

The proof of the upper bound uses Lemma 3.12 (two controlled rational-approximation sequences) and verifies its three growth/error hypotheses in physical pp. 24--26. It does **not** make denominator degrees or gcd degrees computable from a finite prefix. In the inhomogeneous case, the source notes that the relevant gcd-degree behavior is only known case by case (p. 43), and its conclusion explicitly leaves general gap detection and rationality questions open (pp. 61--62). Therefore a finite Padé/Hankel computation remains only a finite certificate.
