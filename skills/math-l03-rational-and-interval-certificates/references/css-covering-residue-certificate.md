# Finite residue certificate for a lattice-simplex covering

Source: Horace Dong, *A non-hollow lattice 4-simplex of covering radius 2 outside the equality list of a conjecture of Codenotti, Santos and Schymura*, author manuscript, 22 November 2026, local PDF SHA-256 `520e8b99fbebb9f3a32398fa5d74f9ad368ee2fc91f64674857be6ab0a0592f9`, physical p. 4, Lemma 3 and the first half of Proposition 1.

For a supplied modulus `m`, integer weight vector `u`, and threshold `C`, define
\[
 \sigma(f,k)=\sum_i ((f_i+k u_i)\bmod m),\qquad 0\le k<m.
\]
The checker exhausts the finite residue cube and reports `max_f min_k sigma(f,k)`.  It also reports every score for an optional witness.  With `m=6`, `u=(2,1,1,1)`, and `C=8`, it checks all 1296 residues and the source witness `(1,1,2,4)`, whose six scores are `8,13,12,11,10,9`.

```sh
python3 scripts/check_residue_cover.py examples/css-residue-positive.json
python3 scripts/check_residue_cover.py examples/css-residue-negative.json
```

The first input is a finite certificate for the residue lemma.  The second reports `certificate_holds: false`.  Neither run proves the affine change of variables, the resulting covering-radius lower bound, the simplex's interior-lattice-point claim, or the equality-list exclusion.
