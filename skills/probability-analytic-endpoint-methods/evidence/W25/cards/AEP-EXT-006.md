> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-006 — Ji Li and Brett D. Wick, weak factorization of (H^1(\mathbb R^n))

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/390b9445e47bb348-AEP-EXT-006.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and scope read

- Complete author preprint arXiv:1603.02699v2, dated 19 March 2016, 12 physical pages, all read through terminal references. The corresponding published work is *Canadian Mathematical Bulletin* 60(3) (2017), 571–585, DOI [10.4153/CMB-2017-033-9](https://doi.org/10.4153/CMB-2017-033-9); the acquired PDF is the arXiv v2 preprint, not the publisher layout.
- Official records: [arXiv](https://arxiv.org/abs/1603.02699) and [Cambridge](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/weak-factorizations-of-the-hardy-space-h1n-in-terms-of-multilinear-riesz-transforms/22B9523879F976D53D835726F448D829).

## Definitions and main factorization

The source defines an (m)-linear Calderón–Zygmund kernel (K(y_0,\ldots,y_m)), away from the diagonal, with size and coordinatewise Hölder regularity estimates (1.1)–(1.2) (printed pp.2–3). It assumes the associated (T:L^{p_1}\times\cdots\times L^{p_m}\to L^p) boundedness for (p_i>1), (p\geq1), and (1/p=\sum_i1/p_i). The printed p.2 homogeneity discussion has two defects and is not adopted literally: it calls (T) (m)-linear but writes (T(1_{B_0},\ldots,1_{B_m})), with (m+1) indicator inputs; and its stronger fixed-sign pointwise kernel bound is printed at scale (M^{-mn}) without the (r^{-mn}) factor expected for a kernel homogeneous of degree (-(mn)). These are isolated as source-print issues, not silently repaired. The p.4 multilinear Riesz example integrates an (m)-input kernel over (m) balls, where the factor (r^{-mn}) from the kernel cancels their product volume (r^{mn}); that calculation does not validate the malformed generic p.2 definition.

Define the partial commutator ([b,T]_l) and product
\[
\Pi_l(g,h_1,\ldots,h_m)=h_lT_l^*(h_1,\ldots,g,\ldots,h_m)-gT(h_1,\ldots,h_m)
\]
with the (l)-th partial adjoint as in (1.4)–(1.6), p.3. Theorem 1.3 (pp.3–4) is printed under the source's (mn)-homogeneity premise; because of the p.2 defects above, the card's operational proof route instead requires the actual denominator condition detailed below. Under a valid such input, every (f\in H^1(\mathbb R^n)) admits an (H^1)-convergent series
\[
f=\sum_{k,s}\lambda_{ks}\Pi_l(g_{ks},h_{ks,1},\ldots,h_{ks,m}),
\]
where (\lambda\in\ell^1), (g_{ks}\in L^{p'}), (h_{ks,j}\in L^{p_j}), (p_i>1), (p\geq1), and reciprocal exponents sum to (1/p). The infimum of the summed products of input norms is equivalent to (|f|_{H^1}). The paper also proves the corresponding BMO/commutator characterization (Theorem 1.4), with the reverse implication additionally requiring local (L^q) membership for some (q>1) and the stated homogeneity (pp.4–5).

## Constructive proof chain (§2, printed pp.5–10)

1. Proposition 2.1: each (\Pi_l) has mean zero; (H^1)–BMO duality plus the multilinear commutator BMO estimate bounds its (H^1) norm by the product of the input norms (pp.5–6). This yields the easy norm direction.
2. Lemma 2.2: a mean-zero function controlled by two separated radius-one ball indicators has (H^1) norm (\lesssim\log M), proved through the maximal-function definition and the annular integral (p.6).
3. Theorem 2.3 constructs a factorization of a mean-zero (H^1) atom supported on (B(x_0,r)). Choose the displayed separated equal-radius balls; set (g=1_{B_l}), (h_j=1_{B_j}) for (j\ne l), and (h_l=a/D_l), where the denominator actually used is
   (D_l=T_l^*(h_1,\ldots,g,\ldots,h_m)(x_0)=\int_{B_1\times\cdots\times B_m}K(y_l,y_1,\ldots,x_0,\ldots,y_m)\,dy_1\cdots dy_m).
   On p.7 the source asserts “(T_l^*) is homogeneous” and then writes (|D_l|\geq C M^{-mn}) in (2.2), without proving that inheritance. Accordingly the usable proof interface requires this actual partial-adjoint denominator lower bound directly, uniformly for the ball configurations used for atoms; the malformed p.2 statement alone does not certify it. Given (|D_l|\geq cM^{-mn}), the exponent relation (1/p'+\sum_j1/p_j=1) cancels all powers of the atom radius (r), leaving the factor (M^{mn}) (pp.6–7).
4. The error (a-\Pi_l(g,h_1,\ldots,h_m)) is split into its part on the atom ball and its separated-ball part. Kernel Hölder regularity and the atom's zero mean give an (M^{-\epsilon}r^{-n}) pointwise bound. Its (H^1) norm is then (\lesssim (\log M)M^{-\epsilon}) by Lemma 2.2 (pp.7–8).
5. Choose (M) large enough that this error coefficient is below a fixed (\delta<1), then atom-decompose the residual and iterate. The resulting geometric series gives the claimed (\ell^1) representation and the reverse norm bound; summing the atomic decomposition proves Theorem 1.3 (pp.8–10). The paper notes the (p<1) issue as open; do not extend the theorem to it.

Theorem 1.4's upper commutator estimate invokes established multilinear results; its lower direction is derived from factorization and duality (pp.10–11). Its printed reverse-direction homogeneity premise is subject to the same p.2 source caveat: use that lower characterization only after the factorization proof's actual denominator condition has been independently established. The final page is references (p.12).

## Direct denominator criterion and checked example

For a concrete sufficient condition avoiding the p.2 arity/scale defect, fix (l), an atom ball (B_0=B(x_0,r)), and the (m) input balls (B_j=B(x_j,r)) used in the p.7 construction. If the partial-adjoint integrand has constant sign on their product and
\[
 |K(y_l,y_1,\ldots,x_0,\ldots,y_m)|\geq c(Mr)^{-mn}
 \quad (y_j\in B_j),
\]
then direct integration gives (|D_l|\geq c|B(0,r)|^m(Mr)^{-mn}=c\omega_n^mM^{-mn}). For a complex kernel it suffices that one fixed phase (\theta) satisfies (\operatorname{Re}(e^{-i\theta}K)\geq c(Mr)^{-mn}) throughout the product. This is an independently verified sufficient interface, not a correction attributed to the source's malformed stronger condition.

It is nonempty even in the source's Riesz family: for (m=n=1), take (K(x,y)=(x-y)/|x-y|^2=1/(x-y)), (x_0=0), (r=1), and (B_1=(M-1,M+1)) with (M>10). The partial-adjoint integrand (K(y,x_0)=1/(y-x_0)) has a fixed positive sign and
\[
 |D_1|=\int_{M-1}^{M+1}\frac{dy}{y}=\log\frac{M+1}{M-1}\geq\frac2M.
\]
Thus the denominator is directly checked for this one-dimensional linear configuration; the general factorization route still requires the bound for every relevant atom-ball configuration with uniform constants, alongside the source's other CZ and exponent assumptions.

## Tool use and boundary

This is a structural (H^1) factorization and (H^1\leftrightarrow\mathrm{BMO}) duality interface when the target has the same multilinear CZ and boundedness hypotheses and one independently verifies the partial-adjoint denominator lower bound used in (2.2) for all required atom configurations. The p.2 source definition and p.7 inheritance sentence are not accepted as proof of that condition. The concrete (m=n=1) example above verifies only its stated configuration. This route does not prove weak type ((1,1)), a distribution-function estimate, or a sharp coordinate/vector Riesz (L^p) bound. In particular, the “weak” in weak factorization refers to the bilinear building-block decomposition, not weak-(L^1).

## Reading evidence

All 12 physical pages, including the bibliography, were extracted and read sequentially; the proof/definition pages were rendered and visually checked against the text. See `evidence/W25/reading_coverage.json`, `evidence/runtime_assets/d78875732b570186-AEP-EXT-006.txt`, and `evidence/runtime_assets/6740ea02f54d0ad5-check_b10_claims.json` for page map and exact radius-exponent check.
