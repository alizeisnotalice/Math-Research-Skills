---
name: math-euler-series-continued-fraction
description: Convert a finite nondegenerate rational series segment to Euler generalized continued-fraction data exactly. Use for finite algebraic identity checks, not for convergence or irrationality claims.
---

# Euler series to a generalized continued fraction

Use this skill when exact rational terms \(a_0,\ldots,a_N\) must be rewritten
as the finite Euler generalized continued fraction behind a series expansion.
Read the pinned statement and its scope before relying on the transform:
[source note](references/mclaughlin-wyshinski-euler-transform.md).

## Admission conditions

Treat every input term as an exact rational number, encoded as `[numerator,
denominator]` with a nonzero integer denominator. The finite representation
implemented here is admissible only when

- every \(a_i\) for \(i\geq1\) is nonzero; and
- \(a_{i-1}+a_i\ne0\) for every \(i=2,\ldots,N\).

`a_0` may be zero. A one-term input is the trivial finite case. Do not
silently cancel or perturb a degenerate input: select another representation
or prove a separate limiting identity instead.

## Exact replay

Run the existing transformer on the supplied finite alternating-harmonic
example:

```bash
python3 \
  scripts/euler_series_to_cf.py \
  --input examples/alternating_pi_partial.json
```

The emitted `series_partial_sum` and `continued_fraction_value` must be the
same rational pair. For the included example both are `[263,315]`. The
[transformer](scripts/euler_series_to_cf.py)
uses `Fraction` arithmetic; retain the emitted input and output when the
identity is used as computational evidence.

## Boundary

This certifies only an equality of a chosen **finite** partial sum and its
finite generalized continued fraction. An infinite identity additionally
needs the source's convergence hypotheses for both expressions. It supplies
neither a tail bound nor positivity, integrality, nonvanishing, rationality,
or irrationality conclusion. In particular, the included alternating
harmonic prefix is not a certificate for \(\pi\).
