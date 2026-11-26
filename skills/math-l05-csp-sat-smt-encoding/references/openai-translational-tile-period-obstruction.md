# Translational-tile period obstruction

Source: OpenAI, *A translational tile with no fully periodic tiling in dimension three*, SHA-256 \`195ccaae8617ea5d18a532aa4913a1ba2ca29e95a791f686808f01a9e6242089\`, physical pp. 3-6, Definition 2.1, Lemmas 2.2-2.5 and Proposition 2.4.

For prime \(p>200\), take \(N=p^2\), \(I=\{0,\ldots,N-1\}\), and alphabet \(\mathbb F_p\).  An allowed word has witness \(a,b\), not both divisible by \(p\): it equals \(an+b\) modulo \(p\) when \(p\nmid an+b\), equals \((an+b)/p\) modulo \(p\) when exactly one \(p\) divides it, and is free at multiples of \(p^2\).  A strip array obeys the line rule if every affine line samples an allowed word.

The stated finite-to-global procedure finds a \(4\times4\) nonexceptional square for slopes \(0,\pm1\), fits \(An+Bm+C\), and propagates four consecutive good cells along lines and diagonals.  If every column is nonconstant, the source states \(B\ne0\); a vertical period is then divisible by \(p\).  Rescaling \(W(n,m)\) to \(W(n,pm)\) preserves the rule and decreases a minimal positive period, giving the stated obstruction.

Use only after encoding this exact finite word rule.  It does not decide periodicity of arbitrary tiles.

## 固定来源

- 物理页 3, 4, 5, 6。Definition 2.1; Lemmas 2.2-2.5; Proposition 2.4 SHA-256 `195ccaae8617ea5d18a532aa4913a1ba2ca29e95a791f686808f01a9e6242089`。[A translational tile with no fully periodic tiling in dimension three](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf)
