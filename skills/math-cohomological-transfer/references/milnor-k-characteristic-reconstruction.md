# Mod-p Milnor K reconstruction interfaces

Sources: *Reconstruction from Milnor K-theory modulo the characteristic*, SHA
`df8a6b4a54b121c692f7221e7b606be0dde89351fcb9ab5bb3853f7c2da4da90`,
physical pp. 3--4; and *Reconstruction of Function Fields from Mod-ell Milnor
K-Theory*, SHA `fafdf71eafc4700ada91598eba0620dc3263dd48b5879aa42af806254124bb2f`,
physical pp. 5, 18--19.

For a supplied characteristic-​`p` field `F`, set `C=F^p`. A declared finite
`p`-basis `s_1,...,s_e` gives monomials with exponents in `0,...,p-1` and
commuting `C`-linear Euler derivations `D_j`; on `C(s_j)`, their nonzero
eigenvectors are exactly `c s_j^i`. This is a useful finite-coordinate
interface only when the basis expansion is already part of the input.

For supplied `s,t`, the source's detector is: if `s` is not in `C` and the
mod-​`p` symbol `{s,t}` vanishes, then `t` lies in `C(s)`. Conversely,
`{t,c+d t}=0` for nonzero `c,d` in `C` whenever the two displayed arguments are
defined. Record whether a computation is using the symbol relation or merely a
formal tensor presentation; do not infer field reconstruction from a finite
sample.

The companion source packages compatibility as preservation of alternating
character pairs, namely
`f(x) g(1-x)=f(1-x) g(x)`. Its five-fibre Riemann--Hurwitz estimate is a
conditional degree bound once the named residual curves, anchor classes and
point-order support counts have been supplied. It is not a finite valuation
recovery routine.

## 固定来源

- 物理页 3, 4。Lemmas 2.1--2.4: p-bases, commuting Euler derivations, a vanishing-symbol detector, and affine-line Steinberg symbols. SHA-256 `df8a6b4a54b121c692f7221e7b606be0dde89351fcb9ab5bb3853f7c2da4da90`。[Reconstruction from Milnor K-theory modulo the characteristic](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf)
- 物理页 5, 18, 19。Section 2.1 defines alternating character pairs; pp.18--19 give the finite five-fibre degree inequality used in the reconstruction route. SHA-256 `fafdf71eafc4700ada91598eba0620dc3263dd48b5879aa42af806254124bb2f`。[Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf)
