# bsu15 — Monotone cellular automata in a random environment

**Reading status:** `fulltext_read`; the complete 33-page article was read (PDF pp. 1–33). The main infection-time and torus-scale statements were visually checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Béla Bollobás, Paul Smith, and Andrew Uzzell, “Monotone Cellular Automata in a Random Environment,” *Combinatorics, Probability and Computing* 24 (2015), 687–722, arXiv [1204.3980](https://arxiv.org/abs/1204.3980), v4. Local PDF SHA-256: `3803d598341080269f4b95ba764167fa8bb281869ba82e241818288c9832e089`.

## Model and classification

An update family \(\mathcal U=\{X_1,\ldots,X_m\}\) is a finite family of finite nonempty subsets of \(\mathbb Z^2\setminus\{0\}\). Initially infected sites form an iid \(p\)-random subset; at each synchronous step, \(x\) is infected if it was already infected or \(x+X_i\) is fully infected for some rule \(X_i\). Define the stable set \(S\subset S^1\) by half-plane closure: \(u\in S\) when \([H_u]=H_u\). A direction is strongly stable when it lies in the interior of an interval of stable directions. Definition 1.3 classifies families as supercritical, critical, or subcritical from the stable-set geometry; no symmetry assumption is imposed.

Theorem 1.4 (PDF p. 6) proves that for a critical two-dimensional update family the first infection time \(\tau\) of the origin satisfies, with high probability as \(p\downarrow0\),

\[
\tau=\exp\bigl(p^{-\Theta(1)}\bigr).
\]

Theorem 1.5 (PDF p. 6) gives \(\tau=p^{-\Theta(1)}\) with high probability for supercritical families. Theorem 1.7 (PDF pp. 6–7) states the corresponding torus critical-probability orders: \(p_c(\mathbb Z_n^2,\mathcal U)=(\log n)^{-\Theta(1)}\) in the critical class and \(n^{-\Theta(1)}\) in the supercritical class. The authors say this torus statement follows by the same methods and do not prove it separately. Theorem 7.1 (PDF pp. 30–31) characterizes supercriticality by existence of a finite set with infinite closure. The paper gives no theorem for subcritical families and records the expected nontrivial transition as a conjecture in §8.

## Proof mechanisms

For critical-family lower bounds, the ordinary rectangles process fails without symmetry. The authors replace it with a covering algorithm initialized by disjoint breakthrough blocks. Lemmas 4.5–4.8 (PDF pp. 16–18) show that the resulting droplets cover the closure, contain linearly many disjoint breakthrough blocks when large, and obey an Aizenman–Lebowitz-type intermediate-scale lemma. A union bound on the probability of covered droplets at scales around \(\log t\) then yields the lower infection-time bound in Theorem 4.1.

For upper bounds, §5 constructs finite quasi-stable directions so a droplet can grow all the way to its corners. Lemmas 5.2–5.5 (PDF pp. 19–25) turn finite boundary blocks into one-row growth and then a nested-droplet growth rule. In §6, independent sprinkling first finds a critical seed and then supplies the blocks needed to expand it; this gives Theorem 6.1. In the supercritical case, the empty set itself is a usable block in a direction with no stable directions, yielding polynomial infection time in §7. These are two-dimensional, update-family-specific arguments with constants/exponents depending on the family.

**Visual checks:** rendered PDF p. 6 for Theorems 1.4–1.5 and p. 30 for the supercritical growth argument and Theorem 7.1.

## Transfer limits

The paper gives order-of-magnitude exponents, not a universal exact threshold or the subcritical exponential infection-time tail sought in B179. Its critical and supercritical labels are specific to finite update families on \(\mathbb Z^2\); neither the result nor the deterministic update rule automatically transfers to higher dimensions, random graphs, strategic games, or zero forcing. The torus theorem is asserted from the same methods but is not separately proved in the article.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bsu15`).
