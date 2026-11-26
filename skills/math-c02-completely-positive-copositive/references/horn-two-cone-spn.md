# Horn two-cone rational certificate

The checker implements the finite example on physical pp. 28--29 of
Ahmadi et al., *Disjunctive Sum of Squares*, arXiv:2605.28674v1, local SHA-256
`6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c`. [arXiv v1](https://arxiv.org/abs/2605.28674v1)

It has one deliberately narrow contract: certify the displayed Horn matrix on
the two displayed cones. It is not a test for arbitrary copositivity, an
arbitrary P+N decomposition, or a disjunctive-hierarchy implementation.

Run the positive certificate:

```sh
python3 -B scripts/horn_spn_certificate.py --case positive
```

Both rejection paths must exit with status 2:

```sh
python3 -B scripts/horn_spn_certificate.py --case perturb-horn
python3 -B scripts/horn_spn_certificate.py --case perturb-coverage
```

The branch coverage is algebraic, not sampled: the checker verifies
`V1 L1 = V2 L2 = I`. For nonnegative `x`, the first formula has nonnegative
coordinates when `x4 >= x5`, and the second when `x5 >= x4`; those two cases
cover the orthant. It also verifies each congruence exactly over `Fraction`,
the rank-one PSD factorization `P_i = u_i u_i^T`, and entrywise
nonnegativity of `N_i`.
