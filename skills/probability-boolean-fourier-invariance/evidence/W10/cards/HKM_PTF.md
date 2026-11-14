# HKM-PTF — sensitivity bounds for polynomial threshold functions

**Source.** Prahladh Harsha, Adam Klivans, and Raghu Meka, “Bounding the Sensitivity of Polynomial Threshold Functions,” *Theory of Computing* 10 (2014), 1–26, DOI 10.4086/toc.2014.v010a001; arXiv:0909.5175v4. The local file is the 20-page arXiv:0909.5175v4 author version; its title/author page matches the journal article, whose published pagination is *Theory of Computing* 10 (2014), 1–26. The local-file page numbers below are physical PDF pages (not journal pages); SHA-256 is in sources.json.

## Theorems read

- **Theorem 1.3 (Boolean noise sensitivity).** For a degree-\(d\) PTF \(f:\{-1,1\}^n\to\{-1,1\}\) under the uniform cube and bit-flip noise of rate \(\delta\),
  \[
  \mathrm{NS}_{\delta}(f)\le 2^{O(d)}\delta^{1/(4d+6)}.
  \]
- **Theorem 1.4 (Gaussian noise sensitivity).** For the paper’s stated degree-\(d\) Gaussian PTF class (the defining polynomial is multilinear or corresponds to an ellipsoid),
  \[
  \mathrm{GNS}_{\delta}(f)\le 2^{O(d)}\delta^{1/(2d+1)}.
  \]
  Preserve this theorem’s stated class; do not silently extend it to every degree-\(d\) polynomial threshold.
- **Theorem 1.6 (average sensitivity).** On the Boolean cube, \(\mathrm{AS}(f)\le 2^{O(d)}n^{1-1/(4d+6)}\). The separate combinatorial Theorem 8.2 gives \(\mathrm{AS}(f)\le3n^{1-2^{-d}}\) (local author-version PDF physical p. 14; its proof continues on p. 15, where it closes).

The proof chain for Gaussian noise sensitivity uses Carbery–Wright anti-concentration for a Gaussian polynomial and a perturbation comparison, optimizing the perturbation scale to obtain the \(1/(2d+1)\) exponent. For regular Boolean PTFs, invariance transfers the problem to Gaussian anti-concentration; a critical-index/random-restriction argument handles general PTFs. Average sensitivity follows both from the noise bound and from a separate induction. The paper also treats agnostic learning, which is outside this skill’s main interface.

## Boundary

These are sensitivity upper bounds and structural proof interfaces, not Fourier-sparsity lower bounds. They do not settle a minimum Fourier-\(\ell_0\) question. Gaussian polynomial anti-concentration and sharp sign-approximation estimates beyond these sensitivity theorems are handled by the W18 Gaussian approximation skill.

**Physical-page coverage:** p. 1 abstract; pp. 2–6 §1 setup, definitions, main theorems, learning application, and proof outline; pp. 6–7 §§3–4 regularity, hypercontractivity, Carbery–Wright, and invariance tools; pp. 7–10 §5 random-restriction structure; pp. 10–11 §6 Gaussian noise sensitivity; pp. 11–14 §7 Boolean noise sensitivity; pp. 14–15 §8 average sensitivity and Theorem 8.2 (statement and proof; printed footer pages 13–14); pp. 16–17 references/closing; pp. 18–20 Appendix A, including the Hermite expansion and full Gaussian perturbation-norm argument. All 20 physical pages were read.

**Reading status:** full text, local PDF pp. 1–20. The independent review status remains pending.
