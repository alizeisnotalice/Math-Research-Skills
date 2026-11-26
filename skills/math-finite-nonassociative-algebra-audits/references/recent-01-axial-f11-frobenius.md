# Four-dimensional F_11 axial-algebra replay

For the supplied four-dimensional commutative multiplication table over `F_11`, use `scripts/check_axial_f11_frobenius.py` to verify its basis idempotents, the Frobenius identity for the displayed diagonal form, the dimension of the space of associative bilinear forms, and the displayed basis swap. The check exhausts the 64 basis-triple form identities and uses modular row reduction on the resulting 64 by 16 linear system.

The source gives the multiplication table and the four claims on physical pp. 2--4. The finite replay establishes only the stated table identities. Axial fusion conventions, the literature question, and any Lean development are separate inputs.
