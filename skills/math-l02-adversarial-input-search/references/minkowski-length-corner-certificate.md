# Exact simplex-corner certificate for a Minkowski-length lower bound

Source: Horace Dong, *Lattice simplices whose Minkowski length exceeds the lattice diameter, and dilates whose Minkowski length is not quasi-linear*, author manuscript, 22 November 2026, local PDF SHA-256 `5070e4926a90b8a6a394013f023ca03b04706d71b36c667ff7ba3a6ab632b528`, physical p. 3, Lemma 1 and the lower-bound step in Proposition 1.

Given a full-dimensional integer simplex, an integer translation, and nondegenerate integer segments, the checker solves every barycentric coordinate system with exact rational arithmetic.  If all `2^k` corners lie in the simplex, convexity certifies that the translated sum of the `k` segments lies in the simplex, hence its lattice Minkowski length is at least `k`.

```sh
python3 scripts/check_simplex_corners.py examples/minkowski-tetrahedron-corners.json
python3 scripts/check_simplex_corners.py examples/minkowski-tetrahedron-outside.json
```

The first fixture checks the four corners of `(1,1,2)+[0,e_1]+[0,e_2]` in the source tetrahedron.  The second has an outside corner.  This supplies a lower-bound construction only.  It does not determine the exact Minkowski length, certify lattice diameter, prove an upper packing bound, or transfer a construction to arbitrary simplices.
