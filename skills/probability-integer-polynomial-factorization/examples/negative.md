# Negative example — algebraic or scaled factors are not automatically probability factors

The raw factorization

`1+z+z^2+z^3 = (2+2z)(1/2+z^2/2)`

has nonnegative coefficients but is not in the monic normalization used by the 0–1 factor theorem; the first factor has leading coefficient 2. Reciprocal positive rescaling gives `(1+z)(1+z^2)`, which is monic and 0–1. The raw scaling is not a counterexample to fairness.

Likewise,

`1+z^3 = (1+z)(1−z+z^2)`

is an exact polynomial identity but one factor has a negative coefficient. It is not a PGF factorization and cannot be interpreted as independent integer-valued probability summands. A signed epsilon-relaxation result has the same model mismatch unless it separately proves nonnegative factors.

These examples check normalization and coefficient-domain guards; neither resolves A175.
