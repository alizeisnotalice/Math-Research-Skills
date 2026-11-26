# Bessel cross-product recurrence

**Source and proof step.** Mangoubi--Rosenblatt, *On multiplicity bounds for eigenvalues of the clamped round plate*, arXiv:2411.07564v2, local SHA-256 `fcbcd8b8abce402f98aa273ff53ee0cbe51fb2fb2db5ae99381b792ba588f372`, physical pp. 4--6.  Key Identity 2.5 follows directly from the displayed `I` three-term recurrence after substituting `F_m=I_m/(xI_{m-1})`; Theorem 3.1 then compares the two displayed expressions for `W_{m-1}+W_{m+1}` and uses that identity.

**Reusable contract.** Input a positive real `x`, an allowed rational index `m`, Bessel and modified-Bessel values obeying the source recurrences, and nonzero denominators defining `F_m` and the required shifts.  The exact consequences are

`x^2 F_{m+1}F_m=1-2mF_m`,

`W_{m+1}=2mF_mW_m-(1-2mF_m)W_{m-1}`.

These equations support finite symbolic elimination from supplied consecutive cross products. They do not establish denominator nonvanishing outside the source's positive-real/index regime, the nonzero character of an elimination polynomial, common-zero exclusion, Bessel zero transcendence, or the spectral theorem.
