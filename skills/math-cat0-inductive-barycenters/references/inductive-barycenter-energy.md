# Inductive-barycenter energy decay

## Source and admitted scope

The transfer is Lemma 5.3, physical PDF p. 28, in *A hyperbolic group with no geometric CAT(0) action* (OpenAI Math, pinned PDF SHA-256 `124f55b0821cc7f18c1b64600b5e5157d939bbc4a6f66294dc1456fc633eb264`, 43 pages, [official pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf)). This card extracts only its finite complete-CAT(0)-metric-cone statement. It does not transfer the paper's geometric-action hypotheses, conditional table coupling, uniform displacement estimate, ultralimit, or no-CAT(0)-action conclusion.

## Statement

Let `C` be a complete CAT(0) metric cone with vertex `0`. Let `V` have finite support, barycenter `0`, and `E||V||^2=sigma2<infinity`. For independent copies, set `m_1=V_1` and `m_j=[m_(j-1),V_j]_(1/j)`. Then

`E||m_t||^2 <= sigma2/t`.

For every deterministic list `V_1,...,V_t` and fixed `h` in the cone tangent geometry,

`(1/t) sum_j <h,V_j> <= <h,m_t>`.

The scalar-product convention is the cone one; do not replace it by an arbitrary bilinear form.

## Independent derivation

The cone geodesic identity is

`||[u,v]_a||^2=(1-a)||u||^2+a||v||^2-a(1-a)d(u,v)^2`.

The barycenter variance inequality at `0` gives, conditionally on `m_(j-1)=u`,

`E[d(u,V_j)^2 | u] >= ||u||^2 + sigma2`.

Putting `a=1/j` in the identity and taking expectations therefore yields, with `A_j=E||m_j||^2`,

`A_j <= ((j-1)^2/j^2) A_(j-1) + sigma2/j^2`.

Since `A_1=sigma2`, induction gives `A_j<=sigma2/j`. Concavity of `u -> <h,u>` along cone geodesics gives the displayed deterministic average inequality by the same induction. No assertion follows when the supplied barycenter or independence condition is absent.

## Exact Euclidean replay

For Euclidean vectors the recursive mean equals the arithmetic sample mean. The bundled replay enumerates a finite support with rational coordinates and weights, checks zero arithmetic mean, and reports the exact equality `E||m_t||^2=sigma2/t`. This validates that special case only; it does not numerically certify CAT(0) barycenters or the variance inequality.
