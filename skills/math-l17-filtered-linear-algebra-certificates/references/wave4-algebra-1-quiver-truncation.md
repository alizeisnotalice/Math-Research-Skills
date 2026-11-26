# Wave 4 algebra-1: quiver flavor base change and finite truncation

OpenAI, *The equivariant cohomological Hikita conjecture for arbitrary quivers*, SHA-256 `9f66ad939e0e51ecbe116ea72084ecef9f1121c6fea1cc733c7dde6d70b3e47b`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/main.pdf), physical pp. 6--8, Lemmas 2.1--2.4 and Proposition 2.2.

After deleting zero-dimensional vertices, the source defines `B_F=A_F/<A_F(d):d!=0>`. Its minuscule expression is the finite Weyl sum
`M_{lambda,p}=sum_{lambda' in W lambda} e^{lambda'}p^{lambda'} prod_beta beta(-<beta,lambda'>)_+ / eu_T(T_{t^{lambda'}}Gr_lambda)`.
For a flavor-torus map `F -> F'`, Lemma 2.3 states `A_{F'} tensor_{H^*_{F'}(pt)} H^*_F(pt) = A_F` and the corresponding identity for `B`, respecting convolution and gradings. The proof filters affine Grassmannians by bounded unions of orbits, truncates section lattices, and uses even equivariant homology so that no Tor term enters finite exact sequences.

Use L17 only for supplied finite truncation matrices, grading tables, and exact base-change/rank calculations. It cannot construct Borel--Moore homology, prove evenness/freeness, stabilize truncations, derive localization Euler factors, or prove Hikita's conjecture.
