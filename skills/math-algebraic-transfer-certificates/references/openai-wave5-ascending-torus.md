# Ascending-torus finiteness interface

**Status:** proposed skill, not installed.

**Pinned original:** *A universal group of type F∞*, SHA-256 `67e7907dc8afc00512ff80ba196072860e0d237e5703d9f013af4dbfde835733`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf), physical pp. 8–10, Theorem 5.1 and its finite-chain criterion.

Input an injective endomorphism `f:U->U`, finite presentation/presentation transfer to the comparison group, and explicit bounded chain data. The candidate ascending torus is

`T(U,f)=< U,t | t^-1 u t=f(u) >`.

For each requested degree, supply a finite chain complex, an iterate `F=(f^k)_*`, a common finite bound on `H_q`, and the checked identity

`partial H_q + H_{q-1} partial = F_q-c_q`.

Verify the identity degree by degree and the stated commutation constraints, then invoke the criterion at the requested finite skeletal level. Never claim `F∞` from a finite prefix: the all-degree family remains required.
