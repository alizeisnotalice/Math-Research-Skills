# Bounded-input-participation concentration

Source: *Correspondence coloring graphs with a forbidden clique*, Lemma 4.3, PDF pp. 22--23, [OpenAI Math commit `3344da59991ed94f9ba711217b29c1d760badfa6`](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf); local PDF SHA-256 `8809bcac3ea81e7bc15d75c6a034b1256af8fe042453f96004236fbbee2eed0e`.

Let `X_1,...,X_m` be bounded real functions of finitely many **independent** inputs.  Declare a dependence set for each function and an interval of length `b_j` containing its range.  If every input occurs in at most `p` declared dependence sets, with real `p >= 1`, then, for `a>0` and `sum_j b_j^2>0`,

`P(sum_j (X_j-E X_j) >= a) <= exp(-2a^2/(p sum_j b_j^2))`,

and the same bound holds for the lower tail.  If the sum of squared range lengths is zero, both events have probability zero.

For verification, the proof first applies the generalized Hölder/Finner inequality to nonnegative bounded `Z_j` with these dependence sets:

`E product_j Z_j <= product_j (E Z_j^p)^(1/p)`.

Conditioning on one independent input and Hölder over the functions that use it preserves the maximum participation bound; induction gives the display.  Hoeffding's range MGF estimate gives `log E exp(s(X-E X)) <= s^2 b^2/8`.  Apply the product inequality to `Z_j=exp(s(X_j-E X_j))`, use the MGF estimate at `p s`, and optimize exponential Markov at `s=4a/(p sum_j b_j^2)`.

The supplied checker verifies only the finite declaration: interval validity and the measured maximum incidence.  It cannot establish that a user-supplied function truly has the declared range/dependence set, nor independence of the base inputs.  This component does not transfer the paper's DP-coloring assumptions or theorem.
