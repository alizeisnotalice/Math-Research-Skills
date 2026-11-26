# Exact finite recursion and its boundary

**Pinned source.** *A logarithmic independence bound for clique-free graphs*, OpenAI Math preprint, 25 September 2026, Lemma 2.2 on physical pp. 5--6; SHA-256 `15717a7c82914df2f220fad05a3fd6de7fd15f2abe26a4d1454d2b005ef39606`. Official pinned PDF: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf>.

Let `G` be a finite simple `K_r`-free graph, let all weights be positive, put `s=w(V)`, and take `0<epsilon<=1/2`. Set `eta=epsilon/4`. In a remaining induced graph repeatedly select a vertex whose open-neighborhood weight exceeds `eta*s`, remove that neighborhood as a part `V_i`, and let `R` be what remains. Then the parts are disjoint, `s_i=w(V_i)>eta*s`, each `G[V_i]` is `K_(r-1)`-free, and every remaining open neighborhood has weight at most `eta*s`. Hence

\[
 M_{G[R]}(w)=\frac12\sum_{v\in R}w_vw(N_R(v))
 \le \frac12\eta s\,w(R)\le\frac12\eta s^2. \tag{1}
\]

For `r=2`, `K_2`-freeness means that there are no edges, so set every multiplier to one. Inductively construct the lemma on every `V_i` at precision `epsilon/4`; let `b=\sum_i s_i` and `p_i=s_i/(2b)`. Choose `R` with probability `1/2`, giving it multiplier `2` and all other vertices multiplier zero. Choose `V_i` with probability `p_i`, use its recursive multiplier, scale it by `1/p_i`, and give all other vertices multiplier zero. (If no `V_i` was removed, use the all-one law.) This is a finite law because the recursion lowers `r`.

For a vertex in `R`, its mean multiplier is `(1/2)2=1`; for a vertex in `V_i`, it is `p_i(1/p_i)E[m_v]=1`. Only internal edges of a chosen part survive. Equation (1) and the induction hypothesis give

\[
\begin{aligned}
 \mathbb E M_G(wm)
 &\le 2M_{G[R]}(w)+\sum_i \frac{\epsilon s_i^2}{4p_i}\\
 &\le \eta s^2+\frac{\epsilon b^2}{2}
 \le \frac34\epsilon s^2\le\epsilon s^2.
\end{aligned}
\]

All arithmetic in the script is rational, so it checks this derived statement rather than estimating it. The source additionally gives an explicit uniform multiplier bound, but this skill does not reproduce that typography-dependent closed form; the emitted finite atoms themselves provide the exact bound for the supplied input.

This does **not** prove the source's entropy-extremizer identities (Lemma 2.1), its cross-mass estimate (Lemma 2.3), the weighted triangle theorem, or any logarithmic lower bound on an independent set. It neither finds a `K_r`-free certificate nor turns an arbitrary numerical graph into exact rational data.
