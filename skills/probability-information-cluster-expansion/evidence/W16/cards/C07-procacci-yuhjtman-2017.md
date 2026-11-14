<!-- Reader: W15; full local arXiv v2 PDF read; review pending. -->
# Aldo Procacci and Sergio A. Yuhjtman (2017), “Convergence of Mayer and Virial Expansions and the Penrose Tree-Graph Identity”

- Source: *Letters in Mathematical Physics* 107, 57–74 (2017), DOI [10.1007/s11005-016-0918-7](https://doi.org/10.1007/s11005-016-0918-7); [arXiv:1508.07379v2](https://arxiv.org/abs/1508.07379), last revised 9 Dec 2016. The local 15-page PDF has the arXiv v2 stamp but the manuscript body date 8 Nov 2018; retain both artifact markings. Local copy: `evidence/fulltexts/C07.pdf`, SHA-256 `c3dbf93d1cac198e6d9fafe655dd69a38ba09aa944daf273017aca0b74e5ce2f`.
- Reader: W15; PDF pp. 1–15, all sections and references.
- Model: continuous classical gas in `R^d`, inverse temperature `β`, grand-canonical fugacity `λ`, and a stable, tempered pair potential `V`. Stability means the total pair energy of every `n`-particle configuration is at least `−Bn`; tempering supplies the integrability required by the coefficient bounds.

## Main bound and proof chain

Theorem 1 (PDF pp. 4–5, Eqs. (2.12)–(2.15)) proves the Mayer coefficient estimate

`|Cₙ(β,Λ)| ≤ exp(βBn) n^(n−2) [Ĉ(β)]^(n−1)/n!`,  
`Ĉ(β)=∫_{R^d}(1−exp(−β|V(x)|)) dx`,

and absolute, volume-uniform convergence for

`|λ| < 1/[exp(βB+1) Ĉ(β)]`.

Proposition 1 (PDF pp. 5–6, Eq. (2.18)) is the tree-graph inequality for stable potentials. The proof in §§3–4 (PDF pp. 6–12) uses Penrose’s partition identity and a minimum-spanning-tree partition scheme with a deterministic tie-break. Stability bounds the extra-edge energy, leaving tree factors `1−exp(−β|V|)`; integrating along the tree gives `Ĉ(β)^(n−1)`, and Cayley’s count contributes `n^(n−2)`. Lagrange inversion then transfers the coefficient majorant to the virial-radius bound in Eq. (2.17). The source notes that its general bound can be improved for special subclasses such as Basuev potentials; it is not universally sharp.

## Full-text map

| Section | PDF pages | Coverage |
|---|---:|---|
| §1, Introduction | 1–3 | Mayer/virial context and Penrose tree-graph approach. |
| §2.1, Model | 3–4 | Stable/tempered pair-potential model and classical comparison bounds. |
| §2.2, Results | 4–6 | Theorem 1, Proposition 1 and induced virial-radius statement. |
| §3, Proof of Proposition 1 | 6–12 | General Penrose identity, MST partition scheme and completion of the tree bound. |
| §4, Proof of Theorem 1 | 12–13 | Integrates the coefficient majorant and derives the convergence radius. |
| §5, Comparison and conclusion | 13 | Model-specific comparisons and closing remarks. |
| References | 13–15 | Bibliography. |

## Transfer limit

This is a theorem about Mayer and virial series for stable, tempered continuous pair-potential gases. It does not establish an abstract cluster expansion for the deletion-channel information rate. A valid channel representation, activities, uniform bounds and justification of the entropy-rate/input-supremum limit would be needed before any transfer to B051.
