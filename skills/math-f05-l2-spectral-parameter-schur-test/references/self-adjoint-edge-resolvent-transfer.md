# Self-adjoint edge resolvent transfer

Source: *Ordinary two-point correlations of multiplicative functions*, SHA
`ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a`,
physical p.39, Lemma 8.1.

Given finite-dimensional self-adjoint `B_1,...,B_N`, an orthogonal projection
`P`, `||B_i||<=a`, and `sum_i ||B_i v||^2 <= b^2||v||^2` for `v=Pv`, form the
off-diagonal edge operator `(Bz)_i=sum_{j!=i}B_jz_j`. If its spectral radius
is bounded by `rho(B)`, then the source gives
`||P(sum_i B_i)P|| <= 3 max(a,b,rho(B))`. No commutation of distinct `B_i` is
part of the contract. Run the scalar two-vertex fixture checker in `scripts/`
for an exact finite replay; it is not a proof for arbitrary matrices.

## 固定来源

- 物理页 39。Lemma 8.1: finite-dimensional self-adjoint edge-operator resolvent transfer. SHA-256 `ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a`。[Ordinary two-point correlations of multiplicative functions](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf)
