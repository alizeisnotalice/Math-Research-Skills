# k-generalized Lucas finite concatenation screen

Source: `EXT-0418`, arXiv:2509.24057v1, physical pp. 1--3 (15 pages total), SHA-256 `46cde8982adb3f0935713bc34ca97b4c64c353a13d52c0d1955e8982cda61cfa`.

For (k\geq3), the source uses (L_0=2,L_1=1), negative initial values zero, and (L_n=\sum_{j=1}^kL_{n-j}).  Its equation is the decimal predicate

\[
L_n=L_m10^{d(L_p)}+L_p.
\]

The example scans (3\leq k\leq12, 2\leq n\leq25) exactly.  It finds the displayed `12` identities for (k\geq4) and `22` for (k=4), but this small box is not a verification of the paper's complete all-(k) classification.  That classification depends on the cited Binet estimate, Matveev, reduction data, and Sage residual computations.
