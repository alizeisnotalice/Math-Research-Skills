# Ryser identity by exact coefficient cancellation

For an \(n\times n\) matrix \(M\) over a commutative ring,
\[
\operatorname{perm}M=
\sum_{S\subseteq[n]}(-1)^{n-|S|}\prod_{i=1}^{n}\sum_{j\in S}M_{ij}.
\]
The coefficient of a row-choice monomial indexed by \(f:[n]\to[n]\) is
\(\sum_{S\supseteq\operatorname{im}f}(-1)^{n-|S|}\).
By binomial cancellation it is one if \(f\) is onto and zero otherwise.
On equal finite sets the onto row choices are the permutations.
The argument applies integrally and hence over any commutative ring.
This gives an unweighted finite permanent evaluation route.

The bounded Python replay uses exact integer coefficient arithmetic at
\(1\le n\le4\), independently of the formal project. At \(n=4\) all
256 row choices were checked, and exactly 24 permutation monomials survive.

~~~sh
python3 -B scripts/replay_ryser_coefficients.py
~~~

The source is the byte-bound formal-math PDF SHA-256
`882f5eefb1e067cc8c99ddfe660c10d1d67f9fcee7b69364bd0bab06c0c1f97c`,
physical pp. 4 and 60 and the corresponding formal module. On p. 60 the sign is written as the product of the \(1-2e_j\) factors times \((-1)^n\), equivalent to the subset sign above.
This reference establishes the permanent identity. The matching Hexagon copy displays the same formula on physical p. 60.
Its SHA-256 is `e6de6806c7fd939ff536451951b0c44231b3ad1b6148bdb33fcc4e3143268b88`.
For these 70 pages, pypdf extracted identical ordered text after whitespace
normalization and removal of the one exact stamp on p. 1. PDFium independently
reported the same ordered Unicode glyphs outside that margin stamp, with
coordinate differences below 0.46 points. The files have different drawing
streams and SHA-256 values. The correspondence supports the same printed
identity. The circuit separation and Lean replay retain their own
verification gates.
[Fixed Ryser source](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Ryser.lean)
