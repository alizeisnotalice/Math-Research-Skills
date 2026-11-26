# Packed A7 terrace witness

## Source and checked statement

Horace Dong, *A terrace for the alternating group A7* (author manuscript,
22 November 2026), physical pp. 2 and 4--5, states a 2,520-term terrace for
`A7`. The public repository `Horace-Maxwell/ai4math-results`, revision
`6334a95f2e0c2396f492f3476c1d4ce80e4106ab`, supplies the packed rows in
`lean/Research/TaskR/A7/Data.lean`.

The source encodes seven zero-based images in 21 bits (three bits per image),
with 64 rows in each hexadecimal block. `replay_packed_a7.py` verifies that
format directly, checks the normalized enumeration of all 2,520 even
permutations, and checks the paper's consecutive-quotient multiplicities.

## Scope

This is a finite certificate replay for that particular data file. It does
not replay the Lean kernel, verify the repository's broader consequences, or
construct a terrace for any other group.
