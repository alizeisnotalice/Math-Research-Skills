# No-power-relation premise in `EXT-0381`

## Source status and exact use

`EXT-0381`, *Linear forms in logarithms of rational numbers: an ineffective
measure with the best possible exponent* (Gregory V. Chudnovsky,
arXiv:2611.30820v1), is a 28-page preprint.  Its Theorem 1.1 on physical
page 1 assumes positive rational numbers with no nontrivial multiplicative
power relation and gives an explicitly **ineffective** lower-bound constant.
Physical pages 23--24 display the corresponding formal predicate
`NoPowerRelation`, the height convention, and the named Lean endpoints;
pages 25 and 27--28 describe the declared dependency closure and reproduction
setup.

The source's ancillary reproduction record is available at
<https://arxiv.org/src/2611.30820v1/anc/REPRODUCTION.txt>, and its additions
manifest at
<https://arxiv.org/src/2611.30820v1/anc/ADDITIONS-MANIFEST.json>.  They pin
the purported sources, compiler and Mathlib revision and report author-side
build/audit results.  No local Lean replay or independent audit of the
interpolation induction is represented by this skill.

## Admitted finite interface

For positive rational inputs, the script exactly decides `NoPowerRelation` by
forming the integer prime-valuation matrix.  If a nonzero integer exponent
vector has product one, it is a kernel vector; conversely every kernel vector
gives such a relation.  Full column rank over \(\mathbb Q\) is therefore
equivalent to the source predicate.

The output is only a reproducible caller-side certificate for that premise.
It does not prove the stated \(H^{-n-\varepsilon}\) bound, make its constant
effective, validate its height normalization for a requested application, or
turn the source's build report into a local formal verification.
