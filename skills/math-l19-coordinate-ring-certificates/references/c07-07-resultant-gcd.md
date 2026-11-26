# Resultant gcd screen for a linear factor and polynomial

Source: Chen--Choi--Houle, *Schäffer's conjecture for even \(k\le42\)*, arXiv:2610.28768v1, SHA-256 `27a3e134b2297f0cc085403c18835fd97f84274c502d82e3c9a326272887013f`, 23 pages, local p. 3, Lemma 2.1.  This is a preprint, so only its elementary resultant proof step is distilled.

For \(f(x)=\alpha x+\beta\) and nonconstant \(g\in\mathbb Z[x]\), with nonzero \(\delta=|\operatorname{Res}(f,g,x)|\), every integer \(x_0\) obeys
\[
 \gcd(f(x_0),g(x_0))\mid\delta.
\]
If a prime \(p\) satisfies \(p\Vert\delta\), \(p\nmid\alpha\), \(p\mid\alpha^{d-1}g'(-\beta/\alpha)\), and divides that gcd, the stated strengthened conclusion is \(p\Vert g(x_0)\).  The checker verifies these finite integer assertions only; a resultant table does not produce the source's coupled generalized-Fermat descent, modular-method computation, or its range of \(k\).
