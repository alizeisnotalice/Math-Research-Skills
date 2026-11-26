# E-value normalization and singularity gate

This is an admission rule for a proposed \(E\)-function route. It is deliberately
not an irrationality criterion for the Euler--Mascheroni constant.

## Source and checked version

S. Fischler and T. Rivoal, *On the singularities of differential equations
satisfied by \(E\)-functions*, arXiv:2604.20332v1 (22 April 2026), local source
07_Irrationality_Transcendence_Compendium/PDF/EXT-0218_On_the_singularities_of_differential_equations_satisfied_by_E_functions.pdf,
SHA-256
6bc1905029fddd975004f55ca88ac31c05f5532defb4d1f392978252ea1b9728.
The local title page and arXiv record agree on the v1 identity. This is a
preprint, not a formally published claim in this admission.

The operative statement is Theorem 3 on physical p. 3: for every
\(\xi\in\mathcal E\), there is an \(E\)-function \(f\) with \(f(1)=\xi\) for
which \(1\) is not a singularity of the minimal homogeneous or inhomogeneous
differential equation of \(f\). Theorem 4 on pp. 3--4 is the stronger finite
interpolation statement. For distinct nonzero algebraic
\(\alpha_1,\ldots,\alpha_N\), prescribed \(\xi_{n,t}\in\mathcal E\), and
\(0\leq t<T\), it produces \(f^{(t)}(\alpha_n)=\xi_{n,t}\), with

\[
 \alpha_n\text{ singular for the constructed minimal homogeneous equation}
 \quad\Longleftrightarrow\quad
 \{\xi_{n,t}:0\leq t<T\}\text{ is }\mathbb Q\text{-linearly dependent},
\]

and with the inhomogeneous version obtained by adjoining \(1\) to that set.

## Dependency spot-check

The source invokes the refined Siegel--Shidlovskii result in Theorem 6 (p. 5)
and the quotient property in Theorem 5 (p. 3). We checked the actual local
dependency F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
Annals of Mathematics 163 (2006), physical pp. 1--5, local SHA-256
e5c83265d88922078fbe1554d0197b42acd195be1e4d9813881dc1caa2be7815:
Corollary 1.4 on p. 3 gives linear independence at a non-singular algebraic
point, and Theorem 2.1 on p. 4 is the nonzero-singularity input. The existing
Fischler--Rivoal *Arithmetic theory of E-operators* source, SHA-256
40ef2ae20cf57ceae3f4a3b849d0e83aaca6a0f9d917adfddaa840bc0635ec46,
pp. 1--3, was also checked only for the separate E-value/E-operator boundary.

## Procedure

1. Give a proof certificate that every desired target value is in
   \(\mathcal E\). Naming a special constant or observing a numerical fit is
   not such a certificate.
2. Specify the finite nonzero algebraic nodes and requested derivative values.
   Check nodes are pairwise distinct. The helper accepts rational nodes only
   and exactly verifies this structural part.
3. Prove, rather than merely declare, the indicated \(\mathbb Q\)-linear
   dependences or independences. The theorem transfers the proved status to a
   singularity statement for its constructed function. It does not decide the
   status.
4. Only after Steps 1--3 may a regular-point E-function theorem be applied to
   the constructed witness. Record that the existence proof is not an algorithm
   producing its minimal operator or coefficients.

For \(\gamma\), stop at Step 1 unless an actual proof of
\(\gamma\in\mathcal E\) is supplied. Neither the integral in EXT-0029 nor an
extended-E approximation establishes that membership. Consequently this gate
does not turn a representation of \(\gamma\) into an irrationality proof.

Run the structural helper with the included manifest:

    python3 -B scripts/check_e_value_normalization.py examples/e_value_normalization_manifest.json

Its output is a check of the exact rational nodes and a restatement of the
declared, externally proved relation status. It is not a dependence oracle.
