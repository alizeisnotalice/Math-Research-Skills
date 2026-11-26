---
name: probability-stationary-law-interfaces
description: Prove or audit stationary laws for Markov environments, tree flows, IPS and drift-jump systems; use for generator/core, flux, coupling, Palm/occupation, regeneration, or projective-limit arguments.
---

# Stationary-law interfaces

## Historical provenance status

**Historical source audit:** R11 granted PASS_SCOPED_WHOLE_PACKAGE for 31 scoped works (G19=9, G20=22). Packaging creates no new global read-registration entry; the prior global identity-deduplicated registration state is root-authoritative historical provenance.

Use this skill to turn a proposed invariant distribution into a theorem with its exact state space, transition rule, domain, normalization, and proof route. It consolidates the unpublished W26 interacting-particle stationary-law scope; do not create or invoke a parallel `probability-interacting-particle-stationary-laws` tool.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Choose the object before the proof

Write whether the object is a discrete kernel (P), a continuous-time semigroup (P_t), a rooted environment chain, a flow-rule child-subtree chain, an induced return chain, or a finite-prefix projection. Name its measurable state space and sigma-field. For random trees, specify the offspring law, survival conditioning, root convention, and whether probabilities are quenched or annealed. For biased walks, state which direction the bias parameter favors.

Stationarity, reversibility, ergodicity, uniqueness, and existence are separate conclusions. A measure equivalent to a reference law need not make a kernel ergodic. Uniqueness of an invariant probability does not mean uniqueness among arbitrary scalar multiples of invariant measures.

## Proof gates

1. **Generator to semigroup.** For a candidate μ, an identity \(\int Lf\,d\mu=0\) is initially only an infinitesimal balance on the functions actually tested. To conclude invariance, identify a core/domain for the generator, prove non-explosion or conservativeness and well-posedness, and state the integrability conditions that make the generator identity sufficient. A formal generator calculation on a convenient class is not a core theorem.
2. **Flux and boundary.** For drift-jump systems, list every boundary, collision, cut, and jump-update convention. Integrate the drift and jump fluxes over a specified region. Check that no mass enters from a boundary or disappears through a cut without appearing in the balance equation.
3. **Construction by coupling, queues, Palm, or regeneration.** State the exact map from the reference process to the proposed law, including rates, conditioning, stability, and normalization. For an induced chain, its base set must have positive measure; normalize the restricted measure, verify returns and the induced transition law, and use a finite mean return time when a finite stationary lift is required. A tower transfers ergodicity only when the base captures almost every orbit. For a PDMP with an active boundary, include incoming/outgoing trace terms and both interior and boundary jump kernels. A stationary embedded jump law needs finite positive total flux; an occupation lift needs its own finite positive mean holding-time normalizer. A Palm construction from an already stationary process does not prove that the continuous-time law exists.
4. **Infinite process from prefixes.** Let \(\pi_k\) delete coordinates beyond prefix \(k\). First prove semigroup intertwining,
   \[
   P_t^{(k+1)}(f\circ\pi_k)=(P_t^{(k)}f)\circ\pi_k,
   \]
   for the relevant bounded measurable test class (and the corresponding compatible transition kernels); formal generator agreement alone does not imply this identity. Next verify the candidate invariant probabilities satisfy \(\mu_k=(\pi_k)_\#\mu_{k+1}\) and that each \(\mu_k\) is invariant for its prefix semigroup. Kolmogorov extension then gives a consistent one-time law. To obtain a stationary path process, additionally prove consistency of the path laws and the needed existence/regularity conditions, such as tightness or compact containment in a specified path space. State any uniqueness assumptions separately.
5. **Tree flow rules.** Define the flow on every descendant tree and verify its consistency. Record every child transition mass. The LPP flow-rule ergodicity result requires strictly positive mass at every first-generation child GW-a.s.; equivalence of a stationary measure by itself is the open A027 hypothesis, not an established substitute.

## Boundaries for current examples

- For simple random walk on a supercritical no-leaf Galton–Watson tree, the AGW rerooting chain is stationary and reversible by LPP (1995), Theorem 3.1. Its path-shift ergodicity is obtained later from the last-exit induced system in Theorem 8.1 and the tower remark; do not attribute ergodicity to Theorem 3.1.
- LPP Proposition 5.1 is a zero-one comparison for two flow rules under \(\Theta_T(x)+\Theta'_T(x)>0\) for every first child GW-a.s. It is not the Markov-chain ergodicity theorem. Proposition 5.2 uses \(\Theta_T(x)>0\) for every first child GW-a.s.; its conclusion does not settle the equivalence-only question in §10.
- In the exact Left-Hamm finite-prefix process, the iid Exp(1) spacing candidate fails a necessary bounded-test Dynkin identity. The one-particle zero-Laplace tests are necessary only. Neither case supplies an invariant law. Do not transfer results from classical Hammersley, source/sink, or HAD dynamics without an explicit generator and boundary mapping.
### Historical audit record

- R11 prior stages admitted 27 scoped works; wave07 admits three new full-read works and a separate CIR-only sub-use from an already read work, for 31 distinct qualified works (G19=9, G20=22). G20.04 is supported only for the specific Behme–Schnurr CIR example; its generic polynomial-characteristics/jump/core claims remain held. G20.05 has a positive finite-influence construction only for Ferrari–Landim–Thorisson’s exact spatial Poisson replacement model; generic coordinate-prefix extension remains open. G19.05 cocycle comparison and any A17 positive invariant law remain unsupported. Qian–Xiao’s normalized-law identity remains held at zero credit, and the Grosskinsky dissertation units are supplementary zero quota. R16 rejected the GWI Theorem 2.13 claim that stationarity automatically forces finite jump flux; use the finite-occupation direction or verify the explicit L1 premise in Theorem 3.14. R16 also rejected Costa–Dufour's unrestricted σ-finite reverse; use only its finite nonzero G-invariant-measure direction with `0 < πH(E) < ∞`. R13 confirmed Holderrieth Lemma 5.1's differentiability claim is false; only the bounded-rate/proper-jump independent core repair is admitted. The Costa σ-finite limitation and Holderrieth repair are bound to the R16 Costa review（本机附件：`evidence/authority/prior_decisions/R16/neutral_CostaDufour2008_CDC/review.json.snapshot.txt`）, R11 Costa addendum（本机附件：`evidence/provenance/aliases.md`）, and R13 Holderrieth review（本机附件：`evidence/authority/prior_decisions/R13/neutral_Holderrieth2021/review.json.snapshot.txt`）. See [the method reference](references/method.md) and [source ledger](references/sources.md) for scoped PDMP boundary, flux, generator-domain, embedded-chain, and Palm routes.

## Choose a method route

Use the method-selection guide（本机附件：`references/method_selection.md`） to route a tree flow, generator/core, boundary-flux, Lyapunov, coupling, Palm/occupation, or infinite-volume question. It names each admitted route and its minimum match conditions. The 31-source index（本机附件：`references/source_index.md`） links every accepted method to its full usage card and states its transfer boundary; the [method contract](references/method.md) gives the proof obligations that still apply in a new model.

## References and examples

Read the method-selection guide（本机附件：`references/method_selection.md`）, then its linked usage card and the [method contract](references/method.md) before using a theorem. The source index（本机附件：`references/source_index.md`） defines the exact 31-work accepted scope; the [source ledger](references/sources.md) records reading and provenance, including held and zero-credit items. Use the [positive examples](examples/positive.md) for source-matched constructions and the [negative examples](examples/negative.md) to test missing hypotheses and prevent invalid transfers.

For stationary square-integrable scalar sequences, use [dyadic chord energy](references/dyadic-chord-energy.md) to obtain a summable finite-block deviation budget before applying a model-specific cocycle or regeneration argument.

For a deterministic finite path prefix in an iid or finite-range random environment, use [departure-row factorization](references/departure-row-factorization.md) before identifying a future-dependent regeneration cut. The required independence is a statement about rows used at departures, not an annealed strong Markov property at the cut.
