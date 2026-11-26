# Wave 4 PA3: spectral variogram and signed logarithmic energy

## The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)

Source SHA-256 `26deb84be9ead6846c9144bab5260a03659cc94d615866a5b3717e632444170f`, physical pp. 45--46 and 76, Lemma 4.7, Proposition 4.8, and Lemma 7.6.  The energy-weighted spectral measure has the symmetrized phase sum rule
\[
2\,\mathrm{sym}(p_*E\mu)=D_0\frac{dp}{2\pi},
\]
and finite mean winding.  The resulting height variogram is
\[
\mathbb E_c(h(k,j)-h(0,0))^2
=2\operatorname{Re}\int(1-f(1)^kf(\pm i)^{|j|})\,d\mu(f)
=4\kappa\log k+O(1),
\]
uniformly for `k\ge1`, `|j|\le k`.  For a compactly supported finite signed measure with ordinary finite Green energy, the source proves atomlessness and finite absolute logarithmic self-energy; Cauchy--Schwarz gives finite mixed absolute logarithmic energy for two such measures.

**Scope.** Scoped reference. It needs the source's spectral-orbit representation and ordinary finite signed-measure integral, not merely a formal cancellation of a divergent signed integral.  It does not prove the six-vertex scaling limit.

## 固定来源

- 物理页 45, 46, 76。Lemma 4.7; Proposition 4.8; Lemma 7.6 SHA-256 `26deb84be9ead6846c9144bab5260a03659cc94d615866a5b3717e632444170f`。[The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf)
