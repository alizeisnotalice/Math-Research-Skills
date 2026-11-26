# Low-Selmer BSD normalization ledger

Sources: `64b46603e174462e5bb32d242852eb7f0afe6e519f26534e42fd3f178a16b885`, physical p.3 (94 pages), and `734e4050dc8416c0f9ea7c9e15a29c6a8627feb53073e40b456d118f68d4dc5a`, physical p.4 (164 pages), each checked against the Wave 4 source index.

For `E/Q`, the first source fixes `s_q(E)=corank_Zq Sel_{q^infty}(E/Q)`, the all-real-components period `Omega_E`, finite component factors `c_l(E)`, and the canonical-height pairing `B`. Under `s_q(E) in {0,1}`, its Theorem 1.1 states `r(E)=ord_{s=1}L(E,s)=s_q(E)`, finiteness of `Sha`, and

`L^(r)(E,1)/r! = Omega_E Reg_E #Sha(E/Q) prod_l c_l(E)/(#E(Q)_tors)^2`.

The second source uses the same explicit height/regulator convention and, under `s_2(E)<=1`, states positivity of the normalized rational quotient and `v_2(Q_E)=v_2(#Sha)`. Its Corollary 1.2 transfers the conclusion when *some* full `p`-power Selmer corank is at most one.

Use this as a normalization ledger, not as a computation of Selmer groups, L-values, or Sha. Log which source's convention is used, the full local Kummer Selmer condition, the prime, rank-zero regulator convention, and the torsion-square denominator.

## 固定来源

- 物理页 3。Theorem 1.1 and equations (1.1)–(1.2) (physical p.3) SHA-256 `64b46603e174462e5bb32d242852eb7f0afe6e519f26534e42fd3f178a16b885`。[Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf)
- 物理页 4。Theorem 1.1 and Corollary 1.2 (physical p.4) SHA-256 `734e4050dc8416c0f9ea7c9e15a29c6a8627feb53073e40b456d118f68d4dc5a`。[The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf)
