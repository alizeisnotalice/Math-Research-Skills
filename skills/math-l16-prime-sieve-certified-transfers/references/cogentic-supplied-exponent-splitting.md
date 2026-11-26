# Supplied-exponent splitting audit

Google Cogentic's deterministic factoring manuscript derives a candidate
\(\widetilde M\) intended to satisfy \(p-1\mid\widetilde M\) for every prime
factor \(p\) of \(N\), then invokes a separate splitter. Physical pp. 55--57
contain that terminal interface. The construction of \(\widetilde M\), the
preconditions of Lemma 11.1, and the claimed global complexity remain source
claims, with fixed local source SHA-256
`0ccf115516dab3cbeee15167f2dea62fcb29d03a19224cb4a9ae69a5ce402993`.
The fixed primary source is [the Google Research PDF](https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/deterministic_factoring_l34/paper.pdf).

The following finite implication requires only supplied integers. Let \(n>1\),
\(a\) be a unit modulo \(n\), \(E\ge1\), and let \(q\) be a supplied prime
divisor of \(E\). If

\[
  a^E\equiv1\pmod n,
  \qquad
  d=\gcd(a^{E/q}-1,n),
\]

then \(1<d<n\) certifies a proper divisor of \(n\). This is direct from the
definition of gcd. The test is exact for arbitrary composite \(n\), including
prime powers. It does not establish \(p-1\mid E\) for every prime factor, find
\(E\), find \(q\), bound search time, or guarantee that any selected base
splits \(n\).

Run `scripts/audit_supplied_exponent_split.py n base E q ...`. It checks that
each supplied \(q\) is prime and divides \(E\), then reports every gcd. A
nontrivial reported gcd is a verified factor. A reported `null` factor is an
inconclusive outcome for that \((a,E,q)\), not a primality conclusion.

For the source-local terminal exponent interface, also read
`cogentic-finite-arithmetic.md`. The two components deliberately keep the
certificate of a supplied exponent separate from the source's unverified
procedure for constructing a globally sufficient exponent.
