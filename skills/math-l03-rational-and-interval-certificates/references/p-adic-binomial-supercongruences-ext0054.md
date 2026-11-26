# Parameter-gated binomial supercongruences (EXT-0054)

Verified source: arXiv:1605.09179v1, local SHA-256 `b4c4a412d92c09005cb74d3673a5951fd6110d826f792f05029deecdc2227c0d`, 20 physical pages.

For a prime `p>3` and `a in Z_p` with `a not == 0 (mod p)`, physical p.6, Theorem 2.1 gives a mod-`p^2` evaluation of a half-truncated binomial sum coupled to a full alternating binomial sum, split according to the least residue `<a>_p <= (p-1)/2` or not. It also gives the full alternating sum in Bernoulli-polynomial terms. Physical p.8 obtains three concrete hypergeometric-looking sums by `a=-1/4,-1/3,-1/6` and the listed Bernoulli-to-Euler/`U` substitutions.

Actual proof interface used: write `a=<a>_p+pt`; p.6 first proves the `pt` base contribution is zero modulo `p^2` using the cited harmonic-square congruence, then expands the finite sum by residues `r` and invokes Lemma 2.1. The substitutions at p.8 additionally use cited identities for `E_{p-3}` and `B_{p-2}`. Therefore a certificate must retain `p`, `<a>_p`, `t`, the residue branch, the modulus, and the imported congruence references.
