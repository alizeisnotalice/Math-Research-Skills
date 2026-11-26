# Polar transport after a strict Cuntz cutdown

## Contract

Let `C` be a C*-algebra, `d in M_n(C)_+`, `v in M_m(C)_+`, and let `epsilon>0`. Assume a supplied Cuntz-comparison witness has been compressed to an element `s in M_{m,n}(C)` satisfying

`||d-s*vs|| < epsilon/2`.

Put `h=(d-epsilon)_+`, `z=v^(1/2)s h`, and take the rectangular polar decomposition `z=w|z|` in `C**`. Functional calculus gives

`(epsilon/2) h^2 <= z*z <= (||d||+epsilon/2) h^2`.

Thus `Her(|z|)=Her(h)` and the polar support satisfies `w*w=e_h`, while `ww*<=e_v`. For every `k in Her(h)`, cutoff functions `g_j` vanishing near zero give `w g_j(|z|) in M_{m,n}(C)` and `w g_j(|z|)k -> wk`; hence `wk` and `wkw*` are algebra elements. Consequently

`theta(k)=wkw* : Her(h) -> Her(v)`

is an injective *-homomorphism. For `l>=0` and `tau>=0`,

`theta((l-tau)_+)=(theta(l)-tau)_+ ~_Cu (l-tau)_+`,

and `theta(Her(l))=Her(theta(l))`. The same support identities after matrix amplification give equality of every represented norm for a finite tuple transported from a common source.

The first inequality follows from `h d h >= epsilon h^2` and the approximation bound; the upper one from `s*vs <= d+(epsilon/2)1` in the unitization. Polar decomposition and the cutoff approximation prove the algebra-membership assertion. The equations `w*w=e_h` then prove multiplicativity, injectivity, functional-calculus compatibility, and the norm statement after normal extension of each representation.

This independently rederives the reusable local step in Lemma 2.2 and the common-source observation on the next page of *Weak pure infiniteness and O-infinity absorption*, OpenAI, 2026, PDF pp. 8–9, SHA-256 `2de287a58acb717007da6bbb6085d3150fba826131877a26c4328565c9208aca` (official fixed source: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/paper.pdf>).

## Exact finite-dimensional check

Take `C=complex`, `n=1`, `m=2`, `d=3`, `v=diag(4,1)`, `epsilon=1`, and `s=(sqrt(3)/2,0)^T`. Then `s*vs=d`, `h=2`, `z=(2sqrt(3),0)^T`, and the polar part is `w=(1,0)^T`. Therefore `theta(x)=diag(x,0)`, so `theta(h)=diag(2,0)` lies in `Her(v)`, preserves every positive spectral cutdown exactly, and is isometric. This verifies the contract in a concrete exact model, not the general comparison premise.

## Boundary

The contract needs a strict positive cutoff and an actual comparison/approximation witness. The polar witness is generally bidual-valued. No conclusion here supplies Cuntz comparison, proper or strong pure infiniteness, amplification removal, nuclearity/exactness, or `O_infinity` absorption.
