# Negative examples: transfers that need another proof

## 1. Replacing a tensor norm by the matrix spectral norm

For (A=\operatorname{diag}(1,-1)) and (p=4),
\[
\sup_{\|x\|_4\le1}|x^TAx|=1,
\qquad
\sup_{\|u\|_4,\|v\|_4\le1}|u^TAv|=\sqrt2.
\]
For (I_2), the diagonal symmetric ℓ(_4) norm is √2 while the Euclidean spectral norm is 1. These exact values are numerically checked by the local MATLAB script `probability-skills-20261113/evidence/W12/checks/norms_lp.m`; the analytic proof is in `evidence/W12/checks/norms_lp-proof.md`. Thus neither the diagonal/full ℓp distinction nor the spectral/ℓp distinction may be erased. W12-002 permits only an order-dependent polarization factor between the first two for symmetric tensors.

## 2. Promoting (p\ge2r) to all (p\ge2)

Theorem 1.2 in W12-002 has the target exponent when (p\ge2r). If (p<2r), its upper exponent is (1/2-1/(2r)), which is strictly larger than (1/2-1/p). The theorem therefore does not prove the missing low-(p) C120 range.

## 3. Promoting a two-block Wishart result

W12-029’s explicit formula and quantitative GPI apply to (d=2) disjoint principal minors. They do not imply the arbitrary-(d) C205 inequality. W12-031’s all-(d) integer-exponent recursion computes moments but does not show the required moment-product difference is nonnegative and does not cover arbitrary real exponents.

## 4. Conflating Wishart moments with event association

C205 is an inequality for positive powers of determinants. C206 is a lower-orthant event inequality for all determinant thresholds. Neither implication is supplied by W12-028. The proved completely-monotone/Laplace-order statements apply to their stated function class; determinant-sublevel indicators need a separate argument.

## 5. Transferring the scalar Gaussian product inequality to determinants

The W12-032 v1 identity is matched to the official arXiv abstract page and PDF by D03; its theorem is about positive powers of jointly Gaussian scalar coordinates. Wishart block determinants are nonlinear functions of Gaussian data, so the scalar-coordinate theorem does not establish C205, and it says nothing about C206's determinant lower-orthant events.

## 6. Extending noncommutative estimates to an Orlicz endpoint

The strong (L_p) row/column square-function equivalence, weak-Φ moment transform inequality, and Orlicz Burkholder estimates on index ranges wholly below/above 2 are distinct statements. None alone gives B171’s same-split, all-(t) weak endpoint or B172’s exact cross-2 Φ-modular upper bound.

