# Augmentation-row handle-cancellation module

Source: *A nondegenerate counterexample to the Morse-number Arnold bound*,
OpenAI (23 September 2026), SHA-256
`f7980995971b08dfbdcf0a1dcc34d1669c2bcc24648dc3782bc111463af0ce9e`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf).

## Scoped interface

This is a source-bound algebraic/handle module adjacent to, but not supplied
by, the fixed-locus transfer skill.  It requires the source's finite group
family, group ring `Lambda=Z[G]`, augmentation ideal `I`, and a handle
complex satisfying the stated exactness and rank inequalities.  It does not
produce an Arnold lower bound or a stable-Morse-number conclusion.

## Algebraic-to-geometric procedure

1. Define `aug(sum a_g g)=sum a_g` and `I=ker(aug)` (physical p. 5).  The
   source proves that the mod-`p` augmentation ideals have a generating pair,
   then performs its integral lift; retain that integral-lift requirement.
2. Given a unimodular row with at least three entries, use Lemma 2.3:
   elementary additions `x_j <- x_j+x_i q`, `i!=j`, can make one entry equal
   to `1` (physical p. 7).  This is a row operation in the stated group ring,
   not arbitrary scalar Gaussian elimination.
3. In the handle chain complex, put an old index-five handle `e` last.  From
   `partial_1 e=0`, exactness gives `e in im partial_2`; if `x_j` are its
   coefficients in `partial_2 h_j`, then `x_1 Lambda+...+x_m Lambda=Lambda`.
   The source's `m>=3` condition permits Lemma 2.3, after which slides among
   index-six handles make one coefficient into `e` exactly one (physical
   p. 12).
4. Only then use the stated local collar/trajectory construction to cancel
   the pair.  The short-period conversion later uses a compact invariant set:
   for `0<tau<tau_0`, `Phi_tau(p)=p` iff `V(p)=0` (Lemma 5.2, p. 15).

## Record boundary

The source's later Morse and Hamiltonian constructions remain required.  In
particular, this reference does not transfer its counterexample claim to a
new manifold or group without rebuilding the handle data.

Locators: physical pp. 5--7, 12, 15, and 19; Lemmas 2.2, 2.3, and 5.2.
