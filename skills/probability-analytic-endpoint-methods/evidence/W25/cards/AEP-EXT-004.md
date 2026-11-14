> Final W25 mother30 binding: R01 approved this source as one of 30 distinct works (686 pages total). The final skill-scope/release review remains pending. Mathematical claims and source-specific caveats below are preserved from the bound card; exact approval is in ../source_approval_matrix.json.

# AEP-EXT-004 — A variant of Yano’s extrapolation theorem on Hardy spaces

**Mother mirror status:** R01 final mother30 source binding approved; this source contributes one of the 30 accepted works. This card mirrors `evidence/runtime_assets/c189384ba09eb230-AEP-EXT-004.md`; its mathematical statements and scope limits remain those of that reviewed helper card.


**Reader/batch:** L15 / W25-L15-B11. **Status:** complete article read; R01 stage review passed. R01 final mother30 source binding is approved; the source counts once in the 30-source inventory.  
**Identity:** Odysseas Bakas, *Archiv der Mathematik* 113 (2019), 537–549, DOI [10.1007/s00013-019-01366-x](https://doi.org/10.1007/s00013-019-01366-x). Springer OA PDF, 13 physical pages.  
**PDF:** ../../../../../scope/source_snapshot/downloads/D04/analytic_B4/papers/analytic-AEP-EXT-004-Bakas-Hardy-Yano.pdf  
**SHA-256:** 61a7eebbaac59ba9c4d17480a40f844f423fe3fb2831826500c50c6c6f35b656  
**Text/render evidence:** text/AEP-EXT-004.txt; all physical pages rendered to rendered/AEP-EXT-004-pNN.png. Theorem/proof formulas were visually checked on physical pp. 2, 4–8; sharpness and extension boundaries on pp. 9–11.

## Exact result and model

Theorem 1 (printed p. 538; physical p. 2) concerns a sublinear operator \(T\) on measurable functions over the one-dimensional torus \(\mathbb T\), with
\[
|T(f+g)|\le |T(f)|+|T(g)|,\qquad |T(\alpha f)|=|\alpha|\,|T(f)|
\]
for measurable \(f,g\) and complex scalars \(\alpha\). Assume fixed \(C_0,r>0\) satisfy, for every \(1<p\le2\),
\[
\sup_{\substack{g\in H^p(\mathbb T)\\ \|g\|_{L^p(\mathbb T)}=1}}
\|Tg\|_{L^p(\mathbb T)}\le C_0(p-1)^{-r}.
\]
Then a constant \(D=D(C_0,r)>0\) satisfies
\[
\|Tf\|_{L^1(\mathbb T)}\le D\|f\|_{L\log^r L(\mathbb T)}
\]
for every **analytic trigonometric polynomial** \(f\) on \(\mathbb T\). This theorem does not state the conclusion for arbitrary \(L\log^rL\) functions or nonanalytic inputs. The Orlicz class is given by integrability of \(|f|\log^r(1+|f|)\); its Luxemburg norm uses \(\Phi_r(x)=x([1+\log(x+1)]^r-1)\), and the paper records the equivalent rearrangement norm \(\int_0^1 f^*(t)\log^r(e/t)\,dt\) (physical p. 4).

## Proof map and dependencies

The self-contained proof is in §2 (printed pp. 540–544; physical pp. 4–8). It first proves the unnormalized estimate (2.1), then uses homogeneity/scaling to obtain the norm form of Theorem 1.

1. **Analytic replacement of layer pieces (physical pp. 4–5).** For \(\lambda>0\), set
   \[
   a_\lambda=\max\{1,(|f|/\lambda)^{1/3}\},\quad
   F_\lambda=(a_\lambda+iHa_\lambda)^{-1},\quad
   G_\lambda=1-(1-F_\lambda^4)^4,
   \]
   where \(H\) is the periodic Hilbert transform. The analytic-decomposition construction gives \(F_\lambda,G_\lambda\in H^\infty(\mathbb T)\) and, for an absolute \(A_0\),
   \[
   |G_\lambda|\le A_0|F_\lambda|^4\le A_0|F_\lambda|^3
   \le A_0\min(1,\lambda/|f|),\qquad |G_\lambda f|\le A_0\lambda.
   \]
   Define \(\widetilde f_0=G_1f\) and \(\widetilde f_n=(G_{2^n}-G_{2^{n-1}})f\) for \(n\ge1\). Since \(f\) is an analytic trigonometric polynomial, the decomposition is finite: for sufficiently large \(N=N(f)\),
   \(f=\sum_{n=0}^N\widetilde f_n\), with every piece in \(H^\infty\). This analytic replacement is essential: ordinary level-set pieces of analytic \(f\) need not be analytic, so the hypothesis on \(H^{p_n}\) could not be applied directly to them.

2. **Near-1 exponent allocation (physical pp. 5–6).** Put \(p_n=1+1/(n+1)\), so \(p_0=2\) and \(p_n\downarrow1\). Sublinearity, Hölder on the probability-normalized torus, and the hypothesis yield
   \[
   \|Tf\|_1\le C_0\sum_{n=0}^N(n+1)^r\|\widetilde f_n\|_{p_n}.
   \]
   The source uses \(|\widetilde f_n|\le A'_0 2^n\), then the elementary comparison
   \[
   t^{(n+1)/(n+2)}\le e^{r+2}t+(n+1)^{-(r+2)}
   \quad(t>0,\ n\ge0),
   \]
   to obtain \(\|\widetilde f_n\|_{p_n}\lesssim_r \|\widetilde f_n\|_1+(n+1)^{-(r+2)}\). The \(n=0\) term is controlled separately by (2.6).

3. **Logarithmic summability (physical pp. 6–8).** Split
   \(\int|\widetilde f_n|=I_n^{(1)}+I_n^{(2)}\) over \(\{|f|<2^{n-1}\}\) and \(\{|f|\ge2^{n-1}\}\). The high-value part uses \(|\widetilde f_n|\lesssim2^n\), Fubini, and that only \(n\lesssim\log_2(1+|f|)\) contribute, giving the \(L\log^rL\) bump. For the low-value part, the source expands \(G_{2^n}-G_{2^{n-1}}\), bounds it by squared defects of \(F_\lambda\), and reduces to \(I_n^{(1,\alpha)}\) and \(I_n^{(1,\beta)}\). Since \(a_{2^n}=1\) on \(|f|<2^{n-1}\), \(H(1)=0\), and \(H\) is \(L^2(\mathbb T)\)-bounded, the paper obtains
   \[
   I_n^{(1,\alpha)}\lesssim 2^{n/3}\int_{|f|\ge2^n}|f|^{2/3},\qquad
   I_n^{(1,\beta)}\lesssim 2^{n/3}\int_{|f|\ge2^{n-1}}|f|^{2/3}.
   \]
   Fubini and a geometric sum again yield \(1+\int |f|\log^r(1+|f|)\). Thus the proof needs only the \(L^2(\mathbb T)\) boundedness of the periodic Hilbert transform beyond the analytic decomposition estimates.

## Sharpness and explicit boundaries

- §3.1 (physical pp. 9–10) uses the Littlewood–Paley square function \(S\) to show the endpoint exponent is sharp: on analytic Hardy spaces its norm grows like \((p-1)^{-1}\) as \(p\downarrow1\), matching \(L\log L\). Without analyticity, the cited behavior is \((p-1)^{-3/2}\) and the endpoint is \(L\log^{3/2}L\); do not transfer the Hardy-space exponent to full \(L^p\).
- The second sharpness example uses a lacunary multiplier with
  \(\Lambda=\{3^k-3^m:0\le m\le k-1,\ k,m\in\mathbb Z\}\). Equations (3.1)–(3.5) give analytic \(H^p\) growth \((p-1)^{-1/2}\) and \(H^1\to L^1\) control by \(L\log^{1/2}L\). The \(\beta_N\) test on physical p. 10 yields output size \(\gtrsim N^{1/2}\) while its source Orlicz norm is \(\lesssim N^r\), forcing \(r\ge1/2\). These sharpness details use the cited lacunary-set estimates; they are separate from the proof of Theorem 1.
- §3.2 (physical pp. 10–11) extends the conclusion from analytic trigonometric polynomials to the full Hardy–Orlicz space only with the additional pointwise difference condition \(|T(f)-T(g)|\le |T(f-g)|\), together with density/unique-extension reasoning.
- §3.3 (physical p. 11) says a two-dimensional version follows from cited \(K\)-closedness for \((H^1(\mathbb T^2),H^\infty(\mathbb T^2))\). It records that corresponding \(K\)-closedness for \(\mathbb T^n\), \(n\ge3\), was open in the author's account. No general higher-dimensional extension is proved here.
- Physical pp. 12–13 are references and terminal publication matter. No external supplement or appendix is required for this complete article.

## Use boundary for the current Riesz-endpoint tool

This is a distinct paper from Yano's classical finite-measure theorem and from other papers about the range of Yano extrapolation: Bakas explicitly supplies an analytic-Hardy-space formulation and direct proof. It is a rigorous endpoint extrapolation result in its own model class. For the current scalar/vector Riesz weak-endpoint skill and isolated C208, however, it is an **eligible auxiliary endpoint-method source** for the broader analytic-endpoint tool: given the stated analytic \(H^p\) growth, Theorem 1 gives the stated \(L\log^rL\to L^1\) conclusion on analytic trigonometric polynomials. This eligibility does not assert a reduction from a Euclidean Riesz transform, a weak-\((1,1)\) estimate, or a dimension-independent C208 constant. R01 accepted the source binding; formal C208 mapping and resolution remain false, while the source counts once in the 30-source inventory.

## Local calculation evidence

computations/l15_b11_checks.py analytically locates the maximum of the paper's displayed scalar comparison \(t^{(n+1)/(n+2)}-e^{r+2}t\), then the local Python decimal run checks selected \(r\in\{0.5,1,2\}\), \(n\in\{0,1,2,5,20,100\}\). All tested maxima are below the printed allowance. This is finite arithmetic evidence only, not a proof for all \(r,n\), and does not verify the operator theorem.
