# Hypergeometric mod-℘ Frobenius gate

Scoped reference. EXT-0265, SHA `f842393c6a7966af0985049469f1ce06bad9d7460249e2caa49133d4059484ef`, local arXiv:1911.09486v3, physical pp. 1 and 4--8. The published version was checked at *Bulletin de la Société mathématique de France* **149** (2021), 439--477, DOI `10.24033/bsmf.2834`; its official record gives the same strong-Frobenius/mod-℘ theorem.

Let
\[
 {}_nF_{n-1}(\alpha;\beta;z)=
 \sum_{j\geq0}\frac{(\alpha_1)_j\cdots(\alpha_n)_j}
 {(\beta_1)_j\cdots(\beta_{n-1})_j j!}z^j,
 \qquad \beta_n=1.
\]
If all \(\alpha_i,\beta_j\in\mathbb Q\setminus\mathbb Z_{\leq0}\), all differences \(\alpha_i-\beta_j\notin\mathbb Z\), and \(d_{\alpha,\beta}\) is the least common denominator of the parameters, then for every prime
\[
 p\nmid d_{\alpha,\beta}
 \quad\hbox{such that}\quad
 {}_nF_{n-1}(\alpha;\beta;z)\in\mathbb Z_{(p)}[[z]],
\]
the reduction modulo \(p\) is algebraic over \(\mathbb F_p(z)\), of degree at most
\[
 p^{n^2\varphi(d_{\alpha,\beta})}.
\]
This is Theorem 1.1 (local physical p. 4).  Its operational core is Theorem 2.1 (p. 8): an order-(n) operator with a strong Frobenius structure of period (h), together with a solution in \(\mathbb Z_{(p)}[[z]]\), gives degree at most \(p^{n^2h}\).  The hypergeometric specialization uses rigidity, regular singularities, rational exponents, and a prime-uniform bound for the Frobenius period; those are proof dependencies, not optional heuristics.

Before invoking this gate, calculate the rational parameters, verify every nonresonance difference and every coefficient-integrality condition for the particular prime, and identify the actual hypergeometric differential operator.  It supplies only a modular algebraicity/degree bound.  It neither supplies a representation of Euler's constant nor turns such a bound into an irrationality proof; a separately proved connection to \(\gamma\), plus integer linear forms and nonvanishing, remains required.
