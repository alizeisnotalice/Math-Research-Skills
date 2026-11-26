# Toroidal nondegeneracy for semi-abelian Ax--Schanuel

Source. J. Noguchi, *Analytic Ax-Schanuel Theorem for semi-abelian varieties and Nevanlinna theory*, arXiv:2203.00470v1, physical pp. 1--3, SHA-256 `468f119fc431c22eb3ed06fa59a5bb584c8f90e900acc2efd80a45a93ae0dfac`.

For a semi-abelian variety \(A\) of dimension \(n\) and an entire map \(f:\mathbb C\to\operatorname{Lie}(A)\), Theorem 1.3 states that \(A\)-nondegeneracy implies
\[
  \dim \overline{(\exp_A\circ f,f)(\mathbb C)}^{\mathrm{Zar}}\geq n+1.
\]
The source defines nondegeneracy by excluding containment of \(\exp_A\circ f(\mathbb C)\) in a translate of any proper connected algebraic subgroup of \(A\). On p. 2 it identifies the torus case \(A=(\mathbb C^*)^n\) with \(\mathbb Q\)-linear independence of the functions \(f_j(z)-f_j(0)\).

`check_torus_q_independence.py` gives an exact sufficient-premise check when every \(f_j\) is explicitly a polynomial with rational coefficients. It computes the rational rank of their nonconstant coefficient vectors. Full rank certifies the quoted torus premise for that encoded input. A rank failure establishes only that this route cannot use the torus nondegeneracy condition.

The checker does not construct a semi-abelian variety, compute a Zariski closure, verify a general entire function, or prove the source theorem. The source proof uses its Log Bloch--Ochiai input and a Nevanlinna key estimate.
