# Mellin matrices, denominators, and a Minkowski criterion

Source: Francis Brown, *Mellin transforms, transfinite diameter and rational approximations of integrals*, local PDF SHA-256 \`fcbcc22ee7504b9e057c534c0e5fae3f3812af8548d132cd2018ce4857a20bef\`, physical pp. 4-5 and 21-22.  Dependency check: the cited pages define the integral matrix/denominator data and derive the linear-form step from Minkowski's theorem.

For a rank-\(N\) Mellin matrix \(Q^\sigma_N\), choose rational invertible matrices \(D_{\ell,N},D_{r,N}\) with
\[
D_{\ell,N}Q^\sigma_ND_{r,N}\in M_N(\mathbb Z[\xi_1,\ldots,\xi_m]),
\qquad \delta_N=|\det(D_{\ell,N}D_{r,N})|.
\]
Minkowski's linear-forms theorem gives a nonzero integral coefficient vector when the product of coordinate bounds is at least the determinant.  The source's Corollary 7.3 states, assuming \(\det Q^\sigma_N\ne0\) infinitely often,
\[
\operatorname{Sup}_{2N}(f(\sigma))\,\delta_N<1
\quad\Longrightarrow\quad
\dim_{\mathbb Q}(\mathbb Q\xi_1+\cdots+\mathbb Q\xi_r)\ge2.
\]
For \(r=2\) and \(\xi_1=1\), this is its irrationality criterion.

The workflow is conditional: fix the period basis, verify the integral matrix and nonzero determinant, give actual denominator matrices, then bound the relevant transfinite diameter.  It does not manufacture any of these arithmetic inputs.
