# Low-density zero rectangles: a finite witness route

## Source and exact adopted locus

*Breaking the Square-Root Barrier for the Log-Rank Conjecture*, Cogentic
Research Papers, Google Research repository commit
`4a7bc8ab0bc770e71a259b7966c500496b99010a`; local PDF SHA-256
`9c941a918c5e5cea1624adee676c010efb85b60b3cd77455640cd578f54f6bc9`.

The adopted source statement is Lemma 3.2(1), physical pp. 12--13.  It is
separate from Appendix Proposition A.3's rank-halving step: it produces a
large **zero** rectangle from low density under a product distribution.

Let \(\pi=\pi_X\times\pi_Y\) have full support and let
\(M\in\{0,1\}^{X\times Y}\) have real rank at most \(r_0\ge1\).  With
\(p=\mathbb E_\pi M\in[0,1/2]\), Lemma 3.2(1) states that some
zero-monochromatic \(A\times B\) obeys
\[
  \pi(A\times B)\ge \frac9{16}\exp(-240\sqrt{r_0p}). \tag{LDR}
\]

## Checked depended proof route

The adopted preprint proof was read at the cited pages.  It restricts to
successive product-conditioned supports, uses a normalized SVD and a
high-leverage trim, then applies Gaussian hyperplane rounding to make the
one-density at least halve while retaining product mass at least
\(\exp(-70s_j)\).  Once the relevant SVD size is at most \(1/4\), a
unit-norm cutoff gives a zero rectangle of conditional mass at least
\(9/16\).  Summing the geometric losses gives the constant 240 in (LDR).

## Finite-use interface

For a small finite instance, run
`scripts/cogentic_zero_rectangle_search.py`.  It enumerates all nonempty
row/column subset pairs, checks zero-monochromaticity, and reports a maximum
product-measure zero rectangle using exact rational arithmetic.  It also
reports the exact real rank and source threshold in symbolic form.

This helper is deliberately not a proof of (LDR): a finite exhaustive search
can confirm a witness in its input but cannot establish the lemma for every
finite matrix, and it does not reproduce the source's Gaussian rounding.
Nor should the displayed exponential threshold be compared with a floating
point approximation.  A claim that a witness meets (LDR) needs an independent
directed/analytic exponential comparison.

## Boundary

The lemma requires a full-support product measure, Boolean entries, a real
rank bound, and \(p\le1/2\).  It says nothing about arbitrary signs or
non-product measures.  It can feed a rectangle-selection stage; only after a
specific monochromatic rectangle is supplied should the existing exact
rank-halving / protocol-tree certificates be invoked.

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/logrank_conjecture/paper.pdf)。
