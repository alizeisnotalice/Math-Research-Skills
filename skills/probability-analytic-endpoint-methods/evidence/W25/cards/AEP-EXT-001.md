> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-001 — O’Neil & Weiss (1963)

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/5be846d5e2999f38-AEP-EXT-001.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and reading record

R. O’Neil and G. Weiss, “The Hilbert transform and rearrangement of functions,” *Studia Mathematica* 23(2) (1963), printed pp. 189–198, DOI [10.4064/sm-23-2-189-198](https://doi.org/10.4064/sm-23-2-189-198). The complete six-physical-page official IMPAN archive scan was read visually, page by page, and all six pages are rendered in ../../../../../scope/source_snapshot/workers/W25/reader_batches/L01_B8/rendered/AEP-EXT-001-p01.png through p06.png. The PDF is image-only. SHA256: 02de8fc4082768502e69ac50a0c434a01eab38167e45c0c502a1cb98d126a4e7. Official metadata: [IMPAN article page](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/23/2/95344/the-hilbert-transform-and-rearrangement-of-functions); full text: [archive PDF](https://matwbn.icm.edu.pl/ksiazki/sm/sm23/sm23113.pdf).

## Rearrangement framework and Hilbert-transform theorem

For measurable \(f\), the paper uses \(\lambda_f(y)=m\{|f|>y\}\), the decreasing rearrangement \(f^*(t)=\inf\{y>0:\lambda_f(y)\le t\}\), and \(f^{**}(s)=s^{-1}\int_0^s f^*(t)\,dt\). The introductory properties include layer cake, equality of \(L^p\) norms of equimeasurable functions, Hardy–Littlewood’s product inequality, and—on atom-free measure spaces—the exact variational formula
\[
s f^{**}(s)=\sup_{m(E)=s}\int_E |f|\,dm.
\]
The authors use the norm property of \(f\mapsto sf^{**}(s)\) to move from indicator estimates to general \(f\).

The real-line Hilbert transform is defined by its principal-value limit. For a finite-measure set \(E\subset\mathbb R\), its transform of the indicator has distribution
\[
\lambda_{\widetilde{\chi_E}}(y)=\frac{2|E|}{\sinh(\pi y)},\qquad
(\widetilde{\chi_E})^*(t)=\frac1\pi\operatorname{arsinh}\!\left(\frac{2|E|}{t}\right).
\]
The paper assumes the cited a.e. existence result for the Hilbert transform in the relevant class; it does not reprove general principal-value existence.

**Theorem 1 (printed pp. 191–193).** If
\[
\int_0^\infty f^*(t)\operatorname{arsinh}(1/t)\,dt<\infty,
\]
then \(\widetilde f\) exists a.e. and, for every \(s>0\),
\[
s\widetilde f^{**}(s)\le \frac2\pi\int_0^\infty f^*(t)\operatorname{arsinh}(s/t)\,dt
=\frac{2s}{\pi}\int_0^\infty\frac{f^{**}(t)}{\sqrt{s^2+t^2}}\,dt.
\]

**Proof chain.** For a finite-measure set \(E\) of measure \(s\), split \(E=E_1\dot\cup E_2\) by the sign of \(\widetilde f\). The principal-value identity for the transform of an indicator rewrites \(\int_E|\widetilde f|\) as two pairings of \(f\) with transforms of \(\chi_{E_i}\). Apply Hardy–Littlewood to each pairing, substitute the explicit rearrangement of \(\widetilde{\chi_{E_i}}\), and use
\[
\operatorname{arsinh}(a/t)+\operatorname{arsinh}(b/t)\le 2\operatorname{arsinh}((a+b)/t).
\]
The variational characterization of \(s\widetilde f^{**}(s)\) gives the first bound. Integration by parts with \(F(t)=\int_0^t f^*(u)du=t f^{**}(t)\), whose endpoint term vanishes under the stated integrability condition, gives the second form.

**Theorem 2 (printed pp. 192–193).** For \(1<p<\infty\), the Hilbert transform is bounded on \(L^p(\mathbb R)\) with the paper’s constant
\[
A_p=\frac2\pi\int_0^\infty\frac{\operatorname{arsinh}(u)}{u^{1+1/p'}}\,du,
\qquad \frac1p+\frac1{p'}=1.
\]
The proof first uses ||f̃||_p <= N_p(f̃), inserts Theorem 1, and applies Minkowski after the substitution t=s/u. The rescaled rearrangement contributes u^(1/p), giving the displayed A_p integral directly. The norm comparison ||f||_p <= N_p(f) <= p/(p-1)||f||_p is stated, but no additional Hardy factor p-prime=p/(p-1) is multiplied into the printed A_p. This is strong type for \(p>1\), not a weak-\((1,1)\) theorem.

## Odd homogeneous kernels and the periodic conjugate function

**Theorem 3 (printed pp. 193–196).** In R^n, let Ω be homogeneous of degree zero, odd on the sphere, and integrable there, with ||Ω|| = integral over S^(n−1) of |Ω(θ)|. For 1<p<infinity and every s>0, the theorem states

> s f-hat**(s) ≤ ||Ω|| integral_0^infinity f*(t) arsinh(s/t) dt.

The separate indicator-set lemma on printed p.193 has the factor ||Ω||/2:

> s χ_E-hat**(s) ≤ (||Ω||/2) integral_0^s arsinh(2m(E)/t) dt.

The proof first treats finite unions of cubes. It writes the homogeneous-kernel integral in polar coordinates, fixes each angular direction, decomposes points into lines parallel to that direction, and applies the one-dimensional Hilbert-transform distribution formula on each line. Fubini gives the indicator estimate with its factor ||Ω||/2. To prove Theorem 3, split a level set into the two sign pieces; their bounds combine to the theorem's full ||Ω|| coefficient, not ||Ω||/2. Approximation then gives the stated rearrangement estimate. This is a rearrangement estimate under oddness and homogeneity, not a weak-(1,1) theorem for arbitrary rough kernels.

Section 4 treats the periodic conjugate function on the circle. **Theorem 4 (printed pp. 197–198)** gives, for \(f\in L^1(0,2\pi)\), \(0<s\le 2\pi\),
\[
s\widetilde f^{**}(s)\le \frac2\pi\int_0^{2\pi} f^*(t)\operatorname{arsinh}\!\left(\frac{\sin(s/4)}{\tan(t/4)}\right)dt
\le \frac2\pi\int_0^{2\pi}f^*(t)\operatorname{arsinh}(s/t)dt.
\]
The indicator distribution on the circle replaces \(2|E|/\sinh(\pi y)\) by the corresponding arctangent expression. **Theorem 5** says that \(f\in L\log^+ L\), i.e. \(\int_0^{2\pi}|f|\log^+|f|<\infty\), implies \(\widetilde f\in L^1\) and
\[
\int_0^{2\pi}|\widetilde f(t)|dt\le\frac2\pi\int_0^{2\pi}f^*(t)\log\cot(t/8)dt.
\]
The estimate is sharp for the sign function taking \(+1\) on one semicircle and \(-1\) on the other.

## Scope for endpoint-method transfer

Reusable inputs are the set-level rearrangement reduction, the exact Hilbert-transform distribution of indicators, Hardy–Littlewood pairing, and the circle \(L\log L\to L^1\) consequence. The source covers the real-line Hilbert transform, the periodic conjugate function, and the stated odd homogeneous kernels; it does not establish arbitrary-dimensional coordinate-Riesz weak type or a vector-valued endpoint bound. Keep its \(L^1(S^{n-1})\) angular factor and model assumptions explicit.

## Local check

../../../../../scope/source_snapshot/workers/W25/reader_batches/L01_B8/math/check_b8_identities.py computes the interval-transform distribution by solving the four regions separated by \(0\) and \(a\): the two exterior pieces contribute \(2a/(e^{\pi y}-1)\), the two interior pieces \(2a/(e^{\pi y}+1)\), totaling \(2a/\sinh(\pi y)\). It also checks inversion to \(f^*(t)=\pi^{-1}\operatorname{arsinh}(2a/t)\) and the derivative identity used in the \(f^*\)-to-\(f^{**}\) integration-by-parts conversion. This is symbolic algebra, not a proof of the paper’s analytic estimates.
