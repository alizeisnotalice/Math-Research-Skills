# Amalgamated-word witness: verified scope

Source: Jiaqi Wang and Lihong Zhi, *An Explicit Polynomial Counterexample to Connes' Embedding
Conjecture*, local author-preprint v2 (SHA-256
`558861199f720a2f810ae9711ec6c75bd38b201a2f8d4c984b89b5a57695426a`), physical p. 5,
Section 2.1.

The source defines an amalgam containing `G` and `H x <v | v^2=1>`.  With its supplied elements
`u,h`, it sets `W=u v u^-1` and `k=u^-1 h u`.  Conditional on the asserted strict membership
`k notin H`, it rewrites `u^-1(h^-1 W h W)u` as `k^-1 v k v`, a reduced nonidentity word.  The
canonical group trace therefore vanishes on that group element, yielding the source’s local
commutator-norm calculation.

This record does not independently establish the source-specific strict membership, group model,
or the later quantitative matrix positivity argument.  It is only a normal-form proof gate after
those inputs are supplied and checked.

Use this conditional proof gate with groups `H <= G`, the factor `B=H x C2`, and
`Gamma=G *_H B`.  Let `v` be the nontrivial generator of the `C2` factor.  If the caller has
independently established `k in G \ H`, then

`k^-1 v k v`

is a reduced alternating word, hence is nonidentity in `Gamma` by the normal-form theorem.

For the source pattern, additionally verify the displayed group equalities which identify the
target word with this normal form.  The canonical group trace then vanishes on the resulting
nonidentity group element.  State separately which subgroup-membership and equality checks were
actually carried out.

This gate does not prove `k notin H`, construct the source’s groups, establish non-hyperlinearity,
or certify a polynomial trace inequality.  See [the source scope](#amalgamated-word-witness-verified-scope).
