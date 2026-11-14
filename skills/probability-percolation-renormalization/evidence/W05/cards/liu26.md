# liu26 — Turán-density upper bound for running time

**Reading status:** `fulltext_read`, complete eight-page paper, PDF pp. 1–8. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Weichan Liu, Xiangxiang Nie, Simón Piga, Bjarne Schülke, “Upper Bounds on the Running Time of Bootstrap Percolation,” arXiv:2604.22630v2, 31 Aug 2026.

## Theorem and hypotheses

For fixed finite \(k\)-uniform hypergraph rule \(F\), each synchronous round adds all missing host \(k\)-edges that complete a copy of \(F\). Theorem 1.3 (PDF p. 3) states, for any \(e\in E(F)\),

\[
M_F(n)\le \bigl(\pi(F-e)+o(1)\bigr)\binom nk,
\]

where \(\pi(F-e)\) is the Turán density. For graph cliques, Theorem 1.1 gives

\[
M_{K_t}(n)\le\left(\frac{t-3}{t-2}+o(1)\right)\binom n2\quad(t\ge3).
\]

## Proof chain read

Track edges by the round in which they are first added and form the auxiliary graph of edges infected by a specified time. If the total running time exceeded the claimed coefficient by \(\varepsilon\binom nk\), supersaturation would create \(\delta n^{v(F)}\) copies of \(F-e\). Classify each into four types according to the infection time of the missing edge \(e\) relative to the latest/second-latest infection times in the copy. Each type has at most \(O(n^{v(F)-1})\) candidates, using shared vertices or the uniqueness of an infection round. For large n this contradicts supersaturation (PDF pp. 4–7).

## What it does not prove

At \(t=5\) the bound is \((2/3+o(1))\binom n2\), still order \(n^2\); it does not prove \(M_{K_5}(n)=o(n^2)\). It gives upper-bound context for C189 and general time questions, not a resolution of them.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/liu26`).
