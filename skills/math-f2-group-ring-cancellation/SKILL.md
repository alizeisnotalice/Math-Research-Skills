---
name: math-f2-group-ring-cancellation
description: Verify a finite characteristic-two group-ring cancellation certificate from two labelled components and a supplied exact group-label product oracle; it does not establish torsion-freeness or nonzero factors.
---

# Finite F2 group-ring cancellation

Use this skill when two finite labelled graph components are proposed as supports for sums in an F2 group algebra and the cancellation is meant to follow from simultaneous same-label steps.

Run `scripts/check_f2_cancellation.py certificate.json`. The certificate supplies directed labelled edges for both components, a fixed-point-free inverse on edge labels, vertex labels `g_x`, inverse right labels `h_y^{-1}`, and an exact finite multiplication table for every product queried. The script checks connected full supports, inverse-edge closure, odd common outgoing-label counts at every pair, constancy of `g_x h_y^{-1}` along each simultaneous-step component, and even component size. On success, every component contributes zero to the proposed product over F2.

Read [the certificate contract](references/group-ring-parity-certificate.md) before preparing data. The finite verifier accepts the group-label multiplication table as an oracle: it does not prove associativity, that the labels come from a group presentation, path-label well-definedness, root separation/nonzeroness, or torsion-freeness/asphericity.

## OpenAI 原稿中的方法

- [OpenAI finite representation interfaces](references/openai-representation-200-206.md)
- [Scoped Bass trace interfaces](references/wave4-pa2-bass-trace.md)
