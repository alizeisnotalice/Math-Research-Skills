# Positive finite example: weighted-triangle transfer current

Take a triangle with conductances (c_{01}=1), (c_{12}=2), (c_{20}=3). A weighted UST assigns weight equal to the product of its two edge conductances. The three trees have weights (6,3,2), so the partition function is 11 and

\[
\mathbb P(01,12\in T)=\frac{2}{11}.
\]

Ground vertex 2. The reduced Laplacian is (L=\begin{pmatrix}4&-1\\-1&3\end{pmatrix}), with inverse (L^{-1}=\frac1{11}\begin{pmatrix}3&1\\1&4\end{pmatrix}). For oriented edges (0\to1) and (1\to2), the unit-current transfer matrix is

\[
Y=\frac1{11}\begin{pmatrix}5&-3\\-3&4\end{pmatrix}.
\]

The weighted transfer-current determinant is (c_{01}c_{12}\det(Y)=2\cdot(20-9)/121=2/11), matching exact tree enumeration. The canonical W07 enumeration is recorded at `workers/W07/examples/verify_finite_examples.py` (earlier archive) and `.json`. L10 independently checked the weighted triangle with exact SymPy arithmetic at `expansions/20261115/readers/L10/G18_determinantal_dependence/analysis/finite_transfer_check.py` (earlier archive) and `.json`; that check explicitly separates transfer resistance from the conductance-weighted current matrix.

This verifies one finite instance of the transfer-current identity. It is not a proof of the general determinant theorem or an infinite-volume limit.
