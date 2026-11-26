# Exact sawtooth/Hermite phase certificate

**Scoped reference.** This is an exact finite checker for the rational-input
case of a common-phase fractional-part inequality.  It does not certify a
lattice covering-radius theorem or an external Lean formalization.

## Source and exact locus

Horace Dong, *Covering minima of the standard terminal simplex and a discrete
surface area bound for the covering radius of simplices*, author-hosted
manuscript dated 22 November 2026, 13 physical pages, SHA-256
`1536f6a641b5eb241191a66351eeaac8b7af17d3cedc88e0ddbf85bf4ab406ef`.

Physical p. 4 states Hermite's identity and Lemma 5.  For a finite nonempty
index set, positive integers `q_j`, positive weights `c_j`, and real `x_j`,
with `W=sum_j q_j c_j`, the lemma states the existence of a common phase `t`
such that

\[
 \sum_j c_j\{x_j+q_jt\}
 \leq \frac12\left(\sum_jc_j-
       \frac{\sum_jq_jc_j^2}{W}\right).
\]

The proof on physical pp. 4--5 takes the finite collection of jump phases
`e_{j,k}=-(x_j+k)/q_j`, applies Hermite's identity to the centered sawtooth,
and averages the values at those phases.  It therefore supplies an explicit
finite witness set, even though the stated lemma permits arbitrary real data.

## Finite interface

For rational `x_j,c_j`, the checker enumerates precisely those `e_{j,k}` using
`Fraction`, evaluates every fractional part exactly, and emits a witness and
the exact left side/right side.  A true result certifies the displayed
inequality for that supplied rational instance only.

```sh
python3 scripts/check_sawtooth_phase.py examples/sawtooth-phase-positive.json
python3 scripts/check_sawtooth_phase.py examples/sawtooth-phase-singleton.json
```

## Boundary

The source then combines Lemma 5 with a kernel-rounding induction and with
determinant/barycentric identities to prove its stated covering results
(physical pp. 5--7).  Those steps require their separate geometric input and
are intentionally not transferred by this finite phase checker.  The source's
claims of Lean verification are external-repository claims and are not used
here.
