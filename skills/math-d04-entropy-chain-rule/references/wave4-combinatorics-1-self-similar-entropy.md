# Averaged grid entropy calculus

Source: OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, SHA-256 \`a09f48f43c41539211024d8e079580fe0712dc3dfd8035a16f7057d9b8b5d198\`, physical pp. 5-7, Lemmas 2.1-2.3. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

For bounded \(X\), define \(H_s(X)=\int_0^1H(\lfloor X/s+u\rfloor)\,du\), \(G_{s,t}=H_s-H_t\), and \(\Delta_s=1-G_{s,2s}\), with base-2 entropy.  The source records
\[
H_s(X)=h(X+V_s)-\log s,\quad H_s(aX+b)=H_{s/|a|}(X),
\]
and for integer \(t/s=N\), \(0\le G_{s,t}\le\log N\), concavity in the law, and \(G_{s,t}(X+Y)\ge G_{s,t}(X)\) for independent inputs.

For a compact exact-dimensional line measure of dimension \(d\), its scale entropies have limsup at most \(d\).  A vanishing one-bit deficit gives a total-variation comparison between a smoothed law and its translate, which the source uses with stopped self-similarity.  Keep the integer-ratio restriction and compact-support assumptions.

## 固定来源

- 物理页 5, 6, 7。Lemmas 2.1-2.3 SHA-256 `a09f48f43c41539211024d8e079580fe0712dc3dfd8035a16f7057d9b8b5d198`。[The entropy-rate dimension formula for self-similar measures on the line](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/main.pdf)
