# Jet matrices and ordered-chain bookkeeping

OpenAI, *Nagata's conjecture for plane curves*, physical pp. 3--4, Lemma 2.1; SHA-256 `42a8897d121e2fc0bff7fe5582ea60b4b2304d706658293fb380166f46c56879`; [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/main.pdf).

For fixed degree `e` and multiplicities `n`, the source encodes Taylor conditions at marked affine points as a matrix with one column per degree-`e` form and polynomial integer-coefficient entries in the point coordinates. A nonzero form is failure of full column rank, so the locus is cut out by full-size minors. Cyclic products then replace a very-general vector by an equal-multiplicity universal system while preserving `d/m <= sqrt(r)`.

OpenAI, *The generalized Mukai conjecture*, physical pp. 16--18, Theorem 6.1 and equality-case use; SHA-256 `0273a9c7907eb9d1ab3b3f99ff5668503c4db51764545764e91b03389e267317`; [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Generalized-Mukai-Conjecture-September-24-2026/article.pdf).

The stated ordered-chain interface takes proper irreducible components `V_1,...,V_k` of `RatCurves^n(Y)` with independent numerical classes and gives `dim Locus(V_1,...,V_k)_y >= sum_j(-K_Y.V_j-1)` when nonempty. The source then applies equality-case geometry.

Use the exact checker only for supplied finite jet matrices, incidence, or leading terms. It exposes exact rank/kernel witnesses but does not prove parameter-space closedness, general-point transfer, properness, curve-family independence, locus dimensions, or either main theorem. Both are source-scoped OpenAI-draft interfaces without independent proof audit.
