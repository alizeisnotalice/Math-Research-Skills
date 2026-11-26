# Weighted Cartan-box calculus

**Status:** proposed skill, not installed.

**Pinned original:** *Quasi-isometric recognition of virtually polycyclic groups*, SHA-256 `c7261a742d7ca88303c7c38071e7e69fc2a53d953a1d7890fbcc5aeb04d137b2`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/paper.pdf), physical pp. 13–20, Lemmas 3.1–3.3 and (3.8).

Give a nilpotent Lie algebra basis `Z`, derivation weights `h_Z(E)`, BCH structure constants, and a finite list of weight-neutral brackets/products. The source's box is

`B_r(E,L)=exp_N(sum_Z [-L exp(r h_Z(E)), L exp(r h_Z(E))] Z)`.

Enumerate BCH monomials to its finite nilpotency class, check every required weight relation (schematically `sum_i c_i alpha_i=0`) exactly, propagate interval radii through the finite BCH polynomial, and retain its multiplicative constant. Without the fixed Lie model and constants, it is not a quasi-isometry recognition test.
