# Successive tensor vanishing over a noetherian ring

## Pinned source and transferred statement

- OpenAI, *Global Arthur Enhancements of Cuspidal Excursion Parameters*, preprint dated 5 October 2026, pinned repository revision `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`.
- Official PDF: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf>.
- Reviewed local byte SHA-256: `98c8561d3049c5b9ec55f39e980e1ec3a3b8b76adc1392ec4e5c3e71e83a50d4`; 69 PDF pages. Lemma 8.4 and its proof occur on PDF/printed p. 64; the concrete use begins on p. 65.

Let `S` be noetherian.  For `i ≥ 1`, let `v_i:D_i → S` be a morphism of `D(S)`, with `D_i` pseudo-coherent and bounded above.  Assume

\[
 v_i\mathbin{\otimes}^{\mathbf L}_S\kappa(\mathfrak p)=0
 \quad\hbox{in }D(\kappa(\mathfrak p))
\tag{1}
\]

for every `i` and every `\mathfrak p\in\operatorname{Spec}S`.  For every `K\in D^b_{\rm coh}(S)` and every `a≥1`, there is a `b≥a` such that

\[
 (v_a\mathbin{\otimes}^{\mathbf L}\cdots\mathbin{\otimes}^{\mathbf L}v_b)
 \mathbin{\otimes}^{\mathbf L}\operatorname{id}_K=0.
\tag{2}
\]

In particular set `K=S` and `a=1`.  This is the exact transfer boundary: (1) is derived base change, not vanishing merely on ordinary cohomology or on a chosen open set.

## Independent proof

For `a≤b`, write `D_{a,b}=D_a\otimes^L\cdots\otimes^LD_b` and `v_{a,b}=v_a\otimes^L\cdots\otimes^Lv_b`.  Say that a bounded coherent complex `K` has `P(K)` if for **every** starting index `a≥1`, some `b≥a` has `v_{a,b}\otimes^L\operatorname{id}_K=0`.

`P` is stable under shifts, finite sums, and triangles, provided one permits the new final index to be later than the old ones.  Indeed, in a triangle `K_1→K→K_2`, first choose a product killing `K_2`; naturality factors its map into `K` through `K_1`.  Apply `P(K_1)` starting at the index immediately after that first product. The resulting consecutive product kills the factorization.  Extending a killed product by further factors remains zero.

Over `S_p`, condition (1) says that `P(κ(p))` holds for all starts (take the first factor `v_a`).  At a generic point `p` of `supp K`, the complex `K_p` has finite-length coherent cohomology.  Finite dévissage by copies of `κ(p)`, the preceding triangle property, and shifts therefore give `P(K_p)`.  If `p_1,...,p_s` are the generic points of `supp K`, extend the finitely many resulting products to one common final index `b`; put

\[
z=v_{a,b}\otimes^L\operatorname{id}_K:D_{a,b}\otimes^L K\longrightarrow K.
\]

Then `z_{p_j}=0` for all `j`.  A finite tensor of pseudo-coherent bounded-above complexes has the same properties.  For a pseudo-coherent bounded-above source and a bounded coherent target, derived `Hom` commutes with localization: locally resolve the source by a bounded-above complex of finite free modules and the target by a bounded complex; in each degree only finitely many terms enter the Hom complex.  Hence `z_{p_j}=0` yields an element outside `p_j` annihilating `z`.  Thus `Ann_S(z)` is contained in none of the finitely many `p_j`; finite prime avoidance supplies

\[
s\in\operatorname{Ann}_S(z)\setminus\bigcup_jp_j.
\]

The equality `s z=0` factors `z` through `K'=fib(s:K→K)`.  The complex `K'` is bounded coherent and has support in `supp K\cap V(s)`, a proper closed subset because `s` avoids every generic point.  Noetherian induction gives `P(K')`; apply it at the starting index `b+1`. Then tensor naturality then makes the combined product `v_{a,c}\otimes^L id_K` zero.  The zero complex starts the induction.  This proves (2).

## Worked boundary check

For `S=k[x]`, take every `D_i=S/(x)` in degree zero and `v_i` the quotient-to-`S` **cannot** be supplied: there is no nonzero `S`-linear map `S/(x)→S`.  Replacing the target by `S/(x)` would change the theorem.  This guards a common invalid "example".

For a nonzero example take \(S=\mathbb Q[\varepsilon]/(\varepsilon^2)\), \(D_i=S\), and \(v_i\) multiplication by \(\varepsilon\). Each \(D_i\) is free of rank one. There is one residue field and every \(v_i\) reduces to zero there. A single factor is nonzero on \(K=S\), whereas two consecutive factors multiply by \(\varepsilon^2=0\).

## Exclusions

The proof produces no effective bound for `b`; it is unsuitable for numerical tensor-nilpotence bounds.  It also does not justify a claimed global Arthur enhancement: the source’s application additionally needs its pullback, equivariance, local-test and finite-level decomposition inputs.
