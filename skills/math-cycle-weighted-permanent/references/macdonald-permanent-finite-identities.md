# Finite identities for the Macdonald cycle-weighted permanent

The Macdonald \((q,t)\)-permanent papers define the cycle weight
\(w_k=(1-t^k)/(1-q^k)\). For a finite matrix, the defining permutation sum supports exact rational evaluation when `q` and `t` are rational and `q**j != 1 for every 1 <= j <= n`.

Paper I gives the immanant decomposition and the relation of its coefficients to the hook-content product on physical pp. 3–6. Paper II, Proposition 2.2 on physical p. 4, gives \(H_n=(t;q)_n/(q;q)_n\), the rank-one identity \(\operatorname{per}_{q,t}(uv^T)=n!H_n\prod_i u_iv_i\), and the block/diagonal identities. The finite evaluator implements only these definitions and finite identities.
