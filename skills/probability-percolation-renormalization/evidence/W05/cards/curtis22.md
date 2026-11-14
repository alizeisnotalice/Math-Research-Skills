# curtis22 — Random-set zero forcing

**Reading status:** `partial_read`; PDF pp. 1–4 and 20–21 were read. The full 22-page proof was not read. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Bryan Curtis, Luyining Gan, Jamie Haddock, Rachel Lawrence, Sam Spiro, “Zero Forcing with Random Sets,” arXiv:2208.12899 (2022).

## Model and relevant results

Choose each vertex of a fixed graph independently blue with probability \(p\); thereafter use deterministic zero forcing: a blue vertex with exactly one white neighbour forces that neighbour blue. This is distinct from probabilistic zero forcing, where forces themselves are randomized.

- Conjecture 1.2 (PDF p. 3) is the all-graphs comparison in A182: the random-set zero-forcing probability is maximized by the path \(P_n\).
- Theorem 1.3 (PDF p. 3) proves this comparison for all sufficiently large trees, with equality only for a path or endpoint probabilities \(p\in\{0,1\}\).
- Theorem 1.4 (PDF p. 3) gives \(p(G)=\Omega(n^{-1/2})\) for every n-vertex graph.
- Conjecture 6.1 (PDF p. 20) is the clique lower bound in A183: if \(G\) contains a clique of size \(k\), then \(p(G)=\Omega(\sqrt{k/n})\). The displayed argument is a motivation, not a proof.
- Problem 6.2 (PDF p. 20) asks whether \(p(Q_n)\to c\) for the n-dimensional hypercube; the paper only notes \(c\ge1/2\) if the limit exists.
- Problem 6.3 (PDF pp. 20–21) asks for the order of \(p(P_m\square P_n)\); the authors state that their upper and lower bounds do not match uniformly.

## Proof and transfer boundary

The path comparison uses zero-forcing-set counting and tree structure (the detailed proof lies in Section 5, not read in full here). These statements concern threshold probability for random initial vertices, not the number of synchronous bootstrap rounds. Any use for A182/A183/A185/B184 must preserve the exact graph family and random-set rule; finite Monte Carlo plots do not resolve the asymptotic conjectures.
