# Gamma-normalized Brégman--Minc bound

Source: Suvrit Sra, *A sharp Brégman--Minc bound for permanents*, author preprint v1, 12 physical pages; reviewed physical pp. 1 and 3--8.  Local source identity: SHA-256 `1610d9f183733a5c3b37c6b29622b38dcf7ea9e933819b3b917f52da2fee57b1`.

For a nonnegative row-stochastic square matrix (A), the source states

\[
\operatorname{per}(\phi[A])\leq 1,\qquad
\phi(x)=\Gamma(1+1/x)^{-x},\quad \phi(0)=0.
\]

The proof reduces the matrix assertion to a scalar simplex inequality and then uses induction, Tonelli interchange, and the Gamma normalization.

## Use boundary

Retain nonnegativity, square shape, and row-stochastic normalization exactly.  Check the zero convention for every entry before forming \(\phi[A]\).  The source proof's scalar-simplex/Gamma and integration steps are the dependencies for a symbolic use; this is not a claim about arbitrary entrywise transforms or about equality cases beyond the source statement.
