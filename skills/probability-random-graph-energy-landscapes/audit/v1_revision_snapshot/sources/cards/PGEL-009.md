> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-009 — Dense networks that do not synchronize and sparse ones that do

## Identity and reading record
Alex Townsend, Michael Stillman, and Steven H. Strogatz, “Dense networks that do not synchronize and sparse ones that do,” arXiv:1906.10627v4 (17 June 2020), DOI [10.1063/5.0018322](https://doi.org/10.1063/5.0018322); [official arXiv record](https://arxiv.org/abs/1906.10627). The D02 sourcepool and local PDF first page match the cited title/authors/version; R05 verified source identity but did not verify metadata independently. The exact local arXiv v4 PDF is 6 physical pages, SHA-256 `1429ddba0df2f4a33af15f6b65e912394de83365003643fa63f0f49775a5802a`. Reader L03 read all six physical pages in order, including figures, discussion, data-availability note, and references. No exact-title/hash accepted canonical full-read match was found. R05 L03_B4 helper-stage review passed; mother-card hash binding is pending.
## Model and claims

The paper studies identical-frequency Kuramoto oscillators on simple, undirected, unweighted circulant graphs. The adjacency is symmetric binary, (a_s=a_{n-s}), with no self-loops. The ODE is a gradient system. “Globally synchronizes” means convergence to the in-phase state from all initial phases except a measure-zero set (physical p. 1). Twisted states are equilibria of every circulant graph; a positive Jacobian eigenvalue proves linear instability, while strictly negative non-rotational eigenvalues certify local asymptotic stability modulo the rotation mode.

For a (p)-twisted state, the source’s exact Fourier eigenvalue formula is Eq. (5), physical p. 3:

\[
\lambda_r(J_p)=\sum_{s=1}^{n-1}a_s\cos(pt_s)\bigl[-1+\cos(rt_s)\bigr],\qquad t_s=2\pi s/n.
\]

The paper gives two different kinds of evidence about the dense threshold:

- For (n=8m), the circulant graph with (a_j=1\) iff (j\bmod 4\ne2\) has degree (6m-1), so its connectivity tends to (3/4). At the (2m)-twist, Eq. (5) reduces to
  \[
  \lambda_r(J_{2m})=-2\sum_{s=1}^{2m-1}\sin^2\!\left(\frac{\pi sr}{2m}\right)\le0.
  \]
  Four modes are zero (the rotational mode and (r=2m,4m,6m)); therefore linearization alone cannot determine stability. The authors’ simulations report weak nonlinear instability and escape time of order (\eta^{-1}\) from an (\eta\)-neighborhood (physical pp. 2–4). This example does **not** establish a stable competing attractor or the conjectured lower bound (\mu_c\ge3/4\); (\mu_c=3/4\) is explicitly a conjecture.
- The paper reports a finite circulant construction improving the lower bound on critical connectivity to about (0.68284): start from an (n=22) WSG graph with a stable 1-twist, twin by (K_{85}), add the described matching edges to obtain (n=1870), degree (1276), and then twin further. The 1-twist and parameter search are supported by Jacobian eigenvalue calculations and computer search (physical pp. 4–5); preserve that computational construction and its exact scope rather than treating the entire search as a general theorem.

For the sparse construction, let (n=2^m) with (m\ge2), and connect cyclic offsets that are powers of two through (2^{m-1}), with the reflectional offsets included. The graph has degree (2m-1=2\log_2n-1) and ((2\log_2n-1)n/2) edges. Eq. (6), physical p. 5, gives

\[
\lambda_p(J_p)=m-\sum_{k=1}^{m-2}\cos\!\left(\frac{2\pi p2^k}{2^m}\right)-2\cos\!\left(\frac{2\pi p}{2^m}\right)>0,\quad 1\le p<2^m.
\]

For (m\ge2), the bound follows by replacing each cosine by at most (1), giving a nonnegative lower bound, and using \(\cos(2\pi p/2^m)<1\) for every nonzero twist to make it strict. The formula's lower limit is not valid at (m=1): there (n=2) and the graph is (K_2). Evaluate the source Eq. (5) directly for its nonzero twist: the eigenvalue is (2), so that state is still strictly unstable; literal extension of the simplified Eq. (6) gives (1-2\cos\pi=3), not (2). Thus all twisted states are linearly unstable in this particular graph family, with the two-vertex case handled separately. The paper does not rule out other stable equilibria for general (n); its Macaulay2 classification for the (n=8) instance is finite computational evidence only, and the authors explicitly leave the all-attractors question open for larger (n) (physical p. 5).

## Reusable method and limits

The Fourier diagonalization is reusable for symmetric circulant positive graphs: test twisted-state stability by the exact spectrum of the symmetric circulant Jacobian. The all-twists sparse calculation is a family-specific strict-instability result. It is not a global-synchronization theorem because non-twisted equilibria are not excluded. The dense (75\%\) razor-edge family has zero Hessian modes and is only numerically shown to be weakly unstable. All results require identical frequencies and nonnegative symmetric couplings; they do not establish a signed-graph Hessian certificate or any claim about C118.

## Formula inspection and local calculation

Source PDF physical pp. 3 and 5 were rendered and viewed to verify Eqs. (5)–(6), the four zero modes, the strict cosine argument, and the stated degree/edge counts. `../math/pgel_012_normalization_check.py` independently evaluated the displayed sparse eigenvalue formula exactly with SymPy for every nonzero twist at (n=8) and (n=16); the minima were (3-\sqrt2>0) and (4-\sqrt{\sqrt2+2}-\sqrt2/2>0). The same script evaluates Eq. (5) at (m=1,n=2) as (2), versus (3) from literal Eq. (6) extension. These finite checks validate only the listed instances; the all-(n) proof for (m\ge2) is the source’s displayed cosine bound.

Complete physical-page and section coverage is recorded in `../reading_coverage.json` (mother source entry PGEL-009; rendered images remain in `../renders/PGEL-009/`).
