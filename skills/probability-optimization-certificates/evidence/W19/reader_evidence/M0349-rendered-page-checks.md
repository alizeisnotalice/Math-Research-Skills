# M0349 rendered-page evidence

- Source: `evidence/fulltexts/M0349.pdf`
- SHA-256: `6d4d2eaa2dd40389fa75fbdc26f4e37f863806d734a6bbbf02005271cc08fea2` (163 physical PDF pages).
- Page convention: physical PDF pages are used below. The article starts on PDF p.1, which is printed Acta Numerica p.287; p.1 has the title, author, corrections list, and article text beginning. It is not an empty correction cover.

| Physical PDF page | Rendered image | Visual check |
|---:|---|---|
| 1 | `evidence/W19/rendered/M0349-p1.png` | Title/author, corrections list, and article opening; printed article p.287. |
| 109 | `evidence/W19/rendered/M0349-p109.png` | Theorem 14.2 hypotheses: residual blocks, candidate feasible primal tuple/caps, bound formula, and nonnegative-residual clause. |
| 110 | `evidence/W19/rendered/M0349-p110.png` | Proof identity `Σ⟨C_j,X_j⟩−bᵀy=Σ⟨D_j,X_j⟩`; trace lower estimate; if `d_j≥0`, then `λ_min(D_j)≥d_j≥0`. |
| 129 | `evidence/W19/rendered/M0349-p129.png` | §16.1 states `X,Y` are two real Hilbert spaces and sets the Frechet derivative. |
| 130 | `evidence/W19/rendered/M0349-p130.png` | Dual-and-symmetric branch uses `Y=X′`, the inner product, Riesz map `Φ`, and symmetry of `Φ⁻¹L`. |
| 152 | `evidence/W19/reader_batches/L01_B2/rendered/M0349-p152.png` | Figure 16.2: successful `(A,B)=(6,2)` and unsuccessful `(6,26)` examples; text says `0<A<B` remains of interest and verification has not succeeded for that general case; acknowledgments follow. The page was read from the render because text extraction did not yield usable complete text. |

The 109–110 trace argument supports the strict subcase recorded in the mother card: when all `d_j≥0`, every residual block is PSD, the trial dual vector is feasible, and weak duality gives `p*≥bᵀy`. It does not establish a negative-residual correction from one pointwise cap.
