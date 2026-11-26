# Polynomial shared-leg separator in arbitrary characteristic

This reference adds a finite alternative to the installed Fourier shared-leg
separator. It does not establish a matrix-multiplication exponent bound.

## Source and statement

Houxi Lu, *Polynomial Separation of a Shared Tensor Leg and Matrix
Multiplication in Arbitrary Characteristic*, arXiv:2610.18914v1, local
preprint dated 9 October 2026,
local source
08_OpenAI_Anthropic_Gamma_PiE/PDF/O42-02_Primes_between_8th_powers_Polynomial_Separation_of_a_Shared_Tensor_Leg_and.pdf,
SHA-256
b9f5231c18a786b07819150152072c75ddb50caf68453c57538c92b9fe34567f.
The local title/author agree with the arXiv v1 record. This source is an
unpublished preprint. Its Proposition 2.1 (physical pp.2--3)
states that, if a field \(F\) has at least \(M+n-1\) distinct elements and

\[
A=\sum_{h=1}^{M} A_h,\qquad A_h:X\times Y_h\times Z_h\longrightarrow F,
\]

has pairwise separate matched \(Y_h,Z_h\) sectors, then

\[
A^{\oplus(M+n-1)}\rightsquigarrow
\bigoplus_{h=1}^{M}\bigl(A_h\otimes B_X(n)\bigr),
\]

where \(B_X(n)\) is the \(n\)-dimensional dot-product tensor. The right-side
summands have independent spaces on all three legs.

Choose distinct \(a_1,\ldots,a_M\), put
\(P=F[t]_{<M}\) and \(J=F[u]/(u^n)\). Evaluation
\(p\mapsto(p(a_1),\ldots,p(a_M))\) separates copies of \(X\).
The local substitution

\[
\sigma_h(p,j)=p(a_h+\varepsilon u)j
\]

has the desired evaluation limit at \(\varepsilon=0\). For
\(Q=F[t]_{<n}\), \(W=F[t]_{<M+n-1}\), ordinary multiplication
\(\mu:P\otimes Q\to W\) satisfies the source identity

\[
\sigma_h\circ(\mathrm{id}_P\otimes g_h)=\iota_h\circ\mu.
\]

Interpolation at \(M+n-1\) field points gives the finite rank restriction
\(C_\mu\leq M+n-1\).

## Dependency boundary

The adopted proposition proves the needed evaluation, substitution, product
identity and multiplication-rank ingredients on pp.2--3, so no external
preprint theorem is used for this finite separator. The source's physical
pp.4--5 invokes OpenAI's *An Upper Bound of 9/4 for the Matrix Multiplication
Exponent* for a character comparison, entropy passage and detecting-character
argument. Those later dependencies and the claimed \(\omega\leq9/4\) are not
adopted here.

## Admission procedure

1. State the field and exhibit \(M+n-1\) distinct elements. Do not use this
   separator over a field that fails this cardinality condition.
2. Give the matched decomposition and prove that all \(Y_h\) are mutually
   separate and all \(Z_h\) are mutually separate. This method does not repair
   unmatched cross-sector tensor terms.
3. Fix the spaces \(P,J,Q,W\), the points \(a_h\), and the three pullback maps.
   Verify the multiplication identity exactly.
4. Pay the \(M+n-1\) copies through the polynomial-multiplication restriction.
   The fact that there are no factorial denominators does not remove this rank
   cost.
5. Treat any character inequality, entropy limit or matrix-exponent conclusion
   as a separate theorem with its own hypotheses.

The helper checks Steps 1 and the finite polynomial identities over a prime
field. It is not a proof of a tensor degeneration for arbitrary input forms.
