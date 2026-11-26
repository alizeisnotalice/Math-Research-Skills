---
name: probability-infection-witness-methods
description: Build and audit finite activation witnesses for specified deterministic infection, zero-forcing, graph-bootstrap, or Young zero-set rules while keeping the host, update clock, and target observable fixed.
---

# Infection witnesses and closure certificates

Use this skill when proving activation of a specified vertex, edge, or site under a deterministic rule. Fix host/domain, state object, initial set or law, update rule, clock, target observable, and finite/infinite setting.

| Model | Route | Boundary |
| --- | --- | --- |
| Fixed finite graph with iid initial blue vertices and unique-white-neighbour forcing | G28 | Randomness is only in the initial set. |
| Fixed vertex set with synchronous edge-\(H\) bootstrap | G29 | Each round uses the graph at its start. |
| Hamming-plane row/column growth from a finite Young zero-set | G30 | Preserve the stated row/column count rule. |
| Explicit LP, interval, SOS, SAT/SMT, or exhaustive object | finite certificate | It certifies its encoding only. |

For finite-premise rules \(P\to h\), an acyclic activation witness has initial facts at depth zero and a rule node at one plus the largest premise depth. Verify each premise in the exact host and rule. Its depth proves activation by that many synchronous rounds. It supplies no slow-time lower bound or universal closure statement.

For G28, a force \(u\to v\) requires \(u\) and every neighbour of \(u\) other than \(v\) to be blue. Keep fixed-host zero forcing separate from probabilistic forcing. For G29, a complete legal sequential schedule bounds synchronous closure time, while a prefix only bounds its listed targets. Weak saturation, random threshold, seed size, and maximum time are separate observables. For G30, finite-rectangle results require their own seed-support and latency hypotheses before any infinite-plane conclusion.

## 尚未获得来源支持的路线

本版不采用固定宿主 G28 的 Russo--Margulis、clique first-entry、frontier automata 或 second-moment/Janson 路线；也不采用 G29 的势函数/摊还分析或 G30 的线性代数弱饱和和覆盖 LP/分数对偶路线。不得由相邻的有限证书或其他模型推断这些方法。

Read [method routing](references/method.md), [source cards and limits](references/sources.md), and [positive](examples/positive.md) or [negative](examples/negative.md) examples. Historical source mappings are available through [the central evidence guide](../math-research/references/evidence.md).
