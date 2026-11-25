---
name: euclidean-tensor-geometry
description: Apply or audit OpenAI family 379 Euclidean tensor prices, Strassen spectral invariants, and common-placement network bounds in arithmetic complexity and combinatorics. 中文触发：欧几里得张量几何、张量价格、渐近谱、跨割下界。Do not use for generic tensor numerics or classical maximal operators without a proved model bridge.
---

# 欧几里得张量几何

本入口用于指定专题的研究核验。预印本及项目材料按固定版本引用，使用具体结论前核验原文假设、证明依赖和迁移步骤。涉及既有课题状态时，先对照当前项目记录。

This is a theorem-transfer workflow, not an assertion that different problems share an invariant. Use the pinned November 24, 2026 manuscripts and distinguish the manuscript claim, the exact Lean statement, and any new bridge being proposed. Never say all proofs in the family were formalized.

## Workflow

1. **Pin the problem model.** Record the base field and characteristic, exact identities vs evaluation vs border approximation, the permitted local maps, tensor legs and placements, and the cost being bounded (arithmetic gates, rank, tape steps, set-family size, or another specified quantity). Use [family-379.md](references/family-379.md) to pick a paper and locate its precise hypothesis and Lean scope.
2. **Construct the two sides at one placement.** Give a target tensor, then a restriction/contraction from resources to that target in the claimed model. For a lower bound, prove a price lower bound for the target and a uniform price upper bound for every allowed candidate decomposition, including a justified sum penalty. For an upper bound, supply a construction and charge each stage in the stated model. Never argue that a price bound for one spectral point alone constructs an algorithm or proves restriction.
3. **Use the invariant, not just the geometry.** At a finite output set S of positive diameter, use the compatible scaled log of a spectral point, with coherent trivial slots and local linear restrictions. Two-site binary equality costs the distance; a q-symbol equality wire costs distance times log₂ q. The normalized mean width is the price of a shared label, not the price of an arbitrary tensor. Use [proof-moves.md](references/proof-moves.md) for exact sum, transport, closure, and cross-model conditions.
4. **Audit the transfer.** Check restriction direction, coefficient domain, all terminal locations, hidden fanout and copy charges, rate normalization, uniformity across sizes/tensor powers, and any conditional complexity assumption. A Zariski-closure argument within a fixed finite tensor format is not a generic bound for analytic limits or a sequence of changing formats. Report a missing bridge as a lemma to prove, including an explicit falsifier or boundary case when available.

## Routing for current research

- Fourier sparsity of Boolean functions: the paper bounds exact transforms as linear circuits, not the Fourier dimension of a sparse Boolean spectrum. Only use it after constructing a reduction that preserves support, span dimension, and field. In particular, do not use the Walsh transform over characteristic two where the required primitive root/invertibility conditions fail.
- Centered-cube weak type, fixed-binary Derrida–Retaux, continuous Cantelli, and general 0–1 polynomial factors: no family-379 theorem applies directly. For centered cubes, shared-source/common-placement accounting is a research analogy only; formulate and prove the measure-to-tensor bridge before importing an estimate. For unfair polynomials, retain positivity and convolution multiplicity, an invariant ordinary field-linear maps do not enforce.
- Exactly two local maxima on a grid: geometric prices of grid state sums do not automatically control the conditional probability or separation of peaks; a finite-state reduction must preserve the event, normalization, and statistics before a comparison is useful.

Output the precise claim, the reduction and price inequalities, and what remains unsupported. Cite exact upstream paths, theorem labels or proof sections and Lean scope where material; don't rely on headlines or paper names as proofs.
