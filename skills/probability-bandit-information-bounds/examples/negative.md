# Negative example: do not transfer by the word “Bernoulli”

Suppose a theorem assumes \(Y\sim\mathrm{Ber}(\sigma(g(x)))\) and \(g\) is linear/RKHS. This is a logistic-link model. B056 instead assumes \(Y\sim\mathrm{Ber}(f(x))\), where the mean function \(f\) itself lies in an RKHS. They differ in the function constrained by the norm and in how alternatives move probabilities; their confidence sets and KL geometry are not interchangeable.

Likewise, a kernel-UCB theorem with \(Y=f(x)+\epsilon\) for subgaussian \(\epsilon\) proves a valid coarse result for bounded Bernoulli observations after centering, but does not exploit Bernoulli KL or establish a matching structure-dependent logarithmic regret coefficient.

Finally, a fixed-confidence theorem with expected stopping time \(T^*(\mu)\log(1/\delta)\) is not a fixed-budget theorem about \(-\log P(\hat a\ne a^*)/T\). State the objective and limit before comparing complexities.


## Do not assume a GLM score-equation MLE always exists

In W15-022, Eq. (4) states the estimate through an unprojected score equation, while the stated lower derivative bound \(c_\mu\) is defined only on the true-parameter ball \(\|\theta\|_2\le S\). For logistic observations with \(d=1,S=L=1,\theta^*=0\), pull \(x_1=1,x_2=1/2\) once each (so \(E=2>d\) and \(M_3=5/4>0\)). Conditional on those two feature pulls, the valid history \(r_1=r_2=1\) has probability \(1/4\), but its score at any finite candidate \(z\) is
\[
(1-\sigma(z))+\tfrac12(1-\sigma(z/2))
=\frac{e^{z/2}+e^z/2+3/2}{e^{3z/2}+e^{z/2}+e^z+1}>0.
\]
Thus the displayed score equation has no finite root for this history. The exact positive form proves the sign; local Decimal values are in `evidence/W15/logistic_mle_well_definedness_check_results.txt` (earlier archive). Before using the confidence proof, require a well-defined estimate and verify the derivative lower bound along the actual segment from the true parameter to the estimate. This exposes a needed algorithm/proof-scope check; it does not establish that the entire paper's theorems are false.
