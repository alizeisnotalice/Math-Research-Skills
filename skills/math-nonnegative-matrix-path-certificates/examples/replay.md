# Exact replay

Run:

```sh
python3 -B scripts/check_odd_path_certificate.py
```

The positive and zero-boundary checks evaluate the finite odd path inequality
with `Fraction` entries.  The final check is the source's three-factor,
even-exponent obstruction: it is kept as a premise guard, not presented as a
counterexample to the two-factor even theorem.
