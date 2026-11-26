# Finite-field affine-line sum certificate

Source: OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness
Conjecture in Characteristic Two*, pinned `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`,
`paper.pdf`, SHA-256
`a97d7915d43b5112b11b7ae39619cf3a7b9c40f207f8f586fc28f22ff4406d12`,
physical PDF pp. 5--6, Lemma 2.2 and Proposition 2.3.
Official pinned PDF: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf>.

Let `Q` be a finite field of order `q`, `n >= 1`, and let `P` have total
degree at most `q-2`.  On an affine line, its restriction is a univariate
polynomial of degree at most `q-2`.  The constant term sums to `q=0` in
`Q`.  For `1 <= k < q-1`, choose `c in Q^*` with `c^k != 1`; multiplication
by `c` permutes `Q`, so `(1-c^k) sum_z z^k=0`.  Thus the sum of `P` on every
full affine line is zero.  Partitioning `Q^n` into parallel lines also gives
the full-space sum zero.

For the paper's pairing step, assume additionally that `q` is a power of
two with `q >= 4`, let `d0=(q-2)/2`, and interpolate indicator polynomials
`f_o` of total degree at most `d0` on a selected lower-set simplex.  Then
each entry `f_o f_{o'}` has degree at most `q-2`, so the lemma gives zero
line and full-space sums for the matrix `W_v=(f_o(v)f_{o'}(v))`.  If the
deleted points have coordinate-vector evaluations, subtracting their sum
from the full-space zero identity gives the claimed negative identity on
the retained points.  This transfer still requires independently checked
interpolation nodes, deletion data, and line incidence assumptions.

The accompanying exact checker only supports fields represented as
`GF(2^r)` by an irreducible binary modulus.  It validates the field
representation, total-degree gate, and enumerates every affine line before
reporting the line and full-space sums.  It is a finite instance check, not
a proof that arbitrary supplied data meets the interpolation or incidence
requirements, and it does not certify the group-algebra counterexample.
