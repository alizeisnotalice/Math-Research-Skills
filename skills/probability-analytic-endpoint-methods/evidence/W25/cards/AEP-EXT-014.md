> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-014 — Bui & Duong (2025)

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/ab52da0ff2f3e35a-AEP-EXT-014.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and reading record

The Anh Bui and Xuan Thinh Duong, “Calderón-Zygmund Decomposition, Hardy Spaces Associated with Operators and Weak Type Estimates,” *Potential Analysis* 63 (2025), 1–18, DOI [10.1007/s11118-024-10158-0](https://doi.org/10.1007/s11118-024-10158-0). Published open-access version (online 27 July 2024). Read all 18 physical pages, including complete references, declarations, and license; text was read sequentially and theorem/proof pages were rendered and visually checked. SHA256:  ef1c3d4e51f0797a160a1a5afd20d47a95c6e6abbd5a00145b3d775a3ff42ed1. Official records: [Springer article page](https://link.springer.com/article/10.1007/s11118-024-10158-0) and [publisher PDF](https://link.springer.com/content/pdf/10.1007/s11118-024-10158-0.pdf).

## Self-adjoint Gaussian setting: Theorem 1.6 (physical pp. 3–12)

The framework is a metric measure space \((X,d,\mu)\) with doubling Borel measure, \(\mu(X)=\infty\), and doubling exponent \(n\). First, \(L\) is a nonnegative self-adjoint operator on \(L^2(X)\); its heat kernel satisfies, for a.e. \(x,y\) and all \(t>0\),
\[
|p_t(x,y)|\le \frac{C}{V(x,\sqrt t)}\exp\!\left(-\frac{d(x,y)^2}{ct}\right).
\]
This yields Davies–Gaffney estimates, finite propagation speed for the cosine family, and corresponding Gaussian bounds for time derivatives. The paper defines \(H_L^p\) by the conical square function \(S_L\). The atomic characterization it invokes requires integer \(M>\frac n2(1/p-1/2)\) for \((p,2,M,L)\)-atoms; for the \(L^1\)-atom characterization used when \(0<p<1\), Theorem 2.2 has the same threshold.

**Theorem 1.6 (physical p. 4).** If \(T\) is sublinear and bounded on \(L^2(X)\), and is bounded from \(H_L^p(X)\) to \(L^p(X)\) for one \(0<p<1\), then \(T\) is weak type \((1,1)\). The proof establishes the estimate first for \(f\in L^1\cap L^2\), then uses the usual extension/density step.

**Proof chain through Theorem 2.5 (physical pp. 8–11).** The spectral Calderón reproducing formula in Proposition 2.4 decomposes each classical bad piece \(b_k\) at scale \(r_{B_k}\) into a frequency-localized integral term \(b_{k,1}\) and a finite-propagation term \(b_{k,2}=\Psi_{r_{B_k}}(\sqrt L)b_k\). The kernel of \(\Psi_{r_{B_k}}(\sqrt L)\) is supported at distance at most \(r_{B_k}\) and bounded at scale \(V(B_k)^{-1}\), so \(b_{k,2}\) is supported in \(3B_k\) and has \(L^\infty\) norm \(\lesssim\alpha\). Bounded overlap and doubling give \(g_2=\sum_k b_{k,2}\) with \(\|g_2\|_\infty\lesssim\alpha\), \(\|g_2\|_1\lesssim\|f\|_1\). Combining with the standard good piece gives \(f=g+b\), \(\|g\|_\infty\lesssim\alpha\), \(\|g\|_1\lesssim\|f\|_1\).

The remaining pieces are normalized by \(\alpha V(B_k)^{1/p}\). Finite propagation supplies the required support of the \(L^j\)-preimages; the Gaussian kernel bound and the reproducing integral give the \(L^1\)-atom inequalities for all \(j=0,\ldots,M\). Thus \(b=\sum_k b_{k,1}\in H_L^p\) and
\[
\|b\|_{H_L^p}^p\lesssim \sum_k(\alpha V(B_k)^{1/p})^p
\lesssim \alpha^{p-1}\|f\|_1.
\]
Finally, split the distribution event for \(Tf\) at threshold \(\alpha/2\). For \(g\), \(\|g\|_2^2\le\|g\|_\infty\|g\|_1\lesssim\alpha\|f\|_1\), so the \(L^2\) Chebyshev bound is \(\lesssim\|f\|_1/\alpha\). For \(b\), the \(H_L^p\to L^p\) bound and \(p\)-Chebyshev give \(\alpha^{-p}\|Tb\|_p^p\lesssim\alpha^{-p}\|b\|_{H_L^p}^p\lesssim\|f\|_1/\alpha\). This proves the weak endpoint with precisely the stated operator and heat-kernel hypotheses.

## General analytic-semigroup setting: Theorem 3.4 and a proof gap (physical pp. 12–16)

Section 3 drops self-adjointness. It assumes a bounded analytic semigroup \(e^{-tL}\), bounded \(H^\infty\) functional calculus on \(L^2(X)\), and a generalized Gaussian kernel bound of order \(m>1\):
\[
|p_t(x,y)|\le \frac{C}{V(x,t^{1/m})}
\exp\!\left(-\frac{d(x,y)^{m/(m-1)}}{c\,t^{1/(m-1)}}\right).
\]
The Hardy-space molecules decay over annuli, and the molecular characterization requires \(\epsilon>0\), \(0<p\le1\), and integer \(M>n(2-p)/(2mp)\). **Theorem 3.4** states that a sublinear \(L^2\)-bounded \(T\) that maps \(H_L^p\) to \(L^p\) for some \(0<p<1\) is weak type \((1,1)\) under those semigroup and functional-calculus assumptions.

The paper only sketches the proof of Theorem 3.4. It introduces \(L^1\)-molecules (Definition 3.6, Theorem 3.7), a semigroup reproducing formula (Proposition 3.8, Eq. (20)), and a second decomposition (Theorem 3.9). The proof of Theorem 3.9 splits each classical bad term into an integral molecule \(b_{k,1}\) and a semigroup-smoothed \(b_{k,2}\); maximal-function duality and \(L^2\)-boundedness of the Hardy–Littlewood maximal operator yield \(\|g_2\|_2^2\lesssim\alpha\|f\|_1\), while the molecule sum gives \(\|b\|_{H_L^p}^p\lesssim\alpha^{p-1}\|f\|_1\). The paper then says the proof of Theorem 3.4 is similar using Theorem 3.9.

**Source gap, not silently corrected:** Proposition 3.8 as printed is false even for a scalar positive operator. Eq. (20) and the following line were checked on the high-resolution render ../../../../../scope/source_snapshot/workers/W25/reader_batches/L01_B8/rendered/AEP-EXT-014-proofEq20-zoom-14.png. The printed formula states
\[
I=\frac{(-1)^{M+1}}{(M-1)!}\int_0^a(tL)^M e^{-tL}\,\frac{dt}{t}
+\sum_{k=1}^M\frac{(-1)^{M+k}(M-1)!}{(M-k)!}(aL)^{M-k}e^{-aL}.
\]
Set \(L=I\), \(M=2\), \(a=1\). The printed right side is
\[
-\int_0^1te^{-t}dt-e^{-1}+e^{-1}=-1+2e^{-1}\ne1.
\]
The integration-by-parts identity immediately below Eq. (20) has the same sign/coefficient problem. Since Theorem 3.9 uses this formula and Theorem 3.4 is only sketched from Theorem 3.9, the non-self-adjoint theorem’s proof route is **not source-verified as printed**. An independent candidate repair is the standard incomplete-gamma identity
\[
I=\frac1{(M-1)!}\int_0^a(tL)^M e^{-tL}\,\frac{dt}{t}
+e^{-aL}\sum_{j=0}^{M-1}\frac{(aL)^j}{j!},
\]
which is exact for scalar positive \(L\) and can be applied via suitable sectorial functional calculus. This is not the paper’s printed formula and does not by itself verify all downstream molecule/kernel estimates; no credit is assigned to Theorem 3.4 without an independent repair of those steps. The self-adjoint Theorem 1.6 route uses Proposition 2.4 instead and is not affected by this specific defect.

## Applications, method fit, and transfer limits

Section 4 states that on a complete noncompact connected Riemannian manifold with doubling measure, the Riesz transform \(\nabla\Delta^{-1/2}\) maps \(H_L^p\to L^p\) for \(0<p\le1\) under Davies–Gaffney estimates, and, if the Laplace heat kernel has the Gaussian upper bound, Theorem 4.2 gives its weak type \((1,1)\) consequence. It also lists heat-semigroup square functions. These are geometric applications of the stated operator framework, not general coordinatewise or arbitrary-dimensional vector endpoint constants.

For transfer, first verify the exact operator \(L\), doubling measure, Gaussian bound, \(L^2\) or \(H_L^p\to L^p\) mapping, and sublinearity. The self-adjoint route is source-supported under those hypotheses; the non-self-adjoint route remains conditional on repairing and rechecking Proposition 3.8 and Theorem 3.9’s downstream argument. Neither route by itself upgrades the formal C207 vector-\(L^p\) model or resolves the isolated C208 weak-\((1,1)\) target.

## Local mathematical check

../../../../../scope/source_snapshot/workers/W25/reader_batches/L01_B8/math/check_b8_identities.py verifies the scalar Proposition 2.4 formula for \(M=2\), \(z=1\), \(\Phi(x)=e^x\), and checks the two exponent cancellations in the self-adjoint weak-type proof. It also gives the exact \(L=I,M=2,a=1\) counterexample to the printed Proposition 3.8 formula and verifies the candidate corrected incomplete-gamma identity for this case. These are exact algebra checks; they do not establish kernel bounds, functional-calculus applicability, or the analytic theorem.
