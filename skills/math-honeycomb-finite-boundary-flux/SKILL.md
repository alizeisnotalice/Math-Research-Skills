---
name: math-honeycomb-finite-boundary-flux
description: 在有限、单连通蜂窝三角形域中认证零环权重的带相位边界通量恒等式及凸域正性界；不用于条带渐近、桥质量或一般自避游走。
---

# 蜂窝有限边界通量

Use this only for the exact finite honeycomb setting in [proof and scope](references/finite-boundary-flux.md): a finite simply connected union of equilateral triangles with a simple polygonal boundary, one inward boundary port, the zero-loop convention, and the source’s signed-turning phase.

1. Freeze the triangular domain, port orientation, path convention, number of visited triangles, and signed-turning convention before summing. A hexagonal graph with a different mid-edge/vertex convention is not automatically the same model.
2. At λ=π/8, set ρ=(2 cos λ)^(-1) and t=3/8. Expand the finite branch tree. Interior branching conserves signed mass by 2ρ cos λ=1; pair every stopped collision with its reversed newly formed cycle. Record why the pairing is an involution and why its two phases cancel.
3. After cancellation, the exiting self-avoiding paths satisfy the complex boundary-flux identity in the reference. If the boundary is convex, take real parts only after deriving the stated turning interval; then the unsigned partition sum is at most 1/cos(3π/8).
4. Stop at this finite identity. It supplies neither a transfer-matrix spectral gap, a critical strip-crossing exponent, bridge renewal, a continuum limit, nor an SLE claim. Nonconvex domains lose the displayed unsigned bound unless a new phase lower bound is proved.

For an explicitly supplied triangular complex, use [the exact checker](scripts/check_honeycomb_boundary_flux.py). It enumerates its finite branch tree in \(\mathbb Q[z]/(z^8+1)\), checks the disk and port conditions, and reports separate exit and collision fluxes. [The six-triangle example](examples/hexagon-six-triangles.json) has exit flux \((1,0,\ldots,0)\) and zero collision flux. This computation certifies that finite input only.

The source is a preprint. This skill rederives the finite cancellation only; it does not certify its paper’s strip-mass theorem or the mutually dependent Family 237 transfer chain.
