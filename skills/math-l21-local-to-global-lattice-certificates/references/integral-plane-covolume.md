# Integral-plane covolume certificate

Source: Terence Tao and Joni Teräväinen, *A power improvement in the Heilbronn triangle lower bound*, Lemma 2.3, PDF p. 5, pinned OpenAI Math preprint (2026-09-25), SHA-256 `e43687a84b82e23fd73f8025d8d8c91e7fee91c8ceead9bc41502b0595f09f0a`.

Let `basis` have full-rank integer rows \(b_1,b_2,b_3\), and let \(\Lambda=\sum_i\mathbb Zb_i\).  For a primitive \(y\in\mathbb Z^3\), set \(I=|\det(b_1,b_2,b_3)|\) and \(g=\gcd(y\cdot b_1,y\cdot b_2,y\cdot b_3)\).  Then \(y\cdot\Lambda=g\mathbb Z\) and
\[
 \det(\Lambda\cap y^\perp)=\frac{I\lvert y\rvert}{g}.
\]

Indeed, choose \(u\in\Lambda\) with \(y\cdot u=g\).  The homomorphism \(v\mapsto(y\cdot v)/g\) splits, so a basis of its kernel followed by \(u\) is a basis of \(\Lambda\).  The altitude of \(u\) over \(y^\perp\) is \(g/|y|\); multiplying this altitude by the kernel covolume gives \(I\).  The checker constructs a unimodular change of coefficient basis reducing the dot-product row to \((g,0,0)\), obtains an exact kernel basis, and compares squared covolumes.  It therefore checks this finite certificate, not the paper's determinant-counting proposition, finite-field construction, deletion step, or Heilbronn lower bound.

Pinned source: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/main.pdf>
