from fractions import Fraction as F

p = 3
source_sum_cubed = F(2**p, 2*p + 1)  # (2/(2p+1)^(1/p))^p
support_sum_p = F(2, p + 2)            # E[U^(p+1)+(1-U)^(p+1)] for U~Unif[0,1]
derived_factor_cubed = support_sum_p
assert source_sum_cubed == F(8, 7) and source_sum_cubed > 1
assert derived_factor_cubed == F(2, 5) and derived_factor_cubed < 1

print('C027 Find-process PDF p.29, p=3 exact coefficient check:')
print('Printed sufficient-condition coefficient = 2/(2p+1)^(1/p).')
print(f'Its cube at p=3 is {source_sum_cubed} > 1, so the printed condition is false at p=3.')
print('Independent disjoint-support calculation: E[U^(p+1)+(1-U)^(p+1)] = 2/(p+2).')
print(f'The derived contraction factor is (2/(p+2))^(1/p); its cube at p=3 is {derived_factor_cubed} < 1.')
print('The check distinguishes the source display from the separate integral derivation; it is not a substitute for the proof hypotheses.')
