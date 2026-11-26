# Iid cycle-type likelihood and Hellinger bounds

Source record. *Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra*, author-hosted manuscript, 16 physical pages, SHA-256 `8ab9be29e6190279d6cc7dbfcea2229308fc514afa44aa5b4535dae902844b36`. The adopted calculation is its physical pp. 5–8, Definition 1, Definition 2, Proposition 1 and Corollary 2.

Let `p` and `q` be supplied probability laws on a finite alphabet and let `m` observations be modeled as independent draws from one of their product laws. Put

\[
\rho=\sum_{\lambda}\sqrt{p(\lambda)q(\lambda)}.
\]

For equal prior probabilities, the likelihood-ratio test has error at most \(\rho^m/2\). Every rule using only those observations has error at least

\[
\frac{1-\sqrt{1-\rho^{2m}}}{2}.
\]

The first inequality follows from \(\min(a,b)\leq\sqrt{ab}\). The second uses the total-variation and Hellinger comparison for the product laws. Corollary 2 gives the sufficient condition \(m\geq\log(1/(2\delta))/\log(1/\rho)\) when \(0<\rho<1\) and one wants the upper bound at most \(\delta\).

This is a finite statistical calculation with caller-provided laws. Physical p. 9 of the source explicitly records that a fixed collection of small primes does not supply the iid assumption, and that finite sampled group profiles differ from exact laws. No finite-prime Galois-group certificate or empirical accuracy claim is adopted.

The JSON observation labels determine the number of draws and validate the alphabet. Bayes-error bounds are unconditional under the supplied iid laws and equal priors. They depend on the draw count alone.
