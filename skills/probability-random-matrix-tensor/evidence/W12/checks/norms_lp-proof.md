# Exact comparison behind `norms_lp.py`

Take (A=\operatorname{diag}(1,-1)) and (p=4). The diagonal symmetric injective norm is
\[
\sup_{|x_1|^4+|x_2|^4\le1}|x_1^2-x_2^2|=1,
\]
since (|x_1^2-x_2^2|\le\max(x_1^2,x_2^2)\le1), with equality at a coordinate vector. The full bilinear injective norm is
\[
\sup_{\|u\|_4,\|v\|_4\le1}|u^TAv|=\sup_{\|v\|_4\le1}\|Av\|_{4/3}=\sqrt2.
\]
The last equality is Hölder duality and the sharp inclusion norm (\ell_4^2\hookrightarrow\ell_{4/3}^2), attained at (v=2^{-1/4}(1,1)) up to signs. Thus the two injective norms are not interchangeable, even though for symmetric tensors they are equivalent within a factor depending only on tensor order.

For (I_2), (\sup_{\|x\|_4\le1}x^TI_2x=\sqrt2), by Cauchy–Schwarz applied to (x_1^2+x_2^2); the Euclidean spectral norm of (I_2) is (1). Hence the operator norm is not a synonym for the diagonal symmetric (\ell_4) norm either. The special identification in the cited tensor paper is the Euclidean matrix case (r=p=2).

The MATLAB grid output is numerical corroboration only; the equalities above are the exact proofs.
