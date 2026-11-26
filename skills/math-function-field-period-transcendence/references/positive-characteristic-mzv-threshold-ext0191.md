# Positive-characteristic MZV threshold

## Source and scope

This is a positive-characteristic result about Thakur multiple zeta values.
It does not transfer to classical multiple zeta values, Euler's constant, or
characteristic-zero q-series.

B.-H. Im, H. Kim, and T. Ngo Dac, *The threshold for linear independence of
multiple zeta values in positive characteristic*, local arXiv:2604.25451v2,
dated 11 September 2026. The supplied 48-page preprint is used at physical
pp. 5 and 8--10. The source proves that all Thakur MZVs of weight strictly
below `2q+1` are linearly independent over `F_q`, and displays one explicit
`F_q`-linear relation of weight `2q+1`.

## Callable interface

Give a finite-field order `q`, together with MZV indices interpreted in the
source's Thakur convention. First verify that `q` is a prime power and that
every supplied index has positive entries and the intended total weight. The
included checker reproduces the twelve index tuples in the displayed
weight-`2q+1` relation and verifies their weights. It verifies only the
combinatorial form of the statement.

```sh
python3 scripts/check_positive_characteristic_mzv_threshold.py 3
```

The linear-independence conclusion requires the source's definition of the
Thakur MZVs over the specified function field and its relation operator. The
checker does not construct Carlitz multiple polylogarithms, compute MZVs, or
prove the relation. For a requested linear relation, retain the finite field,
the coefficient field, the complete tuple list, and the source theorem's
weight range.

## Dependency boundary

The proof transfers MZV relations to Carlitz multiple polylogarithms and uses
the revised relation algorithm and its weight-preserving operator. Those are
proof dependencies of the cited theorem. Neither a finite collection of
numerical values nor a classical shuffle identity supplies the required
positive-characteristic object.
