# Positive example: handle an atomic threshold

Suppose values are independent, shown in uniform random order, and the offline comparator is the sum of the top k realized values. For a candidate static threshold t and tie probability p, let `B_i∼Ber(p)` be independent across items and of the values, and compute the effective count `D_{t,p}=Σ_i[1{V_i>t}+1{V_i=t}B_i]`. Its summands have probabilities `q_i=P(V_i>t)+pP(V_i=t)`. When there is no atom at t (or p=0), this reduces to the strict exceedance count. Then calculate separately

- expected utilization `E[min(D_{t,p}/k,1)]`,
- expected effective demand `E[D_{t,p}]`, and
- stockout probability `P(D_{t,p}≥k)`.

These are different functionals. Under the stated independent-value, uniform-random-order model, the corrected M0062 Theorem 2 gives `gamma_k` when expected utilization equals `gamma_k`; the physical-p.5 literal `k` target is a source typo. For expected demand `k`, retain only the reduced `inf_{m≥k} E AR_k(Bin(m,k/m))` bound, the separately proved `k=1` half guarantee, and the IID `gamma_k` guarantee. The unrestricted all-k closed form is proof-held. Its §5.2 stockout target remains conjectural for `k>1`. Meeting that third target numerically is only a finite numerical observation, not a universal guarantee.
