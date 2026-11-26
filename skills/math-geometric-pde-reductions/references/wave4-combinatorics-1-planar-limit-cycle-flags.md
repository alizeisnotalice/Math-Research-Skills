# Finite flags and exact graph enlargement

Source: OpenAI, *Uniform bounds for planar polynomial limit cycles*, SHA-256 \`8ff8e55372a94e4f494f3412539a3dfb05cb7f36b66e7b94d9be8f99603fbe89\`, physical pp. 1, 8-12 and 153-158. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

For a finite family of large inputs, Lemma 2.2 states that, after a fixed linear coordinate change and bounded ordinary coordinates, a flag can insert \(\log\) of a free scale while retaining prior scale values; it consumes that scale and adds at most one positive free residual or one bounded ordinary residual.  The source explicitly keeps a finite request fixed: no uniform number of scales/heights over an original sequence is asserted.

The exact enlargement interface is Lemma 11.7.  Given isolated solutions \(u_i\) and appended equations \(G(u,v)=0\) with selected graph Jacobian \(G_v(u_i,v_i)\) invertible pointwise, retain all equations.  Recoverable old flag inputs cannot vary on the local lifted solution set with \(u\) fixed.  Intermediate-flow and finite-jet graph equations are triangular with unit diagonal.

Use only with a fixed finite enlargement and its verified selected graph Jacobian.  This does not by itself bound limit cycles.

## 固定来源

- 物理页 1, 8, 9, 10, 11, 12, 153, 154, 155, 156, 157, 158。Sections 2.1 and 11; Lemmas 2.2, 11.7; proof of Theorem 1.1 SHA-256 `8ff8e55372a94e4f494f3412539a3dfb05cb7f36b66e7b94d9be8f99603fbe89`。[Uniform bounds for planar polynomial limit cycles](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf)
