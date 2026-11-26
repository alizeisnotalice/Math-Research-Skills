# Bel's p-adic Hurwitz--Padé dimension bound

Source: Pierre Bel, *Fonction Zêta de Hurwitz p-adique et irrationalité*,
arXiv:0705.1430v1 (10 May 2007), local source SHA-256
`d993101ce5a7a4636193d62c4c3cfd800d7e1474058bea64d0788968ac12ed0a`,
physical pp. 2--23.  The local PDF's text encoding is damaged; its page count
and checksum were checked locally, and the matching arXiv HTML was used to read
the statements and proof.  The source has no later arXiv version.

For a prime `p`, an integer `e >= 2`, `v=lcm(e,p-1)`, a primitive `e`-th root
`xi`, a primitive `v`-th root `chi`, `x=a/b in Q` with `|x|_p >= p`, and an
integer `A >= 2`, the source defines its exact twisted p-adic Hurwitz values
`tilde T_p(s,x)` for `1 <= s <= A`.  Its Theorem 1 asserts that their span with
`1` over `Q(chi)` has dimension at least

\[
 \frac{[\mathbb Q_p(\xi):\mathbb Q_p]}{\varphi(v)}
 \frac{A\log |x|_p}
 {\log b+\sum_{q\mid b}\log q/(q-1)+A+(A-1)\log 2}.
\]

This source-specific claim is available only with all of those inputs and the
source definitions (including the separate `p=2` boundary convention).  It does
not manufacture a generic p-adic approximation sequence.  The proof chain is:
the determinant-form linear-independence criterion (pp. 3--4), simultaneous
Lerch/Hurwitz Padé forms (pp. 5--7), denominator estimates (pp. 8--12), a
nonzero determinant (pp. 13--15), complex asymptotics (pp. 16--17), and the
p-adic transfer/valuation estimates (pp. 18--23).  Calls therefore must retain
the all-index determinant and asymptotic hypotheses; sampled p-adic values are
not a replacement.

Theorem 2 is an asymptotic corollary for large primes and a particular pair of
Hurwitz values.  It does not provide a usable numerical threshold until the
source's explicit `M_A` construction has been instantiated and checked.
