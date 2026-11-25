# Negative examples: preserve sampling, model and theorem gates

## Fixed cyclic gap is not a uniform random pair

In the exact ordered full-binary comb with four leaf depths `(1,2,3,3)`, the centered covariance at cyclic gaps `1,2,3` is respectively `−1/16, −9/16, −1/16`; averaging over all 12 distinct ordered pairs gives `−11/48`. Thus a random-pair average does not identify an individual fixed-gap covariance, even in a finite exact tree. The calculation is a sampling-law example, not an asymptotic counterexample to A127. Code and output are saved with the exact cases（本机附件：`evidence/calculations/recursive_cases.py`）.

## Product UI does not supply joint convergence

Let `Z_1=Z`, `Z_2=(-1)^n Z` for a standard normal `Z`. Each marginal is standard normal and
\[
\mathbb E[|Z_1Z_2|\mathbf 1_{|Z_1Z_2|>M}]\leq \mathbb EZ^4/M=3/M,
\]
so the products are uniformly integrable. But their covariance is `(-1)^n`, which has no limit. RT001's admitted product-UI deduction therefore does not prove the missing fixed-gap joint limit or covariance.

## A mean identity does not certify higher factorial moments

RT030's accepted scope is the exact first-moment identity in v2 Eq. 5.3 for a uniform plane tree conditioned on its full legal finite outdegree profile and a uniformly rooted fringe size. R16 confirmed a local literal-prefactor defect in Eq. 5.4. Keep that higher-factorial-moment formula, proposed repairs, downstream Poisson/LLT claims and whole-paper verdict outside the admitted use. This local finding does not label the whole paper erroneous.

## Conditioned-GW toll CLT does not transfer to size-dependent Beta splitting

RT020's conditioned critical-GW CLT requires mean-one finite-variance i.i.d. offspring, admissible sizes, the source's toll-moment and summability conditions, and its conditioning-projection correction. A size-`m` critical Beta-splitting clade has a size-dependent split law; recursive resemblance is not an i.i.d. offspring representation. Prove and verify that representation and all toll gates before transferring RT020.

## Sampled-distance convergence is not a GHP theorem

RT037's admitted criterion concerns iid uniform-vertex sampled distance matrices under its scaling and the separate log-depth/negligible-LCA bridge. It does not establish GHP convergence, a split-tree/CTCS representation, or the ordered leaf pair at prescribed circular gap. Likewise RT035's accepted raw second-moment interface keeps the finite-type activity/A1–A6 and Jordan-L2 gates; it is not a functional Gaussian CLT.
