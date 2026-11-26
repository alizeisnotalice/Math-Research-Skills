# Augmented matching and rank-factorization route

Source: OpenAI, *A proof of Seymour's second-neighborhood conjecture*, SHA-256 \`20be859799f83e3412dba6fd645a72a0d929cbe05ca546807c591f001f9e6e82\`, physical pp. 7-10, Lemma 3.1.

The source augments a bipartite conflict graph with separate left and right copies of \(Z\); a conflicting row/column pair forces a path through the matching covered point.  A vertex cover selects original members to delete.

For the matching bound it defines sparse matrices \(L,N,A,B\) with \(NL=AB\).  Nonvanishing supported minors enforce ranks, including maximum-rank blocks \(D_{p,i}\).  The resulting kernel implication gives independent vectors in \(\ker A\), and Konig's theorem turns the finite matching bound into a cover/pruning statement.

Use only with the stated finite conflict relation, coverage sets, and checked rank minors.

## 固定来源

- 物理页 7, 8, 9, 10。Lemma 3.1 SHA-256 `20be859799f83e3412dba6fd645a72a0d929cbe05ca546807c591f001f9e6e82`。[A proof of Seymour’s second-neighborhood conjecture](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf)
