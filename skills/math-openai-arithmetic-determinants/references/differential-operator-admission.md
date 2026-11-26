# Differential-operator admission before determinant arguments

Use this check when an E- or G-function construction is proposed as an input to a determinant argument.  It is an admission check, not an irrationality proof and not an implementation of an E-function relation algorithm.

## Required data

Record the exact differential operator, the claimed function class, and the intended algebraic evaluation point.  Keep the following questions separate.

1. Is the displayed function an E- or G-function under the applicable strict or wide definition?
2. Is the displayed operator minimal for that function?  Minimality is not supplied by a numerical differential-equation fit.
3. At the proposed E-value, does the relevant system have an allowed nonsingular presentation?  A root of a cleared denominator needs a separate singularity analysis.
4. Does the arithmetic goal need only a relation ideal, or also a nonzero integer determinant, height bound, and analytic upper bound?  The latter three are independent obligations.

For a finite audit of a candidate operator written in Euler form
\(N(t)\Delta^m-\sum_{j=1}^mP_j(t)\Delta^{m-j}\), use the degree test below only after the equality is proved:

\[
 r_m=\deg P_m=\deg N+1,\qquad \deg P_j<r_m\quad(1\le j<m).
\]

When it holds and the starting coefficient row is nonzero, Matala-aho's determinant theorem gives nonvanishing of its consecutive polynomial determinant.  The test supplies neither a minimal operator nor the integral and analytic estimates needed for a value theorem.

## Source boundary

- Fischler--Rivoal, *Effective algebraic independence of values of E-functions*, arXiv:1906.05589v1 (2019), pp. 1--3 and proof roadmap pp. 3--7.  Theorem 4 is an existence algorithm for relation ideals.  Its source proof explicitly routes through a differential-system relation computation, Beukers lifting, and Groebner elimination.  The authors state that the differential-Galois component was not then implemented.  Do not represent this as a runnable black-box decision procedure.
- Matala-aho, *An analogue of Siegel's determinant*, arXiv:2209.12719v1 (2022), pp. 1--5.  Theorem 3.1 proves the above degree criterion by a unique highest-degree determinant term.  It is a nonvanishing component only.
- Lepetit, *Le theoreme d'Andre--Chudnovsky--Katz « au sens large »*, arXiv:1902.07049v4 (2021), pp. 1--5.  Theorem 1 requires a **minimal** annihilator of a wide G-function and yields regular singularities and rational exponents.  It is structural background, not a certificate that an arbitrary fitted operator is admissible.

None of these sources puts Euler's constant into the required E-value class.  In particular they cannot be used to infer an arithmetic property of gamma without a separately proved representation and every remaining determinant/height/remainder condition.
