# OpenAI assembly and Hochschild averaging references (Wave 4 geometry-a-1)

## Finite witness recovery through the reduced-algebra route

**Scoped reference.** *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI (23 September 2026), physical pp. 1, 5, 59, 63, 67, 70, 80, and 83, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf), SHA-256 `df8d9301aa6d0306d7ac652e989c37a3c46b4c2285944694b746449157fc6714`.

The source's reusable dependency ledger is ordered: construct the geometric detector, obtain its integral detector, pass it through reduced-algebra Bott cancellation, and recover a finite witness from the quotient class.  Each transition requires the stated detector, quotient, reduced-norm, and Bott data.  Use it to organize a proposed finite-witness transfer; it is not a stand-alone algorithm for arbitrary assembly maps.

## Random-walk averaging and central-cut homotopy

**Source.** *Vanishing of higher bounded Hochschild cohomology*, OpenAI (23 September 2026), physical pp. 19–25, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf), SHA-256 `56ec913df9fbe4a2daf371eec1cb06ddc5b544cf9defc838aab540f33171f753`.

For a bounded \(k\)-cochain \(\Phi\) and the source's symmetric countably supported measure \(\mu=\sum_sp_s\delta_{u_s}\), define
\[
 (P\Phi)(a,x)=\sum_sp_s\Phi(a,xu_s)u_s^*,\qquad
 F_n=\frac1n\sum_{j=0}^{n-1}P^jf.
\]
The source uses a pointwise ultraweak cluster point \(F\), with \(PF=F\), and evaluates at \(1\) to obtain a primitive from the exact averaged coboundary identity.  Under the stated type-II\(_1\), separate normality, and Fourier-arc boundary assumptions it obtains \(g\) with \(dg=f\) and \(\|g\|\le\|f\|\).

For a central projection \(z\), its cut/homotopy interface is \(\operatorname{cut}_z\psi(a_1,\ldots,a_n)=\psi(za_1,\ldots,za_n)\) and \(d(J_z\psi)=\psi-\operatorname{cut}_z\psi\), with \(\|J_z\psi\|\le(k-1)\|\psi\|\).  Preserve the coefficient bimodule and centrality assumptions.
