# Negative patterns: same space and same dimension are not enough

## Equal exact dimensions do not imply equivalence

Take the usual binary coding of the middle-thirds Cantor set `E`. Let `ν_p` be the pushforward of an iid Bernoulli digit law with digit-1 probability `p`, and let `ν_{1-p}` use probability `1-p`. Their exact dimensions are

`dim ν_p = h(p)/log 3 = h(1-p)/log 3`,

but for `p=1/3`, the strong law gives different limiting digit frequencies under the two laws. The measurable set of codes with limiting digit-1 frequency `1/3` has full `ν_{1/3}` measure and zero `ν_{2/3}` measure. Thus the measures are mutually singular despite equal dimension. This is an exact counterexample to the inference “same dimension implies equivalent.” The locally run SymPy check and numeric output for `h(1/3)/log(3)` are in the L13 math record（本机附件：`evidence/linked_markdown/1e81b91a1bc1c130_evidence.md`）; the SLLN argument, not the decimal, proves singularity.

This is a derived illustration, not A147’s two named simple-random-walk laws.

## A147 is a question about one common Cantor set

PTN2026 Chapter 16, Question 16.7 asks whether the simple-random-walk harmonic measure from a binary coding tree and that from a ternary coding tree are mutually singular after both are pushed onto the same middle-thirds Cantor set. The chapter leaves this open. Different source trees, capacity formulas, or dimensions do not by themselves provide a common Borel separator or a Radon–Nikodym derivative.

The hyperbolic-group comparison criterion is not an automatic reduction: it requires both laws to be walks on the same non-elementary hyperbolic group and the same boundary-to-Cantor coding map. The binary and ternary source trees in Question 16.7 do not come with that shared representation. Even in its valid model, failure of the criterion gives non-equivalence, not mutual singularity.

## Nonlinear harmonic set functions need not be probabilities

Kaufman–Llorente–Wu’s `F`-harmonic set function can fail subadditivity/additivity: their examples include zero sets whose union has positive set-function value. Without countable additivity and total mass one, do not invoke probability entropy, measure-class, or Radon–Nikodym results for that object.

## Entropy rate without ergodicity

For a stationary but nonergodic mixture, the information-rate limit can depend on the ergodic component; it need not be one deterministic constant. State a conditional component formula or add ergodicity before quoting a constant almost-sure entropy rate. A tree environment that is stationary under one biased-ray law does not automatically make every coding law stationary or ergodic.


## A common map does not preserve singularity

On X={0,1}, let μ₁=δ₀ and μ₂=δ₁. These measures are mutually singular. Under the same measurable constant map φ:X→{*}, both pushforwards are δ*. Thus measurable pushforward preserves μ₁≪μ₂ (and equivalence) but does not preserve singularity unless the map retains a separating set. For a boundary-to-E singularity argument, prove the target Borel separator directly or use a Borel isomorphism on the relevant full-measure parts.


## A branching spectrum is not an arbitrary coding comparison

The Kinnison–Mörters joint spectrum concerns the branching measure and a forward-only child-uniform law on the same Galton–Watson boundary under their stated moment and offspring assumptions. It does not cover an undirected simple-random-walk exit law by notation alone, and the spectrum does not supply an A147 separator for two deterministic tree codes into the Cantor set. Likewise Liu’s branching-set gauge concerns the support gauge and the associated branching measure, whose random total mass is `W`; it is not a probability-measure equivalence theorem. See the branching-measure use card（本机附件：`evidence/usage_cards/G25-branching-measures.md`）.
