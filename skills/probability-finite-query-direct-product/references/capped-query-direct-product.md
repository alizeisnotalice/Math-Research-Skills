# Capped direct products for finite query trees

## Pinned source and scope

OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, pinned manuscript at commit `3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `a99f1c38d086a33591b6204ae3957fe3f25c8f31d97c48087325a18fd66daf3e`, physical PDF p. 11, Lemma 4.1. The checked source is [the pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf).

Let `D` be a finite subset of `{0,1}^n`, let `mu` be a probability distribution on `D`, and let `P:D->{0,1}`. Fix an integer `L>=0`. Suppose every deterministic algorithm using at most `L` coordinate queries has success at most `beta` under `mu`. For independent `U_1,...,U_r~mu`, a (possibly randomized) classical algorithm that makes at most `L` queries to each copy has probability at most `beta^r` of outputting all `P(U_h)` correctly. It may interleave its queries adaptively and receive any auxiliary information independent of the tuple of inputs.

This is a finite classical statement. It does not give a total-function lifting, a quantum lower bound, a result for correlated copies, or a conclusion when the cap is only on the total number of queries.

## Why adaptive interleaving is allowed

Freeze the independent auxiliary information and internal random coins. At a positive-probability transcript `tau`, its observed answers impose one coordinate constraint on each copy. Because the next query is a deterministic function of the prior answers, every tuple satisfying those per-copy constraints follows exactly the same schedule. Thus the conditional law remains a product of its separate conditional laws.

For copy `h`, let `q_h(tau)` be its used queries and let `V_h(tau)` be the best conditional success probability for its target using at most `L-q_h(tau)` additional queries. If the next query is to copy `h`, doing that query followed by an optimal continuation is an admissible strategy, so

`E[V_h(tau_next) | tau] <= V_h(tau)`.

All other factors are unchanged under that conditional step. Hence `prod_h V_h(tau)` is a supermartingale. At a terminal transcript, the conditional probability that the tree's proposed answer vector is correct is at most `prod_h V_h(tau)`. Optional sampling is only finite here: paths can be padded to `rL` query slots. Initially every factor is at most `beta`, yielding `beta^r`. Randomized trees follow by first conditioning on their seed.

## Exact checker schema

The JSON input has `domain` (distinct equal-length binary strings), matching rational `probabilities` written as strings accepted by `Fraction`, matching Boolean `values`, nonnegative `cap`, positive `copies`, and a `tree`.

A tree node is either `{"output":[0,...,1]}` or `{"query":[copy_index, coordinate_index],"zero":node,"one":node}`. Indices are zero based. The checker rejects malformed nodes and any positive-probability root-to-leaf path whose query count for one copy exceeds `cap`. It then computes the one-copy optimum by exact dynamic programming over the finite posterior restrictions and enumerates the product law exactly. A successful check is a certificate for that supplied tree, not an automated proof that an informal algorithm was encoded faithfully.
