# Entropy cancellation on dissociated labels

Source: OpenAI, *Rokhlin's multiple-mixing problem for one transformation*, SHA-256 \`45000cec6bcec95daede6af976803b7fc2ea995c5953cc2448ec48218db2b86d\`, physical pp. 34-35, Lemma 6.3. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

Let \((\ell_m)\) be dissociated and let \(F_m\) take values in one fixed finite subset of the closed unit disk.  If the Shannon entropy of \((F_0,\ldots,F_{n-1})\) satisfies \(H_n=o(n)\), then the source proves
\[
 {1\over n}\sum_{m<n}\left|\int F_m\chi_{\ell_m}\,d\eta\right|\longrightarrow0.
\]
No independence of \(F_m\) and \(\chi_{\ell_m}\) is assumed.  The proof chooses deterministic phases so the correlations are nonnegative real, bounds an exponential moment through dissociation, and uses low word entropy to control the bad set.

The application to a stationary process requires that each sampled word comes from a finite alphabet window and has sublinear entropy.  Do not replace dissociation or the fixed finite alphabet by an unverified approximation.

## 固定来源

- 物理页 34, 35。Lemma 6.3 and application to (61) SHA-256 `45000cec6bcec95daede6af976803b7fc2ea995c5953cc2448ec48218db2b86d`。[Rokhlin's multiple-mixing problem for one transformation](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf)
