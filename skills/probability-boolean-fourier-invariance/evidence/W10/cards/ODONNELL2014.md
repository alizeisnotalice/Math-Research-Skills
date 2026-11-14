# M0145 — O’Donnell, *Analysis of Boolean Functions*

**Source.** Ryan O’Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014; arXiv edition 2021), 419-page PDF. Local PDF identity and publisher DOI 10.1017/CBO9781139814782 were checked.

## Selected sections read

- **Chapter 1, §§1.2–1.4 (PDF pp. 20–27).** Every real-valued cube function has a unique multilinear expansion \(f(x)=\sum_S\hat f(S)\chi_S(x)\); the parity characters are an orthonormal basis under the uniform measure, \(\hat f(S)=\mathbb E[f\chi_S]\), and Parseval gives \(\mathbb E[f^2]=\sum_S\hat f(S)^2\). The variance is the sum over nonempty sets.
- **Chapter 2, §§2.2–2.4 (PDF pp. 46–56).** For Boolean \(\pm1\)-valued \(f\), \(\mathrm{Inf}_i(f)=\Pr[f(x)\ne f(x^{\oplus i})]=\mathbb E[(D_i f)^2]=\sum_{S\ni i}\hat f(S)^2\). For monotone Boolean \(f\), \(\mathrm{Inf}_i(f)=\hat f(\{i\})\); do not use this monotone identity for a general function. Total influence is average sensitivity and \(\mathrm{Inf}(f)=\sum_S|S|\hat f(S)^2\). Noise sensitivity at flip rate \(\delta\) obeys \(\mathrm{NS}_\delta(f)=\frac12(1-\mathrm{Stab}_{1-2\delta}(f))\), with \(\mathrm{Stab}_\rho(f)=\sum_S\rho^{|S|}\hat f(S)^2\).
- **Chapter 9, §9.6 (PDF pp. 265–269).** KKL gives \(\max_i\mathrm{Inf}_i(f)\ge\mathrm{Var}(f)\,\Omega(\log n/n)\). The section also gives an \(O(n/\log n)\)-coordinate monotone bribery/forcing consequence. That coalition bound has different quantifiers and scale from Friedgut's fixed-error small-tribe conjecture.
- **Chapter 11, §§11.6–11.7 (PDF pp. 357–370).** The Basic Invariance Principle assumes independent coordinate sequences with matching first three moments, zero third moment, and bounded fourth moment \(\mathbb E[z_i^4]\le9\); for degree-\(k\) multilinear \(F\) and \(C^4\) test \(\psi\), the expectation error is at most \(\frac{C}{12}9^k\sum_i\mathrm{Inf}_i(F)^2\). If \(\mathrm{Var}(F)\le1\) and all influences are at most \(\epsilon\), this is \(O(Ck9^k\epsilon)\); a smooth approximation yields an \(O(c)2^k\epsilon^{1/4}\) bound for \(c\)-Lipschitz tests. Corollary 11.69 gives a smoothed/no-notable-coordinate variant; Theorem 11.71 adds Gaussian anti-concentration to get cdf closeness. The Majority Is Stablest discussion applies invariance after smoothing and invokes Borell's Gaussian isoperimetric inequality; it keeps the small-influence/notable-coordinate premise explicit.

These are selected complete sections, not complete chapters or a full-book read. Use MOO (2010) as the primary source for product-ensemble invariance hypotheses and theorem variants. A small maximum Fourier coefficient does not replace the maximum-individual-influence hypothesis.

**Reading status:** partial; local PDF, selected sections above only.
