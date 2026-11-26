# Exact scalar witness

Run:

```sh
python3 scripts/check_scalar_witness.py
```

The checker uses `fractions.Fraction` and reports a pass only if the source
Riccati identity and the final 2-by-2 commutator identity both hold exactly.
For this instance the target has Gram matrix with trace (4) and determinant
(0), so its operator norm is exactly (2).

This is a finite scalar test over \(\mathbb R\) or \(\mathbb C\), not a test of a
finite-von-Neumann-algebra uniform bound.
