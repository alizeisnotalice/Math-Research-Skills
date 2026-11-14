> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-011 — Adam Osękowski, weak Fourier multipliers and the Beurling–Ahlfors transform

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/4c3b2dd5c0b52f33-AEP-EXT-011.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


## Identity and scope read

- Official J-STAGE published version: *Journal of the Mathematical Society of Japan* 66(3) (2014), 745–764, DOI [10.2969/jmsj/06630745](https://doi.org/10.2969/jmsj/06630745); 20 physical PDF pages, all read through terminal page 764 and references. [Official article record and correction/revision field](https://www.jstage.jst.go.jp/article/jmath/66/3/66_745/_article/-char/en) lists free access and no revised/correction notice.

## Exact multiplier and martingale statements

The multiplier symbol (1.4), printed pp.746–747, is built from a Lévy measure (\nu) on (\mathbb R^d), a finite measure (\mu) on the unit sphere, and Borel coefficients (\phi,\psi) valued in the complex unit disk. The Lévy integrability condition is (\nu(\{0\})=0), (\int\min(|x|^2,1)\,d\nu<\infty). Theorem 1.2 states a weak-(p,p) estimate for this symbol class for (1<p<\infty), but the printed first-branch normalization has a source-level mismatch detailed below. This does not include (p=1).

For the martingale input (printed pp.748–751), the probability space is complete, the filtration is complete/right-continuous as specified, and (F_0) contains all null events. (X,Y) are adapted Hilbert-valued càdlàg martingales, with differential subordination meaning ([X,X]_t-[Y,Y]_t) is nonnegative and nondecreasing. The norm is (\|X\|_p=\sup_{t\ge0}\|X_t\|_p). Theorem 2.1 (p.749) states
\[
 \|Y\|_q^q\leq C_q\|X\|_1\|X\|_\infty^{q-1},\quad1<q<\infty,
\]
with sharp (C_q=2^{1-q}q/(q-1)) for (1<q\leq2), and (C_q=\Gamma(q+1)/2) for (q>2). The proof uses the integrated Burkholder function (V_q), its lower bound (V_q(x,y)\geq |y|^q-C_q|x|) on (|x|\leq1), submartingale/expectation inequalities and scaling (pp.750–751). The (v_\infty) argument is stated for (X\in L^2); retain that proof condition where used.

## Fourier multiplier proof route (§3, pp.751–758)

- Approximate the Lévy measure by finite-jump measures. Construct a compound-Poisson Lévy process with exponential waiting times and independent jumps, then its natural filtration. The parabolic extension (U f(s,x)=\mathbb E f(x+X_s)) gives a martingale (F); modulating jumps by φ and compensating gives (G).
- Lemma 3.1 proves the martingale property and differential subordination when (|\phi|,|\psi|\leq1). A bilinear pairing identifies the associated multiplier with the transform of these processes.
- Theorem 2.1, Hölder, and Fubini produce the dual weak bound for bounded inputs. Let the time parameter tend to (-\infty); Plancherel gives (L^2) convergence, then an almost-everywhere subsequence and Fatou pass the estimate to the multiplier. General Lévy measures and Brownian/spherical components are obtained by the explicit approximation on p.757.
- Theorem 3.4 (p.758) has a structured (\mathbb C^N)-valued output version with coefficient functions valued in the unit ball of (\mathbb C^N); this is an auxiliary vector weak-(p) result for that symbol construction, not a sharp strong-(L^p) vector Riesz theorem.

## Source-print mismatch in Theorem 1.2 (printed p.748)

The theorem defines
\[
K_p=\left[\tfrac12\Gamma\!\left(\tfrac{2p-1}{p-1}\right)\right]^{(p-1)/p},\quad1<p<2,
\]
then uses (K_p) as the coefficient in the *measure* inequality (|\{|T_mf|\ge1\}|\le K_p\|f\|_p^p), and says the weak operator norm is (K_p^{1/p}). However the dual argument (Eq. (3.6), p.758) gives the measure coefficient (C_{p'}^{1/(p'-1)}=[\frac12\Gamma((2p-1)/(p-1))]^{p-1}). Its (p)-th root is exactly the first-branch formula printed in the abstract. Thus the printed theorem appears to use the abstract weak-norm factor where the distribution coefficient belongs; retain this source discrepancy and do not silently “correct” the paper or claim the source proof verifies the printed first branch. For (p\ge2), the printed measure coefficient (p^{p-1}/2) agrees with the dual calculation.

Concrete exact check at (p=3/2): (p'=3), (C_3=\Gamma(4)/2=3); Eq. (3.6) gives measure coefficient (3^{1/2}), whereas p.748 prints (3^{1/3}) as (K_p). The printed weak norm after taking the theorem's extra (p)-root would be (3^{2/9}), while the abstract/dual-derived norm factor is (3^{1/3}). This exposes an exponent inconsistency, not a counterexample to the multiplier theorem. The script `evidence/runtime_assets/49e32d2bd70c4adf-check_b10_claims.py` verifies these exact expressions symbolically.

## Section 4 and tool boundary (pp.758–764)

Section 4 applies the method to the Beurling–Ahlfors transform. It gives upper bounds from real and imaginary parts, a complex bound, explicit lower examples for (1<p\le2) using (w(z)=\bar z\log|z|^2\,1_{|z|<1}), and radial piecewise constructions for (p\ge2); Corollary 4.4 supplies a lower bound for the multiplier class. These are bounds, not a resolution of the conjectured exact Beurling–Ahlfors (L^p) norm.

Use only as a conditional route for the exact Lévy-symbol multiplier class and (1<p<\infty), keeping the first-branch normalization mismatch visible. Although Theorem 3.4 is a vector-output weak-type statement for a structured symbol, it does not upgrade the separate sharp vector strong-(L^p) C207 question. No (p=1) weak endpoint is established.

## Reading evidence

All 20 physical pages were text-extracted and read sequentially, including terminal references/affiliation. The p.4 normalization, martingale theorem, duality step, and final construction pages were rendered; p.4 and p.13 proof formulas were inspected at high resolution. Full page coverage and extraction: `evidence/W25/reading_coverage.json` and `evidence/runtime_assets/7ffa09da84fce5a0-AEP-EXT-011.txt`.
