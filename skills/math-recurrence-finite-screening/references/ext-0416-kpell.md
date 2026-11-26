# k-generalized Pell finite residual screen

Source: `EXT-0416`, arXiv:2605.17699v2, physical pp. 1--3 and 16 (17 pages total), SHA-256 `a20a7bc85d96ffe0f1b1d7ce0ae1a253f899e42392bb756b1a26ab8eee241a00`.

The source defines (P_0=cdots=P_{-(k-2)}=0, P_1=1) and

\[
P_n=2P_{n-1}+\sum_{j=2}^{k}P_{n-j}.
\]

Its physical p. 16 gives an exact `perfect_power` search.  The bundled input reproduces its stated residual box with exact Python integers: (2\leq k\leq248), (2\leq m<n\leq358).  It found 15,695,862 index pairs and no equal primitive bases.

This is an independent bounded replay of the recurrence/power predicate.  It does **not** verify the paper's all-(k) theorem, which also uses Binet estimates, nonzero logarithmic forms, continued fractions, LLL, and reductions outside this finite box.
