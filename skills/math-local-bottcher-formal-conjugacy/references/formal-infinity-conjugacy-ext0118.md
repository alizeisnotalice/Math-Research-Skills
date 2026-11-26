# Formal Böttcher conjugacy at infinity

The local 58-page copy of Sina Saleh, *Bialgebraic geometry of Böttcher
coordinates*, SHA-256
`821993daf30582f0a32f2b0b06606c25ed2d615c40dce7e25b62031f41ef534f`,
gives the inverse-coordinate equation \(\Psi(z^d)=f(\Psi(z))\) on
physical p. 12. The source records the input root-of-unity ambiguity.
[Fixed source arXiv:2606.24553v2](https://arxiv.org/abs/2606.24553v2)

For \(f(w)=w^d+\sum_{j<d}a_jw^j\), fix the leading Laurent term \(z^{-1}\).
Writing \(u(z)=z\Psi(z)\) gives the formal equation
\[
u(z^d)=u(z)^d+\sum_{j=0}^{d-1}a_jz^{d-j}u(z)^j,\qquad u(0)=1.
\]
At order \(m\ge1\), the left side uses \(u_{m/d}\) if \(d\mid m\) and
zero otherwise. On the right only \(u^d\) contains the new \(u_m\), with
coefficient \(d\). Hence there is a unique formal coefficient at each
order over \(\mathbb Q\). The script computes in \(\mathbb Q[z]/(z^{N+2})\)
by truncated Horner multiplication and checks every resulting Laurent
coefficient through degree \(N-d+1\).

~~~sh
python3 -B scripts/check_formal_conjugacy.py examples/quadratic-conjugacy.json
~~~

The JSON field `lower` lists the coefficients of \(1,w,\ldots,w^{d-1}\)
as integers or rational strings, omitting the leading monic coefficient.
The field `order` gives \(N\), the largest nonnegative Laurent index.
For \(w^2+w\) at \(N=5\) the replay gives
\((-1/2,-1/8,0,-9/128,0,-9/1024)\).
Analytic use of the series requires convergence and a verified local
branch. Julia-set and \(f\)-special conclusions require the independent
global hypotheses and arguments in the source.
