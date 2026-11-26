---
name: math-regular-graph-low-induced-edge-count
description: Exhaustively count finite vertex subsets whose induced subgraph has at most a given number of edges, while checking regularity.
---

# Low-induced-edge counts in finite regular graphs

Use this skill to test a finite graph claim of the form “how many subsets induce at most `t` edges?”  It is particularly useful for checking small counterexamples before relying on an extremal conjecture.

## Procedure

1. Encode a simple undirected graph as `n` and a list of zero-based edges.
2. Run `scripts/count_subsets.py` with `--budget t`.
3. Check the printed degree sequence; only call the input `d`-regular when all degrees agree.
4. Record `n`, edges, threshold, count, command, and the fact that the result is exhaustive only for this finite graph.

## Boundaries

- The program enumerates all `2^n` subsets, so it is intended for small witness graphs.
- It establishes neither an extremal theorem nor asymptotic comparison across all regular graphs.
- It rejects loops, repeated edges, and vertices outside the given range.

## Source

`references/carenini-triangular-prism-witness.md` records the source's physical-p.1 triangular-prism versus `K_{3,3}` witness.  The asset independently reproduces the two finite counts.

## 文献复核采用的构件

- [Source note: regular-graph subset witness](references/carenini-triangular-prism-witness.md)
