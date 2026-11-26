# Continued-fraction brackets for `e^x E_1(x)`

Verified source: arXiv:2210.06768v2, SHA-256 `e94116441dbfd20784c10d5ebb74087d1e6fbac16050e0736072b0cab012c7d6`, 18 physical pages.

For `x>0`, physical p.6 defines convergents `P_n,Q_n` by the source's continued-fraction coefficients and states the exact remainder relation (3.2). It gives explicit polynomials `Q_{2k}` and `Q_{2k-1}` in (4.2),(4.4). Physical pp.6--7 prove the lower bounds

`Q_{2k}(x) >= (x+1)^floor(sqrt(k))` and `Q_{2k-1}(x) >= x(x+1)^floor((-1+sqrt(1+4k))/2)`,

which, together with positivity of the complete quotients, yield convergence and alternating brackets for `F(x)=e^xE_1(x)`.

At `x=1`, this evaluates the Euler--Gompertz constant `delta`, not Euler's constant. Physical pp.15--16 explain that the naïve integer scaling fails and make irrationality conditional on nonzero constructed errors `delta B_i-A_i`; preserve that condition.
