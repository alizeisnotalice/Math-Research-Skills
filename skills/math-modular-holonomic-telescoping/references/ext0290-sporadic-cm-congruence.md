# Sporadic recurrence congruence through a supplied CM coefficient

Kazalicki proves that the integer sequence
\[
 F(n)=\sum_{k=0}^n(-1)^k8^{n-k}\binom nk
 \sum_{j=0}^k\binom kj^3
\]
satisfies \(F((p-1)/2)\equiv\gamma(p)\pmod p\) for primes \(p>2\).  The
published statement also gives a CM description. The checker implements that
description for primes \(p>3\) outside the residue classes
\(5,11\pmod {24}\).  If
\(p=a^2+6b^2\), it uses \(\gamma(p)=2(a^2-6b^2)\).  In the remaining
covered classes the coefficient is zero.

Use the checker only for an individual prime in its stated branch.  Its exact
integer computation verifies the recurrence-side value and the supplied CM
coefficient.  The result does not establish the modular-form identification,
the Atkin--Swinnerton--Dyer congruence, or the \(\ell\)-adic comparison that
proves the theorem.

The local source is arXiv:1901.03098v1, physical pp. 1--6.  The published
version is M. Kazalicki, *Research in the Mathematical Sciences* 6 (2019),
Article 28, DOI 10.1007/s40687-019-0191-3.  Its stated CM formula excludes
the two residue classes that the local v1 extraction made easy to overstate.
