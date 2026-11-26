# bounded realization of a quadratic Siegel domain

**Source.** *Symmetry of Semialgebraic Bounded Domains with Compact Quotient*,
pp. 18, 20–22, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf).

**Input.** Provide a nonempty connected dilation-invariant open cone
\(C\subset\mathbb R^k\), Hermitian vector form \(H\) on \(\mathbb C^m\),
independent real linear forms \(\ell_1,\ldots,\ell_k\), and \(c>0\), with
\[
\ell_a(y)>0\ (y\in C),\qquad \ell_a(H(z,z))\ge c\lVert z\rVert^2.
\]
The domain is \(D=\{(z,w):\operatorname{Im}w-H(z,z)\in C\}\).

**Procedure.** Extend \(\ell_j\) complex linearly and put \(u_j=\ell_j(w)\).
Use the explicit map
\[
B(z,w)=\left(\frac{u_1-i}{u_1+i},\ldots,
\frac{u_k-i}{u_k+i},\frac z{u_1+i}\right).
\]
Then \(\operatorname{Im}u_j>c\lVert z\rVert^2\), so the first coordinates
lie in the unit disk and
\(\lVert z/(u_1+i)\rVert\le1/(2\sqrt c)\). Recover \(u_j,w,z\)
by inverse Cayley coordinates, the independence of the \(\ell_j\), and
multiplication by \(u_1+i\).

**Output.** A biholomorphic bounded realization in \(\mathbb C^{m+k}\).

**Boundary.** This does not derive the quadratic model, its cone inequalities,
or divisibility. Vey's symmetry conclusion additionally requires a verified
properly discontinuous compact-quotient action and the stated invariances.

## 固定来源

- 物理页 1, 18, 21, 22。Theorem 5.2; equations (5.3)–(5.4), (6.1); Theorem 6.1 SHA-256 `a93c6ca7f3221b4598a22cac0b0b313a2661c5d8be148b8f274b04efcb42045d`。[Symmetry of semialgebraic bounded domains with compact quotient](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf)
