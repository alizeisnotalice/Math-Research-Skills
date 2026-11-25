# Negative example: three false substitutions

### Dependence is not a singleton coefficient

Parity \(f(x)=\prod_{i=1}^n x_i\) depends on all (n) coordinates and has one nonzero Fourier coefficient, at (S=[n]). Every coefficient \(\hat f(\{i\})\) is zero. It therefore separates dependence on every variable from the A165 hypothesis; it does not refute A165.

### Small Fourier coefficients are not low individual influence

The MOO Majority Is Stablest theorem assumes a bound on each \(\mathrm{Inf}_i(f)=\sum_{S\ni i}\hat f(S)^2\). The premise \(\max_S|\hat f(S)|\to0\) bounds each summand, not their coordinate-wise sum. Do not substitute the latter without a proven quantitative inequality under the problem's other assumptions.

### A continuous-cube coalition theorem is not the discrete tribe conjecture

Chattopadhyay–Gurumukhani's 2026 bound is (O(n/\sqrt{\log n})) for a finite-alphabet/continuous-cube model. Friedgut's 2004 discrete Conjecture 2.6 asks for (O_{c,\epsilon}(\log n)) coordinates when all Boolean-cube individual influences are at most (c\log n/n), and asks for a fixed conditional bias (1-\epsilon). Replacing (o(1)) by a fixed \(\epsilon\), or switching the domain, changes the statement.

### A nonzero singleton coefficient is not coordinate influence

On the uniform cube with Walsh basis \(\chi_S(x)=\prod_{i\in S}x_i\), the three-bit parity \(f(x)=x_1x_2x_3\) has \(\widehat f(\{i\})=0\) for all \(i\), but \(\mathrm{Inf}_i(f)=1\) for every coordinate. For a \({0,1}\)-valued output, use the factor-four influence identity under this normalization. A165's nonzero-singleton premise and a low-influence hypothesis must never be swapped.

### Accepted source uses do not certify the full headline

- BGP's finite \(k\)-wise LP dual and two-level-majority result do not solve its iterated-majority Question 4. Keep every mixed marginal in the reviewed block-count lift; matching only the total-count moments enlarges the feasible set.
- KKL's random-CNF construction gives an asymptotic density regime. It does not supply an exact finite construction for every real target density \(\alpha\), and its random formula need not be monotone or have small maximum coordinate influence.
- CG's direction-switching existence conclusion additionally needs the named Hatami theorem and its hypotheses; the supplied-coalition back-transfer is proved by the encoding itself. Its resampling influence is not the forced-flip influence.
- Kane's admitted estimate is for a positive-kernel smoothed Taylor remainder. Polynomial moment matching alone does not imply a sign-probability bound; include the zero-set boundary and kernel-tail terms. The reviewed interface does not certify the full headline exponent.
