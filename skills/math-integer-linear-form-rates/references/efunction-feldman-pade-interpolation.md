# Restricted E-function second-kind Padé interpolation

Source. Keijo Väänänen, *On a result of Fel'dman on linear forms in the values of some E-functions*, arXiv:1704.01762v1, local SHA-256 `d21400c88be35a5929a3bca2a98c176514b5ded6ab017f6025645513660b786f`, physical pp. 2--5.

For rational parameters \(\lambda_1,\ldots,\lambda_m\) whose pairwise differences are not integers and positive integer orders \(n_j\), set \(N=\sum_jn_j\). For each chosen index \(i\), equations (9) construct the degree-\(N\) polynomial \(Q_i\) in the falling-factorial basis. Its coefficients satisfy the interpolation value \(Q_i(N+1+\lambda_i)=1\) and vanish at the shifted nodes \(N+\nu+\lambda_j+\delta_{ij}\), where \(1\leq\nu\leq n_j\). Lemma 1 gives the nonzero determinant for the entire \(m+1\) family.

Run `python3 -B scripts/efunction_pade_feldman.py examples/efunction-pade-feldman-positive.json` to reproduce just those finite rational coefficients and interpolation identities. The rejection fixture has an integral parameter difference, where the source denominator can vanish.

This finite checker does not evaluate \(\varphi_\lambda(\alpha)\), clear all number-field denominators, prove the remainder estimates, or invoke the external linear-form criterion. A Baker-type bound requires the full hypotheses on \(K\), \(\alpha\), the parameter family, the integer multiplier and the nonzero linear form from physical pp. 6--10. It provides no representation of the Euler--Mascheroni constant.
