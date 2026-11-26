# Exact cubic bracket for a cograph distance eigenvalue

**Source status:** author-hosted preprint. **Source:** Horace Dong, *Connected cographs with distance eigenvalues just below -2*, SHA-256 `6936a2a60b103c3ffad02d80b7a3ab5d0746abab5d943f2eb75a05af9aded699`, physical pp. 1–2, [source PDF](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/cograph-distance/note.pdf).

This is a narrow extension of L03's exact rational sign-certificate route. Given an integer `m>=1`, form the source family `G_m=K_1 join (K_1 union m K_2)` and its three-cell equitable quotient for the distance matrix,

`Q_m=[[0,2m,1],[1,4m-3,2],[1,4m,0]]`.

The source identifies `det(xI-Q_m)` with

`p_m(x)=x^3+3x^2-x-3-m(4x^2+10x+4)`.

The exact endpoint signs `p_m(-2)>0` and `p_m(-2-1/(2m))<0` bracket a real root in `(-2-1/(2m),-2)`. Equitability lifts a quotient eigenvector to the distance matrix, giving a distance eigenvalue of this explicitly supplied graph.

Run `scripts/cograph_distance_cubic_wave7.py --m 1 3 100` for exact determinant and sign checks. It verifies the displayed finite algebra, not the source's cograph classification, formalization report, or a spectral statement for arbitrary graphs.
