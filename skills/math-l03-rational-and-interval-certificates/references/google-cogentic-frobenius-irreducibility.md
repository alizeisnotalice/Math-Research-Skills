# Frobenius irreducibility certificate over a prime field

**Source.** *Discrete Logarithms in Finite Fields of Fixed Characteristic in
Sub-Quasi-Polynomial Time*, Google Cogentic research paper, local PDF SHA-256
`fba12f4d5e98152d52226887c4af2606039725f898bffecbc8a4d91ccaf9d0d7`,
36 physical pages.  The adopted finite-field procedure is Lemma 2.1(3),
physical p. 34; the input role of a monic irreducible presentation is Definition
1.1 and Theorem 1.2, pp. 2--3.

## Input, certificate, and output

For a supplied prime `p` and a supplied monic polynomial
`A(X) in F_p[X]` of degree `D>=1`, calculate in
`F_p[X]/(A)` the Frobenius residues

\[
 Y_0=X,\qquad Y_{k+1}=Y_k^p\pmod A.
\]

Accept only when `Y_D=X` and, for every proper positive divisor `k` of `D`,

\[
 \gcd(A,Y_k-X)=1.
\]

Then `A` is irreducible. The first equality says that `A` divides the square-free
polynomial `X^(p^D)-X` and each irreducible factor degree divides `D`; a nontrivial factor consequently has degree a proper
divisor of `D`, which would divide the relevant gcd.  Conversely an irreducible
degree-`D` polynomial satisfies the two tests.  The supplied replay implements
this proof in exact polynomial arithmetic for small prime-field instances.

## Boundary

This is a presentation-certificate only: it verifies a given polynomial, not a
field embedding, factorization, discrete logarithm, subgroup relation, or
descent.  It deliberately does not duplicate the existing cyclic-relation or
finite-subgroup checkers in this skill.  The replay is restricted to prime base
fields and small explicit inputs; the paper's extension-field arithmetic and
its complexity bounds remain source-dependent.

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/discrete_logarithm/paper.pdf)。
