---
name: probability-queueing-heavy-traffic
description: Analyze queueing-network stability and heavy-traffic limits using fluid/Lyapunov methods, polling models, state-space collapse, BAR, and reflected diffusions. Renewal/Palm epoch conversion and exact coupling/total-variation questions are out of scope here.
---

# Queueing stability and heavy traffic

Use this skill when a problem depends on queueing stability, polling disciplines, heavy-traffic scaling, state-space collapse, a basic adjoint relationship (BAR), or a reflected Brownian limit. Start by fixing the state, observation epoch, arrival/service assumptions, and exact stability or convergence notion. Do not transfer a result across a change in discipline, input dependence, CRP status, or limit mode without proving that interface.

Read [the method guide](references/method.md) for proof routes and model checks. Read [the 30-row source index](references/sources.md) for the exact R06-admitted operational use cards. Use `source_id` and `work_family_id` from the canonical source-use index（本机附件：`references/accepted_scope_index.json`） for global catalogue matching; `W14-...` local IDs are display aliases. The corresponding complete PDFs and canonical identity/reading cards are included under `sources/` and `cards/`. Each use card controls the source theorem, assumptions, proof route, and transfer limits.

For general renewal input, record the interarrival law, dependence, arrival age/residual life, and exact observation epoch before using a polling formula. PASTA applies to Poisson arrivals under its nonanticipation condition; do not silently extend it to renewal arrivals. General renewal/Palm epoch conversion and exact-coupling methods are outside this entry.

For transform or diffusion work, derive the generator/steady-state identity from the actual model and boundary convention before solving it. Keep the probability-derived transform class distinct from a larger analytic function class. Treat finite-dimensional numerics as consistency checks only; do not use them as a stability proof, a limit theorem, or a transform-uniqueness argument. See the [scoped positive example](examples/positive.md) and [scoped missing-condition example](examples/negative.md).

For B054 Eq. (7), state the intended uniqueness class explicitly: the literal Eq. (8) analytic class has a scalar-normalization ambiguity, the augmented analytic class adds `L(0)=1`, and probability-admissible uniqueness also requires transform positivity/support and unused-service boundary-measure conditions. The scaling observation identifies a source-formulation gap; it does not solve the intended probability-class problem.

This skill's direct open-problem coverage is A006, A007, A008, A011, B054, and B157. The cited literature is an evidence snapshot from 2026-11-14; open/solved status needs fresh source verification before reuse.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## November 16 R06 source-use scope

The active source-use map is [the 30-row accepted index](references/sources.md), with exact row conditions and hashes in accepted_scope_index.json（本机附件：`references/accepted_scope_index.json`）. It is backed by R06's frozen 30-row aggregate and scientific whole-entry review. The latter is not a portability or installation approval. Wider claims in archived records are history-only and are not executable instructions or method credit. See the scope pointer（本机附件：`references/scope_pointer.md`）.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
