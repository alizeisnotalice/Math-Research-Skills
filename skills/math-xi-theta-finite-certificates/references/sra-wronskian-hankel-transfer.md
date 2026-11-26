# Wronskian-to-Hankel-minor transfer

Source: Suvrit Sra, *Sharp order-four sign regularity of a Jacobi theta kernel*, author preprint v1, 11 physical pages; reviewed physical pp. 2--5.  Local source identity: SHA-256 `174241481c47fe7a7228ee173d9784e68f8b2f4223ee3b83e19cfc9553bf02a0`.

For a \(C^{2q-2}\) function \(s\) on \([0,\infty)\), define

\[
W_j[s](t)=\det\bigl(s^{(a+b-2)}(t)\bigr)_{a,b=1}^j,
\qquad \varepsilon_j=(-1)^{j(j-1)/2}.
\]

The source's Lemma 2.2 proves the conditional transfer

\[
\varepsilon_jW_j[s](t)>0\quad(1\leq j\leq q,\ t\geq0)
\quad\Longrightarrow\quad
s(x+y)\text{ is strictly reverse-regular through order }q.
\]

The proof is a Chebyshev-system argument and also gives the converse with non-strict Wronskian signs by coalescing nodes.  Lemma 2.1 separately records the exact identity

\[
f f''-(f')^2=sW_3[s],\qquad f=(s')^2-ss'',
\]

so on the caller-provided domain \(s>0\), \(f>0\), the sign of \((\log f)''\) is the sign of \(W_3[s]\).

## Boundary

This is a transfer lemma.  It neither certifies any Wronskian sign for the Jacobi theta kernel nor validates the source's interval-arithmetic trust model.  Supply the differentiability, sign domain, and each Wronskian premise independently.
