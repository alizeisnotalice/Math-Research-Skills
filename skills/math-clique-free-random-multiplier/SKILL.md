---
name: math-clique-free-random-multiplier
description: Construct and exactly check the finite-support random multiplier from the clique-free neighborhood recursion for a supplied finite weighted K_r-free graph.
---

# Clique-free random multiplier

Use this skill when a finite simple graph has positive rational vertex weights, an explicitly supplied clique exclusion `K_r`, and a calculation needs a mean-one random reweighting with small expected weighted edge mass. This is a finite, exact implementation of the recursion in Lemma 2.2 of the reviewed source; it is not an independence-number theorem or a sampler intended for large graphs.

Run `scripts/construct_multiplier.py INPUT.json`. The input names vertices, unordered edges, positive rational weights, an integer `r >= 2`, and rational `epsilon` with `0 < epsilon <= 1/2`. The script first checks every structural condition, including `K_r`-freeness, then deterministically chooses the first eligible neighborhood at each recursion level. It outputs the complete finite distribution and checks exactly that

\[
0\le m_v,\qquad \mathbb E m_v=1,\qquad
\mathbb E M_G((w_vm_v)_v)\le\epsilon\,w(V)^2.
\]

The construction may have exponentially many atoms. It deliberately stops above a requested `max_outcomes` limit rather than replace the finite law by floating-point simulation. A positive run on `examples/c5.json` and a rejected `K_3` input in `examples/k3-rejected.json` are recorded below.

Read [the derivation and source boundary](references/derivation.md) before transferring the result. The result depends on the supplied `K_r`-free certificate and covers only the multiplier lemma. It does not establish the paper's cross-mass, triangle-mass, or logarithmic independence conclusions.
