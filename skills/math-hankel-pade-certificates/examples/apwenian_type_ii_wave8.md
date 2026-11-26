# Exact replay

Run from this artifact directory:

```sh
python3 -B scripts/check_apwenian_type_ii_wave8.py --word 1,1,-1 --through 7 --base 2
```

The word `(1, 1, -1)` has odd length three and passes the source residue
predicate.  The script then checks seven exact integer Hankel determinants
and proves the elementary `P(2^(-3^m)) != 0` admission bound.  The all-order
Hankel conclusion remains source-derived, as recorded in the reference note.
