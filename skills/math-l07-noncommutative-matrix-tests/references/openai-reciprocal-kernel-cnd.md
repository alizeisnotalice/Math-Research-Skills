# Reciprocal-kernel finite CND certificate

Source 1. OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, physical pp.12 and 15–17, SHA-256 `7a65d7bc83270c2b1eccc49a3921fd61bc281283b7d0c3a5059df0a2f8778413`.

For a finite symmetric rational zero-diagonal matrix `D`, conditional negative semidefiniteness means `a^T D a <= 0` for every rational vector with coordinate sum zero. Use the basis `e_i-e_n`; the restricted matrix is `C_ij=D_ij-D_in-D_nj`. Thus `D` is CND exactly when `-C` is PSD. The helper checks this by exact principal minors.

Source 2. In the source's setting, property (P) for the bordered reciprocal matrix gives this restricted negativity after the substitution `x_i=K(p,s_i)a_i`. Supply the actual matrix and border vector; do not treat this finite check as a proof about Green functions, complete-Pick kernels, embeddings, or critical points.

## 固定来源

- 物理页 12, 15, 16, 17。Theorem 5.1, property (P), and finite resolvent-matrix passage. SHA-256 `7a65d7bc83270c2b1eccc49a3921fd61bc281283b7d0c3a5059df0a2f8778413`。[Strict hot spots and absence of interior critical points on smooth simply connected planar domains](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf)
