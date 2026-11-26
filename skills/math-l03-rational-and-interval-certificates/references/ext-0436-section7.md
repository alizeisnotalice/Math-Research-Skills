# Consecutive-powers Section-7 bound replay

Paper: Angelos Koutsianas and Nikos Tzanakis, *Sum of consecutive powers as a perfect power*, arXiv:2605.18348v1, physical pp. 12--16 (17 pages total), local SHA-256 `22c4e3fcfa12df53a3fbac7c2fcabe5b92877d377d7fe300d5ce7217de12f87a`.

The paper reduces its remaining cases to a two-logarithm inequality and gives the resulting \(n_0\) values in physical Table 2.  The public author repository named on physical p. 3 was recovered from its `master` branch after the former `main` URL was found not to exist.  The acquired source archive SHA-256 is `05067800ea54c8b733f95dfed4cd9cafec657146c79b90ad944cbeb4e3d9d92c`; its `bound_n/linear_forms_in_logarithms.py` implements that table.

`scripts/replay_section7_bounds.py` reconstructs the exact polynomial-coefficient portion and uses Arb 384-bit ball arithmetic for every logarithm, exponential, sign and floor.  It returned the public code's static `bounds_info.py` value for every one of the 24 rows (k=6,10,\ldots,98).  For each row requiring a root crossing it separately isolates the two adjacent signs; for the other Laurent parameters the (n_4) threshold itself dominates.

The integer threshold uses exact signed division before rounding. For the tail
crossing, the replay checks \(\log(a n_4)>1\), which makes
\(\log(a n)/n\) strictly decreasing for all \(n\ge n_4\). If the sign at
\(n_4\) is already negative, it additionally checks a negative derivative.
Otherwise it isolates adjacent integer signs on the decreasing branch. [Author code and bounds table](https://github.com/akoutsianas/SumOfConsecutivePowers/tree/83787e96ee0da4c6587c5bbb3ccc003da1c1448e/bound_n)

This validates a bounded numerical component of Section 7.  It does not prove the hypotheses that permit use of the two-logarithm estimate, nor the paper's modular/Thue computation.  The full author package explicitly requires Sage and Pari/GP for the small-exponent and newform stages; those stages were not replayed here.
