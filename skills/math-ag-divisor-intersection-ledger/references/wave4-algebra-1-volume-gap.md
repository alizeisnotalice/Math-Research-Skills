# Wave 4 algebra-1: cyclic-slice monomial valuation bound

OpenAI, *The normalized-volume gap in dimension four*, SHA-256 `6d58101115e4bf4f963ea2bc4e301f041eaff601e3b325ec475200e43e3031a4`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf), physical p. 8, Lemma 3.3.

On the source's smooth algebraic cyclic slice cover, take the monomial valuation with weights `(1,alpha,alpha,alpha)` and restrict it to the cone field. With punctured-cone stabilizer order `m`, Hilbert leading coefficient `h`, and slice parameter `r`, the source states

`A_C(v_alpha)=r+3 alpha`

and

`vol(v_alpha) <= h (1+alpha (m h)^(1/3))^3`.

The procedure is: evaluate homogeneous elements by `j+alpha*ord_slice`, compare the finite quotient length with character-compatible slice jets, use the simplex count `ell^3/(6m)+O((ell+1)^2)`, and integrate the minimum of the Hilbert and jet cubic profiles. The two profiles cross at `z_0=(1+alpha(mh)^(1/3))^-1`.

`scripts/wave4-algebra-1-monomial-volume.py` checks only the displayed algebra when `m*h` has an exact rational cube root. It is not a normalized-volume calculator: smoothness of the cover, character generation, Hilbert asymptotics, finite-map discrepancy, and the divisorial-infimum interpretation must be separately provided.
