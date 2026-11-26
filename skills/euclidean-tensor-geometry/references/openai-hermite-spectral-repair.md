# Finite Hermite spectral repair

OpenAI, *The logarithmic exponent of finite Fourier transforms*, physical pp.16–19, SHA-256 `275bf75a814d5dcffb57ee906e5b7b90d817fbfb0eef66dfd89940b118047523`.

Given a commutative ring with invertible `ell`, pairwise-unit Vandermonde nodes, a target `z` with `z^ell=1`, a predictor with known error support `J`, and `|J|<=s`, Lemma 4.4 uses `s` parity checks to recover the error. The polynomial `g(y)=y-ell^{-1}y(y^ell-1)` fixes `z` with zero derivative there; the source's right-inverse correction then cancels the error on `J` and outside it.

This is a supplied-data batch repair contract. It does not build the predictor, frequency routing, or a transform-complexity bound.

## 固定来源

- 物理页 16, 17, 18, 19。Theorem 4.1, Lemma 4.2, and Lemma 4.4 full-rate Hermite repair. SHA-256 `275bf75a814d5dcffb57ee906e5b7b90d817fbfb0eef66dfd89940b118047523`。[The logarithmic exponent of finite Fourier transforms](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-exponent-of-finite-Fourier-transforms-November-24-2026/paper.pdf)
