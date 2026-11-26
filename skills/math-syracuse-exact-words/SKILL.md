---
name: math-syracuse-exact-words
description: Verify a supplied finite valuation word for the accelerated positive odd 3x−1 Syracuse map, including its exact source and affine identity. Do not use it to infer predecessor density or a Collatz-type conjecture.
---

# Exact 3x−1 Syracuse words

Use this skill only when the terminal root `R` is a positive odd integer and
every supplied valuation is a positive integer.  It checks the finite inverse
recurrence, rather than searching an unbounded inverse tree.

Run:

```sh
python3 scripts/check_exact_word.py --root R --word a1,a2,...,ad
```

The command either rejects a nonintegral inverse step or reports the positive
odd source `x`, all intermediate odd values, and verifies both

\[
3^d x=2^{a_1+\cdots+a_d}R+
\sum_{i=1}^d3^{d-i}2^{a_1+\cdots+a_{i-1}}
\]

and every exact valuation `v_2(3y-1)=a_i`.  Empty words, even/nonpositive
roots, and nonpositive valuations are outside the interface.

This finite decoder does not give an inverse-tree count, a density lower bound,
or any conclusion about the ordinary `3x+1` map.  Those claims require
additional global arguments not checked by this skill.  For provenance and the
source proof of the decoder, read
[the source boundary](references/syracuse-decoding.md).
