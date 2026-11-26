# Twist selection from congruence and density inputs

Source SHA-256: `bdb2f21b345a4f0fc9943a4e39bee27fedae5cf1e6842c40b3a77bd528ddea01` (82 physical pages; Wave 4 index checked). Physical p.7, Lemma 2.3 supplies the interface.

Given an elliptic curve `A0/Q`, conductor `N`, and an odd prime `p`, the stated density input is used to choose coprime negative odd fundamental discriminants `D,D'` such that primes dividing `2Np` split in both, `(D/|D'|)=1`, and the three twists `A0^D`, `A0^{D'}`, `A0^{DD'}` have the smallest analytic rank allowed by their signs. The construction first imposes finitely many positive-density congruence classes, excludes finitely many fields, then applies the stated analytic twist-density theorem; after fixing `D`, it repeats for `D'` and may impose `D' == -1 mod |D|`.

Finite output: candidate discriminants plus certificates of squarefreeness, fundamentality, congruences, coprimality and splitting. The analytic-rank property is an imported density premise, so never represent finite congruence search as a certificate of it.

## 固定来源

- 物理页 7。Lemma 2.3 (physical p.7) SHA-256 `bdb2f21b345a4f0fc9943a4e39bee27fedae5cf1e6842c40b3a77bd528ddea01`。[The Selmer converse for elliptic curves at every prime](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf)
