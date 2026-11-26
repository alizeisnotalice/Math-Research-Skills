# Effective unit-equation enumeration in a coordinate ring

Source: Jan-Hendrik Evertse and Kálmán Győry, *Effective results for unit equations over finitely generated domains*, arXiv:1107.5756v1, physical pp.3–4, SHA-256 `9005863f1703be9af72721744343f4980873932683e1378d03a151b82b104da5`.

Represent `A` as `Z[X_1,...,X_r]/I`, retain representatives for `a,b,c`, and use an ideal-membership oracle. Corollary 1.2 reduces enumeration of `a epsilon+b eta=c` in units to bounded polynomial quadruples `(epsilon,epsilon',eta,eta')` satisfying

\[
a\epsilon+b\eta-c,\quad \epsilon\epsilon'-1,\quad \eta\eta'-1\in I.
\]

The height/size bound comes from Theorem 1.1. This is a conditional enumeration route; it does not provide the ideal-membership algorithm or unit generators.
