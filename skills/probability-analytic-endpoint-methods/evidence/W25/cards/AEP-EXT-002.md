> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-002 — Shigeki Yano, “An Extrapolation Theorem”

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/ae4c02eec66e8076-AEP-EXT-002.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and scope read

- Official published J-STAGE scan: *Journal of the Mathematical Society of Japan* 3(2) (1951), printed pp. 296–305; 10 physical PDF pages; DOI [10.2969/jmsj/00320296](https://doi.org/10.2969/jmsj/00320296).
- The official article record now separates the title and subtitle as “Notes on Fourier Analysis (XXIX)” / “An Extrapolation Theorem”; the scan has the same two lines. J-STAGE's 2006 correction notice also corrects bibliographic metadata. The scan's reference [4] on printed p.304 says 1838, while the official record's correction metadata says 1938; this card does not silently edit the scanned bibliography.
- Entire article read: physical pages 1–10, including every application and terminal references. It is a one-dimensional finite-interval paper; the author's remark allows finite-total-measure source and target spaces.

## Theorem and exact inputs

The main theorem is stated on pp.296–297. Let T send real integrable functions on a finite interval (a,b) to measurable functions on that interval. The source assumes:

1. For each countable decomposition `f = Σ_v f_v`, `|Tf| ≤ Σ_v |Tf_v|` (subadditivity in modulus).
2. `|T(-f)| = |Tf|`.
3. For every `1<p<2`, `||Tf||_p ≤ A_p||f||_p`, with `A_p ≤ A(p−1)^(−k)` for some `k>0`; the constants are controlled by the interval length as stated on p.296.

Then
\[
 \int_a^b |Tf|\,dx\leq A_k\int_a^b |f|\log^k(1+|f|^2)\,dx+B_k,
\]
where the constants depend only on `k` and `b−a`. This is an (L\log^k L\to L^1)-type estimate with an additive finite-measure constant; it is not a weak-(L^1) estimate.

## Proof chain actually present in §§2–3

- Reduce to (f\geq1): split the signed function into nonnegative and nonpositive parts, add constants to make two functions at least one, and use assumptions 1–2 (printed p.297).
- Partition into dyadic level sets (E_v=\{2^v\leq f<2^{v+1}\}), set (f_v=f1_{E_v}) and (\phi_v=2^{-v}f_v). Subadditivity reduces the integral of (|Tf|) to a sum over levels (pp.297–298).
- For levels (v\geq2), choose (p_v=1+1/v) and its conjugate (q_v=v+1). Hölder and the (A_{p_v}\lesssim(p_v-1)^{-k}=v^k) bound produce a level contribution proportional to (2^v v^k(\int\phi_v)^{v/(v+1)}), up to interval-length constants (printed p.298). The exponent is (v/(v+1)), not (1/(v+1)).
- The p.298 footnote gives the unweighted Young comparison (a^{v/(v+1)}\leq 2a+v^{-2}) for (a>0), (v\geq1); this alone does not control the remainder after multiplication by (2^v v^k). The following is an independent completion of that proof step, not a claim that the source spells it out. Put (\alpha=v/(v+1)). Calculus gives
  (\sup_{t\geq0} 2^v v^k(t^\alpha-A t)=\frac{2^v v^k}{v+1}(\frac{v}{(v+1)A})^v).
  For example, (A(k)=2\exp((k+2)/e)>2) makes this at most (v^{-2}) for all integers (v\geq2): the right side is bounded by (v^k(2/A)^v), and (\log v\leq v/e) for (v\geq2). Therefore the weighted level term is bounded by (A(k)2^v v^k\int\phi_v)+v^{-2}; summing the first term gives the stated (f\log^k(1+f^2)) control, and the remainder is summable.
- The level formula (p_v=1+1/v) is only used for (v\geq2), because the theorem assumes (1<p<2). Treat (v=0,1) separately with one fixed (p_0\in(1,2)): those two level pieces are bounded and supported on a finite-measure space, so the assumed (L^{p_0}\to L^{p_0}) estimate and Hölder give finite contributions. This avoids using (p=2) at (v=1) or an undefined exponent at (v=0).
- The finite-measure-space extension is explicitly stated in the p.298 remark. It does not remove the operator hypotheses.
- §3 applies the result to conjugate functions and truncated conjugate functions, the Hardy–Littlewood maximal operator, double Fourier series, differentiation of multiple integrals, Marcinkiewicz's function, trigonometric interpolation, and Walsh–Kaczmarz series (pp.298–305). Each application invokes the corresponding (L^p) growth facts; the theorem alone does not establish them.

## Tool use and boundary

For a scalar coordinate/operator, this is a possible route from a verified near-(p=1) (L^p\to L^p) blow-up rate ((p-1)^{-k}) to an Orlicz (L\log^k L\to L^1) conclusion, only after checking the countable-decomposition and sign assumptions and the actual finite-measure formulation. The weighted remainder and the two lowest dyadic levels require the independent completion just stated; they are not justified by the printed footnote alone. It supplies neither a distribution-function bound nor uniform weak-(1,1). Do not use it as a vector-valued Riesz endpoint proof without independently verifying its hypotheses for the vector-valued operator and adapting the range statement.

## Reading evidence

All ten physical pages were text-extracted and read in order, including pp.301–305 applications/references. Theorem/proof pages 1–4, p.10 identity, and p.3 footnote were rendered; the footnote received a high-resolution visual crop. Page-level coverage and extraction are in `evidence/W25/reading_coverage.json` and `evidence/runtime_assets/50975f6d44b6f11b-AEP-EXT-002.txt`.
