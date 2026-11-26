# Exact finite three-strip boundary lemma

Source: *A power saving for planar halving lines* (OpenAI, 25 September
2026), pinned commit `3344da59991ed94f9ba711217b29c1d760badfa6`, PDF
pp. 23--25, Lemma 7.1.  Local PDF SHA-256:
`61d7aa1ffad4b7968e5882374ce0e542d3221cf8e7c48b51c52256e1331bb4d9`.
The source is the pinned
[PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf).

## Certified interface

Let \(P\) be finite, \(B\subset\mathbb R^2\) have \(|x|\le D\) for every
\(x\in B\), with \(D\ge1\).  Suppose equal-cardinality sets
\(M_0,\ldots,M_m\subset P\) are represented by strict cuts

\[
 M_i=\{x\in P:\nu_i\mathbin\cdot x<c_i\},\qquad
 |\nu_i|=1,\quad |\nu_i-\nu_0|\le\theta.
\]

For each step choose a bijection from \(M_{i-1}\setminus M_i\) to
\(M_i\setminus M_{i-1}\).  Let \(C_B\) count its pairs with exactly one
endpoint in \(B\), set
\(A=\bigcup_i(M_{i-1}\triangle M_i)\), \(\rho=D\theta\), and put

\[
c_-=\min_i c_i,\quad c_+=\max_i c_i,\quad
S_q=\{x:|\nu_0\mathbin\cdot x-q|\le3\rho\}
\quad(q\in\{c_0,c_-,c_+\}).
\]

Then

\[
\#((A\cap B)\setminus(S_{c_0}\cup S_{c_-}\cup S_{c_+}))\le2C_B.
\]

## Independent derivation

Write \(t(x)=\nu_0\cdot x\) and
\(e_i(x)=(\nu_i-\nu_0)\cdot x\).  On \(B\),
\(|e_i(x)|\le D|\nu_i-\nu_0|\le\rho\).

If an initially marked participant avoids all three strips, then avoidance of
the \(c_0\) strip gives \(t<c_0-3\rho\).  At a state where it is unmarked,
\(t+e_i\ge c_i\ge c_-\), hence \(t>c_--\rho\); avoiding the \(c_-\)
strip improves this to \(t>c_-+3\rho\).  At a state attaining \(c_-\), it is
therefore lost.  If this class is nonempty, \(c_0-c_->6\rho\), so every
initially unmarked point of \(B\) remains unmarked at that state.  There are
thus no gains inside \(B\) in the comparison.  Giving each point of \(M_0\)
a token and moving a token along each prescribed matching shows that these
losses are no more numerous than the transfers that cross the boundary of
\(B\), hence at most \(C_B\).

The symmetric argument starts with an initially unmarked participant.  It is
gained at a state attaining \(c_+\), and, if this class is nonempty, no
initially marked point of \(B\) is lost in that comparison.  Token
conservation again bounds this class by \(C_B\).  The two classes partition
the participants outside the strips, which proves the displayed estimate.
This proof also covers \(\theta=0\); a point that changes and later returns is
still in \(A\).

## Scope boundary

The lemma assumes the cuts and matchings; it does not construct them.  It has
no conclusion about a limiting measure, strip mass, a compatible cone of
transfers, three-foliation compactness, or a global halving-line/k-set bound.
