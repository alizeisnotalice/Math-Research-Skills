# Factorial fractional-part criterion for the Euler--Mascheroni constant

## Source and verification status

- Jaroslav Hancl and Simon Kristensen, *Metrical irrationality results related to values of the Riemann zeta-function*, arXiv:1802.03946v1 (12 February 2018), PDF pp. 13--14 (Corollary 4.2); SHA-256 `6f0ff21275b0c347c0b6dc9665860b13906b12ca766a3f12587301aac70b36d9`.
- This source is a preprint. A search on 2026-11-26 located the arXiv record and later citations that still label it a preprint; no formal publication was established. The usable claim was therefore checked in the source itself, not inferred from a citation.
- Dependency actually used: the derivation on PDF pp. 7--8 reduces rationality to a fractional part tending to zero after factorial truncation; PDF pp. 12--14 records the weaker accumulation-point criterion. Its metrical Theorem 2.1 is **not** an assertion about the unperturbed value `x = 1` and is not used to conclude anything about gamma.

## Conditional criterion

With `floor(log2(n))` denoting the integer binary logarithm, define

\[
A_N=\left\{(N!)^3\sum_{n=N+1}^{(N!)^3}
 \frac{(-1)^n(n-1)!\lfloor\log_2 n\rfloor}{(N+1)(N+2)\cdots n}\right\}.
\]

Corollary 4.2 states: if `(A_N)` has an irrational accumulation point, or infinitely many accumulation points, then the Euler--Mascheroni constant `gamma` is irrational. Algebraically, the summand may be evaluated exactly as

\[
(-1)^n\lfloor\log_2n\rfloor\frac{(N!)^4}{n},
\]

but retaining the first display is useful for tracing the factorial truncation in the proof.

## Safe use

`scripts/hancl_kristensen_gamma_residue.py` evaluates finite `A_N` exactly with rational arithmetic. It verifies neither the required accumulation behaviour nor irrationality of gamma: a finite list, a floating-point plot, or residues close to a chosen value is only exploratory evidence. This is a separate conditional route from Padé, multiple-Laguerre, and Sondow fractional gates. Any claimed proof must establish the stated infinite accumulation condition for the exact sequence.
