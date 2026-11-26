# Exact-3-CNF root-of-unity encoding

For a nonempty exact-3-CNF with variables numbered `0,...,n-1`, let `q_i` be
the `(i+1)`-st odd prime, `N=prod_i q_i`, and `m_i=N/q_i`.  Encode a positive
literal by `P_i^+(X)=X^{m_i}-1` and a negative literal by
`P_i^-(X)=sum_{r=0}^{q_i-1}X^{r m_i}`.  If `C_j` is the product of a clause's
three literal polynomials, put

\[
 S=\sum_jC_j(X)C_j(X^{-1}),\quad d=\max\{|e|:[X^e]S\ne0\},\quad
 A=3X^dS,\quad B=X^N-1,
\]

and `F=A+X^M B` for any integer `M >= 0`.

At an `N`-th root of unity, declare variable `i` true exactly when
`z_i=zeta^{m_i}=1`.  The literal factors make `S(zeta)=0` exactly for a
satisfying assignment.  The source proves the stronger statement that `F`
has *some* root of unity iff the formula is satisfiable.  The script builds
the finite sparse tables and exhaustively checks the `N`-th-root assignment
encoding for small caller-supplied instances.

Run `scripts/build_sparse_cnf_root_encoding.py INPUT.json`.  The input has
positive `variables`, a nonempty `clauses` list of three nonzero signed
variable indices, and optional nonnegative `shift`.  This is an exact finite
construction, not an irreducibility tester: it does not implement the
source's gap theorem or establish coNP/PP claims.

## Source and audit boundary

Cao--Gao--Huang--Nie, *Irreducibility Testing of Sparse Polynomials over
Integers is NP-hard and Probabilistic Polynomial Time*, arXiv:2610.37179v1
(27 October 2026), physical pp. 3--4, Lemma 5 and its proof.  The source's
irreducibility and upper-bound theorems additionally use a
Filaseta--Ford--Konyagin lifting/gap result and recent analytic estimates;
those claims are not adopted here.
