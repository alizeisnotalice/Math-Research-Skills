# Prime-order Ryser construction: finite concentration inputs

Source: OpenAI, *Balanced counterexamples to Ryser's conjecture at prime orders*, SHA-256 \`5be7cf2d1f382e802c7b3e738bc143fff8b48f9504bd579f74719dc754f7a469\`, physical pp. 38-39, Appendix A.

For sequential variables \(X_j\) with conditional drift \(d_j\), set \(Z_j=X_{j+1}-X_j-d_j\).  Under \(|Z_j|\le2L\), the source states the fixed-time bound
\[
\Pr\left(\left|\sum_{j<T}Z_j\right|\ge u\right)\le2\exp(-u^2/(8TL^2)).
\]
The page explicitly excludes an automatic maximum-over-times interpretation.  For an independent-trial function whose \(i\)-th coordinate change is at most \(c_i\), its Doob martingale gives the same form; if \(c_i\le L\), use the displayed bound.

The construction combines this with its finite-field incidence, compatibility, and constituent-multiplicity conditions.  Retain the filtration, increment bounds, and every union bound.  This reference does not certify the construction when those source-specific conditions are absent.

## 固定来源

- 物理页 38, 39。Appendix A, Lemmas A.1-A.3 SHA-256 `5be7cf2d1f382e802c7b3e738bc143fff8b48f9504bd579f74719dc754f7a469`。[Balanced counterexamples to Ryser's conjecture at prime orders](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf)
