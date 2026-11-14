# Negative examples: do not transfer across sampling rule or tree model

## Random pair is not fixed circular separation

RT002's Theorem 1.6/2.4 selects two distinct leaves uniformly over all pairs. Under the paper's h-ansatz it proves their CTCS time-height correlation is (O(1/\log n)). A127 instead fixes the original interval/circular leaf order, chooses a uniform random cyclic shift, and uses a prescribed circular gap (r_n). The pair law is conditional on this distance. The random-pair theorem does not imply the A127 limit (1-\alpha), even though both pairs have uniform one-leaf marginals. Similarly, RT003's exact branchpoint law for two random leaves and RT004's single-leaf CLT do not identify that distance-conditioned covariance.

## Conditioned-GW CLT is not automatic for Beta splits

RT020 assumes a critical offspring law (E\xi=1), (0<\operatorname{Var}\xi<\infty), and a toll meeting conditional-moment decay and summability hypotheses, with n restricted to sizes for which the conditioning event has positive probability. Its proof conditions an i.i.d. degree sequence. At the finite-support CLT step Cov(Y,S_n)=-\mu and the source uses \(\widetilde Y_n=Y_n+(\mu/\sigma^2)(S_n-n)\), leaving variance correction \(-\mu^2/\sigma^2\). The uniform-fringe limit is the ordinary GW tree; the Kesten tree is a separate root-local limit. A size-m Beta clade splits according to \(q(m,i)\propto1/[i(m-i)]\), which is size-dependent; resemblance of a recursive sum or fringe description does not establish an i.i.d. offspring representation. Do not cite RT020 for Beta-splitting without proving that representation and checking the exact toll and variance gates.
