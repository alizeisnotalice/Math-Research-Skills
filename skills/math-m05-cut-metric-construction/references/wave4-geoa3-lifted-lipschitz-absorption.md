# Bi-Lipschitz absorption from a lifted correction

**Source.** OpenAI, *Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0*, Lemma 2.1, PDF pp. 3--4; SHA-256 `4779ddc34774d95aedfb77742849d2b9b4e9078dff503d82cef542539731d1dc`.

## Input contract

Let `D=E direct-sum_infty U`; give a bounded linear `Q:Z -> U`, a bi-Lipschitz bijection `g:D -> U`, and a Lipschitz `K:D -> Z` satisfying the exact lifted-correction identity `Q K(t,u)=g(t,u)-u`.  Record a lower Lipschitz constant `c_g` for `g` and the norms of `Q,K` when quantitative constants are wanted.

## Reuse

Define `F(b,t)=b+K(t,Qb)` from `Z direct-sum_infty E` to `Z`.  Its inverse is obtained constructively: for `d in Z`, write `(t_d,u_d)=g^{-1}(Qd)` and return `(d-K(t_d,u_d),t_d)`.  The source gives `Lip(F)<=1+Lip(K) max(1,||Q||)` and `Lip(F^{-1})<=max(1+Lip(K)||Q||/c_g,||Q||/c_g)`.

This is an identity-driven absorption interface.  It needs neither a linear section of `Q` nor a right inverse, but it cannot be invoked when `QK=g-P` holds only approximately.

## 固定来源

- 物理页 3, 4。Lemma 2.1 SHA-256 `4779ddc34774d95aedfb77742849d2b9b4e9078dff503d82cef542539731d1dc`。[Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf)
