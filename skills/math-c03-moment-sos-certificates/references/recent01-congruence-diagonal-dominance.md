# Congruence-to-diagonal-dominance Gram certificate

For a rational symmetric Gram matrix `Q`, supply a positive rational scale `c`, an integer matrix `A = c Q`, and a square integer matrix `R`. Form \(J=RAR^{\mathsf T}\). If every row satisfies \(J_{ii}>\sum_{j\ne i}|J_{ij}|\), then `J` is positive definite. Writing \(\delta_i=J_{ii}-\sum_{j\ne i}|J_{ij}|>0\), the exact identity

\[
v^{\mathsf T}Jv=\sum_i\delta_i v_i^2+\sum_{i<j:J_{ij}\ne0}|J_{ij}|(v_i+\operatorname{sgn}(J_{ij})v_j)^2
\]

proves this. It also makes `R` invertible, hence `A` and `Q=A/c` are positive definite.

`scripts/check_recent01_congruence_dd.py` checks only these finite integer matrix requirements and emits row margins. It does not reconstruct a polynomial, check a Gram-to-polynomial coefficient identity, find `R`, or establish that an SOS representation proves a requested domain inequality.

Source status: Lemma 4, physical p. 4, Guo, Qiu, Cao, Feng, and Gao, *Exact rational certificates and a Lean formalization of the eleven-variable Vasc inequality*, arXiv:2610.13463v1, local SHA-256 `0f2724a10778fbb1472cd9633914297a841ffe96a290fd8c0892517841c3444a`. The source's full application also relies on six external JSON arrays and Lean replay material; none of that instance data is claimed checked here.
