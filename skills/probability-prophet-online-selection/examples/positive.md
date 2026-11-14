# Positive example: handle an atomic threshold

Suppose values are independent, shown in uniform random order, and the offline comparator is the sum of the top k realized values. For a candidate static threshold t and tie probability p, let `B_i∼Ber(p)` be independent across items and of the values, and compute the effective count `D_{t,p}=Σ_i[1{V_i>t}+1{V_i=t}B_i]`. Its summands have probabilities `q_i=P(V_i>t)+pP(V_i=t)`. When there is no atom at t (or p=0), this reduces to the strict exceedance count. Then calculate separately

- expected utilization `E[min(D_{t,p}/k,1)]`,
- expected effective demand `E[D_{t,p}]`, and
- stockout probability `P(D_{t,p}≥k)`.

These are different functionals. Theorem 2 of M0062 supports a `gamma_k` guarantee when the first equals `gamma_k`. Theorem 3 covers a condition on the second. Its §5.2 conjecture concerns the third. If numerical root-finding chooses p to meet the third target, report only the numerical instance result until a proof of the universal comparison is supplied.
