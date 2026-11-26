# Conditional discrete mixed-universality admission

Source: Roma Kačinskaitė and Kohji Matsumoto, *On mixed joint discrete
universality for a class of zeta-functions III*, arXiv:1905.12144v1 (29 May
2019), local source SHA-256
`ea7022f4158577da1eb9a3a39369770f7d6d898baea8e6b475501ccbbfd06d60`,
physical pp. 2--15.  Theorem 3 is on p. 6 and Theorem 4 continues there; the
proof route is the weak-limit theorem of §§2--3 and support calculation of §4.

This is a conditional interface, not a procedure for deciding rational linear
independence.  To call Theorem 3 (one common step `h`), supply and certify:

* a `phi` in the source's Steuding class, including its `sigma_*`;
* `alpha_j in (0,1)`, nonzero periodic coefficient sequences `B_jl`, and
  `rank(B_j)=l(j)` for every `j`;
* Q-linear independence of
  `{log p} union {log(m+alpha_j)} union {2*pi/h}`;
* compact `K_1 subset D(sigma_*,1)` and `K_2,jl subset D(1/2,1)`, each with
  connected complement, with `f_1` nonvanishing and holomorphic/continuous on
  `K_1`, and every `f_2,jl` holomorphic/continuous on its domain; and
* an `epsilon > 0`.

The conclusion is a positive lower density of integers `k` for which all stated
uniform approximations by `phi(s+ikh)` and the selected periodic Hurwitz zeta
functions hold.  Theorem 4 has the same gates, replacing the independence set
with the source's set containing `h_1 log p`, `h_2j log(m+alpha_j)`, and `pi`,
and uses its distinct shifts.

Dependency boundary: the source's Lemma 5 invokes the discrete-torus
equidistribution result cited as Lemma 6 of its reference [11].  A caller must
either accept that cited input or independently establish it; no finite sampling
of shifts proves this conclusion.
