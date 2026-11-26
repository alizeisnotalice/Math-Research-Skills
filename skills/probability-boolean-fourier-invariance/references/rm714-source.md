# RM(7,14) ANF witness extraction

Source record `e6ff49669127853f9c7817f1131e05e5b3125f10845552e17e8b6e0e8aa0191e`,
*Fourteen new weights of the Reed--Muller code RM(7,14)*, author manuscript dated October
2026, version 2.

Physical p. 4 states the exact inclusion-exclusion formula for an XOR of monomials and
lists ten explicit degree-at-most-seven ANFs. The `354` entry has monomial supports
\(\{1,\ldots,7\}\), \(\{8,\ldots,14\}\), \(\{1,2,3,5,6,7,11\}\),
\(\{1,3,6,7,10,12,13\}\), and \(\{3,4,6,7,10,12,13\}\). The checker derives its weight
from the displayed finite identity and then independently evaluates all \(2^{14}\) points.

The manuscript's broad spectrum and non-existence claims rely on a reported external Lean
repository, a 7,901-witness corpus, and cited reductions. They are not implied by this finite
ANF-weight certificate.
