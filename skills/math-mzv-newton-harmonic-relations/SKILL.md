---
name: math-mzv-newton-harmonic-relations
description: Check finite Newton/binomial duality for positive multiple-harmonic indices exactly. Use to prepare finite inputs for Kawashima-type MZV relations, not to prove MZV independence or Euler-constant claims.
---

# Newton--harmonic duality for MZV relation inputs

Use this skill for exact finite checks of the binomial transform of weak
multiple harmonic sums. Read the precise normalization, published source,
and scope in the
[source note](references/kawashima-newton-harmonic-duality.md).

## Finite object and admissibility

An index is a nonempty tuple \(\mu=(\mu_1,\ldots,\mu_p)\) of positive
integers. Form its dual \(\mu^*\) by complementing the cut set of \(\mu\)
inside \(\{1,\ldots,|\mu|-1\}\). With the source's shifted weak sums
\(s_\mu(n)\), the finite identity to check is

\[
  \sum_{k=0}^{n}(-1)^k\binom nk s_\mu(k)=s_{\mu^*}(n).
\]

Keep the weak inequalities, final-index convention, and the `+1` shift in
the denominators fixed. Changing any of them creates a different identity;
do not reuse this checker without re-deriving the normalization.

## Exact replay

The checker uses rational `Fraction` arithmetic for five indices and
\(n=0,\ldots,7\):

```bash
python3 \
  scripts/check_kawashima_harmonic_duality.py
```

It should report the five checked `(index, dual)` pairs without an assertion
failure. For another finite index, compute the two rational sides with the
same definitions and retain the chosen index and tested range; a successful
finite range is not a universal proof.

## Boundary

The result is an exact finite identity useful for generating or screening
Kawashima-relation inputs. It does not establish a multiple-zeta relation
beyond the cited theorem, linear independence of MZVs, completeness of a
relation family, or any statement about Euler's constant.

## 文献复核采用的构件

- [Geometric regularized double-shuffle scope](references/ext0255-geometric-double-shuffle.md)
- [Motivic multiple-t regularisation boundary](references/motivic-multiple-t-regularisation-ext0174.md)

- [Bradley-normalized multiple q-zeta stuffles](references/wave8-candidate-10-q-stuffle.md)
