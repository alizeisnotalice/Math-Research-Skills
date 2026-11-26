# Foulkes--Howe finite bidegree lowering

Source: *Quadratic stabilization of the canonical Foulkes--Howe map*, OpenAI Math commit `3344da59991ed94f9ba711217b29c1d760badfa6`, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf), SHA-256 `16b2feef6f939f6cf5bda458ab6392860a1a2a1a1dcb27c594960023625ec667`, Lemma 2 (physical p. 4).

For `n` pairs of variables `(U_i,Y_i)`, use

`D_{Y,U} = sum_i Y_i d/dU_i : R[U,Y]_(p,q) -> R[U,Y]_(p-1,q+1)`.

The source's displayed injectivity result is used in the regime `p>q`.  The script builds its exact integer sparse monomial matrix and computes rank over the rationals for a supplied finite `(n,p,q)`.  Optional rational coefficients additionally produce the exact lowered polynomial.  The finite rank result is a calculation for that instance; it neither constructs a Foulkes--Howe inverse nor establishes the paper's representation-theoretic theorem.

For routing, retain L17's requirements that any broader filtered-linear-algebra conclusion needs its own exact spaces and maps.  This component only supplies this explicit bidegree-lowering map.
