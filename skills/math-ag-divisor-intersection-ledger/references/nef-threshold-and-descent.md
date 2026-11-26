# Nef lines, monomial orders, and birational descent

This note records narrow interfaces stated in two OpenAI drafts pinned to `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`.

* *Numerical semiampleness of nef adjoint classes on compact Kähler manifolds*, SHA-256 `2f19b2f37c05dcf943a3ef1b859cb71c9e6692ca9bb0f794590ac6bd16a6ca88`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/numerical-generalized-abundance.pdf), physical p. 5, Lemma 2.1.
* *Fujita's freeness conjecture*, SHA-256 `73aefa0b0e5578dfba86cca2231608f2ba628519238cad062e49b3dc095be40b`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Fujitas-freeness-conjecture-September-23-2026/Fujitas-freeness-conjecture-September-23-2026.pdf), physical pp. 4--6, Lemmas 2.1--2.5.

For a modification `mu:Y -> X` of smooth compact Kähler manifolds, the first draft states that clearing denominators sends a rational line of zero real Chern class to `Pic^0(X)`, pullback identifies `Pic^0(X)` and `Pic^0(Y)`, and `mu_* O_Y=O_X` plus projection formula descends basepoint-freeness from a semiample pullback.

The Fujita draft fixes an SNC chart, divisors `E_j`, a valuation `v`, and weights `u_j=v(E_j)`. Its replacement keeps `v(D_i)=sum_j u_j ord_{E_j}(D_i)` and `A(v)>=sum_j u_j A(E_j)`. For a coherent ideal it uses `lct_x(a)=min_F A(F)/ord_F(a)`; its Lemma 2.5 descends a section of `pi^*P_V+C` when the positive part of integral `C` is exceptional.

Record the model, coefficients, pullback convention, normality, nefness and effectivity before use. The ledger rechecks only supplied finite rational coefficients and intersections. It does not compute `Pic^0`, a log resolution, lct, semiampleness, or either paper's main theorem. These are source-stated OpenAI-draft interfaces, without an independent proof audit.
