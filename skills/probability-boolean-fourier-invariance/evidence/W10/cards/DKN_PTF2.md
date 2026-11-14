# DKN-PTF2 — bounded independence fools degree-2 PTFs

**Source.** Ilias Diakonikolas, Daniel M. Kane, and Jelani Nelson, “Bounded Independence Fools Degree-2 Threshold Functions,” FOCS 2010, arXiv:0911.3389v2. The 36-page local PDF’s first page matches the title, authors, and version; SHA-256 is in `sources.json`.

## Main results and proof route

- **Theorem 1.1.** Any \(\widetilde{\Omega}(\epsilon^{-9})\)-wise independent distribution on {−1,1}ⁿ ε-fools every degree-2 PTF (f(x)=\operatorname{sgn}(p(x))), comparing its expectation with uniform-cube expectation. The sign convention at zero is specified in the paper. This is a sufficient bound with the theorem’s suppressed polylogarithmic factors; the statement is not a bare \(\Omega(\epsilon^{-9})\) bound. No matching lower bound is given.
- **Theorem 6.1 (regular case).** For a normalized multilinear quadratic polynomial with every coordinate influence at most τ, the paper proves an (O(\epsilon+\tau^{1/9})) expectation error using (2k)-wise independence for (k=\Omega(\epsilon^{-8})). The proof decomposes the quadratic form into positive semidefinite pieces with eigenvalues bounded away from zero and a small-operator-norm part. It then represents the threshold as a region in ℝ⁴, Fourier-transform mollifies the region indicator, controls the Taylor remainder by a spectral moment bound, and uses invariance plus Gaussian anti-concentration to bound the boundary layer.
- **Theorem D.1 (Gaussian coordinates).** For a real quadratic form with squared coefficient norm normalized to 1, fully independent standard Gaussian coordinates and (2k)-wise independent standard Gaussian coordinates have sign expectations within (O(\epsilon)) for (k=\Omega(\epsilon^{-8})). This is a Gaussian-marginal bounded-independence theorem, not a sharp polynomial/sign approximation theorem.
- **Theorem 7.1 and Theorem E.1.** A decision-tree regularity reduction turns the regular theorem into Theorem 1.1. The good leaves are either regular PTFs or are close to constants even under sufficiently high-wise independent residual distributions; the tree depth is paid as extra independence.
- **Theorems 8.1 and G.5.** Under Gaussian coordinates, intersections of (m) halfspaces are fooled with (\Omega(m^6/\epsilon^2))-wise independence, improved in Theorem G.5 to (\Omega(m^4/\epsilon^2)). Theorem F.2 gives a polynomial-in-(m), (\epsilon^{-8}) bound for intersections of degree-2 PTFs; the paper also explains the Boolean-cube transfer.
- **Theorem 5.1.** For symmetric (A) and uniform Boolean (x), a spectral moment estimate controls (\mathbb E|x^TAx-\operatorname{tr}A|^k\) by (C^k\max\{\sqrt{k}\|A\|_F,k\|A\|_{op}\}^k). This operator-norm refinement is a key ingredient in the regular-case proof.

## Scope

Keep Boolean-cube and Gaussian-coordinate distributions separate, and distinguish degree-2 PTFs from arbitrary-degree PTFs. The bounded-independence statements are upper bounds for fooling threshold expectations; they do not establish the optimal (k(d,\epsilon)), a lower bound on Fourier support, or the sharp Gaussian sign-approximation results assigned to W18.

**Physical-page coverage:** p. 1 abstract; pp. 2–3 §1 setup, Theorem 1.1, related work, notation, and proof overview; pp. 4–5 §3.1–3.2 FT-mollification approach; pp. 5–9 §4 mollifier estimates and §5 quadratic-form spectral moment bound; pp. 10–16 §6 regular PTF fooling, anti-concentration, and proof of Theorem 6.1; pp. 17–18 §§7–8 regularity reduction and intersections; pp. 19–21 references; pp. 22–24 Appendices A–C; pp. 25–28 Appendix D (Boolean/Gaussian omitted proofs and Theorem D.1); pp. 29–31 Appendix E/F (decision-tree reduction and intersections); pp. 32–36 Appendix G quantitative improvements. All 36 physical pages were read.

**Reading status:** full text, local PDF pp. 1–36. The independent review status remains pending.
