# Bernoulli-convolution prefix realization

Source: OpenAI, *Arithmetic classification and non-Pisot singularity for Bernoulli convolutions*, SHA-256 \`d7c67b840e4422308a315ddebfa30f7eaddf8dde07affa3954afa84ac63034a2\`, physical pp. 3-5 and 9-10, Section 2.2 and Proposition 3.5. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

The source turns a high multiplicity of nearby prefix sums into short intervals whose union has small Lebesgue measure but fixed Bernoulli-convolution mass, thereby ruling out absolute continuity.  For the converse direction, Proposition 3.5 says that for fixed \(\lambda\in(1/2,1)\), appropriate \(d\), and a word \(w\in\{-1,0,1\}^n\) satisfying
\[
\left|\sum_{i<n}w_i\lambda^i\right|\le(L-a)\lambda^n,\qquad L=(1-\lambda)^{-1},
\]
there is an algebraic unit root \(r\in(\lambda,\lambda+4^{-n}/2]\) whose signed minimal polynomial has prefix \(w\).

The construction appends digits to control the value at \(\lambda\), uses two irreducible completions of opposite sign, and invokes an intermediate value root.  Preserve all parameter restrictions and the supplied polynomial family.

## 固定来源

- 物理页 3, 4, 5, 9, 10。Section 2.2 and Proposition 3.5 SHA-256 `d7c67b840e4422308a315ddebfa30f7eaddf8dde07affa3954afa84ac63034a2`。[Arithmetic classification and non-Pisot singularity for Bernoulli convolutions](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/paper.pdf)
