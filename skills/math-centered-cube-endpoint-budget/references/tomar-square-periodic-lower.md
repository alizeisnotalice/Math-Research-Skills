# Exact periodic lower certificate for centred squares

## Source and replay

Tejasvi Singh Tomar, *Bounds for the weak type (1,1) constant of the centred
maximal operator over squares*, physical pp. 2 and 8--9, gives a periodic
atomic-measure lower certificate. The public repository
tejasvi/square-maximal-weak-type, revision
3af09fc359ce262f4a7f63d34b0d97e6d4d95d1a, contains:

- lowerbound/c2lower_1p70272.json, SHA-256
  e2ca1616be95afa6680e3ccf157cc16fdd39026ad0f5fa79ebd32e5214779888;
- a standard-library integer sweep-line replay,
  lowerbound/check_exact2.py; and
- an independently structured replay,
  lowerbound/independent/lb_check2.py.

The two actual local commands were:

    python3 -I lowerbound/check_exact2.py lowerbound/c2lower_1p70272.json
    python3 -I lowerbound/independent/lb_check2.py lowerbound/c2lower_1p70272.json 1099511627776 CLAIM

where CLAIM is the exact fraction printed by the first command. Both returned
the same fraction, whose decimal value is about 1.7027237335963, and passed the
claimed 1.7027237335 lower bound.

## Scope

The two exact outputs equal the fraction
\[
\frac{482167717377842991882283179477574801392641890014291050323}
 {283174368139841919615520431313000857449005056000000000000}.
\]
The strict dyadic radius in Lemma 6.2 permits the transfer to integrable
functions by periodic truncation and smoothing. Use the stated period,
atomic masses and square normalization. The [kernel certificate](tomar-square-kernel-upper.md)
handles the upper bound.
