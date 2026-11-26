# Buffered Fourier division at resonances

Source: OpenAI, *Rigidity of Smooth Billiards with a Continuous Caustic Collar*, SHA-256 \`0fefc18481d52acb6118fa389d84d4d62b8e5e08cc3fd278cb29c040a0b41150\`, physical pp. 25-26, Lemma 3.5. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

For \(d_n(t)=2i\sin(nt/2)/t\), retained modes \(1\le|n|\le N\), and zeros \(t_j=2\pi j/n\) inside the buffered domain, interpolate
\[
R_n(t)=\sum_jF_n(t_j)\frac{\sin(n(t-t_j)/2)}{n(t-t_j)/2},
\qquad H_n(t)=\frac{F_n(t)-R_n(t)}{d_n(t)}.
\]
The source proves removability of the retained divisor zeros and, after a one-buffer domain loss,
\[
\|H\|\le P(M+\eta),\qquad
\|\partial H-F\|\le P(\eta+Me^{-N\delta}),
\]
with specified strip norms and fixed-derivative variants.

The retained zero list, buffer, Fourier cutoff, mean-zero condition, and real/even symmetry assumptions are essential.

## 固定来源

- 物理页 25, 26。Lemma 3.5 SHA-256 `0fefc18481d52acb6118fa389d84d4d62b8e5e08cc3fd278cb29c040a0b41150`。[Rigidity of Smooth Billiards with a Continuous Caustic Collar](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/paper.pdf)
