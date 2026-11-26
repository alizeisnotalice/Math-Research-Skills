# Matrix-to-convex-body metric-entropy conversion

**Source.** OpenAI, *Counterexamples to the duality conjecture for metric entropy*, Theorem 1.1 and Lemma 2.1, PDF pp. 1, 4--5; SHA-256 `6d6f9d0518a6e50da9bb3c026ec384b22edd12a2f112eec67832c76b62c9c8f7`.

## Input contract

Take finite nonempty sets `X,Y`, real functions `g_y:X -> R`, row vectors `R_x in R^Y`, and the absolute-convex column class `f_lambda` for `||lambda||_1<=1`.  Require row separation `||R_x-R_x'||_infty>=1` for distinct rows and a uniform `epsilon`-approximating list of size `M` for every `f_lambda`.  Choose `t>0`.

## Reuse

Set `K=3 absconv{R_x:x in X}+t B_infty^Y` and `L=B_infty^Y`.  Lemma 2.1 gives full-dimensional origin-symmetric convex bodies and
`N(K,L)>=|X|`, `N(L^circ,(6 epsilon+2t)K^circ)<=M`.
The second cover must choose representatives inside the actual coefficient ball; this controls the added cube through the support-function identity.

The construction is finite-dimensional and matrix-specific.  It does not give Pietsch duality, a fixed-dimensional counterexample, or a cover with centers constrained to the covered body.

## 固定来源

- 物理页 1, 4, 5。Theorem 1.1; Lemma 2.1 SHA-256 `6d6f9d0518a6e50da9bb3c026ec384b22edd12a2f112eec67832c76b62c9c8f7`。[Counterexamples to the duality conjecture for metric entropy](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf)
