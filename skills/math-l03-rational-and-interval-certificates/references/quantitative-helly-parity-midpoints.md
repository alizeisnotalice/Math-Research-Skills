# Parity midpoint triples in a lattice polytope

Source: Horace Dong, *The discrete quantitative Helly number for five common lattice points*, author manuscript, 23 November 2026, local PDF SHA-256 `3e0f7a08ccc433dc1e80d0c02d9e0d96572d2617bac6dc0efaa29e2fe72113a5`, physical pp. 4--5, Lemmas 1--2 and Proposition 2.

For three distinct integer points in one mod-two residue class, their three pairwise midpoints are distinct integer points.  They recover the original triple by
\[
 a=u_{ab}+u_{ac}-u_{bc},\quad
 b=u_{ab}+u_{bc}-u_{ac},\quad
 c=u_{ac}+u_{bc}-u_{ab}.
\]
The checker exhausts triples in a supplied finite class and verifies this injection exactly.

```sh
python3 scripts/check_parity_midpoint_triples.py examples/parity-midpoint-triples.json
```

For a lattice polytope, convexity places these midpoints in the polytope and their being proper midpoints makes them nonvertices.  The run checks only a supplied finite class.  It does not certify the global capacity bound, the low-dimensional enumeration, the polytope-to-Helly transfer, or the stated sharp quantitative Helly numbers.
