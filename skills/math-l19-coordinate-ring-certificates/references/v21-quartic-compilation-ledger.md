# Exact quartic compilation of a quadratic row system

For a finite collection of integer quadratic forms \(R_j\), expand
\[
P(x)=\sum_j R_j(x)^2.
\]
Over \(\mathbb Q\), nonnegativity of rational squares proves that \(P(x)=0\)
is equivalent to \(R_j(x)=0\) for every row. The same conclusion works over
an ordered field. Over \(\mathbb C\) or a finite field, check the intended
construction separately. A sum of squares can cancel there.

For the specific v21 manuscript, the local SHA-256
`61410502c6d71bcbd7f699a697c8ea2e7a7d9ea294c61b31225f1e37754e9d47`
matches the PDF at public commit
`964d7dd71f253091dbc5eac793b78cc56d1fcc73`. Physical pp. 799–821 contain
the displayed construction. The genuine source tables and 229-coordinate
quartic were checked together using the pinned construction scripts.
[Fixed v21 construction package](https://github.com/elliotglazer/diophantine-z-q/tree/964d7dd71f253091dbc5eac793b78cc56d1fcc73/research/version21/construction)

From the root of that source checkout run:

~~~sh
python3 -B research/version21/construction/verify229.py
python3 -B research/version21/construction/check_printed.py
python3 -B research/version21/construction/verify_arithmetic.py
~~~

The local replay expanded 207 quadratic rows to 3,312 monomials, checked
the printed TeX rows and coordinate tables, and rejected all ten programmed
mutations. The separate \(N=15\) finite comparison had strict positive
rational margin \(196519/1365000\).

The result identifies the rational zero set of the displayed polynomial
with the common zero set of those displayed rows. Identifying the image of
that zero set under projection to the input coordinate as \(\mathbb Z\)
still requires the arithmetic soundness and completeness of the row system.
