---
name: probability-planar-isoperimetry
description: Analyze planar-graph or tessellation isoperimetry when the embedding, set class, and exact perimeter convention can be matched to a scoped method.
---

# Planar graph isoperimetry and discrete curvature

Use this skill for a finite-set boundary/profile problem on a plane graph, a regular planar tessellation, or a lattice animal. Start only after fixing the graph and embedding, admissible finite sets, and the exact statistic. It does not establish an unrestricted outer-vertex profile, a conditional probability limit, or an infection-interface result merely from a planar-looking picture.

## First gate: name the perimeter

State one of the following before selecting a theorem:

- crossing-edge cut $|E(S,V\setminus S)|$;
- outside-vertex boundary $|N(S)\setminus S|$;
- occupied/inside vertex boundary;
- tile-edge perimeter, including hole boundaries and multiplicity;
- outside-cell site perimeter; or
- primal/dual face-boundary or contour length, including bridges, holes, and repeated traversals.

Do not convert statistics by visual analogy. Prove every conversion, retaining degree, multiplicity, component, and hole terms. In particular, an edge cut need not control an outside-neighbour boundary; the seven-cell honeycomb patch has occupied boundary 6 and triangular-graph edge cut 18. Read [boundary examples and exclusions](references/source-ledger.md#missing-condition-and-boundary-convention-cases) when a proposed step crosses conventions.

## Choose an active method

1. **General finite plane graph, curvature, or Euler identity.** Record components, holes, and which faces are counted; then use Euler/Gauss--Bonnet with separate incidence and boundary terms. Read [G17.01](references/source-ledger.md#g1701).
2. **Cut encoded by a contour or a dual object.** Prove the primal--dual correspondence including bridges, orientations, and repeated traversals. Read [G17.02](references/source-ledger.md#g1702).
3. **Exact lattice profile/minimizer.** Select only a compression or recurrence proved for this lattice and set class; show both the universal lower bound and an upper witness at each asserted size. Read [G17.03](references/source-ledger.md#g1703) and [G17.04](references/source-ledger.md#g1704).
4. **Cheeger or spectral question.** Fix whether the denominator is vertices, degree-volume, faces, or a weighted measure; verify the domain and generator/scaling before a spectral conversion. Read [G17.05](references/source-ledger.md#g1705).
5. **Regular hyperbolic tessellation.** Fix the exact $\{p,q\}$ and parameter range, keep vertex degree and face length separate, and count only in that tessellation. Read [G17.06](references/source-ledger.md#g1706).

## Operational checks

- Specify whether $S$ is arbitrary, connected, induced-connected, hole-free, edge-connected, or a named ball/polygon. Check singletons, bridges, holes, disconnected sets, and terminal layers.
- For an exact profile, a ball is only an upper witness. Supply a lower bound for every admissible set and a matching witness at every claimed size.
- A recurrence must state its erosion/layer operator, its valid range, and its initial and terminal cases.
- Keep finite calculations as instance evidence; they are not a proof outside the enumerated model.

## Equality and near-equality gate

Do not infer a stability, near-minimizer, Wulff, or all-minimizer statement from an exact inequality. An equality or reverse implication is usable only with every source-card hypothesis, including hole-freeness, connectivity, the named boundary convention, and exceptional sizes. The triangular-lattice auxiliary route, for example, retains its nontriangular-face count $h$ and handles $n=1$ separately; see [its positive-case card](references/source-ledger.md#positive-cases). The broad all-$N$ edge-minimizer classification remains held, not an active transfer.

## Scoped source interfaces

Use only the admitted row of a cited source. The 30 historical cards, their conditions, transfer limits, and local-attachment pointers are retained in [the source ledger](references/source-ledger.md). Start with:

- [plane-graph outer-neighbour bounds](references/source-ledger.md#positive-cases) for the Haslegrave--Panagiotis / Oh conditions;
- [finite triangular-grid compression](references/source-ledger.md#positive-cases) for the admitted $T_n$ outside-neighbour profile;
- [regular tessellation edge/face profiles](references/source-ledger.md#positive-cases) for the named normalized regular graphs; and
- [percolation-specific contour and variational interfaces](references/source-ledger.md#positive-cases) only with their stochastic inputs.

The ledger is a historical provenance and scope record, not a claim that all listed results have a common boundary statistic or transfer to a new graph. Its one portable evidence link resolves from the ledger location; private attachment labels remain documented local references and may be unavailable in a portable checkout.
