# Mahler polynomial-orbit vanishing gate

For an integer matrix `T` with nonnegative entries and a point
`x in (C^*)^n`, call `x` `T`-dependent when a nonzero integral row vector `mu`
satisfies

```
(T^k x)^mu = 1
```

on an arithmetic progression.  Theorem 2.2 of the checked source gives the following
exact gate: a nonzero polynomial `P` can vanish at `T^k x` for infinitely many
nonnegative `k` if and only if either `T` has a root-of-unity eigenvalue, or `x` is
`T`-dependent.  Thus, after both negatives are certified, every nonzero polynomial is
eventually nonzero on the orbit.

This is useful only as an orbit-nonvanishing input to a separately established Mahler
functional equation.  It does not establish convergence, regularity of a matrix system,
or algebraic independence of values.  In the source proof, the forward direction invokes
its Lemma 2.1 (a previously proved orbit-polynomial lemma); the reverse direction is the
explicit binomial construction on physical pp. 8--9.  Therefore this is a source-theorem
gate, not an algorithm deciding `T`-dependence.

Source: K. Nishioka, T.-a. Tanaka and Y. Tanuma, *Mahler Method and Vanishing Theorem*,
arXiv:2610.23435v2, physical pp. 7--9, Theorem 2.2 and Definition 2.3. The local source
is a current preprint; the later relation-lifting applications require their additional
admissibility, regularity and coefficient-field conditions.
