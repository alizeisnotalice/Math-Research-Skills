# english21 — Probabilistic zero forcing on random graphs

**Reading status:** `fulltext_read`; complete 27-page article read (PDF pp. 1–27), including the auxiliary lemmas and lower-bound proofs. Theorem 1.3 and the sparse lower-bound recurrence were visually checked. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Sean English, Calum MacRury, and Paweł Prałat, “Probabilistic Zero Forcing on Random Graphs,” *European Journal of Combinatorics* 91 (2021), 103207, DOI [10.1016/j.ejc.2020.103207](https://doi.org/10.1016/j.ejc.2020.103207), arXiv [1909.06568](https://arxiv.org/abs/1909.06568). Local PDF SHA-256: `cc972918976151dcdb97873daab837a99cff4c009015469af2894aac4dcc196c`.

## Rule and theorem

Probabilistic zero forcing (PZF) starts from a fixed blue set. In each round, every blue vertex makes independent randomized attempts to force its white neighbours according to the current blue neighbourhood; the paper’s rule assigns a blue vertex $u$ probability $|N[u]\cap Z|/\deg(u)$ of forcing a given white neighbour, where $Z$ is the current blue set. The round propagation time is random. This is not deterministic unique-white-neighbour zero forcing with a random initial set, nor push/pull rumor spreading.

Theorem 1.3 (PDF p. 5) studies PZF propagation time from a fixed vertex $v$ on $G(n,p)$. If $pn\gg\log n$, it proves a.a.s. for each $v$

\[
\operatorname{pt}_{\rm pzf}(G(n,p),v)\le(1+o(1))\bigl(\log_2\log_2 n+\log_3(1/p)\bigr),
\]

\[
\operatorname{pt}_{\rm pzf}(G(n,p),v)\ge(1+o(1))\max\{\log_2\log_2 n,\,\log_4(1/p)\}.
\]

In Section 1.2, a subscript denotes the logarithm base and unsubscripted $\log$ is natural. Thus these are base-2, base-3, and base-4 logarithms, not iterated-log indices. In particular, if $p=\log^{-o(1)}n$ (for example, constant $p$), the propagation time is asymptotic to $\log_2\log_2 n$. If $\log n/n\ll p=\log^{-\Omega(1)}n$, the bounds imply order $\log(1/p)$. The theorem does not assert these bounds at $p=c\log n/n$.

## Proof ideas and audit points

The upper bound finds expansion for all small vertex sets in $G(n,p)$, then runs five propagation phases: initial growth from one blue vertex; roughly multiplicative growth at small sizes; growth up to a scale near $n\log\log n/[d(\log\log\log n)^2]$, where $d=np$; exploitation of internal blue edges with a recurrence of the form $y_{i+1}\ge(y_i/8)^2p$; and a final round sequence clearing the remaining white vertices. For the sparse-regime lower bound, the paper couples the original process to a faster dominating comparison: its denominator $d_L$ is below the relevant actual degrees, so force probabilities are larger, and the refreshed graph $G_2$ contains $G_1$. It controls average degree in the induced blue graph through an $\eta$ recurrence and proves a time lower bound even for this faster process; the bound therefore transfers to the slower original process and produces the $\log_4(1/p)$ term. This comparison direction is specific to the constructed PZF process; do not assume general monotonicity of PZF propagation time under adding edges or forces. The dense lower bound enlarges the initial blue set using monotonicity and bounds round growth by a quadratic recurrence, yielding the $\log_2\log_2 n$ term. Rendered PDF p. 20 to check the sparse recurrence and bound; rendered p. 5 for the theorem statement and logarithm bases.

The authors’ Conjecture 6.1 asks whether the sparse leading constant sharpens to the base-4 lower-bound scale; Theorem 1.3 as stated does not close its base-3 versus base-4 constant-factor gap.

## Transfer limits

PZF randomizes the forcing step on a random host. It supplies proof techniques for propagation-time recurrences, but its theorem does not directly transfer to a lattice, a deterministic zero-forcing seed-set problem, graph-bootstrap edge infection, or a two-player percolation geography game. A model-specific coupling or rule simulation would need proof before claiming a mapped problem is solved.
**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/english21`).
