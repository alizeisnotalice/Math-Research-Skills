# Optimized Hermite--Padé determinant gate for \(e^\alpha\)

Source: S. Fischler and T. Rivoal, *A new transcendence measure for the
values of the exponential function at algebraic arguments*,
arXiv:2502.17992v1 (25 February 2025), local SHA-256
`117b9935015a294313e1cce7535e5fdc26ffa8c3b70b7a86509fae93cb7c794e`.

## Caller contract and conclusion

Let `K` be a number field, `alpha` a nonzero algebraic number with
`d=[K(alpha):Q]>=1`, `delta>=1`, and
`P in O_K[X]\{0}` have degree at most `delta` and usual coefficient height at
most `H>=1`.  For an auxiliary integer `p>=d delta`, define

\[
 \psi(d,\delta,p)=\delta d^2(p-\delta+1)p-\delta d+1+d(p-\delta+1)-1.
\]

The paper gives an explicit lower bound for `|P(e^alpha)|` with the principal
power `H^{-psi(d,delta,p)}` and an explicit subpower `log log(H+2)` loss
(Proposition 1, physical pp. 10--13).  For the asymptotic form, choose

\[
 p_1=\delta d-1+\lfloor\delta\sqrt{d^2-d}\rfloor,\quad p_2=p_1+1,
\]

and select `lambda` as the one of `p_1,p_2` having smaller `psi`; Theorem 1
gives `|P(e^alpha)|>c H^{-psi(d,delta,lambda)-epsilon}` for each `epsilon>0`
with a source-dependent positive constant `c` (physical p. 2).  This is a
lower-bound/reference gate, not an integer-linear-form certificate for a new
constant.

## Determinant route actually used

1. Take Hermite--Padé polynomials `P_{k,ell}` and remainders
   `R_ell(x)=sum_{k=0}^p P_{k,ell}(x)e^{k alpha x}`.  The source fixes their
   orders of vanishing at zero, degrees, and a nonzero polynomial determinant
   (physical p. 5).
2. Put `q=lcm(1,...,p)d(1/alpha)`.  The source proves integrality of
   `q^{(p+1)n+pn!}P_{k,ell}(1)` over `O_{K(alpha)}`, coefficient and remainder
   bounds, and the nonzero determinant at `x=1` in (2.1)--(2.4).
3. Complete shifted coefficient rows of `P` by selected Padé rows, producing
   a nonzero algebraic integer determinant `D`.  Its norm supplies the lower
   bound; the `L_0=P(e^alpha)` column and the remainder bounds supply the
   upper bound (physical pp. 6--7, especially (2.8)--(2.10)).
4. Choose the least admissible `n` satisfying the source's factorial
   threshold, then use `n!>=n^n e^{-n}` to make Proposition 1 explicit
   (physical pp. 10--13).  The strict condition `p>=d delta` is required for
   this choice.

## Boundary

All height conventions, the field `K`, the embedding degree and the factor
`d(1/alpha)` must be retained.  A finite calculation of Padé rows does not
replace nonvanishing, norm control, or the all-height choice of `n`.

Locators: physical pp. 2, 5--7, 10--13; Theorem 1, (2.1)--(2.10), and
Proposition 1.
